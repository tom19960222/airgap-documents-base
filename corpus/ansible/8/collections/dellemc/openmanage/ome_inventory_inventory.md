---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_inventory inventory – Group inventory plugin on OpenManage Enterprise."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_inventory_inventory.html
fetched_at: 2026-07-28T02:04:58+00:00
---
# dellemc.openmanage.ome_inventory inventory – Group inventory plugin on OpenManage Enterprise.

> **Note:**
>
> This inventory plugin is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](ome_inventory_inventory.md#ansible-collections-dellemc-openmanage-ome-inventory-inventory-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_inventory`.

New in dellemc.openmanage 7.1.0

- [Synopsis](ome_inventory_inventory.md#synopsis)
- [Requirements](ome_inventory_inventory.md#requirements)
- [Parameters](ome_inventory_inventory.md#parameters)
- [Notes](ome_inventory_inventory.md#notes)
- [Examples](ome_inventory_inventory.md#examples)

## [Synopsis](ome_inventory_inventory.md#id1)

- This plugin allows to retrieve inventory hosts from groups on OpenManage Enterprise.

## [Requirements](ome_inventory_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.9.6

## [Parameters](ome_inventory_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **group_vars**  dictionary | To include group variables in the inventory source. |
| **host_vars**  dictionary | To include host related variables in the inventory source. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname.  If the value is not specified in the task, the value of environment variable `OME_HOSTNAME` will be used instead.  **Configuration:**   - Environment variable: [`OME_HOSTNAME`](../../environment_variables.md#envvar-OME_HOSTNAME) |
| **ome_group_name**  string | Group name. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password.  If the value is not specified in the task, the value of environment variable `OME_PASSWORD` will be used instead.  **Configuration:**   - Environment variable: [`OME_PASSWORD`](../../environment_variables.md#envvar-OME_PASSWORD) |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  If the value is not specified in the task, the value of environment variable `OME_PORT` will be used instead.  **Default:** `443` |
| **timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username.  If the value is not specified in the task, the value of environment variable `OME_USERNAME` will be used instead.  **Configuration:**   - Environment variable: [`OME_USERNAME`](../../environment_variables.md#envvar-OME_USERNAME) |
| **validate_certs**  boolean | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_inventory_inventory.md#id4)

> **Note:**
>
> - Run this plugin on a system that has direct access to Dell OpenManage Enterprise.

## [Examples](ome_inventory_inventory.md#id5)

```yaml+jinja
---
# To retrieve all the groups host details.
plugin: dellemc.openmanage.ome_inventory
hostname: "192.168.0.1"
username: username
password: password

# To retrieve specific group host details.
plugin: dellemc.openmanage.ome_inventory
hostname: "192.168.0.1"
username: username
password: password
ome_group_name: group_name

# To set host variables to specific group host.
plugin: dellemc.openmanage.ome_inventory
hostname: "192.168.0.1"
username: username
password: password
ome_group_name: group_name
host_vars:
  idrac_user: username
  idrac_password: password

# To set host variables and multiple group variables.
plugin: dellemc.openmanage.ome_inventory
hostname: "192.168.0.1"
username: username
password: password
host_vars:
  idrac_user: username
  idrac_password: password
group_vars:
  group_name:
    attribute: value
  group_name_one:
    new_attribute: new_value
```

### Authors

- Felix Stephen (@felixs88)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
