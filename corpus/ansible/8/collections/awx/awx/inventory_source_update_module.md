---
collection: ansible
version: "8"
title: "awx.awx.inventory_source_update module – Update inventory source(s)."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/inventory_source_update_module.html
fetched_at: 2026-07-28T01:11:34+00:00
---
# awx.awx.inventory_source_update module – Update inventory source(s).

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.inventory_source_update`.

- [Synopsis](inventory_source_update_module.md#synopsis)
- [Parameters](inventory_source_update_module.md#parameters)
- [Notes](inventory_source_update_module.md#notes)
- [Examples](inventory_source_update_module.md#examples)
- [Return Values](inventory_source_update_module.md#return-values)

## [Synopsis](inventory_source_update_module.md#id1)

- Update Automation Platform Controller inventory source(s). See <https://www.ansible.com/tower> for an overview.

Aliases: tower_inventory_source_update

## [Parameters](inventory_source_update_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **interval**  float | The interval to request an update from the controller.  **Default:** `2.0` |
| **inventory**  string / required | Name or id of the inventory that contains the inventory source(s) to update. |
| **name**  aliases: inventory_source  string / required | The name or id of the inventory source to update. |
| **organization**  string | Name, ID, or named URL of the inventory source’s inventory’s organization. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **timeout**  integer | If waiting for the job to complete this will abort after this amount of seconds |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **wait**  boolean | Wait for the job to complete.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](inventory_source_update_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](inventory_source_update_module.md#id4)

```yaml+jinja
- name: Update a single inventory source
  inventory_source_update:
    name: "Example Inventory Source"
    inventory: "My Inventory"
    organization: Default

- name: Update all inventory sources
  inventory_source_update:
    name: "{{ item }}"
    inventory: "My Other Inventory"
  loop: "{{ query('awx.awx.controller_api', 'inventory_sources', query_params={ 'inventory': 30 }, return_ids=True ) }}"
```

## [Return Values](inventory_source_update_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  integer | id of the inventory update  **Returned:** success  **Sample:** `86` |
| **status**  string | status of the inventory update  **Returned:** success  **Sample:** `"pending"` |

### Authors

- Bianca Henderson (@beeankha)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
