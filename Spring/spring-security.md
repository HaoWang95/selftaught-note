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


