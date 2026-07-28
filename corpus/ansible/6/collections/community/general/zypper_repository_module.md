---
collection: ansible
version: "6"
title: "community.general.zypper_repository module – Add and remove Zypper repositories"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/zypper_repository_module.html
fetched_at: 2026-07-27T17:14:15+00:00
---
# community.general.zypper_repository module – Add and remove Zypper repositories

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
> see [Requirements](zypper_repository_module.md#ansible-collections-community-general-zypper-repository-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.zypper_repository`.

- [Synopsis](zypper_repository_module.md#synopsis)
- [Requirements](zypper_repository_module.md#requirements)
- [Parameters](zypper_repository_module.md#parameters)
- [Examples](zypper_repository_module.md#examples)

## [Synopsis](zypper_repository_module.md#id1)

- Add or remove Zypper repositories on SUSE and openSUSE

## [Requirements](zypper_repository_module.md#id2)

The below requirements are needed on the host that executes this module.

- zypper >= 1.0 # included in openSUSE >= 11.1 or SUSE Linux Enterprise Server/Desktop >= 11.0
- python-xml

## [Parameters](zypper_repository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_import_keys**  boolean | Automatically import the gpg signing key of the new or changed repository.  Has an effect only if state is *present*. Has no effect on existing (unchanged) repositories or in combination with *absent*.  Implies runrefresh.  Only works with `.repo` files if `name` is given explicitly.  Choices:   - `false` ← (default) - `true` |
| **autorefresh**  aliases: refresh  boolean | Enable autorefresh of the repository.  Choices:   - `false` - `true` ← (default) |
| **description**  string | A description of the repository |
| **disable_gpg_check**  boolean | Whether to disable GPG signature checking of all packages. Has an effect only if state is *present*.  Needs zypper version >= 1.6.2.  Choices:   - `false` ← (default) - `true` |
| **enabled**  boolean | Set repository to enabled (or disabled).  Choices:   - `false` - `true` ← (default) |
| **name**  string | A name for the repository. Not required when adding repofiles. |
| **overwrite_multiple**  boolean | Overwrite multiple repository entries, if repositories with both name and URL already exist.  Choices:   - `false` ← (default) - `true` |
| **priority**  integer | Set priority of repository. Packages will always be installed from the repository with the smallest priority number.  Needs zypper version >= 1.12.25. |
| **repo**  string | URI of the repository or .repo file. Required when state=present. |
| **runrefresh**  boolean | Refresh the package list of the given repository.  Can be used with repo=\* to refresh all repositories.  Choices:   - `false` ← (default) - `true` |
| **state**  string | A source string state.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](zypper_repository_module.md#id4)

```yaml+jinja
- name: Add NVIDIA repository for graphics drivers
  community.general.zypper_repository:
    name: nvidia-repo
    repo: 'ftp://download.nvidia.com/opensuse/12.2'
    state: present

- name: Remove NVIDIA repository
  community.general.zypper_repository:
    name: nvidia-repo
    repo: 'ftp://download.nvidia.com/opensuse/12.2'
    state: absent

- name: Add python development repository
  community.general.zypper_repository:
    repo: 'http://download.opensuse.org/repositories/devel:/languages:/python/SLE_11_SP3/devel:languages:python.repo'

- name: Refresh all repos
  community.general.zypper_repository:
    repo: '*'
    runrefresh: true

- name: Add a repo and add its gpg key
  community.general.zypper_repository:
    repo: 'http://download.opensuse.org/repositories/systemsmanagement/openSUSE_Leap_42.1/'
    auto_import_keys: true

- name: Force refresh of a repository
  community.general.zypper_repository:
    repo: 'http://my_internal_ci_repo/repo'
    name: my_ci_repo
    state: present
    runrefresh: true
```

### Authors

- Matthias Vogelgesang (@matze)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
