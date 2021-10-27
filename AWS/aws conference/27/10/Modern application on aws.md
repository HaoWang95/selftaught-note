# Decompose into microservices.
* Separation of UX, UI and services.
* Loosely coupled, independently deployable
* Database per service pattern

> APIs are the front door of modular services.
> Events driven design

## Strangler pattern.
Slowly take out pieces of a monolithic application.

### Service Discovery and Integration(Microservice pattern guideline)
> Gateways
> Datastreams & events
> Message brokers

**Cloud Map** (another option for inter-service communication??)
**App Mesh** (weighted-routing to different virtual servers)

## Orchestrator pattern.


# Software Delivery
Automation, abstraction and standardisation.
> Continuous delivery

### Deployment strategies
* Blue/green deployment
* Canary deployment
* Constant monitoring of metrics, especially include business KPIs where possible