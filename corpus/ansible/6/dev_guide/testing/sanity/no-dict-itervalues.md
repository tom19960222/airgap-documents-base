---
collection: ansible
version: "6"
title: "no-dict-itervalues"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/no-dict-itervalues.html
fetched_at: 2026-07-27T16:42:28+00:00
---
# no-dict-itervalues

The `dict.itervalues` method has been removed in Python 3. There are two recommended alternatives:

```python
for VALUE in DICT.values():
   pass
```

```python
from ansible.module_utils.six import itervalues

for VALUE in itervalues(DICT):
    pass
```
