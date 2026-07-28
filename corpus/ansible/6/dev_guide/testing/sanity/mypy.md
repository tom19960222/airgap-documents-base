---
collection: ansible
version: "6"
title: "mypy"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/mypy.html
fetched_at: 2026-07-27T16:42:27+00:00
---
# mypy

The `mypy` static type checker is used to check the following code against each Python version supported by the controller:

> - `lib/ansible/`
> - `test/lib/ansible_test/_internal/`

Additionally, the following code is checked against Python versions supported only on managed nodes:

> - `lib/ansible/modules/`
> - `lib/ansible/module_utils/`

See <https://mypy.readthedocs.io/en/stable/> for additional details.
