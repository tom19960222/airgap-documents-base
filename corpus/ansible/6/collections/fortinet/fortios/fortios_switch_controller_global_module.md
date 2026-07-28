---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_global module – Configure FortiSwitch global settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_global_module.html
fetched_at: 2026-07-27T17:43:27+00:00
---
# fortinet.fortios.fortios_switch_controller_global module – Configure FortiSwitch global settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_global_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-global-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_global`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_global_module.md#synopsis)
- [Requirements](fortios_switch_controller_global_module.md#requirements)
- [Parameters](fortios_switch_controller_global_module.md#parameters)
- [Notes](fortios_switch_controller_global_module.md#notes)
- [Examples](fortios_switch_controller_global_module.md#examples)
- [Return Values](fortios_switch_controller_global_module.md#return-values)

## [Synopsis](fortios_switch_controller_global_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and global category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_global**  dictionary | Configure FortiSwitch global settings. |
| **allow_multiple_interfaces**  string | Enable/disable multiple FortiLink interfaces for redundant connections between a managed FortiSwitch and FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **bounce_quarantined_link**  string | Enable/disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last. Helps to re-initiate the DHCP process for a device.  Choices:   - `"disable"` - `"enable"` |
| **custom_command**  list / elements=dictionary | List of custom commands to be pushed to all FortiSwitches in the VDOM. |
| **command_entry**  string | List of FortiSwitch commands. |
| **command_name**  string | Name of custom command to push to all FortiSwitches in VDOM. Source switch-controller.custom-command.command-name. |
| **default_virtual_switch_vlan**  string | Default VLAN for ports when added to the virtual-switch. Source system.interface.name. |
| **dhcp_server_access_list**  string | Enable/disable DHCP snooping server access list.  Choices:   - `"enable"` - `"disable"` |
| **disable_discovery**  list / elements=dictionary | Prevent this FortiSwitch from discovering. |
| **name**  string | Managed device ID. |
| **fips_enforce**  string | Enable/disable enforcement of FIPS on managed FortiSwitch devices.  Choices:   - `"disable"` - `"enable"` |
| **firmware_provision_on_authorization**  string | Enable/disable automatic provisioning of latest firmware on authorization.  Choices:   - `"enable"` - `"disable"` |
| **https_image_push**  string | Enable/disable image push to FortiSwitch using HTTPS.  Choices:   - `"enable"` - `"disable"` |
| **log_mac_limit_violations**  string | Enable/disable logs for Learning Limit Violations.  Choices:   - `"enable"` - `"disable"` |
| **mac_aging_interval**  integer | Time after which an inactive MAC is aged out (10 - 1000000 sec). |
| **mac_event_logging**  string | Enable/disable MAC address event logging.  Choices:   - `"enable"` - `"disable"` |
| **mac_retention_period**  integer | Time in hours after which an inactive MAC is removed from client DB (0 = aged out based on mac-aging-interval). |
| **mac_violation_timer**  integer | Set timeout for Learning Limit Violations (0 = disabled). |
| **quarantine_mode**  string | Quarantine mode.  Choices:   - `"by-vlan"` - `"by-redirect"` |
| **sn_dns_resolution**  string | Enable/disable DNS resolution of the FortiSwitch unit”s IP address by use of its serial number.  Choices:   - `"enable"` - `"disable"` |
| **update_user_device**  list / elements=string | Control which sources update the device user list.  Choices:   - `"mac-cache"` - `"lldp"` - `"dhcp-snooping"` - `"l2-db"` - `"l3-db"` |
| **vlan_all_mode**  string | VLAN configuration mode, user-defined-vlans or all-possible-vlans.  Choices:   - `"all"` - `"defined"` |
| **vlan_optimization**  string | FortiLink VLAN optimization.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_global_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_global_module.md#id5)

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
  - name: Configure FortiSwitch global settings.
    fortios_switch_controller_global:
      vdom:  "{{ vdom }}"
      switch_controller_global:
        allow_multiple_interfaces: "enable"
        bounce_quarantined_link: "disable"
        custom_command:
         -
            command_entry: "<your_own_value>"
            command_name: "<your_own_value> (source switch-controller.custom-command.command-name)"
        default_virtual_switch_vlan: "<your_own_value> (source system.interface.name)"
        dhcp_server_access_list: "enable"
        disable_discovery:
         -
            name: "default_name_11"
        fips_enforce: "disable"
        firmware_provision_on_authorization: "enable"
        https_image_push: "enable"
        log_mac_limit_violations: "enable"
        mac_aging_interval: "300"
        mac_event_logging: "enable"
        mac_retention_period: "24"
        mac_violation_timer: "0"
        quarantine_mode: "by-vlan"
        sn_dns_resolution: "enable"
        update_user_device: "mac-cache"
        vlan_all_mode: "all"
        vlan_optimization: "enable"
```

## [Return Values](fortios_switch_controller_global_module.md#id6)

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
