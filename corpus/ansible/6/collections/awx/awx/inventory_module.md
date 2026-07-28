---
collection: ansible
version: "6"
title: "awx.awx.inventory module – create, update, or destroy Automation Platform Controller inventory."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/inventory_module.html
fetched_at: 2026-07-27T16:45:27+00:00
---
# awx.awx.inventory module – create, update, or destroy Automation Platform Controller inventory.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.inventory`.

- [Synopsis](inventory_module.md#synopsis)
- [Parameters](inventory_module.md#parameters)
- [Notes](inventory_module.md#notes)
- [Examples](inventory_module.md#examples)

## [Synopsis](inventory_module.md#id1)

- Create, update, or destroy Automation Platform Controller inventories. See <https://www.ansible.com/tower> for an overview.

## [Parameters](inventory_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **copy_from**  string | Name or id to copy the inventory from.  This will copy an existing inventory and change any parameters supplied.  The new inventory name will be the one provided in the name parameter.  The organization parameter is not used in this, to facilitate copy from one organization to another.  Provide the id or use the lookup plugin to provide the id if multiple inventories share the same name. |
| **description**  string | The description to use for the inventory. |
| **host_filter**  string | The host_filter field. Only useful when `kind=smart`. |
| **instance_groups**  list / elements=string | list of Instance Groups for this Organization to run on. |
| **kind**  string | The kind field. Cannot be modified after created.  Choices:   - `""` ← (default) - `"smart"` |
| **name**  string / required | The name to use for the inventory. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **organization**  string / required | Organization the inventory belongs to. |
| **prevent_instance_group_fallback**  boolean | Prevent falling back to instance groups set on the organization  Choices:   - `false` - `true` |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **variables**  dictionary | Inventory variables. |

## [Notes](inventory_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](inventory_module.md#id4)

```yaml+jinja
- name: Add inventory
  inventory:
    name: "Foo Inventory"
    description: "Our Foo Cloud Servers"
    organization: "Bar Org"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Copy inventory
  inventory:
    name: Copy Foo Inventory
    copy_from: Default Inventory
    description: "Our Foo Cloud Servers"
    organization: Foo
    state: present
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
