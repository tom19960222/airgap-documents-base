---
collection: ansible
version: "6"
title: "community.general.gconftool2 module – Edit GNOME Configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/gconftool2_module.html
fetched_at: 2026-07-27T17:08:58+00:00
---
# community.general.gconftool2 module – Edit GNOME Configurations

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
> To use it in a playbook, specify: `community.general.gconftool2`.

- [Synopsis](gconftool2_module.md#synopsis)
- [Parameters](gconftool2_module.md#parameters)
- [Examples](gconftool2_module.md#examples)
- [Return Values](gconftool2_module.md#return-values)

## [Synopsis](gconftool2_module.md#id1)

- This module allows for the manipulation of GNOME 2 Configuration via gconftool-2. Please see the gconftool-2(1) man pages for more details.

## [Parameters](gconftool2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config_source**  string | Specify a configuration source to use rather than the default path. See man gconftool-2(1) |
| **direct**  boolean | Access the config database directly, bypassing server. If direct is specified then the config_source must be specified as well. See man gconftool-2(1)  Choices:   - `false` ← (default) - `true` |
| **key**  string / required | A GConf preference key is an element in the GConf repository that corresponds to an application preference. See man gconftool-2(1) |
| **state**  string / required | The action to take upon the key/value.  Choices:   - `"absent"` - `"get"` - `"present"` |
| **value**  string | Preference keys typically have simple values such as strings, integers, or lists of strings and integers. This is ignored if the state is “get”. See man gconftool-2(1) |
| **value_type**  string | The type of value being set. This is ignored if the state is “get”.  Choices:   - `"bool"` - `"float"` - `"int"` - `"string"` |

## [Examples](gconftool2_module.md#id3)

```yaml+jinja
- name: Change the widget font to "Serif 12"
  community.general.gconftool2:
    key: "/desktop/gnome/interface/font_name"
    value_type: "string"
    value: "Serif 12"
```

## [Return Values](gconftool2_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **key**  string | The key specified in the module parameters  Returned: success  Sample: `"/desktop/gnome/interface/font_name"` |
| **value**  string | The value of the preference key after executing the module  Returned: success  Sample: `"Serif 12"` |
| **value_type**  string | The type of the value that was changed  Returned: success  Sample: `"string"` |

### Authors

- Kenneth D. Evensen (@kevensen)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
