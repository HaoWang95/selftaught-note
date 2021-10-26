# A tour of C++

## Introduction
By taking a quick tour of C++, it can give me the idea of what C++ is, without going into a lot of details. This is a bottom-up presentation of language and library facilities by enabling the use of a rich set of facilities.

## Basics
C++ is a compiled language. For a program to run, its source text has to be processed by a compiler, producing object files, which are combined by a linker yielding an executable program.
The ISO C++ standard defines two kinds of entities:
* The core language features, such as built-in types(char,int) and loops(for, while)
* Standard library components(vector,map,<< and getline())

## Some hints
> C++ supports two notions of immutability:
* **const**: meaning roughly "I promise not to change this value". This is used primarily to specify interfaces so that data can be passed into functions using pointers and references without fear of it being modified. The compiler enforces the promise made by const. The value of a const can be calculated at run time.
* **constexpr**: meaning roughly "to be evaluated at compile time". This is used primarily to specify constants, to allow placement of data in read-only memory(where it is unlikely to be corrupted), and for performance. The value of a **constexpr** must be calculated by the compiler.
```c++
constexpr int dmv = 17; //dmv is a named constant
int var = 17; //var is just a normal integer

double sum(const vector<double>&); // by providing a const, sum not modify its argument

vector<double> v{1.2, 2.2, 3.2, 4.2}; // vector v is not a constant
const double s1 = sum(v); // sum(v) is evaluated at run time
constexpr double s2 = sum(v) // error here, sum(v) is not a constant expression
```
For a function to be usable in a __constant expression__, that is, in an expression that will be evaluated by the compiler, it must be defined **constexpr**.
```c++
constexpr double square(double x){return x*x;}

constexpr double n1 = square(4); //ok
constexpr double n2 = square(var); //error: var is not a constant expression
const double n3 = square(var); // Ok, may be evaluated at run time
```