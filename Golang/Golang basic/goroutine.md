# Goroutine
A goroutine is a lightweight thread managed by the Go runtime.

# Channels
> - go channel basic
Channels are typed conduit through which programmers can send and receive values with the channel operator **<-**.
Channels must be created before use.
ch := make(chan int) // this is a int channel.

```Go
import "fmt"

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // send sum to c
}

func main() {
	s := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c // receive from c

	fmt.Println(x, y, x+y)
}
```

> - channel range and close
A sender can close a channel to indicate that no more values will be sent. Receivers can test whether a channel has been closed by assigning a second parameter to the receive expression. 
For example: value, isOk := <- ch
Recode the fib in go channel.

> - use select statement to enable a goroutine wait on multiple communication operations. A select blocks untils one of its cases can run, then it executes that case. It chooses one at random if multiple are ready.