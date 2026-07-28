---
collection: ansible
version: "8"
title: "theforeman.foreman.content_export_info module – List content exports"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/content_export_info_module.html
fetched_at: 2026-07-28T02:55:40+00:00
---
# theforeman.foreman.content_export_info module – List content exports

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](content_export_info_module.md#ansible-collections-theforeman-foreman-content-export-info-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_export_info`.

New in theforeman.foreman 3.5.0

- [Synopsis](content_export_info_module.md#synopsis)
- [Requirements](content_export_info_module.md#requirements)
- [Parameters](content_export_info_module.md#parameters)
- [Attributes](content_export_info_module.md#attributes)
- [Examples](content_export_info_module.md#examples)

## [Synopsis](content_export_info_module.md#id1)

- List information about content exports.

## [Requirements](content_export_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_export_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content_view**  string | Content view name. |
| **content_view_version**  string | Content view version. |
| **destination_server**  string | Destination server name |
| **id**  integer | Export history identifier. |
| **location**  string | Label of the Location to scope the search for. |
| **organization**  string / required | Name of the Organization to scope the search for. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **search**  string | Search query to use  If None, all resources are returned. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **type**  string | Specify complete or incremental exports.  **Choices:**   - `"complete"` - `"incremental"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](content_export_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](content_export_info_module.md#id5)

```yaml+jinja
- name: "List all full exports in the organization"
  theforeman.foreman.content_export_info:
    organization: "Default Organization"
    type: complete
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
- name: "Get a specific export history and register the result for the next task"
  vars:
    organization_name: "Export Org"
  theforeman.foreman.content_export_info:
    id: 29
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
  register: result
- name: "Write metadata.json to disk using data from the previous task"
  vars:
    metadata: "{{ result['content_exports'][0]['metadata'] }}"
  ansible.builtin.copy:
    content: "{{ metadata }}"
    dest: ./metadata.json
- name: "List all exports of a specific content view version"
  theforeman.foreman.content_export_info:
    content_view: RHEL8
    content_view_version: '1.0'
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
- name: "List all exports marked for a specific destination server"
  theforeman.foreman.content_export_info:
    destination_server: "airgapped.example.com"
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
- name: "List incremental exports of a specific content view version marked for a specific destination server"
  theforeman.foreman.content_export_info:
    content_view: RHEL8
    destination_server: "airgapped.example.com"
    type: incremental
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
- name: "List all exports of a specific content view marked for a specific destination server"
  theforeman.foreman.content_export_info:
    content_view: RHEL8
    destination_server: "airgapped.example.com"
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
```

### Authors

- Jeremy Lenz (@jeremylenz)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
