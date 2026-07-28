---
collection: ansible
version: "8"
title: "community.general.cargo module – Manage Rust packages with cargo"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cargo_module.html
fetched_at: 2026-07-28T01:44:56+00:00
---
# community.general.cargo module – Manage Rust packages with cargo

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
> see [Requirements](cargo_module.md#ansible-collections-community-general-cargo-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.cargo`.

New in community.general 4.3.0

- [Synopsis](cargo_module.md#synopsis)
- [Requirements](cargo_module.md#requirements)
- [Parameters](cargo_module.md#parameters)
- [Attributes](cargo_module.md#attributes)
- [Examples](cargo_module.md#examples)

## [Synopsis](cargo_module.md#id1)

- Manage Rust packages with cargo.

Aliases: packaging.language.cargo

## [Requirements](cargo_module.md#id2)

The below requirements are needed on the host that executes this module.

- cargo installed

## [Parameters](cargo_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  path  *added in community.general 7.5.0* | Path to the `cargo` installed in the system.  If not specified, the module will look `cargo` in `PATH`. |
| **locked**  boolean  *added in community.general 7.5.0* | Install with locked dependencies.  This is only used when installing packages.  **Choices:**   - `false` ← (default) - `true` |
| **name**  list / elements=string / required | The name of a Rust package to install. |
| **path**  path | -> The base path where to install the Rust packages. Cargo automatically appends `/bin`. In other words, `/usr/local` will become `/usr/local/bin`. |
| **state**  string | The state of the Rust package.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` |
| **version**  string | -> The version to install. If `name` contains multiple values, the module will try to install all of them in this version. |

## [Attributes](cargo_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](cargo_module.md#id5)

```yaml+jinja
- name: Install "ludusavi" Rust package
  community.general.cargo:
    name: ludusavi

- name: Install "ludusavi" Rust package with locked dependencies
  community.general.cargo:
    name: ludusavi
    locked: true

- name: Install "ludusavi" Rust package in version 0.10.0
  community.general.cargo:
    name: ludusavi
    version: '0.10.0'

- name: Install "ludusavi" Rust package to global location
  community.general.cargo:
    name: ludusavi
    path: /usr/local

- name: Remove "ludusavi" Rust package
  community.general.cargo:
    name: ludusavi
    state: absent

- name: Update "ludusavi" Rust package its latest version
  community.general.cargo:
    name: ludusavi
    state: latest
```

### Authors

- Radek Sprta (@radek-sprta)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
