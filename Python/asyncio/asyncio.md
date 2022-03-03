Concurrency means allowing more than one task being handled at the same time.
Asynchronous means that a particular long-running task can be run in the background separaet from the main application. Instead of blocking all other application code waiting for the long-running task to be completed, the system is free to do other work that is not dependant on that task.
A coroutine is a method that can be paused when we have a potentially long-running task and then resumed when that task is finished. **asyncio is a library to execute these coroutines in an asynchronous fashion using a concurrency model known as a single-threaded event loop.**

## What is concurrency, parallelism and multitasking
When two tasks are happening concurrently, those tasks are happening at the same time.
Parallelism, not only are there two or more tasks happening concurrently, but they are also executing at the same time.