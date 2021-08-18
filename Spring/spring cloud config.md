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

