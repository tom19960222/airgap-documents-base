---
collection: ansible
version: "6"
title: "theforeman.foreman.domain module – Manage Domains"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/domain_module.html
fetched_at: 2026-07-28T00:20:41+00:00
---
# theforeman.foreman.domain module – Manage Domains

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
> see [Requirements](domain_module.md#ansible-collections-theforeman-foreman-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.domain`.

New in theforeman.foreman 1.0.0

- [Synopsis](domain_module.md#synopsis)
- [Requirements](domain_module.md#requirements)
- [Parameters](domain_module.md#parameters)
- [Examples](domain_module.md#examples)
- [Return Values](domain_module.md#return-values)

## [Synopsis](domain_module.md#id1)

- Create, update, and delete Domains

## [Requirements](domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: fullname  string | Full name describing the domain |
| **dns_proxy**  aliases: dns  string | DNS proxy to use within this domain for managing A records |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | The full DNS domain name |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **parameters**  list / elements=dictionary | Domain specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  Choices:   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **updated_name**  string | New domain name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](domain_module.md#id4)

```yaml+jinja
- name: domain
  theforeman.foreman.domain:
    name: "example.org"
    description: "Example Domain"
    locations:
      - "Munich"
    organizations:
      - "ACME"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](domain_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **domains**  list / elements=dictionary | List of domains.  Returned: success |

### Authors

- Markus Bucher (@m-bucher) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
