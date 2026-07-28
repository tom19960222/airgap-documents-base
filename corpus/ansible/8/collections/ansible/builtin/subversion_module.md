---
collection: ansible
version: "8"
title: "ansible.builtin.subversion module – Deploys a subversion repository"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/subversion_module.html
fetched_at: 2026-07-28T01:07:44+00:00
---
# ansible.builtin.subversion module – Deploys a subversion repository

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `subversion` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.subversion` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](subversion_module.md#synopsis)
- [Requirements](subversion_module.md#requirements)
- [Parameters](subversion_module.md#parameters)
- [Attributes](subversion_module.md#attributes)
- [Notes](subversion_module.md#notes)
- [Examples](subversion_module.md#examples)

## [Synopsis](subversion_module.md#id1)

- Deploy given repository URL / revision to dest. If dest exists, update to the specified revision, otherwise perform a checkout.

## [Requirements](subversion_module.md#id2)

The below requirements are needed on the host that executes this module.

- subversion (the command line tool with `svn` entrypoint)

## [Parameters](subversion_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **checkout**  boolean | If `false`, do not check out the repository if it does not exist locally.  **Choices:**   - `false` - `true` ← (default) |
| **dest**  path | Absolute path where the repository should be deployed.  The destination directory must be specified unless *checkout=no*, *update=no*, and *export=no*. |
| **executable**  path | Path to svn executable to use. If not supplied, the normal mechanism for resolving binary paths will be used. |
| **export**  boolean | If `true`, do export instead of checkout/update.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | If `true`, modified files will be discarded. If `false`, module will fail if it encounters modified files. Prior to 1.9 the default was `true`.  **Choices:**   - `false` ← (default) - `true` |
| **in_place**  boolean | If the directory exists, then the working copy will be checked-out over-the-top using svn checkout –force; if force is specified then existing files with different content are reverted.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | `--password` parameter passed to svn when svn is less than version 1.10.0. This is not secure and the password will be leaked to argv.  `--password-from-stdin` parameter when svn is greater or equal to version 1.10.0. |
| **repo**  aliases: name, repository  string / required | The subversion URL to the repository. |
| **revision**  aliases: rev, version  string | Specific revision to checkout.  **Default:** `"HEAD"` |
| **switch**  boolean | If `false`, do not call svn switch before update.  **Choices:**   - `false` - `true` ← (default) |
| **update**  boolean | If `false`, do not retrieve new revisions from the origin repository.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | `--username` parameter passed to svn. |
| **validate_certs**  boolean  *added in ansible-core 2.11* | If `false`, passes the `--trust-server-cert` flag to svn.  If `true`, does not pass the flag.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](subversion_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](subversion_module.md#id5)

> **Note:**
>
> - This module does not handle externals.

## [Examples](subversion_module.md#id6)

```yaml+jinja
- name: Checkout subversion repository to specified folder
  ansible.builtin.subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/checkout

- name: Export subversion directory to folder
  ansible.builtin.subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/export
    export: yes

- name: Get information about the repository whether or not it has already been cloned locally
  ansible.builtin.subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/checkout
    checkout: no
    update: no
```

### Authors

- Dane Summers (@dsummersl)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
