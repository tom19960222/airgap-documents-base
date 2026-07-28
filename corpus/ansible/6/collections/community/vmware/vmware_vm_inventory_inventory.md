---
collection: ansible
version: "6"
title: "community.vmware.vmware_vm_inventory inventory – VMware Guest inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vm_inventory_inventory.html
fetched_at: 2026-07-27T17:23:07+00:00
---
# community.vmware.vmware_vm_inventory inventory – VMware Guest inventory source

> **Note:**
>
> This inventory plugin is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_vm_inventory`.

- [Synopsis](vmware_vm_inventory_inventory.md#synopsis)
- [Requirements](vmware_vm_inventory_inventory.md#requirements)
- [Parameters](vmware_vm_inventory_inventory.md#parameters)
- [Examples](vmware_vm_inventory_inventory.md#examples)

## [Synopsis](vmware_vm_inventory_inventory.md#id1)

- Get virtual machines as inventory hosts from VMware environment.
- Uses any file which ends with vmware.yml, vmware.yaml, vmware_vm_inventory.yml, or vmware_vm_inventory.yaml as a YAML configuration file.

## [Requirements](vmware_vm_inventory_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- requests >= 2.3
- vSphere Automation SDK - For tag feature

## [Parameters](vmware_vm_inventory_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  Default: `"memory"`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  Default: `"ansible_inventory_"`  Configuration:   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  Default: `3600`  Configuration:   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **filters**  list / elements=string | This option allows client-side filtering hosts with jinja templating.  When server-side filtering is introduced, it should be preferred over this.  Default: `[]` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **hostname**  string / required | Name of vCenter or ESXi server.  Configuration:   - Environment variable: [`VMWARE_HOST`](../../environment_variables.md#envvar-VMWARE_HOST) - Environment variable: [`VMWARE_SERVER`](../../environment_variables.md#envvar-VMWARE_SERVER) |
| **hostnames**  list / elements=string | A list of templates in order of precedence to compose inventory_hostname.  Ignores template if resulted in an empty string or None value.  You can use property specified in *properties* as variables in the template.  Default: `["config.name + \"_\" + config.uuid"]` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[{"key": "config.guestId", "separator": ""}, {"key": "summary.runtime.powerState", "separator": ""}]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **password**  string / required | Password of vSphere user.  Accepts vault encrypted variable.  Configuration:   - Environment variable: [`VMWARE_PASSWORD`](../../environment_variables.md#envvar-VMWARE_PASSWORD) |
| **port**  integer | Port number used to connect to vCenter or ESXi Server.  Default: `443`  Configuration:   - Environment variable: [`VMWARE_PORT`](../../environment_variables.md#envvar-VMWARE_PORT) |
| **properties**  list / elements=string | Specify the list of VMware schema properties associated with the VM.  These properties will be populated in hostvars of the given VM.  Each value in the list can be a path to a specific property in VM object or a path to a collection of VM objects.  `config.name`, `config.uuid` are required properties if `hostnames` is set to default.  `config.guestId`, `summary.runtime.powerState` are required if `keyed_groups` is set to default.  Please make sure that all the properties that are used in other parameters are included in this options.  In addition to VM properties, the following are special values  Use `customValue` to populate virtual machine’s custom attributes. `customValue` is only supported by vCenter and not by ESXi.  Use `all` to populate all the properties of the virtual machine. The value `all` is time consuming operation, do not use unless required absolutely.  Please refer more VMware guest attributes which can be used as properties <https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.rst>  Default: `["name", "config.cpuHotAddEnabled", "config.cpuHotRemoveEnabled", "config.instanceUuid", "config.hardware.numCPU", "config.template", "config.name", "config.uuid", "guest.hostName", "guest.ipAddress", "guest.guestId", "guest.guestState", "runtime.maxMemoryUsage", "customValue", "summary.runtime.powerState", "config.guestId"]` |
| **proxy_host**  string  added in community.vmware 1.12.0 | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  This feature depends on a version of pyvmomi>=v6.7.1.2018.12.  Configuration:   - Environment variable: [`VMWARE_PROXY_HOST`](../../environment_variables.md#envvar-VMWARE_PROXY_HOST) |
| **proxy_port**  integer  added in community.vmware 1.12.0 | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  Configuration:   - Environment variable: [`VMWARE_PROXY_PORT`](../../environment_variables.md#envvar-VMWARE_PROXY_PORT) |
| **resources**  list / elements=dictionary | A list of resources to limit search scope.  Each resource item is represented by exactly one `'vim_type_snake_case`:`list of resource names` pair and optional nested *resources*  Key name is based on snake case of a vim type name; e.g `host_system` correspond to `vim.HostSystem`  See [VIM Types](https://pubs.vmware.com/vi-sdk/visdk250/ReferenceGuide/index-mo_types.html)  Default: `[]` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **username**  string / required | Name of vSphere user.  Accepts vault encrypted variable.  Configuration:   - Environment variable: [`VMWARE_USER`](../../environment_variables.md#envvar-VMWARE_USER) - Environment variable: [`VMWARE_USERNAME`](../../environment_variables.md#envvar-VMWARE_USERNAME) |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  Choices:   - `false` - `true` ← (default)   Configuration:   - Environment variable: [`VMWARE_VALIDATE_CERTS`](../../environment_variables.md#envvar-VMWARE_VALIDATE_CERTS) |
| **with_nested_properties**  boolean | This option transform flatten properties name to nested dictionary.  From 1.10.0 and onwards, default value is set to `True`.  Choices:   - `false` - `true` ← (default) |
| **with_path**  boolean | Include virtual machines path.  Set this option to a string value to replace root name from *‘Datacenters’*.  Choices:   - `false` ← (default) - `true` |
| **with_sanitized_property_name**  boolean | This option allows property name sanitization to create safe property names for use in Ansible.  Also, transforms property name to snake case.  Choices:   - `false` ← (default) - `true` |
| **with_tags**  boolean | Include tags and associated virtual machines.  Requires ‘vSphere Automation SDK’ library to be installed on the given controller machine.  Please refer following URLs for installation steps  <https://code.vmware.com/web/sdk/7.0/vsphere-automation-python>  Choices:   - `false` ← (default) - `true` |

