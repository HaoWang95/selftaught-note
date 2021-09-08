# Go functions

Functions are values too. Functions can be passed around like normal parameters.

```Go
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func main() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}
```

Go functions can be closures that reference variables from outside of its body.

```Go
import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}

```

Go does not support classes. The feature in go is to **define methods on types**.
> - **A method is a function with a special __receiver__ argument**
**The receiver appears in its own argument list between the func keyword and the method name**
**A method is a function with a receiver argument.**
```Go
import (
	"fmt"
	"math"
)
// use struct to define a type
type Vertex struct {
	X, Y float64
}

// the method Abs()'s receiver is v, whihc is a Vertext type
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}

```
Another example can be:
```Go
type User struct {
	name, email string
	age         int
}

func (u User) UserInfo() string {
	return u.name + ", " + u.email + ", " + strconv.FormatInt(int64(u.age), 10)
}
```

> - Also, a method can be declared on a non-struct type
Note that **it is only allowed to declare a method with a receiver whose type is defined in the same package as the method. It is not allowed to declare a method with a receiver whose type is defined in another package.**

> - Pointer receivers, the receiver type can be a pointer.
This indicates that the receiver type can be *T for type T. The T itself can not be a pointer.
Also, **functions that take a value argument must take a value of that specific type**. While methods **with value receivers take either a value or a pointer as the receiver when they are called**.

### Choose between a value and a pointer receiver
To use a pointer receiver.
* The method can modify the value that its receiver points to.
* Avoid copying the value on each method call. This can be efficient if the receiver is a large struct.
* And methods on a give type should have either value or pointer receivers, but not a mixture of both.

It needs some coding practice to know when to use a ptr and when not.
* Change a struct obj, use pointer receiver, it will change the value in place.
