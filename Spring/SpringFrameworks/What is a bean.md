# @Bean
@Bean is a method level annotation and a direct analog of the XML <bean /> element. @Bean annotation instructs Spring to add the instance returned by the method to the Spring Context.

```java
@Configuration
public class AppConfig{
    @Bean
    CommandLineRunner runner(){
        //
    }
}
```

# @Component
