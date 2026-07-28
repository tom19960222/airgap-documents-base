---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vm module – Creates a virtual machine."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vm_module.html
fetched_at: 2026-07-28T00:22:13+00:00
---
# vmware.vmware_rest.vcenter_vm module – Creates a virtual machine.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_module.md#synopsis)
- [Requirements](vcenter_vm_module.md#requirements)
- [Parameters](vcenter_vm_module.md#parameters)
- [Notes](vcenter_vm_module.md#notes)
- [Examples](vcenter_vm_module.md#examples)
- [Return Values](vcenter_vm_module.md#return-values)

## [Synopsis](vcenter_vm_module.md#id1)

- Creates a virtual machine.

## [Requirements](vcenter_vm_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bios_uuid**  string | 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in “12345678-abcd-1234-cdef-123456789abc” format. |
| **boot**  dictionary | Boot configuration.  Valid attributes are:  - `type` (str): The `type` defines the valid firmware types for a virtual machine. ([‘present’])    - Accepted values:      - BIOS     - EFI - `efi_legacy_boot` (bool): Flag indicating whether to use EFI legacy boot mode. ([‘present’]) - `network_protocol` (str): The `network_protocol` defines the valid network boot protocols supported when booting a virtual machine with [{@link](mailto:{%40link) Type#EFI} firmware over the network. ([‘present’])    - Accepted values:      - IPV4     - IPV6 - `delay` (int): Delay in milliseconds before beginning the firmware boot process when the virtual machine is powered on. This delay may be used to provide a time window for users to connect to the virtual machine console and enter BIOS setup mode. ([‘present’]) - `retry` (bool): Flag indicating whether the virtual machine should automatically retry the boot process after a failure. ([‘present’]) - `retry_delay` (int): Delay in milliseconds before retrying the boot process after a failure; applicable only when [{@link](mailto:{%40link) Info#retry} is true. ([‘present’]) - `enter_setup_mode` (bool): Flag indicating whether the firmware boot process should automatically enter setup mode the next time the virtual machine boots. Note that this flag will automatically be reset to false once the virtual machine enters setup mode. ([‘present’]) |
| **boot_devices**  list / elements=dictionary | Boot device configuration.  Valid attributes are:  - `type` (str): The `type` defines the valid device types that may be used as bootable devices. ([‘present’])  This key is required with [‘present’].    - Accepted values:      - CDROM     - DISK     - ETHERNET     - FLOPPY |
| **cdroms**  list / elements=dictionary | List of CD-ROMs.  Valid attributes are:  - `type` (str): The `host_bus_adapter_type` defines the valid types of host bus adapters that may be used for attaching a Cdrom to a virtual machine. ([‘present’])    - Accepted values:      - IDE     - SATA - `ide` (dict): Address for attaching the device to a virtual IDE adapter. ([‘present’])    - Accepted keys:      - primary (boolean): Flag specifying whether the device should be attached to the primary or secondary IDE adapter of the virtual machine.     - master (boolean): Flag specifying whether the device should be the master or slave device on the IDE adapter. - `sata` (dict): Address for attaching the device to a virtual SATA adapter. ([‘present’])    - Accepted keys:      - bus (integer): Bus number of the adapter to which the device should be attached.     - unit (integer): Unit number of the device. - `backing` (dict): Physical resource backing for the virtual CD-ROM device. ([‘present’])    - Accepted keys:      - type (string): The `backing_type` defines the valid backing types for a virtual CD-ROM device.  Accepted value for this field:  - `CLIENT_DEVICE` - `HOST_DEVICE` - `ISO_FILE`   - iso_file (string): Path of the image file that should be used as the virtual CD-ROM device backing. - host_device (string): Name of the device that should be used as the virtual CD-ROM device backing. - device_access_type (string): The `device_access_type` defines the valid device access types for a physical device packing of a virtual CD-ROM device.  Accepted value for this field:  - `EMULATION` - `PASSTHRU` - `PASSTHRU_EXCLUSIVE`   - `start_connected` (bool): Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on. ([‘present’]) - `allow_guest_control` (bool): Flag indicating whether the guest can connect and disconnect the device. ([‘present’]) |
| **cpu**  dictionary | CPU configuration.  Valid attributes are:  - `count` (int): New number of CPU cores. The number of CPU cores in the virtual machine must be a multiple of the number of cores per socket. The supported range of CPU counts is constrained by the configured guest operating system and virtual hardware version of the virtual machine. If the virtual machine is running, the number of CPU cores may only be increased if [{@link](mailto:{%40link) Info#hotAddEnabled} is true, and may only be decreased if [{@link](mailto:{%40link) Info#hotRemoveEnabled} is true. ([‘present’]) - `cores_per_socket` (int): New number of CPU cores per socket. The number of CPU cores in the virtual machine must be a multiple of the number of cores per socket. ([‘present’]) - `hot_add_enabled` (bool): Flag indicating whether adding CPUs while the virtual machine is running is enabled. This field may only be modified if the virtual machine is powered off. ([‘present’]) - `hot_remove_enabled` (bool): Flag indicating whether removing CPUs while the virtual machine is running is enabled. This field may only be modified if the virtual machine is powered off. ([‘present’]) |
| **datastore**  string | Identifier of the datastore on which the virtual machine’s configuration state is stored. |
| **datastore_path**  string | Datastore path for the virtual machine’s configuration file in the format “[datastore name] path”. For example “[storage1] Test-VM/Test-VM.vmx”. |
| **disconnect_all_nics**  boolean | Indicates whether all NICs on the destination virtual machine should be disconnected from the newtwork  Choices:   - `false` - `true` |
| **disks**  list / elements=dictionary | Individual disk relocation map.  Valid attributes are:  - `type` (str): The `host_bus_adapter_type` defines the valid types of host bus adapters that may be used for attaching a virtual storage device to a virtual machine. ([‘present’])    - Accepted values:      - IDE     - SATA     - SCSI - `ide` (dict): Address for attaching the device to a virtual IDE adapter. ([‘present’])    - Accepted keys:      - primary (boolean): Flag specifying whether the device should be attached to the primary or secondary IDE adapter of the virtual machine.     - master (boolean): Flag specifying whether the device should be the master or slave device on the IDE adapter. - `scsi` (dict): Address for attaching the device to a virtual SCSI adapter. ([‘present’])    - Accepted keys:      - bus (integer): Bus number of the adapter to which the device should be attached.     - unit (integer): Unit number of the device. - `sata` (dict): Address for attaching the device to a virtual SATA adapter. ([‘present’])    - Accepted keys:      - bus (integer): Bus number of the adapter to which the device should be attached.     - unit (integer): Unit number of the device. - `backing` (dict): Existing physical resource backing for the virtual disk. Exactly one of `#backing` or `#new_vmdk` must be specified. ([‘present’])    - Accepted keys:      - type (string): The `backing_type` defines the valid backing types for a virtual disk.  Accepted value for this field:  - `VMDK_FILE`   - vmdk_file (string): Path of the VMDK file backing the virtual disk.   - `new_vmdk` (dict): Specification for creating a new VMDK backing for the virtual disk. Exactly one of `#backing` or `#new_vmdk` must be specified. ([‘present’])    - Accepted keys:      - name (string): Base name of the VMDK file. The name should not include the ‘.vmdk’ file extension.     - capacity (integer): Capacity of the virtual disk backing in bytes.     - storage_policy (object): The `storage_policy_spec` [{@term](mailto:{%40term) structure} contains information about the storage policy that is to be associated the with VMDK file. |
| **disks_to_remove**  list / elements=string | Set of Disks to Remove. |
| **disks_to_update**  dictionary | Map of Disks to Update. |
| **floppies**  list / elements=dictionary | List of floppy drives.  Valid attributes are:  - `backing` (dict): Physical resource backing for the virtual floppy drive. ([‘present’])    - Accepted keys:      - type (string): The `backing_type` defines the valid backing types for a virtual floppy drive.  Accepted value for this field:  - `CLIENT_DEVICE` - `HOST_DEVICE` - `IMAGE_FILE`   - image_file (string): Path of the image file that should be used as the virtual floppy drive backing. - host_device (string): Name of the device that should be used as the virtual floppy drive backing.   - `start_connected` (bool): Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on. ([‘present’]) - `allow_guest_control` (bool): Flag indicating whether the guest can connect and disconnect the device. ([‘present’]) |
| **guest_customization_spec**  dictionary | Guest customization spec to apply to the virtual machine after the virtual machine is deployed.  Valid attributes are:  - `name` (str): Name of the customization specification. ([‘clone’]) |
| **guest_OS**  string | The `guest_o_s` defines the valid guest operating system types used for configuring a virtual machine. Required with *state=[‘present’]*  Choices:   - `"AMAZONLINUX2_64"` - `"AMAZONLINUX3_64"` - `"ASIANUX_3"` - `"ASIANUX_3_64"` - `"ASIANUX_4"` - `"ASIANUX_4_64"` - `"ASIANUX_5_64"` - `"ASIANUX_7_64"` - `"ASIANUX_8_64"` - `"ASIANUX_9_64"` - `"CENTOS"` - `"CENTOS_6"` - `"CENTOS_64"` - `"CENTOS_6_64"` - `"CENTOS_7"` - `"CENTOS_7_64"` - `"CENTOS_8_64"` - `"CENTOS_9_64"` - `"COREOS_64"` - `"CRXPOD_1"` - `"DARWIN"` - `"DARWIN_10"` - `"DARWIN_10_64"` - `"DARWIN_11"` - `"DARWIN_11_64"` - `"DARWIN_12_64"` - `"DARWIN_13_64"` - `"DARWIN_14_64"` - `"DARWIN_15_64"` - `"DARWIN_16_64"` - `"DARWIN_17_64"` - `"DARWIN_18_64"` - `"DARWIN_19_64"` - `"DARWIN_20_64"` - `"DARWIN_21_64"` - `"DARWIN_64"` - `"DEBIAN_10"` - `"DEBIAN_10_64"` - `"DEBIAN_11"` - `"DEBIAN_11_64"` - `"DEBIAN_4"` - `"DEBIAN_4_64"` - `"DEBIAN_5"` - `"DEBIAN_5_64"` - `"DEBIAN_6"` - `"DEBIAN_6_64"` - `"DEBIAN_7"` - `"DEBIAN_7_64"` - `"DEBIAN_8"` - `"DEBIAN_8_64"` - `"DEBIAN_9"` - `"DEBIAN_9_64"` - `"DOS"` - `"ECOMSTATION"` - `"ECOMSTATION_2"` - `"FEDORA"` - `"FEDORA_64"` - `"FREEBSD"` - `"FREEBSD_11"` - `"FREEBSD_11_64"` - `"FREEBSD_12"` - `"FREEBSD_12_64"` - `"FREEBSD_13"` - `"FREEBSD_13_64"` - `"FREEBSD_64"` - `"GENERIC_LINUX"` - `"MANDRAKE"` - `"MANDRIVA"` - `"MANDRIVA_64"` - `"NETWARE_4"` - `"NETWARE_5"` - `"NETWARE_6"` - `"NLD_9"` - `"OES"` - `"OPENSERVER_5"` - `"OPENSERVER_6"` - `"OPENSUSE"` - `"OPENSUSE_64"` - `"ORACLE_LINUX"` - `"ORACLE_LINUX_6"` - `"ORACLE_LINUX_64"` - `"ORACLE_LINUX_6_64"` - `"ORACLE_LINUX_7"` - `"ORACLE_LINUX_7_64"` - `"ORACLE_LINUX_8_64"` - `"ORACLE_LINUX_9_64"` - `"OS2"` - `"OTHER"` - `"OTHER_24X_LINUX"` - `"OTHER_24X_LINUX_64"` - `"OTHER_26X_LINUX"` - `"OTHER_26X_LINUX_64"` - `"OTHER_3X_LINUX"` - `"OTHER_3X_LINUX_64"` - `"OTHER_4X_LINUX"` - `"OTHER_4X_LINUX_64"` - `"OTHER_5X_LINUX"` - `"OTHER_5X_LINUX_64"` - `"OTHER_64"` - `"OTHER_LINUX"` - `"OTHER_LINUX_64"` - `"REDHAT"` - `"RHEL_2"` - `"RHEL_3"` - `"RHEL_3_64"` - `"RHEL_4"` - `"RHEL_4_64"` - `"RHEL_5"` - `"RHEL_5_64"` - `"RHEL_6"` - `"RHEL_6_64"` - `"RHEL_7"` - `"RHEL_7_64"` - `"RHEL_8_64"` - `"RHEL_9_64"` - `"SJDS"` - `"SLES"` - `"SLES_10"` - `"SLES_10_64"` - `"SLES_11"` - `"SLES_11_64"` - `"SLES_12"` - `"SLES_12_64"` - `"SLES_15_64"` - `"SLES_16_64"` - `"SLES_64"` - `"SOLARIS_10"` - `"SOLARIS_10_64"` - `"SOLARIS_11_64"` - `"SOLARIS_6"` - `"SOLARIS_7"` - `"SOLARIS_8"` - `"SOLARIS_9"` - `"SUSE"` - `"SUSE_64"` - `"TURBO_LINUX"` - `"TURBO_LINUX_64"` - `"UBUNTU"` - `"UBUNTU_64"` - `"UNIXWARE_7"` - `"VMKERNEL"` - `"VMKERNEL_5"` - `"VMKERNEL_6"` - `"VMKERNEL_65"` - `"VMKERNEL_7"` - `"VMWARE_PHOTON_64"` - `"WINDOWS_7"` - `"WINDOWS_7_64"` - `"WINDOWS_7_SERVER_64"` - `"WINDOWS_8"` - `"WINDOWS_8_64"` - `"WINDOWS_8_SERVER_64"` - `"WINDOWS_9"` - `"WINDOWS_9_64"` - `"WINDOWS_9_SERVER_64"` - `"WINDOWS_HYPERV"` - `"WINDOWS_SERVER_2019"` - `"WINDOWS_SERVER_2021"` - `"WIN_2000_ADV_SERV"` - `"WIN_2000_PRO"` - `"WIN_2000_SERV"` - `"WIN_31"` - `"WIN_95"` - `"WIN_98"` - `"WIN_LONGHORN"` - `"WIN_LONGHORN_64"` - `"WIN_ME"` - `"WIN_NET_BUSINESS"` - `"WIN_NET_DATACENTER"` - `"WIN_NET_DATACENTER_64"` - `"WIN_NET_ENTERPRISE"` - `"WIN_NET_ENTERPRISE_64"` - `"WIN_NET_STANDARD"` - `"WIN_NET_STANDARD_64"` - `"WIN_NET_WEB"` - `"WIN_NT"` - `"WIN_VISTA"` - `"WIN_VISTA_64"` - `"WIN_XP_HOME"` - `"WIN_XP_PRO"` - `"WIN_XP_PRO_64"` |
| **hardware_version**  string | The `version` defines the valid virtual hardware versions for a virtual machine. See <https://kb.vmware.com/s/article/1003746> (Virtual machine hardware versions (1003746)).  Choices:   - `"VMX_03"` - `"VMX_04"` - `"VMX_06"` - `"VMX_07"` - `"VMX_08"` - `"VMX_09"` - `"VMX_10"` - `"VMX_11"` - `"VMX_12"` - `"VMX_13"` - `"VMX_14"` - `"VMX_15"` - `"VMX_16"` - `"VMX_17"` - `"VMX_18"` - `"VMX_19"` |
| **memory**  dictionary | Memory configuration.  Valid attributes are:  - `size_MiB` (int): New memory size in mebibytes. The supported range of memory sizes is constrained by the configured guest operating system and virtual hardware version of the virtual machine. If the virtual machine is running, this value may only be changed if [{@link](mailto:{%40link) Info#hotAddEnabled} is true, and the new memory size must satisfy the constraints specified by [{@link](mailto:{%40link) Info#hotAddIncrementSizeMiB} and [{@link](mailto:{%40link) Info#hotAddLimitMiB}. ([‘present’]) - `hot_add_enabled` (bool): Flag indicating whether adding memory while the virtual machine is running should be enabled. Some guest operating systems may consume more resources or perform less efficiently when they run on hardware that supports adding memory while the machine is running. This field may only be modified if the virtual machine is not powered on. ([‘present’]) |
| **name**  string | Name of the new virtual machine. |
| **nics**  list / elements=dictionary | List of Ethernet adapters.  Valid attributes are:  - `type` (str): The `emulation_type` defines the valid emulation types for a virtual Ethernet adapter. ([‘present’])    - Accepted values:      - E1000     - E1000E     - PCNET32     - VMXNET     - VMXNET2     - VMXNET3 - `upt_compatibility_enabled` (bool): Flag indicating whether Universal Pass-Through (UPT) compatibility is enabled on this virtual Ethernet adapter. ([‘present’]) - `mac_type` (str): The `mac_address_type` defines the valid MAC address origins for a virtual Ethernet adapter. ([‘present’])    - Accepted values:      - ASSIGNED     - GENERATED     - MANUAL - `mac_address` (str): MAC address. ([‘present’]) - `pci_slot_number` (int): Address of the virtual Ethernet adapter on the PCI bus. If the PCI address is invalid, the server will change when it the VM is started or as the device is hot added. ([‘present’]) - `wake_on_lan_enabled` (bool): Flag indicating whether wake-on-LAN is enabled on this virtual Ethernet adapter. ([‘present’]) - `backing` (dict): Physical resource backing for the virtual Ethernet adapter. ([‘present’])    - Accepted keys:      - type (string): The `backing_type` defines the valid backing types for a virtual Ethernet adapter.  Accepted value for this field:  - `DISTRIBUTED_PORTGROUP` - `HOST_DEVICE` - `OPAQUE_NETWORK` - `STANDARD_PORTGROUP`   - network (string): Identifier of the network that backs the virtual Ethernet adapter. - distributed_port (string): Key of the distributed virtual port that backs the virtual Ethernet adapter. Depending on the type of the Portgroup, the port may be specified using this field. If the portgroup type is early-binding (also known as static), a port is assigned when the Ethernet adapter is configured to use the port. The port may be either automatically or specifically assigned based on the value of this field. If the portgroup type is ephemeral, the port is created and assigned to a virtual machine when it is powered on and the Ethernet adapter is connected. This field cannot be specified as no free ports exist before use.   - `start_connected` (bool): Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on. ([‘present’]) - `allow_guest_control` (bool): Flag indicating whether the guest can connect and disconnect the device. ([‘present’]) |
| **nics_to_update**  dictionary | Map of NICs to update. |
| **parallel_ports**  list / elements=dictionary | List of parallel ports.  Valid attributes are:  - `backing` (dict): Physical resource backing for the virtual parallel port. ([‘present’])    - Accepted keys:      - type (string): The `backing_type` defines the valid backing types for a virtual parallel port.  Accepted value for this field:  - `FILE` - `HOST_DEVICE`   - file (string): Path of the file that should be used as the virtual parallel port backing. - host_device (string): Name of the device that should be used as the virtual parallel port backing.   - `start_connected` (bool): Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on. ([‘present’]) - `allow_guest_control` (bool): Flag indicating whether the guest can connect and disconnect the device. ([‘present’]) |
| **parallel_ports_to_update**  dictionary | Map of parallel ports to Update. |
| **path**  string | Path to the virtual machine’s configuration file on the datastore corresponding to [{@link](mailto:{%40link) #datastore). |
| **placement**  dictionary | Virtual machine placement information.  Valid attributes are:  - `folder` (str): Virtual machine folder into which the virtual machine should be placed. ([‘clone’, ‘instant_clone’, ‘present’, ‘register’, ‘relocate’]) - `resource_pool` (str): Resource pool into which the virtual machine should be placed. ([‘clone’, ‘instant_clone’, ‘present’, ‘register’, ‘relocate’]) - `host` (str): Host onto which the virtual machine should be placed. If `#host` and `#resource_pool` are both specified, `#resource_pool` must belong to `#host`. If `#host` and `#cluster` are both specified, `#host` must be a member of `#cluster`. ([‘clone’, ‘present’, ‘register’, ‘relocate’]) - `cluster` (str): Cluster into which the virtual machine should be placed. If `#cluster` and `#resource_pool` are both specified, `#resource_pool` must belong to `#cluster`. If `#cluster` and `#host` are both specified, `#host` must be a member of `#cluster`. ([‘clone’, ‘present’, ‘register’, ‘relocate’]) - `datastore` (str): Datastore on which the virtual machine’s configuration state should be stored. This datastore will also be used for any virtual disks that are associated with the virtual machine, unless individually overridden. ([‘clone’, ‘instant_clone’, ‘present’, ‘relocate’]) |
| **power_on**  boolean | Attempt to perform a [{@link](mailto:{%40link) #powerOn} after clone.  Choices:   - `false` - `true` |
| **sata_adapters**  list / elements=dictionary | List of SATA adapters.  Valid attributes are:  - `type` (str): The `type` defines the valid emulation types for a virtual SATA adapter. ([‘present’])    - Accepted values:      - AHCI - `bus` (int): SATA bus number. ([‘present’]) - `pci_slot_number` (int): Address of the SATA adapter on the PCI bus. ([‘present’]) |
| **scsi_adapters**  list / elements=dictionary | List of SCSI adapters.  Valid attributes are:  - `type` (str): The `type` defines the valid emulation types for a virtual SCSI adapter. ([‘present’])    - Accepted values:      - BUSLOGIC     - LSILOGIC     - LSILOGICSAS     - PVSCSI - `bus` (int): SCSI bus number. ([‘present’]) - `pci_slot_number` (int): Address of the SCSI adapter on the PCI bus. If the PCI address is invalid, the server will change it when the VM is started or as the device is hot added. ([‘present’]) - `sharing` (str): The `sharing` defines the valid bus sharing modes for a virtual SCSI adapter. ([‘present’])    - Accepted values:      - NONE     - PHYSICAL     - VIRTUAL |
| **serial_ports**  list / elements=dictionary | List of serial ports.  Valid attributes are:  - `yield_on_poll` (bool): CPU yield behavior. If set to true, the virtual machine will periodically relinquish the processor if its sole task is polling the virtual serial port. The amount of time it takes to regain the processor will depend on the degree of other virtual machine activity on the host. ([‘present’]) - `backing` (dict): Physical resource backing for the virtual serial port. ([‘present’])    - Accepted keys:      - type (string): The `backing_type` defines the valid backing types for a virtual serial port.  Accepted value for this field:  - `FILE` - `HOST_DEVICE` - `NETWORK_CLIENT` - `NETWORK_SERVER` - `PIPE_CLIENT` - `PIPE_SERVER`   - file (string): Path of the file backing the virtual serial port. - host_device (string): Name of the device backing the virtual serial port. <p> - pipe (string): Name of the pipe backing the virtual serial port. - no_rx_loss (boolean): Flag that enables optimized data transfer over the pipe. When the value is true, the host buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss. - network_location (string): URI specifying the location of the network service backing the virtual serial port. <ul> <li>If [{@link](mailto:{%40link) #type} is [{@link](mailto:{%40link) BackingType#NETWORK_SERVER}, this field is the location used by clients to connect to this server. The hostname part of the URI should either be empty or should specify the address of the host on which the virtual machine is running.</li> <li>If [{@link](mailto:{%40link) #type} is [{@link](mailto:{%40link) BackingType#NETWORK_CLIENT}, this field is the location used by the virtual machine to connect to the remote server.</li> </ul> - proxy (string): Proxy service that provides network access to the network backing. If set, the virtual machine initiates a connection with the proxy service and forwards the traffic to the proxy.   - `start_connected` (bool): Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on. ([‘present’]) - `allow_guest_control` (bool): Flag indicating whether the guest can connect and disconnect the device. ([‘present’]) |
| **serial_ports_to_update**  dictionary | Map of serial ports to Update. |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **source**  string | Virtual machine to InstantClone from. Required with *state=[‘clone’, ‘instant_clone’]* |
| **state**  string | Choices:   - `"absent"` - `"clone"` - `"instant_clone"` - `"present"` ← (default) - `"register"` - `"relocate"` - `"unregister"` |
| **storage_policy**  dictionary | The `storage_policy_spec` [{@term](mailto:{%40term) structure} contains information about the storage policy that is to be associated with the virtual machine home (which contains the configuration and log files). Required with *state=[‘present’]*  Valid attributes are:  - `policy` (str): Identifier of the storage policy which should be associated with the virtual machine. ([‘present’])  This key is required with [‘present’]. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm**  string | Identifier of the virtual machine to be unregistered. Required with *state=[‘absent’, ‘relocate’, ‘unregister’]* |

## [Notes](vcenter_vm_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_module.md#id5)

```yaml+jinja
- name: Build a list of all the clusters
  vmware.vmware_rest.vcenter_cluster_info:
  register: all_the_clusters

- name: Retrieve details about the first cluster
  vmware.vmware_rest.vcenter_cluster_info:
    cluster: '{{ all_the_clusters.value[0].cluster }}'
  register: my_cluster_info

- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: '{{ my_cluster_info.id }}'
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: '{{ my_virtual_machine_folder.folder }}'
      resource_pool: '{{ my_cluster_info.value.resource_pool }}'
    name: test_vm1
    guest_OS: DEBIAN_7_64
    hardware_version: VMX_10
    memory:
      hot_add_enabled: true
      size_MiB: 1024
  register: my_vm

- name: Collect the list of the existing VM
  vmware.vmware_rest.vcenter_vm_info:
  register: existing_vms
  until: existing_vms is not failed

- name: Delete some VM
  vmware.vmware_rest.vcenter_vm:
    state: absent
    vm: '{{ item.vm }}'
  with_items: '{{ existing_vms.value }}'
  when:
  - not item.name.startswith("vCLS")

- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
    disks:
    - type: SATA
      backing:
        type: VMDK_FILE
        vmdk_file: '[local] test_vm1/{{ disk_name }}.vmdk'
    - type: SATA
      new_vmdk:
        name: second_disk
        capacity: 32000000000
    cdroms:
    - type: SATA
      sata:
        bus: 0
        unit: 2
    nics:
    - backing:
        type: STANDARD_PORTGROUP
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM\
          \ Network') }}"

  register: my_vm

- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    name: test_vm1
    guest_OS: DEBIAN_8_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
  register: my_vm

- name: Create a content library based on a DataStore
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_datastore
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      type: DATASTORE
    state: present
  register: ds_lib

- name: Create a VM template on the library
  vmware.vmware_rest.vcenter_vmtemplate_libraryitems:
    name: foobar2001
    library: '{{ ds_lib.id }}'
    source_vm: '{{ my_vm.id }}'
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
  register: mylib_item

- name: Deploy a new VM based on the template
  vmware.vmware_rest.vcenter_vmtemplate_libraryitems:
    name: foobar2002
    library: '{{ ds_lib.id }}'
    template_library_item: '{{ mylib_item.id }}'
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    state: deploy
  register: my_new_vm

- name: Retrieve all the details about the new VM
  vmware.vmware_rest.vcenter_vm:
    vm: '{{ my_new_vm.value }}'
  register: my_new_vm_info

- name: Create an instant clone of a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    source: '{{ my_vm.id }}'
    name: test_vm2
    state: instant_clone
  register: my_instant_clone

- name: Create a clone of a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local')\
        \ }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources')\
        \ }}"
    source: '{{ my_vm.id }}'
    name: test_vm3
    state: clone
  register: my_clone_vm
```

## [Return Values](vcenter_vm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Delete some VM  Returned: On success  Sample: `"All items completed"` |
| **results**  list / elements=string | Delete some VM  Returned: On success  Sample: `[{"_ansible_item_label": {"cpu_count": 1, "memory_size_MiB": 128, "name": "vCLS-a3e9f505-69fc-43d0-beed-c1a43d06184e", "power_state": "POWERED_OFF", "vm": "vm-1130"}, "_ansible_no_log": 0, "ansible_loop_var": "item", "changed": 0, "item": {"cpu_count": 1, "memory_size_MiB": 128, "name": "vCLS-a3e9f505-69fc-43d0-beed-c1a43d06184e", "power_state": "POWERED_OFF", "vm": "vm-1130"}, "skip_reason": "Conditional result was False", "skipped": 1}, {"_ansible_item_label": {"cpu_count": 1, "memory_size_MiB": 1024, "name": "test_vm1", "power_state": "POWERED_OFF", "vm": "vm-1131"}, "_ansible_no_log": null, "ansible_loop_var": "item", "changed": 1, "failed": 0, "invocation": {"module_args": {"bios_uuid": null, "boot": null, "boot_devices": null, "cdroms": null, "cpu": null, "datastore": null, "datastore_path": null, "disconnect_all_nics": null, "disks": null, "disks_to_remove": null, "disks_to_update": null, "floppies": null, "guest_OS": null, "guest_customization_spec": null, "hardware_version": null, "memory": null, "name": null, "nics": null, "nics_to_update": null, "parallel_ports": null, "parallel_ports_to_update": null, "path": null, "placement": null, "power_on": null, "sata_adapters": null, "scsi_adapters": null, "serial_ports": null, "serial_ports_to_update": null, "session_timeout": null, "source": null, "state": "absent", "storage_policy": null, "vcenter_hostname": "vcenter.test", "vcenter_password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "vcenter_rest_log_file": null, "vcenter_username": "administrator@vsphere.local", "vcenter_validate_certs": 0, "vm": "vm-1131"}}, "item": {"cpu_count": 1, "memory_size_MiB": 1024, "name": "test_vm1", "power_state": "POWERED_OFF", "vm": "vm-1131"}, "value": {}}, {"_ansible_item_label": {"cpu_count": 1, "memory_size_MiB": 1024, "name": "foobar2002", "power_state": "POWERED_OFF", "vm": "vm-1134"}, "_ansible_no_log": null, "ansible_loop_var": "item", "changed": 1, "failed": 0, "invocation": {"module_args": {"bios_uuid": null, "boot": null, "boot_devices": null, "cdroms": null, "cpu": null, "datastore": null, "datastore_path": null, "disconnect_all_nics": null, "disks": null, "disks_to_remove": null, "disks_to_update": null, "floppies": null, "guest_OS": null, "guest_customization_spec": null, "hardware_version": null, "memory": null, "name": null, "nics": null, "nics_to_update": null, "parallel_ports": null, "parallel_ports_to_update": null, "path": null, "placement": null, "power_on": null, "sata_adapters": null, "scsi_adapters": null, "serial_ports": null, "serial_ports_to_update": null, "session_timeout": null, "source": null, "state": "absent", "storage_policy": null, "vcenter_hostname": "vcenter.test", "vcenter_password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "vcenter_rest_log_file": null, "vcenter_username": "administrator@vsphere.local", "vcenter_validate_certs": 0, "vm": "vm-1134"}}, "item": {"cpu_count": 1, "memory_size_MiB": 1024, "name": "foobar2002", "power_state": "POWERED_OFF", "vm": "vm-1134"}, "value": {}}]` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
