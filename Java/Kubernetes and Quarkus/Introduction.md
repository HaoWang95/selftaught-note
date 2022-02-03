# **Quarkus**
Quarkus is a Java microservice runtime. It is designed to be as productive as Node.js for developers and consumes as few resources as Golang. **Quarkus is referred to as Kubernetes-native Java**.

* Live loading
  *  Traditional cloud native Java runtimes does a lot of work when they boot. Each time an application boots, it scans configuration files, scans for annotations, and instantiates and binds annotation to build an internal metamodel before executing application logic.
  *  Quarkus executes these steps during compilation and records the results as bytecode that executes at application startup.

### Kubernetes basic concepts warm up
* Service discovery
    >- Services deployed to Kubernetes are given a stable DNS name and IP addresses. For a microservice to consume another service, it only has to locate the service by a DNS name. Unlike early microservice deployments, Kubernetes does not need a third-party service registry to act as an intermediary to locate a service.
* Horizontal scaling
    >- Applications can be scaled out and scaled in manually or automatically based on metrics like CPU usage.
* Load balancing
    >- Kubernetes load-balances across application instances. This removes the need for client-side load balancing that become popular during the early days of microservices.
* Self-healing
    >- Kubernetes restarts failing containers and directs traffic away from containers that are temporarily unable to serve traffic.
* Configuration management
    >- Kubernetes can store and manage microservice configuration. Configurations can change without updating the application, removing the need for external configuration services used by early microservice deployments.

### Kubernetes architecture
* Cluster
    >- **A kubernetes cluster abstracts hardware or virtual servers(nodes) and presents them as a pool of resources.***`(Understand the cluster as a pool of resources)`* A cluster consists of one or more administration servers used to manage the cluster and any number of worker nodes used to run workloads(pods). The administration server exposes an API server used by administration tool, like `kubectl`, to interact with the cluster. When a workload(pod) is deployed to the cluster, the scheduler schedules the pod to execute on a node within the cluster.
* Namespace
    >- A means to **divide cluster resources between projects or teams**. A namespace can spn multiple nodes in a cluster, so the diagram is a bit oversimplified for readability. Names defined within a namespace must be unique but can be reused across namespaces.
* Pod
    >- A pod is one or more containers that share the same storage volumes, network, namespace, and life cycle. Pods are atomic units, so deploying a pod deploys all containers within that pod to the same node. Eg, a microservice may use a local out-of-process cache service. It may make sense to place the microservice and caching service in the same pod if they are tightly coupled. This ensures they are deployed at the same node and have the same life cycle. Sometimes the pod consists of one container per pod, so it will feel as if a pod is the same thing as a container, but that is not the case. A pod is ephemeral, meaning a pod's state is not maintained between descruction and any subsequent creation.
* Replication controller
    >- Ensures that the number of running pods matches the specifed number of replicas. Specifying more than one replica improves availability and service throughout. If one pod is killed, then the replica controller will instantiate a new one to replace it. A replication controller can also conduct rolling upgrade when a new container image version is specified.
* Deployment
    >- A deployment is a high-level abstraction that describes the state of a deployed application. For example, a deployment can specify the container image to be deployed, the number of replicas for that container image, health check probes used to check pod health, and more.
* Service
    >- A stable endpoint used ot access a group of like pods that brings stability to a highly dynamic environment.
* ConfigMap
    >- Used to store microservice configuration, separating configuration from the microservice itself. ConfigMaps are clear text. As an option, a Kubernetes Secret can be used to store confidential information.
