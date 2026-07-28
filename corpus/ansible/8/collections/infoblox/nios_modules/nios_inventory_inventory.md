---
collection: ansible
version: "8"
title: "infoblox.nios_modules.nios_inventory inventory – Infoblox inventory plugin"
source_url: https://docs.ansible.com/projects/ansible/8/collections/infoblox/nios_modules/nios_inventory_inventory.html
fetched_at: 2026-07-28T02:36:09+00:00
---
# infoblox.nios_modules.nios_inventory inventory – Infoblox inventory plugin

> **Note:**
>
> This inventory plugin is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/ui/repo/published/infoblox/nios_modules/) (version 1.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](nios_inventory_inventory.md#ansible-collections-infoblox-nios-modules-nios-inventory-inventory-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_inventory`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_inventory_inventory.md#synopsis)
- [Requirements](nios_inventory_inventory.md#requirements)
- [Parameters](nios_inventory_inventory.md#parameters)
- [Examples](nios_inventory_inventory.md#examples)

## [Synopsis](nios_inventory_inventory.md#id1)

- This plugin allows you to query the Infoblox Grid for host records and use the response data to populate the inventory file.

## [Requirements](nios_inventory_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.4
- infoblox-client

## [Parameters](nios_inventory_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **extattrs**  dictionary | Allows you to filter the returned host record based on the extensible attributes assigned to them.  **Default:** `{}` |
| **host**  string / required | Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST.  Value can also be specified using `INFOBLOX_HOST` environment variable.  **Configuration:**   - Environment variable: [`INFOBLOX_HOST`](../../environment_variables.md#envvar-INFOBLOX_HOST) |
| **hostfilter**  dictionary | Accepts a key/value pair and uses it to filter the host records to be returned.  **Default:** `{}` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_PASSWORD` environment variable.  **Configuration:**   - Environment variable: [`INFOBLOX_PASSWORD`](../../environment_variables.md#envvar-INFOBLOX_PASSWORD) |
| **username**  string / required | Configures the username to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_USERNAME` environment variable.  **Configuration:**   - Environment variable: [`INFOBLOX_USERNAME`](../../environment_variables.md#envvar-INFOBLOX_USERNAME) |

## [Examples](nios_inventory_inventory.md#id4)

```yaml+jinja
plugin: infoblox.nios_modules.nios_inventory
host: blox.example.com
username: admin
```

### Authors

- Will Tome (@willtome)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
- [Homepage](https://github.com/infobloxopen/infoblox-ansible)
- [Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
