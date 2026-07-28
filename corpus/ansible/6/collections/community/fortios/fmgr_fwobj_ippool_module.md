---
collection: ansible
version: "6"
title: "community.fortios.fmgr_fwobj_ippool module – Allows the editing of IP Pool Objects within FortiManager."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_fwobj_ippool_module.html
fetched_at: 2026-07-27T17:07:40+00:00
---
# community.fortios.fmgr_fwobj_ippool module – Allows the editing of IP Pool Objects within FortiManager.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_fwobj_ippool`.

- [Synopsis](fmgr_fwobj_ippool_module.md#synopsis)
- [Parameters](fmgr_fwobj_ippool_module.md#parameters)
- [Notes](fmgr_fwobj_ippool_module.md#notes)
- [Examples](fmgr_fwobj_ippool_module.md#examples)
- [Return Values](fmgr_fwobj_ippool_module.md#return-values)

## [Synopsis](fmgr_fwobj_ippool_module.md#id1)

- Allows users to add/edit/delete IP Pool Objects.

## [Parameters](fmgr_fwobj_ippool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **arp_intf**  string | Select an interface from available options that will reply to ARP requests. (If blank, any is selected). |
| **arp_reply**  string | Enable/disable replying to ARP requests when an IP Pool is added to a policy (default = enable).  choice | disable | Disable ARP reply.  choice | enable | Enable ARP reply.  Choices:   - `"disable"` - `"enable"` |
| **associated_interface**  string | Associated interface name. |
| **block_size**  string | Number of addresses in a block (64 to 4096, default = 128). |
| **comments**  string | Comment. |
| **dynamic_mapping**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameter.ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **dynamic_mapping_arp_intf**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_arp_reply**  string | Dynamic Mapping clone of original suffixed parameter.  Choices:   - `"disable"` - `"enable"` |
| **dynamic_mapping_associated_interface**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_block_size**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_comments**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_endip**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_num_blocks_per_user**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_pba_timeout**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_permit_any_host**  string | Dynamic Mapping clone of original suffixed parameter.  Choices:   - `"disable"` - `"enable"` |
| **dynamic_mapping_source_endip**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_source_startip**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_startip**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_type**  string | Dynamic Mapping clone of original suffixed parameter.  Choices:   - `"overload"` - `"one-to-one"` - `"fixed-port-range"` - `"port-block-allocation"` |
| **endip**  string | Final IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default| 0.0.0.0). |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | IP pool name. |
| **num_blocks_per_user**  string | Number of addresses blocks that can be used by a user (1 to 128, default = 8). |
| **pba_timeout**  string | Port block allocation timeout (seconds). |
| **permit_any_host**  string | Enable/disable full cone NAT.  choice | disable | Disable full cone NAT.  choice | enable | Enable full cone NAT.  Choices:   - `"disable"` - `"enable"` |
| **source_endip**  string | Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx, Default| 0.0.0.0). |
| **source_startip**  string | First IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx, Default| 0.0.0.0). |
| **startip**  string | First IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default| 0.0.0.0). |
| **type**  string | IP pool type (overload, one-to-one, fixed port range, or port block allocation).  choice | overload | IP addresses in the IP pool can be shared by clients.  choice | one-to-one | One to one mapping.  choice | fixed-port-range | Fixed port range.  choice | port-block-allocation | Port block allocation.  Choices:   - `"overload"` - `"one-to-one"` - `"fixed-port-range"` - `"port-block-allocation"` |

## [Notes](fmgr_fwobj_ippool_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_fwobj_ippool_module.md#id4)

```yaml+jinja
- name: ADD FMGR_FIREWALL_IPPOOL Overload
  community.fortios.fmgr_fwobj_ippool:
    mode: "add"
    adom: "ansible"
    name: "Ansible_pool4_overload"
    comments: "Created by ansible"
    type: "overload"

    # OPTIONS FOR ALL MODES
    startip: "10.10.10.10"
    endip: "10.10.10.100"
    arp_reply: "enable"

- name: ADD FMGR_FIREWALL_IPPOOL one-to-one
  community.fortios.fmgr_fwobj_ippool:
    mode: "add"
    adom: "ansible"
    name: "Ansible_pool4_121"
    comments: "Created by ansible"
    type: "one-to-one"

    # OPTIONS FOR ALL MODES
    startip: "10.10.20.10"
    endip: "10.10.20.100"
    arp_reply: "enable"

- name: ADD FMGR_FIREWALL_IPPOOL FIXED PORT RANGE
  community.fortios.fmgr_fwobj_ippool:
    mode: "add"
    adom: "ansible"
    name: "Ansible_pool4_fixed_port"
    comments: "Created by ansible"
    type: "fixed-port-range"

    # OPTIONS FOR ALL MODES
    startip: "10.10.40.10"
    endip: "10.10.40.100"
    arp_reply: "enable"
    # FIXED PORT RANGE OPTIONS
    source_startip: "192.168.20.1"
    source_endip: "192.168.20.20"

- name: ADD FMGR_FIREWALL_IPPOOL PORT BLOCK ALLOCATION
  community.fortios.fmgr_fwobj_ippool:
    mode: "add"
    adom: "ansible"
    name: "Ansible_pool4_port_block_allocation"
    comments: "Created by ansible"
    type: "port-block-allocation"

    # OPTIONS FOR ALL MODES
    startip: "10.10.30.10"
    endip: "10.10.30.100"
    arp_reply: "enable"
    # PORT BLOCK ALLOCATION OPTIONS
    block_size: "128"
    num_blocks_per_user: "1"
```

## [Return Values](fmgr_fwobj_ippool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
