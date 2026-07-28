---
collection: ansible
version: "8"
title: "community.dns.get_public_suffix filter – Returns the public suffix of a DNS name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/get_public_suffix_filter.html
fetched_at: 2026-07-28T01:43:34+00:00
---
# community.dns.get_public_suffix filter – Returns the public suffix of a DNS name

> **Note:**
>
> This filter plugin is part of the [community.dns collection](https://galaxy.ansible.com/ui/repo/published/community/dns/) (version 2.6.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
>
> To use it in a playbook, specify: `community.dns.get_public_suffix`.

New in community.dns 0.1.0

- [Synopsis](get_public_suffix_filter.md#synopsis)
- [Input](get_public_suffix_filter.md#input)
- [Keyword parameters](get_public_suffix_filter.md#keyword-parameters)
- [Examples](get_public_suffix_filter.md#examples)
- [Return Value](get_public_suffix_filter.md#return-value)

## [Synopsis](get_public_suffix_filter.md#id1)

- Returns the public suffix of a DNS name.

## [Input](get_public_suffix_filter.md#id2)

This describes the input of the filter, the value before `| community.dns.get_public_suffix`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A DNS name. |

## [Keyword parameters](get_public_suffix_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.dns.get_public_suffix(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **icann_only**  boolean | This controls whether only entries from the ICANN section of the Public Suffix List are used, or also entries from the Private section. For example, `.co.uk` is in the ICANN section, but `github.io` is in the Private section.  **Choices:**   - `false` ← (default) - `true` |
| **keep_leading_period**  boolean | This controls whether the leading period of a public suffix is preserved or not.  **Choices:**   - `false` - `true` ← (default) |
| **keep_unknown_suffix**  boolean | This treats unknown TLDs as valid public suffixes. So for example the public suffix of `example.tlddoesnotexist` is `.tlddoesnotexist` if this is `true`. If set to `false`, it will return an empty string in this case.  This option corresponds to whether the global wildcard rule `*` in the Public Suffix List is used or not.  **Choices:**   - `false` - `true` ← (default) |
| **normalize_result**  boolean | This controls whether the result is reconstructed from the normalized name used during lookup. During normalization, ulabels are converted to alabels, and every label is converted to lowercase. For example, the ulabel `ëçãmplê` is converted to `xn--mpl-llatwb` (puny-code), and `Example.COM` is converted to `example.com`.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](get_public_suffix_filter.md#id4)

```yaml+jinja
- name: Extract the public suffix from a DNS name
  ansible.builtin.set_fact:
    public_suffix: "{{ 'www.ansible.co.uk' | community.dns.get_public_suffix }}"
    # Should result in '.co.uk'
```

## [Return Value](get_public_suffix_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The public suffix.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
