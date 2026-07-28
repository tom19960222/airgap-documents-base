---
collection: ansible
version: "8"
title: "community.general.proxmox_kvm module – Management of Qemu(KVM) Virtual Machines in Proxmox VE cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_kvm_module.html
fetched_at: 2026-07-28T01:49:19+00:00
---
# community.general.proxmox_kvm module – Management of Qemu(KVM) Virtual Machines in Proxmox VE cluster

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
> see [Requirements](proxmox_kvm_module.md#ansible-collections-community-general-proxmox-kvm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_kvm`.

- [Synopsis](proxmox_kvm_module.md#synopsis)
- [Requirements](proxmox_kvm_module.md#requirements)
- [Parameters](proxmox_kvm_module.md#parameters)
- [Attributes](proxmox_kvm_module.md#attributes)
- [See Also](proxmox_kvm_module.md#see-also)
- [Examples](proxmox_kvm_module.md#examples)
- [Return Values](proxmox_kvm_module.md#return-values)

## [Synopsis](proxmox_kvm_module.md#id1)

- Allows you to create/delete/stop Qemu(KVM) Virtual Machines in Proxmox VE cluster.
- Since community.general 4.0.0 on, there are no more default values, see `proxmox_default_behavior`.

Aliases: cloud.misc.proxmox_kvm

## [Requirements](proxmox_kvm_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_kvm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acpi**  boolean | Specify if ACPI should be enabled/disabled.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `true`.  **Choices:**   - `false` - `true` |
| **agent**  string | Specify if the QEMU Guest Agent should be enabled/disabled.  Since community.general 5.5.0, this can also be a string instead of a boolean. This allows to specify values such as `enabled=1,fstrim_cloned_disks=1`. |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **archive**  string  *added in community.general 6.5.0* | Specify a path to an archive to restore (instead of creating or cloning a VM). |
| **args**  string | Pass arbitrary arguments to kvm.  This option is for experts only!  If `proxmox_default_behavior` is set to `compatibility`, this option has a default of `-serial unix:/var/run/qemu-server/<vmid>.serial,server,nowait`. |
| **autostart**  boolean | Specify if the VM should be automatically restarted after crash (currently ignored in PVE API).  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `false`.  **Choices:**   - `false` - `true` |
| **balloon**  integer | Specify the amount of RAM for the VM in MB.  Using zero disables the balloon driver.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `0`. |
| **bios**  string | Specify the BIOS implementation.  **Choices:**   - `"seabios"` - `"ovmf"` |
| **boot**  string | Specify the boot order -> boot on floppy `a`, hard disk `c`, CD-ROM `d`, or network `n`.  For newer versions of Proxmox VE, use a boot order like `order=scsi0;net0;hostpci0`.  You can combine to set order.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `cnd`. |
| **bootdisk**  string | Enable booting from specified disk. Format `(ide|sata|scsi|virtio)\d+`. |
| **cicustom**  string  *added in community.general 1.3.0* | cloud-init: Specify custom files to replace the automatically generated ones at start. |
| **cipassword**  string  *added in community.general 1.3.0* | cloud-init: password of default user to create. |
| **citype**  string  *added in community.general 1.3.0* | cloud-init: Specifies the cloud-init configuration format.  The default depends on the configured operating system type (`ostype`).  We use the `nocloud` format for Linux, and `configdrive2` for Windows.  **Choices:**   - `"nocloud"` - `"configdrive2"` |
| **ciuser**  string  *added in community.general 1.3.0* | cloud-init: username of default user to create. |
| **clone**  string | Name of VM to be cloned. If `vmid` is set, `clone` can take an arbitrary value but is required for initiating the clone. |
| **cores**  integer | Specify number of cores per socket.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `1`. |
| **cpu**  string | Specify emulated CPU type.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `kvm64`. |
| **cpulimit**  integer | Specify if CPU usage will be limited. Value 0 indicates no CPU limit.  If the computer has 2 CPUs, it has total of ‘2’ CPU time |
| **cpuunits**  integer | Specify CPU weight for a VM.  You can disable fair-scheduler configuration by setting this to 0  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `1000`. |
| **delete**  string | Specify a list of settings you want to delete. |
| **description**  string | Specify the description for the VM. Only used on the configuration web interface.  This is saved as comment inside the configuration file. |
| **digest**  string | Specify if to prevent changes if current configuration file has different SHA1 digest.  This can be used to prevent concurrent modifications. |
| **efidisk0**  dictionary  *added in community.general 4.5.0* | Specify a hash/dictionary of EFI disk options.  Requires `bios=ovmf` to be set to be able to use it. |
| **efitype**  string | `efitype` indicates the size of the EFI disk.  `2m` will allow for a 2MB EFI disk, which will be enough to persist boot order and new boot entries.  `4m` will allow for a 4MB EFI disk, which will additionally allow to store EFI keys in order to enable Secure Boot  **Choices:**   - `"2m"` - `"4m"` |
| **format**  string | `format` is the drive’s backing file’s data format. Please refer to the Proxmox VE Administrator Guide, section Proxmox VE Storage (see <https://pve.proxmox.com/pve-docs/chapter-pvesm.html> for the latest version, tables 3 to 14) to find out format supported by the provided storage backend. |
| **pre_enrolled_keys**  boolean | `pre_enrolled_keys` indicates whether EFI keys for Secure Boot should be enrolled `1` in the VM firmware upon creation or not (0).  If set to `1`, Secure Boot will also be enabled by default when the VM is created.  **Choices:**   - `false` - `true` |
| **storage**  string | `storage` is the storage identifier where to create the disk. |
| **force**  boolean | Allow to force stop VM.  Can be used with states `stopped`, `restarted`, and `absent`.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `false`.  **Choices:**   - `false` - `true` |
| **format**  string | Target drive’s backing file’s data format.  Used only with clone  Use `format=unspecified` and `full=false` for a linked clone.  Please refer to the Proxmox VE Administrator Guide, section Proxmox VE Storage (see <https://pve.proxmox.com/pve-docs/chapter-pvesm.html> for the latest version, tables 3 to 14) to find out format supported by the provided storage backend.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `qcow2`. If `proxmox_default_behavior` is set to `no_defaults`, not specifying this option is equivalent to setting it to `unspecified`.  **Choices:**   - `"cloop"` - `"cow"` - `"qcow"` - `"qcow2"` - `"qed"` - `"raw"` - `"vmdk"` - `"unspecified"` |
| **freeze**  boolean | Specify if PVE should freeze CPU at startup (use ‘c’ monitor command to start execution).  **Choices:**   - `false` - `true` |
| **full**  boolean | Create a full copy of all disk. This is always done when you clone a normal VM.  For VM templates, we try to create a linked clone by default.  Used only with clone  **Choices:**   - `false` - `true` ← (default) |
| **hostpci**  dictionary | Specify a hash/dictionary of map host pci devices into guest. `hostpci='{"key":"value", "key":"value"}'`.  Keys allowed are - `hostpci[n]` where 0 ≤ n ≤ N.  Values allowed are - `"host="HOSTPCIID[;HOSTPCIID2...]",pcie="1|0",rombar="1|0",x-vga="1|0""`.  The `host` parameter is Host PCI device pass through. HOSTPCIID syntax is `bus:dev.func` (hexadecimal numbers).  `pcie=boolean` `default=0` Choose the PCI-express bus (needs the q35 machine model).  `rombar=boolean` `default=1` Specify whether or not the device’s ROM will be visible in the guest’s memory map.  `x-vga=boolean` `default=0` Enable vfio-vga device support.  /!\ This option allows direct access to host hardware. So it is no longer possible to migrate such machines - use with special care. |
| **hotplug**  string | Selectively enable hotplug features.  This is a comma separated list of hotplug features `network`, `disk`, `cpu`, `memory`, and `usb`.  Value 0 disables hotplug completely and value 1 is an alias for the default `network,disk,usb`. |
| **hugepages**  string | Enable/disable hugepages memory.  **Choices:**   - `"any"` - `"2"` - `"1024"` |
| **ide**  dictionary | A hash/dictionary of volume used as IDE hard disk or CD-ROM. `ide='{"key":"value", "key":"value"}'`.  Keys allowed are - `ide[n]` where 0 ≤ n ≤ 3.  Values allowed are - `"storage:size,format=value"`.  `storage` is the storage identifier where to create the disk.  `size` is the size of the disk in GB.  `format` is the drive’s backing file’s data format. `qcow2|raw|subvol`. Please refer to the Proxmox VE Administrator Guide, section Proxmox VE Storage (see <https://pve.proxmox.com/pve-docs/chapter-pvesm.html> for the latest version, tables 3 to 14) to find out format supported by the provided storage backend. |
| **ipconfig**  dictionary  *added in community.general 1.3.0* | cloud-init: Set the IP configuration.  A hash/dictionary of network ip configurations. `ipconfig='{"key":"value", "key":"value"}'`.  Keys allowed are - `ipconfig[n]` where 0 ≤ n ≤ network interfaces.  Values allowed are - `"[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]"`.  cloud-init: Specify IP addresses and gateways for the corresponding interface.  IP addresses use CIDR notation, gateways are optional but they should be in the same subnet of specified IP address.  The special string ‘dhcp’ can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided.  For IPv6 the special string ‘auto’ can be used to use stateless autoconfiguration.  If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4. |
| **keyboard**  string | Sets the keyboard layout for VNC server. |
| **kvm**  boolean | Enable/disable KVM hardware virtualization.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `true`.  **Choices:**   - `false` - `true` |
| **localtime**  boolean | Sets the real time clock to local time.  This is enabled by default if ostype indicates a Microsoft OS.  **Choices:**   - `false` - `true` |
| **lock**  string | Lock/unlock the VM.  **Choices:**   - `"migrate"` - `"backup"` - `"snapshot"` - `"rollback"` |
| **machine**  string | Specifies the Qemu machine type.  Type => `(pc|pc(-i440fx)?-\d+\.\d+(\.pxe)?|q35|pc-q35-\d+\.\d+(\.pxe)?)`. |
| **memory**  integer | Memory size in MB for instance.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `512`. |
| **migrate**  boolean  *added in community.general 7.0.0* | Migrate the VM to `node` if it is on another node.  **Choices:**   - `false` ← (default) - `true` |
| **migrate_downtime**  integer | Sets maximum tolerated downtime (in seconds) for migrations. |
| **migrate_speed**  integer | Sets maximum speed (in MB/s) for migrations.  A value of 0 is no limit. |
| **name**  string | Specifies the VM name. Name could be non-unique across the cluster.  Required only for `state=present`.  With `state=present` if `vmid` not provided and VM with name exists in the cluster then no changes will be made. |
| **nameservers**  list / elements=string  *added in community.general 1.3.0* | cloud-init: DNS server IP address(es).  If unset, PVE host settings are used. |
| **net**  dictionary | A hash/dictionary of network interfaces for the VM. `net='{"key":"value", "key":"value"}'`.  Keys allowed are - `net[n]` where 0 ≤ n ≤ N.  Values allowed are - `"model="XX:XX:XX:XX:XX:XX",bridge="value",rate="value",tag="value",firewall="1|0",trunks="vlanid""`.  Model is one of `e1000 e1000-82540em e1000-82544gc e1000-82545em i82551 i82557b i82559er ne2k_isa ne2k_pci pcnet rtl8139 virtio vmxnet3`.  `XX:XX:XX:XX:XX:XX` should be an unique MAC address. This is automatically generated if not specified.  The `bridge` parameter can be used to automatically add the interface to a bridge device. The Proxmox VE standard bridge is called ‘vmbr0’.  Option `rate` is used to limit traffic bandwidth from and to this interface. It is specified as floating point number, unit is ‘Megabytes per second’.  If you specify no bridge, we create a kvm ‘user’ (NATed) network device, which provides DHCP and DNS services. |
| **newid**  integer | VMID for the clone. Used only with clone.  If newid is not set, the next available VM ID will be fetched from ProxmoxAPI. |
| **node**  string | Proxmox VE node on which to operate.  Only required for `state=present`.  For every other states it will be autodiscovered. |
| **numa**  dictionary | A hash/dictionaries of NUMA topology. `numa='{"key":"value", "key":"value"}'`.  Keys allowed are - `numa[n]` where 0 ≤ n ≤ N.  Values allowed are - `"cpu="<id[-id];...>",hostnodes="<id[-id];...>",memory="number",policy="(bind|interleave|preferred`“”).  `cpus` CPUs accessing this NUMA node.  `hostnodes` Host NUMA nodes to use.  `memory` Amount of memory this NUMA node provides.  `policy` NUMA allocation policy. |
| **numa_enabled**  boolean | Enables NUMA.  **Choices:**   - `false` - `true` |
| **onboot**  boolean | Specifies whether a VM will be started during system bootup.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `true`.  **Choices:**   - `false` - `true` |
| **ostype**  string | Specifies guest operating system. This is used to enable special optimization/features for specific operating systems.  The l26 is Linux 2.6/3.X Kernel.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `l26`.  **Choices:**   - `"other"` - `"wxp"` - `"w2k"` - `"w2k3"` - `"w2k8"` - `"wvista"` - `"win7"` - `"win8"` - `"win10"` - `"win11"` - `"l24"` - `"l26"` - `"solaris"` |
| **parallel**  dictionary | A hash/dictionary of map host parallel devices. `parallel='{"key":"value", "key":"value"}'`.  Keys allowed are - (parallel[n]) where 0 ≤ n ≤ 2.  Values allowed are - `"/dev/parport\d+|/dev/usb/lp\d+"`. |
| **pool**  string | Add the new VM to the specified pool. |
| **protection**  boolean | Enable/disable the protection flag of the VM. This will enable/disable the remove VM and remove disk operations.  **Choices:**   - `false` - `true` |
| **proxmox_default_behavior**  string  *added in community.general 1.3.0* | As of community.general 4.0.0, various options no longer have default values. These default values caused problems when users expected different behavior from Proxmox by default or filled options which caused problems when set. - The value `compatibility` (default before community.general 4.0.0) will ensure that the default values are used when the values are not explicitly specified by the user. The new default is `no_defaults`, which makes sure these options have no defaults. - This affects the `acpi`, `autostart`, `balloon`, `boot`, `cores`, `cpu`, `cpuunits`, `force`, `format`, `kvm`, `memory`, `onboot`, `ostype`, `sockets`, `tablet`, `template`, and `vga` options.  **Choices:**   - `"compatibility"` - `"no_defaults"` ← (default) |
| **reboot**  boolean | Allow reboot. If set to `true`, the VM exit on reboot.  **Choices:**   - `false` - `true` |
| **revert**  string | Revert a pending change. |
| **sata**  dictionary | A hash/dictionary of volume used as sata hard disk or CD-ROM. `sata='{"key":"value", "key":"value"}'`.  Keys allowed are - `sata[n]` where 0 ≤ n ≤ 5.  Values allowed are - `"storage:size,format=value"`.  `storage` is the storage identifier where to create the disk.  `size` is the size of the disk in GB.  `format` is the drive’s backing file’s data format. `qcow2|raw|subvol`. Please refer to the Proxmox VE Administrator Guide, section Proxmox VE Storage (see <https://pve.proxmox.com/pve-docs/chapter-pvesm.html> for the latest version, tables 3 to 14) to find out format supported by the provided storage backend. |
| **scsi**  dictionary | A hash/dictionary of volume used as SCSI hard disk or CD-ROM. `scsi='{"key":"value", "key":"value"}'`.  Keys allowed are - `scsi[n]` where 0 ≤ n ≤ 13.  Values allowed are - `"storage:size,format=value"`.  `storage` is the storage identifier where to create the disk.  `size` is the size of the disk in GB.  `format` is the drive’s backing file’s data format. `qcow2|raw|subvol`. Please refer to the Proxmox VE Administrator Guide, section Proxmox VE Storage (see <https://pve.proxmox.com/pve-docs/chapter-pvesm.html> for the latest version, tables 3 to 14) to find out format supported by the provided storage backend. |
| **scsihw**  string | Specifies the SCSI controller model.  **Choices:**   - `"lsi"` - `"lsi53c810"` - `"virtio-scsi-pci"` - `"virtio-scsi-single"` - `"megasas"` - `"pvscsi"` |
| **searchdomains**  list / elements=string  *added in community.general 1.3.0* | cloud-init: Sets DNS search domain(s).  If unset, PVE host settings are used. |
| **serial**  dictionary | A hash/dictionary of serial device to create inside the VM. `'{"key":"value", "key":"value"}'`.  Keys allowed are - serial[n](str; required) where 0 ≤ n ≤ 3.  Values allowed are - `(/dev/.+|socket)`.  /!\ If you pass through a host serial device, it is no longer possible to migrate such machines - use with special care. |
| **shares**  integer | Rets amount of memory shares for auto-ballooning. (0 - 50000).  The larger the number is, the more memory this VM gets.  The number is relative to weights of all other running VMs.  Using 0 disables auto-ballooning, this means no limit. |
| **skiplock**  boolean | Ignore locks  Only root is allowed to use this option.  **Choices:**   - `false` - `true` |
| **smbios**  string | Specifies SMBIOS type 1 fields.  Comma separated, Base64 encoded (optional) SMBIOS properties:  `[base64=<1|0>] [,family=<Base64 encoded string>]`  `[,manufacturer=<Base64 encoded string>]`  `[,product=<Base64 encoded string>]`  `[,serial=<Base64 encoded string>]`  `[,sku=<Base64 encoded string>]`  `[,uuid=<UUID>]`  `[,version=<Base64 encoded string>]` |
| **snapname**  string | The name of the snapshot. Used only with clone. |
| **sockets**  integer | Sets the number of CPU sockets. (1 - N).  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `1`. |
| **sshkeys**  string  *added in community.general 1.3.0* | cloud-init: SSH key to assign to the default user. NOT TESTED with multiple keys but a multi-line value should work. |
| **startdate**  string | Sets the initial date of the real time clock.  Valid format for date are `'now'` or `'2016-09-25T16:01:21'` or `'2016-09-25'`. |
| **startup**  string | Startup and shutdown behavior. `[[order=]\d+] [,up=\d+] [,down=\d+]`.  Order is a non-negative number defining the general startup order.  Shutdown in done with reverse ordering. |
| **state**  string | Indicates desired state of the instance.  If `current`, the current state of the VM will be fetched. You can access it with `results.status`  **Choices:**   - `"present"` ← (default) - `"started"` - `"absent"` - `"stopped"` - `"restarted"` - `"current"` |
| **storage**  string | Target storage for full clone. |
| **tablet**  boolean | Enables/disables the USB tablet device.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `false`.  **Choices:**   - `false` - `true` |
| **tags**  list / elements=string  *added in community.general 2.3.0* | List of tags to apply to the VM instance.  Tags must start with `[a-z0-9_]` followed by zero or more of the following characters `[a-z0-9_-+.]`.  Tags are only available in Proxmox 6+. |
| **target**  string | Target node. Only allowed if the original VM is on shared storage.  Used only with clone |
| **tdf**  boolean | Enables/disables time drift fix.  **Choices:**   - `false` - `true` |
| **template**  boolean | Enables/disables the template.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `false`.  **Choices:**   - `false` - `true` |
| **timeout**  integer | Timeout for operations.  When used with `state=stopped` the option sets a graceful timeout for VM stop after which a VM will be forcefully stopped.  **Default:** `30` |
| **tpmstate0**  dictionary  *added in community.general 7.1.0* | A hash/dictionary of options for the Trusted Platform Module disk.  A TPM state disk is required for Windows 11 installations. |
| **storage**  string / required | `tpmstate0.storage` is the storage identifier where to create the disk. |
| **version**  string | The TPM version to use.  **Choices:**   - `"1.2"` - `"2.0"` ← (default) |
| **update**  boolean | If `true`, the VM will be updated with new value.  Because of the operations of the API and security reasons, I have disabled the update of the following parameters `net`, `virtio`, `ide`, `sata`, `scsi`. Per example updating `net` update the MAC address and `virtio` create always new disk…  Update of `pool` is disabled. It needs an additional API endpoint not covered by this module.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |
| **vcpus**  integer | Sets number of hotplugged vcpus. |
| **vga**  string | Select VGA type. If you want to use high resolution modes (>= 1280x1024x16) then you should use option ‘std’ or ‘vmware’.  This option has no default unless `proxmox_default_behavior` is set to `compatibility`; then the default is `std`.  **Choices:**   - `"std"` - `"cirrus"` - `"vmware"` - `"qxl"` - `"serial0"` - `"serial1"` - `"serial2"` - `"serial3"` - `"qxl2"` - `"qxl3"` - `"qxl4"` |
| **virtio**  dictionary | A hash/dictionary of volume used as VIRTIO hard disk. `virtio='{"key":"value", "key":"value"}'`.  Keys allowed are - `virtio[n]` where 0 ≤ n ≤ 15.  Values allowed are - `"storage:size,format=value"`.  `storage` is the storage identifier where to create the disk.  `size` is the size of the disk in GB.  `format` is the drive’s backing file’s data format. `qcow2|raw|subvol`. Please refer to the Proxmox VE Administrator Guide, section Proxmox VE Storage (see <https://pve.proxmox.com/pve-docs/chapter-pvesm.html> for the latest version, tables 3 to 14) to find out format supported by the provided storage backend. |
| **vmid**  integer | Specifies the instance ID.  If not set the next available ID will be fetched from ProxmoxAPI. |
| **watchdog**  string | Creates a virtual hardware watchdog device. |

## [Attributes](proxmox_kvm_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](proxmox_kvm_module.md#id5)

> **See also:**
>
> [community.general.proxmox_vm_info](proxmox_vm_info_module.md#ansible-collections-community-general-proxmox-vm-info-module)
> :   Retrieve information about one or more Proxmox VE virtual machines.

## [Examples](proxmox_kvm_module.md#id6)

```yaml+jinja
- name: Create new VM with minimal options
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf

- name: Create a VM from archive (backup)
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    archive: backup-storage:backup/vm/140/2023-03-08T06:41:23Z
    name: spynal

- name: Create new VM with minimal options and given vmid
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    vmid: 100

- name: Create new VM with two network interface options
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    net:
      net0: 'virtio,bridge=vmbr1,rate=200'
      net1: 'e1000,bridge=vmbr2'

- name: Create new VM with one network interface, three virto hard disk, 4 cores, and 2 vcpus
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    net:
      net0: 'virtio,bridge=vmbr1,rate=200'
    virtio:
      virtio0: 'VMs_LVM:10'
      virtio1: 'VMs:2,format=qcow2'
      virtio2: 'VMs:5,format=raw'
    cores: 4
    vcpus: 2

- name: Create VM with 1 10GB SATA disk and an EFI disk, with Secure Boot disabled by default
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    sata:
      sata0: 'VMs_LVM:10,format=raw'
    bios: ovmf
    efidisk0:
      storage: VMs_LVM_thin
      format: raw
      efitype: 4m
      pre_enrolled_keys: false

- name: Create VM with 1 10GB SATA disk and an EFI disk, with Secure Boot enabled by default
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    sata:
      sata0: 'VMs_LVM:10,format=raw'
    bios: ovmf
    efidisk0:
      storage: VMs_LVM
      format: raw
      efitype: 4m
      pre_enrolled_keys: 1

- name: >
    Clone VM with only source VM name.
    The VM source is spynal.
    The target VM name is zavala
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    clone: spynal
    name: zavala
    node: sabrewulf
    storage: VMs
    format: qcow2
    timeout: 500

- name: >
    Create linked clone VM with only source VM name.
    The VM source is spynal.
    The target VM name is zavala
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    clone: spynal
    name: zavala
    node: sabrewulf
    storage: VMs
    full: false
    format: unspecified
    timeout: 500

- name: Clone VM with source vmid and target newid and raw format
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    clone: arbitrary_name
    vmid: 108
    newid: 152
    name: zavala
    node: sabrewulf
    storage: LVM_STO
    format: raw
    timeout: 300

- name: Create new VM and lock it for snapshot
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    lock: snapshot

- name: Create new VM and set protection to disable the remove VM and remove disk operations
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    protection: true

- name: Create new VM using cloud-init with a username and password
  community.general.proxmox_kvm:
    node: sabrewulf
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    ide:
      ide2: 'local:cloudinit,format=qcow2'
    ciuser: mylinuxuser
    cipassword: supersecret
    searchdomains: 'mydomain.internal'
    nameservers: 1.1.1.1
    net:
      net0: 'virtio,bridge=vmbr1,tag=77'
    ipconfig:
      ipconfig0: 'ip=192.168.1.1/24,gw=192.168.1.1'

- name: Create new VM using Cloud-Init with an ssh key
  community.general.proxmox_kvm:
    node: sabrewulf
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    ide:
      ide2: 'local:cloudinit,format=qcow2'
    sshkeys: 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILJkVm98B71lD5XHfihwcYHE9TVpsJmK1vR1JcaU82L+'
    searchdomains: 'mydomain.internal'
    nameservers:
      - '1.1.1.1'
      - '8.8.8.8'
    net:
      net0: 'virtio,bridge=vmbr1,tag=77'
    ipconfig:
      ipconfig0: 'ip=192.168.1.1/24'

- name: Start VM
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    state: started

- name: Stop VM
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    state: stopped

- name: Stop VM with force
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    state: stopped
    force: true

- name: Restart VM
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    state: restarted

- name: Remove VM
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    state: absent

- name: Get VM current state
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    state: current

- name: Update VM configuration
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    cores: 8
    memory: 16384
    update: true

- name: Delete QEMU parameters
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    delete: 'args,template,cpulimit'

- name: Revert a pending change
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf
    revert: 'template,cpulimit'

- name: Migrate VM on second node
  community.general.proxmox_kvm:
    api_user: root@pam
    api_password: secret
    api_host: helldorado
    name: spynal
    node: sabrewulf-2
    migrate: true
```

## [Return Values](proxmox_kvm_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A short message  **Returned:** always  **Sample:** `"VM kropta with vmid = 110 is running"` |
| **status**  string | The current virtual machine status.  **Returned:** success, not clone, not absent, not update  **Sample:** `"running"` |
| **vmid**  integer | The VM vmid.  **Returned:** success  **Sample:** `115` |

### Authors

- Abdoul Bah (@helldorado) <bahabdoul at gmail.com>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
