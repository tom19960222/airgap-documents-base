---
collection: ansible
version: "8"
title: "community.general.nmap inventory – Uses nmap to find hosts to target"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nmap_inventory.html
fetched_at: 2026-07-28T01:52:34+00:00
---
# community.general.nmap inventory – Uses nmap to find hosts to target

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
> see [Requirements](nmap_inventory.md#ansible-collections-community-general-nmap-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.general.nmap`.

- [Synopsis](nmap_inventory.md#synopsis)
- [Requirements](nmap_inventory.md#requirements)
- [Parameters](nmap_inventory.md#parameters)
- [Notes](nmap_inventory.md#notes)
- [Examples](nmap_inventory.md#examples)

## [Synopsis](nmap_inventory.md#id1)

- Uses a YAML configuration file with a valid YAML extension.

## [Requirements](nmap_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- nmap CLI installed

## [Parameters](nmap_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | Network IP or range of IPs to scan, you can use a simple range (10.2.2.15-25) or CIDR notation.  **Configuration:**   - Environment variable: [`ANSIBLE_NMAP_ADDRESS`](../../environment_variables.md#envvar-ANSIBLE_NMAP_ADDRESS)  *added in community.general 6.6.0* |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **dns_resolve**  boolean  *added in community.general 6.1.0* | Whether to always (`true`) or never (`false`) do DNS resolution.  **Choices:**   - `false` ← (default) - `true` |
| **exclude**  list / elements=string | List of addresses to exclude.  For example `10.2.2.15-25` or `10.2.2.15,10.2.2.16`.  **Configuration:**   - Environment variable: [`ANSIBLE_NMAP_EXCLUDE`](../../environment_variables.md#envvar-ANSIBLE_NMAP_EXCLUDE)  *added in community.general 6.6.0* |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **icmp_timestamp**  boolean  *added in community.general 6.1.0* | Scan via ICMP Timestamp (`-PP`).  Depending on your system you might need `sudo=true` for this to work.  **Choices:**   - `false` ← (default) - `true` |
| **ipv4**  boolean | use IPv4 type addresses  **Choices:**   - `false` - `true` ← (default) |
| **ipv6**  boolean | use IPv6 type addresses  **Choices:**   - `false` - `true` ← (default) |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **open**  boolean  *added in community.general 6.5.0* | Only scan for open (or possibly open) ports.  **Choices:**   - `false` ← (default) - `true` |
| **plugin**  string / required | token that ensures this is a source file for the ‘nmap’ plugin.  **Choices:**   - `"nmap"` - `"community.general.nmap"` |
| **port**  string  *added in community.general 6.5.0* | Only scan specific port or port range (`-p`).  For example, you could pass `22` for a single port, `1-65535` for a range of ports, or `U:53,137,T:21-25,139,8080,S:9` to check port 53 with UDP, ports 21-25 with TCP, port 9 with SCTP, and ports 137, 139, and 8080 with all. |
| **ports**  boolean | Enable/disable scanning ports.  **Choices:**   - `false` - `true` ← (default) |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **sudo**  boolean  *added in community.general 4.8.0* | Set to `true` to execute a `sudo nmap` plugin scan.  **Choices:**   - `false` ← (default) - `true` |
| **udp_scan**  boolean  *added in community.general 6.1.0* | Scan via UDP.  Depending on your system you might need `sudo=true` for this to work.  **Choices:**   - `false` ← (default) - `true` |
| **use_arp_ping**  boolean  *added in community.general 7.4.0* | Whether to always (`true`) use the quick ARP ping or (`false`) a slower but more reliable method.  **Choices:**   - `false` - `true` ← (default) |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Notes](nmap_inventory.md#id4)

> **Note:**
>
> - At least one of ipv4 or ipv6 is required to be True, both can be True, but they cannot both be False.
> - TODO: add OS fingerprinting

## [Examples](nmap_inventory.md#id5)

```yaml+jinja
# inventory.config file in YAML format
plugin: community.general.nmap
strict: false
address: 192.168.0.0/24

# a sudo nmap scan to fully use nmap scan power.
plugin: community.general.nmap
sudo: true
strict: false
address: 192.168.0.0/24

# an nmap scan specifying ports and classifying results to an inventory group
plugin: community.general.nmap
address: 192.168.0.0/24
exclude: 192.168.0.1, web.example.com
port: 22, 443
groups:
  web_servers: "ports | selectattr('port', 'equalto', '443')"
```

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
