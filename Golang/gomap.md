# **Go map**

In Golang, a map performs similiar task like **map** in other programming languages.
The zero value of a map is nil. A nil map has no keys, nor can be added.
Use the **make** function to build a map.

```Go
myMap := make(map[key_type]value_type)
```

A map can be iterated.
```Go
for k,v in range myMap:
    // do something
    fmt.Println(k,v)
```
