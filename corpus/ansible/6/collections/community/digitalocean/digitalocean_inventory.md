---
collection: ansible
version: "6"
title: "community.digitalocean.digitalocean inventory – DigitalOcean Inventory Plugin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digitalocean_inventory.html
fetched_at: 2026-07-27T17:07:00+00:00
---
# community.digitalocean.digitalocean inventory – DigitalOcean Inventory Plugin

> **Note:**
>
> This inventory plugin is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digitalocean`.

New in community.digitalocean 1.1.0

- [Synopsis](digitalocean_inventory.md#synopsis)
- [Parameters](digitalocean_inventory.md#parameters)
- [Examples](digitalocean_inventory.md#examples)

## [Synopsis](digitalocean_inventory.md#id3)

- DigitalOcean (DO) inventory plugin.
- Acquires droplet list from DO API.
- Uses configuration file that ends with ‘(do_hosts|digitalocean|digital_ocean).(yaml|yml)’.

## [Parameters](digitalocean_inventory.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_token**  aliases: oauth_token  string / required | DigitalOcean OAuth token.  Template expressions can be used in this field.  Configuration:   - Environment variable: [`DO_API_TOKEN`](../../environment_variables.md#envvar-DO_API_TOKEN) |
| **attributes**  list / elements=string | Droplet attributes to add as host vars to each inventory host. Check out the DO API docs for full list of attributes at <https://docs.digitalocean.com/reference/api/api-reference/#operation/list_all_droplets>.  Default: `["id", "name", "networks", "region", "size_slug"]` |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  Default: `"memory"`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  Default: `"ansible_inventory_"`  Configuration:   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  Default: `3600`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **filters**  list / elements=string  added in community.digitalocean 1.5.0 | Filter hosts with Jinja templates.  If no filters are specified, all hosts are added to the inventory.  Default: `[]` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **pagination**  integer | Maximum droplet objects per response page.  If the number of droplets related to the account exceeds this value, the query will be broken to multiple requests (pages).  DigitalOcean currently allows a maximum of 200.  Default: `200` |
| **plugin**  string / required | The name of the DigitalOcean Inventory Plugin, this should always be `community.digitalocean.digitalocean`.  Choices:   - `"community.digitalocean.digitalocean"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **var_prefix**  string | Prefix of generated varible names (e.g. `tags` -> `do_tags`)  Default: `"do_"` |

## [Examples](digitalocean_inventory.md#id5)

```yaml+jinja
# Using keyed groups and compose for hostvars
plugin: community.digitalocean.digitalocean
api_token: '{{ lookup("pipe", "./get-do-token.sh" }}'
attributes:
  - id
  - name
  - memory
  - vcpus
  - disk
  - size
  - image
  - networks
  - volume_ids
  - tags
  - region
keyed_groups:
  - key: do_region.slug
    prefix: 'region'
    separator: '_'
  - key: do_tags | lower
    prefix: ''
    separator: ''
compose:
  ansible_host: do_networks.v4 | selectattr('type','eq','public')
    | map(attribute='ip_address') | first
  class: do_size.description | lower
  distro: do_image.distribution | lower
filters:
  - '"kubernetes" in do_tags'
  - 'do_region.slug == "fra1"'
```

### Authors

- Janos Gerzson (@grzs)
- Tadej Borovšak (@tadeboro)
- Max Truxa (@maxtruxa)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
