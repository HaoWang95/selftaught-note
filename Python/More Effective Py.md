# **Effective Python Series**

> - Use the subprocess built-in module to run subprocesses.
```Python
import subprocess
help(subprocess)
```

> - Prefer enumerate over range to iterate over a list if index is required.
enumerate built-in function **wraps any iterator with a lazy generator.**
It provides concise syntax for looping over an iterator and getting the index of each item of the iterator.
```Python
alist = [...]
for i, item in enumerate(alist):
    pass
```

> - Use zip to process iterators in parallel.
The zip built-in function wraps two or more iterators with a lazy generator. But zip truncates its output silently to the
shortest iterator if we supply it with iterators of different lengths. If the iterators are of different lengths, 
use **itertools.zip_longest()** or other methods in **itertools**.
```python
names = ['julia','marie','lise','katrina']
name_len = [len(name) for name in names]
longest_name = None
max_len = 0
for name, length in zip(names, name_len):
    pass
```

> - Metaclass. It lets us intercept Python class statement and provide special behavior each time a class is defined.

