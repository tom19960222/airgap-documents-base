---
collection: ansible
version: "6"
title: "community.general.vmadm module – Manage SmartOS virtual machines and zones"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/vmadm_module.html
fetched_at: 2026-07-27T17:13:56+00:00
---
# community.general.vmadm module – Manage SmartOS virtual machines and zones

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
> see [Requirements](vmadm_module.md#ansible-collections-community-general-vmadm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.vmadm`.

- [Synopsis](vmadm_module.md#synopsis)
- [Requirements](vmadm_module.md#requirements)
- [Parameters](vmadm_module.md#parameters)
- [Examples](vmadm_module.md#examples)
- [Return Values](vmadm_module.md#return-values)

## [Synopsis](vmadm_module.md#id1)

- Manage SmartOS virtual machines through vmadm(1M).

## [Requirements](vmadm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vmadm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **archive_on_delete**  boolean | When enabled, the zone dataset will be mounted on `/zones/archive` upon removal.  Choices:   - `false` - `true` |
| **autoboot**  boolean | Whether or not a VM is booted when the system is rebooted.  Choices:   - `false` - `true` |
| **boot**  string | Set the boot order for KVM VMs. |
| **brand**  string | Type of virtual machine. The `bhyve` option was added in community.general 0.2.0.  Choices:   - `"joyent"` ← (default) - `"joyent-minimal"` - `"lx"` - `"kvm"` - `"bhyve"` |
| **cpu_cap**  integer | Sets a limit on the amount of CPU time that can be used by a VM. Use `0` for no cap. |
| **cpu_shares**  integer | Sets a limit on the number of fair share scheduler (FSS) CPU shares for a VM. This limit is relative to all other VMs on the system. |
| **cpu_type**  string | Control the type of virtual CPU exposed to KVM VMs.  Choices:   - `"qemu64"` ← (default) - `"host"` |
| **customer_metadata**  dictionary | Metadata to be set and associated with this VM, this contain customer modifiable keys. |
| **delegate_dataset**  boolean | Whether to delegate a ZFS dataset to an OS VM.  Choices:   - `false` - `true` |
| **disk_driver**  string | Default value for a virtual disk model for KVM guests. |
| **disks**  list / elements=dictionary | A list of disks to add, valid properties are documented in vmadm(1M). |
| **dns_domain**  string | Domain value for `/etc/hosts`. |
| **docker**  boolean | Docker images need this flag enabled along with the *brand* set to `lx`.  Choices:   - `false` - `true` |
| **filesystems**  list / elements=dictionary | Mount additional filesystems into an OS VM. |
| **firewall_enabled**  boolean | Enables the firewall, allowing fwadm(1M) rules to be applied.  Choices:   - `false` - `true` |
| **force**  boolean | Force a particular action (i.e. stop or delete a VM).  Choices:   - `false` - `true` |
| **fs_allowed**  string | Comma separated list of filesystem types this zone is allowed to mount. |
| **hostname**  string | Zone/VM hostname. |
| **image_uuid**  string | Image UUID. |
| **indestructible_delegated**  boolean | Adds an `@indestructible` snapshot to delegated datasets.  Choices:   - `false` - `true` |
| **indestructible_zoneroot**  boolean | Adds an `@indestructible` snapshot to zoneroot.  Choices:   - `false` - `true` |
| **internal_metadata**  dictionary | Metadata to be set and associated with this VM, this contains operator generated keys. |
| **internal_metadata_namespace**  string | List of namespaces to be set as *internal_metadata-only*; these namespaces will come from *internal_metadata* rather than *customer_metadata*. |
| **kernel_version**  string | Kernel version to emulate for LX VMs. |
| **limit_priv**  string | Set (comma separated) list of privileges the zone is allowed to use. |
| **maintain_resolvers**  boolean | Resolvers in `/etc/resolv.conf` will be updated when updating the *resolvers* property.  Choices:   - `false` - `true` |
| **max_locked_memory**  integer | Total amount of memory (in MiBs) on the host that can be locked by this VM. |
| **max_lwps**  integer | Maximum number of lightweight processes this VM is allowed to have running. |
| **max_physical_memory**  integer | Maximum amount of memory (in MiBs) on the host that the VM is allowed to use. |
| **max_swap**  integer | Maximum amount of virtual memory (in MiBs) the VM is allowed to use. |
| **mdata_exec_timeout**  integer | Timeout in seconds (or 0 to disable) for the `svc:/smartdc/mdata:execute` service that runs user-scripts in the zone. |
| **name**  aliases: alias  string | Name of the VM. vmadm(1M) uses this as an optional name. |
| **nic_driver**  string | Default value for a virtual NIC model for KVM guests. |
| **nics**  list / elements=dictionary | A list of nics to add, valid properties are documented in vmadm(1M). |
| **nowait**  boolean | Consider the provisioning complete when the VM first starts, rather than when the VM has rebooted.  Choices:   - `false` - `true` |
| **qemu_extra_opts**  string | Additional qemu cmdline arguments for KVM guests. |
| **qemu_opts**  string | Additional qemu arguments for KVM guests. This overwrites the default arguments provided by vmadm(1M) and should only be used for debugging. |
| **quota**  integer | Quota on zone filesystems (in MiBs). |
| **ram**  integer | Amount of virtual RAM for a KVM guest (in MiBs). |
| **resolvers**  list / elements=string | List of resolvers to be put into `/etc/resolv.conf`. |
| **routes**  dictionary | Dictionary that maps destinations to gateways, these will be set as static routes in the VM. |
| **spice_opts**  string | Addition options for SPICE-enabled KVM VMs. |
| **spice_password**  string | Password required to connect to SPICE. By default no password is set. Please note this can be read from the Global Zone. |
| **state**  string | States for the VM to be in. Please note that `present`, `stopped` and `restarted` operate on a VM that is currently provisioned. `present` means that the VM will be created if it was absent, and that it will be in a running state. `absent` will shutdown the zone before removing it. `stopped` means the zone will be created if it doesn’t exist already, before shutting it down.  Choices:   - `"present"` - `"running"` ← (default) - `"absent"` - `"deleted"` - `"stopped"` - `"created"` - `"restarted"` - `"rebooted"` |
| **tmpfs**  integer | Amount of memory (in MiBs) that will be available in the VM for the `/tmp` filesystem. |
| **uuid**  string | UUID of the VM. Can either be a full UUID or `*` for all VMs. |
| **vcpus**  integer | Number of virtual CPUs for a KVM guest. |
| **vga**  string | Specify VGA emulation used by KVM VMs. |
| **virtio_txburst**  integer | Number of packets that can be sent in a single flush of the tx queue of virtio NICs. |
| **virtio_txtimer**  integer | Timeout (in nanoseconds) for the TX timer of virtio NICs. |
| **vnc_password**  string | Password required to connect to VNC. By default no password is set. Please note this can be read from the Global Zone. |
| **vnc_port**  integer | TCP port to listen of the VNC server. Or set `0` for random, or `-1` to disable. |
| **zfs_data_compression**  string | Specifies compression algorithm used for this VMs data dataset. This option only has effect on delegated datasets. |
| **zfs_data_recsize**  integer | Suggested block size (power of 2) for files in the delegated dataset’s filesystem. |
| **zfs_filesystem_limit**  integer | Maximum number of filesystems the VM can have. |
| **zfs_io_priority**  integer | IO throttle priority value relative to other VMs. |
| **zfs_root_compression**  string | Specifies compression algorithm used for this VMs root dataset. This option only has effect on the zoneroot dataset. |
| **zfs_root_recsize**  integer | Suggested block size (power of 2) for files in the zoneroot dataset’s filesystem. |
| **zfs_snapshot_limit**  integer | Number of snapshots the VM can have. |
| **zpool**  string | ZFS pool the VM’s zone dataset will be created in. |

## [Examples](vmadm_module.md#id4)

```yaml+jinja
- name: Create SmartOS zone
  community.general.vmadm:
    brand: joyent
    state: present
    alias: fw_zone
    image_uuid: 95f265b8-96b2-11e6-9597-972f3af4b6d5
    firewall_enabled: true
    indestructible_zoneroot: true
    nics:
      - nic_tag: admin
        ip: dhcp
        primary: true
    internal_metadata:
      root_pw: 'secret'
    quota: 1

- name: Delete a zone
  community.general.vmadm:
    alias: test_zone
    state: deleted

- name: Stop all zones
  community.general.vmadm:
    uuid: '*'
    state: stopped
```

## [Return Values](vmadm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **alias**  string | Alias of the managed VM.  Returned: When addressing a VM by alias.  Sample: `"dns-zone"` |
| **state**  string | State of the target, after execution.  Returned: success  Sample: `"running"` |
| **uuid**  string | UUID of the managed VM.  Returned: always  Sample: `"b217ab0b-cf57-efd8-cd85-958d0b80be33"` |

### Authors

- Jasper Lievisse Adriaanse (@jasperla)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
