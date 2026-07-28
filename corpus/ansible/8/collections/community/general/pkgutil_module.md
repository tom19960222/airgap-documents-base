---
collection: ansible
version: "8"
title: "community.general.pkgutil module – OpenCSW package management on Solaris"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pkgutil_module.html
fetched_at: 2026-07-28T01:49:06+00:00
---
# community.general.pkgutil module – OpenCSW package management on Solaris

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
> To use it in a playbook, specify: `community.general.pkgutil`.

- [Synopsis](pkgutil_module.md#synopsis)
- [Parameters](pkgutil_module.md#parameters)
- [Attributes](pkgutil_module.md#attributes)
- [Examples](pkgutil_module.md#examples)

## [Synopsis](pkgutil_module.md#id1)

- This module installs, updates and removes packages from the OpenCSW project for Solaris.
- Unlike the [community.general.svr4pkg](svr4pkg_module.md#ansible-collections-community-general-svr4pkg-module) module, it will resolve and download dependencies.
- See <https://www.opencsw.org/> for more information about the project.

Aliases: packaging.os.pkgutil

## [Parameters](pkgutil_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean  *added in community.general 1.2.0* | To allow the update process to downgrade packages to match what is present in the repository, set this to `true`.  This is useful for rolling back to stable from testing, or similar operations.  **Choices:**   - `false` ← (default) - `true` |
| **name**  aliases: pkg  list / elements=string / required | The name of the package.  When using `state=latest`, this can be `'*'`, which updates all installed packages managed by pkgutil. |
| **site**  string | The repository path to install the package from.  Its global definition is in `/etc/opt/csw/pkgutil.conf`. |
| **state**  string / required | Whether to install (`present`/`installed`), or remove (`absent`/`removed`) packages.  The upgrade (`latest`) operation will update/install the packages to the latest version available.  **Choices:**   - `"absent"` - `"installed"` - `"latest"` - `"present"` - `"removed"` |
| **update_catalog**  boolean | If you always want to refresh your catalog from the mirror, even when it’s not stale, set this to `true`.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](pkgutil_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  In order to check the availability of packages, the catalog cache under `/var/opt/csw/pkgutil` may be refreshed even in check mode. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pkgutil_module.md#id4)

```yaml+jinja
- name: Install a package
  community.general.pkgutil:
    name: CSWcommon
    state: present

- name: Install a package from a specific repository
  community.general.pkgutil:
    name: CSWnrpe
    site: ftp://myinternal.repo/opencsw/kiel
    state: latest

- name: Remove a package
  community.general.pkgutil:
    name: CSWtop
    state: absent

- name: Install several packages
  community.general.pkgutil:
    name:
    - CSWsudo
    - CSWtop
    state: present

- name: Update all packages
  community.general.pkgutil:
    name: '*'
    state: latest

- name: Update all packages and force versions to match latest in catalog
  community.general.pkgutil:
    name: '*'
    state: latest
    force: true
```

### Authors

- Alexander Winkler (@dermute)
- David Ponessa (@scathatheworm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
