---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_rip module – Configure RIP in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_rip_module.html
fetched_at: 2026-07-28T02:26:54+00:00
---
# fortinet.fortios.fortios_router_rip module – Configure RIP in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_rip_module.md#ansible-collections-fortinet-fortios-fortios-router-rip-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_rip`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_rip_module.md#synopsis)
- [Requirements](fortios_router_rip_module.md#requirements)
- [Parameters](fortios_router_rip_module.md#parameters)
- [Notes](fortios_router_rip_module.md#notes)
- [Examples](fortios_router_rip_module.md#examples)
- [Return Values](fortios_router_rip_module.md#return-values)

## [Synopsis](fortios_router_rip_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and rip category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_rip_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_rip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_rip**  dictionary | Configure RIP. |
| **default_information_originate**  string | Enable/disable generation of default route.  **Choices:**   - `"enable"` - `"disable"` |
| **default_metric**  integer | Default metric. |
| **distance**  list / elements=dictionary | Distance. |
| **access_list**  string | Access list for route destination. Source router.access-list.name. |
| **distance**  integer | Distance (1 - 255). |
| **id**  integer / required | Distance ID. see <a href=’#notes’>Notes</a>. |
| **prefix**  string | Distance prefix. |
| **distribute_list**  list / elements=dictionary | Distribute list. |
| **direction**  string | Distribute list direction.  **Choices:**   - `"in"` - `"out"` |
| **id**  integer / required | Distribute list ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | Distribute list interface name. Source system.interface.name. |
| **listname**  string | Distribute access/prefix list name. Source router.access-list.name router.prefix-list.name. |
| **status**  string | Status.  **Choices:**   - `"enable"` - `"disable"` |
| **garbage_timer**  integer | Garbage timer in seconds. |
| **interface**  list / elements=dictionary | RIP interface configuration. |
| **auth_keychain**  string | Authentication key-chain name. Source router.key-chain.name. |
| **auth_mode**  string | Authentication mode.  **Choices:**   - `"none"` - `"text"` - `"md5"` |
| **auth_string**  string | Authentication string/password. |
| **flags**  integer | Flags. |
| **name**  string / required | Interface name. Source system.interface.name. |
| **receive_version**  list / elements=string | Receive version.  **Choices:**   - `"1"` - `"2"` |
| **send_version**  list / elements=string | Send version.  **Choices:**   - `"1"` - `"2"` |
| **send_version2_broadcast**  string | Enable/disable broadcast version 1 compatible packets.  **Choices:**   - `"disable"` - `"enable"` |
| **split_horizon**  string | Enable/disable split horizon.  **Choices:**   - `"poisoned"` - `"regular"` |
| **split_horizon_status**  string | Enable/disable split horizon.  **Choices:**   - `"enable"` - `"disable"` |
| **max_out_metric**  integer | Maximum metric allowed to output(0 means “not set”). |
| **neighbor**  list / elements=dictionary | Neighbor. |
| **id**  integer / required | Neighbor entry ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IP address. |
| **network**  list / elements=dictionary | Network. |
| **id**  integer / required | Network entry ID. see <a href=’#notes’>Notes</a>. |
| **prefix**  string | Network prefix. |
| **offset_list**  list / elements=dictionary | Offset list. |
| **access_list**  string | Access list name. Source router.access-list.name. |
| **direction**  string | Offset list direction.  **Choices:**   - `"in"` - `"out"` |
| **id**  integer / required | Offset-list ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | Interface name. Source system.interface.name. |
| **offset**  integer | Offset. |
| **status**  string | Status.  **Choices:**   - `"enable"` - `"disable"` |
| **passive_interface**  list / elements=dictionary | Passive interface configuration. |
| **name**  string / required | Passive interface name. Source system.interface.name. |
| **recv_buffer_size**  integer | Receiving buffer size. |
| **redistribute**  list / elements=dictionary | Redistribute configuration. |
| **metric**  integer | Redistribute metric setting. |
| **name**  string / required | Redistribute name. |
| **routemap**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  **Choices:**   - `"enable"` - `"disable"` |
| **timeout_timer**  integer | Timeout timer in seconds. |
| **update_timer**  integer | Update timer in seconds. |
| **version**  string | RIP version.  **Choices:**   - `"1"` - `"2"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_rip_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_rip_module.md#id5)

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
  - name: Configure RIP.
    fortios_router_rip:
      vdom:  "{{ vdom }}"
      router_rip:
        default_information_originate: "enable"
        default_metric: "1"
        distance:
         -
            access_list: "<your_own_value> (source router.access-list.name)"
            distance: "0"
            id:  "8"
            prefix: "<your_own_value>"
        distribute_list:
         -
            direction: "in"
            id:  "12"
            interface: "<your_own_value> (source system.interface.name)"
            listname: "<your_own_value> (source router.access-list.name router.prefix-list.name)"
            status: "enable"
        garbage_timer: "120"
        interface:
         -
            auth_keychain: "<your_own_value> (source router.key-chain.name)"
            auth_mode: "none"
            auth_string: "<your_own_value>"
            flags: "8"
            name: "default_name_22 (source system.interface.name)"
            receive_version: "1"
            send_version: "1"
            send_version2_broadcast: "disable"
            split_horizon: "poisoned"
            split_horizon_status: "enable"
        max_out_metric: "0"
        neighbor:
         -
            id:  "30"
            ip: "<your_own_value>"
        network:
         -
            id:  "33"
            prefix: "<your_own_value>"
        offset_list:
         -
            access_list: "<your_own_value> (source router.access-list.name)"
            direction: "in"
            id:  "38"
            interface: "<your_own_value> (source system.interface.name)"
            offset: "0"
            status: "enable"
        passive_interface:
         -
            name: "default_name_43 (source system.interface.name)"
        recv_buffer_size: "655360"
        redistribute:
         -
            metric: "0"
            name: "default_name_47"
            routemap: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        timeout_timer: "180"
        update_timer: "30"
        version: "1"
```

## [Return Values](fortios_router_rip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
