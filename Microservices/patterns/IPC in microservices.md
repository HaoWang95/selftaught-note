## Interaction styles
* The first dimension is whether the interaction is one-to-one or one-to-many
  * One-to-one, each client request is processed by exactly one service
  * One-to-many, each request is processed by multiple services
* The second dimensions is whether the interaction is synchronous or asynchronous
  * Synchronous, the client expects a timely response from the service and might even block while it waits.
  * Asynchronous, the client doesn't block, and the response, if any, isn't necessarily sent immediately.

### One-to-one interactions
* Request/Response, an interaction style that generally results in services being tightly coupled.
* Asynchronous request/response, the client doesn't block while waiting, because the service might not send the response for a long time.
* One-way notifications, a service client sends a request to a service, but no reply is expected.

### One-to-many interactions
* Publish/subscribe, a client publishes a notification message, which is consumed by 0 or more interested services.
* Publish/async responses, a client publishes a request message and then waits for a certain amount of time for responses from interested services.

## Semantic versioning
Given a version number MAJOR.MINOR.PATCH, increment the:

* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards compatible manner, and
* PATCH version when you make backwards compatible bug fixes.

## Handling partial failure using the **circuit breaker pattern**
Using **Hystrix** or **Resilience4j**.

## Using service discovery
Service discovery is conceptually simple, its key component is a service registry, which is a database of the network locations of an application's services instances.
### Applying application level service discovery patterns
* Self-registration pattern, a service invokes the service registry's registration API to register its network location
* Client-discovery pattern, when a client wants to invoke a service, it queries the service registry to obtain a list of the services's instances.
>- Eureka is a highly available service registry.
>- One benefit of application-level service discovery is that it handles the scenario when services are deployed on multiple deployment platforms. Imagine, for example, you’ve deployed only some of services on Kubernetes, and the rest is running in a legacy environment. Application-level service discovery using Eureka, for example, works across both environments, whereas Kubernetes-based service discovery only works within Kubernetes.
>- One drawback of application-level service discovery is that a service discovery library for every language(framework) is needed. Spring cloud only helps Spring developers while Node.js or GoLang require other service discovery framework. Another drawback of application-level service discovery is that developers are responsible to set up and manage the service registry, which is a distraction and can be a configuration issue. It's a better option to use a service discovery mechanism that's provided by the deployment infrastructure.
### Applying the platform-provided service discovery patterns
Docker and Kubernetes have a built-in service discovery registry and service discovery mechanism. The deployment platform gives each services a DNS name, a virtual IP address, and a DNS name that resolves to the VIP address. A service client makes a request to the DNS name/VIP, and the deployment platform automatically routes the request to one of the available service instances. Therefore, service registration, service discovery, and request routing are entirely handled by the deployment platform.
* 3rd party registration pattern, instead of a service registering itself with the service registry, a third party called registrar, which is typically part of the deployment platform, handles the registration.
* Service-side discovery pattern, instead of a client querying the service registry, it makes a request to a DNS name, which resolves to a request router that queries the service registry and load balances requests.

## Communicating using asyn messaging pattern
### Channels
* P2P
* Publish-subscribe
A message-based application typically uses a message-broker, an infrastructure service through which the service communicates.
