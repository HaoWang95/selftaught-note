## Service Registration and Service Discovery

After setting the configuration server that externalizes microservices configurations, the next step is to implement the service registration and service discovery layer.

Here are what the service registration and service discovery layer provides:
> - Service Registration
> - Service Discovery
> - Information Sharing
> - Health Monitoring
> - Cloud side load-balancing(There is a difference between this load-balancing with aws ec2 load-balancing)

### Spring Cloud makes Service Registration & discovery quite easy, we need to know how to use the following Spring Cloud components

> - Spring Cloud Netflix's Eureka service, which works as a service discovery agent.
> - Spring Cloud Load Balancer, which works as a cient-side load-balancing support.
> - Netflix Feign client to look up for a service.

Note: There are many other alternatives supported by Spring Cloud to perform the service discovery and service registration tasks. Like the famous **Apache ZooKeeper, etcd and Consul**.

If we are going to use spring cloud load balancer, exclude spring-cloud-starter-ribbon dependency from eureka server dependency.


