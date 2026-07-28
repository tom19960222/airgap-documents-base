---
collection: ansible
version: "6"
title: "infinidat.infinibox.infini_export_client module – Create, Delete or Modify NFS Client(s) for existing exports on Infinibox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infinidat/infinibox/infini_export_client_module.html
fetched_at: 2026-07-27T17:50:46+00:00
---
# infinidat.infinibox.infini_export_client module – Create, Delete or Modify NFS Client(s) for existing exports on Infinibox

> **Note:**
>
> This module is part of the [infinidat.infinibox collection](https://galaxy.ansible.com/infinidat/infinibox) (version 1.3.12).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infinidat.infinibox`.
> You need further requirements to be able to use this module,
> see [Requirements](infini_export_client_module.md#ansible-collections-infinidat-infinibox-infini-export-client-module-requirements) for details.
>
> To use it in a playbook, specify: `infinidat.infinibox.infini_export_client`.

New in infinidat.infinibox 2.3.0

- [Synopsis](infini_export_client_module.md#synopsis)
- [Requirements](infini_export_client_module.md#requirements)
- [Parameters](infini_export_client_module.md#parameters)
- [Notes](infini_export_client_module.md#notes)
- [Examples](infini_export_client_module.md#examples)

## [Synopsis](infini_export_client_module.md#id1)

- This module creates, deletes or modifys NFS client(s) for existing exports on Infinibox.

## [Requirements](infini_export_client_module.md#id2)

The below requirements are needed on the host that executes this module.

- infinisdk (<https://infinisdk.readthedocs.io/en/latest/>)
- munch
- python2 >= 2.7 or python3 >= 3.6

## [Parameters](infini_export_client_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_mode**  string | Read Write or Read Only Access.  Choices:   - `"RW"` ← (default) - `"RO"` |
| **client**  string / required | Client IP or Range. Ranges can be defined as follows 192.168.0.1-192.168.0.254. |
| **export**  string / required | Name of the export. |
| **no_root_squash**  boolean | Don’t squash root user to anonymous. Will be set to “no” on creation if not specified explicitly.  Choices:   - `false` ← (default) - `true` |
| **password**  string / required | Infinibox User password. |
| **state**  string | Creates/Modifies client when present and removes when absent.  Choices:   - `"stat"` - `"present"` ← (default) - `"absent"` |
| **system**  string / required | Infinibox Hostname or IPv4 Address. |
| **user**  string / required | Infinibox User username with sufficient priveledges ( see notes ). |

## [Notes](infini_export_client_module.md#id4)

> **Note:**
>
> - This module requires infinisdk python library
> - You must set INFINIBOX_USER and INFINIBOX_PASSWORD environment variables if user and password arguments are not passed to the module directly
> - Ansible uses the infinisdk configuration file `~/.infinidat/infinisdk.ini` if no credentials are provided. See <http://infinisdk.readthedocs.io/en/latest/getting_started.html>
> - All Infinidat modules support check mode (–check). However, a dryrun that creates resources may fail if the resource dependencies are not met for a task. For example, consider a task that creates a volume in a pool. If the pool does not exist, the volume creation task will fail. It will fail even if there was a previous task in the playbook that would have created the pool but did not because the pool creation was also part of the dry run.

## [Examples](infini_export_client_module.md#id5)

```yaml+jinja
- name: Make sure nfs client 10.0.0.1 is configured for export. Allow root access
  infini_export_client:
    client: 10.0.0.1
    access_mode: RW
    no_root_squash: yes
    export: /data
    state: present  # Default
    user: admin
    password: secret
    system: ibox001

- name: Add multiple clients with RO access. Squash root privileges
  infini_export_client:
    client: "{{ item }}"
    access_mode: RO
    no_root_squash: no
    export: /data
    user: admin
    password: secret
    system: ibox001
  with_items:
    - 10.0.0.2
    - 10.0.0.3
```

### Authors

- David Ohlemacher (@ohlemacher)

### Collection links

[Issue Tracker](https://www.github.com/infinidat/ansible-infinidat-collection/issues)
[Repository (Sources)](https://www.github.com/infinidat/ansible-infinidat-collection)
