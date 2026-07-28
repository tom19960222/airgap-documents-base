---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_facts module – Collect facts from Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_facts_module.html
fetched_at: 2026-07-27T17:55:26+00:00
---
# mellanox.onyx.onyx_facts module – Collect facts from Mellanox ONYX network devices

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_facts`.

- [Synopsis](onyx_facts_module.md#synopsis)
- [Parameters](onyx_facts_module.md#parameters)
- [Notes](onyx_facts_module.md#notes)
- [Examples](onyx_facts_module.md#examples)
- [Return Values](onyx_facts_module.md#return-values)

## [Synopsis](onyx_facts_module.md#id1)

- Collects a base set of device facts from a ONYX Mellanox network devices This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## [Parameters](onyx_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, version, module, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial `M(!`) to specify that a specific subset should not be collected.  Default: `"version"` |

## [Notes](onyx_facts_module.md#id3)

> **Note:**
>
> - Tested against ONYX 3.6

## [Examples](onyx_facts_module.md#id4)

```yaml+jinja
---
- name: Collect all facts from the device
  onyx_facts:
    gather_subset: all
- name: Collect only the interfaces facts
  onyx_facts:
    gather_subset:
      - interfaces
- name: Do not collect version facts
  onyx_facts:
    gather_subset:
      - "!version"
```

## [Return Values](onyx_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device  Returned: always |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system  Returned: when interfaces is configured |
| **ansible_net_modules**  dictionary | A hash of all modules on the systeme with status  Returned: when modules is configured |
| **ansible_net_version**  dictionary | A hash of all currently running system image information  Returned: when version is configured or when no gather_subset is provided |

### Authors

- Waleed Mousa (@waleedym), Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
