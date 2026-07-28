---
collection: ansible
version: "6"
title: "community.general.dconf module – Modify and read dconf database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dconf_module.html
fetched_at: 2026-07-27T17:08:41+00:00
---
# community.general.dconf module – Modify and read dconf database

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
> To use it in a playbook, specify: `community.general.dconf`.

- [Synopsis](dconf_module.md#synopsis)
- [Parameters](dconf_module.md#parameters)
- [Notes](dconf_module.md#notes)
- [Examples](dconf_module.md#examples)
- [Return Values](dconf_module.md#return-values)

## [Synopsis](dconf_module.md#id1)

- This module allows modifications and reading of `dconf` database. The module is implemented as a wrapper around `dconf` tool. Please see the dconf(1) man page for more details.
- Since `dconf` requires a running D-Bus session to change values, the module will try to detect an existing session and reuse it, or run the tool via `dbus-run-session`.

## [Parameters](dconf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **key**  string / required | A dconf key to modify or read from the dconf database. |
| **state**  string | The action to take upon the key/value.  Choices:   - `"read"` - `"present"` ← (default) - `"absent"` |
| **value**  string | Value to set for the specified dconf key. Value should be specified in GVariant format. Due to complexity of this format, it is best to have a look at existing values in the dconf database.  Required for *state=present*. |

## [Notes](dconf_module.md#id3)

> **Note:**
>
> - This module depends on `psutil` Python library (version 4.0.0 and upwards), `dconf`, `dbus-send`, and `dbus-run-session` binaries. Depending on distribution you are using, you may need to install additional packages to have these available.
> - Detection of existing, running D-Bus session, required to change settings via `dconf`, is not 100% reliable due to implementation details of D-Bus daemon itself. This might lead to running applications not picking-up changes on the fly if options are changed via Ansible and `dbus-run-session`.
> - Keep in mind that the `dconf` CLI tool, which this module wraps around, utilises an unusual syntax for the values (GVariant). For example, if you wanted to provide a string value, the correct syntax would be *value=“‘myvalue’”* - with single quotes as part of the Ansible parameter value.
> - When using loops in combination with a value like :code:`”[(‘xkb’, ‘us’), (‘xkb’, ‘se’)]”`, you need to be aware of possible type conversions. Applying a filter :code:`”{{ item.value | string }}”` to the parameter variable can avoid potential conversion problems.
> - The easiest way to figure out exact syntax/value you need to provide for a key is by making the configuration change in application affected by the key, and then having a look at value set via commands `dconf dump /path/to/dir/` or `dconf read /path/to/key`.

## [Examples](dconf_module.md#id4)

```yaml+jinja
- name: Configure available keyboard layouts in Gnome
  community.general.dconf:
    key: "/org/gnome/desktop/input-sources/sources"
    value: "[('xkb', 'us'), ('xkb', 'se')]"
    state: present

- name: Read currently available keyboard layouts in Gnome
  community.general.dconf:
    key: "/org/gnome/desktop/input-sources/sources"
    state: read
  register: keyboard_layouts

- name: Reset the available keyboard layouts in Gnome
  community.general.dconf:
    key: "/org/gnome/desktop/input-sources/sources"
    state: absent

- name: Configure available keyboard layouts in Cinnamon
  community.general.dconf:
    key: "/org/gnome/libgnomekbd/keyboard/layouts"
    value: "['us', 'se']"
    state: present

- name: Read currently available keyboard layouts in Cinnamon
  community.general.dconf:
    key: "/org/gnome/libgnomekbd/keyboard/layouts"
    state: read
  register: keyboard_layouts

- name: Reset the available keyboard layouts in Cinnamon
  community.general.dconf:
    key: "/org/gnome/libgnomekbd/keyboard/layouts"
    state: absent

- name: Disable desktop effects in Cinnamon
  community.general.dconf:
    key: "/org/cinnamon/desktop-effects"
    value: "false"
    state: present
```

## [Return Values](dconf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  string | value associated with the requested key  Returned: success, state was “read”  Sample: `"'Default'"` |

### Authors

- Branko Majic (@azaghal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
