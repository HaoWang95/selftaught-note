# @Bean
@Bean is a method level annotation and a direct analog of the XML <bean /> element. 

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
