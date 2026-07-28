---
collection: ansible
version: "8"
title: "community.general.proxmox_disk module – Management of a disk of a Qemu(KVM) VM in a Proxmox VE cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_disk_module.html
fetched_at: 2026-07-28T01:49:17+00:00
---
# community.general.proxmox_disk module – Management of a disk of a Qemu(KVM) VM in a Proxmox VE cluster

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
> see [Requirements](proxmox_disk_module.md#ansible-collections-community-general-proxmox-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_disk`.

New in community.general 5.7.0

- [Synopsis](proxmox_disk_module.md#synopsis)
- [Requirements](proxmox_disk_module.md#requirements)
- [Parameters](proxmox_disk_module.md#parameters)
- [Attributes](proxmox_disk_module.md#attributes)
- [Examples](proxmox_disk_module.md#examples)
- [Return Values](proxmox_disk_module.md#return-values)

## [Synopsis](proxmox_disk_module.md#id1)

- Allows you to perform some supported operations on a disk in Qemu(KVM) Virtual Machines in a Proxmox VE cluster.

Aliases: cloud.misc.proxmox_disk

## [Requirements](proxmox_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aio**  string | AIO type to use.  **Choices:**   - `"native"` - `"threads"` - `"io_uring"` |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **backup**  boolean | Whether the drive should be included when making backups.  **Choices:**   - `false` - `true` |
| **bps_max_length**  integer | Maximum length of total r/w I/O bursts in seconds. |
| **bps_rd_max_length**  integer | Maximum length of read I/O bursts in seconds. |
| **bps_wr_max_length**  integer | Maximum length of write I/O bursts in seconds. |
| **bwlimit**  integer | Override I/O bandwidth limit (in KB/s).  Used only when `state=moved`. |
| **cache**  string | The drive’s cache mode.  **Choices:**   - `"none"` - `"writethrough"` - `"writeback"` - `"unsafe"` - `"directsync"` |
| **create**  string | With `create` flag you can control behavior of `state=present`.  When `create=disabled` it will not create new disk (if not exists) but will update options in existing disk.  When `create=regular` it will either create new disk (if not exists) or update options in existing disk.  When `create=forced` it will always create new disk (if disk exists it will be detached and left unused).  **Choices:**   - `"disabled"` - `"regular"` ← (default) - `"forced"` |
| **cyls**  integer | Force the drive’s physical geometry to have a specific cylinder count. |
| **delete_moved**  boolean | Delete the original disk after successful copy.  By default the original disk is kept as unused disk.  Used only when `state=moved`.  **Choices:**   - `false` - `true` |
| **detect_zeroes**  boolean | Control whether to detect and try to optimize writes of zeroes.  **Choices:**   - `false` - `true` |
| **discard**  string | Control whether to pass discard/trim requests to the underlying storage.  **Choices:**   - `"ignore"` - `"on"` |
| **disk**  string / required | The disk key (`unused[n]`, `ide[n]`, `sata[n]`, `scsi[n]` or `virtio[n]`) you want to operate on.  Disk buses (IDE, SATA and so on) have fixed ranges of `n` that accepted by Proxmox API.  For IDE: 0-3; for SCSI: 0-30; for SATA: 0-5; for VirtIO: 0-15; for Unused: 0-255. |
| **format**  string | The drive’s backing file’s data format.  **Choices:**   - `"raw"` - `"cow"` - `"qcow"` - `"qed"` - `"qcow2"` - `"vmdk"` - `"cloop"` |
| **heads**  integer | Force the drive’s physical geometry to have a specific head count. |
| **import_from**  string | Import volume from this existing one.  Volume string format  `<STORAGE>:<VMID>/<FULL_NAME>` or `<ABSOLUTE_PATH>/<FULL_NAME>`  Attention! Only root can use absolute paths.  This parameter is mutually exclusive with `size`.  Increase `timeout` parameter when importing large disk images or using slow storage. |
| **iops**  integer | Maximum total r/w I/O in operations per second.  You can specify either total limit or per operation (mutually exclusive with `iops_rd` and `iops_wr`). |
| **iops_max**  integer | Maximum unthrottled total r/w I/O pool in operations per second. |
| **iops_max_length**  integer | Maximum length of total r/w I/O bursts in seconds. |
| **iops_rd**  integer | Maximum read I/O in operations per second.  You can specify either read or total limit (mutually exclusive with `iops`). |
| **iops_rd_max**  integer | Maximum unthrottled read I/O pool in operations per second. |
| **iops_rd_max_length**  integer | Maximum length of read I/O bursts in seconds. |
| **iops_wr**  integer | Maximum write I/O in operations per second.  You can specify either write or total limit (mutually exclusive with `iops`). |
| **iops_wr_max**  integer | Maximum unthrottled write I/O pool in operations per second. |
| **iops_wr_max_length**  integer | Maximum length of write I/O bursts in seconds. |
| **iothread**  boolean | Whether to use iothreads for this drive (only for SCSI and VirtIO)  **Choices:**   - `false` - `true` |
| **mbps**  float | Maximum total r/w speed in megabytes per second.  Can be fractional but use with caution - fractionals less than 1 are not supported officially.  You can specify either total limit or per operation (mutually exclusive with `mbps_rd` and `mbps_wr`). |
| **mbps_max**  float | Maximum unthrottled total r/w pool in megabytes per second. |
| **mbps_rd**  float | Maximum read speed in megabytes per second.  You can specify either read or total limit (mutually exclusive with `mbps`). |
| **mbps_rd_max**  float | Maximum unthrottled read pool in megabytes per second. |
| **mbps_wr**  float | Maximum write speed in megabytes per second.  You can specify either write or total limit (mutually exclusive with `mbps`). |
| **mbps_wr_max**  float | Maximum unthrottled write pool in megabytes per second. |
| **media**  string | The drive’s media type.  **Choices:**   - `"cdrom"` - `"disk"` |
| **name**  string | The unique name of the VM.  You can specify either `name` or `vmid` or both of them. |
| **queues**  integer | Number of queues (SCSI only). |
| **replicate**  boolean | Whether the drive should considered for replication jobs.  **Choices:**   - `false` - `true` |
| **rerror**  string | Read error action.  **Choices:**   - `"ignore"` - `"report"` - `"stop"` |
| **ro**  boolean | Whether the drive is read-only.  **Choices:**   - `false` - `true` |
| **scsiblock**  boolean | Whether to use scsi-block for full passthrough of host block device.  Can lead to I/O errors in combination with low memory or high memory fragmentation on host.  **Choices:**   - `false` - `true` |
| **secs**  integer | Force the drive’s physical geometry to have a specific sector count. |
| **serial**  string | The drive’s reported serial number, url-encoded, up to 20 bytes long. |
| **shared**  boolean | Mark this locally-managed volume as available on all nodes.  This option does not share the volume automatically, it assumes it is shared already!  **Choices:**   - `false` - `true` |
| **size**  string | Desired volume size in GB to allocate when `state=present` (specify `size` without suffix).  New (or additional) size of volume when `state=resized`. With the `+` sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. |
| **snapshot**  boolean | Control qemu’s snapshot mode feature.  If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.  **Choices:**   - `false` - `true` |
| **ssd**  boolean | Whether to expose this drive as an SSD, rather than a rotational hard disk.  **Choices:**   - `false` - `true` |
| **state**  string | Indicates desired state of the disk.  `state=present` can be used to create, replace disk or update options in existing disk. It will create missing disk or update options in existing one by default. See the `create` parameter description to control behavior of this option.  Some updates on options (like `cache`) are not being applied instantly and require VM restart.  Use `state=detached` to detach existing disk from VM but do not remove it entirely. When `state=detached` and disk is `unused[n]` it will be left in same state (not removed).  `state=moved` may be used to change backing storage for the disk in bounds of the same VM or to send the disk to another VM (using the same backing storage).  `state=resized` intended to change the disk size. As of Proxmox 7.2 you can only increase the disk size because shrinking disks is not supported by the PVE API and has to be done manually.  To entirely remove the disk from backing storage use `state=absent`.  **Choices:**   - `"present"` ← (default) - `"resized"` - `"detached"` - `"moved"` - `"absent"` |
| **storage**  string | The drive’s backing storage.  Used only when `state` is `present`. |
| **target_disk**  string | The config key the disk will be moved to on the target VM (for example, `ide0` or `scsi1`).  Default is the source disk key.  Used only when `state=moved`. |
| **target_storage**  string | Move the disk to this storage when `state=moved`.  You can move between storages only in scope of one VM.  Mutually exclusive with `target_vmid`.  Consider increasing `timeout` in case of large disk images or slow storage backend. |
| **target_vmid**  integer | The (unique) ID of the VM where disk will be placed when `state=moved`.  You can move disk between VMs only when the same storage is used.  Mutually exclusive with `target_vmid`. |
| **timeout**  integer | Timeout in seconds to wait for slow operations such as importing disk or moving disk between storages.  Used only when `state` is `present` or `moved`.  **Default:** `600` |
| **trans**  string | Force disk geometry bios translation mode.  **Choices:**   - `"auto"` - `"lba"` - `"none"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |
| **vmid**  integer | The unique ID of the VM.  You can specify either `vmid` or `name` or both of them. |
| **werror**  string | Write error action.  **Choices:**   - `"enospc"` - `"ignore"` - `"report"` - `"stop"` |
| **wwn**  string | The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by `0x`. |

## [Attributes](proxmox_disk_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](proxmox_disk_module.md#id5)

```yaml+jinja
- name: Create new disk in VM (do not rewrite in case it exists already)
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_token_id: token1
    api_token_secret: some-token-data
    name: vm-name
    disk: scsi3
    backup: true
    cache: none
    storage: local-zfs
    size: 5
    state: present

- name: Create new disk in VM (force rewrite in case it exists already)
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_token_id: token1
    api_token_secret: some-token-data
    vmid: 101
    disk: scsi3
    format: qcow2
    storage: local
    size: 16
    create: forced
    state: present

- name: Update existing disk
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_token_id: token1
    api_token_secret: some-token-data
    vmid: 101
    disk: ide0
    backup: false
    ro: true
    aio: native
    state: present

- name: Grow existing disk
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_token_id: token1
    api_token_secret: some-token-data
    vmid: 101
    disk: sata4
    size: +5G
    state: resized

- name: Detach disk (leave it unused)
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_token_id: token1
    api_token_secret: some-token-data
    name: vm-name
    disk: virtio0
    state: detached

- name: Move disk to another storage
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_password: secret
    vmid: 101
    disk: scsi7
    target_storage: local
    format: qcow2
    state: moved

- name: Move disk from one VM to another
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_token_id: token1
    api_token_secret: some-token-data
    vmid: 101
    disk: scsi7
    target_vmid: 201
    state: moved

- name: Remove disk permanently
  community.general.proxmox_disk:
    api_host: node1
    api_user: root@pam
    api_password: secret
    vmid: 101
    disk: scsi4
    state: absent
```

## [Return Values](proxmox_disk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A short message on what the module did.  **Returned:** always  **Sample:** `"Disk scsi3 created in VM 101"` |
| **vmid**  integer | The VM vmid.  **Returned:** success  **Sample:** `101` |

### Authors

- Castor Sky (@castorsky)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
