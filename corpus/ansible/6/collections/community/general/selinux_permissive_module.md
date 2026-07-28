---
collection: ansible
version: "6"
title: "community.general.selinux_permissive module – Change permissive domain in SELinux policy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/selinux_permissive_module.html
fetched_at: 2026-07-27T17:13:07+00:00
---
# community.general.selinux_permissive module – Change permissive domain in SELinux policy

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](selinux_permissive_module.md#ansible-collections-community-general-selinux-permissive-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.selinux_permissive`.

- [Synopsis](selinux_permissive_module.md#synopsis)
- [Requirements](selinux_permissive_module.md#requirements)
- [Parameters](selinux_permissive_module.md#parameters)
- [Notes](selinux_permissive_module.md#notes)
- [Examples](selinux_permissive_module.md#examples)

## [Synopsis](selinux_permissive_module.md#id1)

- Add and remove a domain from the list of permissive domains.

## [Requirements](selinux_permissive_module.md#id2)

The below requirements are needed on the host that executes this module.

- policycoreutils-python

## [Parameters](selinux_permissive_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain**  aliases: name  string / required | The domain that will be added or removed from the list of permissive domains. |
| **no_reload**  boolean | Disable reloading of the SELinux policy after making change to a domain’s permissive setting.  The default is `false`, which causes policy to be reloaded when a domain changes state.  Reloading the policy does not work on older versions of the `policycoreutils-python` library, for example in EL 6.”  Choices:   - `false` ← (default) - `true` |
| **permissive**  boolean / required | Indicate if the domain should or should not be set as permissive.  Choices:   - `false` - `true` |
| **store**  string | Name of the SELinux policy store to use.  Default: `""` |

## [Notes](selinux_permissive_module.md#id4)

> **Note:**
>
> - Requires a recent version of SELinux and `policycoreutils-python` (EL 6 or newer).

## [Examples](selinux_permissive_module.md#id5)

```yaml+jinja
- name: Change the httpd_t domain to permissive
  community.general.selinux_permissive:
    name: httpd_t
    permissive: true
```

### Authors

- Michael Scherer (@mscherer)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
