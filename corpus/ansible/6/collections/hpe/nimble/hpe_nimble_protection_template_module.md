---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_protection_template module – Manage the HPE Nimble Storage protection templates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_protection_template_module.html
fetched_at: 2026-07-27T17:50:07+00:00
---
# hpe.nimble.hpe_nimble_protection_template module – Manage the HPE Nimble Storage protection templates

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/hpe/nimble) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_protection_template_module.md#ansible-collections-hpe-nimble-hpe-nimble-protection-template-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_protection_template`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_protection_template_module.md#synopsis)
- [Requirements](hpe_nimble_protection_template_module.md#requirements)
- [Parameters](hpe_nimble_protection_template_module.md#parameters)
- [Notes](hpe_nimble_protection_template_module.md#notes)
- [Examples](hpe_nimble_protection_template_module.md#examples)

## [Synopsis](hpe_nimble_protection_template_module.md#id1)

- Manage the protection templates on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_protection_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_protection_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **agent_hostname**  string | Generic backup agent hostname. |
| **agent_password**  string | Generic backup agent password. |
| **agent_username**  string | Generic backup agent username. |
| **app_cluster**  string | If the application is running within a windows cluster environment, this is the cluster name. |
| **app_id**  string | Application ID running on the server.  Choices:   - `"inval"` - `"exchange"` - `"exchange_dag"` - `"hyperv"` - `"sql2005"` - `"sql2008"` - `"sql2012"` - `"sql2014"` - `"sql2016"` - `"sql2017"` |
| **app_server**  string | Application server hostname. |
| **app_service_name**  string | If the application is running within a windows cluster environment then this is the instance name of the service running within the cluster environment. |
| **app_sync**  string | Application synchronization.  Choices:   - `"none"` - `"vss"` - `"vmware"` - `"generic"` |
| **change_name**  string | Change name of the existing protection template. |
| **description**  string | Text description of protection template. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **name**  string / required | Name of the protection template. |
| **password**  string / required | HPE Nimble Storage password. |
| **state**  string / required | The protection template operations.  Choices:   - `"present"` - `"absent"` - `"create"` |
| **username**  string / required | HPE Nimble Storage user name. |
| **vcenter_hostname**  string | VMware vCenter hostname. |
| **vcenter_password**  string | Application VMware vCenter password. A password with few constraints. |
| **vcenter_username**  string | Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\), dash (-), period (.), and underscore (_). |

## [Notes](hpe_nimble_protection_template_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_protection_template_module.md#id5)

```yaml+jinja
# if state is create , then create a protection template if not present. Fails if already present.
# if state is present, then create a protection template if not present. Succeed if it already exists.
- name: Create protection template if not present
  hpe.nimble.hpe_nimble_protection_template:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    description: "{{ description | default(None)}}"
    state: "{{ state | default('present') }}"

- name: Delete protection template
  hpe.nimble.hpe_nimble_protection_template:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: absent
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
