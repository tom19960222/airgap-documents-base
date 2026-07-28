---
collection: ansible
version: "8"
title: "theforeman.foreman.scap_tailoring_file module – Manage SCAP Tailoring Files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/scap_tailoring_file_module.html
fetched_at: 2026-07-28T02:56:33+00:00
---
# theforeman.foreman.scap_tailoring_file module – Manage SCAP Tailoring Files

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
> see [Requirements](scap_tailoring_file_module.md#ansible-collections-theforeman-foreman-scap-tailoring-file-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.scap_tailoring_file`.

New in theforeman.foreman 1.0.0

- [Synopsis](scap_tailoring_file_module.md#synopsis)
- [Requirements](scap_tailoring_file_module.md#requirements)
- [Parameters](scap_tailoring_file_module.md#parameters)
- [Attributes](scap_tailoring_file_module.md#attributes)
- [Examples](scap_tailoring_file_module.md#examples)
- [Return Values](scap_tailoring_file_module.md#return-values)

## [Synopsis](scap_tailoring_file_module.md#id1)

- Create, update, and delete SCAP Tailoring Files

Aliases: foreman_scap_tailoring_file

## [Requirements](scap_tailoring_file_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](scap_tailoring_file_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | Name of the tailoring file. |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **original_filename**  string | Original file name of the XML file.  If unset, the filename of *scap_file* will be used. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **scap_file**  path | File containing XML DataStream content.  Required when creating a new DataStream. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | New name of the tailoring file.  When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scap_tailoring_file_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](scap_tailoring_file_module.md#id5)

```yaml+jinja
- name: Create SCAP tailoring file
  theforeman.foreman.scap_tailoring_file:
    name: "Red Hat firefox default content"
    scap_file: "/home/user/Downloads/ssg-firefox-ds-tailoring.xml"
    original_filename: "ssg-firefox-ds-tailoring.xml"
    organizations:
      - "Default Organization"
    locations:
      - "Default Location"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Update SCAP tailoring file
  theforeman.foreman.scap_tailoring_file:
    name: "Red Hat firefox default content"
    updated_name: "Updated tailoring file name"
    scap_file: "/home/user/Downloads/updated-ssg-firefox-ds-tailoring.xml"
    original_filename: "updated-ssg-firefox-ds-tailoring.xml"
    organizations:
      - "Org One"
      - "Org Two"
    locations:
      - "Loc One"
      - "Loc Two"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Delete SCAP tailoring file
  theforeman.foreman.scap_tailoring_file:
    name: "Red Hat firefox default content"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: absent
```

## [Return Values](scap_tailoring_file_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **scap_tailoring_files**  list / elements=dictionary | List of scap tailoring files.  **Returned:** success |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
