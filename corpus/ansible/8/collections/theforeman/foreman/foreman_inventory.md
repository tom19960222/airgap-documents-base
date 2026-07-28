---
collection: ansible
version: "8"
title: "theforeman.foreman.foreman inventory – Foreman inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/foreman_inventory.html
fetched_at: 2026-07-28T01:06:00+00:00
---
# theforeman.foreman.foreman inventory – Foreman inventory source

> **Note:**
>
> This inventory plugin is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.foreman`.

- [Synopsis](foreman_inventory.md#synopsis)
- [Requirements](foreman_inventory.md#requirements)
- [Parameters](foreman_inventory.md#parameters)
- [Examples](foreman_inventory.md#examples)

## [Synopsis](foreman_inventory.md#id1)

- Get inventory hosts from Foreman.
- Can use the Reports API (default) or the Hosts API to fetch information about the hosts.
- The Reports API is faster with many hosts.
- The Reports API requires the `foreman_ansible` plugin to be installed on the Foreman server.
- Some options only work when using the Reports API.
- Uses a YAML configuration file that ends with ``foreman.(yml|yaml)``.

## [Requirements](foreman_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- requests >= 1.1

## [Parameters](foreman_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **batch_size**  integer | Number of hosts per batch that will be retrieved from the Foreman API per individual call  **Default:** `250` |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **foreman**  string | Foreman server related configuration, deprecated.  You can pass *use_reports_api* in this dict to enable the Reports API.  Only for backward compatibility. |
| **group_prefix**  string | prefix to apply to foreman groups  **Default:** `"foreman_"` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **host_filters**  string | This can be used to restrict the list of returned host |
| **hostnames**  list / elements=string | A list of templates in order of precedence to compose inventory_hostname.  If the template results in an empty string or None value it is ignored.  **Default:** `["name"]` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **legacy_hostvars**  boolean | Toggle, if true the plugin will build legacy hostvars present in the foreman script  Places hostvars in a dictionary with keys `foreman`, `foreman_facts`, and `foreman_params`  **Choices:**   - `false` ← (default) - `true` |
| **max_timeout**  integer | Timeout before falling back to old host API when using report_data endpoint while polling.  **Default:** `600` |
| **password**  string / required | Password of the user accessing the Foreman server.  **Configuration:**   - Environment variable: [`FOREMAN_PASSWORD`](../../environment_variables.md#envvar-FOREMAN_PASSWORD) |
| **plugin**  string / required | token that ensures this is a source file for the `foreman` plugin.  **Choices:**   - `"theforeman.foreman.foreman"` |
| **poll_interval**  integer | The polling interval between 2 calls to the report_data endpoint while polling.  **Default:** `10` |
| **report**  dictionary | Report API specific configuration, deprecated.  You can pass the Report API specific params as part of this dict, instead of the main configuration.  Only for backward compatibility. |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **url**  string | URL of the Foreman server.  **Default:** `"http://localhost:3000"`  **Configuration:**   - Environment variable: [`FOREMAN_SERVER`](../../environment_variables.md#envvar-FOREMAN_SERVER) - Environment variable: [`FOREMAN_SERVER_URL`](../../environment_variables.md#envvar-FOREMAN_SERVER_URL) - Environment variable: [`FOREMAN_URL`](../../environment_variables.md#envvar-FOREMAN_URL) |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_reports_api**  boolean | Use Reports API.  **Choices:**   - `false` - `true` ← (default) |
| **user**  string / required | Username accessing the Foreman server.  **Configuration:**   - Environment variable: [`FOREMAN_USER`](../../environment_variables.md#envvar-FOREMAN_USER) - Environment variable: [`FOREMAN_USERNAME`](../../environment_variables.md#envvar-FOREMAN_USERNAME) |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Environment variable: [`FOREMAN_VALIDATE_CERTS`](../../environment_variables.md#envvar-FOREMAN_VALIDATE_CERTS) |
| **vars_prefix**  string | prefix to apply to host variables, does not include facts nor params  **Default:** `"foreman_"` |
| **want_content_facet_attributes**  boolean | Toggle, if true the inventory will fetch content view details that the host is tied to.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_facts**  boolean | Toggle, if True the plugin will retrieve host facts from the server  **Choices:**   - `false` ← (default) - `true` |
| **want_host_group**  boolean | Toggle, if true the inventory will fetch host_groups and create groupings for the same.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_hostcollections**  boolean | Toggle, if true the plugin will create Ansible groups for host collections  **Choices:**   - `false` ← (default) - `true` |
| **want_ipv4**  boolean | Toggle, if true the inventory will fetch ipv4 address of the host.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_ipv6**  boolean | Toggle, if true the inventory will fetch ipv6 address of the host.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_location**  boolean | Toggle, if true the inventory will fetch location the host belongs to and create groupings for the same.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_organization**  boolean | Toggle, if true the inventory will fetch organization the host belongs to and create groupings for the same.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_params**  boolean | Toggle, if true the inventory will retrieve ‘all_parameters’ information as host vars  **Choices:**   - `false` ← (default) - `true` |
| **want_smart_proxies**  boolean | Toggle, if true the inventory will fetch smart proxy that the host is registered to.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_subnet**  boolean | Toggle, if true the inventory will fetch subnet.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |
| **want_subnet_v6**  boolean | Toggle, if true the inventory will fetch ipv6 subnet.  Only applies to inventories using the Reports API - attribute is ignored otherwise.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](foreman_inventory.md#id4)

```yaml+jinja
# my.foreman.yml
plugin: theforeman.foreman.foreman
url: https://foreman.example.com
user: ansibleinventory
password: changeme
host_filters: 'organization="Web Engineering"'

# shortname.foreman.yml
plugin: theforeman.foreman.foreman
url: https://foreman.example.com
user: ansibleinventory
password: changeme
hostnames:
  - name.split('.')[0]
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
