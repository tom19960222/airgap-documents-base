---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_wag_profile module – Configure wireless access gateway (WAG) profiles used for tunnels on AP in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_wag_profile_module.html
fetched_at: 2026-07-28T02:31:30+00:00
---
# fortinet.fortios.fortios_wireless_controller_wag_profile module – Configure wireless access gateway (WAG) profiles used for tunnels on AP in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_wag_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-wag-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_wag_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_wag_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_wag_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_wag_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_wag_profile_module.md#notes)
- [Examples](fortios_wireless_controller_wag_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_wag_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_wag_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and wag_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_wag_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_wag_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_wag_profile**  dictionary | Configure wireless access gateway (WAG) profiles used for tunnels on AP. |
| **comment**  string | Comment. |
| **dhcp_ip_addr**  string | IP address of the monitoring DHCP request packet sent through the tunnel. |
| **name**  string / required | Tunnel profile name. |
| **ping_interval**  integer | Interval between two tunnel monitoring echo packets (1 - 65535 sec). |
| **ping_number**  integer | Number of the tunnel monitoring echo packets (1 - 65535). |
| **return_packet_timeout**  integer | Window of time for the return packets from the tunnel”s remote end (1 - 65535 sec). |
| **tunnel_type**  string | Tunnel type.  **Choices:**   - `"l2tpv3"` - `"gre"` |
| **wag_ip**  string | IP Address of the wireless access gateway. |
| **wag_port**  integer | UDP port of the wireless access gateway. |

## [Notes](fortios_wireless_controller_wag_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_wag_profile_module.md#id5)

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
  - name: Configure wireless access gateway (WAG) profiles used for tunnels on AP.
    fortios_wireless_controller_wag_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_wag_profile:
        comment: "Comment."
        dhcp_ip_addr: "<your_own_value>"
        name: "default_name_5"
        ping_interval: "1"
        ping_number: "5"
        return_packet_timeout: "160"
        tunnel_type: "l2tpv3"
        wag_ip: "<your_own_value>"
        wag_port: "1701"
```

## [Return Values](fortios_wireless_controller_wag_profile_module.md#id6)

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
