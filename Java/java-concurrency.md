# Concurrency in Java
Java is a multithreaded language, and concurrency issues are present whether you are aware of them or not.

A very common example of performace improvement in single-processor systems is event-driven programming. 

## Basic threading
A thread is a single sequential flow of control within a process. A single process can thus have multiple concurrently executing tasks. A threading model is a programming convenience to simplify switching several operations at the same time within a single program.

A thread drives a task that implements the Runnable interface with the run method.
If a class is derived from **Runnable**, it must have a **run()** method. The run method usually has a kind of loop that continues until the task is no longer necessary. The **static Thread.yield()** inside **run()** is a suggestion to the thread scheduler to switch to some other tasks for a while.

```Java
public class CountDownRunnable implements Runnable {
    
    protected int countDown = 10;
    private static int taskCount = 0;
    private final int id = taskCount++;
    
    public CountDownRunnable(){ }
    
    public CountDownRunnable(int countDown){
        this.countDown = countDown;
    }
    
    public String status(){
        return "> #"+id+"("+(countDown > 0 ? countDown: "completed") +")";
    }
    
    @Override
    public void run() {
        while (countDown -- > 0){
            System.out.println(status());
            Thread.yield();
        }
    }
}
```
The basic Runnable task can be invoked in two ways.
```Java
public static void main(String[] args) {
        CountDownRunnable countDown = new CountDownRunnable();
        countDown.run();
        Thread myThread = new Thread(new CountDownRunnable());
        myThread.start();
}
```
The Thread constructor needs a Runnable object. Calling a Thread object's **start()** will perform the necessary initialization for the thread and then call that Runnable's run() method to start the task in the new thread.

### Using Executors
Using Executor to manage the execution of asynchronous tasks without having to explicitly manage the lifecycle of threads.
```Java
public static void executorTasksCachedThread(){
        ExecutorService executorService = Executors.newCachedThreadPool();
        for(var i = 0; i < 5; i++){
            executorService.execute(new CountDownRunnable(15));
        }
        executorService.shutdown();
    }
    
    public static void executorTasksFixedThread(){
        ExecutorService executorService = Executors.newFixedThreadPool(5);
        for(var i = 0; i < 5; i++){
            executorService.execute(new CountDownRunnable());
        }
        executorService.shutdown();
    }
```
### Implements Callable<T> to return value from tasks.
To deal with situation that a returned value is returned from tasks, implement the Callable instead of Runnable. The **run()** method would be **call()**.

### Priority of a thread
The order in which the CPU runs a set of threads is indeterminate, the scheduler will lean toward running the waiting thread with the highest priority first. Or we **setPriority()** and **getPriority()** of the existing thread.

### Runnable VS Thread
Note that Runnable is an interface while Thread is a class. Implements Runnable is a preferred way. Because implementing from an interface allow us to inherit from a different class, whereas inheriting from Thread does not. By implementing a Runnable, the code can be more flexible.

Also, prefer using an **Executor**.

### Hide threading details by using an inner class.
