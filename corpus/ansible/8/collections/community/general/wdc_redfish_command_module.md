---
collection: ansible
version: "8"
title: "community.general.wdc_redfish_command module – Manages WDC UltraStar Data102 Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/wdc_redfish_command_module.html
fetched_at: 2026-07-28T01:51:22+00:00
---
# community.general.wdc_redfish_command module – Manages WDC UltraStar Data102 Out-Of-Band controllers using Redfish APIs

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
> To use it in a playbook, specify: `community.general.wdc_redfish_command`.

New in community.general 5.4.0

- [Synopsis](wdc_redfish_command_module.md#synopsis)
- [Parameters](wdc_redfish_command_module.md#parameters)
- [Attributes](wdc_redfish_command_module.md#attributes)
- [Notes](wdc_redfish_command_module.md#notes)
- [Examples](wdc_redfish_command_module.md#examples)
- [Return Values](wdc_redfish_command_module.md#return-values)

## [Synopsis](wdc_redfish_command_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to perform an action.
- Manages OOB controller firmware. For example, Firmware Activate, Update and Activate.

Aliases: remote_management.redfish.wdc_redfish_command

## [Parameters](wdc_redfish_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Security token for authentication with OOB controller. |
| **baseuri**  string | Base URI of OOB controller. Must include this or `ioms`. |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **ioms**  list / elements=string | List of IOM FQDNs for the enclosure. Must include this or `baseuri`. |
| **password**  string | Password for authentication with OOB controller. |
| **resource_id**  string  *added in community.general 5.4.0* | ID of the component to modify, such as `Enclosure`, `IOModuleAFRU`, `PowerSupplyBFRU`, `FanExternalFRU3`, or `FanInternalFRU`. |
| **timeout**  integer | Timeout in seconds for URL requests to OOB controller.  **Default:** `10` |
| **update_creds**  dictionary | The credentials for retrieving the update image. |
| **password**  string | The password for retrieving the update image. |
| **username**  string | The username for retrieving the update image. |
| **update_image_uri**  string | The URI of the image for the update. |
| **username**  string | User for authentication with OOB controller. |

## [Attributes](wdc_redfish_command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](wdc_redfish_command_module.md#id4)

> **Note:**
>
> - In the inventory, you can specify baseuri or ioms. See the EXAMPLES section.
> - ioms is a list of FQDNs for the enclosure’s IOMs.

## [Examples](wdc_redfish_command_module.md#id5)

```yaml+jinja
- name: Firmware Activate (required after SimpleUpdate to apply the new firmware)
  community.general.wdc_redfish_command:
    category: Update
    command: FWActivate
    ioms: "{{ ioms }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Firmware Activate with individual IOMs specified
  community.general.wdc_redfish_command:
    category: Update
    command: FWActivate
    ioms:
      - iom1.wdc.com
      - iom2.wdc.com
    username: "{{ username }}"
    password: "{{ password }}"

- name: Firmware Activate with baseuri specified
  community.general.wdc_redfish_command:
    category: Update
    command: FWActivate
    baseuri: "iom1.wdc.com"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Update and Activate (orchestrates firmware update and activation with a single command)
  community.general.wdc_redfish_command:
    category: Update
    command: UpdateAndActivate
    ioms: "{{ ioms }}"
    username: "{{ username }}"
    password: "{{ password }}"
    update_image_uri: "{{ update_image_uri }}"
    update_creds:
      username: operator
      password: supersecretpwd

- name: Turn on enclosure indicator LED
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: Enclosure
    command: IndicatorLedOn
    username: "{{ username }}"
    password: "{{ password }}"

- name: Turn off IOM A indicator LED
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: IOModuleAFRU
    command: IndicatorLedOff
    username: "{{ username }}"
    password: "{{ password }}"

- name: Turn on Power Supply B indicator LED
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: PowerSupplyBFRU
    command: IndicatorLedOn
    username: "{{ username }}"
    password: "{{ password }}"

- name: Turn on External Fan 3 indicator LED
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: FanExternalFRU3
    command: IndicatorLedOn
    username: "{{ username }}"
    password: "{{ password }}"

- name: Turn on Internal Fan indicator LED
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: FanInternalFRU
    command: IndicatorLedOn
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set chassis to Low Power Mode
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: Enclosure
    command: PowerModeLow

- name: Set chassis to Normal Power Mode
  community.general.wdc_redfish_command:
    category: Chassis
    resource_id: Enclosure
    command: PowerModeNormal
```

## [Return Values](wdc_redfish_command_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message with action result or error description  **Returned:** always  **Sample:** `"Action was successful"` |

### Authors

- Mike Moerk (@mikemoerk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
