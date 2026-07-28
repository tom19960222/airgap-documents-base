---
collection: ansible
version: "8"
title: "community.general.gio_mime module – Set default handler for MIME type, for applications using Gnome GIO"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gio_mime_module.html
fetched_at: 2026-07-28T01:45:39+00:00
---
# community.general.gio_mime module – Set default handler for MIME type, for applications using Gnome GIO

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
> To use it in a playbook, specify: `community.general.gio_mime`.

New in community.general 7.5.0

- [Synopsis](gio_mime_module.md#synopsis)
- [Parameters](gio_mime_module.md#parameters)
- [Attributes](gio_mime_module.md#attributes)
- [Notes](gio_mime_module.md#notes)
- [See Also](gio_mime_module.md#see-also)
- [Examples](gio_mime_module.md#examples)
- [Return Values](gio_mime_module.md#return-values)

## [Synopsis](gio_mime_module.md#id1)

- This module allows configuring the default handler for a specific MIME type, to be used by applications built with th Gnome GIO API.

## [Parameters](gio_mime_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **handler**  string / required | Default handler will be set for the MIME type. |
| **mime_type**  string / required | MIME type for which a default handler will be set. |

## [Attributes](gio_mime_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](gio_mime_module.md#id4)

> **Note:**
>
> - This module is a thin wrapper around the `gio mime` command (and subcommand).
> - See man gio(1) for more details.

## [See Also](gio_mime_module.md#id5)

> **See also:**
>
> [GIO Documentation](https://docs.gtk.org/gio/)
> :   Reference documentation for the GIO API..

## [Examples](gio_mime_module.md#id6)

```yaml+jinja
- name: Set chrome as the default handler for https
  community.general.gio_mime:
    mime_type: x-scheme-handler/https
    handler: google-chrome.desktop
  register: result
```

## [Return Values](gio_mime_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **handler**  string | The handler set as default.  **Returned:** success  **Sample:** `"google-chrome.desktop"` |
| **stderr**  string | The error output of the `gio` command.  **Returned:** failure  **Sample:** `"gio: Failed to load info for handler \"never-existed.desktop\""` |
| **stdout**  string | The output of the `gio` command.  **Returned:** success  **Sample:** `"Set google-chrome.desktop as the default for x-scheme-handler/https"` |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
