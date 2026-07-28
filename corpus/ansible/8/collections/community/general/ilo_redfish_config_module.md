---
collection: ansible
version: "8"
title: "community.general.ilo_redfish_config module – Sets or updates configuration attributes on HPE iLO with Redfish OEM extensions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ilo_redfish_config_module.html
fetched_at: 2026-07-28T01:46:25+00:00
---
# community.general.ilo_redfish_config module – Sets or updates configuration attributes on HPE iLO with Redfish OEM extensions

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
> To use it in a playbook, specify: `community.general.ilo_redfish_config`.

New in community.general 4.2.0

- [Synopsis](ilo_redfish_config_module.md#synopsis)
- [Parameters](ilo_redfish_config_module.md#parameters)
- [Attributes](ilo_redfish_config_module.md#attributes)
- [Examples](ilo_redfish_config_module.md#examples)
- [Return Values](ilo_redfish_config_module.md#return-values)

## [Synopsis](ilo_redfish_config_module.md#id1)

- Builds Redfish URIs locally and sends them to iLO to set or update a configuration attribute.
- For use with HPE iLO operations that require Redfish OEM extensions.

Aliases: remote_management.redfish.ilo_redfish_config

## [Parameters](ilo_redfish_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attribute_name**  string / required | Name of the attribute to be configured. |
| **attribute_value**  string | Value of the attribute to be configured. |
| **auth_token**  string | Security token for authenticating to iLO. |
| **baseuri**  string / required | Base URI of iLO. |
| **category**  string / required | Command category to execute on iLO.  **Choices:**   - `"Manager"` |
| **command**  list / elements=string / required | List of commands to execute on iLO. |
| **password**  string | Password for authenticating to iLO. |
| **timeout**  integer | Timeout in seconds for HTTP requests to iLO.  **Default:** `10` |
| **username**  string | Username for authenticating to iLO. |

## [Attributes](ilo_redfish_config_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ilo_redfish_config_module.md#id4)

```yaml+jinja
- name: Disable WINS Registration
  community.general.ilo_redfish_config:
    category: Manager
    command: SetWINSReg
    baseuri: 15.X.X.X
    username: Admin
    password: Testpass123
    attribute_name: WINSRegistration

- name: Set Time Zone
  community.general.ilo_redfish_config:
    category: Manager
    command: SetTimeZone
    baseuri: 15.X.X.X
    username: Admin
    password: Testpass123
    attribute_name: TimeZone
    attribute_value: Chennai

- name: Set NTP Servers
  community.general.ilo_redfish_config:
    category: Manager
    command: SetNTPServers
    baseuri: 15.X.X.X
    username: Admin
    password: Testpass123
    attribute_name: StaticNTPServers
    attribute_value: X.X.X.X
```

## [Return Values](ilo_redfish_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message with action result or error description  **Returned:** always  **Sample:** `"Action was successful"` |

### Authors

- Bhavya B (@bhavya06)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
