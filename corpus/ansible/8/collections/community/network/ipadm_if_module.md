---
collection: ansible
version: "8"
title: "community.network.ipadm_if module – Manage IP interfaces  on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ipadm_if_module.html
fetched_at: 2026-07-28T01:56:58+00:00
---
# community.network.ipadm_if module – Manage IP interfaces on Solaris/illumos systems.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ipadm_if`.

- [Synopsis](ipadm_if_module.md#synopsis)
- [Parameters](ipadm_if_module.md#parameters)
- [Examples](ipadm_if_module.md#examples)
- [Return Values](ipadm_if_module.md#return-values)

## [Synopsis](ipadm_if_module.md#id1)

- Create, delete, enable or disable IP interfaces on Solaris/illumos systems.

Aliases: network.illumos.ipadm_if

## [Parameters](ipadm_if_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | IP interface name. |
| **state**  string | Create or delete Solaris/illumos IP interfaces.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **temporary**  boolean | Specifies that the IP interface is temporary. Temporary IP interfaces do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](ipadm_if_module.md#id3)

```yaml+jinja
- name: Create vnic0 interface
  community.network.ipadm_if:
    name: vnic0
    state: enabled

- name: Disable vnic0 interface
  community.network.ipadm_if:
    name: vnic0
    state: disabled
```

## [Return Values](ipadm_if_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | IP interface name  **Returned:** always  **Sample:** `"vnic0"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | persistence of a IP interface  **Returned:** always  **Sample:** `true` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
