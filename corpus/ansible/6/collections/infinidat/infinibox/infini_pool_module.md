---
collection: ansible
version: "6"
title: "infinidat.infinibox.infini_pool module – Create, Delete and Modify Pools on Infinibox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infinidat/infinibox/infini_pool_module.html
fetched_at: 2026-07-27T17:50:49+00:00
---
# infinidat.infinibox.infini_pool module – Create, Delete and Modify Pools on Infinibox

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
> see [Requirements](infini_pool_module.md#ansible-collections-infinidat-infinibox-infini-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `infinidat.infinibox.infini_pool`.

New in infinidat.infinibox 2.3.0

- [Synopsis](infini_pool_module.md#synopsis)
- [Requirements](infini_pool_module.md#requirements)
- [Parameters](infini_pool_module.md#parameters)
- [Notes](infini_pool_module.md#notes)
- [Examples](infini_pool_module.md#examples)

## [Synopsis](infini_pool_module.md#id1)

- This module to creates, deletes or modifies pools on Infinibox.

## [Requirements](infini_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- capacity
- infinisdk (<https://infinisdk.readthedocs.io/en/latest/>)
- python2 >= 2.7 or python3 >= 3.6

## [Parameters](infini_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compression**  boolean | Enable/Disable Compression on Pool  Choices:   - `false` - `true` ← (default) |
| **name**  string / required | Pool Name |
| **password**  string / required | Infinibox User password. |
| **size**  string | Pool Physical Capacity in MB, GB or TB units. If pool size is not set on pool creation, size will be equal to 1TB. See examples. |
| **ssd_cache**  boolean | Enable/Disable SSD Cache on Pool  Choices:   - `false` - `true` ← (default) |
| **state**  string | Creates/Modifies Pool when present or removes when absent  Choices:   - `"stat"` - `"present"` ← (default) - `"absent"` |
| **system**  string / required | Infinibox Hostname or IPv4 Address. |
| **user**  string / required | Infinibox User username with sufficient priveledges ( see notes ). |
| **vsize**  string | Pool Virtual Capacity in MB, GB or TB units. If pool vsize is not set on pool creation, Virtual Capacity will be equal to Physical Capacity. See examples. |

## [Notes](infini_pool_module.md#id4)

> **Note:**
>
> - Infinibox Admin level access is required for pool modifications
> - This module requires infinisdk python library
> - You must set INFINIBOX_USER and INFINIBOX_PASSWORD environment variables if user and password arguments are not passed to the module directly
> - Ansible uses the infinisdk configuration file `~/.infinidat/infinisdk.ini` if no credentials are provided. See <http://infinisdk.readthedocs.io/en/latest/getting_started.html>
> - All Infinidat modules support check mode (–check). However, a dryrun that creates resources may fail if the resource dependencies are not met for a task. For example, consider a task that creates a volume in a pool. If the pool does not exist, the volume creation task will fail. It will fail even if there was a previous task in the playbook that would have created the pool but did not because the pool creation was also part of the dry run.

## [Examples](infini_pool_module.md#id5)

```yaml+jinja
- name: Make sure pool foo exists. Set pool physical capacity to 10TB
  infini_pool:
    name: foo
    size: 10TB
    vsize: 10TB
    user: admin
    password: secret
    system: ibox001

- name: Disable SSD Cache on pool
  infini_pool:
    name: foo
    ssd_cache: no
    user: admin
    password: secret
    system: ibox001

- name: Disable Compression on pool
  infini_pool:
    name: foo
    compression: no
    user: admin
    password: secret
    system: ibox001
```

### Authors

- David Ohlemacher (@ohlemacher)

### Collection links

[Issue Tracker](https://www.github.com/infinidat/ansible-infinidat-collection/issues)
[Repository (Sources)](https://www.github.com/infinidat/ansible-infinidat-collection)
