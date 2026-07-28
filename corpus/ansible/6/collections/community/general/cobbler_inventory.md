---
collection: ansible
version: "6"
title: "community.general.cobbler inventory – Cobbler inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/cobbler_inventory.html
fetched_at: 2026-07-27T17:14:46+00:00
---
# community.general.cobbler inventory – Cobbler inventory source

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.cobbler`.

New in community.general 1.0.0

- [Synopsis](cobbler_inventory.md#synopsis)
- [Parameters](cobbler_inventory.md#parameters)
- [Examples](cobbler_inventory.md#examples)

## [Synopsis](cobbler_inventory.md#id1)

- Get inventory hosts from the cobbler service.
- Uses a configuration file as an inventory source, it must end in `.cobbler.yml` or `.cobbler.yaml` and has a `plugin: cobbler` entry.

## [Parameters](cobbler_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_fallback**  boolean | Fallback to cached results if connection to cobbler fails  Choices:   - `false` ← (default) - `true` |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  Default: `"memory"`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  Default: `"ansible_inventory_"`  Configuration:   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  Default: `3600`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **exclude_profiles**  list / elements=string | Profiles to exclude from inventory.  Ignored if *include_profiles* is specified.  Default: `[]` |
| **group**  string | Group to place all hosts into  Default: `"cobbler"` |
| **group_by**  list / elements=string | Keys to group hosts by  Default: `["mgmt_classes", "owners", "status"]` |
| **group_prefix**  string | Prefix to apply to cobbler groups  Default: `"cobbler_"` |
| **include_profiles**  list / elements=string  added in community.general 4.4.0 | Profiles to include from inventory.  If specified, all other profiles will be excluded.  *exclude_profiles* is ignored if *include_profiles* is specified.  Default: `[]` |
| **password**  string | Cobbler authentication password  Configuration:   - Environment variable: [`COBBLER_PASSWORD`](../../environment_variables.md#envvar-COBBLER_PASSWORD) |
| **plugin**  string / required | The name of this plugin, it should always be set to `community.general.cobbler` for this plugin to recognize it as it’s own.  Choices:   - `"cobbler"` - `"community.general.cobbler"` |
| **url**  string | URL to cobbler.  Default: `"http://cobbler/cobbler_api"`  Configuration:   - Environment variable: [`COBBLER_SERVER`](../../environment_variables.md#envvar-COBBLER_SERVER) |
| **user**  string | Cobbler authentication user.  Configuration:   - Environment variable: [`COBBLER_USER`](../../environment_variables.md#envvar-COBBLER_USER) |
| **want_facts**  boolean | Toggle, if `true` the plugin will retrieve host facts from the server  Choices:   - `false` - `true` ← (default) |

## [Examples](cobbler_inventory.md#id3)

```yaml+jinja
# my.cobbler.yml
plugin: community.general.cobbler
url: http://cobbler/cobbler_api
user: ansible-tester
password: secure
```

### Authors

- Orion Poplawski (@opoplawski)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
