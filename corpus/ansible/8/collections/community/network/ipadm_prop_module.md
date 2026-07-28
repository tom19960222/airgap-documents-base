---
collection: ansible
version: "8"
title: "community.network.ipadm_prop module – Manage protocol properties on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ipadm_prop_module.html
fetched_at: 2026-07-28T01:56:59+00:00
---
# community.network.ipadm_prop module – Manage protocol properties on Solaris/illumos systems.

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
> To use it in a playbook, specify: `community.network.ipadm_prop`.

- [Synopsis](ipadm_prop_module.md#synopsis)
- [Parameters](ipadm_prop_module.md#parameters)
- [Examples](ipadm_prop_module.md#examples)
- [Return Values](ipadm_prop_module.md#return-values)

## [Synopsis](ipadm_prop_module.md#id1)

- Modify protocol properties on Solaris/illumos systems.

Aliases: network.illumos.ipadm_prop

## [Parameters](ipadm_prop_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **property**  string / required | Specifies the name of property we want to manage. |
| **protocol**  string / required | Specifies the protocol for which we want to manage properties. |
| **state**  string | Set or reset the property value.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"reset"` |
| **temporary**  boolean | Specifies that the property value is temporary. Temporary property values do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **value**  string | Specifies the value we want to set for the property. |

## [Examples](ipadm_prop_module.md#id3)

```yaml+jinja
- name: Set TCP receive buffer size
  community.network.ipadm_prop:
    protocol: tcp
    property: recv_buf
    value: 65536

- name: Reset UDP send buffer size to the default value
  community.network.ipadm_prop:
    protocol: udp
    property: send_buf
    state: reset
```

## [Return Values](ipadm_prop_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **property**  string | name of the property  **Returned:** always  **Sample:** `"recv_maxbuf"` |
| **protocol**  string | property’s protocol  **Returned:** always  **Sample:** `"TCP"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | property’s persistence  **Returned:** always  **Sample:** `true` |
| **value**  integer | value of the property. May be int or string depending on property.  **Returned:** always  **Sample:** `"'1024' or 'never'"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
