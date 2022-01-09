# Ownership
## Ownership rules
* Each value in Rust has a variable that's called its owner.
* There can only be one owner at a time.
* When the owner goes out of scope, the value will be dropped.
  
> Rust will never automatically create 'deep copy' of data. Therefore, any automatic copying can be assumed to be inexpensive in terms of runtime performance. 

# Reference and borrowing
## Mutable references
