---
collection: ansible
version: "8"
title: "ansible.utils.validate test – Validate data with provided criteria"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/validate_test.html
fetched_at: 2026-07-28T01:10:24+00:00
---
# ansible.utils.validate test – Validate data with provided criteria

> **Note:**
>
> This test plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.validate`.

New in ansible.utils 1.0.0

- [Synopsis](validate_test.md#synopsis)
- [Keyword parameters](validate_test.md#keyword-parameters)
- [Notes](validate_test.md#notes)
- [Examples](validate_test.md#examples)
- [Return Value](validate_test.md#return-value)

## [Synopsis](validate_test.md#id1)

- Validate *data* with provided *criteria* based on the validation *engine*.

## [Keyword parameters](validate_test.md#id2)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.utils.validate(key1=value1, key2=value2, ...)` and `input is not ansible.utils.validate(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **criteria**  any / required | The criteria used for validation of value that represents *data* options.  This option is passed to the test plugin as key, value pair For example `config_data is ansible.utils.validate(criteria=criteria`), in this case the value of *criteria* key represents this criteria for data validation.  For the type of *criteria* that represents this value refer documentation of individual validate plugins. |
| **data**  any / required | A data that will be validated against *criteria*.  This option represents the value that is passed to test plugin as check. For example `config_data is ansible.utils.validate(criteria=criteria`, in this case **config_data** represents this option.  For the type of *data* that represents this value refer documentation of individual validate plugins. |
| **engine**  string | The name of the validate plugin to use.  This option can be passed in test plugin as a key, value pair For example `config_data is ansible.utils.validate(engine='ansible.utils.jsonschema', criteria=criteria`), in this case the value of *engine* key represents the engine to be use for data validation. If the value is not provided the default value that is `ansible.utils.jsonschema` will be used.  The value should be in fully qualified collection name format that is **<org-name>.<collection-name>.<validate-plugin-name>**.  **Default:** `"ansible.utils.jsonschema"` |

## [Notes](validate_test.md#id3)

> **Note:**
>
> - For the type of options *data* and *criteria* refer the individual validate plugin documentation that is represented in the value of *engine* option.
> - For additional plugin configuration options refer the individual validate plugin documentation that is represented by the value of *engine* option.
> - The plugin configuration option can be either passed as `key=value` pairs within test plugin or set as environment variables.
> - The precedence the validate plugin configurable option is the variable passed within test plugin as `key=value` pairs followed by task variables followed by environment variables.

## [Examples](validate_test.md#id4)

```yaml+jinja
- name: set facts for data and criteria
  ansible.builtin.set_fact:
    data: "{{ lookup('ansible.builtin.file', './validate/data/show_interfaces_iosxr.json')}}"
    criteria: "{{ lookup('ansible.builtin.file', './validate/criteria/jsonschema/show_interfaces_iosxr.json')}}"

- name: validate data in json format using jsonschema with test plugin
  ansible.builtin.set_fact:
    is_data_valid: "{{ data is ansible.utils.validate(engine='ansible.utils.jsonschema', criteria=criteria, draft='draft7') }}"
```

## [Return Value](validate_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | If data is valid return `true`  If data is invalid return `false`  **Returned:** success |

### Authors

- Ganesh Nalawade (@ganeshrn)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
