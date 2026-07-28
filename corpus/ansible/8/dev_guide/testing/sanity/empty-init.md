---
collection: ansible
version: "8"
title: "empty-init"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/empty-init.html
fetched_at: 2026-07-28T01:03:28+00:00
---
# empty-init

The `__init__.py` files under the following directories must be empty. For some of these (modules
and tests), `__init__.py` files with code won’t be used. For others (module_utils), we want the
possibility of using Python namespaces which an empty `__init__.py` will allow for.

- `lib/ansible/modules/`
- `lib/ansible/module_utils/`
- `test/units/`
