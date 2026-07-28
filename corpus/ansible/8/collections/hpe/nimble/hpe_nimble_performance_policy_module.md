---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_performance_policy module – Manage the HPE Nimble Storage performance policies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_performance_policy_module.html
fetched_at: 2026-07-28T02:34:24+00:00
---
# hpe.nimble.hpe_nimble_performance_policy module – Manage the HPE Nimble Storage performance policies

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
> see [Requirements](hpe_nimble_performance_policy_module.md#ansible-collections-hpe-nimble-hpe-nimble-performance-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_performance_policy`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_performance_policy_module.md#synopsis)
- [Requirements](hpe_nimble_performance_policy_module.md#requirements)
- [Parameters](hpe_nimble_performance_policy_module.md#parameters)
- [Notes](hpe_nimble_performance_policy_module.md#notes)
- [Examples](hpe_nimble_performance_policy_module.md#examples)

## [Synopsis](hpe_nimble_performance_policy_module.md#id1)

- Manage the performance policies on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_performance_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_performance_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app_category**  string | Specifies the application category of the associated volume. |
| **block_size**  integer | Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created. |
| **cache**  boolean | Flag denoting if data in the associated volume should be cached.  **Choices:**   - `false` - `true` |
| **cache_policy**  string | Specifies how data of associated volume should be cached. Normal policy caches data but skips in certain conditions such as sequential I/O. Aggressive policy will accelerate caching of all data belonging to this volume, regardless of sequentiality.  **Choices:**   - `"disabled"` - `"normal"` - `"aggressive"` - `"no_write"` - `"aggressive_read_no_write"` |
| **change_name**  string | Change name of the existing performance policy. |
| **compress**  boolean | Flag denoting if data in the associated volume should be compressed.  **Choices:**   - `false` - `true` |
| **dedupe**  boolean | Specifies if dedupe is enabled for volumes created with this performance policy.  **Choices:**   - `false` - `true` |
| **description**  string | Description of a performance policy. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **name**  string / required | Name of the performance policy. |
| **password**  string / required | HPE Nimble Storage password. |
| **space_policy**  string | Specifies the state of the volume upon space constraint violation such as volume limit violation or volumes above their volume reserve, if the pool free space is exhausted. Supports two policies, ‘offline’ and ‘non_writable’.  **Choices:**   - `"invalid"` - `"offline"` - `"non_writable"` - `"read_only"` - `"login_only"` |
| **state**  string / required | The performance policy operation.  **Choices:**   - `"present"` - `"absent"` - `"create"` |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_performance_policy_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_performance_policy_module.md#id5)

```yaml+jinja
# if state is create , then create a performance policy if not present. Fails if already present.
# if state is present, then create a performance policy if not present. Succeed if it already exists.
- name: Create performance policy if not present
  hpe.nimble.hpe_nimble_performance_policy:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: "{{ state | default('present') }}"
    name: "{{ name }}"
    description: "{{ description }}"
    block_size: "{{ block_size }}"
    compress: "{{ compress }}"

- name: Delete performance policy
  hpe.nimble.hpe_nimble_performance_policy:
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
