---
collection: ansible
version: "8"
title: "ansible.utils.validate filter – Validate data with provided criteria"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/validate_filter.html
fetched_at: 2026-07-28T01:10:04+00:00
---
# ansible.utils.validate filter – Validate data with provided criteria

> **Note:**
>
> This filter plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.validate`.

New in ansible.utils 1.0.0

- [Synopsis](validate_filter.md#synopsis)
- [Keyword parameters](validate_filter.md#keyword-parameters)
- [Notes](validate_filter.md#notes)
- [Examples](validate_filter.md#examples)
- [Return Value](validate_filter.md#return-value)

## [Synopsis](validate_filter.md#id1)

- Validate *data* with provided *criteria* based on the validation *engine*.

## [Keyword parameters](validate_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.validate(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **criteria**  any / required | The criteria used for validation of value that represents *data* options.  This option represents the first argument passed in the filter plugin. For example `config_data|ansible.utils.validate(config_criteria`), in this case the value of `config_criteria` represents this option.  For the type of *criteria* that represents this value refer to the documentation of individual validator plugins. |
| **data**  any / required | Data that will be validated against *criteria*.  This option represents the value that is passed to the filter plugin in pipe format. For example `config_data|ansible.utils.validate(`), in this case `config_data` represents this option.  For the type of *data* that represents this value refer to the documentation of individual validator plugins. |
| **engine**  string | The name of the validator plugin to use.  This option can be passed in lookup plugin as a key, value pair. For example `config_data|ansible.utils.validate(config_criteria, engine='ansible.utils.jsonschema'`), in this case the value `ansible.utils.jsonschema` represents the engine to be use for data validation. If the value is not provided the default value that is `ansible.utils.jsonschema` will be used.  The value should be in fully qualified collection name format that is `<org-name>.<collection-name>.<validator-plugin-name>`.  **Default:** `"ansible.utils.jsonschema"` |

## [Notes](validate_filter.md#id3)

> **Note:**
>
> - For the type of options *data* and *criteria* refer to the individual validate plugin documentation that is represented in the value of *engine* option.
> - For additional plugin configuration options refer to the individual validate plugin documentation that is represented by the value of *engine* option.
> - The plugin configuration option can be either passed as `key=value` pairs within filter plugin or environment variables.
> - The precedence of the *validate* plugin configurable option is the variable passed within filter plugin as `key=value` pairs followed by the environment variables.

## [Examples](validate_filter.md#id4)

```yaml+jinja
- name: set facts for data and criteria
  ansible.builtin.set_fact:
    data: "{{ lookup('ansible.builtin.file', './validate/data/show_interfaces_iosxr.json')}}"
    criteria: "{{ lookup('ansible.builtin.file', './validate/criteria/jsonschema/show_interfaces_iosxr.json')}}"

- name: validate data in json format using jsonschema by passing plugin configuration variable as key/value pairs
  ansible.builtin.set_fact:
    data_validity: "{{ data|ansible.utils.validate(criteria, engine='ansible.utils.jsonschema', draft='draft7') }}"
```

## [Return Value](validate_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | If data is valid returns empty list  If data is invalid returns list of errors in data  **Returned:** success |

### Authors

- Ganesh Nalawade (@ganeshrn)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
