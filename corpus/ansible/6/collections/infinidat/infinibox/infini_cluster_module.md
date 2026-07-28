---
collection: ansible
version: "6"
title: "infinidat.infinibox.infini_cluster module – Create, Delete and Modify Host Cluster on Infinibox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infinidat/infinibox/infini_cluster_module.html
fetched_at: 2026-07-27T17:50:45+00:00
---
# infinidat.infinibox.infini_cluster module – Create, Delete and Modify Host Cluster on Infinibox

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
> see [Requirements](infini_cluster_module.md#ansible-collections-infinidat-infinibox-infini-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `infinidat.infinibox.infini_cluster`.

New in infinidat.infinibox 2.9.0

- [Synopsis](infini_cluster_module.md#synopsis)
- [Requirements](infini_cluster_module.md#requirements)
- [Parameters](infini_cluster_module.md#parameters)
- [Notes](infini_cluster_module.md#notes)
- [Examples](infini_cluster_module.md#examples)

## [Synopsis](infini_cluster_module.md#id1)

- This module creates, deletes or modifies host clusters on Infinibox.

## [Requirements](infini_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python2 >= 2.7 or python3 >= 3.6
- infinisdk (<https://infinisdk.readthedocs.io/en/latest/>)

## [Parameters](infini_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster_hosts**  list / elements=dictionary | A list of hosts to add to a cluster when state is present. |
| **name**  string / required | Cluster Name |
| **password**  string / required | Infinibox User password. |
| **state**  string | Creates/Modifies Cluster when present, removes when absent, or provides details of a cluster when stat.  Choices:   - `"stat"` - `"present"` ← (default) - `"absent"` |
| **system**  string / required | Infinibox Hostname or IPv4 Address. |
| **user**  string / required | Infinibox User username with sufficient priveledges ( see notes ). |

## [Notes](infini_cluster_module.md#id4)

> **Note:**
>
> - This module requires infinisdk python library
> - You must set INFINIBOX_USER and INFINIBOX_PASSWORD environment variables if user and password arguments are not passed to the module directly
> - Ansible uses the infinisdk configuration file `~/.infinidat/infinisdk.ini` if no credentials are provided. See <http://infinisdk.readthedocs.io/en/latest/getting_started.html>
> - All Infinidat modules support check mode (–check). However, a dryrun that creates resources may fail if the resource dependencies are not met for a task. For example, consider a task that creates a volume in a pool. If the pool does not exist, the volume creation task will fail. It will fail even if there was a previous task in the playbook that would have created the pool but did not because the pool creation was also part of the dry run.

## [Examples](infini_cluster_module.md#id5)

```yaml+jinja
- name: Create new cluster
  infini_cluster:
    name: foo_cluster
    user: admin
    password: secret
    system: ibox001
```

### Authors

- David Ohlemacher (@ohlemacher)

### Collection links

[Issue Tracker](https://www.github.com/infinidat/ansible-infinidat-collection/issues)
[Repository (Sources)](https://www.github.com/infinidat/ansible-infinidat-collection)
