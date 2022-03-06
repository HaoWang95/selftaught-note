# The -> Operator
In C and C++, we can use . to call method on the object directly and `->` if we are calling the method on a pointer to the object and need to dereference the pointer first.
Rust doesn't have an equivalent to the -> operator, instead, Rust has a feature called **`automatic referencing and dereferencing.`** The automatic referencing behavior works because methods have a clear receiver, which is the type of `self`. Given the receiver and name of a method, Rust can figure out definitely whether the method is **reading(&self), mutating(mut &self) or consuming(self).**

# The match control flow
Rust has an extremely powerful control flow construct called `match` that allows us to compare a value against a series of patterns and then execute code based on which pattern matches. 
# Concise control flow with if let
The `if let` syntax lets us combine if and let into a less verbose way to handle values that match one pattern while ignoring the rest.
```Rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {}", max),
    _ => (),
}
```

Consider the code above, if the value is `Some`, we print out the value in the `Some` variant by binding the value the the variable `max` in the pattern.
Instead, we could write this in a shorter way using `if let`.
```Rust
let config_max = Some(3u8);
if let Some(max) = config_max{
    println!();
}
```

Using if let means less typing, less indentation, and less boilerplate code. However, you lose the exhaustive checking that match enforces. Choosing between match and if let depends on what you’re doing in your particular situation and whether gaining conciseness is an appropriate trade-off for losing exhaustive checking.