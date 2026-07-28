---
collection: ansible
version: "6"
title: "community.general.profitbricks module – Create, destroy, start, stop, and reboot a ProfitBricks virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/profitbricks_module.html
fetched_at: 2026-07-27T17:12:02+00:00
---
# community.general.profitbricks module – Create, destroy, start, stop, and reboot a ProfitBricks virtual machine

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
> see [Requirements](profitbricks_module.md#ansible-collections-community-general-profitbricks-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.profitbricks`.

- [Synopsis](profitbricks_module.md#synopsis)
- [Requirements](profitbricks_module.md#requirements)
- [Parameters](profitbricks_module.md#parameters)
- [Examples](profitbricks_module.md#examples)

## [Synopsis](profitbricks_module.md#id1)

- Create, destroy, update, start, stop, and reboot a ProfitBricks virtual machine. When the virtual machine is created it can optionally wait for it to be ‘running’ before returning. This module has a dependency on profitbricks >= 1.0.0

## [Requirements](profitbricks_module.md#id2)

The below requirements are needed on the host that executes this module.

- profitbricks
- python >= 2.6

## [Parameters](profitbricks_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **assign_public_ip**  boolean | This will assign the machine to the public LAN. If no LAN exists with public Internet access it is created.  Choices:   - `false` ← (default) - `true` |
| **auto_increment**  boolean | Whether or not to increment a single number in the name for created virtual machines.  Choices:   - `false` - `true` ← (default) |
| **bus**  string | The bus type for the volume.  Choices:   - `"IDE"` - `"VIRTIO"` ← (default) |
| **cores**  integer | The number of CPU cores to allocate to the virtual machine.  Default: `2` |
| **count**  integer | The number of virtual machines to create.  Default: `1` |
| **cpu_family**  string | The CPU family type to allocate to the virtual machine.  Choices:   - `"AMD_OPTERON"` ← (default) - `"INTEL_XEON"` |
| **datacenter**  string | The datacenter to provision this virtual machine. |
| **disk_type**  string | the type of disk to be allocated.  Choices:   - `"SSD"` - `"HDD"` ← (default) |
| **image**  string | The system image ID for creating the virtual machine, e.g. a3eae284-a2fe-11e4-b187-5f1f641608c8. |
| **image_password**  string | Password set for the administrative user. |
| **instance_ids**  list / elements=string | list of instance ids, currently only used when state=’absent’ to remove instances.  Default: `[]` |
| **lan**  integer | The ID of the LAN you wish to add the servers to.  Default: `1` |
| **location**  string | The datacenter location. Use only if you want to create the Datacenter or else this value is ignored.  Choices:   - `"us/las"` ← (default) - `"de/fra"` - `"de/fkb"` |
| **name**  string | The name of the virtual machine. |
| **ram**  integer | The amount of memory to allocate to the virtual machine.  Default: `2048` |
| **remove_boot_volume**  boolean | remove the bootVolume of the virtual machine you’re destroying.  Choices:   - `false` - `true` ← (default) |
| **ssh_keys**  list / elements=string | Public SSH keys allowing access to the virtual machine.  Default: `[]` |
| **state**  string | create or terminate instances  The choices available are: `running`, `stopped`, `absent`, `present`.  Default: `"present"` |
| **subscription_password**  string | THe ProfitBricks password. Overrides the PB_PASSWORD environment variable. |
| **subscription_user**  string | The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable. |
| **volume_size**  integer | The size in GB of the boot volume.  Default: `10` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | how long before wait gives up, in seconds  Default: `600` |

## [Examples](profitbricks_module.md#id4)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Provisioning example
- name: Create three servers and enumerate their names
  community.general.profitbricks:
    datacenter: Tardis One
    name: web%02d.stackpointcloud.com
    cores: 4
    ram: 2048
    volume_size: 50
    cpu_family: INTEL_XEON
    image: a3eae284-a2fe-11e4-b187-5f1f641608c8
    location: us/las
    count: 3
    assign_public_ip: true

- name: Remove virtual machines
  community.general.profitbricks:
    datacenter: Tardis One
    instance_ids:
      - 'web001.stackpointcloud.com'
      - 'web002.stackpointcloud.com'
      - 'web003.stackpointcloud.com'
    wait_timeout: 500
    state: absent

- name: Start virtual machines
  community.general.profitbricks:
    datacenter: Tardis One
    instance_ids:
      - 'web001.stackpointcloud.com'
      - 'web002.stackpointcloud.com'
      - 'web003.stackpointcloud.com'
    wait_timeout: 500
    state: running

- name: Stop virtual machines
  community.general.profitbricks:
    datacenter: Tardis One
    instance_ids:
      - 'web001.stackpointcloud.com'
      - 'web002.stackpointcloud.com'
      - 'web003.stackpointcloud.com'
    wait_timeout: 500
    state: stopped
```

### Authors

- Matt Baldwin (@baldwinSPC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
