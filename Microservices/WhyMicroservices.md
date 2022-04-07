# Monolith
* Single integrated application
* Backend service

Adding features increases:
* Size
* Complexity
* Effort of next change
  
# Microservice
Microservices are small, are independent, no inducing downtime in other services.
* Technology-independent.

## Human advantages of microservices
Efficiently managing large teams and large applications
For individual developers
* Narrowed scope of responsibilty
* Mitigate and eliminate bottlenecks
* Onbard new developers faster
* Easy to find expertise

For teams
* Isolated decision making
  * No pressure for one-size-fits-all
  * Isolated impact
* Self-organization
* Decentralized decision making
  * Fewer bottlenecks
* Framework for high-critically decisions
  * Microservices API and boundaries

## Hub and Spoke architecture
* Backend services aligned to business
* Cross-cutting concerns at API gateway
  * Authorization
* Gateway concerns

## Event-driven architecture
* Events can be consumed and produced via Event Bus(eg: kafka)

# Sync communications
* Rely on RPCs
* Service discovery
* Availability and latency
  
# Async communications
Message bus communications

**Eventual consistency and async comm/event driven architecture often go hand in hand.**

### Accelerate: the science of devops
* Deployment Frequency
  * Deplpoyment frequency is the measure of how often the software is released to production
* Lead time
  * Time takes to build, test, and deploy a new increment of functionality
* MTTR mean time to recovery
  * When a service is interrupted, how long it takes to restore.
* Change failure rate
  * Change failure rate is the percentage of changes delivered to production that cause service degradation or immediately require remediation
