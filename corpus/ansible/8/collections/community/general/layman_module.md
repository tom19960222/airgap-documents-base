---
collection: ansible
version: "8"
title: "community.general.layman module – Manage Gentoo overlays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/layman_module.html
fetched_at: 2026-07-28T01:47:25+00:00
---
# community.general.layman module – Manage Gentoo overlays

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](layman_module.md#ansible-collections-community-general-layman-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.layman`.

- [Synopsis](layman_module.md#synopsis)
- [Requirements](layman_module.md#requirements)
- [Parameters](layman_module.md#parameters)
- [Attributes](layman_module.md#attributes)
- [Examples](layman_module.md#examples)

## [Synopsis](layman_module.md#id1)

- Uses Layman to manage an additional repositories for the Portage package manager on Gentoo Linux. Please note that Layman must be installed on a managed node prior using this module.

Aliases: packaging.os.layman

## [Requirements](layman_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- layman python module

## [Parameters](layman_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **list_url**  aliases: url  string | An URL of the alternative overlays list that defines the overlay to install. This list will be fetched and saved under `${overlay_defs}/${name}.xml`, where `overlay_defs` is read from the Layman’s configuration. |
| **name**  string / required | The overlay id to install, synchronize, or uninstall. Use ‘ALL’ to sync all of the installed overlays (can be used only when `state=updated`). |
| **state**  string | Whether to install (`present`), sync (`updated`), or uninstall (`absent`) the overlay.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"updated"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be set to `false` when no other option exists. Prior to 1.9.3 the code defaulted to `false`.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](layman_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](layman_module.md#id5)

```yaml+jinja
- name: Install the overlay mozilla which is on the central overlays list
  community.general.layman:
    name: mozilla

- name: Install the overlay cvut from the specified alternative list
  community.general.layman:
    name: cvut
    list_url: 'http://raw.github.com/cvut/gentoo-overlay/master/overlay.xml'

- name: Update (sync) the overlay cvut or install if not installed yet
  community.general.layman:
    name: cvut
    list_url: 'http://raw.github.com/cvut/gentoo-overlay/master/overlay.xml'
    state: updated

- name: Update (sync) all of the installed overlays
  community.general.layman:
    name: ALL
    state: updated

- name: Uninstall the overlay cvut
  community.general.layman:
    name: cvut
    state: absent
```

### Authors

- Jakub Jirutka (@jirutka)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
