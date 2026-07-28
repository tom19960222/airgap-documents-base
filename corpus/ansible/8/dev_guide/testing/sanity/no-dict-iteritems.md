---
collection: ansible
version: "8"
title: "no-dict-iteritems"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/no-dict-iteritems.html
fetched_at: 2026-07-28T01:03:35+00:00
---
# no-dict-iteritems

The `dict.iteritems` method has been removed in Python 3. There are two recommended alternatives:

```python
for KEY, VALUE in DICT.items():
   pass
```

```python
from ansible.module_utils.six import iteritems

for KEY, VALUE in iteritems(DICT):
    pass
```
