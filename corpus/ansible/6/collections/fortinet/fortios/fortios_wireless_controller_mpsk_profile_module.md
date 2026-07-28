---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_mpsk_profile module – Configure MPSK profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_mpsk_profile_module.html
fetched_at: 2026-07-27T17:47:15+00:00
---
# fortinet.fortios.fortios_wireless_controller_mpsk_profile module – Configure MPSK profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_mpsk_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-mpsk-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_mpsk_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_mpsk_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_mpsk_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_mpsk_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_mpsk_profile_module.md#notes)
- [Examples](fortios_wireless_controller_mpsk_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_mpsk_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_mpsk_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and mpsk_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_mpsk_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_mpsk_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_mpsk_profile**  dictionary | Configure MPSK profile. |
| **mpsk_concurrent_clients**  integer | Maximum number of concurrent clients that connect using the same passphrase in multiple PSK authentication (0 - 65535). |
| **mpsk_group**  list / elements=dictionary | List of multiple PSK groups. |
| **mpsk_key**  list / elements=dictionary | List of multiple PSK entries. |
| **comment**  string | Comment. |
| **concurrent_client_limit_type**  string | MPSK client limit type options.  Choices:   - `"default"` - `"unlimited"` - `"specified"` |
| **concurrent_clients**  integer | Number of clients that can connect using this pre-shared key (1 - 65535). |
| **mac**  string | MAC address. |
| **mpsk_schedules**  list / elements=dictionary | Firewall schedule for MPSK passphrase. The passphrase will be effective only when at least one schedule is valid. |
| **name**  string | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime .name. |
| **name**  string | Pre-shared key name. |
| **passphrase**  string | WPA Pre-shared key. |
| **name**  string | MPSK group name. |
| **vlan_id**  integer | Optional VLAN ID. |
| **vlan_type**  string | MPSK group VLAN options.  Choices:   - `"no-vlan"` - `"fixed-vlan"` |
| **name**  string / required | MPSK profile name. |

## [Notes](fortios_wireless_controller_mpsk_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_mpsk_profile_module.md#id5)

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
  - name: Configure MPSK profile.
    fortios_wireless_controller_mpsk_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_mpsk_profile:
        mpsk_concurrent_clients: "0"
        mpsk_group:
         -
            mpsk_key:
             -
                comment: "Comment."
                concurrent_client_limit_type: "default"
                concurrent_clients: "256"
                mac: "<your_own_value>"
                mpsk_schedules:
                 -
                    name: "default_name_11 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
                name: "default_name_12"
                passphrase: "<your_own_value>"
            name: "default_name_14"
            vlan_id: "0"
            vlan_type: "no-vlan"
        name: "default_name_17"
```

## [Return Values](fortios_wireless_controller_mpsk_profile_module.md#id6)

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
