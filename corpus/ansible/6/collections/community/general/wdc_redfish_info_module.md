---
collection: ansible
version: "6"
title: "community.general.wdc_redfish_info module – Manages WDC UltraStar Data102 Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/wdc_redfish_info_module.html
fetched_at: 2026-07-27T17:13:58+00:00
---
# community.general.wdc_redfish_info module – Manages WDC UltraStar Data102 Out-Of-Band controllers using Redfish APIs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.wdc_redfish_info`.

New in community.general 5.4.0

- [Synopsis](wdc_redfish_info_module.md#synopsis)
- [Parameters](wdc_redfish_info_module.md#parameters)
- [Notes](wdc_redfish_info_module.md#notes)
- [Examples](wdc_redfish_info_module.md#examples)
- [Return Values](wdc_redfish_info_module.md#return-values)

## [Synopsis](wdc_redfish_info_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to get information back.

## [Parameters](wdc_redfish_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Security token for authentication with OOB controller. |
| **baseuri**  string | Base URI of OOB controller. Must include this or *ioms*. |
| **category**  string / required | Category to execute on OOB controller. |
| **command**  list / elements=string / required | List of commands to execute on OOB controller. |
| **ioms**  list / elements=string | List of IOM FQDNs for the enclosure. Must include this or *baseuri*. |
| **password**  string | Password for authentication with OOB controller. |
| **timeout**  integer | Timeout in seconds for URL requests to OOB controller.  Default: `10` |
| **username**  string | User for authentication with OOB controller. |

## [Notes](wdc_redfish_info_module.md#id3)

> **Note:**
>
> - In the inventory, you can specify baseuri or ioms. See the EXAMPLES section.
> - ioms is a list of FQDNs for the enclosure’s IOMs.

## [Examples](wdc_redfish_info_module.md#id4)

```yaml+jinja
- name: Get Simple Update Status with individual IOMs specified
  community.general.wdc_redfish_info:
    category: Update
    command: SimpleUpdateStatus
    ioms:
      - iom1.wdc.com
      - iom2.wdc.com
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.simple_update_status.entries | to_nice_json }}"

- name: Get Simple Update Status with baseuri specified
  community.general.wdc_redfish_info:
    category: Update
    command: SimpleUpdateStatus
    baseuri: "iom1.wdc.com"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.simple_update_status.entries | to_nice_json }}"
```

## [Return Values](wdc_redfish_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **Description**  string | Firmware update status description.  Returned: always  Sample: `"Ready for FW update"` |
| **ErrorCode**  integer | Numeric error code for firmware update status. Non-zero indicates an error condition.  Returned: always  Sample: `0` |
| **EstimatedRemainingMinutes**  integer | Estimated number of minutes remaining in firmware update operation.  Returned: always  Sample: `20` |
| **StatusCode**  integer | Firmware update status code.  Returned: always  Sample: `2` |

### Authors

- Mike Moerk (@mikemoerk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
