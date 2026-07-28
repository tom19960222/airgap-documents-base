---
collection: ansible
version: "6"
title: "community.general.ilo_redfish_info module – Gathers server information through iLO using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ilo_redfish_info_module.html
fetched_at: 2026-07-27T17:09:41+00:00
---
# community.general.ilo_redfish_info module – Gathers server information through iLO using Redfish APIs

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
> To use it in a playbook, specify: `community.general.ilo_redfish_info`.

New in community.general 4.2.0

- [Synopsis](ilo_redfish_info_module.md#synopsis)
- [Parameters](ilo_redfish_info_module.md#parameters)
- [Examples](ilo_redfish_info_module.md#examples)
- [Return Values](ilo_redfish_info_module.md#return-values)

## [Synopsis](ilo_redfish_info_module.md#id1)

- Builds Redfish URIs locally and sends them to iLO to get information back.
- For use with HPE iLO operations that require Redfish OEM extensions.

## [Parameters](ilo_redfish_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Security token for authenticating to iLO. |
| **baseuri**  string / required | Base URI of iLO. |
| **category**  list / elements=string / required | List of categories to execute on iLO. |
| **command**  list / elements=string / required | List of commands to execute on iLO. |
| **password**  string | Password for authenticating to iLO. |
| **timeout**  integer | Timeout in seconds for HTTP requests to iLO.  Default: `10` |
| **username**  string | Username for authenticating to iLO. |

## [Examples](ilo_redfish_info_module.md#id3)

```yaml+jinja
- name: Get iLO Sessions
  community.general.ilo_redfish_info:
    category: Sessions
    command: GetiLOSessions
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result_sessions
```

## [Return Values](ilo_redfish_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ilo_redfish_info**  dictionary | Returns iLO sessions.  Returned: always |
| **GetiLOSessions**  dictionary | Returns the iLO session msg and whether the function executed successfully.  Returned: success |
| **msg**  list / elements=dictionary | Information of all active iLO sessions.  Returned: success |
| **Description**  string | Provides a description of the resource.  Returned: success |
| **Id**  string | The sessionId.  Returned: success |
| **Name**  string | The name of the resource.  Returned: success |
| **UserName**  string | Name to use to log in to the management processor.  Returned: success |
| **ret**  boolean | Check variable to see if the information was successfully retrieved.  Returned: success |

### Authors

- Bhavya B (@bhavya06)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
