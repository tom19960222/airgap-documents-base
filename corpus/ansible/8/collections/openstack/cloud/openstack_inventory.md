---
collection: ansible
version: "8"
title: "openstack.cloud.openstack inventory – OpenStack inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/openstack_inventory.html
fetched_at: 2026-07-28T01:05:55+00:00
---
# openstack.cloud.openstack inventory – OpenStack inventory source

> **Note:**
>
> This inventory plugin is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](openstack_inventory.md#ansible-collections-openstack-cloud-openstack-inventory-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.openstack`.

- [Synopsis](openstack_inventory.md#synopsis)
- [Requirements](openstack_inventory.md#requirements)
- [Parameters](openstack_inventory.md#parameters)
- [Examples](openstack_inventory.md#examples)

## [Synopsis](openstack_inventory.md#id1)

- Gather servers from OpenStack clouds and add them as Ansible hosts to your inventory.
- Use YAML configuration file `openstack.{yaml,yml}` to configure this inventory plugin.
- Consumes cloud credentials from standard YAML configuration files `clouds{,-public}.yaml`.

## [Requirements](openstack_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](openstack_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_projects**  boolean | Lists servers from all projects  **Choices:**   - `false` ← (default) - `true` |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **clouds_yaml_path**  list / elements=string | Override path to `clouds.yaml` file.  If this value is given it will be searched first.  Search paths for cloud credentials are complemented with files `/etc/ansible/openstack.{yaml,yml}`.  Default search paths are documented in <https://docs.openstack.org/os-client-config/latest/user/configuration.html#config-files>.  **Configuration:**   - Environment variable: [`OS_CLIENT_CONFIG_FILE`](../../environment_variables.md#envvar-OS_CLIENT_CONFIG_FILE) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **expand_hostvars**  boolean | Enrich server facts with additional queries to OpenStack services. This includes requests to Cinder and Neutron which can be time-consuming for clouds with many servers.  Default value of *expand_hostvars* is opposite of the default value for option `expand_hostvars` in legacy openstack.py inventory script.  **Choices:**   - `false` ← (default) - `true` |
| **fail_on_errors**  boolean | Whether the inventory script fails, returning no hosts, when connection to a cloud failed, for example due to bad credentials or connectivity issues.  When *fail_on_errors* is `false` this inventory script will return all hosts it could fetch from clouds on a best effort basis.  Default value of *fail_on_errors* is opposite of the default value for option `fail_on_errors` in legacy openstack.py inventory script.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **inventory_hostname**  string | What to register as inventory hostname.  When set to `uuid` the ID of a server will be used and a group will be created for a server name.  When set to `name` the name of a server will be used. When multiple servers share the same name, then the servers IDs will be used.  Default value of *inventory_hostname* is opposite of the default value for option `use_hostnames` in legacy openstack.py inventory script.  **Choices:**   - `"name"` ← (default) - `"uuid"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **legacy_groups**  boolean | Automatically create groups from host variables.  **Choices:**   - `false` - `true` ← (default) |
| **only_clouds**  list / elements=string | List of clouds in `clouds.yaml` which will be contacted to use instead of using all clouds.  **Default:** `[]` |
| **plugin**  string / required | Token which marks a given YAML configuration file as a valid input file for this inventory plugin.  **Choices:**   - `"openstack"` - `"openstack.cloud.openstack"` |
| **private**  boolean | Use private interfaces of servers, if available, when determining ip addresses for Ansible hosts.  Using *private* helps when running Ansible from a server in the cloud and one wants to ensure that servers communicate over private networks only.  **Choices:**   - `false` ← (default) - `true` |
| **show_all**  boolean | Whether all servers should be listed or not.  When *show_all* is `false` then only servers with a valid ip address, regardless it is private or public, will be listed.  **Choices:**   - `false` ← (default) - `true` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_names**  boolean | When *use_names* is `false`, its default value, then a server’s first floating ip address will be used for both facts `ansible_host` and `ansible_ssh_host`. When no floating ip address is attached to a server, then its first non-floating ip addresses is used instead. If no addresses are attached to a server, then both facts will not be defined.  When *use_names* is `true`, then the server name will be for both `ansible_host` and `ansible_ssh_host` facts. This is useful for jump or bastion hosts where each server name is actually a server’s FQDN.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](openstack_inventory.md#id4)

```yaml+jinja
# Create a file called openstack.yaml, add the following content and run
# $> ansible-inventory --list -vvv -i openstack.yaml
plugin: openstack.cloud.openstack

all_projects: false
expand_hostvars: true
fail_on_errors: true
only_clouds:
  - "devstack-admin"
strict: true
```

### Authors

- OpenStack Ansible SIG

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
