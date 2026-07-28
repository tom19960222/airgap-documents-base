---
collection: ansible
version: "8"
title: "community.general.unicode_normalize filter – Normalizes unicode strings to facilitate comparison of characters with normalized forms"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/unicode_normalize_filter.html
fetched_at: 2026-07-28T01:52:29+00:00
---
# community.general.unicode_normalize filter – Normalizes unicode strings to facilitate comparison of characters with normalized forms

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.unicode_normalize`.

New in community.general 3.7.0

- [Synopsis](unicode_normalize_filter.md#synopsis)
- [Input](unicode_normalize_filter.md#input)
- [Positional parameters](unicode_normalize_filter.md#positional-parameters)
- [Examples](unicode_normalize_filter.md#examples)
- [Return Value](unicode_normalize_filter.md#return-value)

## [Synopsis](unicode_normalize_filter.md#id1)

- Normalizes unicode strings to facilitate comparison of characters with normalized forms.

## [Input](unicode_normalize_filter.md#id2)

This describes the input of the filter, the value before `| community.general.unicode_normalize`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A unicode string. |

## [Positional parameters](unicode_normalize_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | community.general.unicode_normalize(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **form**  string | The normal form to use.  See <https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize> for details.  **Choices:**   - `"NFC"` ← (default) - `"NFD"` - `"NFKC"` - `"NFKD"` |

## [Examples](unicode_normalize_filter.md#id4)

```yaml+jinja
- name: Normalize unicode string
  ansible.builtin.set_fact:
    dictionary: "{{ 'ä' | community.general.unicode_normalize('NFKD') }}"
    # The resulting string has length 2: one letter is 'a', the other
    # the diacritic combiner.
```

## [Return Value](unicode_normalize_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The normalized unicode string of the specified normal form.  **Returned:** success |

### Authors

- Andrew Pantuso (@Ajpantuso)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
