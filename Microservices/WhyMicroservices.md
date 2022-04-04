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

# Event-driven architecture
* Events can be consumed and produced via Event Bus(eg: kafka)