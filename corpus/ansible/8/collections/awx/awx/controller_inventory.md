---
collection: ansible
version: "8"
title: "awx.awx.controller inventory – Ansible dynamic inventory plugin for the Automation Platform Controller."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/controller_inventory.html
fetched_at: 2026-07-28T01:11:50+00:00
---
# awx.awx.controller inventory – Ansible dynamic inventory plugin for the Automation Platform Controller.

> **Note:**
>
> This inventory plugin is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.controller`.

- [Synopsis](controller_inventory.md#synopsis)
- [Parameters](controller_inventory.md#parameters)
- [Notes](controller_inventory.md#notes)
- [Examples](controller_inventory.md#examples)

## [Synopsis](controller_inventory.md#id1)

- Reads inventories from the Automation Platform Controller.
- Supports reading configuration from both YAML config file and environment variables.
- If reading from the YAML file, the file name must end with controller.(yml|yaml) or controller_inventory.(yml|yaml), the path in the command would be /path/to/controller_inventory.(yml|yaml). If some arguments in the config file are missing, this plugin will try to fill in missing arguments by reading from environment variables.
- If reading configurations from environment variables, the path in the command must be @controller_inventory.

Aliases: tower

## [Parameters](controller_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | The network address of your Automation Platform Controller host.  **Configuration:**   - Environment variable: [`CONTROLLER_HOST`](../../environment_variables.md#envvar-CONTROLLER_HOST) - Environment variable: [`TOWER_HOST`](../../environment_variables.md#envvar-TOWER_HOST)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_HOST |
| **include_metadata**  boolean | Make extra requests to provide all group vars with metadata about the source host.  **Choices:**   - `false` ← (default) - `true` |
| **inventory_id**  any / required | The ID of the inventory that you wish to import.  This is allowed to be either the inventory primary key or its named URL slug.  Primary key values will be accepted as strings or integers, and URL slugs must be strings.  Named URL slugs follow the syntax of “inventory_name++organization_name”.  **Configuration:**   - Environment variable: [`CONTROLLER_INVENTORY`](../../environment_variables.md#envvar-CONTROLLER_INVENTORY) |
| **oauth_token**  string | The OAuth token to use.  **Configuration:**   - Environment variable: [`CONTROLLER_OAUTH_TOKEN`](../../environment_variables.md#envvar-CONTROLLER_OAUTH_TOKEN) - Environment variable: [`TOWER_OAUTH_TOKEN`](../../environment_variables.md#envvar-TOWER_OAUTH_TOKEN)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_OAUTH_TOKEN |
| **password**  string | The password for your controller user.  **Configuration:**   - Environment variable: [`CONTROLLER_PASSWORD`](../../environment_variables.md#envvar-CONTROLLER_PASSWORD) - Environment variable: [`TOWER_PASSWORD`](../../environment_variables.md#envvar-TOWER_PASSWORD)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_PASSWORD |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10 seconds  This will not work with the export or import modules.  **Configuration:**   - Environment variable: [`CONTROLLER_REQUEST_TIMEOUT`](../../environment_variables.md#envvar-CONTROLLER_REQUEST_TIMEOUT) |
| **username**  string | The user that you plan to use to access inventories on the controller.  **Configuration:**   - Environment variable: [`CONTROLLER_USERNAME`](../../environment_variables.md#envvar-CONTROLLER_USERNAME) - Environment variable: [`TOWER_USERNAME`](../../environment_variables.md#envvar-TOWER_USERNAME)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_USERNAME |
| **verify_ssl**  aliases: validate_certs  boolean | Specify whether Ansible should verify the SSL certificate of the controller host.  Defaults to True, but this is handled by the shared module_utils code  **Choices:**   - `false` - `true`   **Configuration:**   - Environment variable: [`CONTROLLER_VERIFY_SSL`](../../environment_variables.md#envvar-CONTROLLER_VERIFY_SSL) - Environment variable: [`TOWER_VERIFY_SSL`](../../environment_variables.md#envvar-TOWER_VERIFY_SSL)  Removed in: version 4.0.0  Why: Collection name change  Alternative: CONTROLLER_VERIFY_SSL |

## [Notes](controller_inventory.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](controller_inventory.md#id4)

```yaml+jinja
# Before you execute the following commands, you should make sure this file is in your plugin path,
# and you enabled this plugin.

# Example for using controller_inventory.yml file

plugin: awx.awx.controller
host: your_automation_controller_server_network_address
username: your_automation_controller_username
password: your_automation_controller_password
inventory_id: the_ID_of_targeted_automation_controller_inventory
# Then you can run the following command.
# If some of the arguments are missing, Ansible will attempt to read them from environment variables.
# ansible-inventory -i /path/to/controller_inventory.yml --list

# Example for reading from environment variables:

# Set environment variables:
# export CONTROLLER_HOST=YOUR_AUTOMATION_PLATFORM_CONTROLLER_HOST_ADDRESS
# export CONTROLLER_USERNAME=YOUR_CONTROLLER_USERNAME
# export CONTROLLER_PASSWORD=YOUR_CONTROLLER_PASSWORD
# export CONTROLLER_INVENTORY=THE_ID_OF_TARGETED_INVENTORY
# Read the inventory specified in CONTROLLER_INVENTORY from the controller, and list them.
# The inventory path must always be @controller_inventory if you are reading all settings from environment variables.
# ansible-inventory -i @controller_inventory --list
```

### Authors

- Matthew Jones (@matburt)
- Yunfan Zhang (@YunfanZhang42)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
