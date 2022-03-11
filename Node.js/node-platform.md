# The Node.js Platform
Know and understand how Node.js works will provide a strong foundation for understanding the reasoning behind some complex topics and patterns. Approaching Node.js is far more than simply learning a new technology. 
In this note, I'll need to address the following questions.
* The Node.js philosophy, what is the `Node way` to code.
* The reactor pattern which is at the heart of Node.js asynchronous event-driven architecture.
* Differences between running JavaScript on the browser and running JavaScript on the server.

# Node.js philosophy
* **Small Core**
* **Small modules**
  * with npm and yarn being the popular module managers, Node.js helps to solve the dependency hell problem by making sure that two packages depending on different versions of the same pacakge will use their own installations of such a package, thus avoiding conflicts.
* **Small surface area**
* **Simplicity and pragmatism**
  
# Event demultiplexing
Multiplexing refers to the method by which multiple signals are combined into one so that they can be easily transimitted over a medium with limited capacity.
Demultiplexing refers to the opposite that signal is split again into its original components.
# The reactor pattern
The main idea behind the reactor pattern is to have a handler associated with each I/O operation. A handler in Node.js is represented by a `callback` function. The handler will be invoked as soon as an event is produced and processed by the event loop.
```
watchedList.add(socketA, FOR_READ) // (1)
watchedList.add(fileB, FOR_READ)
while (events = demultiplexer.watch(watchedList)) { // (2)
 // event loop
 for (event of events) { // (3)
 // This read will never block and will always return data
 data = event.resource.read()
 if (data === RESOURCE_CLOSED) {
 // the resource was closed, remove it from the watched list
 demultiplexer.unwatch(event.resource)
 } else {
 // some actual data was received, process it
 consumeData(data)
 }
 }
}
```