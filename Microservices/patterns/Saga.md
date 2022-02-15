## Using the Sage pattern to maintain data consistency
A saga is a sequence of local transactions. Each local transactions updates data within a single service using the familiar ACID transaction frameworks and libraries. The completion of a local transaction triggers the execution of the next local transaction.

### Two challenges of saga
* Lack of isolation
* Rolling back changes when an error occurs

## Coordinating sagas
* **Choreography**, distrubute the decision making and sequencing among the saga participants. Primarily communicate by exchanging events.
  * There's no central coordinator telling saga participants what to do. The saga participants subscribe to each other's events and respond accordingly.
    * Advantages:
      * Simplicity, service publish events when they create, update, or delete business objects.
      * Losse coupling, the participants subscribe to events and don't have a direct knowledge of each other.
    * Disadvantages
      * Difficult to understand, unlike with orchestration, there isn't a single place in the code to define the saga. It can be hard to understand how a saga works, it's more like a mental graph.
      * Cyclic dependencies between services, the saga participants subscribe to each other's events, which often creates cyclic dependencies.
    * It works well for simple sagas, it's better to use orchestration for complex sagas.
* **`Orchestration`**, centralize saga's coordination logic in a saga orchestrator class. A saga *orchestrator* sends command messages to saga participants telling them which operations to perform
  * A good way to model a saga orchestration is as a state machine. A state machine consists of a set of states and a set of transitions between states that are triggerred by the completion of a local transaction performed by a saga participant. Using state machine model makes designing, implementing and testing sagas easier.
  * Advantages
    * Simpler dependencies
    * Less coupling
    * Improves separation of concerns and simplifies the business logic
  * Disadvantages
    * Centralizing too much business logic in the orchestrator.

