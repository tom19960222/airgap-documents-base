---
collection: ansible
version: "8"
title: "community.general.flatpak_remote module – Manage flatpak repository remotes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/flatpak_remote_module.html
fetched_at: 2026-07-28T01:45:34+00:00
---
# community.general.flatpak_remote module – Manage flatpak repository remotes

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
> see [Requirements](flatpak_remote_module.md#ansible-collections-community-general-flatpak-remote-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.flatpak_remote`.

- [Synopsis](flatpak_remote_module.md#synopsis)
- [Requirements](flatpak_remote_module.md#requirements)
- [Parameters](flatpak_remote_module.md#parameters)
- [Attributes](flatpak_remote_module.md#attributes)
- [Examples](flatpak_remote_module.md#examples)
- [Return Values](flatpak_remote_module.md#return-values)

## [Synopsis](flatpak_remote_module.md#id1)

- Allows users to add or remove flatpak remotes.
- The flatpak remotes concept is comparable to what is called repositories in other packaging formats.
- Currently, remote addition is only supported via `flatpakrepo` file URLs.
- Existing remotes will not be updated.
- See the [community.general.flatpak](flatpak_module.md#ansible-collections-community-general-flatpak-module) module for managing flatpaks.

Aliases: packaging.os.flatpak_remote

## [Requirements](flatpak_remote_module.md#id2)

The below requirements are needed on the host that executes this module.

- flatpak

## [Parameters](flatpak_remote_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean  *added in community.general 6.4.0* | Indicates whether this remote is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **executable**  string | The path to the `flatpak` executable to use.  By default, this module looks for the `flatpak` executable on the path.  **Default:** `"flatpak"` |
| **flatpakrepo_url**  string | The URL to the `flatpakrepo` file representing the repository remote to add.  When used with `state=present`, the flatpak remote specified under the `flatpakrepo_url` is added using the specified installation `method`.  When used with `state=absent`, this is not required.  Required when `state=present`. |
| **method**  string | The installation method to use.  Defines if the `flatpak` is supposed to be installed globally for the whole `system` or only for the current `user`.  **Choices:**   - `"system"` ← (default) - `"user"` |
| **name**  string / required | The desired name for the flatpak remote to be registered under on the managed host.  When used with `state=present`, the remote will be added to the managed host under the specified `name`.  When used with `state=absent` the remote with that name will be removed. |
| **state**  string | Indicates the desired package state.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](flatpak_remote_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](flatpak_remote_module.md#id5)

```yaml+jinja
- name: Add the Gnome flatpak remote to the system installation
  community.general.flatpak_remote:
    name: gnome
    state: present
    flatpakrepo_url: https://sdk.gnome.org/gnome-apps.flatpakrepo

- name: Add the flathub flatpak repository remote to the user installation
  community.general.flatpak_remote:
    name: flathub
    state: present
    flatpakrepo_url: https://dl.flathub.org/repo/flathub.flatpakrepo
    method: user

- name: Remove the Gnome flatpak remote from the user installation
  community.general.flatpak_remote:
    name: gnome
    state: absent
    method: user

- name: Remove the flathub remote from the system installation
  community.general.flatpak_remote:
    name: flathub
    state: absent

- name: Disable the flathub remote in the system installation
  community.general.flatpak_remote:
    name: flathub
    state: present
    enabled: false
```

## [Return Values](flatpak_remote_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | The exact flatpak command that was executed  **Returned:** When a flatpak command has been executed  **Sample:** `"/usr/bin/flatpak remote-add --system flatpak-test https://dl.flathub.org/repo/flathub.flatpakrepo"` |
| **msg**  string | Module error message  **Returned:** failure  **Sample:** `"Executable '/usr/local/bin/flatpak' was not found on the system."` |
| **rc**  integer | Return code from flatpak binary  **Returned:** When a flatpak command has been executed  **Sample:** `0` |
| **stderr**  string | Error output from flatpak binary  **Returned:** When a flatpak command has been executed  **Sample:** `"error: GPG verification enabled, but no summary found (check that the configured URL in remote config is correct)\n"` |
| **stdout**  string | Output from flatpak binary  **Returned:** When a flatpak command has been executed  **Sample:** `"flathub\tFlathub\thttps://dl.flathub.org/repo/\t1\t\n"` |

### Authors

- John Kwiatkoski (@JayKayy)
- Alexander Bethke (@oolongbrothers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
