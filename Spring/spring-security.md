## Spring Security
Spring Security contains huge lists of implementation details, it is also a key point to combine Spring Boot with Spring Security to build Java applications.

### Get started with Spring Security
#### A starter case
A simple and easy starter to use Spring Securty is to include the Spring Security dependency in the pom.xml

```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

(Do not include any jpa dependency for now, because it requires datasource configuration, but feel free to include actuator.)

Then define a simple rest endpoint, by starting the application and calling the endpoint, we will have the basic authentication provided by Spring Security. No other annotations or configurations are required for this most basic use case. The password will be generated at the starting console and the default username is user.
```java
@RestController
public class TestEndpoint {
    @GetMapping("/test")
    public String testIndex(){
        return "Test endpoint";
    }
}
```
The Rest endpoint above will be protected by basic authentication.

#### What happened in the starter case
The dependency included in the pom.xml will enable the basic authentication for our Spring Boot application.

When the application is started, (I set the server port to 8081)
```PowerShell
curl http://localhost:8081/test
```
By calling the api without any basic authentication data provided, we will get the 401 Unauthorized response.
```json
{"timestamp":"2021-08-26T03:42:47.695+00:00","status":401,"error":"Unauthorized","path":"/"}
```
If we call the api using basic user authentication:
```PowerShell
curl user:your_generated_password http://localhost:8081/test
```
We will see the responsed text.
```text
Test endpoint
```

#### Next, let's override the default configuration provided by Spring Security
**A very important concept in Spring Security is UserDetailServices**,  
For experimental purposes, we can use InMemoryUserDetailsManager to implement the user and its credential. 
```java
@Configuration
public class AuthConfig {
    // override the default spring security setting
    @Bean
    public UserDetailsService userDetailService(){
        // We use the InMemoryUserDetailManager to simulate the process
        InMemoryUserDetailsManager userDetailService = new InMemoryUserDetailsManager();
        // Create a user profile
        UserDetails user = User.withUsername("alan").password("alanpassword123456").authorities("read").build(); // Do not forget the autorities
        userDetailService.createUser(user);
        return userDetailService;
    }
    
    @Bean
    public PasswordEncoder passwordEncoder(){
        // The NoOpPasswordEncoder processes passwords as plaintext.
        // The reason to treat passwords as plaintext is because in UserDetailService(), the created password is plaintext
        return NoOpPasswordEncoder.getInstance();
    }
}
```
After implementing this feature, test the application again.
```PowerShell
>curl -u alan:alanpassword123456  http://localhost:8081/test
```


#### Endpoint authorization configuration
By implementing the Sprint Security mechanism above, we can treat all endpoints equally important, that all endpoints assume we have a valid user managed by the application. Also, based on the basic Http authentication, we can override the previous setting easily. 

Basic Authentication does not fit into our scenarios. And not all endpoints need to be secured, that means we need to choose authorization roles. By extending the **WebSecurityConfigurerAdapter** class and overriding the **configure** method, we can build a different scenario.

(Delete previously tested code because we are going to do something more complex)

For now, let's set all endpoints to be accessible. Permit all requests.
```Java
@Configuration
public class AuthConfig extends WebSecurityConfigurerAdapter {
    // override the configure method.
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.httpBasic();
        http.authorizeRequests().anyRequest().permitAll();
    }
}
```
Then run the app the test the endpoint: we should notice that the authentication has been disabled.
```PowerShell
>curl http://localhost:8081/test
```

Now, let's set all endpoints to be accessible. All requests needs to be authenticated. By implementing this, we are actually changing the application to the initial starter stage.
```java
@Configuration
public class AuthConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.httpBasic();
        http.authorizeRequests().anyRequest().authenticated();
    }
}
```
Test this change using the starter approach:
```PowerShell
>curl user:generated_password http://localhost:8081/test
```

#### Set our specified routes under protection and set public routes available to everyone.
Now we set our test endpoint being public to everyone, and create a new endpoint called greeting and set it to be authenticated.
Create a new endpoint greeting.
```Java
@RestController
public class TestEndpoint {
    @GetMapping("/test")
    public String testIndex(){
        return "Test endpoint";
    }

    @GetMapping("/greeting")
    public String greeting(){
        return "Hello everyone";
    }
}
```

Set the **/test** to be public and secure the **/greeting**
```java
@Override
    protected void configure(HttpSecurity http) throws Exception {
        http.httpBasic();
        http.authorizeRequests()
                .antMatchers("/test").permitAll()  // /test endpoint is now public
                .antMatchers("/greeting").authenticated(); // greeting requires authentication
    }
```
By testing these two endpoints, we can see different results.
```PowerShell
>curl http://localhost:8081/test
>curl http://localhost:8081/greeting
```

### Spring Security general concepts
> - WebSecurityConfigureAdapter, this is our of the core parts of normal Spring Security implementation. It provides 3 different configure methods we can override.
> - UserDetailService, this is an interface that has a method to load User by username and returns a UserDetails object that Spring Security can use for authentication and validation.
> - UserDetails is the object returned from UserDetailService lookup, it contains username, password, authorities and other information to build an Authentication object
> - SecurityContext, 

### Workflow to implement a JWT mechanism
In general, we will need
> - Authentication controller, to handle login/register requests
> - Functional or testing controller, that enable us to test public, private and accessing protected resources based on authorized roles.

To clarify the ideas, we divide the problem of designing the JWT mechanism with Spring Security using bottom-up approach: 
- > The general models can be divided into 2 classes, one is User, another is Role.
- > The models can extend JpaRepository
- > Controllers to respond http requests, one is AuthController, another one is general endpoint controller.
- > JWT validation, generation mechanism implementation from Spring Security

* Models
    * User model, includes id, username, email, password, roles
    * Role model, name

* Repositories
    * UserRepository that extends JpaRepository<User, Long>
    * RoleRepository that extends JpaRepository<Role, Long>
**Optional**: with repositories in mind, we can choose to implement service layer( UserService, RoleService) or use the repository in the controller directly.
* Controllers
    * AuthController: receives and processes the login/register requests
    * Testing/Functional Controller: expose resources(We can keep using the two endpoints above for demo)
* Security implementation
    * SecurityConfig which extends the WebSecurityConfigurerAdapter, we've done this in previous section. The name was AuthConfig
    * UserDetailServiceImpl which should implement the UserDetailService interface(Spring Security core concept)
    * UserDetailImpl which should implement the UserDetail interface(Spring Security core concept)
    * JwtAuthenticationEntry which implements the AuthenticationEntryPoint
    * JwtTokenFilter which extends the OncePerRequestFilter(This is to validate the request for each time our app receives a http request)
    * JwtUtils provides static methods to generate, and validate JWT
-----------------------------------------------------------------------------