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
1. The resources are added to a data structure, associating each one of them with a specific operation.
2. The demultiplexer is set up with the group of resources to be watched. The call to `demultiplexer.watch()` is synchronous and blocks until any of the watched resources are ready for read. When this occurs, the event demultiplexer returns from the call and a new set of events is available to be processed. 
3. Each event returned by the event demultiplexer is processed. At this point, the resource associated with each event is guaranteed to be ready to read and to not block during the operation. When all the events are processed, the flow will block again on the event demultiplexer until new events are again available to be processed. This is called event loop.

Withe the reactor pattern, we can handle several I/O operation inside a single thread, without using the busy-waiting technique. 

# The reactor pattern
The main idea behind the reactor pattern is to have a handler associated with each I/O operation. A handler in Node.js is represented by a `callback` function. The handler will be invoked as soon as an event is produced and processed by the event loop.

1. The application generates a new I/O operation by submitting a request to the **Event Demultiplexer.** The application also specifies a handler(event handler), which will be invoked when the operation completes. Submitting a new request to the **Event Demultiplexer** is a non-blocking call and it immediately returns control of the application
2. When a set of I/O operation completes, the **Event Demultiplexer** pushes a set of corresponding events into the **Event Queue**.
3. The event loop iterates over the items of the **Event Queue.**
4. For each event, the associated handler(event handler) is invoked.
5. The handler, which is part of the application code(because it is a callback function), gives back control to the Event Loop when its execution completes. While the handler executes, it can request new asynchronous operations, causing new items to be added into the Event Demultiplexer and eventaully add a new event into the event queue.
6. When all the items in the Event Queue are processed, the Event Loop blocks again on the Event Demultiplexer, which then triggers another cycle when a new event is available. 

> The reactor pattern handles I/O by blocking until new events are available from a set of observed resources, and then reacts by dispatching each event to an associated handler. 

# Libuv, the I/O engine of Node.js
Each OS has its own interface for the event demultiplexer, **`epoll` on Linux**, **`kqueue` on macOS**, and **`IOCP`(I/O completion port API) on Windows.** On top of that, each I/O operation can behave differently depending on the type of resource, even within the same OS. In Unix like OS, regular filesystem files do not support non-blocking operations, so in order to simulate the non-blocking behavior, it is necessary to use a separate thread outside the event loop.
All these inconsistencies across and within different operating systems required a higher-level abstraction to be built for the event demultiplexer. That's why **`libuv`** is created. The objective is to make Node.js compatible with all major operating systems and normalize the non-blocking behavior of different types of resource. Libuv represents the low-level I/O engine of Node.js and is probably the most important component that Node.js is built on.

# V8 as the execution engine
The reactor pattern and libuv are the basic building blocks of Node.js, but we need three more components to build the full platform.
* A set of binds responsible for wrapping and exposing libuv and other low-level functionalities to JavaScript.
* **V8**, the JavaScript engine originally developed by Google for the Chrome browser.
* A core JavaScript lib that implements the high-level Node.js API.

# JavaScript code in Node.js
There are differences between JavaScript running in Node.js and JavaScript we run in the browser.
The most obvious difference is that in Node.js we don't need a DOM and we don't have a `window` or a `document`. Node.js has access to a set of services offered by the underlying OS that are not available in the browser.

# The module system
* Node.js ships with a module system.
* Full access to operating system services.
  * Eg, we can access any file on the filesystem(with `fs` module), or we can write application tht use low-level TCP or UDP sockets using `net` and `dgram` modules. We can create HTTP(S) servers using `http` and `https` modules. Or we use the standard encryption and hashing algorithms of OpenSSL. We can also access some of the V8 internals or run code in a different V8 context. 

# Running Native Code
One of the powerful capabilities of Node.js is the possibility to create userland modules that can bind to native code. This gives the platform a tremendous advantage as it allows us to reuse existing or new components written in C/C++. Node.js provides great support for implemening native modules thanks to the N-API interface.
Also, most JavaScript VMs support **Wasm**.
