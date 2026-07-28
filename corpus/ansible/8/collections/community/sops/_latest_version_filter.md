---
collection: ansible
version: "8"
title: "community.sops._latest_version filter – [INTERNAL] Get latest version from a list of versions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/sops/_latest_version_filter.html
fetched_at: 2026-07-28T01:59:25+00:00
---
# community.sops._latest_version filter – [INTERNAL] Get latest version from a list of versions

> **Note:**
>
> This filter plugin is part of the [community.sops collection](https://galaxy.ansible.com/ui/repo/published/community/sops/) (version 1.6.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sops`.
>
> To use it in a playbook, specify: `community.sops._latest_version`.

New in community.sops 1.4.0

- [Synopsis](_latest_version_filter.md#synopsis)
- [Input](_latest_version_filter.md#input)
- [Examples](_latest_version_filter.md#examples)
- [Return Value](_latest_version_filter.md#return-value)

## [Synopsis](_latest_version_filter.md#id1)

- **This is an internal tool and must only be used from roles in this collection!** If you use it from outside this collection, be warned that its behavior can change and it can be removed at any time, even in bugfix releases!
- Given a list of version numbers, returns the largest of them.

## [Input](_latest_version_filter.md#id2)

This describes the input of the filter, the value before `| community.sops._latest_version`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list of strings. Every string must be a version number. |

## [Examples](_latest_version_filter.md#id3)

```yaml+jinja
- name: Print latest version
  ansible.builtin.debug:
    msg: "{{ versions | community.sops._latest_version }}"
  vars:
    versions:
      - 1.0.0
      - 1.0.0rc1
      - 1.1.0
```

## [Return Value](_latest_version_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The latest version from the input.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.sops)
- [Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-sops)
