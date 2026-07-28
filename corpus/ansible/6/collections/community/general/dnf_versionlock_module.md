---
collection: ansible
version: "6"
title: "community.general.dnf_versionlock module – Locks package versions in dnf based systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dnf_versionlock_module.html
fetched_at: 2026-07-27T17:08:46+00:00
---
# community.general.dnf_versionlock module – Locks package versions in `dnf` based systems

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
> see [Requirements](dnf_versionlock_module.md#ansible-collections-community-general-dnf-versionlock-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dnf_versionlock`.

New in community.general 4.0.0

- [Synopsis](dnf_versionlock_module.md#synopsis)
- [Requirements](dnf_versionlock_module.md#requirements)
- [Parameters](dnf_versionlock_module.md#parameters)
- [Notes](dnf_versionlock_module.md#notes)
- [Examples](dnf_versionlock_module.md#examples)
- [Return Values](dnf_versionlock_module.md#return-values)

## [Synopsis](dnf_versionlock_module.md#id1)

- Locks package versions using the `versionlock` plugin in `dnf` based systems. This plugin takes a set of name and versions for packages and excludes all other versions of those packages. This allows you to for example protect packages from being updated by newer versions. The state of the plugin that reflects locking of packages is the `locklist`.

## [Requirements](dnf_versionlock_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnf
- dnf-plugin-versionlock

## [Parameters](dnf_versionlock_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  list / elements=string | Package name spec to add or exclude to or delete from the `locklist` using the format expected by the `dnf repoquery` command.  This parameter is mutually exclusive with *state=clean*.  Default: `[]` |
| **raw**  boolean | Do not resolve package name specs to NEVRAs to find specific version to lock to. Instead the package name specs are used as they are. This enables locking to not yet available versions of the package.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Whether to add (`present` or `excluded`) to or remove (`absent` or `clean`) from the `locklist`.  `present` will add a package name spec to the `locklist`. If there is a installed package that matches, then only that version will be added. Otherwise, all available package versions will be added.  `excluded` will add a package name spec as excluded to the `locklist`. It means that packages represented by the package name spec will be excluded from transaction operations. All available package versions will be added.  `absent` will delete entries in the `locklist` that match the package name spec.  `clean` will delete all entries in the `locklist`. This option is mutually exclusive with `name`.  Choices:   - `"absent"` - `"clean"` - `"excluded"` - `"present"` ← (default) |

## [Notes](dnf_versionlock_module.md#id4)

> **Note:**
>
> - The logics of the `versionlock` plugin for corner cases could be confusing, so please take in account that this module will do its best to give a `check_mode` prediction on what is going to happen. In case of doubt, check the documentation of the plugin.
> - Sometimes the module could predict changes in `check_mode` that will not be such because `versionlock` concludes that there is already a entry in `locklist` that already matches.
> - In an ideal world, the `versionlock` plugin would have a dry-run option to know for sure what is going to happen. So far we have to work with a best guess as close as possible to the behaviour inferred from its code.
> - For most of cases where you want to lock and unlock specific versions of a package, this works fairly well.
> - Supports `check_mode`.

## [Examples](dnf_versionlock_module.md#id5)

```yaml+jinja
- name: Prevent installed nginx from being updated
  community.general.dnf_versionlock:
    name: nginx
    state: present

- name: Prevent multiple packages from being updated
  community.general.dnf_versionlock:
    name:
      - nginx
      - haproxy
    state: present

- name: Remove lock from nginx to be updated again
  community.general.dnf_versionlock:
    package: nginx
    state: absent

- name: Exclude bind 32:9.11 from installs or updates
  community.general.dnf_versionlock:
    package: bind-32:9.11*
    state: excluded

- name: Keep bash package in major version 4
  community.general.dnf_versionlock:
    name: bash-0:4.*
    raw: true
    state: present

- name: Delete all entries in the locklist of versionlock
  community.general.dnf_versionlock:
    state: clean
```

## [Return Values](dnf_versionlock_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **locklist_post**  list / elements=string | Locklist after module execution.  Returned: success and (not check mode or state is clean)  Sample: `["bash-0:4.4.20-1.el8_4.*"]` |
| **locklist_pre**  list / elements=string | Locklist before module execution.  Returned: success  Sample: `["bash-0:4.4.20-1.el8_4.*", "!bind-32:9.11.26-4.el8_4.*"]` |
| **specs_toadd**  list / elements=string | Package name specs meant to be added by versionlock.  Returned: success  Sample: `["bash"]` |
| **specs_todelete**  list / elements=string | Package name specs meant to be deleted by versionlock.  Returned: success  Sample: `["bind"]` |

### Authors

- Roberto Moreda (@moreda)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
