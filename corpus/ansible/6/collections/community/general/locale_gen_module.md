---
collection: ansible
version: "6"
title: "community.general.locale_gen module – Creates or removes locales"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/locale_gen_module.html
fetched_at: 2026-07-27T17:10:34+00:00
---
# community.general.locale_gen module – Creates or removes locales

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.locale_gen`.

- [Synopsis](locale_gen_module.md#synopsis)
- [Parameters](locale_gen_module.md#parameters)
- [Examples](locale_gen_module.md#examples)

## [Synopsis](locale_gen_module.md#id1)

- Manages locales by editing /etc/locale.gen and invoking locale-gen.

## [Parameters](locale_gen_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name and encoding of the locale, such as “en_GB.UTF-8”. |
| **state**  string | Whether the locale shall be present.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](locale_gen_module.md#id3)

```yaml+jinja
- name: Ensure a locale exists
  community.general.locale_gen:
    name: de_CH.UTF-8
    state: present
```

### Authors

- Augustus Kling (@AugustusKling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
