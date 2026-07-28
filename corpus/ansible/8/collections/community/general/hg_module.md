---
collection: ansible
version: "8"
title: "community.general.hg module – Manages Mercurial (hg) repositories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hg_module.html
fetched_at: 2026-07-28T01:45:59+00:00
---
# community.general.hg module – Manages Mercurial (hg) repositories

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
> To use it in a playbook, specify: `community.general.hg`.

- [Synopsis](hg_module.md#synopsis)
- [Parameters](hg_module.md#parameters)
- [Attributes](hg_module.md#attributes)
- [Notes](hg_module.md#notes)
- [Examples](hg_module.md#examples)

## [Synopsis](hg_module.md#id1)

- Manages Mercurial (hg) repositories. Supports SSH, HTTP/S and local address.

Aliases: source_control.hg

## [Parameters](hg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clone**  boolean | If `false`, do not clone the repository if it does not exist locally.  **Choices:**   - `false` - `true` ← (default) |
| **dest**  path | Absolute path of where the repository should be cloned to. This parameter is required, unless clone and update are set to no |
| **executable**  string | Path to hg executable to use. If not supplied, the normal mechanism for resolving binary paths will be used. |
| **force**  boolean | Discards uncommitted changes. Runs `hg update -C`. Prior to Ansible 1.9, the default was `true`.  **Choices:**   - `false` ← (default) - `true` |
| **purge**  boolean | Deletes untracked files. Runs `hg purge`.  **Choices:**   - `false` ← (default) - `true` |
| **repo**  aliases: name  string / required | The repository address. |
| **revision**  aliases: version  string | Equivalent `-r` option in hg command which could be the changeset, revision number, branch name or even tag. |
| **update**  boolean | If `false`, do not retrieve new revisions from the origin repository  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](hg_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](hg_module.md#id4)

> **Note:**
>
> - This module does not support push capability. See <https://github.com/ansible/ansible/issues/31156>.
> - If the task seems to be hanging, first verify remote host is in `known_hosts`. SSH will prompt user to authorize the first contact with a remote host. To avoid this prompt, one solution is to add the remote host public key in `/etc/ssh/ssh_known_hosts` before calling the hg module, with the following command: ssh-keyscan remote_host.com >> /etc/ssh/ssh_known_hosts.
> - As per 01 Dec 2018, Bitbucket has dropped support for TLSv1 and TLSv1.1 connections. As such, if the underlying system still uses a Python version below 2.7.9, you will have issues checking out bitbucket repositories. See <https://bitbucket.org/blog/deprecating-tlsv1-tlsv1-1-2018-12-01>.

## [Examples](hg_module.md#id5)

```yaml+jinja
- name: Ensure the current working copy is inside the stable branch and deletes untracked files if any.
  community.general.hg:
    repo: https://bitbucket.org/user/repo1
    dest: /home/user/repo1
    revision: stable
    purge: true

- name: Get information about the repository whether or not it has already been cloned locally.
  community.general.hg:
    repo: git://bitbucket.org/user/repo
    dest: /srv/checkout
    clone: false
    update: false
```

### Authors

- Yeukhon Wong (@yeukhon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
