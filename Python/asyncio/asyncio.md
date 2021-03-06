Concurrency means allowing more than one task being handled at the same time.
Asynchronous means that a particular long-running task can be run in the background separaet from the main application. Instead of blocking all other application code waiting for the long-running task to be completed, the system is free to do other work that is not dependant on that task.
A coroutine is a method that can be paused when we have a potentially long-running task and then resumed when that task is finished. **asyncio is a library to execute these coroutines in an asynchronous fashion using a concurrency model known as a single-threaded event loop.**

## What is concurrency, parallelism and multitasking
When two tasks are happening concurrently, those tasks are happening at the same time.
Parallelism, not only are there two or more tasks happening concurrently, but they are also executing at the same time.

## Global Interpreter Lock
GIL is a controversial topic, gil prevents one Python process from executing more than one Python Bytecode instruction at any given time. In CPython, memory is managed by a process known as reference counting. Reference counting works by keeping track of who currently needs access to a particular Python object, such as an integer, dictionary or list.


## Coroutine
Think of coroutine like a `regular Python function but with superpower that it can pasue its execution when it encounters an operation that could take a while to complete. When that long-running operation is complete, we can wake up the paused coroutine and finish executing any other code in that coroutine`.

## Creating coroutines with async keyword
* Using **`async`** keyword marks a function as a coroutine instead of a normal Python function.
* Using **`asyncio.run()`** to create an event. It runs the coroutine and returns the result. **asyncio.run** is intended to be the main entry point into the asyncio application.