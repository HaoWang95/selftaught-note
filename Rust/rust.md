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
