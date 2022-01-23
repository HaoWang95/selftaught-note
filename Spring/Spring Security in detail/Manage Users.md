## UserDetails, UserDetailsService, UserDetailsServiceManager
> UserDetails Interface.
> Use UserDetailService in the authentication flow.   
> Creating a custom implementation of UserDetailsService.
> Creating a custom implementation of UserDetailsManager.
> Using the JdbcUserDetailManager in the authentication flow.

* UserDetails, which describes the user for Spring Security.
* GrantedAuthority, which allows us to define actions that user can execute.
* UserDetailsManager, which extends the UserDetailsService contract. Beyond the inherited behavior, it also describes actions like creating a user and modifying or deleting a user's password.

1. The request is intercepted by the authentication filter
2. Authentication responsibility is delegated to the authentication manager
3. The authentication manager users the authentication provider which implements the authentication logic.
4. The authentication provider finds the user with a user details service and validates the password using a password encoder.
5. The result of the authentication is returned to the filter
6. Details about the authenticated context are stored in security context

The UserDetailsService is only responsible for retrieving the user by username. This action is the only one needed by the framework to complete the authentication. The UserDetailsManager adds behavior that refers to adding, modifying or deleting the user, which is a required functionality in most applications.(The separation between the two contracts is an excellent example of the interface segregation principle. For example, if your app only needs to authenticate the users, then implementing the UserDetailsService contract is enough to cover the desired functionality.)
```Java
public interface UserDetails extends Serializable {
    String getUsername(); // we can retrieve the username
    String getPassword(); // we can retrive the password
    Collection<? extends GrantedAuthority> getAuthorities(); // we can get the authorities the user have
    boolean isAccountNonExpired(); // Fm, we can let the account expire
    boolean isAccountNonLocked(); // we can let the account locked
    boolean isEnabled(); // we can enable/disable the account
    boolean isCredentialsNonExpired(); // we can expire the credentials
}
```
To describe the authorities in Spring Security, we use the GrantedAuthority interface
```Java
public interface GrantedAuthority extends Serializable {
    String getAuthority();
}
```
**We should define our own User class with POJO Java, and decorates the User class with by implementing a CustomSecurityUser class which implements UserDetails.** 
For **`UserDetailsService`** interface, it only has one method defined.
```Java
public interface UserDetailsService{
    UserDetails loadUserByUsername(String username) throws UsernameNotFoundException;
    // UsernameNotFoundException is a `RuntimeException`. The UsernameNotFoundException inherits directly from the type AuthenticationException, which is the parent of all the exceptions related to the process of authentication. AuthenticationException inherits further the RuntimeException class
}
// With our own POJO User class and UserRepository, we just need to implement a CustomSecurityUserDetailsService class, by overriding the loadUserByUsername that uses `UserRepository` to find a User instance, then decorates the User instance as a UserDetails instance. 
```
We might implement the UserDetailsService to load the user from a database, an external system, a vault and so on.
Also, **`UsernameNotFoundException` is a `RuntimeException`**. Because `UsernameNotFoundException` inherits from `AuthenticationException`, and `AuthenticationException` inherits `RuntimeException`.
One of the most basic and important note about Spring Security here, is to **know how to implement my `UserDetailsService` properly.**

The **`UserDetailsManager`** interface extends and adds more methods to the UserDetailsService contract.
```Java
public interface UserDetailsManager extends UserDetailsService{
    void createUser(UserDetails user);
    void updateUser(UserDetails user);
    void deleteUser(String username);
    void changePassword(String oldPassword, String newPassword);
    boolean userExists(String username);
}
```

## Authentication
The **`AuthenticationProvider`** layer is responsible for the logic of authentication. The AuthenticationProvider is where we find the conditions and instructions that decide whether to authenticate a request or not. **The component that delegates this responsibility to the AuthenticationProvider is the AuthenticationManager, which receives the request from the HTTP filter layer.**
>- Implementing authentication logic using a custom AuthenticationProvider
>- Using the HTTP Basic and form-based login authentication methods
>- Understanding and managing the SecurityContext component

* If the request is authenticated, the details of the request are stored in SecurityContext.
* If the request is not authenticated, the application rejects the request without delegating to the authorization process.
  
In Spring Security, **use the AuthenticationProvider contract to define any custom authentication logic**. **`AuthenticationProvider`** will take care of the authentication logic. The detail implementation of the AuthenticationProvider interface delegates the responsibility of finding the system's user to a `UserDetailsService`.

### Representing the request during authentication
```Java
public interface Authentication extends Principal, Serializable{
    Collection<? extends GrantedAuthority> getAuthorities();
    Object getCredentials();
    Object getDetails();
    Object getPrincipal();
    boolean isAuthenticated(); // return true if the authentication process ends or false if the authentication process is still in progress
    void setAuthenticated(boolean isAuthenticated) throws IllegalArgumentException
}

public interface AuthenticationProvider {
    Authentication authenticate(Authentication authentication) throws AuthenticationException;

    boolean supports(Class<?> authentication);
}
```
1. Declare a class that implements the `AuthenticationProvider` contract.
2. Decide which kinds of Authentication objects the new AuthenticationProvider supports.
   1. Override the `supports(Class<?> authentication);` method to specify which type of authentication is supported by the AuthenticationProvider that we define.
   2. Override the `Authentication authenticate(Authentication authentication) throws AuthenticationException;` method to implement the authentication logic.
