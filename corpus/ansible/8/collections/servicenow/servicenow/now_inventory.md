---
collection: ansible
version: "8"
title: "servicenow.servicenow.now inventory – ServiceNow Inventory Plugin"
source_url: https://docs.ansible.com/projects/ansible/8/collections/servicenow/servicenow/now_inventory.html
fetched_at: 2026-07-28T01:05:58+00:00
---
# servicenow.servicenow.now inventory – ServiceNow Inventory Plugin

> **Note:**
>
> This inventory plugin is part of the [servicenow.servicenow collection](https://galaxy.ansible.com/ui/repo/published/servicenow/servicenow/) (version 1.0.6).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install servicenow.servicenow`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory-requirements) for details.
>
> To use it in a playbook, specify: `servicenow.servicenow.now`.

New in servicenow.servicenow 2.10

- [Synopsis](now_inventory.md#synopsis)
- [Requirements](now_inventory.md#requirements)
- [Parameters](now_inventory.md#parameters)
- [Examples](now_inventory.md#examples)

## [Synopsis](now_inventory.md#id1)

- ServiceNow Inventory plugin.

## [Requirements](now_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python requests (requests)
- netaddr

## [Parameters](now_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **enhanced**  boolean | Enable enhanced inventory which provides relationship information from CMDB.  Requires installation of Update Set located in update_sets directory.  **Choices:**   - `false` ← (default) - `true` |
| **enhanced_groups**  boolean | enable enhanced groups from CMDB relationships. Only used if enhanced is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **fields**  list / elements=string | Comma seperated string providing additional table columns to add as host vars to each inventory host.  **Default:** `["ip_address", "fqdn", "host_name", "sys_class_name", "name"]` |
| **filter_results**  string | Filter results with sysparm_query encoded query string syntax. Complete list of operators available for filters and queries.  **Default:** `""` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **host**  string | The ServiceNow hostname.  This value is FQDN for ServiceNow host.  If the value is not specified in the task, the value of environment variable `SN_HOST` will be used instead.  Mutually exclusive with `instance`.  **Configuration:**   - Environment variable: [`SN_HOST`](../../environment_variables.md#envvar-SN_HOST) |
| **instance**  string | The ServiceNow instance name, without the domain, service-now.com.  If the value is not specified in the task, the value of environment variable `SN_INSTANCE` will be used instead.  **Configuration:**   - Environment variable: [`SN_INSTANCE`](../../environment_variables.md#envvar-SN_INSTANCE) |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **password**  string / required | Password for username.  If the value is not specified, the value of environment variable `SN_PASSWORD` will be used instead.  **Configuration:**   - Environment variable: [`SN_PASSWORD`](../../environment_variables.md#envvar-SN_PASSWORD) |
| **plugin**  string / required | The name of the ServiceNow Inventory Plugin, this should always be ‘servicenow.servicenow.now’.  **Choices:**   - `"servicenow.servicenow.now"` |
| **proxy**  string | Proxy server to use for requests to ServiceNow.  **Default:** `""` |
| **selection_order**  list / elements=string | Comma seperated string providing ability to define selection preference order.  **Default:** `["ip_address", "fqdn", "host_name", "name"]` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **table**  string | The ServiceNow table to query.  **Default:** `"cmdb_ci_server"` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **username**  string | Name of user for connection to ServiceNow.  If the value is not specified, the value of environment variable `SN_USERNAME` will be used instead.  **Configuration:**   - Environment variable: [`SN_USERNAME`](../../environment_variables.md#envvar-SN_USERNAME) |

## [Examples](now_inventory.md#id4)

```yaml+jinja
# Simple Inventory Plugin example
plugin: servicenow.servicenow.now
instance: dev89007
username: admin
password: password
keyed_groups:
  - key: sn_sys_class_name | lower
    prefix: ''
    separator: ''

# Using Keyed Groups
plugin: servicenow.servicenow.now
host: servicenow.mydomain.com
username: admin
password: password
fields: [name,host_name,fqdn,ip_address,sys_class_name, install_status, classification,vendor]
keyed_groups:
  - key: sn_classification | lower
    prefix: 'env'
  - key: sn_vendor | lower
    prefix: ''
    separator: ''
  - key: sn_sys_class_name | lower
    prefix: ''
    separator: ''
  - key: sn_install_status | lower
    prefix: 'status'

# Compose hostvars
plugin: servicenow.servicenow.now
instance: dev89007
username: admin
password: password
fields:
  - name
  - sys_tags
compose:
  sn_tags: sn_sys_tags.replace(" ", "").split(',')
  ansible_host: sn_ip_address
keyed_groups:
  - key: sn_tags | lower
    prefix: 'tag'
```

### Authors

- Will Tome (@willtome)
- Alex Mittell (@alex_mittell)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ServiceNowITOM/servicenow-ansible/issues)
- [Repository (Sources)](https://github.com/ServiceNowITOM/servicenow-ansible)
