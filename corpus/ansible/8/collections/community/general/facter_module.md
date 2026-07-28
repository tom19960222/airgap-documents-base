---
collection: ansible
version: "8"
title: "community.general.facter module – Runs the discovery program facter on the remote system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/facter_module.html
fetched_at: 2026-07-28T01:45:31+00:00
---
# community.general.facter module – Runs the discovery program `facter` on the remote system

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
> see [Requirements](facter_module.md#ansible-collections-community-general-facter-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.facter`.

- [Synopsis](facter_module.md#synopsis)
- [Requirements](facter_module.md#requirements)
- [Parameters](facter_module.md#parameters)
- [Attributes](facter_module.md#attributes)
- [Examples](facter_module.md#examples)

## [Synopsis](facter_module.md#id1)

- Runs the `facter` discovery program (<https://github.com/puppetlabs/facter>) on the remote system, returning JSON data that can be useful for inventory purposes.

Aliases: system.facter

## [Requirements](facter_module.md#id2)

The below requirements are needed on the host that executes this module.

- facter
- ruby-json

## [Parameters](facter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arguments**  list / elements=string | Specifies arguments for facter. |

## [Attributes](facter_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](facter_module.md#id5)

```yaml+jinja
# Example command-line invocation
# ansible www.example.net -m facter

- name: Execute facter no arguments
  community.general.facter:

- name: Execute facter with arguments
  community.general.facter:
    arguments:
        - -p
        - system_uptime
        - timezone
        - is_virtual
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
