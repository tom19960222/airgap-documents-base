---
collection: ansible
version: "8"
title: "community.general.homebrew module – Package manager for Homebrew"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/homebrew_module.html
fetched_at: 2026-07-28T01:46:01+00:00
---
# community.general.homebrew module – Package manager for Homebrew

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
> see [Requirements](homebrew_module.md#ansible-collections-community-general-homebrew-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.homebrew`.

- [Synopsis](homebrew_module.md#synopsis)
- [Requirements](homebrew_module.md#requirements)
- [Parameters](homebrew_module.md#parameters)
- [Attributes](homebrew_module.md#attributes)
- [Notes](homebrew_module.md#notes)
- [Examples](homebrew_module.md#examples)
- [Return Values](homebrew_module.md#return-values)

## [Synopsis](homebrew_module.md#id1)

- Manages Homebrew packages

Aliases: packaging.os.homebrew

## [Requirements](homebrew_module.md#id2)

The below requirements are needed on the host that executes this module.

- homebrew must already be installed on the target system

## [Parameters](homebrew_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **install_options**  aliases: options  list / elements=string | options flags to install a package. |
| **name**  aliases: formula, package, pkg  list / elements=string | A list of names of packages to install/remove. |
| **path**  path | A `:` separated list of paths to search for `brew` executable. Since a package (*formula* in homebrew parlance) location is prefixed relative to the actual path of `brew` command, providing an alternative `brew` path enables managing different set of packages in an alternative location in the system.  **Default:** `"/usr/local/bin:/opt/homebrew/bin:/home/linuxbrew/.linuxbrew/bin"` |
| **state**  string | state of the package.  **Choices:**   - `"absent"` - `"head"` - `"installed"` - `"latest"` - `"linked"` - `"present"` ← (default) - `"removed"` - `"uninstalled"` - `"unlinked"` - `"upgraded"` |
| **update_homebrew**  boolean | update homebrew itself first.  **Choices:**   - `false` ← (default) - `true` |
| **upgrade_all**  aliases: upgrade  boolean | upgrade all homebrew packages.  **Choices:**   - `false` ← (default) - `true` |
| **upgrade_options**  list / elements=string  *added in community.general 0.2.0* | Option flags to upgrade. |

## [Attributes](homebrew_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](homebrew_module.md#id5)

> **Note:**
>
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the `name` option.

## [Examples](homebrew_module.md#id6)

```yaml+jinja
# Install formula foo with 'brew' in default path
- community.general.homebrew:
    name: foo
    state: present

# Install formula foo with 'brew' in alternate path (/my/other/location/bin)
- community.general.homebrew:
    name: foo
    path: /my/other/location/bin
    state: present

# Update homebrew first and install formula foo with 'brew' in default path
- community.general.homebrew:
    name: foo
    state: present
    update_homebrew: true

# Update homebrew first and upgrade formula foo to latest available with 'brew' in default path
- community.general.homebrew:
    name: foo
    state: latest
    update_homebrew: true

# Update homebrew and upgrade all packages
- community.general.homebrew:
    update_homebrew: true
    upgrade_all: true

# Miscellaneous other examples
- community.general.homebrew:
    name: foo
    state: head

- community.general.homebrew:
    name: foo
    state: linked

- community.general.homebrew:
    name: foo
    state: absent

- community.general.homebrew:
    name: foo,bar
    state: absent

- community.general.homebrew:
    name: foo
    state: present
    install_options: with-baz,enable-debug

- name: Install formula foo with 'brew' from cask
  community.general.homebrew:
    name: homebrew/cask/foo
    state: present

- name: Use ignore-pinned option while upgrading all
  community.general.homebrew:
    upgrade_all: true
    upgrade_options: ignore-pinned
```

## [Return Values](homebrew_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed_pkgs**  list / elements=string  *added in community.general 0.2.0* | List of package names which are changed after module run  **Returned:** success  **Sample:** `["git", "git-cola"]` |
| **msg**  string | if the cache was updated or not  **Returned:** always  **Sample:** `"Changed: 0, Unchanged: 2"` |
| **unchanged_pkgs**  list / elements=string  *added in community.general 0.2.0* | List of package names which are unchanged after module run  **Returned:** success  **Sample:** `["awscli", "ag"]` |

### Authors

- Indrajit Raychaudhuri (@indrajitr)
- Daniel Jaouen (@danieljaouen)
- Andrew Dunham (@andrew-d)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
