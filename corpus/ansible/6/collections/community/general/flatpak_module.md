---
collection: ansible
version: "6"
title: "community.general.flatpak module – Manage flatpaks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/flatpak_module.html
fetched_at: 2026-07-27T17:08:55+00:00
---
# community.general.flatpak module – Manage flatpaks

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](flatpak_module.md#ansible-collections-community-general-flatpak-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.flatpak`.

- [Synopsis](flatpak_module.md#synopsis)
- [Requirements](flatpak_module.md#requirements)
- [Parameters](flatpak_module.md#parameters)
- [Examples](flatpak_module.md#examples)
- [Return Values](flatpak_module.md#return-values)

## [Synopsis](flatpak_module.md#id1)

- Allows users to add or remove flatpaks.
- See the [community.general.flatpak_remote](flatpak_remote_module.md#ansible-collections-community-general-flatpak-remote-module) module for managing flatpak remotes.

## [Requirements](flatpak_module.md#id2)

The below requirements are needed on the host that executes this module.

- flatpak

## [Parameters](flatpak_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  path | The path to the `flatpak` executable to use.  By default, this module looks for the `flatpak` executable on the path.  Default: `"flatpak"` |
| **method**  string | The installation method to use.  Defines if the *flatpak* is supposed to be installed globally for the whole `system` or only for the current `user`.  Choices:   - `"system"` ← (default) - `"user"` |
| **name**  list / elements=string / required | The name of the flatpak to manage. To operate on several packages this can accept a list of packages.  When used with *state=present*, *name* can be specified as a URL to a `flatpakref` file or the unique reverse DNS name that identifies a flatpak.  Both `https://` and `http://` URLs are supported.  When supplying a reverse DNS name, you can use the *remote* option to specify on what remote to look for the flatpak. An example for a reverse DNS name is `org.gnome.gedit`.  When used with *state=absent*, it is recommended to specify the name in the reverse DNS format.  When supplying a URL with *state=absent*, the module will try to match the installed flatpak based on the name of the flatpakref to remove it. However, there is no guarantee that the names of the flatpakref file and the reverse DNS name of the installed flatpak do match. |
| **no_dependencies**  boolean  added in community.general 3.2.0 | If installing runtime dependencies should be omitted or not  This parameter is primarily implemented for integration testing this module. There might however be some use cases where you would want to have this, like when you are packaging your own flatpaks.  Choices:   - `false` ← (default) - `true` |
| **remote**  string | The flatpak remote (repository) to install the flatpak from.  By default, `flathub` is assumed, but you do need to add the flathub flatpak_remote before you can use this.  See the [community.general.flatpak_remote](flatpak_remote_module.md#ansible-collections-community-general-flatpak-remote-module) module for managing flatpak remotes.  Default: `"flathub"` |
| **state**  string | Indicates the desired package state.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](flatpak_module.md#id4)

```yaml+jinja
- name: Install the spotify flatpak
  community.general.flatpak:
    name:  https://s3.amazonaws.com/alexlarsson/spotify-repo/spotify.flatpakref
    state: present

- name: Install the gedit flatpak package without dependencies (not recommended)
  community.general.flatpak:
    name: https://git.gnome.org/browse/gnome-apps-nightly/plain/gedit.flatpakref
    state: present
    no_dependencies: true

- name: Install the gedit package from flathub for current user
  community.general.flatpak:
    name: org.gnome.gedit
    state: present
    method: user

- name: Install the Gnome Calendar flatpak from the gnome remote system-wide
  community.general.flatpak:
    name: org.gnome.Calendar
    state: present
    remote: gnome

- name: Install multiple packages
  community.general.flatpak:
    name:
      - org.gimp.GIMP
      - org.inkscape.Inkscape
      - org.mozilla.firefox

- name: Remove the gedit flatpak
  community.general.flatpak:
    name: org.gnome.gedit
    state: absent

- name: Remove multiple packages
  community.general.flatpak:
    name:
      - org.gimp.GIMP
      - org.inkscape.Inkscape
      - org.mozilla.firefox
    state: absent
```

## [Return Values](flatpak_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | The exact flatpak command that was executed  Returned: When a flatpak command has been executed  Sample: `"/usr/bin/flatpak install --user --nontinteractive flathub org.gnome.Calculator"` |
| **msg**  string | Module error message  Returned: failure  Sample: `"Executable '/usr/local/bin/flatpak' was not found on the system."` |
| **rc**  integer | Return code from flatpak binary  Returned: When a flatpak command has been executed  Sample: `0` |
| **stderr**  string | Error output from flatpak binary  Returned: When a flatpak command has been executed  Sample: `"error: Error searching remote flathub: Can't find ref org.gnome.KDE"` |
| **stdout**  string | Output from flatpak binary  Returned: When a flatpak command has been executed  Sample: `"org.gnome.Calendar/x86_64/stable\tcurrent\norg.gnome.gitg/x86_64/stable\tcurrent\n"` |

### Authors

- John Kwiatkoski (@JayKayy)
- Alexander Bethke (@oolongbrothers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
