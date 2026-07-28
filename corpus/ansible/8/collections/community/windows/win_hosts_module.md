---
collection: ansible
version: "8"
title: "community.windows.win_hosts module – Manages hosts file entries on Windows."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_hosts_module.html
fetched_at: 2026-07-28T02:01:57+00:00
---
# community.windows.win_hosts module – Manages hosts file entries on Windows.

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_hosts`.

- [Synopsis](win_hosts_module.md#synopsis)
- [Parameters](win_hosts_module.md#parameters)
- [Notes](win_hosts_module.md#notes)
- [See Also](win_hosts_module.md#see-also)
- [Examples](win_hosts_module.md#examples)

## [Synopsis](win_hosts_module.md#id1)

- Manages hosts file entries on Windows.
- Maps IPv4 or IPv6 addresses to canonical names.
- Adds, removes, or sets cname records for ip and hostname pairs.
- Modifies %windir%\\system32\\drivers\\etc\\hosts.

## [Parameters](win_hosts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Controls the behavior of *aliases*.  Only applicable when `state=present`.  If `add`, each alias in *aliases* will be added to the host entry.  If `set`, each alias in *aliases* will be added to the host entry, and other aliases will be removed from the entry.  **Choices:**   - `"add"` - `"remove"` - `"set"` ← (default) |
| **aliases**  list / elements=string | A list of additional names (cname records) for the host entry.  Only applicable when `state=present`. |
| **canonical_name**  string | A canonical name for the host entry.  required for `state=present`. |
| **ip_address**  string | The ip address for the host entry.  Can be either IPv4 (A record) or IPv6 (AAAA record).  Required for `state=present`. |
| **state**  string | Whether the entry should be present or absent.  If only *canonical_name* is provided when `state=absent`, then all hosts entries with the canonical name of *canonical_name* will be removed.  If only *ip_address* is provided when `state=absent`, then all hosts entries with the ip address of *ip_address* will be removed.  If *ip_address* and *canonical_name* are both omitted when `state=absent`, then all hosts entries will be removed.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](win_hosts_module.md#id3)

> **Note:**
>
> - Each canonical name can only be mapped to one IPv4 and one IPv6 address. If *canonical_name* is provided with `state=present` and is found to be mapped to another IP address that is the same type as, but unique from *ip_address*, then *canonical_name* and all *aliases* will be removed from the entry and added to an entry with the provided IP address.
> - Each alias can only be mapped to one canonical name. If *aliases* is provided with `state=present` and an alias is found to be mapped to another canonical name, then the alias will be removed from the entry and either added to or removed from (depending on *action*) an entry with the provided canonical name.

## [See Also](win_hosts_module.md#id4)

> **See also:**
>
> [ansible.windows.win_template](../../ansible/windows/win_template_module.md#ansible-collections-ansible-windows-win-template-module)
> :   Template a file out to a remote server.
>
> [ansible.windows.win_file](../../ansible/windows/win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.
>
> [ansible.windows.win_copy](../../ansible/windows/win_copy_module.md#ansible-collections-ansible-windows-win-copy-module)
> :   Copies files to remote locations on windows hosts.

## [Examples](win_hosts_module.md#id5)

```yaml+jinja
- name: Add 127.0.0.1 as an A record for localhost
  community.windows.win_hosts:
    state: present
    canonical_name: localhost
    ip_address: 127.0.0.1

- name: Add ::1 as an AAAA record for localhost
  community.windows.win_hosts:
    state: present
    canonical_name: localhost
    ip_address: '::1'

- name: Remove 'bar' and 'zed' from the list of aliases for foo (192.168.1.100)
  community.windows.win_hosts:
    state: present
    canonical_name: foo
    ip_address: 192.168.1.100
    action: remove
    aliases:
      - bar
      - zed

- name: Remove hosts entries with canonical name 'bar'
  community.windows.win_hosts:
    state: absent
    canonical_name: bar

- name: Remove 10.2.0.1 from the list of hosts
  community.windows.win_hosts:
    state: absent
    ip_address: 10.2.0.1

- name: Ensure all name resolution is handled by DNS
  community.windows.win_hosts:
    state: absent
```

### Authors

- Micah Hunsberger (@mhunsber)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
