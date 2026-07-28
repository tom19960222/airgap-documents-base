---
collection: ansible
version: "8"
title: "community.general.idrac_redfish_config module – Manages servers through iDRAC using Dell Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/idrac_redfish_config_module.html
fetched_at: 2026-07-28T01:46:22+00:00
---
# community.general.idrac_redfish_config module – Manages servers through iDRAC using Dell Redfish APIs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.idrac_redfish_config`.

- [Synopsis](idrac_redfish_config_module.md#synopsis)
- [Parameters](idrac_redfish_config_module.md#parameters)
- [Attributes](idrac_redfish_config_module.md#attributes)
- [Examples](idrac_redfish_config_module.md#examples)
- [Return Values](idrac_redfish_config_module.md#return-values)

## [Synopsis](idrac_redfish_config_module.md#id1)

- For use with Dell iDRAC operations that require Redfish OEM extensions
- Builds Redfish URIs locally and sends them to remote iDRAC controllers to set or update a configuration attribute.

Aliases: remote_management.redfish.idrac_redfish_config

## [Parameters](idrac_redfish_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string  *added in community.general 2.3.0* | Security token for authenticating to iDRAC. |
| **baseuri**  string / required | Base URI of iDRAC. |
| **category**  string / required | Category to execute on iDRAC. |
| **command**  list / elements=string / required | List of commands to execute on iDRAC.  `SetManagerAttributes`, `SetLifecycleControllerAttributes` and `SetSystemAttributes` are mutually exclusive commands when `category` is `Manager`. |
| **manager_attributes**  dictionary  *added in community.general 0.2.0* | Dictionary of iDRAC attribute name and value pairs to update.  **Default:** `{}` |
| **password**  string | Password for authenticating to iDRAC. |
| **resource_id**  string  *added in community.general 0.2.0* | ID of the System, Manager or Chassis to modify. |
| **timeout**  integer | Timeout in seconds for HTTP requests to iDRAC.  **Default:** `10` |
| **username**  string | Username for authenticating to iDRAC. |

## [Attributes](idrac_redfish_config_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](idrac_redfish_config_module.md#id4)

```yaml+jinja
- name: Enable NTP and set NTP server and Time zone attributes in iDRAC
  community.general.idrac_redfish_config:
    category: Manager
    command: SetManagerAttributes
    resource_id: iDRAC.Embedded.1
    manager_attributes:
      NTPConfigGroup.1.NTPEnable: "Enabled"
      NTPConfigGroup.1.NTP1: "{{ ntpserver1 }}"
      Time.1.Timezone: "{{ timezone }}"
    baseuri: "{{ baseuri }}"
    username: "{{ username}}"
    password: "{{ password }}"

- name: Enable Syslog and set Syslog servers in iDRAC
  community.general.idrac_redfish_config:
    category: Manager
    command: SetManagerAttributes
    resource_id: iDRAC.Embedded.1
    manager_attributes:
      SysLog.1.SysLogEnable: "Enabled"
      SysLog.1.Server1: "{{ syslog_server1 }}"
      SysLog.1.Server2: "{{ syslog_server2 }}"
    baseuri: "{{ baseuri }}"
    username: "{{ username}}"
    password: "{{ password }}"

- name: Configure SNMP community string, port, protocol and trap format
  community.general.idrac_redfish_config:
    category: Manager
    command: SetManagerAttributes
    resource_id: iDRAC.Embedded.1
    manager_attributes:
      SNMP.1.AgentEnable: "Enabled"
      SNMP.1.AgentCommunity: "public_community_string"
      SNMP.1.TrapFormat: "SNMPv1"
      SNMP.1.SNMPProtocol: "All"
      SNMP.1.DiscoveryPort: 161
      SNMP.1.AlertPort: 162
    baseuri: "{{ baseuri }}"
    username: "{{ username}}"
    password: "{{ password }}"

- name: Enable CSIOR
  community.general.idrac_redfish_config:
    category: Manager
    command: SetLifecycleControllerAttributes
    resource_id: iDRAC.Embedded.1
    manager_attributes:
      LCAttributes.1.CollectSystemInventoryOnRestart: "Enabled"
    baseuri: "{{ baseuri }}"
    username: "{{ username}}"
    password: "{{ password }}"

- name: Set Power Supply Redundancy Policy to A/B Grid Redundant
  community.general.idrac_redfish_config:
    category: Manager
    command: SetSystemAttributes
    resource_id: iDRAC.Embedded.1
    manager_attributes:
      ServerPwr.1.PSRedPolicy: "A/B Grid Redundant"
    baseuri: "{{ baseuri }}"
    username: "{{ username}}"
    password: "{{ password }}"
```

## [Return Values](idrac_redfish_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message with action result or error description  **Returned:** always  **Sample:** `"Action was successful"` |

### Authors

- Jose Delarosa (@jose-delarosa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
