---
collection: ansible
version: "6"
title: "ansible.builtin.yaml inventory – Uses a specific YAML file as an inventory source."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/yaml_inventory.html
fetched_at: 2026-07-27T16:42:47+00:00
---
# ansible.builtin.yaml inventory – Uses a specific YAML file as an inventory source.

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `yaml` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](yaml_inventory.md#synopsis)
- [Parameters](yaml_inventory.md#parameters)
- [Notes](yaml_inventory.md#notes)
- [Examples](yaml_inventory.md#examples)

## [Synopsis](yaml_inventory.md#id1)

- YAML-based inventory, should start with the `all` group and contain hosts/vars/children entries.
- Host entries can have sub-entries defined, which will be treated as variables.
- Vars entries are normal group vars.
- Children are ‘child groups’, which can also have their own vars/hosts/children and so on.
- File MUST have a valid extension, defined in configuration.

## [Parameters](yaml_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **yaml_extensions**  list / elements=string | list of ‘valid’ extensions for files containing YAML  Default: `[".yaml", ".yml", ".json"]`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   yaml_valid_extensions = .yaml, .yml, .json   ```  ```YAML+Jinja   [inventory_plugin_yaml]   yaml_valid_extensions = .yaml, .yml, .json   ``` - Environment variable: [`ANSIBLE_YAML_FILENAME_EXT`](../../../reference_appendices/config.md#envvar-ANSIBLE_YAML_FILENAME_EXT) - Environment variable: [`ANSIBLE_INVENTORY_PLUGIN_EXTS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_PLUGIN_EXTS) |

## [Notes](yaml_inventory.md#id3)

> **Note:**
>
> - If you want to set vars for the `all` group inside the inventory file, the `all` group must be the first entry in the file.
> - Enabled in configuration by default.

## [Examples](yaml_inventory.md#id4)

```yaml+jinja
all: # keys must be unique, i.e. only one 'hosts' per group
    hosts:
        test1:
        test2:
            host_var: value
    vars:
        group_all_var: value
    children:   # key order does not matter, indentation does
        other_group:
            children:
                group_x:
                    hosts:
                        test5   # Note that one machine will work without a colon
                #group_x:
                #    hosts:
                #        test5  # But this won't
                #        test7  #
                group_y:
                    hosts:
                        test6:  # So always use a colon
            vars:
                g2_var2: value3
            hosts:
                test4:
                    ansible_host: 127.0.0.1
        last_group:
            hosts:
                test1 # same host as above, additional group membership
            vars:
                group_last_var: value
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
