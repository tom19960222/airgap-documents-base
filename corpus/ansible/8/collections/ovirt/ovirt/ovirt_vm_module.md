---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_vm module – Module to manage Virtual Machines in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_vm_module.html
fetched_at: 2026-07-28T02:50:09+00:00
---
# ovirt.ovirt.ovirt_vm module – Module to manage Virtual Machines in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_vm_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_vm`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_vm_module.md#synopsis)
- [Requirements](ovirt_vm_module.md#requirements)
- [Parameters](ovirt_vm_module.md#parameters)
- [Notes](ovirt_vm_module.md#notes)
- [Examples](ovirt_vm_module.md#examples)
- [Return Values](ovirt_vm_module.md#return-values)

## [Synopsis](ovirt_vm_module.md#id1)

- This module manages whole lifecycle of the Virtual Machine(VM) in oVirt/RHV.
- Since VM can hold many states in oVirt/RHV, this see notes to see how the states of the VM are handled.

## [Requirements](ovirt_vm_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_vm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **affinity_group_mappings**  list / elements=dictionary | Mapper which maps affinity name between VM’s OVF and the destination affinity this VM should be registered to, relevant when `state` is registered. |
| **affinity_label_mappings**  list / elements=dictionary | Mapper which maps affinity label name between VM’s OVF and the destination label this VM should be registered to, relevant when `state` is registered. |
| **allow_partial_import**  boolean | Boolean indication whether to allow partial registration of Virtual Machine when `state` is registered.  **Choices:**   - `false` - `true` |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **ballooning_enabled**  boolean | If *true*, use memory ballooning.  Memory balloon is a guest device, which may be used to re-distribute / reclaim the host memory based on VM needs in a dynamic way. In this way it’s possible to create memory over commitment states.  **Choices:**   - `false` - `true` |
| **bios_type**  string | Set bios type, necessary for some operating systems and secure boot.  If no value is passed, default value is set from cluster.  NOTE - Supported since oVirt 4.3.  **Choices:**   - `"i440fx_sea_bios"` - `"q35_ovmf"` - `"q35_sea_bios"` - `"q35_secure_boot"` |
| **boot_devices**  list / elements=string | List of boot devices which should be used to boot. For example `[ cdrom, hd ]`.  Default value is set by oVirt/RHV engine.  **Choices:**   - `"cdrom"` - `"hd"` - `"network"` |
| **boot_menu**  boolean | *True* enable menu to select boot device, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **cd_iso**  string | ISO file from ISO storage domain which should be attached to Virtual Machine.  If you have multiple ISO disks with the same name use disk ID to specify which should be used or use `storage_domain` to filter disks.  If you pass empty string the CD will be ejected from VM.  If used with `state` *running* or *present* and VM is running the CD will be attached to VM.  If used with `state` *running* or *present* and VM is down the CD will be attached to VM persistently. |
| **clone**  boolean | If *yes* then the disks of the created virtual machine will be cloned and independent of the template.  This parameter is used only when `state` is *running* or *present* and VM didn’t exist before.  **Choices:**   - `false` ← (default) - `true` |
| **clone_permissions**  boolean | If *yes* then the permissions of the template (only the direct ones, not the inherited ones) will be copied to the created virtual machine.  This parameter is used only when `state` is *running* or *present* and VM didn’t exist before.  **Choices:**   - `false` ← (default) - `true` |
| **cloud_init**  dictionary | Dictionary with values for Unix-like Virtual Machine initialization using cloud init. |
| **authorized_ssh_keys**  string | Use this SSH keys to login to Virtual Machine. |
| **custom_script**  string | Cloud-init script which will be executed on Virtual Machine when deployed.  This is appended to the end of the cloud-init script generated by any other options.  For further information, refer to cloud-init User-Data documentation. |
| **dns_search**  string | DNS search domains to be configured on Virtual Machine. |
| **dns_servers**  string | DNS servers to be configured on Virtual Machine, maximum of two, space-separated. |
| **host_name**  string | Hostname to be set to Virtual Machine when deployed. |
| **nic_boot_protocol**  string | Set boot protocol of the network interface of Virtual Machine.  **Choices:**   - `"none"` - `"dhcp"` - `"static"` |
| **nic_boot_protocol_v6**  string | Set boot protocol of the network interface of Virtual Machine.  **Choices:**   - `"none"` - `"dhcp"` - `"static"` |
| **nic_gateway**  string | If boot protocol is static, set this gateway to network interface of Virtual Machine. |
| **nic_gateway_v6**  string | If boot protocol is static, set this gateway to network interface of Virtual Machine.  For IPv6 addresses the value is an integer in the range of 0-128, which represents the subnet prefix. |
| **nic_ip_address**  string | If boot protocol is static, set this IP address to network interface of Virtual Machine. |
| **nic_ip_address_v6**  string | If boot protocol is static, set this IP address to network interface of Virtual Machine. |
| **nic_name**  string | Set name to network interface of Virtual Machine. |
| **nic_netmask**  string | If boot protocol is static, set this netmask to network interface of Virtual Machine. |
| **nic_netmask_v6**  string | If boot protocol is static, set this netmask to network interface of Virtual Machine. |
| **regenerate_ssh_keys**  boolean | If *True* SSH keys will be regenerated on Virtual Machine.  **Choices:**   - `false` - `true` |
| **root_password**  string | Password to be set for user specified by `user_name` parameter. |
| **timezone**  string | Timezone to be set to Virtual Machine when deployed. |
| **user_name**  string | Username to be used to set password to Virtual Machine when deployed. |
| **cloud_init_nics**  list / elements=dictionary | List of dictionaries representing network interfaces to be setup by cloud init.  This option is used, when user needs to setup more network interfaces via cloud init.  If one network interface is enough, user should use `cloud_init` *nic_\** parameters. `cloud_init` *nic_\** parameters are merged with `cloud_init_nics` parameters. |
| **nic_boot_protocol**  string | Set boot protocol of the network interface of Virtual Machine. Can be one of `none`, `dhcp` or `static`. |
| **nic_boot_protocol_v6**  string | Set boot protocol of the network interface of Virtual Machine. Can be one of `none`, `dhcp` or `static`. |
| **nic_gateway**  string | If boot protocol is static, set this gateway to network interface of Virtual Machine. |
| **nic_gateway_v6**  string | If boot protocol is static, set this gateway to network interface of Virtual Machine.  For IPv6 addresses the value is an integer in the range of 0-128, which represents the subnet prefix. |
| **nic_ip_address**  string | If boot protocol is static, set this IP address to network interface of Virtual Machine. |
| **nic_ip_address_v6**  string | If boot protocol is static, set this IP address to network interface of Virtual Machine. |
| **nic_name**  string | Set name to network interface of Virtual Machine. |
| **nic_netmask**  string | If boot protocol is static, set this netmask to network interface of Virtual Machine. |
| **nic_netmask_v6**  string | If boot protocol is static, set this netmask to network interface of Virtual Machine. |
| **cloud_init_persist**  aliases: sysprep_persist  boolean | If *yes* the `cloud_init` or `sysprep` parameters will be saved for the virtual machine and the virtual machine won’t be started as run-once.  **Choices:**   - `false` ← (default) - `true` |
| **cluster**  string | Name of the cluster, where Virtual Machine should be created.  Required if creating VM. |
| **cluster_mappings**  list / elements=dictionary | Mapper which maps cluster name between VM’s OVF and the destination cluster this VM should be registered to, relevant when `state` is registered. Cluster mapping is described by the following dictionary: |
| **dest_name**  string | The name of the destination cluster. |
| **source_name**  string | The name of the source cluster. |
| **comment**  string | Comment of the Virtual Machine. |
| **cpu_cores**  integer | Number of virtual CPUs cores of the Virtual Machine.  Default value is set by oVirt/RHV engine. |
| **cpu_mode**  string | CPU mode of the virtual machine. It can be some of the following: *host_passthrough*, *host_model* or *custom*.  For *host_passthrough* CPU type you need to set `placement_policy` to *pinned*.  If no value is passed, default value is set by oVirt/RHV engine. |
| **cpu_pinning**  list / elements=dictionary | CPU Pinning topology to map virtual machine CPU to host CPU.  CPU Pinning topology is a list of dictionary which can have following values: |
| **cpu**  string | Number of the host CPU. |
| **vcpu**  string | Number of the virtual machine CPU. |
| **cpu_shares**  integer | Set a CPU shares for this Virtual Machine.  Default value is set by oVirt/RHV engine. |
| **cpu_sockets**  integer | Number of virtual CPUs sockets of the Virtual Machine.  Default value is set by oVirt/RHV engine. |
| **cpu_threads**  integer | Number of threads per core of the Virtual Machine.  Default value is set by oVirt/RHV engine. |
| **custom_compatibility_version**  string | Enables a virtual machine to be customized to its own compatibility version. If ‘`custom_compatibility_version`‘ is set, it overrides the cluster’s compatibility version for this particular virtual machine. |
| **custom_emulated_machine**  string | Sets the value of the custom_emulated_machine attribute. |
| **custom_properties**  list / elements=dictionary | Properties sent to VDSM to configure various hooks.  Custom properties is a list of dictionary which can have following values: |
| **name**  string | Name of the custom property. For example: *hugepages*, *vhost*, *sap_agent*, etc. |
| **regexp**  string | Regular expression to set for custom property. |
| **value**  string | Value to set for custom property. |
| **delete_protected**  boolean | If *yes* Virtual Machine will be set as delete protected.  If *no* Virtual Machine won’t be set as delete protected.  If no value is passed, default value is set by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **description**  string | Description of the Virtual Machine. |
| **disk_format**  string | Specify format of the disk.  If `cow` format is used, disk will by created as sparse, so space will be allocated for the volume as needed, also known as *thin provision*.  If `raw` format is used, disk storage will be allocated right away, also known as *preallocated*.  Note that this option isn’t idempotent as it’s not currently possible to change format of the disk via API.  This parameter is considered only when `template` and `storage domain` is provided.  **Choices:**   - `"cow"` ← (default) - `"raw"` |
| **disks**  list / elements=dictionary | List of disks, which should be attached to Virtual Machine. Disk is described by following dictionary. |
| **activate**  boolean | *True* if the disk should be activated, default is activated.  NOTE - This parameter is used only when `state` is *running* or *present* and is able to only attach disks. To manage disks of the VM in more depth please use [ovirt.ovirt.ovirt_disk](ovirt_disk_module.md#ansible-collections-ovirt-ovirt-ovirt-disk-module) module instead.  **Choices:**   - `false` - `true` |
| **bootable**  boolean | *True* if the disk should be bootable, default is non bootable.  **Choices:**   - `false` - `true` |
| **id**  string | ID of the disk. Either `name` or `id` is required. |
| **interface**  string | Interface of the disk.  **Choices:**   - `"virtio"` ← (default) - `"ide"` |
| **name**  string | Name of the disk. Either `name` or `id` is required. |
| **domain_mappings**  list / elements=dictionary | Mapper which maps aaa domain name between VM’s OVF and the destination aaa domain this VM should be registered to, relevant when `state` is registered. The aaa domain mapping is described by the following dictionary: |
| **dest_name**  string | The name of the destination aaa domain. |
| **source_name**  string | The name of the source aaa domain. |
| **exclusive**  boolean | When `state` is *exported* this parameter indicates if the existing VM with the same name should be overwritten.  **Choices:**   - `false` - `true` |
| **export_domain**  string | When `state` is *exported*this parameter specifies the name of the export storage domain. |
| **export_ova**  dictionary | Dictionary of values to be used to export VM as OVA. |
| **directory**  string | The name of the directory where the OVA has to be exported. |
| **filename**  string | The name of the exported OVA file. |
| **host**  string | The name of the destination host where the OVA has to be exported. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | Please check to *Synopsis* to more detailed description of force parameter, it can behave differently in different situations.  **Choices:**   - `false` ← (default) - `true` |
| **force_migrate**  boolean | If *true*, the VM will migrate when *placement_policy=user-migratable* but not when *placement_policy=pinned*.  **Choices:**   - `false` - `true` |
| **graphical_console**  dictionary | Assign graphical console to the virtual machine. |
| **copy_paste_enabled**  boolean | Indicates whether a user is able to copy and paste content from an external host into the graphic console.  This option is only available for the SPICE console type.  **Choices:**   - `false` - `true` |
| **disconnect_action**  string | Returns the action that will take place when the graphic console(SPICE only) is disconnected. The options are:  *none* No action is taken.  *lock_screen* Locks the currently active user session.  *logout* Logs out the currently active user session.  *reboot* Initiates a graceful virtual machine reboot.  *shutdown* Initiates a graceful virtual machine shutdown. |
| **file_transfer_enabled**  boolean | Indicates if a user is able to drag and drop files from an external host into the graphic console.  This option is only available for the SPICE console type.  **Choices:**   - `false` - `true` |
| **headless_mode**  boolean | If *true* disable the graphics console for this virtual machine.  **Choices:**   - `false` - `true` |
| **keyboard_layout**  string | The keyboard layout to use with this graphic console.  This option is only available for the VNC console type.  If no keyboard is enabled then it won’t be reported. |
| **monitors**  integer | The number of monitors opened for this graphic console.  This option is only available for the SPICE protocol.  Possible values are 1, 2 or 4. |
| **protocol**  list / elements=string | Graphical protocol, a list of *spice*, *vnc*, or both. |
| **high_availability**  boolean | If *yes* Virtual Machine will be set as highly available.  If *no* Virtual Machine won’t be set as highly available.  If no value is passed, default value is set by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **high_availability_priority**  integer | Indicates the priority of the virtual machine inside the run and migration queues. Virtual machines with higher priorities will be started and migrated before virtual machines with lower priorities. The value is an integer between 0 and 100. The higher the value, the higher the priority.  If no value is passed, default value is set by oVirt/RHV engine. |
| **host**  string | Specify host where Virtual Machine should be running. By default the host is chosen by engine scheduler.  This parameter is used only when `state` is *running* or *present*. |
| **host_devices**  list / elements=dictionary | Single Root I/O Virtualization - technology that allows single device to expose multiple endpoints that can be passed to VMs  host_devices is an list which contain dictionary with name and state of device |
| **id**  string | ID of the Virtual Machine to manage. |
| **initrd_path**  string | Path to an initial ramdisk to be used with the kernel specified by `kernel_path` option.  Ramdisk image must be stored on either the ISO domain or on the host’s storage. |
| **instance_type**  string | Name of virtual machine’s hardware configuration.  By default no instance type is used. |
| **io_threads**  integer | Number of IO threads used by virtual machine. *0* means IO threading disabled. |
| **kernel_params**  string | Kernel command line parameters (formatted as string) to be used with the kernel specified by `kernel_path` option. |
| **kernel_params_persist**  boolean | If *true* `kernel_params`, `initrd_path` and `kernel_path` will persist in virtual machine configuration, if *False* it will be used for run once.  **Choices:**   - `false` ← (default) - `true` |
| **kernel_path**  string | Path to a kernel image used to boot the virtual machine.  Kernel image must be stored on either the ISO domain or on the host’s storage. |
| **kvm**  dictionary | Dictionary of values to be used to connect to kvm and import a virtual machine to oVirt. |
| **drivers_iso**  string | The name of the ISO containing drivers that can be used during the *virt-v2v* conversion process. |
| **name**  string | The name of the KVM virtual machine. |
| **password**  string | The password to authenticate against the KVM. |
| **sparse**  boolean | Specifies the disk allocation policy of the resulting virtual machine. *true* for sparse, *false* for preallocated.  **Choices:**   - `false` - `true` ← (default) |
| **storage_domain**  string | Specifies the target storage domain for converted disks. This is required parameter. |
| **url**  string | The URL to be passed to the *virt-v2v* tool for conversion.  For example *qemu:///system*. This is required parameter. |
| **username**  string | The username to authenticate against the KVM. |
| **lease**  string | Name of the storage domain this virtual machine lease reside on. Pass an empty string to remove the lease.  NOTE - Supported since oVirt 4.1. |
| **lun_mappings**  list / elements=dictionary | Mapper which maps lun between VM’s OVF and the destination lun this VM should contain, relevant when `state` is registered. lun_mappings is described by the following dictionary: |
| **logical_unit_address**  string | The address of the block storage host. |
| **logical_unit_id**  string | The logical unit number to identify a logical unit, |
| **logical_unit_password)**  string | Password to be used to connect to the block storage host. |
| **logical_unit_port**  string | The port being used to connect with the LUN disk. |
| **logical_unit_portal**  string | The portal being used to connect with the LUN disk. |
| **logical_unit_target**  string | The iSCSI specification located on an iSCSI server |
| **logical_unit_username**  string | Username to be used to connect to the block storage host. |
| **storage_type**  string | The storage type which the LUN reside on (iscsi or fcp)” |
| **memory**  string | Amount of memory of the Virtual Machine. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  Default value is set by engine. |
| **memory_guaranteed**  string | Amount of minimal guaranteed memory of the Virtual Machine. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  `memory_guaranteed` parameter can’t be lower than `memory` parameter.  Default value is set by engine. |
| **memory_max**  string | Upper bound of virtual machine memory up to which memory hot-plug can be performed. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  Default value is set by engine. |
| **migrate**  boolean | If *true*, the VM will migrate to any available host.  **Choices:**   - `false` - `true` |
| **multi_queues_enabled**  boolean  *added in ovirt.ovirt 1.7.0* | If `true`, each virtual interface will get the optimal number of queues, depending on the available virtual Cpus.  **Choices:**   - `false` - `true` |
| **name**  string | Name of the Virtual Machine to manage.  If VM don’t exists `name` is required. Otherwise `id` or `name` can be used. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **next_run**  boolean | If *true*, the update will not be applied to the VM immediately and will be only applied when virtual machine is restarted.  NOTE - If there are multiple next run configuration changes on the VM, the first change may get reverted if this option is not passed.  **Choices:**   - `false` - `true` |
| **nics**  list / elements=dictionary | List of NICs, which should be attached to Virtual Machine. NIC is described by following dictionary. |
| **interface**  string | Type of the network interface.  **Choices:**   - `"virtio"` ← (default) - `"e1000"` - `"rtl8139"` |
| **mac_address**  string | Custom MAC address of the network interface, by default it’s obtained from MAC pool.  NOTE - This parameter is used only when `state` is *running* or *present* and is able to only create NICs. To manage NICs of the VM in more depth please use [ovirt.ovirt.ovirt_nic](ovirt_nic_module.md#ansible-collections-ovirt-ovirt-ovirt-nic-module) module instead. |
| **name**  string | Name of the NIC. |
| **profile_name**  string | Profile name where NIC should be attached. |
| **numa_nodes**  list / elements=dictionary | List of vNUMA Nodes to set for this VM and pin them to assigned host’s physical NUMA node.  Each vNUMA node is described by following dictionary: |
| **cores**  list / elements=integer / required | List of VM CPU cores indexes to be included in this NUMA node. |
| **index**  string / required | The index of this NUMA node. |
| **memory**  string / required | Memory size of the NUMA node in MiB. |
| **numa_node_pins**  list / elements=integer | List of physical NUMA node indexes to pin this virtual NUMA node to. |
| **numa_tune_mode**  string | Set how the memory allocation for NUMA nodes of this VM is applied (relevant if NUMA nodes are set for this VM).  It can be one of the following: *interleave*, *preferred* or *strict*.  If no value is passed, default value is set by oVirt/RHV engine.  **Choices:**   - `"interleave"` - `"preferred"` - `"strict"` |
| **operating_system**  string | Operating system of the Virtual Machine, for example ‘rhel_8x64’.  Default value is set by oVirt/RHV engine.  Use the [ovirt.ovirt.ovirt_vm_os_info](ovirt_vm_os_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-os-info-module) module to obtain the current list. |
| **placement_policy**  string | The configuration of the virtual machine’s placement policy.  If no value is passed, default value is set by oVirt/RHV engine.  Placement policy can be one of the following values: |
| **migratable**  string | Allow manual and automatic migration. |
| **pinned**  string | Do not allow migration. |
| **user_migratable**  string | Allow manual migration only. |
| **placement_policy_hosts**  list / elements=string | List of host names. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **quota_id**  string | Virtual Machine quota ID to be used for disk. By default quota is chosen by oVirt/RHV engine. |
| **reassign_bad_macs**  boolean | Boolean indication whether to reassign bad macs when `state` is registered.  **Choices:**   - `false` - `true` |
| **rng_device**  string | Random number generator (RNG). You can choose of one the following devices *urandom*, *random* or *hwrng*.  In order to select *hwrng*, you must have it enabled on cluster first.  /dev/urandom is used for cluster version >= 4.1, and /dev/random for cluster version <= 4.0 |
| **role_mappings**  list / elements=dictionary | Mapper which maps role name between VM’s OVF and the destination role this VM should be registered to, relevant when `state` is registered. Role mapping is described by the following dictionary: |
| **dest_name**  string | The name of the destination role. |
| **source_name**  string | The name of the source role. |
| **serial_console**  boolean | *True* enable VirtIO serial console, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **serial_policy**  string | Specify a serial number policy for the Virtual Machine.  Following options are supported.  `vm` - Sets the Virtual Machine’s UUID as its serial number.  `host` - Sets the host’s UUID as the Virtual Machine’s serial number.  `custom` - Allows you to specify a custom serial number in `serial_policy_value`.  **Choices:**   - `"vm"` - `"host"` - `"custom"` |
| **serial_policy_value**  string | Allows you to specify a custom serial number.  This parameter is used only when `serial_policy` is *custom*. |
| **smartcard_enabled**  boolean | If *true*, use smart card authentication.  **Choices:**   - `false` - `true` |
| **snapshot_name**  string | Snapshot to clone VM from.  Snapshot with description specified should exist.  You have to specify `snapshot_vm` parameter with virtual machine name of this snapshot. |
| **snapshot_vm**  string | Source VM to clone VM from.  VM should have snapshot specified by `snapshot`.  If `snapshot_name` specified `snapshot_vm` is required. |
| **soundcard_enabled**  boolean | If *true*, the sound card is added to the virtual machine.  **Choices:**   - `false` - `true` |
| **sso**  boolean | *True* enable Single Sign On by Guest Agent, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **state**  string | Should the Virtual Machine be running/stopped/present/absent/suspended/next_run/registered/exported/reboot. When `state` is *registered* and the unregistered VM’s name belongs to an already registered in engine VM in the same DC then we fail to register the unregistered template.  *present* state will create/update VM and don’t change its state if it already exists.  *running* state will create/update VM and start it.  *next_run* state updates the VM and if the VM has next run configuration it will be rebooted.  Please check *notes* to more detailed description of states.  *exported* state will export the VM to export domain or as OVA.  *registered* is supported since 2.4.  *reboot* is supported since 2.10, virtual machine is rebooted only if it’s in up state.  *reset* sends a reset request to a virtual machine.  **Choices:**   - `"absent"` - `"next_run"` - `"present"` ← (default) - `"registered"` - `"running"` - `"stopped"` - `"suspended"` - `"exported"` - `"reboot"` - `"reset"` |
| **stateless**  boolean | If *yes* Virtual Machine will be set as stateless.  If *no* Virtual Machine will be unset as stateless.  If no value is passed, default value is set by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **storage_domain**  string | Name of the storage domain where all template disks should be created.  This parameter is considered only when `template` is provided.  IMPORTANT - This parameter is not idempotent, if the VM exists and you specify different storage domain, disk won’t move. |
| **storage_error_resume_behaviour**  string  *added in ovirt.ovirt 3.2.0* | If the storage, on which this virtual machine has some disks gets unresponsive, the virtual machine gets paused.  These are the possible options, what should happen with the virtual machine at the moment the storage becomes available again.  **Choices:**   - `"auto_resume"` - `"kill"` - `"leave_paused"` |
| **sysprep**  dictionary | Dictionary with values for Windows Virtual Machine initialization using sysprep. |
| **active_directory_ou**  string | Active Directory Organizational Unit, to be used for login of user. |
| **custom_script**  string | A custom Sysprep definition in the format of a complete unattended installation answer file. |
| **domain**  string | Domain to be set to Windows Virtual Machine. |
| **host_name**  string | Hostname to be set to Virtual Machine when deployed. |
| **input_locale**  string | Input localization of the Windows Virtual Machine. |
| **org_name**  string | Organization name to be set to Windows Virtual Machine. |
| **root_password**  string | Password to be set for username to Windows Virtual Machine. |
| **system_locale**  string | System localization of the Windows Virtual Machine. |
| **timezone**  string | Timezone to be set to Windows Virtual Machine. |
| **ui_language**  string | UI language of the Windows Virtual Machine. |
| **user_name**  string | Username to be used for set password to Windows Virtual Machine. |
| **windows_license_key**  string | License key to be set to Windows Virtual Machine. |
| **template**  string | Name of the template, which should be used to create Virtual Machine.  Required if creating VM.  If template is not specified and VM doesn’t exist, VM will be created from *Blank* template. |
| **template_version**  integer | Version number of the template to be used for VM.  By default the latest available version of the template is used. |
| **ticket**  boolean | If *true*, in addition return *remote_vv_file* inside *vm* dictionary, which contains compatible content for remote-viewer application. Works only `state` is *running*.  **Choices:**   - `false` - `true` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **timezone**  string | Sets time zone offset of the guest hardware clock.  For example `Etc/GMT` |
| **tpm_enabled**  boolean  *added in ovirt.ovirt 3.2.0* | If `true`, a TPM device is added to the virtual machine.  **Choices:**   - `false` - `true` |
| **type**  string | Type of the Virtual Machine.  Default value is set by oVirt/RHV engine.  *high_performance* is supported since Ansible 2.5 and oVirt/RHV 4.2.  **Choices:**   - `"desktop"` - `"server"` - `"high_performance"` |
| **usb_support**  boolean | *True* enable USB support, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **use_latest_template_version**  boolean | Specify if latest template version should be used, when running a stateless VM.  If this parameter is set to *yes* stateless VM is created.  **Choices:**   - `false` - `true` |
| **virtio_scsi_enabled**  boolean  *added in ovirt.ovirt 1.7.0* | Enable Virtio SCSI support.  **Choices:**   - `false` - `true` |
| **virtio_scsi_multi_queues**  integer  *added in ovirt.ovirt 1.7.0* | Number of queues for a Virtio-SCSI controller, possible values: -1 - Indicates that the queues will be automatically set. 0 - Indicates that the Virtio SCSI multi-queue will be disabled. >0 - Number of Virtio SCSI queues to use by virtual machine. |
| **vmware**  dictionary | Dictionary of values to be used to connect to VMware and import a virtual machine to oVirt. |
| **drivers_iso**  string | The name of the ISO containing drivers that can be used during the *virt-v2v* conversion process. |
| **password**  string | The password to authenticate against the VMware. |
| **sparse**  boolean | Specifies the disk allocation policy of the resulting virtual machine. *true* for sparse, *false* for preallocated.  **Choices:**   - `false` - `true` ← (default) |
| **storage_domain**  string | Specifies the target storage domain for converted disks. This is required parameter. |
| **url**  string | The URL to be passed to the *virt-v2v* tool for conversion.  For example *vpx://wmware_user@vcenter-host/DataCenter/Cluster/esxi-host?no_verify=1* |
| **username**  string | The username to authenticate against the VMware. |
| **vnic_profile_mappings**  list / elements=dictionary | Mapper which maps an external virtual NIC profile to one that exists in the engine when `state` is registered. vnic_profile is described by the following dictionary: |
| **source_network_name**  string | The network name of the source network. |
| **source_profile_name**  string | The profile name related to the source network. |
| **target_profile_id**  string | The id of the target profile id to be mapped to in the engine. |
| **volatile**  boolean  *added in ovirt.ovirt 2.2.0* | Indicates that this run configuration will be discarded even in the case of guest-initiated reboot.  **Choices:**   - `false` - `true` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |
| **wait_after_lease**  integer  *added in ovirt.ovirt 2.1.0* | Number of seconds which should the module wait after the lease is changed.  **Default:** `5` |
| **watchdog**  dictionary | Assign watchdog device for the virtual machine.  Watchdogs is a dictionary which can have following values: |
| **action**  string | Watchdog action to be performed when watchdog is triggered. For example: *none*, *reset*, *poweroff*, *pause* or *dump*. |
| **model**  string | Model of the watchdog device. For example: *i6300esb*, *diag288* or *null*. |
| **xen**  dictionary | Dictionary of values to be used to connect to XEN and import a virtual machine to oVirt. |
| **drivers_iso**  string | The name of the ISO containing drivers that can be used during the *virt-v2v* conversion process. |
| **sparse**  boolean | Specifies the disk allocation policy of the resulting virtual machine. *true* for sparse, *false* for preallocated.  **Choices:**   - `false` - `true` ← (default) |
| **storage_domain**  string | Specifies the target storage domain for converted disks. This is required parameter. |
| **url**  string | The URL to be passed to the *virt-v2v* tool for conversion.  For example *xen+ssh://root@zen.server*. This is required parameter. |

## [Notes](ovirt_vm_module.md#id4)

> **Note:**
>
> - If VM is in *UNASSIGNED* or *UNKNOWN* state before any operation, the module will fail. If VM is in *IMAGE_LOCKED* state before any operation, we try to wait for VM to be *DOWN*. If VM is in *SAVING_STATE* state before any operation, we try to wait for VM to be *SUSPENDED*. If VM is in *POWERING_DOWN* state before any operation, we try to wait for VM to be *UP* or *DOWN*. VM can get into *UP* state from *POWERING_DOWN* state, when there is no ACPI or guest agent running inside VM, or if the shutdown operation fails. When user specify *UP* `state`, we always wait to VM to be in *UP* state in case VM is *MIGRATING*, *REBOOTING*, *POWERING_UP*, *RESTORING_STATE*, *WAIT_FOR_LAUNCH*. In other states we run start operation on VM. When user specify *stopped* `state`, and If user pass `force` parameter set to *true* we forcibly stop the VM in any state. If user don’t pass `force` parameter, we always wait to VM to be in UP state in case VM is *MIGRATING*, *REBOOTING*, *POWERING_UP*, *RESTORING_STATE*, *WAIT_FOR_LAUNCH*. If VM is in *PAUSED* or *SUSPENDED* state, we start the VM. Then we gracefully shutdown the VM. When user specify *suspended* `state`, we always wait to VM to be in UP state in case VM is *MIGRATING*, *REBOOTING*, *POWERING_UP*, *RESTORING_STATE*, *WAIT_FOR_LAUNCH*. If VM is in *PAUSED* or *DOWN* state, we start the VM. Then we suspend the VM. When user specify *absent* `state`, we forcibly stop the VM in any state and remove it.
> - If you update a VM parameter that requires a reboot, the oVirt engine always creates a new snapshot for the VM, and an Ansible playbook will report this as changed.
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_vm_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Creates a new Virtual Machine from template named 'rhel7_template'
  ovirt.ovirt.ovirt_vm:
    state: present
    name: myvm
    template: rhel7_template
    cluster: mycluster

- name: Register VM
  ovirt.ovirt.ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    name: myvm

- name: Register VM using id
  ovirt.ovirt.ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111

- name: Register VM, allowing partial import
  ovirt.ovirt.ovirt_vm:
    state: registered
    storage_domain: mystorage
    allow_partial_import: "True"
    cluster: mycluster
    id: 1111-1111-1111-1111

- name: Register VM with vnic profile mappings and reassign bad macs
  ovirt.ovirt.ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111
    vnic_profile_mappings:
    - source_network_name: mynetwork
      source_profile_name: mynetwork
      target_profile_id: 3333-3333-3333-3333
    - source_network_name: mynetwork2
      source_profile_name: mynetwork2
      target_profile_id: 4444-4444-4444-4444
    reassign_bad_macs: "True"

- name: Register VM with mappings
  ovirt.ovirt.ovirt_vm:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111
    role_mappings:
      - source_name: Role_A
        dest_name: Role_B
    domain_mappings:
      - source_name: Domain_A
        dest_name: Domain_B
    lun_mappings:
      - source_storage_type: iscsi
        source_logical_unit_id: 1IET_000d0001
        source_logical_unit_port: 3260
        source_logical_unit_portal: 1
        source_logical_unit_address: 10.34.63.203
        source_logical_unit_target: iqn.2016-08-09.brq.str-01:omachace
        dest_storage_type: iscsi
        dest_logical_unit_id: 1IET_000d0002
        dest_logical_unit_port: 3260
        dest_logical_unit_portal: 1
        dest_logical_unit_address: 10.34.63.204
        dest_logical_unit_target: iqn.2016-08-09.brq.str-02:omachace
    affinity_group_mappings:
      - source_name: Affinity_A
        dest_name: Affinity_B
    affinity_label_mappings:
      - source_name: Label_A
        dest_name: Label_B
    cluster_mappings:
      - source_name: cluster_A
        dest_name: cluster_B

- name: Creates a stateless VM which will always use latest template version
  ovirt.ovirt.ovirt_vm:
    name: myvm
    template: rhel7
    cluster: mycluster
    use_latest_template_version: true

# Creates a new server rhel7 Virtual Machine from Blank template
# on brq01 cluster with 2GiB memory and 2 vcpu cores/sockets
# and attach bootable disk with name rhel7_disk and attach virtio NIC
- ovirt.ovirt.ovirt_vm:
    state: present
    cluster: brq01
    name: myvm
    memory: 2GiB
    cpu_cores: 2
    cpu_sockets: 2
    cpu_shares: 1024
    type: server
    operating_system: rhel_7x64
    disks:
      - name: rhel7_disk
        bootable: True
    nics:
      - name: nic1

# Change VM Name
- ovirt.ovirt.ovirt_vm:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_vm_name"

- name: Run VM with cloud init
  ovirt.ovirt.ovirt_vm:
    name: rhel7
    template: rhel7
    cluster: Default
    memory: 1GiB
    high_availability: true
    high_availability_priority: 50  # Available from Ansible 2.5
    cloud_init:
      dns_servers: '8.8.8.8 8.8.4.4'
      nic_boot_protocol: static
      nic_ip_address: 10.34.60.86
      nic_netmask: 255.255.252.0
      nic_gateway: 10.34.63.254
      nic_name: eth1
      host_name: example.com
      custom_script: |
        write_files:
         - content: |
             Hello, world!
           path: /tmp/greeting.txt
           permissions: '0644'
      user_name: root
      root_password: super_password

- name: Run VM with cloud init, with multiple network interfaces
  ovirt.ovirt.ovirt_vm:
    name: rhel7_4
    template: rhel7
    cluster: mycluster
    cloud_init_nics:
    - nic_name: eth0
      nic_boot_protocol: dhcp
    - nic_name: eth1
      nic_boot_protocol: static
      nic_ip_address: 10.34.60.86
      nic_netmask: 255.255.252.0
      nic_gateway: 10.34.63.254
    # IP version 6 parameters are supported since ansible 2.9
    - nic_name: eth2
      nic_boot_protocol_v6: static
      nic_ip_address_v6: '2620:52:0:2282:b898:1f69:6512:36c5'
      nic_gateway_v6: '2620:52:0:2282:b898:1f69:6512:36c9'
      nic_netmask_v6: '120'
    - nic_name: eth3
      nic_boot_protocol_v6: dhcp

- name: Run VM with sysprep
  ovirt.ovirt.ovirt_vm:
    name: windows2012R2_AD
    template: windows2012R2
    cluster: Default
    memory: 3GiB
    high_availability: true
    sysprep:
      host_name: windowsad.example.com
      user_name: Administrator
      root_password: SuperPassword123

- name: Migrate/Run VM to/on host named 'host1'
  ovirt.ovirt.ovirt_vm:
    state: running
    name: myvm
    host: host1

- name: Migrate/Run VM to/on host named 'host1' on cluster 'cluster1'
  ovirt.ovirt.ovirt_vm:
    state: running
    name: myvm
    host: host1
    cluster: cluster1

- name: Migrate VM to any available host
  ovirt.ovirt.ovirt_vm:
    state: running
    name: myvm
    migrate: true

- name: Change VMs CD
  ovirt.ovirt.ovirt_vm:
    name: myvm
    cd_iso: drivers.iso

- name: Eject VMs CD
  ovirt.ovirt.ovirt_vm:
    name: myvm
    cd_iso: ''

- name: Boot VM from CD
  ovirt.ovirt.ovirt_vm:
    name: myvm
    cd_iso: centos7_x64.iso
    boot_devices:
        - cdrom

- name: Stop vm
  ovirt.ovirt.ovirt_vm:
    state: stopped
    name: myvm

- name: Upgrade memory to already created VM
  ovirt.ovirt.ovirt_vm:
    name: myvm
    memory: 4GiB

- name: Hot plug memory to already created and running VM (VM won't be restarted)
  ovirt.ovirt.ovirt_vm:
    name: myvm
    memory: 4GiB

# Create/update a VM to run with two vNUMA nodes and pin them to physical NUMA nodes as follows:
# vnuma index 0-> numa index 0, vnuma index 1-> numa index 1
- name: Create a VM to run with two vNUMA nodes
  ovirt.ovirt.ovirt_vm:
    name: myvm
    cluster: mycluster
    numa_tune_mode: "interleave"
    numa_nodes:
    - index: 0
      cores: [0]
      memory: 20
      numa_node_pins: [0]
    - index: 1
      cores: [1]
      memory: 30
      numa_node_pins: [1]

- name: Update an existing VM to run without previously created vNUMA nodes (i.e. remove all vNUMA nodes+NUMA pinning setting)
  ovirt.ovirt.ovirt_vm:
    name: myvm
    cluster: mycluster
    state: "present"
    numa_tune_mode: "interleave"
    numa_nodes:
    - index: -1

# When change on the VM needs restart of the VM, use next_run state,
# The VM will be updated and rebooted if there are any changes.
# If present state would be used, VM won't be restarted.
- ovirt.ovirt.ovirt_vm:
    state: next_run
    name: myvm
    boot_devices:
      - network

- name: Import virtual machine from VMware
  ovirt.ovirt.ovirt_vm:
    state: stopped
    cluster: mycluster
    name: vmware_win10
    timeout: 1800
    poll_interval: 30
    vmware:
      url: vpx://user@1.2.3.4/Folder1/Cluster1/2.3.4.5?no_verify=1
      name: windows10
      storage_domain: mynfs
      username: user
      password: password

- name: Create vm from template and create all disks on specific storage domain
  ovirt.ovirt.ovirt_vm:
    name: vm_test
    cluster: mycluster
    template: mytemplate
    storage_domain: mynfs
    nics:
    - name: nic1

- name: Remove VM, if VM is running it will be stopped
  ovirt.ovirt.ovirt_vm:
    state: absent
    name: myvm

# Defining a specific quota for a VM:
# Since Ansible 2.5
- ovirt.ovirt.ovirt_quotas_info:
    data_center: Default
    name: myquota
  register: ovirt_quotas
- ovirt.ovirt.ovirt_vm:
    name: myvm
    sso: False
    boot_menu: True
    bios_type: q35_ovmf
    usb_support: True
    serial_console: True
    quota_id: "{{ ovirt_quotas[0]['id'] }}"

- name: Create a VM that has the console configured for both Spice and VNC
  ovirt.ovirt.ovirt_vm:
    name: myvm
    template: mytemplate
    cluster: mycluster
    graphical_console:
      protocol:
        - spice
        - vnc

# Execute remote viewer to VM
- block:
  - name: Create a ticket for console for a running VM
    ovirt.ovirt.ovirt_vm:
      name: myvm
      ticket: true
      state: running
    register: myvm

  - name: Save ticket to file
    ansible.builtin.copy:
      content: "{{ myvm.vm.remote_vv_file }}"
      dest: ~/vvfile.vv

  - name: Run remote viewer with file
    ansible.builtin.command: remote-viewer ~/vvfile.vv

# Default value of host_device state is present
- name: Attach host devices to virtual machine
  ovirt.ovirt.ovirt_vm:
    name: myvm
    host: myhost
    placement_policy: pinned
    host_devices:
      - name: pci_0000_00_06_0
      - name: pci_0000_00_07_0
        state: absent
      - name: pci_0000_00_08_0
        state: present

- name: Add placement policy with multiple hosts
  ovirt.ovirt.ovirt_vm:
    name: myvm
    placement_policy: migratable
    placement_policy_hosts:
      - host1
      - host2

- name: Export the VM as OVA
  ovirt.ovirt.ovirt_vm:
    name: myvm
    state: exported
    cluster: mycluster
    export_ova:
        host: myhost
        filename: myvm.ova
        directory: /tmp/

- name: Clone VM from snapshot
  ovirt.ovirt.ovirt_vm:
    snapshot_vm: myvm
    snapshot_name: myvm_snap
    name: myvm_clone
    state: present

- name: Import external ova VM
  ovirt.ovirt.ovirt_vm:
    cluster: mycluster
    name: myvm
    host: myhost
    timeout: 1800
    poll_interval: 30
    kvm:
      name: myvm
      url: ova:///path/myvm.ova
      storage_domain: mystorage

- name: Cpu pinning of 0#12_1#13_2#14_3#15
  ovirt.ovirt.ovirt_vm:
    state: present
    cluster: mycluster
    name: myvm
    cpu_pinning:
      - cpu: 12
        vcpu: 0
      - cpu: 13
        vcpu: 1
      - cpu: 14
        vcpu: 2
      - cpu: 15
        vcpu: 3
```

## [Return Values](ovirt_vm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the VM which is managed  **Returned:** On success if VM is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **vm**  dictionary | Dictionary of all the VM attributes. VM attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/vm>. Additionally when user sent ticket=true, this module will return also remote_vv_file parameter in vm dictionary, which contains remote-viewer compatible file to open virtual machine console. Please note that this file contains sensible information.  **Returned:** On success if VM is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
