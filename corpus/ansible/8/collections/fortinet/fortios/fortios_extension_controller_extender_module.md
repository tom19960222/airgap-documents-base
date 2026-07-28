---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_extension_controller_extender module – Extender controller configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_extension_controller_extender_module.html
fetched_at: 2026-07-28T02:24:06+00:00
---
# fortinet.fortios.fortios_extension_controller_extender module – Extender controller configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_extension_controller_extender_module.md#ansible-collections-fortinet-fortios-fortios-extension-controller-extender-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_extension_controller_extender`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_extension_controller_extender_module.md#synopsis)
- [Requirements](fortios_extension_controller_extender_module.md#requirements)
- [Parameters](fortios_extension_controller_extender_module.md#parameters)
- [Notes](fortios_extension_controller_extender_module.md#notes)
- [Examples](fortios_extension_controller_extender_module.md#examples)
- [Return Values](fortios_extension_controller_extender_module.md#return-values)

## [Synopsis](fortios_extension_controller_extender_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify extension_controller feature and extender category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_extension_controller_extender_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_extension_controller_extender_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **extension_controller_extender**  dictionary | Extender controller configuration. |
| **allowaccess**  list / elements=string | Control management access to the managed extender. Separate entries with a space.  **Choices:**   - `"ping"` - `"telnet"` - `"http"` - `"https"` - `"ssh"` - `"snmp"` |
| **authorized**  string | FortiExtender Administration (enable or disable).  **Choices:**   - `"discovered"` - `"disable"` - `"enable"` |
| **bandwidth_limit**  integer | FortiExtender LAN extension bandwidth limit (Mbps). |
| **description**  string | Description. |
| **device_id**  integer | Device ID. |
| **enforce_bandwidth**  string | Enable/disable enforcement of bandwidth on LAN extension interface.  **Choices:**   - `"enable"` - `"disable"` |
| **ext_name**  string | FortiExtender name. |
| **extension_type**  string | Extension type for this FortiExtender.  **Choices:**   - `"wan-extension"` - `"lan-extension"` |
| **firmware_provision_latest**  string | Enable/disable one-time automatic provisioning of the latest firmware version.  **Choices:**   - `"disable"` - `"once"` |
| **id**  string | FortiExtender serial number. |
| **login_password**  string | Set the managed extender”s administrator password. |
| **login_password_change**  string | Change or reset the administrator password of a managed extender (yes, default, or no).  **Choices:**   - `"yes"` - `"default"` - `"no"` |
| **name**  string / required | FortiExtender entry name. |
| **override_allowaccess**  string | Enable to override the extender profile management access configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_enforce_bandwidth**  string | Enable to override the extender profile enforce-bandwidth setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_login_password_change**  string | Enable to override the extender profile login-password (administrator password) setting.  **Choices:**   - `"enable"` - `"disable"` |
| **profile**  string | FortiExtender profile configuration. Source extension-controller.extender-profile.name. |
| **wan_extension**  dictionary | FortiExtender wan extension configuration. |
| **modem1_extension**  string | FortiExtender interface name. Source system.interface.name. |
| **modem2_extension**  string | FortiExtender interface name. Source system.interface.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_extension_controller_extender_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_extension_controller_extender_module.md#id5)

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
  - name: Extender controller configuration.
    fortios_extension_controller_extender:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      extension_controller_extender:
        allowaccess: "ping"
        authorized: "discovered"
        bandwidth_limit: "1024"
        description: "<your_own_value>"
        device_id: "128"
        enforce_bandwidth: "enable"
        ext_name: "<your_own_value>"
        extension_type: "wan-extension"
        firmware_provision_latest: "disable"
        id:  "12"
        login_password: "<your_own_value>"
        login_password_change: "yes"
        name: "default_name_15"
        override_allowaccess: "enable"
        override_enforce_bandwidth: "enable"
        override_login_password_change: "enable"
        profile: "<your_own_value> (source extension-controller.extender-profile.name)"
        wan_extension:
            modem1_extension: "<your_own_value> (source system.interface.name)"
            modem2_extension: "<your_own_value> (source system.interface.name)"
```

## [Return Values](fortios_extension_controller_extender_module.md#id6)

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
