---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest module – Manages virtual machines in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_module.html
fetched_at: 2026-07-27T17:21:48+00:00
---
# community.vmware.vmware_guest module – Manages virtual machines in vCenter

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest`.

- [Synopsis](vmware_guest_module.md#synopsis)
- [Parameters](vmware_guest_module.md#parameters)
- [Notes](vmware_guest_module.md#notes)
- [Examples](vmware_guest_module.md#examples)
- [Return Values](vmware_guest_module.md#return-values)

## [Synopsis](vmware_guest_module.md#id1)

- This module can be used to create new virtual machines from templates or other virtual machines, manage power state of virtual machine such as power on, power off, suspend, shutdown, reboot, restart etc., modify various virtual machine components like network, disk, customization etc., rename a virtual machine and remove a virtual machine with associated components.

## [Parameters](vmware_guest_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advanced_settings**  list / elements=dictionary  added in community.vmware 1.8.0 | Define a list of advanced settings to be added to the VMX config.  An advanced settings object takes two fields `key` and `value`.  Incorrect key and values will be ignored.  Default: `[]` |
| **annotation**  aliases: notes  string | A note or annotation to include in the virtual machine. |
| **cdrom**  any | A list of CD-ROM configurations for the virtual machine. Added in version 2.9.  Providing CD-ROM configuration as dict is deprecated and will be removed VMware collection 4.0.0. Please use a list instead.  Parameters `controller_type`, `controller_number`, `unit_number`, `state` are added for a list of CD-ROMs configuration support.  For `ide` controller, hot-add or hot-remove CD-ROM is not supported.  Default: `[]` |
| **controller_number**  integer | For `ide` controller, valid value is 0 or 1.  For `sata` controller, valid value is 0 to 3. |
| **controller_type**  string | Valid options are `ide` and `sata`.  Default value is `ide`.  When set to `sata`, please make sure `unit_number` is correct and not used by SATA disks. |
| **iso_path**  string | The datastore path to the ISO file to use, in the form of `[datastore1] path/to/file.iso`.  Required if type is set `iso`. |
| **state**  string | Valid value is `present` or `absent`.  Default is `present`.  If set to `absent`, then the specified CD-ROM will be removed. |
| **type**  string | The type of CD-ROM, valid options are `none`, `client` or `iso`.  With `none` the CD-ROM will be disconnected but present.  The default value is `client`. |
| **unit_number**  integer | For CD-ROM device attach to `ide` controller, valid value is 0 or 1.  For CD-ROM device attach to `sata` controller, valid value is 0 to 29.  `controller_number` and `unit_number` are mandatory attributes. |
| **cluster**  string | The cluster name where the virtual machine will run.  This is a required parameter, if `esxi_hostname` is not set.  `esxi_hostname` and `cluster` are mutually exclusive parameters.  This parameter is case sensitive. |
| **convert**  string | Specify convert disk type while cloning template or virtual machine.  Choices:   - `"thin"` - `"thick"` - `"eagerzeroedthick"` |
| **customization**  dictionary | Parameters for OS customization when cloning from the template or the virtual machine, or apply to the existing virtual machine directly.  Not all operating systems are supported for customization with respective vCenter version, please check VMware documentation for respective OS customization.  For supported customization operating system matrix, (see <http://partnerweb.vmware.com/programs/guestOS/guest-os-customization-matrix.pdf>)  All parameters and VMware object names are case sensitive.  Linux based OSes requires Perl package to be installed for OS customizations.  Default: `{}` |
| **autologon**  boolean | Auto logon after virtual machine customization.  Specific to Windows customization.  Choices:   - `false` - `true` |
| **autologoncount**  integer | Number of autologon after reboot.  Specific to Windows customization.  Ignored if `autologon` is unset or set to `False`.  If unset, 1 will be used. |
| **dns_servers**  list / elements=string | List of DNS servers to configure.  Common for Linux and Windows customization. |
| **dns_suffix**  list / elements=string | List of domain suffixes, also known as DNS search path.  Default `domain` parameter.  Common for Linux and Windows customization. |
| **domain**  string | DNS domain name to use.  Common for Linux and Windows customization. |
| **domainadmin**  string | User used to join in AD domain.  Required if `joindomain` specified.  Specific to Windows customization. |
| **domainadminpassword**  string | Password used to join in AD domain.  Required if `joindomain` specified.  Specific to Windows customization. |
| **existing_vm**  boolean | If set to `True`, do OS customization on the specified virtual machine directly.  Common for Linux and Windows customization.  Choices:   - `false` - `true` |
| **fullname**  string | Server owner name.  Specific to Windows customization.  If unset, “Administrator” will be used as a fall-back. |
| **hostname**  string | Computer hostname.  Default is shortened `name` parameter.  Allowed characters are alphanumeric (uppercase and lowercase) and minus, rest of the characters are dropped as per RFC 952.  Common for Linux and Windows customization. |
| **hwclockUTC**  boolean | Specifies whether the hardware clock is in UTC or local time.  Specific to Linux customization.  Choices:   - `false` - `true` |
| **joindomain**  string | AD domain to join.  Not compatible with `joinworkgroup`.  Specific to Windows customization. |
| **joinworkgroup**  string | Workgroup to join.  Not compatible with `joindomain`.  Specific to Windows customization.  If unset, “WORKGROUP” will be used as a fall-back. |
| **orgname**  string | Organisation name.  Specific to Windows customization.  If unset, “ACME” will be used as a fall-back. |
| **password**  string | Local administrator password.  If not defined, the password will be set to blank (that is, no password).  Specific to Windows customization. |
| **productid**  string | Product ID.  Specific to Windows customization. |
| **runonce**  list / elements=string | List of commands to run at first user logon.  Specific to Windows customization. |
| **timezone**  string | Timezone.  See List of supported time zones for different vSphere versions in Linux/Unix.  Common for Linux and Windows customization.  [Windows](https://msdn.microsoft.com/en-us/library/ms912391.aspx). |
| **customization_spec**  string | Unique name identifying the requested customization specification.  This parameter is case sensitive.  If set, then overrides `customization` parameter values. |
| **customvalues**  list / elements=dictionary | Define a list of custom values to set on virtual machine.  A custom value object takes two fields `key` and `value`.  Incorrect key and values will be ignored.  Default: `[]` |
| **datacenter**  string | Destination datacenter for the deploy operation.  This parameter is case sensitive.  Default: `"ha-datacenter"` |
| **datastore**  string | Specify datastore or datastore cluster to provision virtual machine.  This parameter takes precedence over `disk.datastore` parameter.  This parameter can be used to override datastore or datastore cluster setting of the virtual machine when deployed from the template.  Please see example for more usage. |
| **delete_from_inventory**  boolean | Whether to delete Virtual machine from inventory or delete from disk.  Choices:   - `false` ← (default) - `true` |
| **disk**  list / elements=dictionary | A list of disks to add.  This parameter is case sensitive.  Shrinking disks is not supported.  Removing existing disks of the virtual machine is not supported.  Attributes `controller_type`, `controller_number`, `unit_number` are used to configure multiple types of disk controllers and disks for creating or reconfiguring virtual machine. Added in Ansible 2.10.  Default: `[]` |
| **autoselect_datastore**  boolean | Select the less used datastore.  `disk.datastore` and `disk.autoselect_datastore` will not be used if `datastore` is specified outside this `disk` configuration.  Choices:   - `false` - `true` |
| **controller_number**  integer | Disk controller bus number.  The maximum number of same type controller is 4 per VM.  Choices:   - `0` - `1` - `2` - `3` |
| **controller_type**  string | Type of disk controller.  `nvme` controller type support starts on ESXi 6.5 with VM hardware version `version` 13. Set this type on not supported ESXi or VM hardware version will lead to failure in deployment.  When set to `sata`, please make sure `unit_number` is correct and not used by SATA CDROMs.  If set to `sata` type, please make sure `controller_number` and `unit_number` are set correctly when `cdrom` also set to `sata` type.  Choices:   - `"buslogic"` - `"lsilogic"` - `"lsilogicsas"` - `"paravirtual"` - `"sata"` - `"nvme"` |
| **datastore**  string | The name of datastore which will be used for the disk.  If `autoselect_datastore` is set to True, will select the less used datastore whose name contains this “disk.datastore” string. |
| **disk_mode**  string | Type of disk mode.  Added in Ansible 2.6.  If `persistent` specified, changes are immediately and permanently written to the virtual disk. This is default.  If `independent_persistent` specified, same as persistent, but not affected by snapshots.  If `independent_nonpersistent` specified, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.  Choices:   - `"persistent"` - `"independent_persistent"` - `"independent_nonpersistent"` |
| **filename**  string | Existing disk image to be used.  Filename must already exist on the datastore.  Specify filename string in `[datastore_name] path/to/file.vmdk` format. Added in Ansible 2.8. |
| **size**  string | Disk storage size.  Please specify storage unit like [kb, mb, gb, tb]. |
| **size_gb**  integer | Disk storage size in gb. |
| **size_kb**  integer | Disk storage size in kb. |
| **size_mb**  integer | Disk storage size in mb. |
| **size_tb**  integer | Disk storage size in tb. |
| **type**  string | Type of disk.  If `thin` specified, disk type is set to thin disk.  If `eagerzeroedthick` specified, disk type is set to eagerzeroedthick disk. Added Ansible 2.5.  If not specified, disk type is inherited from the source VM or template when cloned and thick disk, no eagerzero otherwise.  Choices:   - `"thin"` - `"thick"` - `"eagerzeroedthick"` |
| **unit_number**  integer | Disk Unit Number.  Valid value range from 0 to 15 for SCSI controller, except 7.  Valid value range from 0 to 14 for NVME controller.  Valid value range from 0 to 29 for SATA controller.  `controller_type`, `controller_number` and `unit_number` are required when creating or reconfiguring VMs with multiple types of disk controllers and disks.  When creating new VM, the first configured disk in the `disk` list will be “Hard Disk 1”. |
| **esxi_hostname**  string | The ESXi hostname where the virtual machine will run.  This is a required parameter, if `cluster` is not set.  `esxi_hostname` and `cluster` are mutually exclusive parameters.  This parameter is case sensitive. |
| **folder**  string | Destination folder, absolute path to find an existing guest or create the new guest.  The folder should include the datacenter. ESXi’s datacenter is ha-datacenter.  This parameter is case sensitive.  If multiple machines are found with same name, this parameter is used to identify  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **force**  boolean | Ignore warnings and complete the actions.  This parameter is useful while removing virtual machine which is powered on state.  This module reflects the VMware vCenter API and UI workflow, as such, in some cases the `force` flag will be mandatory to perform the action to ensure you are certain the action has to be taken, no matter what the consequence. This is specifically the case for removing a powered on the virtual machine when `state` is set to `absent`.  Choices:   - `false` ← (default) - `true` |
| **guest_id**  string | Set the guest ID.  This parameter is case sensitive.  `rhel7_64Guest` for virtual machine with RHEL7 64 bit.  `centos64Guest` for virtual machine with CentOS 64 bit.  `ubuntu64Guest` for virtual machine with Ubuntu 64 bit.  This field is required when creating a virtual machine, not required when creating from the template.  Valid values are referenced here: <https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html> |
| **hardware**  dictionary | Manage virtual machine’s hardware attributes.  All parameters case sensitive.  Default: `{}` |
| **boot_firmware**  string | Choose which firmware should be used to boot the virtual machine.  Choices:   - `"bios"` - `"efi"` |
| **cpu_limit**  integer | The CPU utilization of a virtual machine will not exceed this limit.  Unit is MHz. |
| **cpu_reservation**  integer | The amount of CPU resource that is guaranteed available to the virtual machine. |
| **hotadd_cpu**  boolean | Allow virtual CPUs to be added while the virtual machine is running.  Choices:   - `false` - `true` |
| **hotadd_memory**  boolean | Allow memory to be added while the virtual machine is running.  Choices:   - `false` - `true` |
| **hotremove_cpu**  boolean | Allow virtual CPUs to be removed while the virtual machine is running.  Choices:   - `false` - `true` |
| **iommu**  boolean  added in community.vmware 1.11.0 | Flag to specify if I/O MMU is enabled for this virtual machine.  Choices:   - `false` - `true` |
| **max_connections**  integer | Maximum number of active remote display connections for the virtual machines. |
| **mem_limit**  integer | The memory utilization of a virtual machine will not exceed this limit.  Unit is MB. |
| **mem_reservation**  aliases: memory_reservation  integer | The amount of memory resource that is guaranteed available to the virtual machine. |
| **memory_mb**  integer | Amount of memory in MB. |
| **memory_reservation_lock**  boolean | If set `true`, memory resource reservation for the virtual machine.  Choices:   - `false` - `true` |
| **nested_virt**  boolean | Enable nested virtualization.  Choices:   - `false` - `true` |
| **num_cpu_cores_per_socket**  integer | Number of Cores Per Socket. |
| **num_cpus**  integer | Number of CPUs.  `num_cpus` must be a multiple of `num_cpu_cores_per_socket`.  For example, to create a VM with 2 sockets of 4 cores, specify `num_cpus` as 8 and `num_cpu_cores_per_socket` as 4. |
| **scsi**  string | Valid values are `buslogic`, `lsilogic`, `lsilogicsas` and `paravirtual`.  `paravirtual` is default.  Choices:   - `"buslogic"` - `"lsilogic"` - `"lsilogicsas"` - `"paravirtual"` |
| **secure_boot**  boolean  added in community.vmware 1.11.0 | Whether to enable or disable (U)EFI secure boot.  Choices:   - `false` - `true` |
| **version**  string | The Virtual machine hardware versions.  Default is 10 (ESXi 5.5 and onwards).  If set to `latest`, the specified virtual machine will be upgraded to the most current hardware version supported on the host.  `latest` is added in Ansible 2.10.  Please check VMware documentation for correct virtual machine hardware version.  Incorrect hardware version may lead to failure in deployment. If hardware version is already equal to the given. |
| **virt_based_security**  boolean | Enable Virtualization Based Security feature for Windows on ESXi 6.7 and later, from hardware version 14.  Supported Guest OS are Windows 10 64 bit, Windows Server 2016, Windows Server 2019 and later.  The firmware of virtual machine must be EFI and secure boot must be enabled.  Virtualization Based Security depends on nested virtualization and Intel Virtualization Technology for Directed I/O.  Deploy on unsupported ESXi, hardware version or firmware may lead to failure or deployed VM with unexpected configurations.  Choices:   - `false` - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **is_template**  boolean | Flag the instance as a template.  This will mark the given virtual machine as template.  Note, this may need to be done in a dedicated task invocation that is not making any other changes. For example, user cannot change the state from powered-on to powered-off AND save as template in the same task.  See [community.vmware.vmware_guest](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) source for more details.  Choices:   - `false` ← (default) - `true` |
| **linked_clone**  boolean | Whether to create a linked clone from the snapshot specified.  If specified, then `snapshot_src` is required parameter.  Choices:   - `false` ← (default) - `true` |
| **name**  string | Name of the virtual machine to work with.  Virtual machine names in vCenter are not necessarily unique, which may be problematic, see `name_match`.  If multiple virtual machines with same name exists, then `folder` is required parameter to identify uniqueness of the virtual machine.  This parameter is required, if `state` is set to `poweredon`, `powered-on`, `poweredoff`, `powered-off`, `present`, `restarted`, `suspended` and virtual machine does not exists.  This parameter is case sensitive. |
| **name_match**  string | If multiple virtual machines matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **networks**  list / elements=dictionary | A list of networks (in the order of the NICs).  Removing NICs is not allowed, while reconfiguring the virtual machine.  All parameters and VMware object names are case sensitive.  The *type*, *ip*, *netmask*, *gateway*, *domain*, *dns_servers* options don’t set to a guest when creating a blank new virtual machine. They are set by the customization via vmware-tools. If you want to set the value of the options to a guest, you need to clone from a template with installed OS and vmware-tools(also Perl when Linux).  Default: `[]` |
| **connected**  boolean  added in community.vmware 1.5.0 | Indicates whether the NIC is currently connected.  Choices:   - `false` - `true` |
| **device_type**  string | Virtual network device.  Valid value can be one of `e1000`, `e1000e`, `pcnet32`, `vmxnet2`, `vmxnet3`, `sriov`.  `vmxnet3` is default.  Optional per entry.  Used for virtual hardware. |
| **dns_servers**  string | DNS servers for this network interface (Windows).  Optional per entry.  Used for OS customization. |
| **domain**  string | Domain name for this network interface (Windows).  Optional per entry.  Used for OS customization. |
| **dvswitch_name**  string | Name of the distributed vSwitch.  Optional per entry.  Used for virtual hardware. |
| **gateway**  string | Static gateway.  Optional per entry.  Used for OS customization. |
| **ip**  string | Static IP address. Implies `type=static`.  Optional per entry.  Used for OS customization. |
| **mac**  string | Customize MAC address.  Optional per entry.  Used for virtual hardware. |
| **name**  string | Name of the portgroup or distributed virtual portgroup for this interface.  Required per entry.  When specifying distributed virtual portgroup make sure given `esxi_hostname` or `cluster` is associated with it. |
| **netmask**  string | Static netmask required for `ip`.  Optional per entry.  Used for OS customization. |
| **start_connected**  boolean | Specifies whether or not to connect the device when the virtual machine starts.  Choices:   - `false` - `true` |
| **type**  string | Type of IP assignment.  Valid values are one of `dhcp`, `static`.  `dhcp` is default.  Optional per entry.  Used for OS customization. |
| **vlan**  integer | VLAN number for this interface.  Required per entry. |
| **nvdimm**  dictionary  added in community.vmware 1.13.0 | Add or remove a virtual NVDIMM device to the virtual machine.  VM virtual hardware version must be 14 or higher on vSphere 6.7 or later.  Verify that guest OS of the virtual machine supports PMem before adding virtual NVDIMM device.  Verify that you have the *Datastore.Allocate* space privilege on the virtual machine.  Make sure that the host or the cluster on which the virtual machine resides has available PMem resources.  To add or remove virtual NVDIMM device to the existing virtual machine, it must be in power off state.  Default: `{}` |
| **label**  string | The label of the virtual NVDIMM device to be removed or configured, e.g., “NVDIMM 1”.  This parameter is required when `state` is set to `absent`, or `present` to reconfigure NVDIMM device size. When add a new device, please do not set `label`. |
| **size_mb**  integer | Virtual NVDIMM device size in MB.  Default: `1024` |
| **state**  string | Valid value is `present` or `absent`.  If set to `absent`, then the NVDIMM device with specified `label` will be removed.  Choices:   - `"present"` - `"absent"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string | Use the given resource pool for virtual machine operation.  This parameter is case sensitive.  Resource pool should be child of the selected host parent.  When not specified *Resources* is taken as default value. |
| **snapshot_src**  string | Name of the existing snapshot to use to create a clone of a virtual machine.  This parameter is case sensitive.  While creating linked clone using `linked_clone` parameter, this parameter is required. |
| **state**  string | Specify the state the virtual machine should be in.  If `state` is set to `present` and virtual machine exists, ensure the virtual machine configurations conforms to task arguments.  If `state` is set to `absent` and virtual machine exists, then the specified virtual machine is removed with it’s associated components.  If `state` is set to one of the following `poweredon`, `powered-on`, `poweredoff`, `powered-off`, `present`, `restarted`, `suspended` and virtual machine does not exists, virtual machine is deployed with the given parameters.  If `state` is set to `poweredon` or `powered-on` and virtual machine exists with powerstate other than powered on, then the specified virtual machine is powered on.  If `state` is set to `poweredoff` or `powered-off` and virtual machine exists with powerstate other than powered off, then the specified virtual machine is powered off.  If `state` is set to `restarted` and virtual machine exists, then the virtual machine is restarted.  If `state` is set to `suspended` and virtual machine exists, then the virtual machine is set to suspended mode.  If `state` is set to `shutdownguest` or `shutdown-guest` and virtual machine exists, then the virtual machine is shutdown.  If `state` is set to `rebootguest` or `reboot-guest` and virtual machine exists, then the virtual machine is rebooted.  Powerstate `powered-on` and `powered-off` is added in version 2.10.  Choices:   - `"absent"` - `"poweredon"` - `"powered-on"` - `"poweredoff"` - `"powered-off"` - `"present"` ← (default) - `"rebootguest"` - `"reboot-guest"` - `"restarted"` - `"suspended"` - `"shutdownguest"` - `"shutdown-guest"` |
| **state_change_timeout**  integer | If the `state` is set to `shutdownguest`, by default the module will return immediately after sending the shutdown signal.  If this argument is set to a positive integer, the module will instead wait for the virtual machine to reach the poweredoff state.  The value sets a timeout in seconds for the module to wait for the state change.  Default: `0` |
| **template**  aliases: template_src  string | Template or existing virtual machine used to create new virtual machine.  If this value is not set, virtual machine is created without using a template.  If the virtual machine already exists, this parameter will be ignored.  This parameter is case sensitive.  From version 2.8 onwards, absolute path to virtual machine or template can be used. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the virtual machine to manage if known, this is VMware’s unique identifier.  This is required if `name` is not supplied.  If virtual machine does not exists, then this parameter is ignored.  Please note that a supplied UUID will be ignored on virtual machine creation, as VMware creates the UUID internally. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vapp_properties**  list / elements=dictionary | A list of vApp properties.  For full list of attributes and types refer to: <https://code.vmware.com/apis/704/vsphere/vim.vApp.PropertyInfo.html>  Default: `[]` |
| **id**  string | Property ID.  Required per entry. |
| **operation**  string | The `remove` attribute is required only when removing properties. |
| **type**  string | Value type, string type by default. |
| **value**  string | Property value. |
| **wait_for_customization**  boolean | Wait until vCenter detects all guest customizations as successfully completed.  When enabled, the VM will automatically be powered on.  If vCenter does not detect guest customization start or succeed, failed events after time `wait_for_customization_timeout` parameter specified, warning message will be printed and task result is fail.  Choices:   - `false` ← (default) - `true` |
| **wait_for_customization_timeout**  integer | Define a timeout (in seconds) for the wait_for_customization parameter.  Be careful when setting this value since the time guest customization took may differ among guest OSes.  Default: `3600` |
| **wait_for_ip_address**  boolean | Wait until vCenter detects an IP address for the virtual machine.  This requires vmware-tools (vmtoolsd) to properly work after creation.  vmware-tools needs to be installed on the given virtual machine in order to work with this parameter.  Choices:   - `false` ← (default) - `true` |
| **wait_for_ip_address_timeout**  integer | Define a timeout (in seconds) for the wait_for_ip_address parameter.  Default: `300` |

