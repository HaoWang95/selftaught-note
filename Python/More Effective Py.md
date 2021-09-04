# **Effective Python Series**

> - Use the subprocess built-in module to run subprocesses.
```Python
import subprocess
help(subprocess)
```

> - Prefer enumerate over range to iterate over a list if index is required.
```Python
alist = [...]
for i, item in enumerate(alist):
    pass
```
