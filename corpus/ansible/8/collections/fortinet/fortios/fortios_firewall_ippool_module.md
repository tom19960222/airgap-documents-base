---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_ippool module – Configure IPv4 IP pools in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_ippool_module.html
fetched_at: 2026-07-28T02:24:43+00:00
---
# fortinet.fortios.fortios_firewall_ippool module – Configure IPv4 IP pools in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_ippool_module.md#ansible-collections-fortinet-fortios-fortios-firewall-ippool-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_ippool`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_ippool_module.md#synopsis)
- [Requirements](fortios_firewall_ippool_module.md#requirements)
- [Parameters](fortios_firewall_ippool_module.md#parameters)
- [Notes](fortios_firewall_ippool_module.md#notes)
- [Examples](fortios_firewall_ippool_module.md#examples)
- [Return Values](fortios_firewall_ippool_module.md#return-values)

## [Synopsis](fortios_firewall_ippool_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and ippool category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_ippool_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_ippool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_ippool**  dictionary | Configure IPv4 IP pools. |
| **add_nat64_route**  string | Enable/disable adding NAT64 route.  **Choices:**   - `"disable"` - `"enable"` |
| **arp_intf**  string | Select an interface from available options that will reply to ARP requests. (If blank, any is selected). Source system.interface.name. |
| **arp_reply**  string | Enable/disable replying to ARP requests when an IP Pool is added to a policy .  **Choices:**   - `"disable"` - `"enable"` |
| **associated_interface**  string | Associated interface name. Source system.interface.name. |
| **block_size**  integer | Number of addresses in a block (64 - 4096). |
| **comments**  string | Comment. |
| **endip**  string | Final IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx). |
| **endport**  integer | Final port number (inclusive) in the range for the address pool . |
| **name**  string / required | IP pool name. |
| **nat64**  string | Enable/disable NAT64.  **Choices:**   - `"disable"` - `"enable"` |
| **num_blocks_per_user**  integer | Number of addresses blocks that can be used by a user (1 to 128). |
| **pba_timeout**  integer | Port block allocation timeout (seconds). |
| **permit_any_host**  string | Enable/disable full cone NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **port_per_user**  integer | Number of port for each user (32 - 60416). |
| **source_endip**  string | Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx). |
| **source_startip**  string | First IPv4 address (inclusive) in the range of the source addresses to be translated (format = xxx.xxx.xxx.xxx). |
| **startip**  string | First IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx). |
| **startport**  integer | First port number (inclusive) in the range for the address pool . |
| **subnet_broadcast_in_ippool**  string | Enable/disable inclusion of the subnetwork address and broadcast IP address in the NAT64 IP pool.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | IP pool type (overload, one-to-one, fixed port range, or port block allocation).  **Choices:**   - `"overload"` - `"one-to-one"` - `"fixed-port-range"` - `"port-block-allocation"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_ippool_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_ippool_module.md#id5)

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
  - name: Configure IPv4 IP pools.
    fortios_firewall_ippool:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_ippool:
        add_nat64_route: "disable"
        arp_intf: "<your_own_value> (source system.interface.name)"
        arp_reply: "disable"
        associated_interface: "<your_own_value> (source system.interface.name)"
        block_size: "128"
        comments: "<your_own_value>"
        endip: "<your_own_value>"
        endport: "65533"
        name: "default_name_11"
        nat64: "disable"
        num_blocks_per_user: "8"
        pba_timeout: "30"
        permit_any_host: "disable"
        port_per_user: "0"
        source_endip: "<your_own_value>"
        source_startip: "<your_own_value>"
        startip: "<your_own_value>"
        startport: "5117"
        subnet_broadcast_in_ippool: "disable"
        type: "overload"
```

## [Return Values](fortios_firewall_ippool_module.md#id6)

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
