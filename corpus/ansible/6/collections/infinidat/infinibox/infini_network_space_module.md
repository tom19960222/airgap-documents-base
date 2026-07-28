---
collection: ansible
version: "6"
title: "infinidat.infinibox.infini_network_space module – Create, Delete and Modify network spaces on Infinibox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infinidat/infinibox/infini_network_space_module.html
fetched_at: 2026-07-27T17:50:49+00:00
---
# infinidat.infinibox.infini_network_space module – Create, Delete and Modify network spaces on Infinibox

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
> see [Requirements](infini_network_space_module.md#ansible-collections-infinidat-infinibox-infini-network-space-module-requirements) for details.
>
> To use it in a playbook, specify: `infinidat.infinibox.infini_network_space`.

New in infinidat.infinibox 2.12.0

- [Synopsis](infini_network_space_module.md#synopsis)
- [Requirements](infini_network_space_module.md#requirements)
- [Parameters](infini_network_space_module.md#parameters)
- [Notes](infini_network_space_module.md#notes)
- [Examples](infini_network_space_module.md#examples)

## [Synopsis](infini_network_space_module.md#id1)

- This module creates, deletes or modifies network spaces on Infinibox.

## [Requirements](infini_network_space_module.md#id2)

The below requirements are needed on the host that executes this module.

- python2 >= 2.7 or python3 >= 3.6
- infinisdk (<https://infinisdk.readthedocs.io/en/latest/>)

## [Parameters](infini_network_space_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **interfaces**  list / elements=string | A list of interfaces for the space. |
| **ips**  list / elements=string | List of IPs.  Default: `[]` |
| **mtu**  integer | Set an MTU. If not specified, defaults to 1500 bytes. |
| **name**  string / required | Network space name |
| **netmask**  integer | Network mask. |
| **network**  string | Starting IP address. |
| **password**  string / required | Infinibox User password. |
| **rate_limit**  integer | Specify the throughput limit per node.  The limit is specified in Mbps, megabits per second (not megabytes).  Note the limit affects NFS, iSCSI and async-replication traffic.  It does not affect sync-replication or active-active traffic. |
| **service**  string | Choose a service.  Choices:   - `"replication"` ← (default) - `"NAS"` - `"iSCSI"` |
| **state**  string | Creates/Modifies network spaces when present. Removes when absent. Shows status when stat.  Choices:   - `"stat"` - `"present"` ← (default) - `"absent"` |
| **system**  string / required | Infinibox Hostname or IPv4 Address. |
| **user**  string / required | Infinibox User username with sufficient priveledges ( see notes ). |

## [Notes](infini_network_space_module.md#id4)

> **Note:**
>
> - This module requires infinisdk python library
> - You must set INFINIBOX_USER and INFINIBOX_PASSWORD environment variables if user and password arguments are not passed to the module directly
> - Ansible uses the infinisdk configuration file `~/.infinidat/infinisdk.ini` if no credentials are provided. See <http://infinisdk.readthedocs.io/en/latest/getting_started.html>
> - All Infinidat modules support check mode (–check). However, a dryrun that creates resources may fail if the resource dependencies are not met for a task. For example, consider a task that creates a volume in a pool. If the pool does not exist, the volume creation task will fail. It will fail even if there was a previous task in the playbook that would have created the pool but did not because the pool creation was also part of the dry run.

## [Examples](infini_network_space_module.md#id5)

```yaml+jinja
- name: Create new network space
  infini_network_space:
    name: iSCSI
    state: present
    interfaces:
        - 1680
        - 1679
        - 1678
    service: ISCSI_SERVICE
    netmask: 19
    network: 172.31.32.0
    default_gateway: 172.31.63.254
    ips:
        - 172.31.32.145
        - 172.31.32.146
        - 172.31.32.147
        - 172.31.32.148
        - 172.31.32.149
        - 172.31.32.150
    user: admin
    password: secret
    system: ibox001
```

### Authors

- David Ohlemacher (@ohlemacher)

### Collection links

[Issue Tracker](https://www.github.com/infinidat/ansible-infinidat-collection/issues)
[Repository (Sources)](https://www.github.com/infinidat/ansible-infinidat-collection)
