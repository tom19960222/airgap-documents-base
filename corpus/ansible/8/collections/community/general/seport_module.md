---
collection: ansible
version: "8"
title: "community.general.seport module – Manages SELinux network port type definitions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/seport_module.html
fetched_at: 2026-07-28T01:50:34+00:00
---
# community.general.seport module – Manages SELinux network port type definitions

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
> see [Requirements](seport_module.md#ansible-collections-community-general-seport-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.seport`.

- [Synopsis](seport_module.md#synopsis)
- [Requirements](seport_module.md#requirements)
- [Parameters](seport_module.md#parameters)
- [Attributes](seport_module.md#attributes)
- [Notes](seport_module.md#notes)
- [Examples](seport_module.md#examples)

## [Synopsis](seport_module.md#id1)

- Manages SELinux network port type definitions.

Aliases: system.seport

## [Requirements](seport_module.md#id2)

The below requirements are needed on the host that executes this module.

- libselinux-python
- policycoreutils-python

## [Parameters](seport_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ignore_selinux_state**  boolean | Run independent of selinux runtime state  **Choices:**   - `false` ← (default) - `true` |
| **local**  boolean  *added in community.general 5.6.0* | Work with local modifications only.  **Choices:**   - `false` ← (default) - `true` |
| **ports**  list / elements=string / required | Ports or port ranges.  Can be a list (since 2.6) or comma separated string. |
| **proto**  string / required | Protocol for the specified port.  **Choices:**   - `"tcp"` - `"udp"` |
| **reload**  boolean | Reload SELinux policy after commit.  **Choices:**   - `false` - `true` ← (default) |
| **setype**  string / required | SELinux type for the specified port. |
| **state**  string | Desired boolean value.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](seport_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](seport_module.md#id5)

> **Note:**
>
> - The changes are persistent across reboots.
> - Not tested on any debian based system.

## [Examples](seport_module.md#id6)

```yaml+jinja
- name: Allow Apache to listen on tcp port 8888
  community.general.seport:
    ports: 8888
    proto: tcp
    setype: http_port_t
    state: present

- name: Allow sshd to listen on tcp port 8991
  community.general.seport:
    ports: 8991
    proto: tcp
    setype: ssh_port_t
    state: present

- name: Allow memcached to listen on tcp ports 10000-10100 and 10112
  community.general.seport:
    ports: 10000-10100,10112
    proto: tcp
    setype: memcache_port_t
    state: present

- name: Allow memcached to listen on tcp ports 10000-10100 and 10112
  community.general.seport:
    ports:
      - 10000-10100
      - 10112
    proto: tcp
    setype: memcache_port_t
    state: present

- name: Remove tcp port 22 local modification if exists
  community.general.seport:
    ports: 22
    protocol: tcp
    setype: ssh_port_t
    state: absent
    local: true
```

### Authors

- Dan Keder (@dankeder)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
