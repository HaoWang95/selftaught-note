# Understand and use hash functions
A `cryptographic hash function` must meet three additional criteria
* One-way function property
* Weak collision resistance
* Strong collision resistance

- Collision resistance.
  - What is a collision?
    - When two messages hash to the same hash value, it is called a collision. 
    - A hash function has `weak collision resistance` if, given a message, it is infeasible to identify a second message that hashes to the same value. In other words, if an attacker has one input, it must be infeasible to identify another input capable of producing the same output.
    - A hash function has `strong collision resistance` if it is infeasible to find any collision whatsoever. The difference between weak collision resistance and strong collision resistance is subtle. Weak collision resistance is bound to a particular given message; strong collision resistance applies to any pair of messages. Strong collision resistance implies weak collision resistance, not the other way around. 

```Python
import hashlib

sorted(hashlib.algorithms_guaranteed)
```

- SHA-2
  - SHA-224, SHA-256, SHA-386, SHA-512. SHA-256 and SHA-512 are the core of the family.
- SHA-3
- BLAKE2

- MD5 and SHA-1 are not secure