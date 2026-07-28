---
collection: ansible
version: "8"
title: "ansible.builtin.template lookup – retrieve contents of file after templating with Jinja2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/template_lookup.html
fetched_at: 2026-07-28T01:08:37+00:00
---
# ansible.builtin.template lookup – retrieve contents of file after templating with Jinja2

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `template`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.template` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](template_lookup.md#synopsis)
- [Terms](template_lookup.md#terms)
- [Keyword parameters](template_lookup.md#keyword-parameters)
- [Notes](template_lookup.md#notes)
- [Examples](template_lookup.md#examples)
- [Return Value](template_lookup.md#return-value)

## [Synopsis](template_lookup.md#id1)

- Returns a list of strings; for each template in the list of templates you pass in, returns a string containing the results of processing that template.

## [Terms](template_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | list of files to template |

## [Keyword parameters](template_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.template', key1=value1, key2=value2, ...)` and `query('ansible.builtin.template', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **comment_end_string**  string  *added in ansible-core 2.12* | The string marking the end of a comment statement.  **Default:** `"#}"` |
| **comment_start_string**  string  *added in ansible-core 2.12* | The string marking the beginning of a comment statement.  **Default:** `"{#"` |
| **convert_data**  boolean | Whether to convert YAML into data. If False, strings that are YAML will be left untouched.  Mutually exclusive with the jinja2_native option.  **Choices:**   - `false` - `true` ← (default) |
| **jinja2_native**  boolean  *added in ansible-core 2.11* | Controls whether to use Jinja2 native types.  It is off by default even if global jinja2_native is True.  Has no effect if global jinja2_native is False.  This offers more flexibility than the template module which does not use Jinja2 native types at all.  Mutually exclusive with the convert_data option.  **Choices:**   - `false` ← (default) - `true` |
| **template_vars**  dictionary | A dictionary, the keys become additional variables available for templating.  **Default:** `{}` |
| **variable_end_string**  string  *added in Ansible 2.8* | The string marking the end of a print statement.  **Default:** `"}}"` |
| **variable_start_string**  string  *added in Ansible 2.8* | The string marking the beginning of a print statement.  **Default:** `"{{"` |

## [Notes](template_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.template', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.template', term1, term2, key1=value1, key2=value2)`

## [Examples](template_lookup.md#id5)

```yaml+jinja
- name: show templating results
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.template', './some_template.j2') }}"

- name: show templating results with different variable start and end string
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.template', './some_template.j2', variable_start_string='[%', variable_end_string='%]') }}"

- name: show templating results with different comment start and end string
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.template', './some_template.j2', comment_start_string='[#', comment_end_string='#]') }}"
```

## [Return Value](template_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | file(s) content after templating  **Returned:** success |

### Authors

- Michael DeHaan

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
