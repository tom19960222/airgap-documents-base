---
collection: ansible
version: "6"
title: "community.general.sl_vm module – Create or cancel a virtual instance in SoftLayer"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sl_vm_module.html
fetched_at: 2026-07-27T17:13:14+00:00
---
# community.general.sl_vm module – Create or cancel a virtual instance in SoftLayer

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](sl_vm_module.md#ansible-collections-community-general-sl-vm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.sl_vm`.

- [Synopsis](sl_vm_module.md#synopsis)
- [Requirements](sl_vm_module.md#requirements)
- [Parameters](sl_vm_module.md#parameters)
- [Examples](sl_vm_module.md#examples)

## [Synopsis](sl_vm_module.md#id1)

- Creates or cancels SoftLayer instances.
- When created, optionally waits for it to be ‘running’.

## [Requirements](sl_vm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- softlayer >= 4.1.1

## [Parameters](sl_vm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cpus**  integer | Count of cpus to be assigned to new virtual instance.  Choices:   - `1` - `2` - `4` - `8` - `16` - `32` - `56` |
| **datacenter**  string | Datacenter for the virtual instance to be deployed.  Choices:   - `"ams01"` - `"ams03"` - `"che01"` - `"dal01"` - `"dal05"` - `"dal06"` - `"dal09"` - `"dal10"` - `"dal12"` - `"dal13"` - `"fra02"` - `"fra04"` - `"fra05"` - `"hkg02"` - `"hou02"` - `"lon02"` - `"lon04"` - `"lon06"` - `"mel01"` - `"mex01"` - `"mil01"` - `"mon01"` - `"osl01"` - `"par01"` - `"sao01"` - `"sea01"` - `"seo01"` - `"sjc01"` - `"sjc03"` - `"sjc04"` - `"sng01"` - `"syd01"` - `"syd04"` - `"tok02"` - `"tor01"` - `"wdc01"` - `"wdc04"` - `"wdc06"` - `"wdc07"` |
| **dedicated**  boolean | Flag to determine if the instance should be deployed in dedicated space.  Choices:   - `false` ← (default) - `true` |
| **disks**  list / elements=integer | List of disk sizes to be assigned to new virtual instance.  Default: `[25]` |
| **domain**  string | Domain name to be provided to a virtual instance. |
| **flavor**  string  added in community.general 0.2.0 | Specify which SoftLayer flavor template to use instead of cpus and memory. |
| **hostname**  string | Hostname to be provided to a virtual instance. |
| **hourly**  boolean | Flag to determine if the instance should be hourly billed.  Choices:   - `false` - `true` ← (default) |
| **image_id**  string | Image Template to be used for new virtual instance. |
| **instance_id**  string | Instance Id of the virtual instance to perform action option. |
| **local_disk**  boolean | Flag to determine if local disk should be used for the new instance.  Choices:   - `false` - `true` ← (default) |
| **memory**  integer | Amount of memory to be assigned to new virtual instance.  Choices:   - `1024` - `2048` - `4096` - `6144` - `8192` - `12288` - `16384` - `32768` - `49152` - `65536` - `131072` - `247808` |
| **nic_speed**  integer | NIC Speed to be assigned to new virtual instance.  Choices:   - `10` - `100` - `1000` |
| **os_code**  string | OS Code to be used for new virtual instance. |
| **post_uri**  string | URL of a post provisioning script to be loaded and executed on virtual instance. |
| **private**  boolean | Flag to determine if the instance should be private only.  Choices:   - `false` ← (default) - `true` |
| **private_vlan**  string | VLAN by its Id to be assigned to the private NIC. |
| **public_vlan**  string | VLAN by its Id to be assigned to the public NIC. |
| **ssh_keys**  list / elements=string | List of ssh keys by their Id to be assigned to a virtual instance.  Default: `[]` |
| **state**  string | Create, or cancel a virtual instance.  Specify `present` for create, `absent` to cancel.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tags**  string | Tag or list of tags to be provided to a virtual instance. |
| **wait**  boolean | Flag used to wait for active status before returning.  Choices:   - `false` - `true` ← (default) |
| **wait_time**  integer | Time in seconds before wait returns.  Default: `600` |

## [Examples](sl_vm_module.md#id4)

```yaml+jinja
- name: Build instance
  hosts: localhost
  gather_facts: false
  tasks:
  - name: Build instance request
    community.general.sl_vm:
      hostname: instance-1
      domain: anydomain.com
      datacenter: dal09
      tags: ansible-module-test
      hourly: true
      private: false
      dedicated: false
      local_disk: true
      cpus: 1
      memory: 1024
      disks: [25]
      os_code: UBUNTU_LATEST
      wait: false

- name: Build additional instances
  hosts: localhost
  gather_facts: false
  tasks:
  - name: Build instances request
    community.general.sl_vm:
      hostname: "{{ item.hostname }}"
      domain: "{{ item.domain }}"
      datacenter: "{{ item.datacenter }}"
      tags: "{{ item.tags }}"
      hourly: "{{ item.hourly }}"
      private: "{{ item.private }}"
      dedicated: "{{ item.dedicated }}"
      local_disk: "{{ item.local_disk }}"
      cpus: "{{ item.cpus }}"
      memory: "{{ item.memory }}"
      disks: "{{ item.disks }}"
      os_code: "{{ item.os_code }}"
      ssh_keys: "{{ item.ssh_keys }}"
      wait: "{{ item.wait }}"
    with_items:
      - hostname: instance-2
        domain: anydomain.com
        datacenter: dal09
        tags:
          - ansible-module-test
          - ansible-module-test-replicas
        hourly: true
        private: false
        dedicated: false
        local_disk: true
        cpus: 1
        memory: 1024
        disks:
          - 25
          - 100
        os_code: UBUNTU_LATEST
        ssh_keys: []
        wait: true
      - hostname: instance-3
        domain: anydomain.com
        datacenter: dal09
        tags:
          - ansible-module-test
          - ansible-module-test-replicas
        hourly: true
        private: false
        dedicated: false
        local_disk: true
        cpus: 1
        memory: 1024
        disks:
          - 25
          - 100
        os_code: UBUNTU_LATEST
        ssh_keys: []
        wait: true

- name: Cancel instances
  hosts: localhost
  gather_facts: false
  tasks:
  - name: Cancel by tag
    community.general.sl_vm:
      state: absent
      tags: ansible-module-test
```

### Authors

- Matt Colton (@mcltn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
