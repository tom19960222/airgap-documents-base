---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_pool module – Manage the HPE Nimble Storage pools"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_pool_module.html
fetched_at: 2026-07-28T02:34:25+00:00
---
# hpe.nimble.hpe_nimble_pool module – Manage the HPE Nimble Storage pools

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_pool_module.md#ansible-collections-hpe-nimble-hpe-nimble-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_pool`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_pool_module.md#synopsis)
- [Requirements](hpe_nimble_pool_module.md#requirements)
- [Parameters](hpe_nimble_pool_module.md#parameters)
- [Notes](hpe_nimble_pool_module.md#notes)
- [Examples](hpe_nimble_pool_module.md#examples)

## [Synopsis](hpe_nimble_pool_module.md#id1)

- Manage the storage pools on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **array_list**  list / elements=dictionary | List of arrays in the pool with detailed information. To create or update array list, only array ID is required. |
| **change_name**  string | Change name of the existing pool. |
| **dedupe_all_volumes**  boolean | Indicates if dedupe is enabled by default for new volumes on this pool.  **Choices:**   - `false` - `true` |
| **description**  string | Text description of pool. |
| **force**  boolean | Forcibly delete the specified pool even if it contains deleted volumes whose space is being reclaimed. Forcibly remove an array from array_list via an update operation even if the array is not reachable. There should no volumes in the pool for the force update operation to succeed.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **is_default**  boolean | Indicates if this is the default pool.  **Choices:**   - `false` - `true` |
| **merge**  boolean | Merge the specified pool into the target pool. All volumes on the specified pool are moved to the target pool and the specified pool is then deleted. All the arrays in the pool are assigned to the target pool.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the pool. |
| **password**  string / required | HPE Nimble Storage password. |
| **state**  string / required | The pool operation.  **Choices:**   - `"present"` - `"absent"` - `"create"` |
| **target**  string | Name of the target pool. |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_pool_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_pool_module.md#id5)

```yaml+jinja
# if state is create , then create a pool if not present. Fails if already present.
# if state is present, then create a pool if not present. Succeed if it already exists.
- name: Create pool if not present
  hpe.nimble.hpe_nimble_pool:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: "{{ state | default('present') }}"
    name: "{{ name }}"
    array_list: "{{ array_list }} "
    description: "{{ description }}"

- name: Delete pool
  hpe.nimble.hpe_nimble_pool:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: absent
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
