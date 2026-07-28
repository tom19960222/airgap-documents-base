---
collection: ansible
version: "8"
title: "community.general.random_string lookup – Generates random string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/random_string_lookup.html
fetched_at: 2026-07-28T01:52:58+00:00
---
# community.general.random_string lookup – Generates random string

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
> To use it in a playbook, specify: `community.general.random_string`.

New in community.general 3.2.0

- [Synopsis](random_string_lookup.md#synopsis)
- [Keyword parameters](random_string_lookup.md#keyword-parameters)
- [Examples](random_string_lookup.md#examples)
- [Return Value](random_string_lookup.md#return-value)

## [Synopsis](random_string_lookup.md#id1)

- Generates random string based upon the given constraints.
- Uses [random.SystemRandom](https://docs.python.org/3/library/random.html#random.SystemRandom), so should be strong enough for cryptographic purposes.

## [Keyword parameters](random_string_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.random_string', key1=value1, key2=value2, ...)` and `query('community.general.random_string', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **base64**  boolean | Returns base64 encoded string.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_similar_chars**  boolean  *added in community.general 7.5.0* | Ignore similar characters, such as `l` and `1`, or `O` and `0`.  These characters can be configured in `similar_chars`.  **Choices:**   - `false` ← (default) - `true` |
| **length**  integer | The length of the string.  **Default:** `8` |
| **lower**  boolean | Include lowercase letters in the string.  **Choices:**   - `false` - `true` ← (default) |
| **min_lower**  integer | Minimum number of lowercase alphabets in the string.  If set, overrides `lower=false`.  **Default:** `0` |
| **min_numeric**  integer | Minimum number of numeric characters in the string.  If set, overrides `numbers=false`.  **Default:** `0` |
| **min_special**  integer | Minimum number of special character in the string.  **Default:** `0` |
| **min_upper**  integer | Minimum number of uppercase alphabets in the string.  If set, overrides `upper=false`.  **Default:** `0` |
| **numbers**  boolean | Include numbers in the string.  **Choices:**   - `false` - `true` ← (default) |
| **override_all**  string | Override all values of `numbers`, `upper`, `lower`, and `special` with the given list of characters. |
| **override_special**  string | Override a list of special characters to use in the string.  If set `min_special` should be set to a non-default value. |
| **similar_chars**  string  *added in community.general 7.5.0* | Override a list of characters not to be use in the string.  **Default:** `"il1LoO0"` |
| **special**  boolean | Include special characters in the string.  Special characters are taken from Python standard library `string`. See [the documentation of string.punctuation](https://docs.python.org/3/library/string.html#string.punctuation) for which characters will be used.  The choice of special characters can be changed to setting `override_special`.  **Choices:**   - `false` - `true` ← (default) |
| **upper**  boolean | Include uppercase letters in the string.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](random_string_lookup.md#id3)

```yaml+jinja
- name: Generate random string
  ansible.builtin.debug:
    var: lookup('community.general.random_string')
  # Example result: ['DeadBeeF']

- name: Generate random string with length 12
  ansible.builtin.debug:
    var: lookup('community.general.random_string', length=12)
  # Example result: ['Uan0hUiX5kVG']

- name: Generate base64 encoded random string
  ansible.builtin.debug:
    var: lookup('community.general.random_string', base64=True)
  # Example result: ['NHZ6eWN5Qk0=']

- name: Generate a random string with 1 lower, 1 upper, 1 number and 1 special char (at least)
  ansible.builtin.debug:
    var: lookup('community.general.random_string', min_lower=1, min_upper=1, min_special=1, min_numeric=1)
  # Example result: ['&Qw2|E[-']

- name: Generate a random string with all lower case characters
  debug:
    var: query('community.general.random_string', upper=false, numbers=false, special=false)
  # Example result: ['exolxzyz']

- name: Generate random hexadecimal string
  debug:
    var: query('community.general.random_string', upper=false, lower=false, override_special=hex_chars, numbers=false)
  vars:
    hex_chars: '0123456789ABCDEF'
  # Example result: ['D2A40737']

- name: Generate random hexadecimal string with override_all
  debug:
    var: query('community.general.random_string', override_all=hex_chars)
  vars:
    hex_chars: '0123456789ABCDEF'
  # Example result: ['D2A40737']
```

## [Return Value](random_string_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A one-element list containing a random string  **Returned:** success |

### Authors

- Abhijeet Kasurde (@Akasurde)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
