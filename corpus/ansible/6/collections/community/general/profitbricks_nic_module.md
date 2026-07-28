---
collection: ansible
version: "6"
title: "community.general.profitbricks_nic module – Create or Remove a NIC"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/profitbricks_nic_module.html
fetched_at: 2026-07-27T17:12:04+00:00
---
# community.general.profitbricks_nic module – Create or Remove a NIC

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](profitbricks_nic_module.md#ansible-collections-community-general-profitbricks-nic-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.profitbricks_nic`.

- [Synopsis](profitbricks_nic_module.md#synopsis)
- [Requirements](profitbricks_nic_module.md#requirements)
- [Parameters](profitbricks_nic_module.md#parameters)
- [Examples](profitbricks_nic_module.md#examples)

## [Synopsis](profitbricks_nic_module.md#id1)

- This module allows you to create or restore a volume snapshot. This module has a dependency on profitbricks >= 1.0.0

## [Requirements](profitbricks_nic_module.md#id2)

The below requirements are needed on the host that executes this module.

- profitbricks

## [Parameters](profitbricks_nic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | The datacenter in which to operate. |
| **lan**  string | The LAN to place the NIC on. You can pass a LAN that doesn’t exist and it will be created. Required on create. |
| **name**  string | The name or ID of the NIC. This is only required on deletes, but not on create.  If not specified, it defaults to a value based on UUID4. |
| **server**  string / required | The server name or ID. |
| **state**  string | Indicate desired state of the resource  The available choices are: `present`, `absent`.  Default: `"present"` |
| **subscription_password**  string / required | THe ProfitBricks password. Overrides the PB_PASSWORD environment variable. |
| **subscription_user**  string / required | The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable. |
| **wait**  boolean | wait for the operation to complete before returning  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | how long before wait gives up, in seconds  Default: `600` |

## [Examples](profitbricks_nic_module.md#id4)

```yaml+jinja
- name: Create a NIC
  community.general.profitbricks_nic:
    datacenter: Tardis One
    server: node002
    lan: 2
    wait_timeout: 500
    state: present

- name: Remove a NIC
  community.general.profitbricks_nic:
    datacenter: Tardis One
    server: node002
    name: 7341c2454f
    wait_timeout: 500
    state: absent
```

### Authors

- Matt Baldwin (@baldwinSPC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
