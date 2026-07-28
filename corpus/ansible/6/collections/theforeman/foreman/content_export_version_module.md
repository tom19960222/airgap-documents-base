---
collection: ansible
version: "6"
title: "theforeman.foreman.content_export_version module – Manage content view version content exports"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/content_export_version_module.html
fetched_at: 2026-07-28T00:20:36+00:00
---
# theforeman.foreman.content_export_version module – Manage content view version content exports

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](content_export_version_module.md#ansible-collections-theforeman-foreman-content-export-version-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_export_version`.

New in theforeman.foreman 3.6.0

- [Synopsis](content_export_version_module.md#synopsis)
- [Requirements](content_export_version_module.md#requirements)
- [Parameters](content_export_version_module.md#parameters)
- [Examples](content_export_version_module.md#examples)

## [Synopsis](content_export_version_module.md#id1)

- Export a content view version to a directory.

## [Requirements](content_export_version_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_export_version_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chunk_size_gb**  integer | Split the exported content into archives no greater than the specified size in gigabytes. |
| **content_view**  string / required | Content view name. |
| **content_view_version**  string / required | Content view version, e.g. “7.0” |
| **destination_server**  string | Destination server name; optional parameter to differentiate between exports |
| **fail_on_missing_content**  boolean | Fails if any of the repositories belonging to this version are unexportable.  Choices:   - `false` - `true` |
| **from_history_id**  integer | Export history identifier used for incremental export. If not provided the most recent export history will be used. |
| **incremental**  boolean | Export only the content that has changed since the last export.  Choices:   - `false` - `true` |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](content_export_version_module.md#id4)

```yaml+jinja
- name: "Export content view version (full)"
  theforeman.foreman.content_export_version:
    content_view: RHEL8
    content_view_version: '1.0'
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    destination_server: "airgapped.example.com"

- name: "Export content view version (full) in chunks of 10 GB"
  theforeman.foreman.content_export_version:
    content_view: RHEL8
    content_view_version: '1.0'
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    destination_server: "airgapped.example.com"
    chunk_size_gb: 10

- name: "Export content view version (full) and fail if any repos are unexportable"
  theforeman.foreman.content_export_version:
    content_view: RHEL8
    content_view_version: '1.0'
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    destination_server: "airgapped.example.com"
    fail_on_missing_content: true

- name: "Export content view version (incremental) since the most recent export"
  theforeman.foreman.content_export_version:
      content_view: RHEL8
      content_view_version: '1.0'
      username: "admin"
      password: "changeme"
      server_url: "https://foreman.example.com"
      organization: "Default Organization"
      destination_server: "airgapped.example.com"
      incremental: true

- name: "Export content view version (incremental) since a specific export"
  theforeman.foreman.content_export_version:
      content_view: RHEL8
      content_view_version: '1.0'
      username: "admin"
      password: "changeme"
      server_url: "https://foreman.example.com"
      organization: "Default Organization"
      destination_server: "airgapped.example.com"
      incremental: true
      from_history_id: 12345
```

### Authors

- Jeremy Lenz (@jeremylenz)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
