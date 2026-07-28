---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_inventory inventory – VMware ESXi hostsystem inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_inventory_inventory.html
fetched_at: 2026-07-28T02:01:34+00:00
---
# community.vmware.vmware_host_inventory inventory – VMware ESXi hostsystem inventory source

> **Note:**
>
> This inventory plugin is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_host_inventory`.

- [Synopsis](vmware_host_inventory_inventory.md#synopsis)
- [Requirements](vmware_host_inventory_inventory.md#requirements)
- [Parameters](vmware_host_inventory_inventory.md#parameters)
- [Examples](vmware_host_inventory_inventory.md#examples)

## [Synopsis](vmware_host_inventory_inventory.md#id1)

- Get VMware ESXi hostsystem as inventory hosts from VMware environment.
- Uses any file which ends with vmware.yml, vmware.yaml, vmware_host_inventory.yml, or vmware_host_inventory.yaml as a YAML configuration file.

## [Requirements](vmware_host_inventory_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- vSphere Automation SDK - For tag feature

## [Parameters](vmware_host_inventory_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **filters**  list / elements=string | This option allows client-side filtering hosts with jinja templating.  When server-side filtering is introduced, it should be preferred over this.  **Default:** `[]` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **hostname**  string / required | Name of vCenter or ESXi server.  **Configuration:**   - Environment variable: [`VMWARE_HOST`](../../environment_variables.md#envvar-VMWARE_HOST) - Environment variable: [`VMWARE_SERVER`](../../environment_variables.md#envvar-VMWARE_SERVER) |
| **hostnames**  list / elements=string | A list of templates in order of precedence to compose inventory_hostname.  Ignores template if resulted in an empty string or None value.  You can use property specified in *properties* as variables in the template.  **Default:** `["name"]` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[{"key": "summary.runtime.powerState", "separator": ""}]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **password**  string / required | Password of vSphere user.  Accepts vault encrypted variable.  Accepts Jinja to template the value  **Configuration:**   - Environment variable: [`VMWARE_PASSWORD`](../../environment_variables.md#envvar-VMWARE_PASSWORD) |
| **port**  integer | Port number used to connect to vCenter or ESXi Server.  **Default:** `443`  **Configuration:**   - Environment variable: [`VMWARE_PORT`](../../environment_variables.md#envvar-VMWARE_PORT) |
| **properties**  list / elements=string | Specify the list of VMware schema properties associated with the ESXi hostsystem.  These properties will be populated in hostvars of the given ESXi hostsystem.  Each value in the list can be a path to a specific property in hostsystem object or a path to a collection of hostsystem objects.  `summary.runtime.powerState` are required if `keyed_groups` is set to default.  Please make sure that all the properties that are used in other parameters are included in this options.  In addition to ESXi hostsystem’s properties, the following are special values  Use `customValue` to populate ESXi hostsystem’s custom attributes. `customValue` is only supported by vCenter and not by ESXi.  Use `all` to populate all the properties of the virtual machine. The value `all` is time consuming operation, do not use unless required absolutely.  **Default:** `["name", "customValue", "summary.runtime.powerState"]` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  This feature depends on a version of pyvmomi>=v6.7.1.2018.12.  **Configuration:**   - Environment variable: [`VMWARE_PROXY_HOST`](../../environment_variables.md#envvar-VMWARE_PROXY_HOST) |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  **Configuration:**   - Environment variable: [`VMWARE_PROXY_PORT`](../../environment_variables.md#envvar-VMWARE_PROXY_PORT) |
| **resources**  list / elements=dictionary | A list of resources to limit search scope.  Each resource item is represented by exactly one `'vim_type_snake_case`:`list of resource names` pair and optional nested *resources*  Key name is based on snake case of a vim type name; e.g `host_system` correspond to `vim.HostSystem`  **Default:** `[]` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **username**  string / required | Name of vSphere user.  Accepts vault encrypted variable.  Accepts Jinja to template the value  **Configuration:**   - Environment variable: [`VMWARE_USER`](../../environment_variables.md#envvar-VMWARE_USER) - Environment variable: [`VMWARE_USERNAME`](../../environment_variables.md#envvar-VMWARE_USERNAME) |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - Environment variable: [`VMWARE_VALIDATE_CERTS`](../../environment_variables.md#envvar-VMWARE_VALIDATE_CERTS) |
| **with_nested_properties**  boolean | This option transform flatten properties name to nested dictionary.  **Choices:**   - `false` - `true` ← (default) |
| **with_path**  boolean | Include ESXi hostsystem’s path.  Set this option to a string value to replace root name from *‘Datacenters’*.  **Choices:**   - `false` ← (default) - `true` |
| **with_sanitized_property_name**  boolean | This option allows property name sanitization to create safe property names for use in Ansible.  Also, transforms property name to snake case.  **Choices:**   - `false` ← (default) - `true` |
| **with_tags**  boolean | Include tags and associated hosts.  Requires ‘vSphere Automation SDK’ library to be installed on the given controller machine.  Please refer following URLs for installation steps  <https://code.vmware.com/web/sdk/7.0/vsphere-automation-python>  **Choices:**   - `false` ← (default) - `true` |

## [Examples](vmware_host_inventory_inventory.md#id4)

```yaml+jinja
# Sample configuration file for VMware Host dynamic inventory
    plugin: community.vmware.vmware_host_inventory
    strict: false
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: false
    with_tags: true

# Sample configuration file for VMware Guest dynamic inventory using Jinja to template the username and password.
    plugin: community.vmware.vmware_host_inventory
    strict: false
    hostname: 10.65.223.31
    username: '{{ (lookup("file","~/.config/vmware.yaml") | from_yaml).username }}'
    password: '{{ (lookup("file","~/.config/vmware.yaml") | from_yaml).password }}'
    validate_certs: false
    with_tags: true

# Using compose
    plugin: community.vmware.vmware_host_inventory
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: false
    properties:
    - name
    - summary
    - config.lockdownMode
    compose:
        ansible_user: "'root'"
        ansible_connection: "'ssh'"
```

### Authors

- Abhijeet Kasurde (@Akasurde)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
