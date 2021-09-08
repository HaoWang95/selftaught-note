# Interface

> - Interfaces are implemented implicitly.
```Go
type Profile interface {
	Show() // Profile interface has a method called Show
}

type MyProfile struct {
	profile string // A self-defined data type called MyProfile
}

// Implicitly implement the Show() for type MyProfile
func (p MyProfile) Show() {
	if len(p.profile) > 0 {
		fmt.Printf("Profile is %v.\n", p.profile)
	} else {
		// By default, it will be a default string
		fmt.Printf("Profile is empty. %v, %T", p.profile, p.profile)
	}
}

func testInterface() {
	var me MyProfile = MyProfile{profile: "Associate Developer"}
	me.Show()
	var you MyProfile = MyProfile{}
	you.Show()
}
```
Implicit interfaces decouple the definition of an interface from its implementation, which could then appear in any package without prearrangement.

> - Interface values can be thought of as a tuple of a value and a concrete type. **(value, type)**
An interface value holds a value of a specific underlying concrete type. And calling a method on an interface value executes the method of the same name on its underlying type.
```Go
// An interface called I, which has a M() method
type I interface {
	M()
}

// A type T
type T struct {
	S string
}

// Implements the M() for type T implicitly
func (t *T) M() {
	fmt.Println(t.S)
}

// Another type F
type F float64

// Implements the M() for type F implicitly
func (f F) M() {
	fmt.Println(f)
}

func main() {
	var i I // create an interface value
	i = &T{"Hello"} // i is type T
	describe(i)
	i.M() // call M()

	i = F(math.Pi) // re-assign to F
	describe(i)
	i.M()
}

func describe(i I) {
	fmt.Printf("(%v, %T)\n", i, i) // interface is (value, type)
}
```
> - If the concret value inside the interface is nil, the method will be called with a nil receiver.
```Go
// still, a simple interface with a method M()
type I interface{
    M()
}

type T struct{
    S string
}

func (t *T) M(){
    if t == nil{
        fmt.Println("nil")
        return
    }
    fmt.Println(t.)
}
```
> -  A nil interface value holds neither value nor concrete type. Calling a method on a nil interface is a run-time error because there's no type inside the interface tuple to indicate which concrete method to call.

```Go
type I interface{
    M()
}

// panic: runtime error: invalid memory address or nil pointer dereference.
func main(){
    var i I
    describe(i)
    i.M()
}

func describe(i I){
    fmt.Println("(%v, %T)", i, i)
}
```
> -  A pretty tricky but common use case is empty interface. The interface type that specifies 0 methods. An empty interface may hold values of any type. It can be used as values of unknown type.