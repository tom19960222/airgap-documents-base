---
collection: ansible
version: "8"
title: "awx.awx.inventory_source module – create, update, or destroy Automation Platform Controller inventory source."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/inventory_source_module.html
fetched_at: 2026-07-28T01:11:32+00:00
---
# awx.awx.inventory_source module – create, update, or destroy Automation Platform Controller inventory source.

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
> To use it in a playbook, specify: `awx.awx.inventory_source`.

- [Synopsis](inventory_source_module.md#synopsis)
- [Parameters](inventory_source_module.md#parameters)
- [Notes](inventory_source_module.md#notes)
- [Examples](inventory_source_module.md#examples)

## [Synopsis](inventory_source_module.md#id1)

- Create, update, or destroy Automation Platform Controller inventory source. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_inventory_source

## [Parameters](inventory_source_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credential**  string | Credential name, ID, or named URL to use for the source. |
| **custom_virtualenv**  string | Local absolute file path containing a custom Python virtualenv to use.  Only compatible with older versions of AWX/Controller  Deprecated, will be removed in the future |
| **description**  string | The description to use for the inventory source. |
| **enabled_value**  string | Value when the host is considered enabled, e.g., “powered_on” |
| **enabled_var**  string | The variable to use to determine enabled state e.g., “status.power_state” |
| **execution_environment**  string | Execution Environment name, ID, or named URL to use for the source. |
| **host_filter**  string | If specified, AWX will only import hosts that match this regular expression. |
| **inventory**  string / required | Inventory name, ID, or named URL the group should be made a member of. |
| **limit**  string | Enter host, group or pattern match |
| **name**  string / required | The name to use for the inventory source. |
| **new_name**  string | A new name for this assets (will rename the asset) |
| **notification_templates_error**  list / elements=string | list of notifications to send on error |
| **notification_templates_started**  list / elements=string | list of notifications to send on start |
| **notification_templates_success**  list / elements=string | list of notifications to send on success |
| **organization**  string | Name of the inventory source’s inventory’s organization. |
| **overwrite**  boolean | Delete child groups and hosts not found in source.  **Choices:**   - `false` - `true` |
| **overwrite_vars**  boolean | Override vars in child groups and hosts with those from external source.  **Choices:**   - `false` - `true` |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **scm_branch**  string | Inventory source SCM branch.  Project must have branch override enabled. |
| **source**  string | The source to use for this group.  **Choices:**   - `"scm"` - `"ec2"` - `"gce"` - `"azure_rm"` - `"vmware"` - `"satellite6"` - `"openstack"` - `"rhv"` - `"controller"` - `"insights"` |
| **source_path**  string | For an SCM based inventory source, the source path points to the file within the repo to use as an inventory. |
| **source_project**  string | Project name, ID, or named URL to use as source with scm option |
| **source_vars**  dictionary | The variables or environment fields to apply to this source type. |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **timeout**  integer | The amount of time (in seconds) to run before the task is canceled. |
| **update_cache_timeout**  integer | Time in seconds to consider an inventory sync to be current. |
| **update_on_launch**  boolean | Refresh inventory data from its source each time a job is run.  **Choices:**   - `false` - `true` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **verbosity**  integer | The verbosity level to run this inventory source under.  **Choices:**   - `0` - `1` - `2` |

## [Notes](inventory_source_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](inventory_source_module.md#id4)

```yaml+jinja
- name: Add an inventory source
  inventory_source:
    name: "source-inventory"
    description: Source for inventory
    inventory: previously-created-inventory
    credential: previously-created-credential
    overwrite: True
    update_on_launch: True
    organization: Default
    source_vars:
      private: false
```

### Authors

- Adrien Fleury (@fleu42)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
