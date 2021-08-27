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
#### **The design and thinking of how to implement JWT**
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

### Setting up dependencies for the project
We have spring boot starter security dependency already resolved at the start of the doc.
```XML
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
Now we need Jpa, database, and jwt dependencies.
```XML
<!-- Dependency for JWT, quite popular in Maven central, we'll use this dependency	-->
<!-- https://mvnrepository.com/artifact/io.jsonwebtoken/jjwt -->
<dependency>
	<groupId>io.jsonwebtoken</groupId>
	<artifactId>jjwt</artifactId>
	<version>0.9.1</version>
</dependency>

<!-- Dependency for Jpa -->
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- Dependency for h2 -->
<dependency>
	<groupId>com.h2database</groupId>
	<artifactId>h2</artifactId>
	<scope>runtime</scope>
</dependency>

<!-- Dependency for mysql	-->
<dependency>
	<groupId>mysql</groupId>
	<artifactId>mysql-connector-java</artifactId>
	<scope>runtime</scope>
</dependency>
```
The corresponding settings in application.properties
```
# For h2 
spring.datasource.url=jdbc:h2:mem:test
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=user
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true

# For mysql
# connect to a test db called myservice
spring.datasource.url=jdbc:mysql://localhost:3306/myservice?useSSL=false
spring.datasource.username= root
spring.datasource.password= root
spring.jpa.database-platform=org.hibernate.dialect.MariaDB10Dialect
# create create-drop update validate, we choose default update
spring.jpa.hibernate.ddl-auto=update
```
With application properties defined, we implement the basic entities. 
**Note: in our User entity, we choose to use username instead of userName. The reason to do this is to be consistent with definitions in UserDetails and User of Spring Security.**
```Java
// RoleType definition
public enum RoleType {
    ROLE_USER,
    ROLE_ADMIN
}

// Role definition
@Entity
@Table(name = "roles")
public class Role {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Enumerated(EnumType.STRING)
    @Column(name = "roletype")
    private RoleType roleType;

    public Role(RoleType roleType) {
        this.roleType = roleType;
    }

    public Role(){}

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public RoleType getRoleType() {
        return roleType;
    }

    public void setRoleType(RoleType roleType) {
        this.roleType = roleType;
    }
}


// User definition

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username", nullable = false)
    private String username;

    @Column(name = "email",nullable = false)
    @Email
    private String email;

    @Column(name = "password", nullable = false)
    private String password;

    @ManyToMany
    @JoinTable(name = "user_roles", joinColumns = @JoinColumn(name="user_id"), inverseJoinColumns = @JoinColumn(name = "role_id"))
    private Set<Role> roles = new HashSet<>();

    public User(){}

    public User(String username, String email, String password){
        this.username = username;
        this.email = email;
        this.password = password;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Set<Role> getRoles() {
        return roles;
    }

    public void setRoles(Set<Role> roles) {
        this.roles = roles;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}
```
With the entity class defined, we can easily have the repositories
```Java
// Role repository
@Repository
public interface RoleRepository extends JpaRepository<Role, Long> {
    Optional<Role> findByRoleType(RoleType type);
}

// User repository
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByUserName(String userName);

    Boolean existsByUserName(String userName);

    Boolean existsByEmail(String email);
}

```

#### **Security related services**
Now with basic code generated, we need to have our UserDetails class implementation to represent the UserDetails in Spring Security. Then we need to briefly implement a UserDetailServiceImpl which should ovrride the loadUserByUsernme method. If we are confused why we are doing this, please refer to the source implementation of User and UserDetails.

By default, Spring Security provides us a very handy implementation which can represent the user instance, this class is User, below is the implementation of the User class in Spring Security. What we are going to implement is quite similiar with this User class.
```Java
public class User implements UserDetails, CredentialsContainer {
    private static final long serialVersionUID = 550L;
    private static final Log logger = LogFactory.getLog(User.class);
    private String password;
    private final String username;
    private final Set<GrantedAuthority> authorities;
    private final boolean accountNonExpired;
    private final boolean accountNonLocked;
    private final boolean credentialsNonExpired;
    private final boolean enabled;
  // More code omitted here
}
```
Our implementation, just contain the necessary fields.
```Java
public class UserDetailsImpl implements UserDetails {
    private static final long serialVersionUID = 1L; // Keep it the same value with User in Spring Security
    private Long id;
    private String username;
    private String email;
    @JsonIgnore
    private String password;
    private Collection<? extends GrantedAuthority> authorities;

    public UserDetailsImpl(Long id, String username, String email, String password, Collection<? extends GrantedAuthority> authorities){
        this.id = id;
        this.username = username;
        this.email = email;
        this.password = password;
        this.authorities = authorities;
    }
    
    public static UserDetailsImpl build(User user){
        List<GrantedAuthority> authorities = 
                user.getRoles()
                .stream()
                .map(role -> new SimpleGrantedAuthority(role.getRoleType().name()))
                .collect(Collectors.toList());
        return new UserDetailsImpl(user.getId(), user.getUsername(), user.getEmail(), user.getPassword(), authorities);
    }
    
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return authorities;
    }

    @Override
    public String getPassword() {
        return password;
    }

    @Override
    public String getUsername() {
        return username;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj){
            return true;
        }
        if(obj == null || getClass() != obj.getClass()){
            return false;
        }
        UserDetailsImpl userDetails = (UserDetailsImpl) obj;
        return Objects.equals(id, userDetails.id);
    }
}
```

Next, we implement the UserDetailsService that loads the user information by username.
```Java
@Service
public class UserDetailsServiceImpl implements UserDetailsService {
    @Autowired
    UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository
                .findByUsername(username)
                // In UserRepository, we used Optional<User>, needs to check if it is null
                .orElseThrow(() -> new UsernameNotFoundException("User data not found"));
        // By using the static UserDetailsImpl.build(userInstance), build a UserDetails instance
        return UserDetailsImpl.build(user);
    }
}
```
Now, we have the basic loaders prepared.
In the application.properties, include the jwt secret value and a expiration value:
```
# Then we can use them to generate and validate jwt tokens
app.jwtSecret=jwtSecret
app.jwtExpirations=36000000
```
A simple jwt util class that generates, and validate tokens.
```Java
public class JwtUtils {
    private static final Logger log = LoggerFactory.getLogger(JwtUtils.class);

    @Value("${app.jwtSecret}")
    private String jwtSecret;

    @Value("${app.jwtExpirations}")
    private int jwtExpirations;

    // Generate a token
    public String generateJwt(Authentication authentication){
        UserDetailsImpl userDetails = (UserDetailsImpl) authentication.getPrincipal();
        return Jwts.builder()
                .setSubject((userDetails.getUsername()))
                .setExpiration(new Date(new Date().getTime() + jwtExpirations))
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS512, jwtSecret)
                .compact();
    }

    public String getUserNameFromJwt(String jwtToken){
        return Jwts.parser()
                .setSigningKey(jwtSecret)
                .parseClaimsJws(jwtToken)
                .getBody()
                .getSubject();
    }

    public boolean validateJwt(String authToken){
        try {
            Jwts.parser().setSigningKey(jwtSecret).parseClaimsJws(authToken);
            return true;
        }catch (Exception e){
            log.error("Jwt validation exception: {}", e.getMessage());
        }
        return false;
    }
}
```

