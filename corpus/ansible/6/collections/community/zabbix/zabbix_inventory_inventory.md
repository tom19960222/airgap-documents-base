---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_inventory inventory – Zabbix Inventory Plugin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_inventory_inventory.html
fetched_at: 2026-07-27T16:43:25+00:00
---
# community.zabbix.zabbix_inventory inventory – Zabbix Inventory Plugin

> **Note:**
>
> This inventory plugin is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_inventory`.

New in community.zabbix 1.4.0

- [Synopsis](zabbix_inventory_inventory.md#synopsis)
- [Requirements](zabbix_inventory_inventory.md#requirements)
- [Parameters](zabbix_inventory_inventory.md#parameters)
- [Examples](zabbix_inventory_inventory.md#examples)

## [Synopsis](zabbix_inventory_inventory.md#id1)

- Zabbix Inventory plugin
- All vars from zabbix are prefixed with zbx_

## [Requirements](zabbix_inventory_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.6
- zabbix-api >= 0.5.4

## [Parameters](zabbix_inventory_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_zabbix_groups**  boolean | If set to True, hosts will be added to groups based on their zabbix groups  Choices:   - `false` ← (default) - `true` |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  Default: `"memory"`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  Default: `"ansible_inventory_"`  Configuration:   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  Default: `3600`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **host_zapi_query**  dictionary | API query for hosts - see zabbix documentation for more details <https://www.zabbix.com/documentation/current/manual/api/reference/host/get>  Default: `{}` |
| **selectApplications**  string | query  Return an applications property with host applications.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/application/object> for more details on field names |
| **selectDashboards**  string | query  Return a dashboards property.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/templatedashboard/object> for more details on field names |
| **selectDiscoveries**  string | query  Return a discoveries property with host low-level discovery rules.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/discoveryrule/object> for more details on field names |
| **selectDiscoveryRule**  string | query  Return a discoveryRule property with the low-level discovery rule that created the host (from host prototype in VMware monitoring).  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  please see <https://www.zabbix.com/documentation/current/manual/api/reference/discoveryrule/object> for more details on field names |
| **selectGraphs**  string | query  Return a discoveries property with host low-level discovery rules.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/graph/object> for more details on field names |
| **selectGroups**  string | query  Return a groups property with host groups data that the host belongs to.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/hostgroup/object> for more details on field names |
| **selectHostDiscovery**  string | query  Return a hostDiscovery property with host discovery object data.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/host/get> for more details on field names |
| **selectHttpTests**  string | query  Return an httpTests property with host web scenarios.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/httptest/object> for more details on field names |
| **selectInheritedTags**  string | query  Return an inheritedTags property with tags that are on all templates which are linked to host.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/host/object#host_tag> for more details on field names |
| **selectInterfaces**  string | query  Return an interfaces property with host interfaces.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/hostinterface/object> for more details on field names |
| **selectInventory**  string | query  Return an inventory property with host inventory data.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/host/object#host_inventory> for more details on field names |
| **selectItems**  string | query  Return an items property with host items.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/item/object> for more details on field names |
| **selectMacros**  string | query  Return a macros property with host macros.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/usermacro/object> for more details on field names |
| **selectParentTemplates**  string | query  Return a parentTemplates property with templates that the host is linked to  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/template/object> for more details on field names |
| **selectTags**  string | query  Return a tags property with host tags.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/host/object#host_tag> for more details on field names |
| **selectTriggers**  string | query  Return a triggers property with host triggers.  To return all values specify ‘extend’  Can be limited to different fields for example setting the vaule to [‘name’] will only return the name  Additional fields can be specified by comma seperated value [‘name’, ‘field2’]  Please see <https://www.zabbix.com/documentation/current/manual/api/reference/host/object#host_tag> for more details on field names |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **login_password**  string / required | Zabbix user password.  Configuration:   - Environment variable: [`ZABBIX_PASSWORD`](../../environment_variables.md#envvar-ZABBIX_PASSWORD) |
| **login_user**  string / required | Zabbix user name.  Configuration:   - Environment variable: [`ZABBIX_USERNAME`](../../environment_variables.md#envvar-ZABBIX_USERNAME) |
| **proxy**  string | Proxy server to use for reaching zabbix API  Default: `""` |
| **server_url**  aliases: url  string / required | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  Configuration:   - Environment variable: [`ZABBIX_SERVER`](../../environment_variables.md#envvar-ZABBIX_SERVER) |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | The timeout of API request (seconds).  Default: `10` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default)   Configuration:   - Environment variable: [`ZABBIX_VALIDATE_CERTS`](../../environment_variables.md#envvar-ZABBIX_VALIDATE_CERTS) |

## [Examples](zabbix_inventory_inventory.md#id4)

```yaml+jinja
# Simple Inventory Plugin example
# This will create an inventory with details from zabbix such as applications name, applicaitonids, Parent Template Name, and group membership name
#It will also create 2 ansible inventory groups for enabled and disabled hosts in zabbix based on the status field.
plugin: community.zabbix.zabbix_inventory
server_url: https://zabbix.com
login_user: Admin
login_password: password
host_zapi_query:
  selectApplications: ['name', 'applicationid']
  selectParentTemplates: ['name']
  selectGroups: ['name']
validate_certs: false
groups:
  enabled: zbx_status == "0"
  disabled: zbx_status == "1"

#Using Keyed Groups
plugin: community.zabbix.zabbix_inventory
server_url: https://zabbix.com
login_user: Admin
login_password: password
validate_certs: false
keyed_groups:
  - key: zbx_status | lower
    prefix: 'env'
  - key: zbx_description | lower
    prefix: 'test'
    separator: ''

#Using proxy format of proxy is 'http://<user>:<pass>@<proxy>:<port>' or 'http://<proxy>:<port>'
plugin: community.zabbix.zabbix_inventory
server_url: https://zabbix.com
proxy: http://someproxy:8080
login_user: Admin
login_password: password
validate_certs: false

#Organize inventory groups based on zabbix host groups
plugin: community.zabbix.zabbix_inventory
server_url: https://zabbix.com
add_zabbix_groups: true
login_user: Admin
login_password: password
validate_certs: false

#Using compose to modify vars
plugin: community.zabbix.zabbix_inventory
server_url: https://zabbix.com
login_user: Admin
login_password: password
validate_certs: false
compose:
  zbx_testvar: zbx_status.replace("1", "Disabled")
```

### Authors

- Timothy Test (@ttestscripting)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
