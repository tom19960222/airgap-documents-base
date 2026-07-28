---
collection: ansible
version: "6"
title: "no-main-display"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/no-main-display.html
fetched_at: 2026-07-27T16:42:29+00:00
---
# no-main-display

As of Ansible 2.8, `Display` should no longer be imported from `__main__`.

`Display` is now a singleton and should be utilized like the following:

```python
from ansible.utils.display import Display
display = Display()
```

There is no longer a need to attempt `from __main__ import display` inside
a `try/except` block.
