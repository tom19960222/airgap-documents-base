---
collection: ansible
version: "8"
title: "community.general.xbps module – Manage packages with XBPS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xbps_module.html
fetched_at: 2026-07-28T01:51:28+00:00
---
# community.general.xbps module – Manage packages with XBPS

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
> To use it in a playbook, specify: `community.general.xbps`.

- [Synopsis](xbps_module.md#synopsis)
- [Parameters](xbps_module.md#parameters)
- [Attributes](xbps_module.md#attributes)
- [Examples](xbps_module.md#examples)
- [Return Values](xbps_module.md#return-values)

## [Synopsis](xbps_module.md#id1)

- Manage packages with the XBPS package manager.

Aliases: packaging.os.xbps

## [Parameters](xbps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pkg, package  list / elements=string | Name of the package to install, upgrade, or remove. |
| **recurse**  boolean | When removing a package, also remove its dependencies, provided that they are not required by other packages and were not explicitly installed by a user.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Desired state of the package.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` - `"installed"` - `"removed"` |
| **update_cache**  boolean | Whether or not to refresh the master package lists. This can be run as part of a package installation or as a separate step.  **Choices:**   - `false` - `true` ← (default) |
| **upgrade**  boolean | Whether or not to upgrade whole system  **Choices:**   - `false` ← (default) - `true` |
| **upgrade_xbps**  boolean  *added in community.general 0.2.0* | Whether or not to upgrade the xbps package when necessary. Before installing new packages, xbps requires the user to update the xbps package itself. Thus when this option is set to `false`, upgrades and installations will fail when xbps is not up to date.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](xbps_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](xbps_module.md#id4)

```yaml+jinja
- name: Install package foo (automatically updating the xbps package if needed)
  community.general.xbps:
    name: foo
    state: present

- name: Upgrade package foo
  community.general.xbps:
    name: foo
    state: latest
    update_cache: true

- name: Remove packages foo and bar
  community.general.xbps:
    name:
      - foo
      - bar
    state: absent

- name: Recursively remove package foo
  community.general.xbps:
    name: foo
    state: absent
    recurse: true

- name: Update package cache
  community.general.xbps:
    update_cache: true

- name: Upgrade packages
  community.general.xbps:
    upgrade: true

- name: Install a package, failing if the xbps package is out of date
  community.general.xbps:
    name: foo
    state: present
    upgrade_xbps: false
```

## [Return Values](xbps_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message about results  **Returned:** success  **Sample:** `"System Upgraded"` |
| **packages**  list / elements=string | Packages that are affected/would be affected  **Returned:** success  **Sample:** `["ansible"]` |

### Authors

- Dino Occhialini (@dinoocch)
- Michael Aldridge (@the-maldridge)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
