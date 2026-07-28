---
collection: ansible
version: "8"
title: "ansible.builtin.to_nice_json filter – Convert variable to ‘nicely formatted’ JSON string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/to_nice_json_filter.html
fetched_at: 2026-07-28T01:04:45+00:00
---
# ansible.builtin.to_nice_json filter – Convert variable to ‘nicely formatted’ JSON string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `to_nice_json`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.to_nice_json` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](to_nice_json_filter.md#synopsis)
- [Input](to_nice_json_filter.md#input)
- [Keyword parameters](to_nice_json_filter.md#keyword-parameters)
- [Notes](to_nice_json_filter.md#notes)
- [Examples](to_nice_json_filter.md#examples)
- [Return Value](to_nice_json_filter.md#return-value)

## [Synopsis](to_nice_json_filter.md#id1)

- Converts an Ansible variable into a ‘nicely formatted’ JSON string representation
- This filter functions as a wrapper to the Python `json.dumps` function.
- Ansible automatically converts JSON strings into variable structures so this plugin is used to forcibly retain a JSON string.

## [Input](to_nice_json_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.to_nice_json`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | A variable or expression that returns a data structure. |

## [Keyword parameters](to_nice_json_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.to_nice_json(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **allow_nan**  boolean | When `False`, strict adherence to float value limits of the JSON specification, so `nan`, `inf` and `-inf` values will produce errors. When `True`, JavaScript equivalents will be used (`NaN`, `Infinity`, `-Infinity`).  **Choices:**   - `false` - `true` ← (default) |
| **check_circular**  boolean | Controls the usage of the internal circular reference detection, if off can result in overflow errors.  **Choices:**   - `false` - `true` ← (default) |
| **ensure_ascii**  boolean | Escapes all non ASCII characters.  **Choices:**   - `false` - `true` ← (default) |
| **preprocess_unsafe**  boolean  *added in Ansible 2.9* | Toggle to represent unsafe values directly in JSON or create a unsafe object in JSON.  **Choices:**   - `false` - `true` ← (default) |
| **skipkeys**  boolean | If `True`, keys that are not basic Python types will be skipped.  **Choices:**   - `false` ← (default) - `true` |
| **vault_to_text**  boolean  *added in Ansible 2.9* | Toggle to either unvault a vault or create the JSON version of a vaulted object.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](to_nice_json_filter.md#id4)

> **Note:**
>
> - Both *vault_to_text* and *preprocess_unsafe* defaulted to `False` between Ansible 2.9 and 2.12.
> - These parameters to `json.dumps` will be ignored, they are overridden for internal use: *cls*, *default*, *indent*, *separators*, *sort_keys*.

## [Examples](to_nice_json_filter.md#id5)

```yaml+jinja
# dump variable in a template to create a nicely formatted JSON document
{{ docker_config|to_nice_json }}
```

## [Return Value](to_nice_json_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The ‘nicely formatted’ JSON serialized string representing the variable structure inputted.  **Returned:** success |

### Authors

- core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
