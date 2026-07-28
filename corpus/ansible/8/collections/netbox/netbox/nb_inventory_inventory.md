---
collection: ansible
version: "8"
title: "netbox.netbox.nb_inventory inventory – NetBox inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/nb_inventory_inventory.html
fetched_at: 2026-07-28T02:45:39+00:00
---
# netbox.netbox.nb_inventory inventory – NetBox inventory source

> **Note:**
>
> This inventory plugin is part of the [netbox.netbox collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
>
> To use it in a playbook, specify: `netbox.netbox.nb_inventory`.

- [Synopsis](nb_inventory_inventory.md#synopsis)
- [Parameters](nb_inventory_inventory.md#parameters)
- [Examples](nb_inventory_inventory.md#examples)

## [Synopsis](nb_inventory_inventory.md#id1)

- Get inventory hosts from NetBox

## [Parameters](nb_inventory_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **ansible_host_dns_name**  boolean | If True, sets DNS Name (fetched from primary_ip) to be used in ansible_host variable, instead of IP Address.  **Choices:**   - `false` ← (default) - `true` |
| **api_endpoint**  string / required | Endpoint of the NetBox API  **Configuration:**   - Environment variable: [`NETBOX_API`](../../environment_variables.md#envvar-NETBOX_API) |
| **ca_path**  string | CA path  **Default:** `false` |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **cert**  string | Certificate path  **Default:** `false` |
| **compose**  dictionary | List of custom ansible host vars to create from the device object fetched from NetBox  **Default:** `{}` |
| **config_context**  boolean | If True, it adds config_context in host vars.  Config-context enables the association of arbitrary data to devices and virtual machines grouped by region, site, role, platform, and/or tenant. Please check official netbox docs for more info.  **Choices:**   - `false` ← (default) - `true` |
| **device_query_filters**  list / elements=string | List of parameters passed to the query string for devices (Multiple values may be separated by commas).  You can also use Jinja2 templates.  **Default:** `[]` |
| **dns_name**  boolean | Force IP Addresses to be fetched so that the dns_name for the primary_ip of each device or VM is set as a host_var.  Setting interfaces will also fetch IP addresses and the dns_name host_var will be set.  **Choices:**   - `false` ← (default) - `true` |
| **fetch_all**  boolean  *added in netbox.netbox 0.2.1* | By default, fetching interfaces and services will get all of the contents of NetBox regardless of query_filters applied to devices and VMs.  When set to False, separate requests will be made fetching interfaces, services, and IP addresses for each device_id and virtual_machine_id.  If you are using the various query_filters options to reduce the number of devices, you may find querying NetBox faster with fetch_all set to False.  For efficiency, when False, these requests will be batched, for example /api/dcim/interfaces?limit=0&device_id=1&device_id=2&device_id=3  These GET request URIs can become quite large for a large number of devices. If you run into HTTP 414 errors, you can adjust the max_uri_length option to suit your web server.  **Choices:**   - `false` - `true` ← (default) |
| **flatten_config_context**  boolean  *added in netbox.netbox 0.2.1* | If *config_context* is enabled, by default it’s added as a host var named config_context.  If flatten_config_context is set to True, the config context variables will be added directly to the host instead.  **Choices:**   - `false` ← (default) - `true` |
| **flatten_custom_fields**  boolean  *added in netbox.netbox 0.2.1* | By default, host custom fields are added as a dictionary host var named custom_fields.  If flatten_custom_fields is set to True, the fields will be added directly to the host instead.  **Choices:**   - `false` ← (default) - `true` |
| **flatten_local_context_data**  boolean  *added in netbox.netbox 0.3.0* | If *local_context_data* is enabled, by default it’s added as a host var named local_context_data.  If flatten_local_context_data is set to True, the config context variables will be added directly to the host instead.  **Choices:**   - `false` ← (default) - `true` |
| **follow_redirects**  string | Determine how redirects are followed.  By default, *follow_redirects* is set to uses urllib2 default behavior.  **Choices:**   - `"urllib2"` ← (default) - `"all"` - `"yes"` - `"safe"` - `"none"` |
| **group_by**  list / elements=string | Keys used to create groups. The *plurals* and *racks* options control which of these are valid.  *rack_group* is supported on NetBox versions 2.10 or lower only  *location* is supported on NetBox versions 2.11 or higher only  **Choices:**   - `"sites"` - `"site"` - `"location"` - `"tenants"` - `"tenant"` - `"racks"` - `"rack"` - `"rack_group"` - `"rack_role"` - `"tags"` - `"tag"` - `"device_roles"` - `"role"` - `"device_types"` - `"device_type"` - `"manufacturers"` - `"manufacturer"` - `"platforms"` - `"platform"` - `"region"` - `"site_group"` - `"cluster"` - `"cluster_type"` - `"cluster_group"` - `"is_virtual"` - `"services"` - `"status"` - `"time_zone"` - `"utc_offset"`   **Default:** `[]` |
| **group_names_raw**  boolean  *added in netbox.netbox 0.2.0* | Will not add the group_by choice name to the group names  **Choices:**   - `false` ← (default) - `true` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **interfaces**  boolean  *added in netbox.netbox 0.1.7* | If True, it adds the device or virtual machine interface information in host vars.  **Choices:**   - `false` ← (default) - `true` |
| **key**  string | Certificate key path  **Default:** `false` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **max_uri_length**  integer  *added in netbox.netbox 0.2.1* | When fetch_all is False, GET requests to NetBox may become quite long and return a HTTP 414 (URI Too Long).  You can adjust this option to be smaller to avoid 414 errors, or larger for a reduced number of requests.  **Default:** `4000` |
| **plugin**  string / required | token that ensures this is a source file for the ‘netbox’ plugin.  **Choices:**   - `"netbox.netbox.nb_inventory"` |
| **plurals**  boolean  *added in netbox.netbox 0.2.1* | If True, all host vars are contained inside single-element arrays for legacy compatibility with old versions of this plugin.  Group names will be plural (ie. “sites_mysite” instead of “site_mysite”)  The choices of *group_by* will be changed by this option.  **Choices:**   - `false` - `true` ← (default) |
| **prefixes**  boolean  *added in netbox.netbox 3.5.0* | If True, it adds the device or virtual machine prefixes to hostvars nested under “site”.  Must match selection for “site_data”, as this changes the structure of “site” in hostvars  **Choices:**   - `false` ← (default) - `true` |
| **query_filters**  list / elements=string | List of parameters passed to the query string for both devices and VMs (Multiple values may be separated by commas).  You can also use Jinja2 templates.  **Default:** `[]` |
| **racks**  boolean  *added in netbox.netbox 3.6.0* | If False, skip querying the racks for information, which can be slow with great amounts of racks.  The choices of *group_by* will be changed by this option.  **Choices:**   - `false` - `true` ← (default) |
| **services**  boolean  *added in netbox.netbox 0.2.0* | If True, it adds the device or virtual machine services information in host vars.  **Choices:**   - `false` - `true` ← (default) |
| **site_data**  boolean  *added in netbox.netbox 3.5.0* | If True, sites’ full data structures returned from Netbox API are included in host vars.  **Choices:**   - `false` ← (default) - `true` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | Timeout for NetBox requests in seconds  **Default:** `60` |
| **token**  string | NetBox API token to be able to read against NetBox.  This may not be required depending on the NetBox setup.  You can provide a “type” and “value” for a token if your NetBox deployment is using a more advanced authentication like OAUTH.  If you do not provide a “type” and “value” parameter, the HTTP authorization header will be set to “Token”, which is the NetBox default  **Configuration:**   - Environment variable: [`NETBOX_TOKEN`](../../environment_variables.md#envvar-NETBOX_TOKEN) - Environment variable: [`NETBOX_API_KEY`](../../environment_variables.md#envvar-NETBOX_API_KEY) |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  **Choices:**   - `false` - `true` ← (default) |
| **virtual_chassis_name**  boolean | When a device is part of a virtual chassis, use the virtual chassis name as the Ansible inventory hostname.  The host var values will be from the virtual chassis master.  **Choices:**   - `false` ← (default) - `true` |
| **vm_query_filters**  list / elements=string | List of parameters passed to the query string for VMs (Multiple values may be separated by commas).  You can also use Jinja2 templates.  **Default:** `[]` |

## [Examples](nb_inventory_inventory.md#id3)

```yaml+jinja
# netbox_inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i netbox_inventory.yml

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
validate_certs: True
config_context: False
group_by:
  - device_roles
query_filters:
  - role: network-edge-router
device_query_filters:
  - has_primary_ip: 'true'
  - tenant__n: internal

# has_primary_ip is a useful way to filter out patch panels and other passive devices
# Adding '__n' to a field searches for the negation of the value.
# The above searches for devices that are NOT "tenant = internal"

# Query filters are passed directly as an argument to the fetching queries.
# You can repeat tags in the query string.

query_filters:
  - role: server
  - tag: web
  - tag: production

# See the NetBox documentation at https://netbox.readthedocs.io/en/stable/rest-api/overview/
# the query_filters work as a logical **OR**
#
# Prefix any custom fields with cf_ and pass the field value with the regular NetBox query string

query_filters:
  - cf_foo: bar

# NetBox inventory plugin also supports Constructable semantics
# You can fill your hosts vars using the compose option:

plugin: netbox.netbox.nb_inventory
compose:
  foo: last_updated
  bar: display_name
  nested_variable: rack.display_name

# You can use keyed_groups to group on properties of devices or VMs.
# NOTE: It's only possible to key off direct items on the device/VM objects.
plugin: netbox.netbox.nb_inventory
keyed_groups:
  - prefix: status
    key: status.value

# For use in Ansible Tower (AWX), please see this blog from RedHat: https://www.ansible.com/blog/using-an-inventory-plugin-from-a-collection-in-ansible-tower
# The credential for NetBox will need to expose NETBOX_API and NETBOX_TOKEN as environment variables.
# Example Ansible Tower credential Input Configuration:

fields:
  - id: NETBOX_API
    type: string
    label: NetBox Host URL
  - id: NETBOX_TOKEN
    type: string
    label: NetBox API Token
    secret: true
required:
  - NETBOX_API
  - NETBOX_TOKEN

# Example Ansible Tower credential Injector Configuration:

env:
  NETBOX_API: '{{ NETBOX_API }}'
  NETBOX_TOKEN: '{{ NETBOX_TOKEN }}'

# Example of time_zone and utc_offset usage

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
token: <insert token>
validate_certs: True
config_context: True
group_by:
  - site
  - role
  - time_zone
  - utc_offset
device_query_filters:
  - has_primary_ip: 'true'
  - manufacturer_id: 1

# using group by time_zone, utc_offset it will group devices in ansible groups depending on time zone configured on site.
# time_zone gives grouping like:
# - "time_zone_Europe_Bucharest"
# - "time_zone_Europe_Copenhagen"
# - "time_zone_America_Denver"
# utc_offset gives grouping like:
# - "time_zone_utc_minus_7"
# - "time_zone_utc_plus_1"
# - "time_zone_utc_plus_10"

# Example of using a token type

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
token:
  type: Bearer
  value: test123456
```

### Authors

- Remy Leone (@sieben)
- Anthony Ruhier (@Anthony25)
- Nikhil Singh Baliyan (@nikkytub)
- Sander Steffann (@steffann)
- Douglas Heriot (@DouglasHeriot)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
