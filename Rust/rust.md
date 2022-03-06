# Ownership

Ownership in rust is a unique feature and has deep implications for the rest of the language. It enables Rust to make memory safety guarantees without needing a garbage collector.
Related features:

- borrowing
- slices

## Ownership rules

- Each value in Rust has a variable that's called its owner.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.

> Rust will never automatically create 'deep copy' of data. Therefore, any automatic copying can be assumed to be inexpensive in terms of runtime performance.

# Reference and borrowing

- Reference
  A reference is like a pointer in that it's an address we can follow to access data stored at te address that is owned by some other variables. Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type. The signature of **`&`** indicates a reference.

## Mutable references

- &mut Type indicates a mutable reference
  We can have only one mutable reference to a particular piece of data at a time.
  The restriction of **mutable reference** prevents data races at compile time. And Rust also enforces a similar rule for combining mutbale and immutable references.

```Rust
    let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    let r3 = &mut s; // BIG PROBLEM

    println!("{}, {}, and {}", r1, r2, r3);
```
Multiple immutbale references are allowed because no one who is reading the data has the ability to affect anyone else's reading of the data. But we can not have a mutable reference while we have an immutable one to the same value.

## Dangling References
Danging pointer, a pointer that references a location in memory that many have been given to someone else. 
In Rust, the compiler guarantees that references will never be dangling references, if we have a reference to some data, the compiler will ensure that the data will not go out of scope before the reference to the data does.

## The rules of references
* At any given time, we can either hae one mutable reference or multiple immutable references.
* References must be valid. 

## Slices
`Slices` lets us reference a contiguous sequence of elements in a collection rather than the whole collection. A slice is a kind of reference, so it does not have ownership

```rust
fn first_words(s: &String) -> usize:
    let bytes = s.as_bytes();

    for(i, &item) in bytes.iter().enumerate(){
        if item == b' '{
            return i;
        }
    }
    s.len()
// as_bytes, converts a Sring to an array of bytes
// iter that returns each element in a collection
// enumerate wraps the result of iter and returns each element as part of a tuple instead
```

### String slices
A string slice is a reference to part of a `String`.
```Rust
let st = String::from("Hello World");

let hello = &st[0..5];
let world = &st[6..11];
```
**[starting_index..ending_index]**, where `starting_index` is the first position in the slice and `ending_position` is one more than the last position in the slice.
```Rust
fn first_word(s: &String) -> &str{
    let bytes = s.as_bytes();

    for(i, &item) in bytes.iter().enumerate() {
        if item == b' '{
            return &s[..i];
        }
        return &s[..]; // or &s[..]
    }
}
```
