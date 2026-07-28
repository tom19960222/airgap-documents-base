---
collection: ansible
version: "6"
title: "theforeman.foreman.host_collection module – Manage Host Collections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/host_collection_module.html
fetched_at: 2026-07-28T00:20:45+00:00
---
# theforeman.foreman.host_collection module – Manage Host Collections

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
> see [Requirements](host_collection_module.md#ansible-collections-theforeman-foreman-host-collection-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.host_collection`.

New in theforeman.foreman 1.0.0

- [Synopsis](host_collection_module.md#synopsis)
- [Requirements](host_collection_module.md#requirements)
- [Parameters](host_collection_module.md#parameters)
- [Examples](host_collection_module.md#examples)
- [Return Values](host_collection_module.md#return-values)

## [Synopsis](host_collection_module.md#id1)

- Create and Manage host collections

## [Requirements](host_collection_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](host_collection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the host collection |
| **name**  string / required | Name of the host collection |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | New name of the host collection. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](host_collection_module.md#id4)

```yaml+jinja
- name: "Create Foo host collection"
  theforeman.foreman.host_collection:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Foo"
    description: "Foo host collection for Foo servers"
    organization: "My Cool new Organization"
    state: present
```

## [Return Values](host_collection_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **host_collections**  list / elements=dictionary | List of host collections.  Returned: success |

### Authors

- Maxim Burgerhout (@wzzrd)
- Christoffer Reijer (@ephracis)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
