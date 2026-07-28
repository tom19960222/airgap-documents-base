---
collection: ansible
version: "8"
title: "ansible.builtin.version test – compare version strings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/version_test.html
fetched_at: 2026-07-28T01:09:03+00:00
---
# ansible.builtin.version test – compare version strings

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `version`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.version` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](version_test.md#synopsis)
- [Input](version_test.md#input)
- [Keyword parameters](version_test.md#keyword-parameters)
- [Notes](version_test.md#notes)
- [Examples](version_test.md#examples)
- [Return Value](version_test.md#return-value)

## [Synopsis](version_test.md#id1)

- Compare version strings using various versioning schemes

Aliases: version_compare

## [Input](version_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.version` or `is not ansible.builtin.version`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Left hand version to compare |

## [Keyword parameters](version_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.version(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.version(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **operator**  string | Comparison operator  **Choices:**   - `"=="` - `"="` - `"eq"` ← (default) - `"<"` - `"lt"` - `"<="` - `"le"` - `">"` - `"gt"` - `">="` - `"ge"` - `"!="` - `"<>"` - `"ne"` |
| **strict**  boolean | Whether to use strict version scheme. Mutually exclusive with `version_type`  **Choices:**   - `false` ← (default) - `true` |
| **version**  string / required | Right hand version to compare |
| **version_type**  string | Version scheme to use for comparison. Mutually exclusive with `strict`. See `notes` for descriptions on the version types.  **Choices:**   - `"loose"` ← (default) - `"strict"` - `"semver"` - `"semantic"` - `"pep440"` |

## [Notes](version_test.md#id4)

> **Note:**
>
> - `loose` - This type corresponds to the Python `distutils.version.LooseVersion` class. All version formats are valid for this type. The rules for comparison are simple and predictable, but may not always give expected results.
> - `strict` - This type corresponds to the Python `distutils.version.StrictVersion` class. A version number consists of two or three dot-separated numeric components, with an optional “pre-release” tag on the end. The pre-release tag consists of a single letter `a` or `b` followed by a number. If the numeric components of two version numbers are equal, then one with a pre-release tag will always be deemed earlier (lesser) than one without.
> - `semver`/`semantic` - This type implements the [Semantic Version](https://semver.org) scheme for version comparison.
> - `pep440` - This type implements the Python [PEP-440](https://peps.python.org/pep-0440/) versioning rules for version comparison. Added in version 2.14.

## [Examples](version_test.md#id5)

```yaml+jinja
- name: version test examples
  assert:
    that:
      - "'1.0' is version_compare('1.0', '==')"  # old name
      - "'1.0' is version('1.0', '==')"
      - "'1.0' is version('2.0', '!=')"
      - "'1.0' is version('2.0', '<')"
      - "'2.0' is version('1.0', '>')"
      - "'1.0' is version('1.0', '<=')"
      - "'1.0' is version('1.0', '>=')"
      - "'1.0' is version_compare('1.0', '==', strict=true)"  # old name
      - "'1.0' is version('1.0', '==', strict=true)"
      - "'1.0' is version('2.0', '!=', strict=true)"
      - "'1.0' is version('2.0', '<', strict=true)"
      - "'2.0' is version('1.0', '>', strict=true)"
      - "'1.0' is version('1.0', '<=', strict=true)"
      - "'1.0' is version('1.0', '>=', strict=true)"
      - "'1.2.3' is version('2.0.0', 'lt', version_type='semver')"
      - "'2.14.0rc1' is version('2.14.0', 'lt', version_type='pep440')"
```

## [Return Value](version_test.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` or `False` depending on the outcome of the comparison.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
