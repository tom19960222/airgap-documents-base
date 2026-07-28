---
collection: ansible
version: "8"
title: "community.general.apt_rpm module – APT-RPM package manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/apt_rpm_module.html
fetched_at: 2026-07-28T01:44:42+00:00
---
# community.general.apt_rpm module – APT-RPM package manager

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
> To use it in a playbook, specify: `community.general.apt_rpm`.

- [Synopsis](apt_rpm_module.md#synopsis)
- [Parameters](apt_rpm_module.md#parameters)
- [Attributes](apt_rpm_module.md#attributes)
- [Examples](apt_rpm_module.md#examples)

## [Synopsis](apt_rpm_module.md#id1)

- Manages packages with `apt-rpm`. Both low-level (`rpm`) and high-level (`apt-get`) package manager binaries required.

Aliases: packaging.os.apt_rpm

## [Parameters](apt_rpm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clean**  boolean  *added in community.general 6.5.0* | Run the equivalent of `apt-get clean` to clear out the local repository of retrieved package files. It removes everything but the lock file from `/var/cache/apt/archives/` and `/var/cache/apt/archives/partial/`.  Can be run as part of the package installation (clean runs before install) or as a separate step.  **Choices:**   - `false` ← (default) - `true` |
| **dist_upgrade**  boolean  *added in community.general 6.5.0* | If true performs an `apt-get dist-upgrade` to upgrade system.  **Choices:**   - `false` ← (default) - `true` |
| **package**  aliases: name, pkg  list / elements=string | List of packages to install, upgrade, or remove. |
| **state**  string | Indicates the desired package state.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"installed"` - `"removed"` |
| **update_cache**  boolean | Run the equivalent of `apt-get update` before the operation. Can be run as part of the package installation or as a separate step.  Default is not to update the cache.  **Choices:**   - `false` ← (default) - `true` |
| **update_kernel**  boolean  *added in community.general 6.5.0* | If true performs an `update-kernel` to upgrade kernel packages.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](apt_rpm_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](apt_rpm_module.md#id4)

```yaml+jinja
- name: Install package foo
  community.general.apt_rpm:
    pkg: foo
    state: present

- name: Install packages foo and bar
  community.general.apt_rpm:
    pkg:
      - foo
      - bar
    state: present

- name: Remove package foo
  community.general.apt_rpm:
    pkg: foo
    state: absent

- name: Remove packages foo and bar
  community.general.apt_rpm:
    pkg: foo,bar
    state: absent

# bar will be the updated if a newer version exists
- name: Update the package database and install bar
  community.general.apt_rpm:
    name: bar
    state: present
    update_cache: true

- name: Run the equivalent of "apt-get clean" as a separate step
  community.general.apt_rpm:
    clean: true

- name: Perform cache update and complete system upgrade (includes kernel)
  community.general.apt_rpm:
    update_cache: true
    dist_upgrade: true
    update_kernel: true
```

### Authors

- Evgenii Terechkov (@evgkrsk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
