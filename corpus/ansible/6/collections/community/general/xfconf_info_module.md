---
collection: ansible
version: "6"
title: "community.general.xfconf_info module – Retrieve XFCE4 configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/xfconf_info_module.html
fetched_at: 2026-07-27T17:14:08+00:00
---
# community.general.xfconf_info module – Retrieve XFCE4 configurations

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
> To use it in a playbook, specify: `community.general.xfconf_info`.

New in community.general 3.5.0

- [Synopsis](xfconf_info_module.md#synopsis)
- [Parameters](xfconf_info_module.md#parameters)
- [Notes](xfconf_info_module.md#notes)
- [Examples](xfconf_info_module.md#examples)
- [Return Values](xfconf_info_module.md#return-values)

## [Synopsis](xfconf_info_module.md#id1)

- This module allows retrieving Xfce 4 configurations with the help of `xfconf-query`.

## [Parameters](xfconf_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel**  string | A Xfconf preference channel is a top-level tree key, inside of the Xfconf repository that corresponds to the location for which all application properties/keys are stored.  If not provided, the module will list all available channels. |
| **property**  string | A Xfce preference key is an element in the Xfconf repository that corresponds to an application preference.  If provided, then *channel* is required.  If not provided and a *channel* is provided, then the module will list all available properties in that *channel*. |

## [Notes](xfconf_info_module.md#id3)

> **Note:**
>
> - See man xfconf-query(1) for more details.

## [Examples](xfconf_info_module.md#id4)

```yaml+jinja
- name: Get list of all available channels
  community.general.xfconf_info: {}
  register: result

- name: Get list of all properties in a specific channel
  community.general.xfconf_info:
    channel: xsettings
  register: result

- name: Retrieve the DPI value
  community.general.xfconf_info:
    channel: xsettings
    property: /Xft/DPI
  register: result

- name: Get workspace names (4)
  community.general.xfconf_info:
    channel: xfwm4
    property: /general/workspace_names
  register: result
```

## [Return Values](xfconf_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **channels**  list / elements=string | List of available channels.  Returned when the module receives no parameter at all.  Returned: success  Sample: `["xfce4-desktop", "displays", "xsettings", "xfwm4"]` |
| **is_array**  boolean | Flag indicating whether the property is an array or not.  Returned: success |
| **properties**  list / elements=string | List of available properties for a specific channel.  Returned by passing only the *channel* parameter to the module.  Returned: success  Sample: `["/Gdk/WindowScalingFactor", "/Gtk/ButtonImages", "/Gtk/CursorThemeSize", "/Gtk/DecorationLayout", "/Gtk/FontName", "/Gtk/MenuImages", "/Gtk/MonospaceFontName", "/Net/DoubleClickTime", "/Net/IconThemeName", "/Net/ThemeName", "/Xft/Antialias", "/Xft/Hinting", "/Xft/HintStyle", "/Xft/RGBA"]` |
| **value**  string | The value of the property. Empty if the property is of array type.  Returned: success  Sample: `"Monospace 10"` |
| **value_array**  list / elements=string | The array value of the property. Empty if the property is not of array type.  Returned: success  Sample: `["Main", "Work", "Tmp"]` |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
