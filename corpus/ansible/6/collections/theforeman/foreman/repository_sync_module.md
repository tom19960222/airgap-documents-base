---
collection: ansible
version: "6"
title: "theforeman.foreman.repository_sync module – Sync a Repository or Product"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/repository_sync_module.html
fetched_at: 2026-07-28T00:21:04+00:00
---
# theforeman.foreman.repository_sync module – Sync a Repository or Product

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](repository_sync_module.md#ansible-collections-theforeman-foreman-repository-sync-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.repository_sync`.

New in theforeman.foreman 1.0.0

- [Synopsis](repository_sync_module.md#synopsis)
- [Requirements](repository_sync_module.md#requirements)
- [Parameters](repository_sync_module.md#parameters)
- [Examples](repository_sync_module.md#examples)

## [Synopsis](repository_sync_module.md#id1)

- Sync a repository or product

## [Requirements](repository_sync_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](repository_sync_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **product**  string / required | Product to which the *repository* lives in |
| **repository**  string | Name of the repository to sync  If omitted, all repositories in *product* are synched. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](repository_sync_module.md#id4)

```yaml+jinja
- name: "Sync repository"
  theforeman.foreman.repository_sync:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    repository: "My repository"
    product: "My Product"
    organization: "Default Organization"
```

### Authors

- Eric D Helms (@ehelms)
- Matthias M Dellweg (@mdellweg) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
