---
collection: ansible
version: "6"
title: "theforeman.foreman.bookmark module – Manage Bookmarks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/bookmark_module.html
fetched_at: 2026-07-28T00:20:30+00:00
---
# theforeman.foreman.bookmark module – Manage Bookmarks

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
> see [Requirements](bookmark_module.md#ansible-collections-theforeman-foreman-bookmark-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.bookmark`.

New in theforeman.foreman 1.0.0

- [Synopsis](bookmark_module.md#synopsis)
- [Requirements](bookmark_module.md#requirements)
- [Parameters](bookmark_module.md#parameters)
- [Examples](bookmark_module.md#examples)
- [Return Values](bookmark_module.md#return-values)

## [Synopsis](bookmark_module.md#id1)

- Manage Bookmark Entities

## [Requirements](bookmark_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](bookmark_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **controller**  string / required | Controller for the bookmark |
| **name**  string / required | Name of the bookmark |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **public**  boolean | Make bookmark available for all users  Choices:   - `false` - `true` ← (default) |
| **query**  string | Query of the bookmark |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  Choices:   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](bookmark_module.md#id4)

```yaml+jinja
- name: "Create a Bookmark"
  theforeman.foreman.bookmark:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "recent"
    controller: "job_invocations"
    query: "started_at > '24 hours ago'"
    state: present_with_defaults

- name: "Update a Bookmark"
  theforeman.foreman.bookmark:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "recent"
    controller: "job_invocations"
    query: "started_at > '12 hours ago'"
    state: present

- name: "Delete a Bookmark"
  theforeman.foreman.bookmark:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "recent"
    controller: "job_invocations"
    state: absent
```

## [Return Values](bookmark_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **bookmarks**  list / elements=dictionary | List of bookmarks.  Returned: success |
| **controller**  string | Controller, the query is performed on.  Returned: success |
| **id**  integer | Database id of the bookmark.  Returned: success |
| **name**  string | Name of the bookmark.  Returned: success |
| **owner_id**  integer | Database id of the owner entity.  Returned: success |
| **owner_type**  string | Class of the owner entity.  Returned: success |
| **public**  boolean | Publicity of the bookmark.  Returned: success |
| **query**  string | Query to be performed on the controller.  Returned: success |

### Authors

- Bernhard Hopfenmueller (@Fobhep) ATIX AG
- Christoffer Reijer (@ephracis) Basalt AB

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
