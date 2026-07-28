---
collection: ansible
version: "8"
title: "community.general.merge_variables lookup – merge variables with a certain suffix"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/merge_variables_lookup.html
fetched_at: 2026-07-28T01:52:54+00:00
---
# community.general.merge_variables lookup – merge variables with a certain suffix

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.merge_variables`.

New in community.general 6.5.0

- [Synopsis](merge_variables_lookup.md#synopsis)
- [Terms](merge_variables_lookup.md#terms)
- [Keyword parameters](merge_variables_lookup.md#keyword-parameters)
- [Notes](merge_variables_lookup.md#notes)
- [Examples](merge_variables_lookup.md#examples)
- [Return Value](merge_variables_lookup.md#return-value)

## [Synopsis](merge_variables_lookup.md#id1)

- This lookup returns the merged result of all variables in scope that match the given prefixes, suffixes, or regular expressions, optionally.

## [Terms](merge_variables_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | Depending on the value of `pattern_type`, this is a list of prefixes, suffixes, or regular expressions that will be used to match all variables that should be merged. |

## [Keyword parameters](merge_variables_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.merge_variables', key1=value1, key2=value2, ...)` and `query('community.general.merge_variables', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **initial_value**  any | An initial value to start with. |
| **override**  string | Return an error, print a warning or ignore it when a key will be overwritten.  The default behavior `error` makes the plugin fail when a key would be overwritten.  When `warn` and `ignore` are used, note that it is important to know that the variables are sorted by name before being merged. Keys for later variables in this order will overwrite keys of the same name for variables earlier in this order. To avoid potential confusion, better use `override=error` whenever possible.  **Choices:**   - `"error"` ← (default) - `"warn"` - `"ignore"`   **Configuration:**   - INI entry:  ```YAML+Jinja   [merge_variables_lookup]   override = error   ``` - Environment variable: [`ANSIBLE_MERGE_VARIABLES_OVERRIDE`](../../environment_variables.md#envvar-ANSIBLE_MERGE_VARIABLES_OVERRIDE) |
| **pattern_type**  string | Change the way of searching for the specified pattern.  **Choices:**   - `"prefix"` - `"suffix"` - `"regex"` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [merge_variables_lookup]   pattern_type = regex   ``` - Environment variable: [`ANSIBLE_MERGE_VARIABLES_PATTERN_TYPE`](../../environment_variables.md#envvar-ANSIBLE_MERGE_VARIABLES_PATTERN_TYPE) |

## [Notes](merge_variables_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.merge_variables', term1, term2, key1=value1, key2=value2)` and `query('community.general.merge_variables', term1, term2, key1=value1, key2=value2)`

## [Examples](merge_variables_lookup.md#id5)

```yaml+jinja
# Some example variables, they can be defined anywhere as long as they are in scope
test_init_list:
  - "list init item 1"
  - "list init item 2"

testa__test_list:
  - "test a item 1"

testb__test_list:
  - "test b item 1"

testa__test_dict:
  ports:
    - 1

testb__test_dict:
  ports:
    - 3

# Merge variables that end with '__test_dict' and store the result in a variable 'example_a'
example_a: "{{ lookup('community.general.merge_variables', '__test_dict', pattern_type='suffix') }}"

# The variable example_a now contains:
# ports:
#   - 1
#   - 3

# Merge variables that match the '^.+__test_list$' regular expression, starting with an initial value and store the
# result in a variable 'example_b'
example_b: "{{ lookup('community.general.merge_variables', '^.+__test_list$', initial_value=test_init_list) }}"

# The variable example_b now contains:
#   - "list init item 1"
#   - "list init item 2"
#   - "test a item 1"
#   - "test b item 1"
```

## [Return Value](merge_variables_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  any | In case the search matches list items, a list will be returned. In case the search matches dicts, a dict will be returned.  **Returned:** success |

### Authors

- Roy Lenferink (@rlenferink)
- Mark Ettema (@m-a-r-k-e)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
