---
collection: ansible
version: "8"
title: "vultr.cloud.vultr inventory – Retrieves list of instances via Vultr v2 API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/vultr_inventory.html
fetched_at: 2026-07-28T01:06:02+00:00
---
# vultr.cloud.vultr inventory – Retrieves list of instances via Vultr v2 API

> **Note:**
>
> This inventory plugin is part of the [vultr.cloud collection](https://galaxy.ansible.com/ui/repo/published/vultr/cloud/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.vultr`.

New in vultr.cloud 1.4.0

- [Synopsis](vultr_inventory.md#synopsis)
- [Parameters](vultr_inventory.md#parameters)
- [Notes](vultr_inventory.md#notes)
- [Examples](vultr_inventory.md#examples)

## [Synopsis](vultr_inventory.md#id1)

- Vultr inventory plugin.
- Retrieves list of instances via Vultr v2 API.
- Configuration of this plugin is done with files ending with ‘(vultr|vultr_hosts|vultr_instances).(yaml|yml)’

## [Parameters](vultr_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"`  **Configuration:**   - Environment variable: [`VULTR_API_ENDPOINT`](../../environment_variables.md#envvar-VULTR_API_ENDPOINT) |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`.  **Configuration:**   - Environment variable: [`VULTR_API_KEY`](../../environment_variables.md#envvar-VULTR_API_KEY) |
| **api_results_per_page**  integer | When receiving large numbers of instances, specify how many instances should be returned per call to API.  This does not determine how many results are returned; all instances are returned according to other filters.  Vultr API maximum is 500.  Fallback environment variable `VULTR_API_RESULTS_PER_PAGE`.  **Default:** `100`  **Configuration:**   - Environment variable: [`VULTR_API_RESULTS_PER_PAGE`](../../environment_variables.md#envvar-VULTR_API_RESULTS_PER_PAGE) |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `60`  **Configuration:**   - Environment variable: [`VULTR_API_TIMEOUT`](../../environment_variables.md#envvar-VULTR_API_TIMEOUT) |
| **attributes**  list / elements=string | Instance attributes to add as host variables to each host added to inventory.  See <https://www.vultr.com/api/#operation/list-instances> for valid values.  The *internal_ip* attribute was added in version 1.10.0.  **Default:** `["id", "region", "label", "plan", "hostname", "main_ip", "v6_main_ip", "tags", "internal_ip"]` |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **filters**  list / elements=string | Filter hosts with Jinja2 templates.  If not provided, all hosts are added to inventory.  **Default:** `[]` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **instance_type**  string  *added in vultr.cloud 1.8.0* | Type of instance.  **Choices:**   - `"cloud"` ← (default) - `"bare_metal"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | Name of Vultr inventory plugin.  This should always be `vultr.cloud.vultr`.  **Choices:**   - `"vultr.cloud.vultr"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |
| **variable_prefix**  string | Prefix of generated variables (e.g. `id` becomes `vultr_id`).  **Default:** `"vultr_"` |

## [Notes](vultr_inventory.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_inventory.md#id4)

```yaml+jinja
---
# File endings vultr{,_{hosts,instances}}.y{,a}ml
# All configuration done via environment variables:
plugin: vultr.cloud.vultr

# Grouping and filtering configuration in inventory file
plugin: vultr.cloud.vultr
api_key: '{{ lookup("pipe"), "./get_vultr_api_key.sh" }}'
keyed_groups:
  - key: vultr_tags | lower
    prefix: ''
    separator: ''
filters:
  - '"vpc" in vultr_tags'
  - 'vultr_plan == "vc2-2c-4gb"'

# Unless you can connect to your servers via it's vultr label,
# we suggest setting ansible_host with compose:
plugin: vultr.cloud.vultr
compose:
  ansible_host: vultr_main_ip

# Respectively for IPv6:
plugin: vultr.cloud.vultr
compose:
  ansible_host: vultr_v6_main_ip

# Prioritize IPv6 over IPv4 if available.
plugin: vultr.cloud.vultr
compose:
  ansible_host: vultr_v6_main_ip or vultr_main_ip

# Use the internal IP
plugin: vultr.cloud.vultr
compose:
  ansible_host: vultr_internal_ip

# Querying the bare metal instances
plugin: vultr.cloud.vultr
instance_type: bare_metal
```

### Authors

- jasites (@jasites)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
