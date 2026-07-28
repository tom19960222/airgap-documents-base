---
collection: ansible
version: "6"
title: "community.general.syspatch module – Manage OpenBSD system patches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/syspatch_module.html
fetched_at: 2026-07-27T17:13:31+00:00
---
# community.general.syspatch module – Manage OpenBSD system patches

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
> To use it in a playbook, specify: `community.general.syspatch`.

- [Synopsis](syspatch_module.md#synopsis)
- [Parameters](syspatch_module.md#parameters)
- [Examples](syspatch_module.md#examples)
- [Return Values](syspatch_module.md#return-values)

## [Synopsis](syspatch_module.md#id1)

- Manage OpenBSD system patches using syspatch.

## [Parameters](syspatch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **revert**  string | Revert system patches.  Choices:   - `"all"` - `"one"` |

## [Examples](syspatch_module.md#id3)

```yaml+jinja
- name: Apply all available system patches
  community.general.syspatch:

- name: Revert last patch
  community.general.syspatch:
    revert: one

- name: Revert all patches
  community.general.syspatch:
    revert: all

# NOTE: You can reboot automatically if a patch requires it:
- name: Apply all patches and store result
  community.general.syspatch:
  register: syspatch

- name: Reboot if patch requires it
  ansible.builtin.reboot:
  when: syspatch.reboot_needed
```

## [Return Values](syspatch_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rc**  integer | The command return code (0 means success)  Returned: always |
| **reboot_needed**  boolean | Whether or not a reboot is required after an update.  Returned: always  Sample: `true` |
| **stderr**  string | syspatch standard error.  Returned: always  Sample: `"syspatch: need root privileges"` |
| **stdout**  string | syspatch standard output.  Returned: always  Sample: `"001_rip6cksum"` |

### Authors

- Andrew Klaus (@precurse)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
