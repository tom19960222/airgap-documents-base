---
collection: ansible
version: "6"
title: "theforeman.foreman.content_view_version module – Manage Content View Versions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/content_view_version_module.html
fetched_at: 2026-07-28T00:20:39+00:00
---
# theforeman.foreman.content_view_version module – Manage Content View Versions

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
> see [Requirements](content_view_version_module.md#ansible-collections-theforeman-foreman-content-view-version-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_view_version`.

New in theforeman.foreman 1.0.0

- [Synopsis](content_view_version_module.md#synopsis)
- [Requirements](content_view_version_module.md#requirements)
- [Parameters](content_view_version_module.md#parameters)
- [Notes](content_view_version_module.md#notes)
- [Examples](content_view_version_module.md#examples)
- [Return Values](content_view_version_module.md#return-values)

## [Synopsis](content_view_version_module.md#id1)

- Publish, Promote or Remove a Content View Version

## [Requirements](content_view_version_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_view_version_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content_view**  string / required | Name of the content view |
| **current_lifecycle_environment**  string | The lifecycle environment that is already associated with the content view version  Helpful for promoting a content view version |
| **description**  string | Description of the Content View Version |
| **force_promote**  aliases: force  boolean | Force content view promotion and bypass lifecycle environment restriction  Choices:   - `false` ← (default) - `true` |
| **force_yum_metadata_regeneration**  boolean | Force metadata regeneration when performing Publish and Promote tasks  Choices:   - `false` ← (default) - `true` |
| **lifecycle_environments**  list / elements=string | The lifecycle environments the Content View Version should be in. |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **version**  string | The content view version number (i.e. 1.0) |

## [Notes](content_view_version_module.md#id4)

> **Note:**
>
> - You cannot use this to remove a Content View Version from a Lifecycle environment, you should promote another version first.
> - For idempotency you must specify either `version` or `current_lifecycle_environment`.

## [Examples](content_view_version_module.md#id5)

```yaml+jinja
- name: "Ensure content view version 2.0 is in Test & Pre Prod"
  theforeman.foreman.content_view_version:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    content_view: "CV 1"
    organization: "Default Organization"
    version: "2.0"
    lifecycle_environments:
      - Test
      - Pre Prod

- name: "Ensure content view version in Test is also in Pre Prod"
  theforeman.foreman.content_view_version:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    content_view: "CV 1"
    organization: "Default Organization"
    current_lifecycle_environment: Test
    lifecycle_environments:
      - Pre Prod

- name: "Publish a content view, not idempotent"
  theforeman.foreman.content_view_version:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    content_view: "CV 1"
    organization: "Default Organization"

- name: "Publish a content view and promote that version to Library & Dev, not idempotent"
  theforeman.foreman.content_view_version:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    content_view: "CV 1"
    organization: "Default Organization"
    lifecycle_environments:
      - Library
      - Dev

- name: "Ensure content view version 1.0 doesn't exist"
  theforeman.foreman.content_view_version:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    content_view: "Web Servers"
    organization: "Default Organization"
    version: "1.0"
    state: absent

# Obtain information about a Content View and its versions
- name: find all CVs
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    resource: content_views
    search: 'name="Example Content"'
  register: example_content

# Obtain more details about all versions of a specific Content View
- name: "find content view versions of {{ cv_id }}"
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    resource: content_view_versions
    params:
      content_view_id: "{{ example_content.resources[0].id }}"
  register: version_information
```

## [Return Values](content_view_version_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **content_view_versions**  list / elements=dictionary | List of content view versions.  Returned: success |

### Authors

- Sean O’Keeffe (@sean797)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
