---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_template module – Module to manage virtual machine templates in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_template_module.html
fetched_at: 2026-07-28T02:50:05+00:00
---
# ovirt.ovirt.ovirt_template module – Module to manage virtual machine templates in oVirt/RHV

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
> see [Requirements](ovirt_template_module.md#ansible-collections-ovirt-ovirt-ovirt-template-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_template`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_template_module.md#synopsis)
- [Requirements](ovirt_template_module.md#requirements)
- [Parameters](ovirt_template_module.md#parameters)
- [Notes](ovirt_template_module.md#notes)
- [Examples](ovirt_template_module.md#examples)
- [Return Values](ovirt_template_module.md#return-values)

## [Synopsis](ovirt_template_module.md#id1)

- Module to manage virtual machine templates in oVirt/RHV.

## [Requirements](ovirt_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_partial_import**  boolean | Boolean indication whether to allow partial registration of a template when `state` is registered.  **Choices:**   - `false` - `true` |
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
| **bios_type**  string  *added in ovirt.ovirt 2.0.0* | Set bios type, necessary for some operating systems and secure boot.  If no value is passed, default value is set from cluster.  NOTE - Supported since oVirt 4.3.  **Choices:**   - `"i440fx_sea_bios"` - `"q35_ovmf"` - `"q35_sea_bios"` - `"q35_secure_boot"` |
| **boot_menu**  boolean  *added in ovirt.ovirt 2.0.0* | *True* enable menu to select boot device, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **clone_name**  string | Name for importing Template from storage domain.  If not defined, `name` will be used. |
| **clone_permissions**  boolean | If *True* then the permissions of the VM (only the direct ones, not the inherited ones) will be copied to the created template.  This parameter is used only when `state` *present*.  **Choices:**   - `false` - `true` |
| **cloud_init**  dictionary | Dictionary with values for Unix-like Virtual Machine initialization using cloud init. |
| **authorized_ssh_keys**  string | Use this SSH keys to login to Virtual Machine. |
| **custom_script**  string | Cloud-init script which will be executed on Virtual Machine when deployed.  This is appended to the end of the cloud-init script generated by any other options.  For further information, refer to cloud-init User-Data documentation. |
| **dns_search**  string | DNS search domains to be configured on Virtual Machine. |
| **dns_servers**  string | DNS servers to be configured on Virtual Machine, maximum of two, space-separated. |
| **host_name**  string | Hostname to be set to Virtual Machine when deployed. |
| **nic_boot_protocol**  string | Set boot protocol of the network interface of Virtual Machine.  **Choices:**   - `"none"` - `"dhcp"` - `"static"` |
| **nic_gateway**  string | If boot protocol is static, set this gateway to network interface of Virtual Machine. |
| **nic_ip_address**  string | If boot protocol is static, set this IP address to network interface of Virtual Machine. |
| **nic_name**  string | Set name to network interface of Virtual Machine. |
| **nic_netmask**  string | If boot protocol is static, set this netmask to network interface of Virtual Machine. |
| **regenerate_ssh_keys**  boolean | If *True* SSH keys will be regenerated on Virtual Machine.  **Choices:**   - `false` - `true` |
| **root_password**  string | Password to be set for user specified by `user_name` parameter. |
| **timezone**  string | Timezone to be set to Virtual Machine when deployed. |
| **user_name**  string | Username to be used to set password to Virtual Machine when deployed. |
| **cloud_init_nics**  list / elements=dictionary | List of dictionaries representing network interfaces to be setup by cloud init.  This option is used, when user needs to setup more network interfaces via cloud init.  If one network interface is enough, user should use `cloud_init` *nic_\** parameters. `cloud_init` *nic_\** parameters are merged with `cloud_init_nics` parameters. |
| **nic_boot_protocol**  string | Set boot protocol of the network interface of Virtual Machine. Can be one of `none`, `dhcp` or `static`. |
| **nic_gateway**  string | If boot protocol is static, set this gateway to network interface of Virtual Machine. |
| **nic_ip_address**  string | If boot protocol is static, set this IP address to network interface of Virtual Machine. |
| **nic_name**  string | Set name to network interface of Virtual Machine. |
| **nic_netmask**  string | If boot protocol is static, set this netmask to network interface of Virtual Machine. |
| **cluster**  string | Name of the cluster, where template should be created/imported. |
| **cluster_mappings**  list / elements=dictionary | Mapper which maps cluster name between Template’s OVF and the destination cluster this Template should be registered to, relevant when `state` is registered. Cluster mapping is described by the following dictionary: |
| **dest_name**  string | The name of the destination cluster. |
| **source_name**  string | The name of the source cluster. |
| **cpu_profile**  string | CPU profile to be set to template. |
| **description**  string | Description of the template. |
| **domain_mappings**  list / elements=dictionary | Mapper which maps aaa domain name between Template’s OVF and the destination aaa domain this Template should be registered to, relevant when `state` is registered. The aaa domain mapping is described by the following dictionary: |
| **dest_name**  string | The name of the destination aaa domain. |
| **source_name**  string | The name of the source aaa domain. |
| **exclusive**  boolean | When `state` is *exported* this parameter indicates if the existing templates with the same name should be overwritten.  **Choices:**   - `false` - `true` |
| **export_domain**  string | When `state` is *exported* or *imported* this parameter specifies the name of the export storage domain. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **id**  string | ID of the template to be registered. |
| **image_disk**  aliases: glance_image_disk_name  string | When `state` is *imported* and `image_provider` is used this parameter specifies the name of disk to be imported as template. |
| **image_provider**  string | When `state` is *imported* this parameter specifies the name of the image provider to be used. |
| **io_threads**  integer | Number of IO threads used by virtual machine. *0* means IO threading disabled. |
| **kvm**  dictionary | Dictionary of values to be used to connect to kvm and import a template to oVirt. |
| **clone**  string | Indicates if the identifiers of the imported template should be regenerated. |
| **host**  string | The host name from which the template will be imported. |
| **storage_domain**  string | Specifies the target storage domain for converted disks. This is required parameter. |
| **url**  string | The URL to be passed to the *virt-v2v* tool for conversion.  For example *qemu:///system*. This is required parameter. |
| **memory**  string | Amount of memory of the template. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB). |
| **memory_guaranteed**  string | Amount of minimal guaranteed memory of the template. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  `memory_guaranteed` parameter can’t be lower than `memory` parameter. |
| **memory_max**  string | Upper bound of template memory up to which memory hot-plug can be performed. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB). |
| **name**  string | Name of the template to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **nics**  list / elements=dictionary | List of NICs, which should be attached to Virtual Machine. NIC is described by following dictionary. |
| **interface**  string | Type of the network interface.  **Choices:**   - `"virtio"` ← (default) - `"e1000"` - `"rtl8139"` |
| **mac_address**  string | Custom MAC address of the network interface, by default it’s obtained from MAC pool. |
| **name**  string | Name of the NIC. |
| **profile_name**  string | Profile name where NIC should be attached. |
| **operating_system**  string | Operating system of the template, for example ‘rhel_8x64’.  Default value is set by oVirt/RHV engine.  Use the [ovirt.ovirt.ovirt_vm_os_info](ovirt_vm_os_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-os-info-module) module to obtain the current list. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **role_mappings**  list / elements=dictionary | Mapper which maps role name between Template’s OVF and the destination role this Template should be registered to, relevant when `state` is registered. Role mapping is described by the following dictionary: |
| **dest_name**  string | The name of the destination role. |
| **source_name**  string | The name of the source role. |
| **seal**  boolean | ‘Sealing’ is an operation that erases all machine-specific configurations from a filesystem: This includes SSH keys, UDEV rules, MAC addresses, system ID, hostname, etc. If *true* subsequent virtual machines made from this template will avoid configuration inheritance.  This parameter is used only when `state` *present*.  **Choices:**   - `false` - `true` |
| **smartcard_enabled**  boolean | If *true*, use smart card authentication.  **Choices:**   - `false` - `true` |
| **soundcard_enabled**  boolean | If *true*, the sound card is added to the virtual machine.  **Choices:**   - `false` - `true` |
| **sso**  boolean | *True* enable Single Sign On by Guest Agent, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **state**  string | Should the template be present/absent/exported/imported/registered. When `state` is *registered* and the unregistered template’s name belongs to an already registered in engine template in the same DC then we fail to register the unregistered template.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exported"` - `"imported"` - `"registered"` |
| **storage_domain**  string | When `state` is *imported* this parameter specifies the name of the destination data storage domain. When `state` is *registered* this parameter specifies the name of the data storage domain of the unregistered template. |
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
| **template_image_disk_name**  string | When `state` is *imported* and `image_provider` is used this parameter specifies the new name for imported disk, if omitted then *image_disk* name is used by default. This parameter is used only in case of importing disk image from Glance domain. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **timezone**  string | Sets time zone offset of the guest hardware clock.  For example `Etc/GMT` |
| **usb_support**  boolean | *True* enable USB support, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **version**  dictionary | `name` - The name of this version.  `number` - The index of this version in the versions hierarchy of the template. Used for editing of sub template. |
| **vm**  string | Name of the VM, which will be used to create template. |
| **vnic_profile_mappings**  list / elements=dictionary | Mapper which maps an external virtual NIC profile to one that exists in the engine when `state` is registered. vnic_profile is described by the following dictionary: |
| **source_network_name**  string | The network name of the source network. |
| **source_profile_name**  string | The profile name related to the source network. |
| **target_profile_id**  string | The id of the target profile id to be mapped to in the engine. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_template_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_template_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create template from vm
- ovirt.ovirt.ovirt_template:
    cluster: Default
    name: mytemplate
    vm: rhel7
    cpu_profile: Default
    description: Test

# Import template
- ovirt.ovirt.ovirt_template:
    state: imported
    name: mytemplate
    export_domain: myexport
    storage_domain: mystorage
    cluster: mycluster

# Remove template
- ovirt.ovirt.ovirt_template:
    state: absent
    name: mytemplate

# Change Template Name
- ovirt.ovirt.ovirt_template:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_template_name"

# Register template
- ovirt.ovirt.ovirt_template:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    name: mytemplate

# Register template using id
- ovirt.ovirt.ovirt_template:
    state: registered
    storage_domain: mystorage
    cluster: mycluster
    id: 1111-1111-1111-1111

# Register template, allowing partial import
- ovirt.ovirt.ovirt_template:
    state: registered
    storage_domain: mystorage
    allow_partial_import: "True"
    cluster: mycluster
    id: 1111-1111-1111-1111

# Register template with vnic profile mappings
- ovirt.ovirt.ovirt_template:
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

# Register template with mapping
- ovirt.ovirt.ovirt_template:
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
    cluster_mappings:
      - source_name: cluster_A
        dest_name: cluster_B

# Import image from Glance s a template
- ovirt.ovirt.ovirt_template:
    state: imported
    name: mytemplate
    image_disk: "centos7"
    template_image_disk_name: centos7_from_glance
    image_provider: "glance_domain"
    storage_domain: mystorage
    cluster: mycluster

# Edit template subversion
- ovirt.ovirt.ovirt_template:
    cluster: mycluster
    name: mytemplate
    vm: rhel7
    version:
        number: 2
        name: subversion

# Create new template subversion
- ovirt.ovirt.ovirt_template:
    cluster: mycluster
    name: mytemplate
    vm: rhel7
    version:
        name: subversion

- name: Template with cloud init
  ovirt.ovirt.ovirt_template:
    name: mytemplate
    cluster: Default
    vm: rhel8
    memory: 1GiB
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

- name: Template with cloud init, with multiple network interfaces
  ovirt.ovirt.ovirt_template:
    name: mytemplate
    cluster: mycluster
    vm: rhel8
    cloud_init_nics:
    - nic_name: eth0
      nic_boot_protocol: dhcp
    - nic_name: eth1
      nic_boot_protocol: static
      nic_ip_address: 10.34.60.86
      nic_netmask: 255.255.252.0
      nic_gateway: 10.34.63.254

- name: Template with timezone and nic
  ovirt.ovirt.ovirt_template:
    cluster: MyCluster
    name: mytemplate
    vm: rhel8
    timezone: America/Godthab
    memory_max: 2Gib
    nics:
      - name: nic1

- name: Template with sysprep
  ovirt.ovirt.ovirt_template:
    name: windows2012R2_AD
    cluster: Default
    vm: windows2012
    memory: 3GiB
    sysprep:
      host_name: windowsad.example.com
      user_name: Administrator
      root_password: SuperPassword123

- name: Import external ova template
  ovirt.ovirt.ovirt_template:
    cluster: mycluster
    name: mytemplate
    state: present
    timeout: 1800
    poll_interval: 30
    kvm:
      host: myhost
      url: ova:///tmp/test.ova
      storage_domain: mystorage
```

## [Return Values](ovirt_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the template which is managed  **Returned:** On success if template is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **template**  dictionary | Dictionary of all the template attributes. Template attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/template>.  **Returned:** On success if template is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
