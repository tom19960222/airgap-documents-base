---
collection: ansible
version: "8"
title: "ngine_io.vultr.vultr inventory – Vultr inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/vultr/vultr_inventory.html
fetched_at: 2026-07-28T01:05:54+00:00
---
# ngine_io.vultr.vultr inventory – Vultr inventory source

> **Note:**
>
> This inventory plugin is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/vultr/) (version 1.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr`.

- [Synopsis](vultr_inventory.md#synopsis)
- [Parameters](vultr_inventory.md#parameters)
- [Examples](vultr_inventory.md#examples)

## [Synopsis](vultr_inventory.md#id1)

- Get inventory hosts from Vultr public cloud.
- Uses an YAML configuration file ending with either *vultr.yml* or *vultr.yaml* to set parameter values (also see examples).
- Uses *api_config*, *~/.vultr.ini*, *./vultr.ini* or `VULTR_API_CONFIG` pointing to a Vultr credentials INI file (see <https://docs.ansible.com/ansible/latest/scenario_guides/guide_vultr.html>).

## [Parameters](vultr_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Specify the account to be used.  **Default:** `"default"` |
| **api_config**  path | Path to the vultr configuration file. If not specified will be taken from regular Vultr configuration.  **Configuration:**   - Environment variable: [`VULTR_API_CONFIG`](../../environment_variables.md#envvar-VULTR_API_CONFIG) |
| **api_key**  string | Vultr API key. If not specified will be taken from regular Vultr configuration.  **Configuration:**   - Environment variable: [`VULTR_API_KEY`](../../environment_variables.md#envvar-VULTR_API_KEY) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **filter_by_tag**  string | Only return servers filtered by this tag |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **hostname**  string | Field to match the hostname. Note v4_main_ip corresponds to the main_ip field returned from the API and name to label.  **Choices:**   - `"v4_main_ip"` ← (default) - `"v6_main_ip"` - `"name"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | Token that ensures this is a source file for the ‘vultr’ plugin.  **Choices:**   - `"vultr"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](vultr_inventory.md#id3)

```yaml+jinja
# inventory_vultr.yml file in YAML format
# Example command line: ansible-inventory --list -i inventory_vultr.yml

# Group by a region as lower case and with prefix e.g. "vultr_region_amsterdam" and by OS without prefix e.g. "CentOS_7_x64"
plugin: vultr
keyed_groups:
  - prefix: vultr_region
    key: region | lower
  - separator: ""
    key: os

# Pass a tag filter to the API
plugin: vultr
filter_by_tag: Cache
```

### Authors

- Yanis Guenane (@Spredzy)
- René Moser (@resmo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