3. Register a new instance of the new AuthenticationProvider implementation with Spring Security.
```Java
// Please note using @Bean can also configure a CustomAuthenticationProvider
@Component
public class CustomAuthenticationProvider implements AuthenticationProvider {

    @Autowired
    private UserDetailsService userDetailsService; // UserDetailsService will loadUserByUsername

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Override
    public Authentication authenticate(Authentication authentication){
        String username = authentication.getName();
        String password = authentication.getCredentials().toString();
        UserDetails userDetails = UserDetailsService.loadUserByUsername(username);

        if(passwordEncoder.matches(password, userDetails.getPasswrod())){
            return new UsernamePasswordAuthenticationToken(username, password, userDetails.getAuthorities());
        }else{
            throw new BadCredentialsException("");
        }
    }

    @Override
    public boolean supports(Class<?> authenticationType){
        return authenticationType.equals(UsernamePasswordAuthenticationToken.class);
    }
}

```

## Build a sample app that implements Basic Spring Security
* Define a User entity class that represents the user profile.
* Decorates the User entity with a customed UserDetails class which implements the UserDetails interface.
* Use Spring Data JPA to implement UserRepository that performs CRUD operations with User entity.
* Create customed UserDetailsService and override loadByUsername that use UserRepository to find user data in db and decorates to a UserDetails
* In Spring security configuration class, define the following beans.
  * PasswordEncoder bean that returns an instance of PasswordEncoder(There can be one or more beans to return PasswordEncoder).
  * UserDetailsService bean that returns the instance of the customed UserDetailsService.
  * AuthenticationProvider bean that will have the authentication logic.(Or use DaoAuthenticationProvider).
  * Override the configure methods, to set up AuthenticationManagerBuilder which will take the AuthenticationProvider bean and HttpSecurity configurations to set up basic authentication rules.

## Authorization
To choose the requests to which to apply authorization configuration, use HttpSecurity matchers.
* MVC matchers, use MVC expressions for path matching.
* Ant matchers, use Ant expression for path matching.
* regex matchers, use regex for path matching.

> Prefer MVC matchers. We can avoid some of the risks involved with the way Spring maps paths to actions.


## Understand and customize filters
In Spring Security, HTTP filters manage each responsibility that must be applied to the request. The filters form a chain of responsibilities. A filter receives a request, executes its logic, and eventually delegates the request to the next filter in the chain.
* Filters are HTTP filters, so by implementing the **`Filter` interface** from `javax.servlet`. As for other HTTP filter, you need to override the **doFilter()** method to implement the logic.
* ServletRequest, which is the HTTP request.
* ServletResponse, which is the HTTP response.
* FilterChain, the chain of filters. The filter chain is a collection of filters.
  
Spring Security provides some filter implementations.
* **BasicAuthenticationFilter**, http basic authentication.
* **CsrfFilter**, cross-site request forgery(CSRF) protection.
* **CorsFilter**, cross-origin resources sharing authorization rules.

## CSRF protection and CORS
**CSRF - Cross-site request forgery** is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform.
CSRF is enabled by default in Spring Security. CSRF attacks assume that a user is logged into a web application. They're tricked by the attacker into opening a page that contains scripts that execute actions in the same application the user was working on. Because the user was logged in, the forgery code can now impersonate the user and perform actions on their behalf. So the CSRF protections is to ensure only the frontend of web applications can perform mutation operations.

* Basic theory for CSRF protection
  * Before being able to do any action that could change data, a user must send a request using HTTP GET to see the web page. When this happens, the application generates a unique token. The application now accepts only requests for mutating operations that contain the unique value in the header, which is knowing the value of the token is proof that it is the app itself making the mutation request and not another system. Any page containing mutation calls(POST, PUT, DELETE) should receive through response the CSRF token, and the page must use the token to make mutation calls.
  * The starting point of CSRF protection is a filter in the filter chain called **CsrfFilter**. The **CsrfFilter** uses a component called **CsrfTokenRepository** to manage the CSRF token values that generate new tokens, store tokens, and eventually invalidate these. **CsrfTokenRepository** stores the token on the HTTP session and generates the tokens as random universially unique identifiers.

**CORS** The CORS mechanism works based on HTTP headers.
* **Access-Control-Allow-Origin**, which foreign domains/origins can access resources in our service.
* **Access-Control-Allow-Methods**, allowed Http methods
* **Access-Control-Allow-Headers**, adds limitations to which headers you can use in a specific request.


## A more practical example
* The client calls the login endpoint with credentials(Normally username/email and password)
* The business logic server calls the /user/auth endpoint of the authentication server to authenticate the user and send them an OTP.
* The authentication server reaches the user in its database and authenticates user
* If the user is authenticated, the authentication server sends an OTP to the user through SMS.
* The client sends the OTP together with their username for the second authentication
* The business logic server calls the authentication server to validate the OTP.
* If the OPT is valid, the business logic server issues a token back to the client. The client uses this token to call any endpoint of the business logic server.

### Understanding and using tokens
Token is like an access card. A token is usually sent through an HTTP header by clients and tokens are often used in authentication and authorization architectures. Token provided a method that an application uses to prove it has authenticated a user, which allows the user to access the application's resources. One of the most widely used example is **`JWT`**.
