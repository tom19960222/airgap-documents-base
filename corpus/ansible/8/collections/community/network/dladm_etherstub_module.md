---
collection: ansible
version: "8"
title: "community.network.dladm_etherstub module – Manage etherstubs on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/dladm_etherstub_module.html
fetched_at: 2026-07-28T01:56:25+00:00
---
# community.network.dladm_etherstub module – Manage etherstubs on Solaris/illumos systems.

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
> To use it in a playbook, specify: `community.network.dladm_etherstub`.

- [Synopsis](dladm_etherstub_module.md#synopsis)
- [Parameters](dladm_etherstub_module.md#parameters)
- [Examples](dladm_etherstub_module.md#examples)
- [Return Values](dladm_etherstub_module.md#return-values)

## [Synopsis](dladm_etherstub_module.md#id1)

- Create or delete etherstubs on Solaris/illumos systems.

Aliases: network.illumos.dladm_etherstub

## [Parameters](dladm_etherstub_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Etherstub name. |
| **state**  string | Create or delete Solaris/illumos etherstub.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **temporary**  boolean | Specifies that the etherstub is temporary. Temporary etherstubs do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](dladm_etherstub_module.md#id3)

```yaml+jinja
- name: Create 'stub0' etherstub
  community.network.dladm_etherstub:
    name: stub0
    state: present

- name: Remove 'stub0 etherstub
  community.network.dladm_etherstub:
    name: stub0
    state: absent
```

## [Return Values](dladm_etherstub_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | etherstub name  **Returned:** always  **Sample:** `"switch0"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | etherstub’s persistence  **Returned:** always  **Sample:** `true` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
