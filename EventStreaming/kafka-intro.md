# **Kafka**
Kafka combines three key capabilities.
* To publish and subscribe to streams of events, including continuous import/export of the data from other systems.
* To store streams of events durably and reliably for as long as we want
* To process streams of events as they occur or retrospectively.

Kafka is a distributed system consisting of servers and clients that communicae via **tcp** protocol.
> Kafka servers
    > Kafka servers are one or more servers that span multiple datacenters or cloud regions. Some of these servers form the storage layer, called the brokers. Other servers run Kafka connect to continuously import and export data as event streams to integrate Kafka with our existing systems such as relational databases as well as other Kafka clusters.
> Kafka Clients
    > Clients allow us to write distributed applications and microservices that read, write and process streams of events in parallel. Kafka ships with dozens of clients that available for Java, Scala, Go, Python, C/C++, .Net, PHP...

## **Kafka Main Concepts**
* An **event** records the fact that something happened. It is also called record or message.
* **Producers** are client applications that **publish(write) events** to Kafka, and **consumers** are those **subscribe(read and process)** these events.

* **Events** are organized and durably stored in **topics**, a topic is similiar to a folder in a filesystem, and the events are the files in that folder. An example topic can be **"payments"**.  

* A **topic in Kafka are always multi-producer and multi-consumer**. You define how long Kafka should retain your events through a per-topic configuration setting, after which old events will be discarded. Kafka's performance is effectively constant with respect to data size, so storing data for a long time is perfectly fine. 
  
* **Topics are partitioned**, meaning a topic is spread over a number of buckets located on different kafka brokers. **Events with the same event key(a customer id)** are written to the same partition, and Kafka guarantees that any consumer of a given topic-partition will always read the partition's events in exactly the same order as they were written.
  
* **Topics can be replicated**, -> refer to Designing data-intensive applications.
