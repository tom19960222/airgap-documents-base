---
collection: ansible
version: "6"
title: "community.hrobot.robot inventory – Hetzner Robot inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/robot_inventory.html
fetched_at: 2026-07-27T17:15:57+00:00
---
# community.hrobot.robot inventory – Hetzner Robot inventory source

> **Note:**
>
> This inventory plugin is part of the [community.hrobot collection](https://galaxy.ansible.com/community/hrobot) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.robot`.

New in community.hrobot 1.1.0

- [Synopsis](robot_inventory.md#synopsis)
- [Parameters](robot_inventory.md#parameters)
- [Notes](robot_inventory.md#notes)
- [Examples](robot_inventory.md#examples)

## [Synopsis](robot_inventory.md#id1)

- Reads servers from Hetzner Robot API.
- Uses a YAML configuration file that ends with `robot.yml` or `robot.yaml`.
- The inventory plugin adds all values from <https://robot.your-server.de/doc/webservice/en.html#get-server> prepended with `hrobot_` to the server’s inventory. For example, the variable `hrobot_dc` contains the data center the server is located in.

## [Parameters](robot_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  Default: `"memory"`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  Default: `"ansible_inventory_"`  Configuration:   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  Default: `3600`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **filters**  dictionary | A dictionary of filter value pairs.  Available filters are listed here are keys of server like `status` or `server_ip`.  See <https://robot.your-server.de/doc/webservice/en.html#get-server> for all values that can be used.  Default: `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **hetzner_password**  string / required | The password for the Robot webservice user.  Configuration:   - Environment variable: [`HROBOT_API_PASSWORD`](../../environment_variables.md#envvar-HROBOT_API_PASSWORD) |
| **hetzner_user**  string / required | The username for the Robot webservice user.  Configuration:   - Environment variable: [`HROBOT_API_USER`](../../environment_variables.md#envvar-HROBOT_API_USER) |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **plugin**  string / required | Token that ensures this is a source file for the plugin.  Choices:   - `"community.hrobot.robot"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Notes](robot_inventory.md#id3)

> **Note:**
>
> - The *hetzner_user* and *hetzner_password* options can be templated.

## [Examples](robot_inventory.md#id4)

```yaml+jinja
# Fetch all hosts in Hetzner Robot
plugin: community.hrobot.robot
# Filters all servers in ready state
filters:
  status: ready

# Example showing encrypted credentials
# (This assumes that Mozilla sops was used to encrypt keys/hetzner.sops.yaml, which contains two values
# hetzner_username and hetzner_password. Needs the community.sops collection to decode that file.)
plugin: community.hrobot.robot
hetzner_user: '{{ (lookup("community.sops.sops", "keys/hetzner.sops.yaml") | from_yaml).hetzner_username }}'
hetzner_password: '{{ (lookup("community.sops.sops", "keys/hetzner.sops.yaml") | from_yaml).hetzner_password }}'

# Example using constructed features to create groups
plugin: community.hrobot.robot
filters:
  status: ready
  traffic: unlimited
# keyed_groups may be used to create custom groups
strict: false
keyed_groups:
  # Add e.g. groups for every data center
  - key: hrobot_dc
    separator: ""
# Use the IP address to connect to the host
compose:
  server_name_ip: hrobot_server_name ~ '-' ~ hrobot_server_ip
```

### Authors

- Oleksandr Stepanov (@alexandrst88)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