## [Examples](vmware_vm_inventory_inventory.md#id4)

```yaml+jinja
# Sample configuration file for VMware Guest dynamic inventory
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    with_tags: True

# Gather minimum set of properties for VMware guest
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    properties:
    - 'name'
    - 'guest.ipAddress'
    - 'config.name'
    - 'config.uuid'

# Create Groups based upon VMware Tools status
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    properties:
    - 'name'
    - 'config.name'
    - 'guest.toolsStatus'
    - 'guest.toolsRunningStatus'
    hostnames:
    - config.name
    keyed_groups:
    - key: guest.toolsStatus
      separator: ''
    - key: guest.toolsRunningStatus
      separator: ''

# Filter VMs based upon condition
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    properties:
    - 'runtime.powerState'
    - 'config.name'
    filters:
    - runtime.powerState == "poweredOn"
    hostnames:
    - config.name

# Filter VM's based on OR conditions
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    properties:
    - 'name'
    - 'config.name'
    - 'guest.ipAddress'
    - 'guest.toolsStatus'
    - 'guest.toolsRunningStatus'
    - 'config.guestFullName'
    - 'config.guestId'
    hostnames:
    - 'config.name'
    filters:
    - config.guestId == "rhel7_64Guest" or config.name == "rhel_20_04_empty"

# Filter VM's based on regex conditions
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    properties:
    - 'config.name'
    - 'config.guestId'
    - 'guest.ipAddress'
    - 'summary.runtime.powerState'
    filters:
    - guest.ipAddress is defined and (guest.ipAddress is match('192.168.*') or guest.ipAddress is match('192.169.*'))

# Using compose and groups
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    properties:
    - 'name'
    - 'config.name'
    - 'guest.ipAddress'
    compose:
      # This will populate the IP address of virtual machine if available
      # and will be used while communicating to the given virtual machine
      ansible_host: 'guest.ipAddress'
      composed_var: 'config.name'
      # This will populate a host variable with a string value
      ansible_user: "'admin'"
      ansible_connection: "'ssh'"
    groups:
      VMs: True
    hostnames:
    - config.name

# Use Datacenter, Cluster and Folder value to list VMs
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.200.241
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    with_tags: True
    resources:
      - datacenter:
        - Asia-Datacenter1
        - Asia-Datacenter2
        resources:
        - compute_resource:
          - Asia-Cluster1
          resources:
          - host_system:
            - Asia-ESXI4
        - folder:
          - dev
          - prod

# Use Category and it's relation with Tag
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.201.128
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    hostnames:
    - 'config.name'
    properties:
    - 'config.name'
    - 'config.guestId'
    - 'guest.ipAddress'
    - 'summary.runtime.powerState'
    with_tags: True
    keyed_groups:
    - key: tag_category.OS
      prefix: "vmware_tag_os_category_"
      separator: ""
    with_nested_properties: True
    filters:
    - "tag_category.OS is defined and 'Linux' in tag_category.OS"

# customizing hostnames based on VM's FQDN. The second hostnames template acts as a fallback mechanism.
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    hostnames:
     - 'config.name+"."+guest.ipStack.0.dnsConfig.domainName'
     - 'config.name'
    properties:
      - 'config.name'
      - 'config.guestId'
      - 'guest.hostName'
      - 'guest.ipAddress'
      - 'guest.guestFamily'
      - 'guest.ipStack'

# Select a specific IP address for use by ansible when multiple NICs are present on the VM
    plugin: community.vmware.vmware_vm_inventory
    strict: False
    hostname: 10.65.223.31
    username: administrator@vsphere.local
    password: Esxi@123$%
    validate_certs: False
    compose:
      # Set the IP address used by ansible to one that starts by 10.42. or 10.43.
      ansible_host: >-
        guest.net
        | selectattr('ipAddress')
        | map(attribute='ipAddress')
        | flatten
        | select('match', '^10.42.*|^10.43.*')
        | list
        | first
    properties:
      - guest.net
```

### Authors

- Abhijeet Kasurde (@Akasurde)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
