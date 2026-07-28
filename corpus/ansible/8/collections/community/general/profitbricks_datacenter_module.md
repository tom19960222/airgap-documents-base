---
collection: ansible
version: "8"
title: "community.general.profitbricks_datacenter module – Create or destroy a ProfitBricks Virtual Datacenter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/profitbricks_datacenter_module.html
fetched_at: 2026-07-28T01:49:13+00:00
---
# community.general.profitbricks_datacenter module – Create or destroy a ProfitBricks Virtual Datacenter

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](profitbricks_datacenter_module.md#ansible-collections-community-general-profitbricks-datacenter-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.profitbricks_datacenter`.

- [Synopsis](profitbricks_datacenter_module.md#synopsis)
- [Requirements](profitbricks_datacenter_module.md#requirements)
- [Parameters](profitbricks_datacenter_module.md#parameters)
- [Attributes](profitbricks_datacenter_module.md#attributes)
- [Examples](profitbricks_datacenter_module.md#examples)

## [Synopsis](profitbricks_datacenter_module.md#id1)

- This is a simple module that supports creating or removing vDCs. A vDC is required before you can create servers. This module has a dependency on profitbricks >= 1.0.0

Aliases: cloud.profitbricks.profitbricks_datacenter

## [Requirements](profitbricks_datacenter_module.md#id2)

The below requirements are needed on the host that executes this module.

- profitbricks

## [Parameters](profitbricks_datacenter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description of the virtual datacenter. |
| **location**  string | The datacenter location.  **Choices:**   - `"us/las"` ← (default) - `"de/fra"` - `"de/fkb"` |
| **name**  string | The name of the virtual datacenter. |
| **state**  string | Create or terminate datacenters.  The available choices are: `present`, `absent`.  **Default:** `"present"` |
| **subscription_password**  string | THe ProfitBricks password. Overrides the PB_PASSWORD environment variable. |
| **subscription_user**  string | The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable. |
| **wait**  boolean | wait for the datacenter to be created before returning  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `600` |

## [Attributes](profitbricks_datacenter_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](profitbricks_datacenter_module.md#id5)

```yaml+jinja
- name: Create a datacenter
  community.general.profitbricks_datacenter:
    datacenter: Tardis One
    wait_timeout: 500

- name: Destroy a datacenter (remove all servers, volumes, and other objects in the datacenter)
  community.general.profitbricks_datacenter:
    datacenter: Tardis One
    wait_timeout: 500
    state: absent
```

### Authors

- Matt Baldwin (@baldwinSPC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
