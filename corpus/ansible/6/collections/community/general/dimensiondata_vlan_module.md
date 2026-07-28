---
collection: ansible
version: "6"
title: "community.general.dimensiondata_vlan module – Manage a VLAN in a Cloud Control network domain"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dimensiondata_vlan_module.html
fetched_at: 2026-07-27T17:08:43+00:00
---
# community.general.dimensiondata_vlan module – Manage a VLAN in a Cloud Control network domain

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.dimensiondata_vlan`.

- [Synopsis](dimensiondata_vlan_module.md#synopsis)
- [Parameters](dimensiondata_vlan_module.md#parameters)
- [Examples](dimensiondata_vlan_module.md#examples)
- [Return Values](dimensiondata_vlan_module.md#return-values)

## [Synopsis](dimensiondata_vlan_module.md#id1)

- Manage VLANs in Cloud Control network domains.

## [Parameters](dimensiondata_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_expand**  boolean | Permit expansion of the target VLAN’s network if the module parameters specify a larger network than the VLAN currently possesses.  If `False`, the module will fail under these conditions.  This is intended to prevent accidental expansion of a VLAN’s network (since this operation is not reversible).  Choices:   - `false` ← (default) - `true` |
| **description**  string | A description of the VLAN.  Default: `""` |
| **location**  string / required | The target datacenter. |
| **mcp_password**  string | The password used to authenticate to the CloudControl API.  If not specified, will fall back to `MCP_PASSWORD` from environment variable or `~/.dimensiondata`.  Required if *mcp_user* is specified. |
| **mcp_user**  string | The username used to authenticate to the CloudControl API.  If not specified, will fall back to `MCP_USER` from environment variable or `~/.dimensiondata`. |
| **name**  string / required | The name of the target VLAN. |
| **network_domain**  string / required | The Id or name of the target network domain. |
| **private_ipv4_base_address**  string | The base address for the VLAN’s IPv4 network (e.g. 192.168.1.0).  Default: `""` |
| **private_ipv4_prefix_size**  integer | The size of the IPv4 address space, e.g 24.  Required, if `private_ipv4_base_address` is specified.  Default: `0` |
| **region**  string | The target region.  Regions are defined in Apache libcloud project [libcloud/common/dimensiondata.py]  They are also listed in <https://libcloud.readthedocs.io/en/latest/compute/drivers/dimensiondata.html>  Note that the default value “na” stands for “North America”.  The module prepends ‘dd-’ to the region choice.  Default: `"na"` |
| **state**  string | The desired state for the target VLAN.  `readonly` ensures that the state is only ever read, not modified (the module will fail if the resource does not exist).  Choices:   - `"present"` ← (default) - `"absent"` - `"readonly"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on private instances of the CloudControl API that use self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Should we wait for the task to complete before moving onto the next.  Choices:   - `false` ← (default) - `true` |
| **wait_poll_interval**  integer | The amount of time (in seconds) to wait between checks for task completion.  Only applicable if *wait=true*.  Default: `2` |
| **wait_time**  integer | The maximum amount of time (in seconds) to wait for the task to complete.  Only applicable if *wait=true*.  Default: `600` |

## [Examples](dimensiondata_vlan_module.md#id3)

```yaml+jinja
- name: Add or update VLAN
  community.general.dimensiondata_vlan:
    region: na
    location: NA5
    network_domain: test_network
    name: my_vlan1
    description: A test VLAN
    private_ipv4_base_address: 192.168.23.0
    private_ipv4_prefix_size: 24
    state: present
    wait: true

- name: Read / get VLAN details
  community.general.dimensiondata_vlan:
    region: na
    location: NA5
    network_domain: test_network
    name: my_vlan1
    state: readonly
    wait: true

- name: Delete a VLAN
  community.general.dimensiondata_vlan:
    region: na
    location: NA5
    network_domain: test_network
    name: my_vlan_1
    state: absent
    wait: true
```

## [Return Values](dimensiondata_vlan_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vlan**  complex | Dictionary describing the VLAN.  Returned: On success when *state* is ‘present’ |
| **description**  string | VLAN description.  Returned: success  Sample: `"My VLAN description"` |
| **id**  string | VLAN ID.  Returned: success  Sample: `"aaaaa000-a000-4050-a215-2808934ccccc"` |
| **location**  string | Datacenter location.  Returned: success  Sample: `"NA3"` |
| **name**  string | VLAN name.  Returned: success  Sample: `"My VLAN"` |
| **private_ipv4_base_address**  string | The base address for the VLAN’s private IPV4 network.  Returned: success  Sample: `"192.168.23.0"` |
| **private_ipv4_gateway_address**  string | The gateway address for the VLAN’s private IPV4 network.  Returned: success  Sample: `"192.168.23.1"` |
| **private_ipv4_prefix_size**  integer | The prefix size for the VLAN’s private IPV4 network.  Returned: success  Sample: `24` |
| **private_ipv6_base_address**  string | The base address for the VLAN’s IPV6 network.  Returned: success  Sample: `"2402:9900:111:1195:0:0:0:0"` |
| **private_ipv6_gateway_address**  string | The gateway address for the VLAN’s IPV6 network.  Returned: success  Sample: `"2402:9900:111:1195:0:0:0:1"` |
| **private_ipv6_prefix_size**  integer | The prefix size for the VLAN’s IPV6 network.  Returned: success  Sample: `64` |
| **status**  string | VLAN status.  Returned: success  Sample: `"NORMAL"` |

### Authors

- Adam Friedman (@tintoy)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
