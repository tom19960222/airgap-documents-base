---
collection: ansible
version: "8"
title: "community.general.xenserver_guest module – Manages virtual machines running on Citrix Hypervisor/XenServer host or pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xenserver_guest_module.html
fetched_at: 2026-07-28T01:51:30+00:00
---
# community.general.xenserver_guest module – Manages virtual machines running on Citrix Hypervisor/XenServer host or pool

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
> see [Requirements](xenserver_guest_module.md#ansible-collections-community-general-xenserver-guest-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.xenserver_guest`.

- [Synopsis](xenserver_guest_module.md#synopsis)
- [Requirements](xenserver_guest_module.md#requirements)
- [Parameters](xenserver_guest_module.md#parameters)
- [Attributes](xenserver_guest_module.md#attributes)
- [Notes](xenserver_guest_module.md#notes)
- [Examples](xenserver_guest_module.md#examples)
- [Return Values](xenserver_guest_module.md#return-values)

## [Synopsis](xenserver_guest_module.md#id1)

- This module can be used to create new virtual machines from templates or other virtual machines, modify various virtual machine components like network and disk, rename a virtual machine and remove a virtual machine with associated components.

Aliases: cloud.xenserver.xenserver_guest

## [Requirements](xenserver_guest_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- XenAPI

## [Parameters](xenserver_guest_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cdrom**  dictionary | A CD-ROM configuration for the VM.  All parameters are case sensitive. |
| **iso_name**  string | The file name of an ISO image from one of the XenServer ISO Libraries (implies `cdrom.type=iso`).  Required if `cdrom.type` is set to `iso`. |
| **type**  string | The type of CD-ROM. With `none` the CD-ROM device will be present but empty.  **Choices:**   - `"none"` - `"iso"` |
| **custom_params**  list / elements=dictionary | Define a list of custom VM params to set on VM.  Useful for advanced users familiar with managing VM params through xe CLI.  A custom value object takes two fields `custom_params[].key` and `custom_params[].value` (see example below). |
| **key**  string / required | VM param name. |
| **value**  any / required | VM param value. |
| **disks**  aliases: disk  list / elements=dictionary | A list of disks to add to VM.  All parameters are case sensitive.  Removing or detaching existing disks of VM is not supported.  New disks are required to have either a `disks[].size` or one of `disks[].size_[tb,gb,mb,kb,b]` parameters specified.  VM needs to be shut down to reconfigure disk size. |
| **name**  aliases: name_label  string | Disk name. |
| **name_desc**  string | Disk description. |
| **size**  string | Disk size with unit. Unit must be: `b`, `kb`, `mb`, `gb`, `tb`. VM needs to be shut down to reconfigure this parameter.  If no unit is specified, size is assumed to be in bytes. |
| **size_b**  string | Disk size in bytes. |
| **size_gb**  string | Disk size in gigabytes. |
| **size_kb**  string | Disk size in kilobytes. |
| **size_mb**  string | Disk size in megabytes. |
| **size_tb**  string | Disk size in terabytes. |
| **sr**  string | Storage Repository to create disk on. If not specified, will use default SR. Cannot be used for moving disk to other SR. |
| **sr_uuid**  string | UUID of a SR to create disk on. Use if SR name is not unique. |
| **folder**  string | Destination folder for VM.  This parameter is case sensitive.  Example:  folder: /folder1/folder2 |
| **force**  boolean | Ignore warnings and complete the actions.  This parameter is useful for removing VM in running state or reconfiguring VM params that require VM to be shut down.  **Choices:**   - `false` ← (default) - `true` |
| **hardware**  dictionary | Manage VM’s hardware parameters. VM needs to be shut down to reconfigure these parameters. |
| **memory_mb**  integer | Amount of memory in MB. |
| **num_cpu_cores_per_socket**  integer | Number of Cores Per Socket. `hardware.num_cpus` has to be a multiple of `hardware.num_cpu_cores_per_socket`. |
| **num_cpus**  integer | Number of CPUs. |
| **home_server**  string | Name of a XenServer host that will be a Home Server for the VM.  This parameter is case sensitive. |
| **hostname**  aliases: host, pool  string | The hostname or IP address of the XenServer host or XenServer pool master.  If the value is not specified in the task, the value of environment variable `XENSERVER_HOST` will be used instead.  **Default:** `"localhost"` |
| **is_template**  boolean | Convert VM to template.  **Choices:**   - `false` ← (default) - `true` |
| **linked_clone**  boolean | Whether to create a Linked Clone from the template, existing VM or snapshot. If no, will create a full copy.  This is equivalent to `Use storage-level fast disk clone` option in XenCenter.  **Choices:**   - `false` ← (default) - `true` |
| **name**  aliases: name_label  string | Name of the VM to work with.  VMs running on XenServer do not necessarily have unique names. The module will fail if multiple VMs with same name are found.  In case of multiple VMs with same name, use `uuid` to uniquely specify VM to manage.  This parameter is case sensitive. |
| **name_desc**  string | VM description. |
| **networks**  aliases: network  list / elements=dictionary | A list of networks (in the order of the NICs).  All parameters are case sensitive.  Name is required for new NICs. Other parameters are optional in all cases. |
| **gateway**  string | Static IPv4 gateway. |
| **gateway6**  string | Static IPv6 gateway. |
| **ip**  string | Static IPv4 address (implies `networks[].type=static`). Can include prefix in format `<IPv4 address>/<prefix>` instead of using `netmask`. |
| **ip6**  string | Static IPv6 address (implies `networks[].type6=static`) with prefix in format `<IPv6 address>/<prefix>`. |
| **mac**  string | Customize MAC address of the interface. |
| **name**  aliases: name_label  string | Name of a XenServer network to attach the network interface to. |
| **netmask**  string | Static IPv4 netmask required for `networks[].ip` if prefix is not specified. |
| **type**  string | Type of IPv4 assignment. Value `none` means whatever is default for OS.  On some operating systems it could be DHCP configured (e.g. Windows) or unconfigured interface (e.g. Linux).  **Choices:**   - `"none"` - `"dhcp"` - `"static"` |
| **type6**  string | Type of IPv6 assignment. Value `none` means whatever is default for OS.  **Choices:**   - `"none"` - `"dhcp"` - `"static"` |
| **password**  aliases: pass, pwd  string | The password to use for connecting to XenServer.  If the value is not specified in the task, the value of environment variable `XENSERVER_PASSWORD` will be used instead. |
| **state**  string | Specify the state VM should be in.  If `state` is set to `present` and VM exists, ensure the VM configuration conforms to given parameters.  If `state` is set to `present` and VM does not exist, then VM is deployed with given parameters.  If `state` is set to `absent` and VM exists, then VM is removed with its associated components.  If `state` is set to `poweredon` and VM does not exist, then VM is deployed with given parameters and powered on automatically.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"poweredon"` |
| **state_change_timeout**  integer | By default, module will wait indefinitely for VM to acquire an IP address if `wait_for_ip_address=true`.  If this parameter is set to positive value, the module will instead wait specified number of seconds for the state change.  In case of timeout, module will generate an error message.  **Default:** `0` |
| **template**  aliases: template_src  string | Name of a template, an existing VM (must be shut down) or a snapshot that should be used to create VM.  Templates/VMs/snapshots on XenServer do not necessarily have unique names. The module will fail if multiple templates with same name are found.  In case of multiple templates/VMs/snapshots with same name, use `template_uuid` to uniquely specify source template.  If VM already exists, this setting will be ignored.  This parameter is case sensitive. |
| **template_uuid**  string | UUID of a template, an existing VM or a snapshot that should be used to create VM.  It is required if template name is not unique. |
| **username**  aliases: admin, user  string | The username to use for connecting to XenServer.  If the value is not specified in the task, the value of environment variable `XENSERVER_USER` will be used instead.  **Default:** `"root"` |
| **uuid**  string | UUID of the VM to manage if known. This is XenServer’s unique identifier.  It is required if name is not unique.  Please note that a supplied UUID will be ignored on VM creation, as XenServer creates the UUID internally. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `XENSERVER_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_ip_address**  boolean | Wait until XenServer detects an IP address for the VM. If `state` is set to `absent`, this parameter is ignored.  This requires XenServer Tools to be preinstalled on the VM to work properly.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](xenserver_guest_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](xenserver_guest_module.md#id5)

> **Note:**
>
> - Minimal supported version of XenServer is 5.6.
> - Module was tested with XenServer 6.5, 7.1, 7.2, 7.6, Citrix Hypervisor 8.0, XCP-ng 7.6 and 8.0.
> - To acquire XenAPI Python library, just run `pip install XenAPI` on your Ansible Control Node. The library can also be found inside Citrix Hypervisor/XenServer SDK (downloadable from Citrix website). Copy the XenAPI.py file from the SDK to your Python site-packages on your Ansible Control Node to use it. Latest version of the library can also be acquired from GitHub: <https://raw.githubusercontent.com/xapi-project/xen-api/master/scripts/examples/python/XenAPI/XenAPI.py>
> - If no scheme is specified in `hostname`, module defaults to `http://` because `https://` is problematic in most setups. Make sure you are accessing XenServer host in trusted environment or use `https://` scheme explicitly.
> - To use `https://` scheme for `hostname` you have to either import host certificate to your OS certificate store or use `validate_certs=false` which requires XenAPI library from XenServer 7.2 SDK or newer and Python 2.7.9 or newer.
> - Network configuration inside a guest OS, by using `networks[].type`, `networks[].ip`, `networks[].gateway` etc. parameters, is supported on XenServer 7.0 or newer for Windows guests by using official XenServer Guest agent support for network configuration. The module will try to detect if such support is available and utilize it, else it will use a custom method of configuration via xenstore. Since XenServer Guest agent only support None and Static types of network configuration, where None means DHCP configured interface, `networks[].type` and `networks[].type6` values `none` and `dhcp` have same effect. More info here: <https://www.citrix.com/community/citrix-developer/citrix-hypervisor-developer/citrix-hypervisor-developing-products/citrix-hypervisor-staticip.html>
> - On platforms without official support for network configuration inside a guest OS, network parameters will be written to xenstore `vm-data/networks/<vif_device>` key. Parameters can be inspected by using `xenstore ls` and `xenstore read` tools on \\*nix guests or through WMI interface on Windows guests. They can also be found in VM facts `instance.xenstore_data` key as returned by the module. It is up to the user to implement a boot time scripts or custom agent that will read the parameters from xenstore and configure network with given parameters. Take note that for xenstore data to become available inside a guest, a VM restart is needed hence module will require VM restart if any parameter is changed. This is a limitation of XenAPI and xenstore. Considering these limitations, network configuration through xenstore is most useful for bootstrapping newly deployed VMs, much less for reconfiguring existing ones. More info here: <https://support.citrix.com/article/CTX226713>

## [Examples](xenserver_guest_module.md#id6)

```yaml+jinja
- name: Create a VM from a template
  community.general.xenserver_guest:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    validate_certs: false
    folder: /testvms
    name: testvm_2
    state: poweredon
    template: CentOS 7
    disks:
    - size_gb: 10
      sr: my_sr
    hardware:
      num_cpus: 6
      num_cpu_cores_per_socket: 3
      memory_mb: 512
    cdrom:
      type: iso
      iso_name: guest-tools.iso
    networks:
    - name: VM Network
      mac: aa:bb:dd:aa:00:14
    wait_for_ip_address: true
  delegate_to: localhost
  register: deploy

- name: Create a VM template
  community.general.xenserver_guest:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    validate_certs: false
    folder: /testvms
    name: testvm_6
    is_template: true
    disk:
    - size_gb: 10
      sr: my_sr
    hardware:
      memory_mb: 512
      num_cpus: 1
  delegate_to: localhost
  register: deploy

- name: Rename a VM (requires the VM's UUID)
  community.general.xenserver_guest:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    name: new_name
    state: present
  delegate_to: localhost

- name: Remove a VM by UUID
  community.general.xenserver_guest:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: absent
  delegate_to: localhost

- name: Modify custom params (boot order)
  community.general.xenserver_guest:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    name: testvm_8
    state: present
    custom_params:
    - key: HVM_boot_params
      value: { "order": "ndc" }
  delegate_to: localhost

- name: Customize network parameters
  community.general.xenserver_guest:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    name: testvm_10
    networks:
    - name: VM Network
      ip: 192.168.1.100/24
      gateway: 192.168.1.1
    - type: dhcp
  delegate_to: localhost
```

## [Return Values](xenserver_guest_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changes**  list / elements=string | Detected or made changes to VM  **Returned:** always  **Sample:** `[{"hardware": ["num_cpus"]}, {"disks_changed": [[], ["size"]]}, {"disks_new": [{"name": "new-disk", "name_desc": "", "position": 2, "size_gb": "4", "vbd_userdevice": "2"}]}, {"cdrom": ["type", "iso_name"]}, {"networks_changed": [["mac"]]}, {"networks_new": [{"name": "Pool-wide network associated with eth2", "position": 1, "vif_device": "1"}]}, "need_poweredoff"]` |
| **instance**  dictionary | Metadata about the VM  **Returned:** always  **Sample:** `{"cdrom": {"type": "none"}, "customization_agent": "native", "disks": [{"name": "testvm_11-0", "name_desc": "", "os_device": "xvda", "size": 42949672960, "sr": "Local storage", "sr_uuid": "0af1245e-bdb0-ba33-1446-57a962ec4075", "vbd_userdevice": "0"}, {"name": "testvm_11-1", "name_desc": "", "os_device": "xvdb", "size": 42949672960, "sr": "Local storage", "sr_uuid": "0af1245e-bdb0-ba33-1446-57a962ec4075", "vbd_userdevice": "1"}], "domid": "56", "folder": "", "hardware": {"memory_mb": 8192, "num_cpu_cores_per_socket": 2, "num_cpus": 4}, "home_server": "", "is_template": false, "name": "testvm_11", "name_desc": "", "networks": [{"gateway": "192.168.0.254", "gateway6": "fc00::fffe", "ip": "192.168.0.200", "ip6": ["fe80:0000:0000:0000:e9cb:625a:32c5:c291", "fc00:0000:0000:0000:0000:0000:0000:0001"], "mac": "ba:91:3a:48:20:76", "mtu": "1500", "name": "Pool-wide network associated with eth1", "netmask": "255.255.255.128", "prefix": "25", "prefix6": "64", "vif_device": "0"}], "other_config": {"base_template_name": "Windows Server 2016 (64-bit)", "import_task": "OpaqueRef:e43eb71c-45d6-5351-09ff-96e4fb7d0fa5", "install-methods": "cdrom", "instant": "true", "mac_seed": "f83e8d8a-cfdc-b105-b054-ef5cb416b77e"}, "platform": {"acpi": "1", "apic": "true", "cores-per-socket": "2", "device_id": "0002", "hpet": "true", "nx": "true", "pae": "true", "timeoffset": "-25200", "vga": "std", "videoram": "8", "viridian": "true", "viridian_reference_tsc": "true", "viridian_time_ref_count": "true"}, "state": "poweredon", "uuid": "e3c0b2d5-5f05-424e-479c-d3df8b3e7cda", "xenstore_data": {"vm-data": ""}}` |

### Authors

- Bojan Vitnik (@bvitnik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
