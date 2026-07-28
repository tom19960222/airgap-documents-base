---
collection: ansible
version: "6"
title: "no-dict-iterkeys"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/no-dict-iterkeys.html
fetched_at: 2026-07-27T16:42:28+00:00
---
# no-dict-iterkeys

The `dict.iterkeys` method has been removed in Python 3. Use the following instead:

```python
for KEY in DICT:
    pass
```
