## Spring Cloud Config
A separated config server can be implemented with spring cloud config dependencies.
The main purpose of using a spring cloud config is to separate configuration settings from all running instances of microservices. For each microservices(it can be 10 or 1000 instances of microservices), the configuration information for these services can be managed in a single config service instance and be loaded/refreshed at run time.

Except from Spring Cloud Configuration Server, other tools can also be used to build a configuration management solution. 

> - Zookeeper, pretty complex to use
> - Consul, doesn't offer client dynamic refresh out of the box. Native service discovery support.
> - etcd, distributable, fast and scalable, easy to use and set up.
> - Eureka, from Netflix, Used for both service discovery and key-value management

### Get started with spring cloud configuration server
Spring cloud configuration server is a REST-based app that is built on top of Spring Boot. Building a Spring Cloud Configuration Server app follows the same routine as building a getting-started, hello-world Spring Boot app.
> - Include Spring Cloud projects dependency, spring cloud config server 
> - Update the dependency management
> - Include the maven plugin that supports mvn spring-boot:build-image


### Common issues and confusions
Some of the official documentation and many tutorials use application.properties, application.yml, bootstrap.properties and bootstrap.yml for Spring Cloud and Spring Boot apps without mentioning why use one of them and how to tell the differences between them.

***For application.yml or application.properties***
application.yml/application.properties file is specific to Spring Boot applications. Spring Boot will always load application.yml from this location -> **/src/main/resources/application.yml**. Unless we changed it to our customized location.

***For bootstrap.yml or bootstrap.properties***
They are only used if we are using Spring Cloud and our application's configuration is stored on a remote configuration server. (In our case, the bootstrap.yml or bootstrap.properties should be applied in our client microservices apps)
Also, bootstrap file is loaded before the application.yml/application.properties.
Typically, it should contain two properties:

> - Location of the configuration server. spring.cloud.config.uri
> - Name of the application. spring.application.name