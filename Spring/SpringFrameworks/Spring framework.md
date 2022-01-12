# Spring Framework
Spring framework bases on the principle of IOC(Inversion of control). When using this principle, instead of allowing the app to control the execution, we give control to the Spring framework. We instruct the framework on how to manage the code.

> Use Spring/Spring Boot in a back end service implementation.
> Use Spring/Spring Boot in an automation test app.

## SpringBoot DevTools
* Automatic application restart when code changes
** With DevTools, changes made to Java code and properties files in the project and see those changes applied after a brief moment. DevTools monitors for changes, and when it sees something has changed, it automatically restarts the app. More precisely, then DevTools is in play, the application is loaded into two separate class loaders in the JVM. One class loader is loaded with Java code, property files(These files are likely to change frequently). The other class loader is loaded with dependency libraries, which are not likely to change as often. The downside of this strategy is that changes to dependencies won't be available in automatic restarts. This is because class loader containing the dependency libraries isn't automatically reloaded. This means any time we add, change or remove a dependency in the build specification, we'll need to do a hard restart of the application for those dependencies to take effect. 
* Automatic browser refresh and template cache disable
** By default, template options such as `Thymeleaf` and `FreeMarker` are configured to cache the results of template parsing so that templates don't need to be prepared with every request they serve(This is a good feature in production, but not in dev). Cached templates make it impossible to make changes to the templates while the application is running and see the results after refreshing the browser. Even if we've made changes, the cached template will still be in use until the application is restarted.
* Built-in H2 console
** Dev tools will automatically enable H2 console that we can access. 