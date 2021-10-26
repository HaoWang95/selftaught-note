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
> Pointers, arrays, and references.
The most fundamental collection of data is a contiguously allocated sequence of elements of the same type, which is an array. 
```c++
char c[6]; // A char array of length 6

char* cp; // A pointer to char

// In declarations, [] means array of, * means "pointer to", & means "address of"
```
* "*" means "pointer to".
* & means "address of".
```c++
char *p = &v[3] // p points to v's fourth element
char x = *p // *p is the object that p points to
```

If we don't want to copy the values during function call or looping, use the reference can avoid that.
```c++
int v[] {1,2,3,4,5,6};
for(auto& item: container){
    item ++;
}
```
When we don't want to modify an argument but still don't want the cost of copying, we use the **const** reference.
For example"
```c++
double sum(const vector<double>&);// using the reference to avoid copying and using const to avoid modification
```
> The Null Pointer
There's only one **nullptr** shared by all pointer types.
```c++
double* doubleptr = nullptr;
Link<Record>* list = nullptr;
char* c = nullptr;
```
It is wise to check that a pointer argument actually points to something.
```c++
int count_x(const char*p, char x)
    // count the number of occurences of x in p[]
    // p can be a pointer const points to a char, or an array 
{
    if(p == nullptr){
        return 0;
    }
    int count{0};
    for(;*p!=0;++p){
        if(*p==x){
            count++;
        }
    }
    return count;
}
// we can have another version of count_x using while loop
int count_x_v2(const char* p, char x){
    if(p==nullptr){
        return 0;
    }
    int count{0};
    while(*p){
        if(*p==x){
            count++;
        }
    }
    return count;
}
```