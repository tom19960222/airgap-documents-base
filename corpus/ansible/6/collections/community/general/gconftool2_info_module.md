---
collection: ansible
version: "6"
title: "community.general.gconftool2_info module – Retrieve GConf configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gconftool2_info_module.html
fetched_at: 2026-07-27T17:08:58+00:00
---
# community.general.gconftool2_info module – Retrieve GConf configurations

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
> To use it in a playbook, specify: `community.general.gconftool2_info`.

New in community.general 5.1.0

- [Synopsis](gconftool2_info_module.md#synopsis)
- [Parameters](gconftool2_info_module.md#parameters)
- [Notes](gconftool2_info_module.md#notes)
- [See Also](gconftool2_info_module.md#see-also)
- [Examples](gconftool2_info_module.md#examples)
- [Return Values](gconftool2_info_module.md#return-values)

## [Synopsis](gconftool2_info_module.md#id1)

- This module allows retrieving application preferences from the GConf database, with the help of `gconftool-2`.

## [Parameters](gconftool2_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **key**  string / required | The key name for an element in the GConf database. |

## [Notes](gconftool2_info_module.md#id3)

> **Note:**
>
> - See man gconftool-2(1) for more details.

## [See Also](gconftool2_info_module.md#id4)

> **See also:**
>
> [gconf repository (archived)](https://gitlab.gnome.org/Archive/gconf)
> :   Git repository for the project. It is an archived project, so the repository is read-only.

## [Examples](gconftool2_info_module.md#id5)

```yaml+jinja
- name: Get value for a certain key in the database.
  community.general.gconftool2_info:
    key: /desktop/gnome/background/picture_filename
  register: result
```

## [Return Values](gconftool2_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  string | The value of the property.  Returned: success  Sample: `"Monospace 10"` |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
