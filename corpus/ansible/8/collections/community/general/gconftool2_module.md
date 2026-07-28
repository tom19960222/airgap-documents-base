---
collection: ansible
version: "8"
title: "community.general.gconftool2 module – Edit GNOME Configurations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gconftool2_module.html
fetched_at: 2026-07-28T01:45:37+00:00
---
# community.general.gconftool2 module – Edit GNOME Configurations

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.gconftool2`.

- [Synopsis](gconftool2_module.md#synopsis)
- [Parameters](gconftool2_module.md#parameters)
- [Attributes](gconftool2_module.md#attributes)
- [Examples](gconftool2_module.md#examples)
- [Return Values](gconftool2_module.md#return-values)

## [Synopsis](gconftool2_module.md#id1)

- This module allows for the manipulation of GNOME 2 Configuration via gconftool-2. Please see the gconftool-2(1) man pages for more details.

Aliases: system.gconftool2

## [Parameters](gconftool2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_source**  string | Specify a configuration source to use rather than the default path. See man gconftool-2(1). |
| **direct**  boolean | Access the config database directly, bypassing server. If `direct` is specified then the `config_source` must be specified as well. See man gconftool-2(1).  **Choices:**   - `false` ← (default) - `true` |
| **key**  string / required | A GConf preference key is an element in the GConf repository that corresponds to an application preference. See man gconftool-2(1). |
| **state**  string / required | The action to take upon the key/value.  State `get` is deprecated and will be removed in community.general 8.0.0. Please use the module [community.general.gconftool2_info](gconftool2_info_module.md#ansible-collections-community-general-gconftool2-info-module) instead.  **Choices:**   - `"absent"` - `"get"` - `"present"` |
| **value**  string | Preference keys typically have simple values such as strings, integers, or lists of strings and integers. This is ignored unless `state=present`. See man gconftool-2(1). |
| **value_type**  string | The type of value being set. This is ignored unless `state=present`. See man gconftool-2(1).  **Choices:**   - `"bool"` - `"float"` - `"int"` - `"string"` |

## [Attributes](gconftool2_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](gconftool2_module.md#id4)

```yaml+jinja
- name: Change the widget font to "Serif 12"
  community.general.gconftool2:
    key: "/desktop/gnome/interface/font_name"
    value_type: "string"
    value: "Serif 12"
```

## [Return Values](gconftool2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **key**  string | The key specified in the module parameters.  **Returned:** success  **Sample:** `"/desktop/gnome/interface/font_name"` |
| **previous_value**  string | The value of the preference key before executing the module.  From community.general 7.0.0 onwards it returns `null` for a non-existent `key`, and returned `""` before that.  **Returned:** success  **Sample:** `"Serif 12"` |
| **value**  string | The value of the preference key after executing the module or `null` if key is removed.  From community.general 7.0.0 onwards it returns `null` for a non-existent `key`, and returned `""` before that.  **Returned:** success  **Sample:** `"Serif 12"` |
| **value_type**  string | The type of the value that was changed.  **Returned:** success  **Sample:** `"string"` |

### Authors

- Kenneth D. Evensen (@kevensen)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
