# What is event loop in general
**JavaScript is single-threaded.**
Most modern kernels are multi-threaded, they can handle multiple operations executing in the background. When one of these ops complete, the kernel tells Node.js that the appropriate callback may be added to the **poll** queue to eventually by executed.

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
