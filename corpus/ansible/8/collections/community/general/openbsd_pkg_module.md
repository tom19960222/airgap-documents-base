---
collection: ansible
version: "8"
title: "community.general.openbsd_pkg module – Manage packages on OpenBSD"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/openbsd_pkg_module.html
fetched_at: 2026-07-28T01:48:42+00:00
---
# community.general.openbsd_pkg module – Manage packages on OpenBSD

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
> To use it in a playbook, specify: `community.general.openbsd_pkg`.

- [Synopsis](openbsd_pkg_module.md#synopsis)
- [Parameters](openbsd_pkg_module.md#parameters)
- [Attributes](openbsd_pkg_module.md#attributes)
- [Notes](openbsd_pkg_module.md#notes)
- [Examples](openbsd_pkg_module.md#examples)

## [Synopsis](openbsd_pkg_module.md#id1)

- Manage packages on OpenBSD using the pkg tools.

Aliases: packaging.os.openbsd_pkg

## [Parameters](openbsd_pkg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **build**  boolean | Build the package from source instead of downloading and installing a binary. Requires that the port source tree is already installed. Automatically builds and installs the ‘sqlports’ package, if it is not already installed.  Mutually exclusive with `snapshot`.  **Choices:**   - `false` ← (default) - `true` |
| **clean**  boolean | When updating or removing packages, delete the extra configuration file(s) in the old packages which are annotated with @extra in the packaging-list.  **Choices:**   - `false` ← (default) - `true` |
| **name**  list / elements=string / required | A name or a list of names of the packages. |
| **ports_dir**  path | When used in combination with the `build` option, allows overriding the default ports source directory.  **Default:** `"/usr/ports"` |
| **quick**  boolean | Replace or delete packages quickly; do not bother with checksums before removing normal files.  **Choices:**   - `false` ← (default) - `true` |
| **snapshot**  boolean  *added in community.general 1.3.0* | Force `%c` and `%m` to expand to `snapshots`, even on a release kernel.  Mutually exclusive with `build`.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | `present` will make sure the package is installed.  `latest` will make sure the latest version of the package is installed.  `absent` will make sure the specified package is not installed.  **Choices:**   - `"absent"` - `"latest"` - `"present"` ← (default) - `"installed"` - `"removed"` |

## [Attributes](openbsd_pkg_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](openbsd_pkg_module.md#id4)

> **Note:**
>
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the `name` option.

## [Examples](openbsd_pkg_module.md#id5)

```yaml+jinja
- name: Make sure nmap is installed
  community.general.openbsd_pkg:
    name: nmap
    state: present

- name: Make sure nmap is the latest version
  community.general.openbsd_pkg:
    name: nmap
    state: latest

- name: Make sure nmap is not installed
  community.general.openbsd_pkg:
    name: nmap
    state: absent

- name: Make sure nmap is installed, build it from source if it is not
  community.general.openbsd_pkg:
    name: nmap
    state: present
    build: true

- name: Specify a pkg flavour with '--'
  community.general.openbsd_pkg:
    name: vim--no_x11
    state: present

- name: Specify the default flavour to avoid ambiguity errors
  community.general.openbsd_pkg:
    name: vim--
    state: present

- name: Specify a package branch (requires at least OpenBSD 6.0)
  community.general.openbsd_pkg:
    name: python%3.5
    state: present

- name: Update all packages on the system
  community.general.openbsd_pkg:
    name: '*'
    state: latest

- name: Purge a package and it's configuration files
  community.general.openbsd_pkg:
    name: mpd
    clean: true
    state: absent

- name: Quickly remove a package without checking checksums
  community.general.openbsd_pkg:
    name: qt5
    quick: true
    state: absent
```

### Authors

- Patrik Lundin (@eest)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
