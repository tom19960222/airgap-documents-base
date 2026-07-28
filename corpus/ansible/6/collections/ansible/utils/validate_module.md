---
collection: ansible
version: "6"
title: "ansible.utils.validate module – Validate data with provided criteria"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/utils/validate_module.html
fetched_at: 2026-07-27T16:42:59+00:00
---
# ansible.utils.validate module – Validate data with provided criteria

> **Note:**
>
> This module is part of the [ansible.utils collection](https://galaxy.ansible.com/ansible/utils) (version 2.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.validate`.

New in ansible.utils 1.0.0

- [Synopsis](validate_module.md#synopsis)
- [Parameters](validate_module.md#parameters)
- [Notes](validate_module.md#notes)
- [Examples](validate_module.md#examples)
- [Return Values](validate_module.md#return-values)

## [Synopsis](validate_module.md#id1)

- Validate data with provided criteria based on the validation engine.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](validate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **criteria**  any / required | The criteria used for validation of *data*. For the type of criteria refer to the documentation of individual validate plugins. |
| **data**  any / required | Data that will be validated against *criteria*. For the type of data refer to the documentation of individual validate plugins. |
| **engine**  string | The name of the validate plugin to use. The engine value should follow the fully qualified collection name format, that is <org-name>.<collection-name>.<validate-plugin-name>.  Default: `"ansible.utils.jsonschema"` |

## [Notes](validate_module.md#id3)

> **Note:**
>
> - For the type of options *data* and *criteria* refer to the individual validate plugin documentation that is represented in the value of *engine* option.
> - For additional plugin configuration options refer to the individual validate plugin documentation that is represented by the value of *engine* option.
> - The plugin configuration option can be either passed as task or environment variables.
> - The precedence of the validate plugin configurable option is task variables followed by the environment variables.

## [Examples](validate_module.md#id4)

```yaml+jinja
- name: set facts for data and criteria
  ansible.builtin.set_fact:
    data: "{{ lookup('ansible.builtin.file', './validate/data/show_interfaces_iosxr.json')}}"
    criteria: "{{ lookup('ansible.builtin.file', './validate/criteria/jsonschema/show_interfaces_iosxr.json')}}"

- name: validate data in with jsonschema engine (by passing task vars as configurable plugin options)
  ansible.utils.validate:
    data: "{{ data }}"
    criteria: "{{ criteria }}"
    engine: ansible.utils.jsonschema
  vars:
    ansible_jsonschema_draft: draft7

- name: validate configuration with config plugin (see config plugin for criteria examples)
  ansible.utils.validate:
    data: "{{ lookup('ansible.builtin.file', './backup/eos.config' }}"
    criteria: "{{ lookup('ansible.builtin.file', './validate/criteria/config/eos_config_rules.yaml' }}"
    engine: ansible.utils.config
```

## [Return Values](validate_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **errors**  list / elements=string | The list of errors in *data* based on the *criteria*.  Returned: when *data* value is invalid |
| **msg**  string | The msg indicates if the *data* is valid as per the *criteria*.  In case data is valid return success message **all checks passed**.  In case data is invalid return error message **Validation errors were found** along with more information on error is available.  Returned: always |

### Authors

- Bradley Thornton (@cidrblock)
- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
