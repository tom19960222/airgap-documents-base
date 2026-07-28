---
collection: ansible
version: "6"
title: "theforeman.foreman.discovery_rule module – Manage Host Discovery Rules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/discovery_rule_module.html
fetched_at: 2026-07-28T00:20:40+00:00
---
# theforeman.foreman.discovery_rule module – Manage Host Discovery Rules

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
> see [Requirements](discovery_rule_module.md#ansible-collections-theforeman-foreman-discovery-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.discovery_rule`.

New in theforeman.foreman 3.5.0

- [Synopsis](discovery_rule_module.md#synopsis)
- [Requirements](discovery_rule_module.md#requirements)
- [Parameters](discovery_rule_module.md#parameters)
- [Examples](discovery_rule_module.md#examples)
- [Return Values](discovery_rule_module.md#return-values)

## [Synopsis](discovery_rule_module.md#id1)

- Manage Host Discovery Rules

## [Requirements](discovery_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](discovery_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Enable or disable the rule  Choices:   - `false` - `true` |
| **hostgroup**  string | Hostgroup to assign hosts to  Required if *state=present* |
| **hostname**  string | Hostname to assign to discovered host(s)  When matching multiple hosts, must provide unique hostnames for each of the discovered hosts |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **max_count**  integer | Maximum amount of hosts to provision with the rule  0 means no limit |
| **name**  string / required | Name of the Discovery Rule |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **priority**  integer | Priority of the rule |
| **search**  string | Expression to match newly discovered hosts with  Required if *state=present* |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](discovery_rule_module.md#id4)

```yaml+jinja
- name: 'Ensure Discovery Rule'
  theforeman.foreman.discovery_rule:
    username: 'admin'
    password: 'secret_password'
    server_url: 'https://foreman.example.com'
    name: 'my-first-disco'
    search: 'mac = bb:bb:bb:bb:bb:bb'
    hostgroup: 'RedHat7-Base'
    hostname: 'servera'
    max_count: 1
    organizations:
      - 'MyOrg'
    locations:
      - 'DC1'

- name: 'Remove Discovery Rule'
  theforeman.foreman.discovery_rule:
    username: 'admin'
    password: 'secret_password'
    server_url: 'https://foreman.example.com'
    name: 'my-first-disco'
    state: 'absent'
```

## [Return Values](discovery_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **discovery_rules**  list / elements=dictionary | List of discovery rules.  Returned: success |

### Authors

- Jeffrey van Pelt (@Thulium-Drake)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
