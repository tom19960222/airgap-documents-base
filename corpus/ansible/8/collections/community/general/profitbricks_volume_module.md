---
collection: ansible
version: "8"
title: "community.general.profitbricks_volume module – Create or destroy a volume"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/profitbricks_volume_module.html
fetched_at: 2026-07-28T01:49:14+00:00
---
# community.general.profitbricks_volume module – Create or destroy a volume

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
> see [Requirements](profitbricks_volume_module.md#ansible-collections-community-general-profitbricks-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.profitbricks_volume`.

- [Synopsis](profitbricks_volume_module.md#synopsis)
- [Requirements](profitbricks_volume_module.md#requirements)
- [Parameters](profitbricks_volume_module.md#parameters)
- [Attributes](profitbricks_volume_module.md#attributes)
- [Examples](profitbricks_volume_module.md#examples)

## [Synopsis](profitbricks_volume_module.md#id1)

- Allows you to create or remove a volume from a ProfitBricks datacenter. This module has a dependency on profitbricks >= 1.0.0

Aliases: cloud.profitbricks.profitbricks_volume

## [Requirements](profitbricks_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- profitbricks

## [Parameters](profitbricks_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_increment**  boolean | Whether or not to increment a single number in the name for created virtual machines.  **Choices:**   - `false` - `true` ← (default) |
| **bus**  string | The bus type.  **Choices:**   - `"IDE"` - `"VIRTIO"` ← (default) |
| **count**  integer | The number of volumes you wish to create.  **Default:** `1` |
| **datacenter**  string | The datacenter in which to create the volumes. |
| **disk_type**  string | The disk type of the volume.  **Choices:**   - `"HDD"` ← (default) - `"SSD"` |
| **image**  string | The system image ID for the volume, e.g. a3eae284-a2fe-11e4-b187-5f1f641608c8. This can also be a snapshot image ID. |
| **image_password**  string | Password set for the administrative user. |
| **instance_ids**  list / elements=string | list of instance ids, currently only used when state=’absent’ to remove instances.  **Default:** `[]` |
| **licence_type**  string | The licence type for the volume. This is used when the image is non-standard.  The available choices are: `LINUX`, `WINDOWS`, `UNKNOWN`, `OTHER`.  **Default:** `"UNKNOWN"` |
| **name**  string | The name of the volumes. You can enumerate the names using auto_increment. |
| **server**  string | Server name to attach the volume to. |
| **size**  integer | The size of the volume.  **Default:** `10` |
| **ssh_keys**  list / elements=string | Public SSH keys allowing access to the virtual machine.  **Default:** `[]` |
| **state**  string | create or terminate datacenters  The available choices are: `present`, `absent`.  **Default:** `"present"` |
| **subscription_password**  string | THe ProfitBricks password. Overrides the PB_PASSWORD environment variable. |
| **subscription_user**  string | The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable. |
| **wait**  boolean | wait for the datacenter to be created before returning  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `600` |

## [Attributes](profitbricks_volume_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](profitbricks_volume_module.md#id5)

```yaml+jinja
- name: Create multiple volumes
  community.general.profitbricks_volume:
    datacenter: Tardis One
    name: vol%02d
    count: 5
    auto_increment: true
    wait_timeout: 500
    state: present

- name: Remove Volumes
  community.general.profitbricks_volume:
    datacenter: Tardis One
    instance_ids:
      - 'vol01'
      - 'vol02'
    wait_timeout: 500
    state: absent
```

### Authors

- Matt Baldwin (@baldwinSPC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
