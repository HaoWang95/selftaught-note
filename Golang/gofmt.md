# **Go formats**
fmt implements formatted I/O, similiar with C's printf and scanf.
The basic date type of go is quite similiar with C.


> - %v the value in a default format
> - %#v Go-syntax representation of the value
> - %T Go-syntax representation of the type of the value
> - %% percent sign
> - %t the word true or false
> - %b base 2
> - %c the char represented by the corresponding Unicode code point 
> - %d base 10
> - %o base 8
> - %O base 8 with 0o prefix
> - %q a single-quoted character literal safely escaped with Go-syntax
> - %x base 16, with lower-case letters for a-f
> - %X base 16, with upper-case letters for A-F
> - %U Unicode format

Floating-point and complex constituents:
> - %b decimalless scientific notation with exponent a power of two, in the manner  of strconv.FormatFloat with the 'b' format.
> - %e scientific notation with lower-case e
> - %E scientific notation with upper-case E
> - %f decimal point but no exponent 
> - %F synonym for %f
> - %g %e for large exponents, %f otherwise.
> - %G %E for large exponents, %F otherwise.
> - %x hexadecimal notation
> - %X upper-case hexadecimal notation

For normal cases of floating point num:
* %f default width, default precision
* %9f width 9, default precision
* %.2f default width, precision 2
* %9.2f width 9, precision 2
* %9.f width 9, precision 0

```Go
func testPrimitives() {
	// It is quite straghtforward to practice concepts in csapp.
	numInt1 := 10 //1010
	numInt2 := 3  // 0011
	numFloat1 := 3.14
	numFloat2 := 2.1e14
	strString1 := "This is string in go"
	fmt.Printf("The two numbers are %d\tand %d.\n", numInt1, numInt2)
	fmt.Printf("Perform & operation between %d and %d is %d.\n", numInt1, numInt2, numInt1&numInt2)
	fmt.Printf("Perform | operation between %d and %d is %d.\n", numInt1, numInt2, numInt1|numInt2)
	fmt.Printf("Perform ^ operation between %d and %d is %d.\n", numInt1, numInt2, numInt1^numInt2)
	fmt.Printf("Perform %d << %d is %d.", numInt1, numInt2, numInt1<<numInt2)
	fmt.Printf("Perform %d >> %d is %d.\n", numInt1, numInt2, numInt1>>numInt2)
	fmt.Printf("The data type of %v is %T, the data type of %v is %T\n", numFloat1, numFloat1, numFloat2, numFloat2)
	fmt.Println(strString1)
	formatterString := fmt.Sprintf("The result is: %s", strString1) // It returns a formatted string
	fmt.Println(formatterString)
}
```