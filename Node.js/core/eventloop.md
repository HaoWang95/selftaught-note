# What is event loop in general
**JavaScript is single-threaded.**
Most modern kernels are multi-threaded, they can handle multiple operations executing in the background. When one of these ops complete, the kernel tells Node.js that the appropriate callback may be added to the **poll** queue to eventually by executed.

**The most basic mechanism to get notified about the completion of an asynchronous operation in Node.js is the `callback`, which is nothing more than a function invoked by the runtime with the result of an asynchronous operation.**

## Event Loop
When Node.js starts, it initializes the event loop, the processes that provide input script which may make async API calls, schedule timers, or call `process.nextTick()`, then begins processing the event loop.

### Phases
* timers: execute callbacks scheduled by `setTimeout()` and `setInterval()`.
  * A timer specifies the **threshold** after which a provided callback may be executed rather than the exact time a person wants it to be executed. Timers callbacks will run as early as they can be scheduled after the specified amount of time has passed; however, OS scheduling or the running or other callbacks may delay them.
* pending callbacks: executes I/O callbacks deferred to the next loop iteration.
* idle, prepare: only used internally
* poll: retrive new I/O events; executes I/O related callbacks; node will block here when appropriate.
* check: `setImmediate()` callbacks are invoked here.
* close callbacks: some close callbacks.
Between each run of the event loop, Node.js checks if it is waiting for any asynchronous I/O or timers and shuts down cleanly if there are not any.

```JavaScript
// in this code snippet, 
// we schedule a timeout to execute after a 100ms threshold, then this script starts asynchornously
// reading a file which takes 95ms.
const fs = require('fs');

const asyncOperation = (callback) => {
    // Assume this takes 95ms to complete
    fs.readFile('path', callback);
};

const timeoutScheduled = Date.now();

setTimeout(() => {
    const delay = Date.now() - timeoutScheduled;
    console.log(`${delay}ms have passed since it was scheduled`);
}, 100);

asyncOperation(() => {
    const startCallback = Date.now();

    while(Date.now() - startCallback < 10){
        // do nothing
    }
});
```
When the event loop enters the **poll** phase, it has an empty queue(fs.readFile() has not completed), so it will wait for the number of ms remaining until the soonest timer's threshold is reached. While it is waiting the 95ms pass, `fs.readFile()` finishes reading the file and its callback which takes 10ms to complete is added to the poll queue and executed. When the callback finishes, there are no more callbacks in the queue, so the event loop will see that the threshold of the soonest timer has been reached then wrap back to the timers phase to execute the timer's callback. As the code snippet above, the total delay between the timer being scheduled and its callback being executed will be 105ms.

## What needs to be covered to understand callbacks and events
* The callback pattern
* The observer pattern

## The Callback pattern
**Callbacks are the materialization of the handlers of the Reactor pattern.** 
> While the **reactor design pattern** is an event handling pattern for handling services delivered concurrently to a service handler by one or more inputs. The service handler then demultiplexes the incoming requests and dispatches them synchronously to the associated request handlers. The **Reactor pattern** is one implementation technique of event-driven architecture. For short, it uses a single threaded event loop blocking on resource-emitting events and dispatches them to corresponding handlers and callbacks.

Callbacks are functions that are invoked to propagate the result of an operation, and this is exactly what we need when dealing with asynchronous operations. In asynchronous world, callbacks replace the use of `return` operation.
```JavaScript
function additionAsync(a, b, callback){
    setTimeout(() => callback(a+b), 1000);
}

console.log('before);
additionAsync(1, 2, result => console.log(`Result: ${result}`))
console.log('after');
```
### SYNC AND ASYNC callbacks
* Sync callbacks:
  * Are invoked in the original thread, so do not create thread-safety concerns by themselves
  * In languages like C/C++, may access data on the stack such as local variables
  * May access data tied to the current thread, such as thread-local variables. For example Java Web Frameworks my create thread-local variables for current transaction or request
  * May be able to assume that certain application state is unchanged, for example assume that objects exist, timers have not fired, IO has not occurred, or whatever state the structure of a program involves.
* Async callbacks:
  * May be invoked on another thread(for thread-based deferral mechanism), so apps must synchronize any resources the callback accesses.
  * Cannot touch anything tied to the original stack or thread, such as local variables or thread-local data
  * If the original thread held lock, the callback will be invoked outside them
  * Must assume that other threads or events could have modified the application's state
#### Synchronized resources should defer all callbacks they invoke
A lib should drop all its locks before invoking an application callback. But the simplist way to drop all locks is to make the callback async, thereby deferring it until the stack unwinds back to the main loop, or running it on another thread's stack.
> Callbacks work very well in client-side **`JavaScript(single-threaded)`** and in `**Node.js**`. If we are using a callback-based solution on the **JVM**, we will need to pick a event loop library like **Vert.X**.

### CPS -> The continuation-passing style
In JavaScript, a callback is a function that is passed as an argument to another function, and is invoked with the result when the operation completes. In functional programming, this way of propagating the result is called **continuation-passing style.** In a general concept, it is not always associated with asynchronous operations. In fact, **it simply indicates that a result is propagated by passing it to another function(the callback function)**, instead of directly returning it to the caller.

### Synchronous CPS & Asynchronous CPS && Non-CPS callbacks
```JavaScript
function simpleAdd(a, b){
    return a + b;
}

function simpleAddCps(a, b, callback){
    callback(a, b);
}

function simpleAddAsyncCps(a, b, callback){
    setTimeout(() => callback(a, b), 1000);
}
```