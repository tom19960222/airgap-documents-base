---
collection: ansible
version: "6"
title: "cloud.common.turbo_fail module – A short module which honor additional args when calling fail_json"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cloud/common/turbo_fail_module.html
fetched_at: 2026-07-27T17:03:03+00:00
---
# cloud.common.turbo_fail module – A short module which honor additional args when calling fail_json

> **Note:**
>
> This module is part of the [cloud.common collection](https://galaxy.ansible.com/cloud/common) (version 2.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloud.common`.
>
> To use it in a playbook, specify: `cloud.common.turbo_fail`.

New in cloud.common 1.0.0

- [Synopsis](turbo_fail_module.md#synopsis)
- [Parameters](turbo_fail_module.md#parameters)
- [Examples](turbo_fail_module.md#examples)

## [Synopsis](turbo_fail_module.md#id1)

- This module aims to test fail_json method on Ansible.turbo module

## [Parameters](turbo_fail_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **params**  dictionary | parameter to display in task output |

## [Examples](turbo_fail_module.md#id3)

```yaml+jinja
- name: Fail without additional arguments
  cloud.common.turbo_fail:

- name: Fail with additional arguments
  cloud.common.turbo_fail:
    params:
        test: "ansible"
```

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cloud.common/issues)
[Repository (Sources)](https://github.com/ansible-collections/cloud.common)
