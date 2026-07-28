---
collection: ansible
version: "6"
title: "community.windows.win_product_facts module – Provides Windows product and license information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_product_facts_module.html
fetched_at: 2026-07-27T17:23:42+00:00
---
# community.windows.win_product_facts module – Provides Windows product and license information

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_product_facts`.

- [Synopsis](win_product_facts_module.md#synopsis)
- [Examples](win_product_facts_module.md#examples)
- [Returned Facts](win_product_facts_module.md#returned-facts)

## [Synopsis](win_product_facts_module.md#id1)

- Provides Windows product and license information.

## [Examples](win_product_facts_module.md#id2)

```yaml+jinja
- name: Get product id and product key
  community.windows.win_product_facts:

- name: Display Windows edition
  debug:
    var: ansible_os_license_edition

- name: Display Windows license status
  debug:
    var: ansible_os_license_status
```

## [Returned Facts](win_product_facts_module.md#id3)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_os_license_channel**  string | The Windows license channel.  Returned: always  Sample: `"Volume:MAK"` |
| **ansible_os_license_edition**  string | The Windows license edition.  Returned: always  Sample: `"Windows(R) ServerStandard edition"` |
| **ansible_os_license_status**  string | The Windows license status.  Returned: always  Sample: `"Licensed"` |
| **ansible_os_product_id**  string | The Windows product ID.  Returned: always  Sample: `"00326-10000-00000-AA698"` |
| **ansible_os_product_key**  string | The Windows product key.  Returned: always  Sample: `"T49TD-6VFBW-VV7HY-B2PXY-MY47H"` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
