---
collection: ansible
version: "8"
title: "community.general.ilo_redfish_command module – Manages Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ilo_redfish_command_module.html
fetched_at: 2026-07-28T01:46:24+00:00
---
# community.general.ilo_redfish_command module – Manages Out-Of-Band controllers using Redfish APIs

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
> To use it in a playbook, specify: `community.general.ilo_redfish_command`.

New in community.general 6.6.0

- [Synopsis](ilo_redfish_command_module.md#synopsis)
- [Parameters](ilo_redfish_command_module.md#parameters)
- [Attributes](ilo_redfish_command_module.md#attributes)
- [Examples](ilo_redfish_command_module.md#examples)
- [Return Values](ilo_redfish_command_module.md#return-values)

## [Synopsis](ilo_redfish_command_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to perform an action.

## [Parameters](ilo_redfish_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Security token for authenticating to iLO. |
| **baseuri**  string / required | Base URI of OOB controller. |
| **category**  string / required | Category to execute on OOB controller.  **Choices:**   - `"Systems"` |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **password**  string | Password for authenticating to iLO. |
| **timeout**  integer | Timeout in seconds for HTTP requests to iLO.  **Default:** `60` |
| **username**  string | Username for authenticating to iLO. |

## [Attributes](ilo_redfish_command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ilo_redfish_command_module.md#id4)

```yaml+jinja
- name: Wait for iLO Reboot Completion
  community.general.ilo_redfish_command:
    category: Systems
    command: WaitforiLORebootCompletion
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
```

## [Return Values](ilo_redfish_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ilo_redfish_command**  dictionary | Returns the status of the operation performed on the iLO.  **Returned:** always |
| **WaitforiLORebootCompletion**  dictionary | Returns the output msg and whether the function executed successfully.  **Returned:** success |
| **msg**  string | Status of the operation performed on the iLO.  **Returned:** success |
| **ret**  boolean | Return True/False based on whether the operation was performed successfully.  **Returned:** success |

### Authors

- Varni H P (@varini-hp)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
