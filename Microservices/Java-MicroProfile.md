# **What is MicroProfile**
MicroProfile is an open-source specification that brings a number of microservices-centric features to the JavaEE ecosystem.

## **MicroProfile APIs**
> - Open API
    > Provides a JAX-RS binding for the OpenAPI specification. It is an API description format for REST. The feature is enabled by default in all MicroProfile applications and automatically generates API documentation for JAX-RS endpoints
> - Open Tracing
    > Providing a standard for instrumenting microservices for distributed tracing in a tech agnostic manner. Tools can be Zipkin or Jaeger.
> - JWT propagation
    > Java binding for the JWT specification.
> - Configuration
> - Rest Client
> - Health Check
    > Health checks probe the state of a computing node from another machine to facilitate things like monitoring dashboards, auto-restart and self-healing.
> - Metrics
    > Similiar to health checks, metrics publish common statistics in a standard location and format. This information is collected and used by distributed metrics registries such as Prometheus/K8s.
> Fault Tolerance
    > This is similiar to resiliency4j, it makes dealing with unrealiability by standardizing a set of common failure-handling patterns via annotations.