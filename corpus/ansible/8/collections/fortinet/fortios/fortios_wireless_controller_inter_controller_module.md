---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_inter_controller module – Configure inter wireless controller operation in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_inter_controller_module.html
fetched_at: 2026-07-28T02:31:17+00:00
---
# fortinet.fortios.fortios_wireless_controller_inter_controller module – Configure inter wireless controller operation in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_inter_controller_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-inter-controller-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_inter_controller`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_inter_controller_module.md#synopsis)
- [Requirements](fortios_wireless_controller_inter_controller_module.md#requirements)
- [Parameters](fortios_wireless_controller_inter_controller_module.md#parameters)
- [Notes](fortios_wireless_controller_inter_controller_module.md#notes)
- [Examples](fortios_wireless_controller_inter_controller_module.md#examples)
- [Return Values](fortios_wireless_controller_inter_controller_module.md#return-values)

## [Synopsis](fortios_wireless_controller_inter_controller_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and inter_controller category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_inter_controller_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_inter_controller_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_inter_controller**  dictionary | Configure inter wireless controller operation. |
| **fast_failover_max**  integer | Maximum number of retransmissions for fast failover HA messages between peer wireless controllers (3 - 64). |
| **fast_failover_wait**  integer | Minimum wait time before an AP transitions from secondary controller to primary controller (10 - 86400 sec). |
| **inter_controller_key**  string | Secret key for inter-controller communications. |
| **inter_controller_mode**  string | Configure inter-controller mode (disable, l2-roaming, 1+1).  **Choices:**   - `"disable"` - `"l2-roaming"` - `"1+1"` |
| **inter_controller_peer**  list / elements=dictionary | Fast failover peer wireless controller list. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **peer_ip**  string | Peer wireless controller”s IP address. |
| **peer_port**  integer | Port used by the wireless controller”s for inter-controller communications (1024 - 49150). |
| **peer_priority**  string | Peer wireless controller”s priority (primary or secondary).  **Choices:**   - `"primary"` - `"secondary"` |
| **inter_controller_pri**  string | Configure inter-controller”s priority (primary or secondary).  **Choices:**   - `"primary"` - `"secondary"` |
| **l3_roaming**  string | Enable/disable layer 3 roaming .  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_wireless_controller_inter_controller_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_inter_controller_module.md#id5)

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
  - name: Configure inter wireless controller operation.
    fortios_wireless_controller_inter_controller:
      vdom:  "{{ vdom }}"
      wireless_controller_inter_controller:
        fast_failover_max: "10"
        fast_failover_wait: "10"
        inter_controller_key: "<your_own_value>"
        inter_controller_mode: "disable"
        inter_controller_peer:
         -
            id:  "8"
            peer_ip: "<your_own_value>"
            peer_port: "5246"
            peer_priority: "primary"
        inter_controller_pri: "primary"
        l3_roaming: "enable"
```

## [Return Values](fortios_wireless_controller_inter_controller_module.md#id6)

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
