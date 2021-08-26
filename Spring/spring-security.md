## Spring Security

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

#### Set our specified route under protection and set public routes available to everyone.
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
                .antMatchers("/test").permitAll()  // /test endpoint are now public
                .antMatchers("/greeting").authenticated(); // greeting requires authentication
    }
```
By testing these two endpoints, we can see different results.
```PowerShell
>curl http://localhost:8081/test
>curl http://localhost:8081/greeting
```

### Getting started with self-implemented security mechanism with Spring Security