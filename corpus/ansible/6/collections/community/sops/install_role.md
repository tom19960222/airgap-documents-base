---
collection: ansible
version: "6"
title: "community.sops.install role – Install Mozilla sops"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sops/install_role.html
fetched_at: 2026-07-27T17:21:14+00:00
---
# community.sops.install role – Install Mozilla sops

> **Note:**
>
> This role is part of the [community.sops collection](https://galaxy.ansible.com/community/sops) (version 1.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install community.sops`.
>
> To use it in a playbook, specify: `community.sops.install`.

- [Entry point `main` – Install Mozilla sops](install_role.md#entry-point-main-install-mozilla-sops)

  - [Synopsis](install_role.md#synopsis)
  - [Parameters](install_role.md#parameters)
  - [Authors](install_role.md#authors)

## [Entry point `main` – Install Mozilla sops](install_role.md#id1)

New in community.sops 1.5.0

### [Synopsis](install_role.md#id2)

- This role installs [Mozilla sops](https://github.com/mozilla/sops) and Gnu Privacy Guard (GPG).
- This role supports the following operating systems: Alpine (new enough), Arch Linux, CentOS 7, Stream 8, or newer, Debian 10 (Buster) or newer, Fedora (new enough), RHEL 7 or newer, Ubuntu 16.04 or newer LTS versions
- The Ansible facts `ansible_facts.architecture`, `ansible_facts.distribution`, `ansible_facts.distribution_major_version`, `ansible_facts.distribution_version`, and `ansible_facts.os_family` are expected to be present if *sops_install_on_localhost* is `false`.

### [Parameters](install_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **sops_become_on_install**  boolean | Whether the role should use `become: true` when installing packages.  Choices:   - `false` - `true` ← (default) |
| **sops_install_on_localhost**  boolean | Installs sops on the Ansible controller (`localhost`) instead of the remote host.  Choices:   - `false` ← (default) - `true` |
| **sops_source**  string | Determines the source from where sops is installed.  The value `github` will install sops from the Mozilla sops releases on GitHub (<https://github.com/mozilla/sops/releases/>).  The value `system` will install sops from the system packages. Note that not all system package repositories support sops.  The value `auto` will determine the best source to install sops from. Here, system package repositories are preferred over GitHub.  Choices:   - `"auto"` ← (default) - `"github"` - `"system"` |
| **sops_version**  string | The version of sops to install.  Should be a version like `3.7.2`. The special value `latest` will select the latest version available form the given source.  Default: `"latest"` |

### [Authors](install_role.md#id4)

- Felix Fontein (@felixfontein)

#### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.sops)
[Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-sops)
