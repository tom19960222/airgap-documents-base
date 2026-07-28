---
collection: ansible
version: "8"
title: "community.general.linode module – Manage instances on the Linode Public Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/linode_module.html
fetched_at: 2026-07-28T01:47:31+00:00
---
# community.general.linode module – Manage instances on the Linode Public Cloud

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
> see [Requirements](linode_module.md#ansible-collections-community-general-linode-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.linode`.

- [Synopsis](linode_module.md#synopsis)
- [Requirements](linode_module.md#requirements)
- [Parameters](linode_module.md#parameters)
- [Attributes](linode_module.md#attributes)
- [Notes](linode_module.md#notes)
- [Examples](linode_module.md#examples)

## [Synopsis](linode_module.md#id1)

- Manage Linode Public Cloud instances and optionally wait for it to be ‘running’.

Aliases: cloud.linode.linode

## [Requirements](linode_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- linode-python

## [Parameters](linode_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additional_disks**  list / elements=dictionary | List of dictionaries for creating additional disks that are added to the Linode configuration settings.  Dictionary takes Size, Label, Type. Size is in MB. |
| **alert_bwin_enabled**  boolean | Set status of bandwidth in alerts.  **Choices:**   - `false` - `true` |
| **alert_bwin_threshold**  integer | Set threshold in MB of bandwidth in alerts. |
| **alert_bwout_enabled**  boolean | Set status of bandwidth out alerts.  **Choices:**   - `false` - `true` |
| **alert_bwout_threshold**  integer | Set threshold in MB of bandwidth out alerts. |
| **alert_bwquota_enabled**  boolean | Set status of bandwidth quota alerts as percentage of network transfer quota.  **Choices:**   - `false` - `true` |
| **alert_bwquota_threshold**  integer | Set threshold in MB of bandwidth quota alerts. |
| **alert_cpu_enabled**  boolean | Set status of receiving CPU usage alerts.  **Choices:**   - `false` - `true` |
| **alert_cpu_threshold**  integer | Set percentage threshold for receiving CPU usage alerts. Each CPU core adds 100% to total. |
| **alert_diskio_enabled**  boolean | Set status of receiving disk IO alerts.  **Choices:**   - `false` - `true` |
| **alert_diskio_threshold**  integer | Set threshold for average IO ops/sec over 2 hour period. |
| **api_key**  string / required | Linode API key.  `LINODE_API_KEY` environment variable can be used instead. |
| **backupweeklyday**  integer | Day of the week to take backups. |
| **backupwindow**  integer | The time window in which backups will be taken. |
| **datacenter**  integer | datacenter to create an instance in (Linode Datacenter) |
| **displaygroup**  string | Add the instance to a Display Group in Linode Manager.  **Default:** `""` |
| **distribution**  integer | distribution to use for the instance (Linode Distribution) |
| **kernel_id**  integer | kernel to use for the instance (Linode Kernel) |
| **linode_id**  aliases: lid  integer | Unique ID of a linode server. This value is read-only in the sense that if you specify it on creation of a Linode it will not be used. The Linode API generates these IDs and we can those generated value here to reference a Linode more specifically. This is useful for idempotence. |
| **name**  string / required | Name to give the instance (alphanumeric, dashes, underscore).  To keep sanity on the Linode Web Console, name is prepended with `LinodeID-`. |
| **password**  string | root password to apply to a new server (auto generated if missing) |
| **payment_term**  integer | payment term to use for the instance (payment term in months)  **Choices:**   - `1` ← (default) - `12` - `24` |
| **plan**  integer | plan to use for the instance (Linode plan) |
| **private_ip**  boolean | Add private IPv4 address when Linode is created.  Default is `false`.  **Choices:**   - `false` - `true` |
| **ssh_pub_key**  string | SSH public key applied to root user |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"absent"` - `"active"` - `"deleted"` - `"present"` ← (default) - `"restarted"` - `"started"` - `"stopped"` |
| **swap**  integer | swap size in MB  **Default:** `512` |
| **wait**  boolean | wait for the instance to be in state `running` before returning  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `300` |
| **watchdog**  boolean | Set status of Lassie watchdog.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](linode_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](linode_module.md#id5)

> **Note:**
>
> - Please note, linode-python does not have python 3 support.
> - This module uses the now deprecated v3 of the Linode API.
> - Please review <https://www.linode.com/api/linode> for determining the required parameters.

## [Examples](linode_module.md#id6)

```yaml+jinja
- name: Create a new Linode
  community.general.linode:
    name: linode-test1
    plan: 1
    datacenter: 7
    distribution: 129
    state: present
  register: linode_creation

- name: Create a server with a private IP Address
  community.general.linode:
     module: linode
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     plan: 1
     datacenter: 2
     distribution: 99
     password: 'superSecureRootPassword'
     private_ip: true
     ssh_pub_key: 'ssh-rsa qwerty'
     swap: 768
     wait: true
     wait_timeout: 600
     state: present
  delegate_to: localhost
  register: linode_creation

- name: Fully configure new server
  community.general.linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     plan: 4
     datacenter: 2
     distribution: 99
     kernel_id: 138
     password: 'superSecureRootPassword'
     private_ip: true
     ssh_pub_key: 'ssh-rsa qwerty'
     swap: 768
     wait: true
     wait_timeout: 600
     state: present
     alert_bwquota_enabled: true
     alert_bwquota_threshold: 80
     alert_bwin_enabled: true
     alert_bwin_threshold: 10
     alert_cpu_enabled: true
     alert_cpu_threshold: 210
     alert_bwout_enabled: true
     alert_bwout_threshold: 10
     alert_diskio_enabled: true
     alert_diskio_threshold: 10000
     backupweeklyday: 1
     backupwindow: 2
     displaygroup: 'test'
     additional_disks:
      - {Label: 'disk1', Size: 2500, Type: 'raw'}
      - {Label: 'newdisk', Size: 2000}
     watchdog: true
  delegate_to: localhost
  register: linode_creation

- name: Ensure a running server (create if missing)
  community.general.linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     plan: 1
     datacenter: 2
     distribution: 99
     password: 'superSecureRootPassword'
     ssh_pub_key: 'ssh-rsa qwerty'
     swap: 768
     wait: true
     wait_timeout: 600
     state: present
  delegate_to: localhost
  register: linode_creation

- name: Delete a server
  community.general.linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     linode_id: "{{ linode_creation.instance.id }}"
     state: absent
  delegate_to: localhost

- name: Stop a server
  community.general.linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     linode_id: "{{ linode_creation.instance.id }}"
     state: stopped
  delegate_to: localhost

- name: Reboot a server
  community.general.linode:
     api_key: 'longStringFromLinodeApi'
     name: linode-test1
     linode_id: "{{ linode_creation.instance.id }}"
     state: restarted
  delegate_to: localhost
```

### Authors

- Vincent Viallet (@zbal)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
