---
collection: ansible
version: "8"
title: "ansible.builtin.host_group_vars vars – In charge of loading group_vars and host_vars"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/host_group_vars_vars.html
fetched_at: 2026-07-28T01:05:18+00:00
---
# ansible.builtin.host_group_vars vars – In charge of loading group_vars and host_vars

> **Note:**
>
> This vars plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `host_group_vars`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.host_group_vars` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same vars plugin name.

- [Synopsis](host_group_vars_vars.md#synopsis)
- [Requirements](host_group_vars_vars.md#requirements)
- [Parameters](host_group_vars_vars.md#parameters)

## [Synopsis](host_group_vars_vars.md#id1)

- Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
- Files are restricted by extension to one of .yaml, .json, .yml or no extension.
- Hidden (starting with ‘.’) and backup (ending with ‘~’) files and directories are ignored.
- Only applies to inventory sources that are existing paths.
- Starting in 2.10, this plugin requires enabling and is enabled by default.

## [Requirements](host_group_vars_vars.md#id2)

The below requirements are needed on the local controller node that executes this vars.

- Enabled in configuration

## [Parameters](host_group_vars_vars.md#id3)

| Parameter | Comments |
| --- | --- |
| **_valid_extensions**  list / elements=string | Check all of these extensions when looking for ‘variable’ files which should be YAML or JSON or vaulted versions of these.  This affects vars_files, include_vars, inventory and vars plugins among others.  **Default:** `[".yml", ".yaml", ".json"]`  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   yaml_valid_extensions = .yml, .yaml, .json   ``` - Environment variable: [`ANSIBLE_YAML_FILENAME_EXT`](../../../reference_appendices/config.md#envvar-ANSIBLE_YAML_FILENAME_EXT) |
| **stage**  string  *added in ansible-base 2.10* | Control when this vars plugin may be executed.  Setting this option to `all` will run the vars plugin after importing inventory and whenever it is demanded by a task.  Setting this option to `task` will only run the vars plugin whenever it is demanded by a task.  Setting this option to `inventory` will only run the vars plugin after parsing inventory.  If this option is omitted, the global *RUN_VARS_PLUGINS* configuration is used to determine when to execute the vars plugin.  **Choices:**   - `"all"` - `"task"` - `"inventory"`   **Configuration:**   - INI entry:  ```YAML+Jinja   [vars_host_group_vars]   stage = VALUE   ``` - Environment variable: [`ANSIBLE_VARS_PLUGIN_STAGE`](../../environment_variables.md#envvar-ANSIBLE_VARS_PLUGIN_STAGE) |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
