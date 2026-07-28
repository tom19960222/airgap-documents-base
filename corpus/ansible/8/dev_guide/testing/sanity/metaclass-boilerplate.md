---
collection: ansible
version: "8"
title: "metaclass-boilerplate"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/metaclass-boilerplate.html
fetched_at: 2026-07-28T01:03:32+00:00
---
# metaclass-boilerplate

Most Python files should include the following boilerplate at the top of the file, right after the
comment header and `from __future__ import`:

```python
__metaclass__ = type
```

Python 2 has “new-style classes” and “old-style classes” whereas Python 3 only has new-style classes.
Adding the `__metaclass__ = type` boilerplate makes every class defined in that file into
a new-style class as well.

```python
from __future__ import absolute_import, division, print_function
__metaclass__ = type

class Foo:
    # This is a new-style class even on Python 2 because of the __metaclass__
    pass
```
