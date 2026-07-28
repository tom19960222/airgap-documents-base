---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_pppoe_interface module – Configure the PPPoE interfaces in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_pppoe_interface_module.html
fetched_at: 2026-07-27T17:45:02+00:00
---
# fortinet.fortios.fortios_system_pppoe_interface module – Configure the PPPoE interfaces in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_pppoe_interface_module.md#ansible-collections-fortinet-fortios-fortios-system-pppoe-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_pppoe_interface`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_pppoe_interface_module.md#synopsis)
- [Requirements](fortios_system_pppoe_interface_module.md#requirements)
- [Parameters](fortios_system_pppoe_interface_module.md#parameters)
- [Notes](fortios_system_pppoe_interface_module.md#notes)
- [Examples](fortios_system_pppoe_interface_module.md#examples)
- [Return Values](fortios_system_pppoe_interface_module.md#return-values)

## [Synopsis](fortios_system_pppoe_interface_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and pppoe_interface category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_pppoe_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_pppoe_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_pppoe_interface**  dictionary | Configure the PPPoE interfaces. |
| **ac_name**  string | PPPoE AC name. |
| **auth_type**  string | PPP authentication type to use.  Choices:   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **device**  string | Name for the physical interface. Source system.interface.name. |
| **dial_on_demand**  string | Enable/disable dial on demand to dial the PPPoE interface when packets are routed to the PPPoE interface.  Choices:   - `"enable"` - `"disable"` |
| **disc_retry_timeout**  integer | PPPoE discovery init timeout value in (0-4294967295 sec). |
| **idle_timeout**  integer | PPPoE auto disconnect after idle timeout (0-4294967295 sec). |
| **ipunnumbered**  string | PPPoE unnumbered IP. |
| **ipv6**  string | Enable/disable IPv6 Control Protocol (IPv6CP).  Choices:   - `"enable"` - `"disable"` |
| **lcp_echo_interval**  integer | Time in seconds between PPPoE Link Control Protocol (LCP) echo requests. |
| **lcp_max_echo_fails**  integer | Maximum missed LCP echo messages before disconnect. |
| **name**  string / required | Name of the PPPoE interface. |
| **padt_retry_timeout**  integer | PPPoE terminate timeout value in (0-4294967295 sec). |
| **password**  string | Enter the password. |
| **pppoe_unnumbered_negotiate**  string | Enable/disable PPPoE unnumbered negotiation.  Choices:   - `"enable"` - `"disable"` |
| **service_name**  string | PPPoE service name. |
| **username**  string | User name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_pppoe_interface_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_pppoe_interface_module.md#id5)

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
  - name: Configure the PPPoE interfaces.
    fortios_system_pppoe_interface:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_pppoe_interface:
        ac_name: "<your_own_value>"
        auth_type: "auto"
        device: "<your_own_value> (source system.interface.name)"
        dial_on_demand: "enable"
        disc_retry_timeout: "1"
        idle_timeout: "0"
        ipunnumbered: "<your_own_value>"
        ipv6: "enable"
        lcp_echo_interval: "5"
        lcp_max_echo_fails: "3"
        name: "default_name_13"
        padt_retry_timeout: "1"
        password: "<your_own_value>"
        pppoe_unnumbered_negotiate: "enable"
        service_name: "<your_own_value>"
        username: "<your_own_value>"
```

## [Return Values](fortios_system_pppoe_interface_module.md#id6)

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
