---
collection: ansible
version: "6"
title: "community.general.proxmox_tasks_info module – Retrieve information about one or more Proxmox VE tasks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/proxmox_tasks_info_module.html
fetched_at: 2026-07-27T17:12:11+00:00
---
# community.general.proxmox_tasks_info module – Retrieve information about one or more Proxmox VE tasks

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](proxmox_tasks_info_module.md#ansible-collections-community-general-proxmox-tasks-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_tasks_info`.

New in community.general 3.8.0

- [Synopsis](proxmox_tasks_info_module.md#synopsis)
- [Requirements](proxmox_tasks_info_module.md#requirements)
- [Parameters](proxmox_tasks_info_module.md#parameters)
- [Examples](proxmox_tasks_info_module.md#examples)
- [Return Values](proxmox_tasks_info_module.md#return-values)

## [Synopsis](proxmox_tasks_info_module.md#id1)

- Retrieve information about one or more Proxmox VE tasks.

## [Requirements](proxmox_tasks_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_tasks_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use `PROXMOX_PASSWORD` environment variable. |
| **api_token_id**  string  added in community.general 1.3.0 | Specify the token ID. |
| **api_token_secret**  string  added in community.general 1.3.0 | Specify the token secret. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **node**  string / required | Node where to get tasks. |
| **task**  aliases: upid, name  string | Return specific task. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` ← (default) - `true` |

## [Examples](proxmox_tasks_info_module.md#id4)

```yaml+jinja
- name: List tasks on node01
  community.general.proxmox_task_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    api_token_id: '{{ token_id | default(omit) }}'
    api_token_secret: '{{ token_secret | default(omit) }}'
    node: node01
  register: result

- name: Retrieve information about specific tasks on node01
  community.general.proxmox_task_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    api_token_id: '{{ token_id | default(omit) }}'
    api_token_secret: '{{ token_secret | default(omit) }}'
    task: 'UPID:node01:00003263:16167ACE:621EE230:srvreload:networking:root@pam:'
    node: node01
  register: proxmox_tasks
```

## [Return Values](proxmox_tasks_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Short message.  Returned: on failure  Sample: `"Task: UPID:xyz:xyz does not exist on node: proxmoxnode"` |
| **proxmox_tasks**  list / elements=dictionary | List of tasks.  Returned: on success |
| **endtime**  integer | Endtime of the task.  Returned: on success, can be absent |
| **failed**  boolean | If the task failed.  Returned: when status is defined |
| **id**  string | ID of the task.  Returned: on success |
| **node**  string | Node name.  Returned: on success |
| **pid**  integer | PID of the task.  Returned: on success |
| **pstart**  integer | pastart of the task.  Returned: on success |
| **starttime**  integer | Starting time of the task.  Returned: on success |
| **status**  string | Status of the task.  Returned: on success, can be absent |
| **type**  string | Type of the task.  Returned: on success |
| **upid**  string | UPID of the task.  Returned: on success |
| **user**  string | User that owns the task.  Returned: on success |

### Authors

- Andreas Botzner (@paginabianca) <andreas at botzner dot com>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
