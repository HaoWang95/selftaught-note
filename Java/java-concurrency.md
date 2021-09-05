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