## [Notes](vmware_guest_module.md#id3)

> **Note:**
>
> - Please make sure that the user used for [community.vmware.vmware_guest](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) has the correct level of privileges.
> - For example, following is the list of minimum privileges required by users to create virtual machines.
> - DataStore > Allocate Space
> - Virtual Machine > Configuration > Add New Disk
> - Virtual Machine > Configuration > Add or Remove Device
> - Virtual Machine > Inventory > Create New
> - Network > Assign Network
> - Resource > Assign Virtual Machine to Resource Pool
> - Module may require additional privileges as well, which may be required for gathering facts - e.g. ESXi configurations.
> - Use SCSI disks instead of IDE when you want to expand online disks by specifying a SCSI controller.
> - Uses SysPrep for Windows VM (depends on ‘guest_id’ parameter match ‘win’) with PyVmomi.
> - In order to change the VM’s parameters (e.g. number of CPUs), the VM must be powered off unless the hot-add support is enabled and the `state=present` must be used to apply the changes.
> - For additional information please visit Ansible VMware community wiki - <https://github.com/ansible/community/wiki/VMware>.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_module.md#id4)

```yaml+jinja
- name: Create a virtual machine on given ESXi hostname
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /DC1/vm/
    name: test_vm_0001
    state: poweredon
    guest_id: centos64Guest
    # This is hostname of particular ESXi server on which user wants VM to be deployed
    esxi_hostname: "{{ esxi_hostname }}"
    disk:
    - size_gb: 10
      type: thin
      datastore: datastore1
    hardware:
      memory_mb: 512
      num_cpus: 4
      scsi: paravirtual
    networks:
    - name: VM Network
      mac: aa:bb:dd:aa:00:14
      ip: 10.10.10.100
      netmask: 255.255.255.0
      device_type: vmxnet3
    wait_for_ip_address: true
    wait_for_ip_address_timeout: 600
  delegate_to: localhost
  register: deploy_vm

- name: Create a virtual machine from a template
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /testvms
    name: testvm_2
    state: poweredon
    template: template_el7
    disk:
    - size_gb: 10
      type: thin
      datastore: g73_datastore
    # Add another disk from an existing VMDK
    - filename: "[datastore1] testvms/testvm_2_1/testvm_2_1.vmdk"
    hardware:
      memory_mb: 512
      num_cpus: 6
      num_cpu_cores_per_socket: 3
      scsi: paravirtual
      memory_reservation_lock: True
      mem_limit: 8096
      mem_reservation: 4096
      cpu_limit: 8096
      cpu_reservation: 4096
      max_connections: 5
      hotadd_cpu: True
      hotremove_cpu: True
      hotadd_memory: False
      version: 12 # Hardware version of virtual machine
      boot_firmware: "efi"
    cdrom:
        - controller_number: 0
          unit_number: 0
          state: present
          type: iso
          iso_path: "[datastore1] livecd.iso"
    networks:
    - name: VM Network
      mac: aa:bb:dd:aa:00:14
    wait_for_ip_address: true
  delegate_to: localhost
  register: deploy

- name: Clone a virtual machine from Windows template and customize
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: datacenter1
    cluster: cluster
    name: testvm-2
    template: template_windows
    networks:
    - name: VM Network
      ip: 192.168.1.100
      netmask: 255.255.255.0
      gateway: 192.168.1.1
      mac: aa:bb:dd:aa:00:14
      domain: my_domain
      dns_servers:
      - 192.168.1.1
      - 192.168.1.2
    - vlan: 1234
      type: dhcp
    customization:
      autologon: true
      dns_servers:
      - 192.168.1.1
      - 192.168.1.2
      domain: my_domain
      password: new_vm_password
      runonce:
      - powershell.exe -ExecutionPolicy Unrestricted -File C:\Windows\Temp\ConfigureRemotingForAnsible.ps1 -ForceNewSSLCert -EnableCredSSP
  delegate_to: localhost

- name:  Clone a virtual machine from Linux template and customize
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    state: present
    folder: /DC1/vm
    template: "{{ template }}"
    name: "{{ vm_name }}"
    cluster: DC1_C1
    networks:
      - name: VM Network
        ip: 192.168.10.11
        netmask: 255.255.255.0
    wait_for_ip_address: True
    customization:
      domain: "{{ guest_domain }}"
      dns_servers:
        - 8.9.9.9
        - 7.8.8.9
      dns_suffix:
        - example.com
        - example2.com
  delegate_to: localhost

- name: Rename a virtual machine (requires the virtual machine's uuid)
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: "{{ vm_uuid }}"
    name: new_name
    state: present
  delegate_to: localhost

- name: Remove a virtual machine by uuid
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: "{{ vm_uuid }}"
    state: absent
  delegate_to: localhost

- name: Remove a virtual machine from inventory
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: vm_name
    delete_from_inventory: True
    state: absent
  delegate_to: localhost

- name: Manipulate vApp properties
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: vm_name
    state: present
    vapp_properties:
      - id: remoteIP
        category: Backup
        label: Backup server IP
        type: string
        value: 10.10.10.1
      - id: old_property
        operation: remove
  delegate_to: localhost

- name: Set powerstate of a virtual machine to poweroff by using UUID
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: "{{ vm_uuid }}"
    state: poweredoff
  delegate_to: localhost

- name: Deploy a virtual machine in a datastore different from the datastore of the template
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "{{ vm_name }}"
    state: present
    template: "{{ template_name }}"
    # Here datastore can be different which holds template
    datastore: "{{ virtual_machine_datastore }}"
    hardware:
      memory_mb: 512
      num_cpus: 2
      scsi: paravirtual
  delegate_to: localhost

- name: Create a diskless VM
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ dc1 }}"
    state: poweredoff
    cluster: "{{ ccr1 }}"
    name: diskless_vm
    folder: /Asia-Datacenter1/vm
    guest_id: centos64Guest
    datastore: "{{ ds1 }}"
    hardware:
        memory_mb: 1024
        num_cpus: 2
        num_cpu_cores_per_socket: 1

- name: Create a VM with multiple disks of different disk controller types
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /DC1/vm/
    name: test_vm_multi_disks
    state: poweredoff
    guest_id: centos64Guest
    datastore: datastore1
    disk:
    - size_gb: 10
      controller_type: 'nvme'
      controller_number: 0
      unit_number: 0
    - size_gb: 10
      controller_type: 'paravirtual'
      controller_number: 0
      unit_number: 1
    - size_gb: 10
      controller_type: 'sata'
      controller_number: 0
      unit_number: 2
    hardware:
      memory_mb: 512
      num_cpus: 4
      version: 14
    networks:
    - name: VM Network
      device_type: vmxnet3
  delegate_to: localhost
  register: deploy_vm

- name: Create a VM with NVDIMM device
  community.vmware.vmware_guest:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /DC1/vm/
    name: test_vm_nvdimm
    state: poweredoff
    guest_id: centos7_64Guest
    datastore: datastore1
    hardware:
      memory_mb: 512
      num_cpus: 4
      version: 14
    networks:
    - name: VM Network
      device_type: vmxnet3
    nvdimm:
      state: present
      size_mb: 2048
  delegate_to: localhost
  register: deploy_vm
```

## [Return Values](vmware_guest_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the new virtual machine  Returned: always  Sample: `"None"` |

### Authors

- Loic Blot (@nerzhul)
- Philippe Dellaert (@pdellaert)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
