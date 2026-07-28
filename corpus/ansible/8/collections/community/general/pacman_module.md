---
collection: ansible
version: "8"
title: "community.general.pacman module – Manage packages with pacman"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pacman_module.html
fetched_at: 2026-07-28T01:48:53+00:00
---
# community.general.pacman module – Manage packages with *pacman*

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
> To use it in a playbook, specify: `community.general.pacman`.

- [Synopsis](pacman_module.md#synopsis)
- [Parameters](pacman_module.md#parameters)
- [Attributes](pacman_module.md#attributes)
- [Notes](pacman_module.md#notes)
- [Examples](pacman_module.md#examples)
- [Return Values](pacman_module.md#return-values)

## [Synopsis](pacman_module.md#id1)

- Manage packages with the *pacman* package manager, which is used by Arch Linux and its variants.

Aliases: packaging.os.pacman

## [Parameters](pacman_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **executable**  string  *added in community.general 3.1.0* | Path of the binary to use. This can either be `pacman` or a pacman compatible AUR helper.  Pacman compatibility is unfortunately ill defined, in particular, this modules makes extensive use of the `--print-format` directive which is known not to be implemented by some AUR helpers (notably, `yay`).  Beware that AUR helpers might behave unexpectedly and are therefore not recommended.  **Default:** `"pacman"` |
| **extra_args**  string | Additional option to pass to pacman when enforcing `state`.  **Default:** `""` |
| **force**  boolean | When removing packages, forcefully remove them, without any checks. Same as `extra_args="--nodeps --nodeps"`.  When combined with `update_cache`, force a refresh of all package databases. Same as `update_cache_extra_args="--refresh --refresh"`.  **Choices:**   - `false` ← (default) - `true` |
| **name**  aliases: package, pkg  list / elements=string | Name or list of names of the package(s) or file(s) to install, upgrade, or remove. Cannot be used in combination with `upgrade`. |
| **reason**  string  *added in community.general 5.4.0* | The install reason to set for the packages.  **Choices:**   - `"dependency"` - `"explicit"` |
| **reason_for**  string  *added in community.general 5.4.0* | Set the install reason for `all` packages or only for `new` packages.  In case of `state=latest` already installed packages which will be updated to a newer version are not counted as `new`.  **Choices:**   - `"all"` - `"new"` ← (default) |
| **remove_nosave**  boolean  *added in community.general 4.6.0* | When removing packages, do not save modified configuration files as `.pacsave` files. (passes `--nosave` to pacman)  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether to install (`present` or `installed`, `latest`), or remove (`absent` or `removed`) a package.  `present` and `installed` will simply ensure that a desired package is installed.  `latest` will update the specified package if it is not of the latest available version.  `absent` and `removed` will remove the specified package.  **Choices:**   - `"absent"` - `"installed"` - `"latest"` - `"present"` ← (default) - `"removed"` |
| **update_cache**  boolean | Whether or not to refresh the master package lists.  This can be run as part of a package installation or as a separate step.  If not specified, it defaults to `false`.  Please note that this option only had an influence on the module’s `changed` state if `name` and `upgrade` are not specified before community.general 5.0.0. See the examples for how to keep the old behavior.  **Choices:**   - `false` - `true` |
| **update_cache_extra_args**  string | Additional option to pass to pacman when enforcing `update_cache`.  **Default:** `""` |
| **upgrade**  boolean | Whether or not to upgrade the whole system. Cannot be used in combination with `name`.  If not specified, it defaults to `false`.  **Choices:**   - `false` - `true` |
| **upgrade_extra_args**  string | Additional option to pass to pacman when enforcing `upgrade`.  **Default:** `""` |

## [Attributes](pacman_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pacman_module.md#id4)

> **Note:**
>
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the `name` option.
> - To use an AUR helper (`executable` option), a few extra setup steps might be required beforehand. For example, a dedicated build user with permissions to install packages could be necessary.
> - In the tests, while using `yay` as the `executable` option, the module failed to install AUR packages with the error: `error: target not found: <pkg>`.

## [Examples](pacman_module.md#id5)

```yaml+jinja
- name: Install package foo from repo
  community.general.pacman:
    name: foo
    state: present

- name: Install package bar from file
  community.general.pacman:
    name: ~/bar-1.0-1-any.pkg.tar.xz
    state: present

- name: Install package foo from repo and bar from file
  community.general.pacman:
    name:
      - foo
      - ~/bar-1.0-1-any.pkg.tar.xz
    state: present

- name: Install package from AUR using a Pacman compatible AUR helper
  community.general.pacman:
    name: foo
    state: present
    executable: yay
    extra_args: --builddir /var/cache/yay

- name: Upgrade package foo
  # The 'changed' state of this call will indicate whether the cache was
  # updated *or* whether foo was installed/upgraded.
  community.general.pacman:
    name: foo
    state: latest
    update_cache: true

- name: Remove packages foo and bar
  community.general.pacman:
    name:
      - foo
      - bar
    state: absent

- name: Recursively remove package baz
  community.general.pacman:
    name: baz
    state: absent
    extra_args: --recursive

- name: Run the equivalent of "pacman -Sy" as a separate step
  community.general.pacman:
    update_cache: true

- name: Run the equivalent of "pacman -Su" as a separate step
  community.general.pacman:
    upgrade: true

- name: Run the equivalent of "pacman -Syu" as a separate step
  # Since community.general 5.0.0 the 'changed' state of this call
  # will be 'true' in case the cache was updated, or when a package
  # was updated.
  #
  # The previous behavior was to only indicate whether something was
  # upgraded. To keep the old behavior, add the following to the task:
  #
  #   register: result
  #   changed_when: result.packages | length > 0
  community.general.pacman:
    update_cache: true
    upgrade: true

- name: Run the equivalent of "pacman -Rdd", force remove package baz
  community.general.pacman:
    name: baz
    state: absent
    force: true

- name: Install foo as dependency and leave reason untouched if already installed
  community.general.pacman:
    name: foo
    state: present
    reason: dependency
    reason_for: new

- name: Run the equivalent of "pacman -S --asexplicit", mark foo as explicit and install it if not present
  community.general.pacman:
    name: foo
    state: present
    reason: explicit
    reason_for: all
```

## [Return Values](pacman_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cache_updated**  boolean  *added in community.general 4.6.0* | The changed status of `pacman -Sy`.  Useful when `name` or `upgrade=true` are specified next to `update_cache=true`.  **Returned:** success, when `update_cache=true`  **Sample:** `false` |
| **packages**  list / elements=string | A list of packages that have been changed.  Before community.general 4.5.0 this was only returned when `upgrade=true`. In community.general 4.5.0, it was sometimes omitted when the package list is empty, but since community.general 4.6.0 it is always returned when `name` is specified or `upgrade=true`.  **Returned:** success and `name` is specified or `upgrade=true`  **Sample:** `["package", "other-package"]` |
| **stderr**  string  *added in community.general 4.1.0* | Error output from pacman.  **Returned:** success, when needed  **Sample:** `"warning: libtool: local (2.4.6+44+gb9b44533-14) is newer than core (2.4.6+42+gb88cebd5-15) warning ..."` |
| **stdout**  string  *added in community.general 4.1.0* | Output from pacman.  **Returned:** success, when needed  **Sample:** `":: Synchronizing package databases...  core is up to date :: Starting full system upgrade..."` |

### Authors

- Indrajit Raychaudhuri (@indrajitr)
- Aaron Bull Schaefer (@elasticdog)
- Maxime de Roucy (@tchernomax)
- Jean Raby (@jraby)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
