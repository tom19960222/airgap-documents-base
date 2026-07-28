---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt inventory – oVirt inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_inventory.html
fetched_at: 2026-07-28T02:50:33+00:00
---
# ovirt.ovirt.ovirt inventory – oVirt inventory source

> **Note:**
>
> This inventory plugin is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_inventory.md#synopsis)
- [Requirements](ovirt_inventory.md#requirements)
- [Parameters](ovirt_inventory.md#parameters)
- [Examples](ovirt_inventory.md#examples)

## [Synopsis](ovirt_inventory.md#id1)

- Get inventory hosts from the ovirt service.
- Requires a YAML file ending in ‘ovirt.yml’, ‘ovirt4.yml’, ‘ovirt.yaml’, ‘ovirt4.yaml’.

## [Requirements](ovirt_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- ovirt-engine-sdk-python >= 4.2.4

## [Parameters](ovirt_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **ovirt_cafile**  string | path to ovirt-engine CA file. If `ovirt_cafile` parameter is not set and `ovirt_insecure` is not True, system wide CA certificate store is used. |
| **ovirt_hostname_preference**  list / elements=string | List of options that describe the ordering for which hostnames should be assigned.  See <https://ovirt.github.io/ovirt-engine-api-model/master/#types/vm> for available attributes.  **Default:** `["fqdn", "name"]` |
| **ovirt_insecure**  string | A boolean flag that indicates if the server TLS certificate and host name should be checked. |
| **ovirt_password**  string / required | ovirt authentication password.  **Configuration:**   - Environment variable: [`OVIRT_PASSWORD`](../../environment_variables.md#envvar-OVIRT_PASSWORD) |
| **ovirt_query_filter**  string | dictionary of filter key-values to query VM’s. See <https://ovirt.github.io/ovirt-engine-sdk/master/services.m.html#ovirtsdk4.services.VmsService.list> for filter parameters. |
| **ovirt_url**  string / required | URL to ovirt-engine API.  **Configuration:**   - Environment variable: [`OVIRT_URL`](../../environment_variables.md#envvar-OVIRT_URL) |
| **ovirt_username**  string / required | ovirt authentication user.  **Configuration:**   - Environment variable: [`OVIRT_USERNAME`](../../environment_variables.md#envvar-OVIRT_USERNAME) |
| **plugin**  string / required | the name of this plugin, it should always be set to ‘ovirt’ for this plugin to recognise it as it’s own.  **Choices:**   - `"ovirt"` - `"ovirt.ovirt.ovirt"` - `"redhat.rhv.ovirt"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](ovirt_inventory.md#id4)

```yaml+jinja
# Ensure the CA is available:
# $ wget "https://engine/ovirt-engine/services/pki-resource?resource=ca-certificate&format=X509-PEM-CA" -O /path/to/ca.pem
# Sample content of ovirt.yml:
plugin: ovirt.ovirt.ovirt
ovirt_url: https://engine/ovirt-engine/api
ovirt_cafile: /path/to/ca.pem
ovirt_username: ansible-tester
ovirt_password: secure
ovirt_query_filter:
  search: 'name=myvm AND cluster=mycluster'
  case_sensitive: no
  max: 15
keyed_groups:
  - key: cluster
    prefix: 'cluster'
groups:
  dev: "'dev' in tags"
compose:
  ansible_host: devices["eth0"][0]
```

### Authors

- Bram Verschueren (@bverschueren)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
