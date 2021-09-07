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

Go does not support classes. The feature in go is to **define methods on types**. So the definition of **function** and **methods** are different in go.
> - **A method is a function with a special __receiver__ argument**
**The receiver appears in its own argument list between the func keyword and the method name**
```Go
import (
	"fmt"
	"math"
)
// use struct to define a type
type Vertex struct {
	X, Y float64
}

type User struct {
    name, email string
    age int
}

// the method Abs()'s receiver is v, whihc is a Vertext type
// This syntax is werid
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}

```