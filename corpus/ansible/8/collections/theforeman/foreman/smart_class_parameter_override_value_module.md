---
collection: ansible
version: "8"
title: "theforeman.foreman.smart_class_parameter_override_value module – Manage Smart Class Parameter Override Values"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/smart_class_parameter_override_value_module.html
fetched_at: 2026-07-28T02:56:39+00:00
---
# theforeman.foreman.smart_class_parameter_override_value module – Manage Smart Class Parameter Override Values

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
> see [Requirements](smart_class_parameter_override_value_module.md#ansible-collections-theforeman-foreman-smart-class-parameter-override-value-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.smart_class_parameter_override_value`.

New in theforeman.foreman 3.14.0

- [Synopsis](smart_class_parameter_override_value_module.md#synopsis)
- [Requirements](smart_class_parameter_override_value_module.md#requirements)
- [Parameters](smart_class_parameter_override_value_module.md#parameters)
- [Attributes](smart_class_parameter_override_value_module.md#attributes)
- [Examples](smart_class_parameter_override_value_module.md#examples)
- [Return Values](smart_class_parameter_override_value_module.md#return-values)

## [Synopsis](smart_class_parameter_override_value_module.md#id1)

- Manage Smart Class Parameter Override Values

## [Requirements](smart_class_parameter_override_value_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](smart_class_parameter_override_value_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **match**  string / required | Override match |
| **omit**  boolean | Foreman will not send this parameter in classification output  **Choices:**   - `false` - `true` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **puppetclass**  aliases: puppetclass_name  string / required | Puppet Class the Smart Class Parameter belongs to |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **smart_class_parameter**  aliases: parameter  string / required | Smart Class Parameter the Override Value belongs to |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **value**  any | Override value, required if omit is false |

## [Attributes](smart_class_parameter_override_value_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](smart_class_parameter_override_value_module.md#id5)

```yaml+jinja
- name: Set ntp::servers override value
  theforeman.foreman.smart_class_parameter_override_value:
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    puppetclass: ntp
    smart_class_parameter: servers
    match: domain=example.org
    value:
      - ntp1.example.org
      - ntp2.example.org
    state: present
```

## [Return Values](smart_class_parameter_override_value_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **override_values**  list / elements=dictionary | List of override_values.  **Returned:** success |

### Authors

- Evgeni Golov (@evgeni)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
