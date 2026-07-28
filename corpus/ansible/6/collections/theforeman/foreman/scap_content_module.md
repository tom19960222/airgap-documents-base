---
collection: ansible
version: "6"
title: "theforeman.foreman.scap_content module – Manage SCAP content"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/scap_content_module.html
fetched_at: 2026-07-28T00:21:06+00:00
---
# theforeman.foreman.scap_content module – Manage SCAP content

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
> see [Requirements](scap_content_module.md#ansible-collections-theforeman-foreman-scap-content-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.scap_content`.

New in theforeman.foreman 1.0.0

- [Synopsis](scap_content_module.md#synopsis)
- [Requirements](scap_content_module.md#requirements)
- [Parameters](scap_content_module.md#parameters)
- [Examples](scap_content_module.md#examples)
- [Return Values](scap_content_module.md#return-values)

## [Synopsis](scap_content_module.md#id1)

- Create, update, and delete SCAP content

## [Requirements](scap_content_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](scap_content_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **original_filename**  string | Original file name of the XML file.  If unset, the filename of *scap_file* will be used. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **scap_file**  path | File containing XML DataStream content.  Required when creating a new DataStream. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **title**  string / required | Title of SCAP content. |
| **updated_title**  string | New SCAP content title.  When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](scap_content_module.md#id4)

```yaml+jinja
- name: Create SCAP content
  theforeman.foreman.scap_content:
    title: "Red Hat firefox default content"
    scap_file: "/home/user/Downloads/ssg-firefox-ds.xml"
    original_filename: "ssg-firefox-ds.xml"
    organizations:
      - "Default Organization"
    locations:
      - "Default Location"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Update SCAP content
  theforeman.foreman.scap_content:
    title: "Red Hat firefox default content"
    updated_title: "Updated scap content title"
    scap_file: "/home/user/Downloads/updated-ssg-firefox-ds.xml"
    original_filename: "updated-ssg-firefox-ds.xml"
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

- name: Delete SCAP content
  theforeman.foreman.scap_content:
    title: "Red Hat firefox default content"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: absent
```

## [Return Values](scap_content_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **scap_contents**  list / elements=dictionary | List of scap contents.  Returned: success |

### Authors

- Jameer Pathan (@jameerpathan111)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
