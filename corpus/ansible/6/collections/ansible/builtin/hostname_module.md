---
collection: ansible
version: "6"
title: "ansible.builtin.hostname module – Manage hostname"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/hostname_module.html
fetched_at: 2026-07-27T16:44:03+00:00
---
# ansible.builtin.hostname module – Manage hostname

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `hostname` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](hostname_module.md#synopsis)
- [Requirements](hostname_module.md#requirements)
- [Parameters](hostname_module.md#parameters)
- [Attributes](hostname_module.md#attributes)
- [Notes](hostname_module.md#notes)
- [Examples](hostname_module.md#examples)

## [Synopsis](hostname_module.md#id1)

- Set system’s hostname. Supports most OSs/Distributions including those using `systemd`.
- Windows, HP-UX, and AIX are not currently supported.

## [Requirements](hostname_module.md#id2)

The below requirements are needed on the host that executes this module.

- hostname

## [Parameters](hostname_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the host.  If the value is a fully qualified domain name that does not resolve from the given host, this will cause the module to hang for a few seconds while waiting for the name resolution attempt to timeout. |
| **use**  string  added in Ansible 2.9 | Which strategy to use to update the hostname.  If not set we try to autodetect, but this can be problematic, particularly with containers as they can present misleading information.  Note that ‘systemd’ should be specified for RHEL/EL/CentOS 7+. Older distributions should use ‘redhat’.  Choices:   - `"alpine"` - `"debian"` - `"freebsd"` - `"generic"` - `"macos"` - `"macosx"` - `"darwin"` - `"openbsd"` - `"openrc"` - `"redhat"` - `"sles"` - `"solaris"` - `"systemd"` |

## [Attributes](hostname_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Notes](hostname_module.md#id5)

> **Note:**
>
> - This module does **NOT** modify `/etc/hosts`. You need to modify it yourself using other modules such as [ansible.builtin.template](template_module.md#ansible-collections-ansible-builtin-template-module) or [ansible.builtin.replace](replace_module.md#ansible-collections-ansible-builtin-replace-module).
> - On macOS, this module uses `scutil` to set `HostName`, `ComputerName`, and `LocalHostName`. Since `LocalHostName` cannot contain spaces or most special characters, this module will replace characters when setting `LocalHostName`.

## [Examples](hostname_module.md#id6)

```yaml+jinja
- name: Set a hostname
  ansible.builtin.hostname:
    name: web01

- name: Set a hostname specifying strategy
  ansible.builtin.hostname:
    name: web01
    use: systemd
```

### Authors

- Adrian Likins (@alikins)
- Hideki Saito (@saito-hideki)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
