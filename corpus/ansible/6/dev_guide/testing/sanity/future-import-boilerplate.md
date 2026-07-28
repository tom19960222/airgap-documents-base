---
collection: ansible
version: "6"
title: "future-import-boilerplate"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/future-import-boilerplate.html
fetched_at: 2026-07-27T16:42:24+00:00
---
# future-import-boilerplate

Most Python files should include the following boilerplate at the top of the file, right after the
comment header:

```python
from __future__ import (absolute_import, division, print_function)
```

This uses Python 3 semantics for absolute vs relative imports, division, and print. By doing this,
we can write code which is portable between Python 2 and Python 3 by following the Python 3 semantics.

## absolute_import

When Python 2 encounters an import of a name in a file like `import copy` it attempts to load
`copy.py` from the same directory as the file is in. This can cause problems if there is a python
file of that name in the directory and also a python module in `sys.path` with that same name. In
that case, Python 2 would load the one in the same directory and there would be no way to load the
one on `sys.path`. Python 3 fixes this by making imports absolute by default. `import copy`
will find `copy.py` from `sys.path`. If you want to import `copy.py` from the same directory,
the code needs to be changed to perform a relative import: `from . import copy`.

> **See also:**
>
> - [Absolute and relative imports](https://www.python.org/dev/peps/pep-0328)

## division

In Python 2, the division operator (`/`) returns integer values when used with integers. If there
was a remainder, this part would be left off (aka, floor division). In Python 3, the division
operator (`/`) always returns a floating point number. Code that needs to calculate the integer
portion of the quotient needs to switch to using the floor division operator (//) instead.

> **See also:**
>
> - [Changing the division operator](https://www.python.org/dev/peps/pep-0238)

## print_function

In Python 2, [`print()`](https://docs.python.org/2/library/functions.html#print "(in Python v2.7)") is a keyword. In Python 3, [`print()`](https://docs.python.org/3/library/functions.html#print "(in Python v3.11)") is a function with different
parameters. Using this `__future__` allows using the Python 3 print semantics everywhere.

> **See also:**
>
> - [Make print a function](https://www.python.org/dev/peps/pep-3105)
