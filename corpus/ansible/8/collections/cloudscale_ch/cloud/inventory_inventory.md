---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.inventory inventory – cloudscale.ch inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/inventory_inventory.html
fetched_at: 2026-07-28T01:05:38+00:00
---
# cloudscale_ch.cloud.inventory inventory – cloudscale.ch inventory source

> **Note:**
>
> This inventory plugin is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/ui/repo/published/cloudscale_ch/cloud/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.inventory`.

- [Synopsis](inventory_inventory.md#synopsis)
- [Parameters](inventory_inventory.md#parameters)
- [Examples](inventory_inventory.md#examples)

## [Synopsis](inventory_inventory.md#id1)

- Get inventory hosts from cloudscale.ch API
- Uses an YAML configuration file ending with either *cloudscale.yml* or *cloudscale.yaml* to set parameter values (also see examples).

Aliases: cloudscale

## [Parameters](inventory_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **ansible_host**  string | Which IP address to register as the ansible_host. If the  requested value does not exist or this is set to ‘none’, no ansible_host will be set.  **Choices:**   - `"public_v4"` ← (default) - `"public_v6"` - `"private"` - `"none"` |
| **api_token**  string | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **inventory_hostname**  string | What to register as the inventory hostname.  If set to ‘uuid’ the uuid of the server will be used and a group will be created for the server name. If set to ‘name’ the name of the server will be used unless there are more than one server with the same name in which case the ‘uuid’ logic will be used.  **Choices:**   - `"name"` ← (default) - `"uuid"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | Token that ensures this is a source file for the ‘cloudscale’  plugin.  **Choices:**   - `"cloudscale"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](inventory_inventory.md#id3)

```yaml+jinja
# cloudscale.yml name ending file in YAML format
# Example command line: ansible-inventory --list -i inventory_cloudscale.yml

plugin: cloudscale_ch.cloud.inventory

# Example grouping by tag key "project"
plugin: cloudscale_ch.cloud.inventory
keyed_groups:
  - prefix: project
    key: cloudscale.tags.project

# Example grouping by key "operating_system" lowercased and prefixed with "os"
plugin: cloudscale_ch.cloud.inventory
keyed_groups:
  - prefix: os
    key: cloudscale.image.operating_system | lower
```

### Authors

- Gaudenz Steinlin (@gaudenz)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
