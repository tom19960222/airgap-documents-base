---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_vlan_ip_range module – Manages VLAN IP ranges on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_vlan_ip_range_module.html
fetched_at: 2026-07-28T00:15:52+00:00
---
# ngine_io.cloudstack.cs_vlan_ip_range module – Manages VLAN IP ranges on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_vlan_ip_range_module.md#ansible-collections-ngine-io-cloudstack-cs-vlan-ip-range-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_vlan_ip_range`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_vlan_ip_range_module.md#synopsis)
- [Requirements](cs_vlan_ip_range_module.md#requirements)
- [Parameters](cs_vlan_ip_range_module.md#parameters)
- [Notes](cs_vlan_ip_range_module.md#notes)
- [Examples](cs_vlan_ip_range_module.md#examples)
- [Return Values](cs_vlan_ip_range_module.md#return-values)

## [Synopsis](cs_vlan_ip_range_module.md#id1)

- Create and delete VLAN IP range.

## [Requirements](cs_vlan_ip_range_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_vlan_ip_range_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account who owns the VLAN.  Mutually exclusive with *project*. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidr_ipv6**  string | The CIDR of IPv6 network, must be at least /64. |
| **domain**  string | Domain of the account owning the VLAN. |
| **end_ip**  string | The ending IPv4 address in the VLAN IP range.  If not specified, value of *start_ip* is used.  Only considered on create. |
| **end_ipv6**  string | The ending IPv6 address in the IPv6 network range.  If not specified, value of *start_ipv6* is used.  Only considered on create. |
| **for_system_vms**  boolean | `yes` if IP range is set to system vms, `no` if not  Choices:   - `false` ← (default) - `true` |
| **for_virtual_network**  boolean  added in ngine_io.cloudstack 1.0.0 | `yes` if VLAN is of Virtual type, `no` if Direct.  If set to `yes` but neither *physical_network* or *network* is set CloudStack will try to add the VLAN range to the Physical Network with a Public traffic type.  Choices:   - `false` ← (default) - `true` |
| **gateway**  string | The gateway of the VLAN IP range.  Required if *state=present*. |
| **gateway_ipv6**  string | The gateway of the IPv6 network.  Only considered on create. |
| **netmask**  string | The netmask of the VLAN IP range.  Required if *state=present*. |
| **network**  string | The network name or id.  Required if *for_virtual_network* and *physical_network* are not set. |
| **physical_network**  string | The physical network name or id. |
| **pod**  string  added in ngine_io.cloudstack 1.0.0 | Name of the pod. |
| **project**  string | Project who owns the VLAN.  Mutually exclusive with *account*. |
| **start_ip**  string / required | The beginning IPv4 address in the VLAN IP range.  Only considered on create. |
| **start_ipv6**  string | The beginning IPv6 address in the IPv6 network range.  Only considered on create. |
| **state**  string | State of the network ip range.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vlan**  string | The ID or VID of the network.  If not specified, will be defaulted to the vlan of the network. |
| **zone**  string / required | The Zone ID of the VLAN IP range. |

## [Notes](cs_vlan_ip_range_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_vlan_ip_range_module.md#id5)

```yaml+jinja
- name: create a VLAN IP range for network test
  ngine_io.cloudstack.cs_vlan_ip_range:
    network: test
    vlan: 98
    start_ip: 10.2.4.10
    end_ip: 10.2.4.100
    gateway: 10.2.4.1
    netmask: 255.255.255.0
    zone: zone-02

- name: remove a VLAN IP range for network test
  ngine_io.cloudstack.cs_vlan_ip_range:
    state: absent
    network: test
    start_ip: 10.2.4.10
    end_ip: 10.2.4.100
    zone: zone-02
```

## [Return Values](cs_vlan_ip_range_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account who owns the network.  Returned: if available  Sample: `"example account"` |
| **cidr_ipv6**  string | The CIDR of IPv6 network.  Returned: if available  Sample: `"2001:db8::/64"` |
| **domain**  string | Domain name of the VLAN IP range.  Returned: success  Sample: `"ROOT"` |
| **end_ip**  string | The end ip of the VLAN IP range.  Returned: success  Sample: `"10.2.4.100"` |
| **end_ipv6**  string | The end ipv6 of the VLAN IP range.  Returned: if available  Sample: `"2001:db8::50"` |
| **for_systemvms**  boolean | Whether VLAN IP range is dedicated to system vms or not.  Returned: success  Sample: `false` |
| **for_virtual_network**  boolean | Whether VLAN IP range is of Virtual type or not.  Returned: success  Sample: `false` |
| **gateway**  string | IPv4 gateway.  Returned: success  Sample: `"10.2.4.1"` |
| **gateway_ipv6**  string | IPv6 gateway.  Returned: if available  Sample: `"2001:db8::1"` |
| **id**  string | UUID of the VLAN IP range.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **netmask**  string | IPv4 netmask.  Returned: success  Sample: `"255.255.255.0"` |
| **network**  string | The network of vlan range  Returned: if available  Sample: `"test"` |
| **physical_network**  string | The physical network VLAN IP range belongs to.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **project**  string | Project who owns the network.  Returned: if available  Sample: `"example project"` |
| **start_ip**  string | The start ip of the VLAN IP range.  Returned: success  Sample: `"10.2.4.10"` |
| **start_ipv6**  string | The start ipv6 of the VLAN IP range.  Returned: if available  Sample: `"2001:db8::10"` |
| **vlan**  string | The ID or VID of the VLAN.  Returned: success  Sample: `"vlan://98"` |
| **zone**  string | Name of zone.  Returned: success  Sample: `"zone-02"` |

### Authors

- David Passante (@dpassante)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
