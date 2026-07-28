---
collection: ansible
version: "6"
title: "community.fortios.fmgr_fwobj_service module – Manages FortiManager Firewall Service Objects."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_fwobj_service_module.html
fetched_at: 2026-07-27T17:07:41+00:00
---
# community.fortios.fmgr_fwobj_service module – Manages FortiManager Firewall Service Objects.

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
> To use it in a playbook, specify: `community.fortios.fmgr_fwobj_service`.

- [Synopsis](fmgr_fwobj_service_module.md#synopsis)
- [Parameters](fmgr_fwobj_service_module.md#parameters)
- [Notes](fmgr_fwobj_service_module.md#notes)
- [Examples](fmgr_fwobj_service_module.md#examples)
- [Return Values](fmgr_fwobj_service_module.md#return-values)

## [Synopsis](fmgr_fwobj_service_module.md#id1)

- Manages FortiManager Firewall Service Objects.

## [Parameters](fmgr_fwobj_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | -The ADOM the configuration should belong to.  Default: `"root"` |
| **app_category**  string | Application category ID. |
| **app_service_type**  string | Application service type. |
| **application**  string | Application ID. |
| **category**  string | Service category. |
| **check_reset_range**  string | Enable disable RST check. |
| **color**  string | GUI icon color.  Default: `22` |
| **comment**  string | Comment. |
| **custom_type**  string | Tells module what kind of custom service to be added.  Choices:   - `"tcp_udp_sctp"` - `"icmp"` - `"icmp6"` - `"ip"` - `"http"` - `"ftp"` - `"connect"` - `"socks_tcp"` - `"socks_udp"` - `"all"` ← (default) |
| **explicit_proxy**  string | Enable/disable explicit web proxy service.  Choices:   - `"enable"` - `"disable"` ← (default) |
| **fqdn**  string | Fully qualified domain name.  Default: `""` |
| **group_member**  string | Comma-Seperated list of members’ names. |
| **group_name**  string | Name of the Service Group. |
| **icmp_code**  string | ICMP code. |
| **icmp_type**  string | ICMP type. |
| **iprange**  string | Start IP-End IP.  Default: `"0.0.0.0"` |
| **mode**  string | Sets one of three modes for managing the object.  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` |
| **name**  string | Custom service name. |
| **object_type**  string | Tells module if we are adding a custom service, category, or group.  Choices:   - `"custom"` - `"group"` - `"category"` |
| **protocol**  string | Protocol type. |
| **protocol_number**  string | IP protocol number. |
| **sctp_portrange**  string | Multiple SCTP port ranges. Comma separated list of destination ports to add (i.e. ‘443,80’).  Syntax is <destPort:sourcePort>  If no sourcePort is defined, it assumes all of them.  Ranges can be defined with a hyphen -  Examples – ‘443’ (destPort 443 only) ‘443:1000-2000’ (destPort 443 from source ports 1000-2000).  String multiple together in same quotes, comma separated. (‘443:1000-2000, 80:1000-2000’). |
| **session_ttl**  string | Session TTL (300 - 604800, 0 = default).  Default: `0` |
| **tcp_halfclose_timer**  string | TCP half close timeout (1 - 86400 sec, 0 = default).  Default: `0` |
| **tcp_halfopen_timer**  string | TCP half close timeout (1 - 86400 sec, 0 = default).  Default: `0` |
| **tcp_portrange**  string | Comma separated list of destination ports to add (i.e. ‘443,80’).  Syntax is <destPort:sourcePort>  If no sourcePort is defined, it assumes all of them.  Ranges can be defined with a hyphen -  Examples – ‘443’ (destPort 443 only) ‘443:1000-2000’ (destPort 443 from source ports 1000-2000).  String multiple together in same quotes, comma separated. (‘443:1000-2000, 80:1000-2000’). |
| **tcp_timewait_timer**  string | TCP half close timeout (1 - 300 sec, 0 = default).  Default: `0` |
| **udp_idle_timer**  string | TCP half close timeout (0 - 86400 sec, 0 = default).  Default: `0` |
| **udp_portrange**  string | Comma separated list of destination ports to add (i.e. ‘443,80’).  Syntax is <destPort:sourcePort>  If no sourcePort is defined, it assumes all of them.  Ranges can be defined with a hyphen -  Examples – ‘443’ (destPort 443 only) ‘443:1000-2000’ (destPort 443 from source ports 1000-2000).  String multiple together in same quotes, comma separated. (‘443:1000-2000, 80:1000-2000’). |
| **visibility**  string | Enable/disable service visibility.  Choices:   - `"enable"` ← (default) - `"disable"` |

## [Notes](fmgr_fwobj_service_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_fwobj_service_module.md#id4)

```yaml+jinja
- name: ADD A CUSTOM SERVICE FOR TCP/UDP/SCP
  community.fortios.fmgr_fwobj_service:
    adom: "ansible"
    name: "ansible_custom_service"
    object_type: "custom"
    custom_type: "tcp_udp_sctp"
    tcp_portrange: "443"
    udp_portrange: "51"
    sctp_portrange: "100"

- name: ADD A CUSTOM SERVICE FOR TCP/UDP/SCP WITH SOURCE RANGES AND MULTIPLES
  community.fortios.fmgr_fwobj_service:
    adom: "ansible"
    name: "ansible_custom_serviceWithSource"
    object_type: "custom"
    custom_type: "tcp_udp_sctp"
    tcp_portrange: "443:2000-1000,80-82:10000-20000"
    udp_portrange: "51:100-200,162:200-400"
    sctp_portrange: "100:2000-2500"

- name: ADD A CUSTOM SERVICE FOR ICMP
  community.fortios.fmgr_fwobj_service:
    adom: "ansible"
    name: "ansible_custom_icmp"
    object_type: "custom"
    custom_type: "icmp"
    icmp_type: "8"
    icmp_code: "3"

- name: ADD A CUSTOM SERVICE FOR ICMP6
  community.fortios.fmgr_fwobj_service:
    adom: "ansible"
    name: "ansible_custom_icmp6"
    object_type: "custom"
    custom_type: "icmp6"
    icmp_type: "5"
    icmp_code: "1"

- name: ADD A CUSTOM SERVICE FOR IP - GRE
  community.fortios.fmgr_fwobj_service:
    adom: "ansible"
    name: "ansible_custom_icmp6"
    object_type: "custom"
    custom_type: "ip"
    protocol_number: "47"

- name: ADD A CUSTOM PROXY FOR ALL WITH SOURCE RANGES AND MULTIPLES
  community.fortios.fmgr_fwobj_service:
    adom: "ansible"
    name: "ansible_custom_proxy_all"
    object_type: "custom"
    custom_type: "all"
    explicit_proxy: "enable"
    tcp_portrange: "443:2000-1000,80-82:10000-20000"
    iprange: "www.ansible.com"
```

## [Return Values](fmgr_fwobj_service_module.md#id5)

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
