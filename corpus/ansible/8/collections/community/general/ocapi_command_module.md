---
collection: ansible
version: "8"
title: "community.general.ocapi_command module – Manages Out-Of-Band controllers using Open Composable API (OCAPI)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ocapi_command_module.html
fetched_at: 2026-07-28T01:48:14+00:00
---
# community.general.ocapi_command module – Manages Out-Of-Band controllers using Open Composable API (OCAPI)

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
> To use it in a playbook, specify: `community.general.ocapi_command`.

New in community.general 6.3.0

- [Synopsis](ocapi_command_module.md#synopsis)
- [Parameters](ocapi_command_module.md#parameters)
- [Attributes](ocapi_command_module.md#attributes)
- [Examples](ocapi_command_module.md#examples)
- [Return Values](ocapi_command_module.md#return-values)

## [Synopsis](ocapi_command_module.md#id1)

- Builds OCAPI URIs locally and sends them to remote OOB controllers to perform an action.
- Manages OOB controller such as Indicator LED, Reboot, Power Mode, Firmware Update.

## [Parameters](ocapi_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | Base URI of OOB controller. |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  string / required | Command to execute on OOB controller. |
| **job_name**  string | For `command=DeleteJob` command, the name of the job to delete. |
| **password**  string / required | Password for authenticating to OOB controller. |
| **proxy_slot_number**  integer | For proxied inband requests, the slot number of the IOM. Only applies if `baseuri` is a proxy server. |
| **timeout**  integer | Timeout in seconds for URL requests to OOB controller.  **Default:** `10` |
| **update_image_path**  string | For `command=FWUpload`, the path on the local filesystem of the firmware update image. |
| **username**  string / required | Username for authenticating to OOB controller. |

## [Attributes](ocapi_command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ocapi_command_module.md#id4)

```yaml+jinja
- name: Set the power state to low
  community.general.ocapi_command:
    category: Chassis
    command: PowerModeLow
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Set the power state to normal
  community.general.ocapi_command:
    category: Chassis
    command: PowerModeNormal
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
- name: Set chassis indicator LED to on
  community.general.ocapi_command:
    category: Chassis
    command: IndicatorLedOn
    baseuri: "{{ baseuri }}"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
- name: Set chassis indicator LED to off
  community.general.ocapi_command:
    category: Chassis
    command: IndicatorLedOff
    baseuri: "{{ baseuri }}"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
- name: Reset Enclosure
  community.general.ocapi_command:
    category: Systems
    command: PowerGracefulRestart
    baseuri: "{{ baseuri }}"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
- name: Firmware Upload
  community.general.ocapi_command:
    category: Update
    command: FWUpload
    baseuri: "iom1.wdc.com"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
    update_image_path: "/path/to/firmware.tar.gz"
- name: Firmware Update
  community.general.ocapi_command:
    category: Update
    command: FWUpdate
    baseuri: "iom1.wdc.com"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
- name: Firmware Activate
  community.general.ocapi_command:
    category: Update
    command: FWActivate
    baseuri: "iom1.wdc.com"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
- name: Delete Job
  community.general.ocapi_command:
    category: Jobs
    command: DeleteJob
    job_name: FirmwareUpdate
    baseuri: "{{ baseuri }}"
    proxy_slot_number: 2
    username: "{{ username }}"
    password: "{{ password }}"
```

## [Return Values](ocapi_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **jobUri**  string | URI to use to monitor status of the operation. Returned for async commands such as Firmware Update, Firmware Activate.  **Returned:** when supported  **Sample:** `"https://ioma.wdc.com/Storage/Devices/openflex-data24-usalp03020qb0003/Jobs/FirmwareUpdate/"` |
| **msg**  string | Message with action result or error description.  **Returned:** always  **Sample:** `"Action was successful"` |
| **operationStatusId**  integer | OCAPI State ID (see OCAPI documentation for possible values).  **Returned:** when supported  **Sample:** `2` |

### Authors

- Mike Moerk (@mikemoerk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
