---
collection: ansible
version: "8"
title: "no-dict-itervalues"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/no-dict-itervalues.html
fetched_at: 2026-07-28T01:03:36+00:00
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
