---
collection: ansible
version: "6"
title: "community.general.random_words lookup – Return a number of random words"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/random_words_lookup.html
fetched_at: 2026-07-27T17:15:11+00:00
---
# community.general.random_words lookup – Return a number of random words

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](random_words_lookup.md#ansible-collections-community-general-random-words-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.random_words`.

New in community.general 4.0.0

- [Synopsis](random_words_lookup.md#synopsis)
- [Requirements](random_words_lookup.md#requirements)
- [Keyword parameters](random_words_lookup.md#keyword-parameters)
- [Examples](random_words_lookup.md#examples)
- [Return Value](random_words_lookup.md#return-value)

## [Synopsis](random_words_lookup.md#id1)

- Returns a number of random words. The output can for example be used for passwords.
- See <https://xkcd.com/936/> for background.

## [Requirements](random_words_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- xkcdpass <https://github.com/redacted/XKCD-password-generator>

## [Keyword parameters](random_words_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.random_words', key1=value1, key2=value2, ...)` and `query('community.general.random_words', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **case**  string | The method for setting the case of each word in the passphrase.  Choices:   - `"alternating"` - `"upper"` - `"lower"` ← (default) - `"random"` - `"capitalize"` |
| **delimiter**  string | The delimiter character between words.  Default: `" "` |
| **max_length**  integer | Maximum length of words to make password.  Default: `9` |
| **min_length**  integer | Minimum length of words to make password.  Default: `5` |
| **numwords**  integer | The number of words.  Default: `6` |

## [Examples](random_words_lookup.md#id4)

```yaml+jinja
- name: Generate password with default settings
  ansible.builtin.debug:
    var: lookup('community.general.random_words')
  # Example result: 'traitor gigabyte cesarean unless aspect clear'

- name: Generate password with six, five character, words
  ansible.builtin.debug:
    var: lookup('community.general.random_words', min_length=5, max_length=5)
  # Example result: 'brink banjo getup staff trump comfy'

- name: Generate password with three capitalized words and the '-' delimiter
  ansible.builtin.debug:
    var: lookup('community.general.random_words', numwords=3, delimiter='-', case='capitalize')
  # Example result: 'Overlabor-Faucet-Coastline'

- name: Generate password with three words without any delimiter
  ansible.builtin.debug:
    var: lookup('community.general.random_words', numwords=3, delimiter='')
  # Example result: 'deskworkmonopolystriking'
  # https://www.ncsc.gov.uk/blog-post/the-logic-behind-three-random-words
```

## [Return Value](random_words_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A single-element list containing random words.  Returned: success |

### Authors

- Thomas Sjögren (@konstruktoid)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
