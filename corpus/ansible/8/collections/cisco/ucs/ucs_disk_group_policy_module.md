---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_disk_group_policy module – Configures disk group policies on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_disk_group_policy_module.html
fetched_at: 2026-07-28T01:39:30+00:00
---
# cisco.ucs.ucs_disk_group_policy module – Configures disk group policies on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_disk_group_policy_module.md#ansible-collections-cisco-ucs-ucs-disk-group-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_disk_group_policy`.

- [Synopsis](ucs_disk_group_policy_module.md#synopsis)
- [Requirements](ucs_disk_group_policy_module.md#requirements)
- [Parameters](ucs_disk_group_policy_module.md#parameters)
- [Examples](ucs_disk_group_policy_module.md#examples)

## [Synopsis](ucs_disk_group_policy_module.md#id1)

- Configures disk group policies on Cisco UCS Manager.

## [Requirements](ucs_disk_group_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_disk_group_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configuration_mode**  string | Disk group configuration mode. Choose one of the following:  automatic - Automatically configures the disks in the disk group.  manual - Enables you to manually configure the disks in the disk group.  **Choices:**   - `"automatic"` ← (default) - `"manual"` |
| **description**  aliases: descr  string | The user-defined description of the storage profile.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **drive_type**  string | Specify the drive type to use in the drive group.  This can be one of the following:  unspecified — Selects the first available drive type, and applies that to all drives in the group.  HDD — Hard disk drive  SSD — Solid state drive  Option only applies when configuration mode is automatic.  **Choices:**   - `"unspecified"` ← (default) - `"HDD"` - `"SSD"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **manual_disks**  list / elements=dictionary | List of manually configured disks.  Options are only used when you choose manual configuration_mode. |
| **role**  string | The role of the disk. This can be one of the following:  normal - Normal  ded-hot-spare - Dedicated Hot Spare  glob-hot-spare - Glob Hot Spare  **Choices:**   - `"normal"` ← (default) - `"ded-hot-spare"` - `"glob-hot-spare"` |
| **slot_num**  string / required | The slot number of the specific disk. |
| **span_id**  string | The Span ID of the specific disk.  **Default:** `"unspecified"` |
| **state**  string | If `present`, will verify disk slot is configured within policy. If `absent`, will verify disk slot is absent from policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **min_drive_size**  string | Specify the minimum drive size or unspecified to allow all drive sizes.  This can be from 0 to 10240 GB.  Option only applies when configuration mode is automatic.  **Default:** `"unspecified"` |
| **name**  string / required | The name of the disk group policy.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the policy is created. |
| **num_ded_hot_spares**  string | Specify the number of hot spares for the disk group.  This can be from 0 to 24.  Option only applies when configuration mode is automatic.  **Default:** `"unspecified"` |
| **num_drives**  string | Specify the number of drives for the disk group.  This can be from 0 to 24.  Option only applies when configuration mode is automatic.  **Default:** `"1"` |
| **num_glob_hot_spares**  string | Specify the number of global hot spares for the disk group.  This can be from 0 to 24.  Option only applies when configuration mode is automatic.  **Default:** `"unspecified"` |
| **org_dn**  string | The distinguished name (dn) of the organization where the resource is assigned.  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **raid_level**  string | The RAID level for the disk group policy. This can be one of the following:  stripe - UCS Manager shows RAID 0 Striped  mirror - RAID 1 Mirrored  mirror-stripe - RAID 10 Mirrored and Striped  stripe-parity - RAID 5 Striped Parity  stripe-dual-parity - RAID 6 Striped Dual Parity  stripe-parity-stripe - RAID 50 Striped Parity and Striped  stripe-dual-parity-stripe - RAID 60 Striped Dual Parity and Striped  **Choices:**   - `"stripe"` ← (default) - `"mirror"` - `"mirror-stripe"` - `"stripe-parity"` - `"stripe-dual-parity"` - `"stripe-parity-stripe"` - `"stripe-dual-parity-stripe"` |
| **state**  string | Desired state of the disk group policy.  If `present`, will verify that the disk group policy is present and will create if needed.  If `absent`, will verify that the disk group policy is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_remaining_disks**  string | Specifies whether you can use all the remaining disks in the disk group or not.  Option only applies when configuration mode is automatic.  **Choices:**   - `"yes"` - `"no"` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **virtual_drive**  dictionary | Configuration of virtual drive options. |
| **access_policy**  string | Configure access policy to virtual drive.  **Choices:**   - `"blocked"` - `"hidden"` - `"platform-default"` ← (default) - `"read-only"` - `"read-write"` - `"transport-ready"` |
| **drive_cache**  string | Configure drive caching.  **Choices:**   - `"disable"` - `"enable"` - `"no-change"` - `"platform-default"` ← (default) |
| **io_policy**  string | Direct or Cached IO path.  **Choices:**   - `"cached"` - `"direct"` - `"platform-default"` ← (default) |
| **read_policy**  string | Read access policy to virtual drive.  **Choices:**   - `"normal"` - `"platform-default"` ← (default) - `"read-ahead"` |
| **strip_size**  string | Virtual drive strip size.  **Choices:**   - `"1024KB"` - `"128KB"` - `"16KB"` - `"256KB"` - `"32KB"` - `"512KB"` - `"64KB"` - `"8KB"` - `"platform-default"` ← (default) |
| **write_cache_policy**  string | Write back cache policy.  **Choices:**   - `"always-write-back"` - `"platform-default"` ← (default) - `"write-back-good-bbu"` - `"write-through"` |

## [Examples](ucs_disk_group_policy_module.md#id4)

```yaml+jinja
- name: Configure Disk Group Policy
  cisco.ucs.ucs_disk_group_policy:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-DG
    raid_level: mirror
    configuration_mode: manual
    manual_disks:
    - slot_num: '1'
      role: normal
    - slot_num: '2'
      role: normal

- name: Remove Disk Group Policy
  cisco.ucs.ucs_disk_group_policy:
    name: DEE-DG
    hostname: 172.16.143.150
    username: admin
    password: password
    state: absent

- name: Remove Disk from Policy
  cisco.ucs.ucs_disk_group_policy:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-DG
    description: Testing Ansible
    raid_level: stripe
    configuration_mode: manual
    manual_disks:
    - slot_num: '1'
      role: normal
    - slot_num: '2'
      role: normal
      state: absent
    virtual_drive:
      access_policy: platform-default
      io_policy: direct
      strip_size: 64KB
```

### Authors

- Sindhu Sudhir (@sisudhir)
- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)
- Brett Johnson (@sdbrett)
- John McDonough (@movinalot)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
