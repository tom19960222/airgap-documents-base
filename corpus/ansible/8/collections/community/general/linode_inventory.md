---
collection: ansible
version: "8"
title: "community.general.linode inventory – Ansible dynamic inventory plugin for Linode."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/linode_inventory.html
fetched_at: 2026-07-28T01:52:32+00:00
---
# community.general.linode inventory – Ansible dynamic inventory plugin for Linode.

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](linode_inventory.md#ansible-collections-community-general-linode-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.general.linode`.

- [Synopsis](linode_inventory.md#synopsis)
- [Requirements](linode_inventory.md#requirements)
- [Parameters](linode_inventory.md#parameters)
- [Examples](linode_inventory.md#examples)

## [Synopsis](linode_inventory.md#id1)

- Reads inventories from the Linode API v4.
- Uses a YAML configuration file that ends with linode.(yml|yaml).
- Linode labels are used by default as the hostnames.
- The default inventory groups are built from groups (deprecated by Linode) and not tags.

## [Requirements](linode_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.7
- linode_api4 >= 2.0.0

## [Parameters](linode_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string / required | The Linode account personal access token.  **Configuration:**   - Environment variable: [`LINODE_ACCESS_TOKEN`](../../environment_variables.md#envvar-LINODE_ACCESS_TOKEN) |
| **cache**  boolean  *added in community.general 4.5.0* | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string  *added in community.general 4.5.0* | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string  *added in community.general 4.5.0* | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string  *added in community.general 4.5.0* | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer  *added in community.general 4.5.0* | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary  *added in community.general 2.0.0* | Create vars from jinja2 expressions.  **Default:** `{}` |
| **groups**  dictionary  *added in community.general 2.0.0* | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **ip_style**  string  *added in community.general 3.6.0* | Populate hostvars with all information available from the Linode APIv4.  **Choices:**   - `"plain"` ← (default) - `"api"` |
| **keyed_groups**  list / elements=dictionary  *added in community.general 2.0.0* | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | Marks this as an instance of the ‘linode’ plugin.  **Choices:**   - `"linode"` - `"community.general.linode"` |
| **regions**  list / elements=string | Populate inventory with instances in this region.  **Default:** `[]` |
| **strict**  boolean  *added in community.general 2.0.0* | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **tags**  list / elements=string  *added in community.general 2.0.0* | Populate inventory only with instances which have at least one of the tags listed here.  **Default:** `[]` |
| **types**  list / elements=string | Populate inventory with instances with this type.  **Default:** `[]` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](linode_inventory.md#id4)

```yaml+jinja
# Minimal example. `LINODE_ACCESS_TOKEN` is exposed in environment.
plugin: community.general.linode

# You can use Jinja to template the access token.
plugin: community.general.linode
access_token: "{{ lookup('ini', 'token', section='your_username', file='~/.config/linode-cli') }}"
# For older Ansible versions, you need to write this as:
# access_token: "{{ lookup('ini', 'token section=your_username file=~/.config/linode-cli') }}"

# Example with regions, types, groups and access token
plugin: community.general.linode
access_token: foobar
regions:
  - eu-west
types:
  - g5-standard-2

# Example with keyed_groups, groups, and compose
plugin: community.general.linode
access_token: foobar
keyed_groups:
  - key: tags
    separator: ''
  - key: region
    prefix: region
groups:
  webservers: "'web' in (tags|list)"
  mailservers: "'mail' in (tags|list)"
compose:
  # By default, Ansible tries to connect to the label of the instance.
  # Since that might not be a valid name to connect to, you can
  # replace it with the first IPv4 address of the linode as follows:
  ansible_ssh_host: ipv4[0]
  ansible_port: 2222

# Example where control traffic limited to internal network
plugin: community.general.linode
access_token: foobar
ip_style: api
compose:
  ansible_host: "ipv4 | community.general.json_query('[?public==`false`].address') | first"
```

### Authors

- Luke Murphy (@decentral1se)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
