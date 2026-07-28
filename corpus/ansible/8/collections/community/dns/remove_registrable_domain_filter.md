---
collection: ansible
version: "8"
title: "community.dns.remove_registrable_domain filter – Removes the registrable domain name from a DNS name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/remove_registrable_domain_filter.html
fetched_at: 2026-07-28T01:43:36+00:00
---
# community.dns.remove_registrable_domain filter – Removes the registrable domain name from a DNS name

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
> To use it in a playbook, specify: `community.dns.remove_registrable_domain`.

New in community.dns 0.1.0

- [Synopsis](remove_registrable_domain_filter.md#synopsis)
- [Input](remove_registrable_domain_filter.md#input)
- [Keyword parameters](remove_registrable_domain_filter.md#keyword-parameters)
- [Examples](remove_registrable_domain_filter.md#examples)
- [Return Value](remove_registrable_domain_filter.md#return-value)

## [Synopsis](remove_registrable_domain_filter.md#id1)

- Removes the registrable domain name from a DNS name.

## [Input](remove_registrable_domain_filter.md#id2)

This describes the input of the filter, the value before `| community.dns.remove_registrable_domain`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A DNS name. |

## [Keyword parameters](remove_registrable_domain_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.dns.remove_registrable_domain(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **icann_only**  boolean | This controls whether only entries from the ICANN section of the Public Suffix List are used, or also entries from the Private section. For example, `.co.uk` is in the ICANN section, but `github.io` is in the Private section.  **Choices:**   - `false` ← (default) - `true` |
| **keep_trailing_period**  boolean | This controls whether the trailing period of the prefix (that is, the part before the registrable domain) is preserved or not.  **Choices:**   - `false` ← (default) - `true` |
| **keep_unknown_suffix**  boolean | This treats unknown TLDs as valid public suffixes. So for example the public suffix of `example.tlddoesnotexist` is `.tlddoesnotexist` if this is `true`, and hence the registrable domain of `www.example.tlddoesnotexist` is `example.tlddoesnotexist`. If set to `false`, the registrable domain of `www.example.tlddoesnotexist` is `tlddoesnotexist`.  This option corresponds to whether the global wildcard rule `*` in the Public Suffix List is used or not.  **Choices:**   - `false` - `true` ← (default) |
| **only_if_registerable**  boolean | This controls the behavior in case there is no label in front of the public suffix. This is the case if the DNS name itself is a public suffix.  If set to `false`, in this case the public suffix is treated as a registrable domain.  If set to `true` (default), the registrable domain of a public suffix is interpreted as an empty string.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](remove_registrable_domain_filter.md#id4)

```yaml+jinja
- name: Remove the registrable domain from a DNS name
  ansible.builtin.set_fact:
    public_suffix: "{{ 'www.ansible.co.uk' | community.dns.remove_registrable_domain }}"
    # Should result in 'www'
```

## [Return Value](remove_registrable_domain_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The part of the DNS name before the registrable domain.  **Returned:** success |

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
