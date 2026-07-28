---
collection: ansible
version: "6"
title: "community.general.xfconf module – Edit XFCE4 Configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/xfconf_module.html
fetched_at: 2026-07-27T17:14:07+00:00
---
# community.general.xfconf module – Edit XFCE4 Configurations

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
> To use it in a playbook, specify: `community.general.xfconf`.

- [Synopsis](xfconf_module.md#synopsis)
- [Parameters](xfconf_module.md#parameters)
- [See Also](xfconf_module.md#see-also)
- [Examples](xfconf_module.md#examples)
- [Return Values](xfconf_module.md#return-values)

## [Synopsis](xfconf_module.md#id1)

- This module allows for the manipulation of Xfce 4 Configuration with the help of xfconf-query. Please see the xfconf-query(1) man page for more details.

## [Parameters](xfconf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel**  string / required | A Xfconf preference channel is a top-level tree key, inside of the Xfconf repository that corresponds to the location for which all application properties/keys are stored. See man xfconf-query(1). |
| **disable_facts**  boolean  added in community.general 2.1.0 | The value `false` is no longer allowed since community.general 4.0.0.  This option will be deprecated in a future version, and eventually be removed.  Choices:   - `false` - `true` ← (default) |
| **force_array**  aliases: array  boolean  added in community.general 1.0.0 | Force array even if only one element.  Choices:   - `false` ← (default) - `true` |
| **property**  string / required | A Xfce preference key is an element in the Xfconf repository that corresponds to an application preference. See man xfconf-query(1). |
| **state**  string | The action to take upon the property/value.  The state `get` has been removed in community.general 5.0.0. Please use the module [community.general.xfconf_info](xfconf_info_module.md#ansible-collections-community-general-xfconf-info-module) instead.  Choices:   - `"present"` ← (default) - `"absent"` |
| **value**  list / elements=any | Preference properties typically have simple values such as strings, integers, or lists of strings and integers. See man xfconf-query(1). |
| **value_type**  list / elements=string | The type of value being set.  When providing more than one *value_type*, the length of the list must be equal to the length of *value*.  If only one *value_type* is provided, but *value* contains more than on element, that *value_type* will be applied to all elements of *value*.  If the *property* being set is an array and it can possibly have ony one element in the array, then *force_array=true* must be used to ensure that `xfconf-query` will interpret the value as an array rather than a scalar.  Support for `uchar`, `char`, `uint64`, and `int64` has been added in community.general 4.8.0.  Choices:   - `"string"` - `"int"` - `"double"` - `"bool"` - `"uint"` - `"uchar"` - `"char"` - `"uint64"` - `"int64"` - `"float"` |

## [See Also](xfconf_module.md#id3)

> **See also:**
>
> [xfconf-query(1) man page](https://docs.xfce.org/xfce/xfconf/xfconf-query)
> :   Manual page of the `xfconf-query` tool at the XFCE documentation site.
>
> [xfconf - Configuration Storage System](https://docs.xfce.org/xfce/xfconf/start)
> :   XFCE documentation for the Xfconf configuration system.

## [Examples](xfconf_module.md#id4)

```yaml+jinja
- name: Change the DPI to "192"
  xfconf:
    channel: "xsettings"
    property: "/Xft/DPI"
    value_type: "int"
    value: "192"

- name: Set workspace names (4)
  xfconf:
    channel: xfwm4
    property: /general/workspace_names
    value_type: string
    value: ['Main', 'Work1', 'Work2', 'Tmp']

- name: Set workspace names (1)
  xfconf:
    channel: xfwm4
    property: /general/workspace_names
    value_type: string
    value: ['Main']
    force_array: true
```

## [Return Values](xfconf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **channel**  string | The channel specified in the module parameters  Returned: success  Sample: `"xsettings"` |
| **cmd**  list / elements=string  added in community.general 5.4.0 | A list with the resulting `xfconf-query` command executed by the module.  Returned: success  Sample: `["/usr/bin/xfconf-query", "--channel", "xfce4-panel", "--property", "/plugins/plugin-19/timezone", "--create", "--type", "string", "--set", "Pacific/Auckland"]` |
| **previous_value**  any | The value of the preference key before executing the module. Either a single string value or a list of strings for array types.  This is a string or a list of strings.  Returned: success  Sample: `"\"96\" or [\"red\", \"blue\", \"green\"]"` |
| **property**  string | The property specified in the module parameters  Returned: success  Sample: `"/Xft/DPI"` |
| **value**  any | The value of the preference key after executing the module. Either a single string value or a list of strings for array types.  This is a string or a list of strings.  Returned: success  Sample: `"\"192\" or [\"orange\", \"yellow\", \"violet\"]"` |
| **value_type**  any | The type of the value that was changed (`none` for `reset` state). Either a single string value or a list of strings for array types.  This is a string or a list of strings.  Returned: success  Sample: `"\"int\" or [\"str\", \"str\", \"str\"]"` |

### Authors

- Joseph Benden (@jbenden)
- Alexei Znamensky (@russoz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
