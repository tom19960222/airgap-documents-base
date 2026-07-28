---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_router_ripng module – Configure RIPng in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_router_ripng_module.html
fetched_at: 2026-07-27T17:43:11+00:00
---
# fortinet.fortios.fortios_router_ripng module – Configure RIPng in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_ripng_module.md#ansible-collections-fortinet-fortios-fortios-router-ripng-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_ripng`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_ripng_module.md#synopsis)
- [Requirements](fortios_router_ripng_module.md#requirements)
- [Parameters](fortios_router_ripng_module.md#parameters)
- [Notes](fortios_router_ripng_module.md#notes)
- [Examples](fortios_router_ripng_module.md#examples)
- [Return Values](fortios_router_ripng_module.md#return-values)

## [Synopsis](fortios_router_ripng_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and ripng category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_ripng_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_router_ripng_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **router_ripng**  dictionary | Configure RIPng. |
| **aggregate_address**  list / elements=dictionary | Aggregate address. |
| **id**  integer | Aggregate address entry ID. |
| **prefix6**  string | Aggregate address prefix. |
| **default_information_originate**  string | Enable/disable generation of default route.  Choices:   - `"enable"` - `"disable"` |
| **default_metric**  integer | Default metric. |
| **distance**  list / elements=dictionary | Distance. |
| **access_list6**  string | Access list for route destination. Source router.access-list6.name. |
| **distance**  integer | Distance (1 - 255). |
| **id**  integer | Distance ID. |
| **prefix6**  string | Distance prefix6. |
| **distribute_list**  list / elements=dictionary | Distribute list. |
| **direction**  string | Distribute list direction.  Choices:   - `"in"` - `"out"` |
| **id**  integer | Distribute list ID. |
| **interface**  string | Distribute list interface name. Source system.interface.name. |
| **listname**  string | Distribute access/prefix list name. Source router.access-list6.name router.prefix-list6.name. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **garbage_timer**  integer | Garbage timer. |
| **interface**  list / elements=dictionary | RIPng interface configuration. |
| **flags**  integer | Flags. |
| **name**  string | Interface name. Source system.interface.name. |
| **split_horizon**  string | Enable/disable split horizon.  Choices:   - `"poisoned"` - `"regular"` |
| **split_horizon_status**  string | Enable/disable split horizon.  Choices:   - `"enable"` - `"disable"` |
| **max_out_metric**  integer | Maximum metric allowed to output(0 means “not set”). |
| **neighbor**  list / elements=dictionary | Neighbor. |
| **id**  integer | Neighbor entry ID. |
| **interface**  string | Interface name. Source system.interface.name. |
| **ip6**  string | IPv6 link-local address. |
| **network**  list / elements=dictionary | Network. |
| **id**  integer | Network entry ID. |
| **prefix**  string | Network IPv6 link-local prefix. |
| **offset_list**  list / elements=dictionary | Offset list. |
| **access_list6**  string | IPv6 access list name. Source router.access-list6.name. |
| **direction**  string | Offset list direction.  Choices:   - `"in"` - `"out"` |
| **id**  integer | Offset-list ID. |
| **interface**  string | Interface name. Source system.interface.name. |
| **offset**  integer | Offset. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **passive_interface**  list / elements=dictionary | Passive interface configuration. |
| **name**  string | Passive interface name. Source system.interface.name. |
| **redistribute**  list / elements=dictionary | Redistribute configuration. |
| **metric**  integer | Redistribute metric setting. |
| **name**  string | Redistribute name. |
| **routemap**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **timeout_timer**  integer | Timeout timer. |
| **update_timer**  integer | Update timer. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_router_ripng_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_ripng_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure RIPng.
    fortios_router_ripng:
      vdom:  "{{ vdom }}"
      router_ripng:
        aggregate_address:
         -
            id:  "4"
            prefix6: "<your_own_value>"
        default_information_originate: "enable"
        default_metric: "1"
        distance:
         -
            access_list6: "<your_own_value> (source router.access-list6.name)"
            distance: "0"
            id:  "11"
            prefix6: "<your_own_value>"
        distribute_list:
         -
            direction: "in"
            id:  "15"
            interface: "<your_own_value> (source system.interface.name)"
            listname: "<your_own_value> (source router.access-list6.name router.prefix-list6.name)"
            status: "enable"
        garbage_timer: "120"
        interface:
         -
            flags: "8"
            name: "default_name_22 (source system.interface.name)"
            split_horizon: "poisoned"
            split_horizon_status: "enable"
        max_out_metric: "0"
        neighbor:
         -
            id:  "27"
            interface: "<your_own_value> (source system.interface.name)"
            ip6: "<your_own_value>"
        network:
         -
            id:  "31"
            prefix: "<your_own_value>"
        offset_list:
         -
            access_list6: "<your_own_value> (source router.access-list6.name)"
            direction: "in"
            id:  "36"
            interface: "<your_own_value> (source system.interface.name)"
            offset: "0"
            status: "enable"
        passive_interface:
         -
            name: "default_name_41 (source system.interface.name)"
        redistribute:
         -
            metric: "0"
            name: "default_name_44"
            routemap: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        timeout_timer: "180"
        update_timer: "30"
```

## [Return Values](fortios_router_ripng_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
