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
* Token helps aviod sharing credentials in all requests.
* Define tokens with a short lifetime.
* Invalidate tokens without invalidating credentials.
* Tokens can also store details like user authorities that client needs to send in the request(This is for an easier implementation of token-based authorization).
* Helps to delegate the authentication responsibility to another component in the system.


## OAUTH 2 authentication architecture
* All applications owneed by the organization use the authorization server to authenticate users.
* The authorization server keeps users' credentials.
This will eliminate the duplication of credentials representing the same individual.
OAuth 2 components:
* The resource server which hosts resources like user data or their authorized actions(roles)
* The resource owner

### Know how tokens are created for different grants.
* **`Authorization code`**
  * Make the authentication request
    * User doesn't send the credentials to the client app, the user interacts directly with the authorization server.
    >- The client redirects the user to an endpoint of the authorization server where they need to authenticate. Say we are using app A, and we want to access some protected resource that requires us to authenticate. The app opens a page for us with a login form on the authorization server that we must fill with our credentials.
    >- The client redirects the user to the authorization server, the clients calls the authorization endpoint with the following details provided
    1. **`response_type`**: with value code. This value tells the authorization server that the client expects a code. The client needs the code to obtain an access token.
    2. **`client_id`**, the client_id identifies the client application.
    3. **`redirect_uri`**, this value tells the authorization server where to redirect the user after successful authentication. The auth server might already know a default redirect URI for each client(Registered client app in auth server).
    4. **`scope`**, granted authorities.
    5. **`state`**, this is important as it defines a *CSRF* token used for the **CSRF protection**.
    >- After being authenticated successfully on the auth server, the authorization server calls back the client on the redirect URI and privdes **a code and the state value**. The client checks the state value is the same as the one it sent in the request to confirm that it was not someone else attempting to call the redirect URI. The client uses the code to obtain an access token.
  * Obtain an access token
    * The code from the **step:** *Make the authentication request* is the client'f proof that the user is authenticated. Now the client calls the auth server with the code to get the token. For last step, the interaction was between the user and the auth server. In this step, the interaction is between the client and the authorization server.
    * Why two steps? One step for the code and one more step for the token?
    >- The auth server generates the first code as proof that the user directly interacted with it. The client receives this code and has to authenticate again using it and its credentials to obtain an access token.
    >- Then the client uses the second token to access resources on the resource server.
    >- **The simple fact is the auth server would call the redirect URI directly with an access token without making sure that it was indeed the right client receiving that token makes the flow less secure. By sending the authorization code first, the client has to prove again who they are by using their credentials to obtain an access token.**  

  * Call the protected resource
* **`Password`**
  * The password grant type assumes the user shares their credentials with the client. The client uses these to obtain a token from the authorization server. It then accesses the resources from the resource server on behalf of the user. **We use this authentication flow only if the client and the authorzation server are built and maintained by the same org.**
  * Requesting an access token using the password grant type
    * **`grant_type`** with value password
    * **`client_id`** and **`client_secret`**, which are the credentials used by the client to authenticate itself.
    * **`scope`**, granted authorities.
    * **`username`** and **`password`**, which are the user credentials.(Plain text values in the request header)
  * Using an access token to call resources.
    * Consider using the `authorization code grant type` because the the `password grant type` is authorized using shared user credentials from the client app to the server.
* **`Refresh token`**
  * The client has an access token that expired. To avoid forcing the user to log in again, the client uses a refresh token to issue a new access token.
* **`Client credentials`**
  * This is the simplest of grant type. A general use-case senario is *when no users is involved* which is to implement authentication between two applications.

### A basic example of OAuth2
```Java
@Configuration
public class OAuthConfig extends WebSecurityConfigurerAdapter{

     private ClientRegistration clientRegistration(){
        return CommonOAuth2Provider.GITHUB
                .getBuilder("github")
                .clientId("registed github client id")
                .clientSecret("generated client secret")
                .build();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception{
        http.oauthLogin();
        http.authorizeRequests()
            .anyRequest()
                .authenticated();
    }
}
```
>- When we add the **`http.oauthLogin();`**, it simply adds a new authentication filter(**Oauth2LoginAuthenticationLoginFilter**) to the filter chain. The Oauth2LoginAuthenticationFilter will intercept requests and apply OAuth 2 authentication logic.
* ClientRegistration contract in Spring security.
  * Client Id and client secret
  * Grant type used for authentication
  * Redirect URI
  * Scopes

* Implement the *`ClientRegistrationRepository`*
  * The **`ClientRegistrationRepository`** interface is similar to the UserDetailsService interface. A ClientRegistrationRepository object finds the ClientRegistration by its registration ID.
  * Spring Security offers an implementation for ClientRegistrationRepository, which is **`InMemoryClientRegistrationRepository`**

```Java
@Configuration
public class OAuth2Config extends WebSecurityConfigurerAdapter {

    @Bean
    public ClientRegistrationRepository clientRegistrationRepository(){
        var client = clientRegistration();
        return new InMemoryClientRegistrationRepository(client);
    }

    private ClientRegistration clientRegistration(){
        return CommonOAuth2Provider.GITHUB
                .getBuilder("github")
                .clientId("client id")
                .clientSecret("client secret")
                .build();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.oauth2Login(c -> {
            c.clientRegistrationRepository(clientRegistrationRepository());
        });
        http.authorizeRequests().anyRequest().authenticated();
    }
}
```

## Implement an authentication server using OAuth2
**The role of the authorization server is to authenticate user and provide token to the client.** The authorization server can identify the user. It provides an access token to the client. The client uses the access token to call resources exposed by the resource server.

