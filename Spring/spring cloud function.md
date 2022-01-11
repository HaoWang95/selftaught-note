# Spring Cloud Function

Short-lived, asynchronous microservices.

* Spring Cloud Function apps are powered by Spring Boot
* Relies on Project Reactor for reactive APIs
* Used in other projects like Spring Cloud Stream

Steps to create a Spring Cloud Function
* Add dependencies
* Choose functional interface
* Add business logic into the function
* Annotate as bean

Choose from functional interfaces
>- The Supplier interface
* This interface returns a data stream and would respond to an **Http GET** request.

>- The Consumer interface
* Privides data and would respond to an **Http POST** request.

>- The Functional interface
* The Functional interface accepts and returns data and would responds to an **HTTP POST or GET request**.