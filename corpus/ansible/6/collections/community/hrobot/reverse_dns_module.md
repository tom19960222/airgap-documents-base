---
collection: ansible
version: "6"
title: "community.hrobot.reverse_dns module – Set or remove reverse DNS entry for IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/reverse_dns_module.html
fetched_at: 2026-07-27T17:15:54+00:00
---
# community.hrobot.reverse_dns module – Set or remove reverse DNS entry for IP

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/community/hrobot) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.reverse_dns`.

New in community.hrobot 1.2.0

- [Synopsis](reverse_dns_module.md#synopsis)
- [Parameters](reverse_dns_module.md#parameters)
- [Attributes](reverse_dns_module.md#attributes)
- [Notes](reverse_dns_module.md#notes)
- [Examples](reverse_dns_module.md#examples)

## [Synopsis](reverse_dns_module.md#id1)

- Allows to set, update or remove a reverse DNS entry for an IP address.

## [Parameters](reverse_dns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **ip**  string / required | The IP address to set or remove a reverse DNS entry for. |
| **state**  string | Whether to set or update (`present`) or delete (`absent`) the reverse DNS entry for *ip*.  Choices:   - `"present"` ← (default) - `"absent"` |
| **value**  string | The reverse DNS entry for *ip*.  Required if *state=present*. |

## [Attributes](reverse_dns_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](reverse_dns_module.md#id4)

> **Note:**
>
> - For the main IPv4 address of a server, deleting it actually sets it to a default hostname like `static.X.Y.Z.W.clients.your-server.de`. This substitution (delete is replaced by changing to this value) is done automatically by the API and results in the module not being idempotent in this case.

## [Examples](reverse_dns_module.md#id5)

```yaml+jinja
- name: Set reverse DNS entry for 1.2.3.4
  community.hrobot.reverse_dns:
    hetzner_user: foo
    hetzner_password: bar
    ip: 1.2.3.4
    value: foo.example.com

- name: Remove reverse DNS entry for 2a01:f48:111:4221::1
  community.hrobot.reverse_dns:
    hetzner_user: foo
    hetzner_password: bar
    ip: 2a01:f48:111:4221::1
    state: absent
```

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
