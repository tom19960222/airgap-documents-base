---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.instance inventory – Apache CloudStack instance inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/instance_inventory.html
fetched_at: 2026-07-28T00:15:59+00:00
---
# ngine_io.cloudstack.instance inventory – Apache CloudStack instance inventory source

> **Note:**
>
> This inventory plugin is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.instance`.

New in ngine_io.cloudstack 2.1.0

- [Synopsis](instance_inventory.md#synopsis)
- [Requirements](instance_inventory.md#requirements)
- [Parameters](instance_inventory.md#parameters)
- [Notes](instance_inventory.md#notes)
- [Examples](instance_inventory.md#examples)

## [Synopsis](instance_inventory.md#id1)

- Get inventory hosts from Apache CloudStack
- Allows filtering and grouping inventory hosts.
- Uses an YAML configuration file ending with either *cloudstack-instances.yml* or *cloudstack-instances.yaml*to set parameter values (also see examples).

## [Requirements](instance_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](instance_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"`   Configuration:   - Environment variable: [`CLOUDSTACK_METHOD`](../../environment_variables.md#envvar-CLOUDSTACK_METHOD) |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered.  Configuration:   - Environment variable: [`CLOUDSTACK_KEY`](../../environment_variables.md#envvar-CLOUDSTACK_KEY) |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered.  Configuration:   - Environment variable: [`CLOUDSTACK_SECRET`](../../environment_variables.md#envvar-CLOUDSTACK_SECRET) |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10`  Configuration:   - Environment variable: [`CLOUDSTACK_TIMEOUT`](../../environment_variables.md#envvar-CLOUDSTACK_TIMEOUT) |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered.  Configuration:   - Environment variable: [`CLOUDSTACK_ENDPOINT`](../../environment_variables.md#envvar-CLOUDSTACK_ENDPOINT) |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered.  Configuration:   - Environment variable: [`CLOUDSTACK_VERIFY`](../../environment_variables.md#envvar-CLOUDSTACK_VERIFY) |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **filter_by_domain**  string | Only return instances in the provided domain. |
| **filter_by_project**  string | Only return instances in the provided project. |
| **filter_by_vpc**  string | Only return instances in the provided VPC. |
| **filter_by_zone**  string | Only return instances in the provided zone. |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **hostname**  string | Field to match the hostname. Note v4_main_ip corresponds to the primary ipv4address of the first nic  adapter of the instance.  Choices:   - `"v4_default_ip"` ← (default) - `"hostname"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **plugin**  string / required | Token that ensures this is a source file for the ‘instance’ plugin.  Choices:   - `"ngine_io.cloudstack.instance"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Notes](instance_inventory.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](instance_inventory.md#id5)

```yaml+jinja
# inventory_cloudstack.yml file in YAML format
# Example command line: ansible-inventory --list -i cloudstack-instances.yml
plugin: ngine_io.cloudstack.instance

# Use the default ip as ansible_host
hostname: v4_default_ip

# Return only instances related to the VPC vpc1 and in the zone EU
filter_by_vpc: vpc1
filter_by_zone: EU

# Group instances with a disk_offering as storage
# Create a group dmz for instances connected to the dmz network
groups:
  storage: disk_offering is defined
  dmz: "'dmz' in networks"

# Group the instances by network, with net_network1 as name of the groups
# Group the instanes by custom tag sla, groups like sla_value for tag sla
keyed_groups:
  - prefix: net
    key: networks
  - prefix: sla
    key: tags.sla
```

### Authors

- Rafael del Valle (@rvalle)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
