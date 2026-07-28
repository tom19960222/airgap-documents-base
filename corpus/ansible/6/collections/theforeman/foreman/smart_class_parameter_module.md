---
collection: ansible
version: "6"
title: "theforeman.foreman.smart_class_parameter module – Manage Smart Class Parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/smart_class_parameter_module.html
fetched_at: 2026-07-28T00:21:10+00:00
---
# theforeman.foreman.smart_class_parameter module – Manage Smart Class Parameters

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
> see [Requirements](smart_class_parameter_module.md#ansible-collections-theforeman-foreman-smart-class-parameter-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.smart_class_parameter`.

New in theforeman.foreman 1.0.0

- [Synopsis](smart_class_parameter_module.md#synopsis)
- [Requirements](smart_class_parameter_module.md#requirements)
- [Parameters](smart_class_parameter_module.md#parameters)
- [Examples](smart_class_parameter_module.md#examples)
- [Return Values](smart_class_parameter_module.md#return-values)

## [Synopsis](smart_class_parameter_module.md#id1)

- Update Smart Class Parameters.
- Smart Class Parameters are created/deleted for Puppet classes during import and cannot be created or deleted otherwise.

## [Requirements](smart_class_parameter_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](smart_class_parameter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **avoid_duplicates**  boolean | Remove duplicate values (only array type)  Choices:   - `false` - `true` |
| **default_value**  any | Value to use by default. |
| **description**  string | Description of the Smart Class Parameter |
| **hidden_value**  boolean | When enabled the parameter is hidden in the UI.  Choices:   - `false` - `true` |
| **merge_default**  boolean | Include default value when merging all matching values.  Choices:   - `false` - `true` |
| **merge_overrides**  boolean | Merge all matching values (only array/hash type).  Choices:   - `false` - `true` |
| **omit**  boolean | Don’t send this parameter in classification output.  Puppet will use the value defined in the Puppet manifest for this parameter.  Choices:   - `false` - `true` |
| **override**  boolean | Whether the smart class parameter value is managed by Foreman  Choices:   - `false` - `true` |
| **override_value_order**  list / elements=string | The order in which values are resolved. |
| **override_values**  list / elements=dictionary | Value overrides |
| **match**  string / required | Override match |
| **omit**  boolean | Don’t send this parameter in classification output, replaces use_puppet_default.  Choices:   - `false` - `true` |
| **value**  any | Override value, required if omit is false |
| **parameter**  string / required | Name of the parameter |
| **parameter_type**  string | Types of variable values. If `none`, set the parameter type to empty value.  Choices:   - `"string"` - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` - `"none"` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **puppetclass_name**  string / required | Name of the puppetclass that own the parameter |
| **required**  boolean | If true, will raise an error if there is no default value and no matcher provide a value.  Choices:   - `false` - `true` |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity.  Choices:   - `"present"` ← (default) - `"present_with_defaults"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **validator_rule**  string | Used to enforce certain values for the parameter values. |
| **validator_type**  string | Types of validation values.  Choices:   - `"regexp"` - `"list"` |

## [Examples](smart_class_parameter_module.md#id4)

```yaml+jinja
- name: "Update prometheus::server alertmanagers_config param default value"
  theforeman.foreman.smart_class_parameter:
    puppetclass_name: "prometheus::server"
    parameter: alertmanagers_config
    override: true
    required: true
    default_value: /etc/prometheus/alert.yml
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: "Update prometheus::server alertmanagers_config param default value"
  theforeman.foreman.smart_class_parameter:
    puppetclass_name: "prometheus::server"
    parameter: alertmanagers_config
    override: true
    override_value_order:
      - fqdn
      - hostgroup
      - domain
    required: true
    default_value: /etc/prometheus/alert.yml
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    override_values:
      - match: domain=example.com
        value: foo
      - match: domain=foo.example.com
        omit: true
    state: present
```

## [Return Values](smart_class_parameter_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **smart_class_parameters**  list / elements=dictionary | List of smart class parameters.  Returned: success |

### Authors

- Baptiste Agasse (@bagasse)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
