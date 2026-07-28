---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_vmpool module – Module to manage VM pools in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_vmpool_module.html
fetched_at: 2026-07-28T02:50:13+00:00
---
# ovirt.ovirt.ovirt_vmpool module – Module to manage VM pools in oVirt/RHV

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
> see [Requirements](ovirt_vmpool_module.md#ansible-collections-ovirt-ovirt-ovirt-vmpool-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_vmpool`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_vmpool_module.md#synopsis)
- [Requirements](ovirt_vmpool_module.md#requirements)
- [Parameters](ovirt_vmpool_module.md#parameters)
- [Notes](ovirt_vmpool_module.md#notes)
- [Examples](ovirt_vmpool_module.md#examples)
- [Return Values](ovirt_vmpool_module.md#return-values)

## [Synopsis](ovirt_vmpool_module.md#id1)

- Module to manage VM pools in oVirt/RHV.

## [Requirements](ovirt_vmpool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_vmpool_module.md#id3)

| Parameter | Comments |
| --- | --- |
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
| **cluster**  string | Name of the cluster, where VM pool should be created. |
| **comment**  string | Comment of the Virtual Machine pool. |
| **description**  string | Description of the VM pool. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **id**  string | ID of the vmpool to manage. |
| **name**  string / required | Name of the VM pool to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **prestarted**  integer | Number of pre-started VMs defines the number of VMs in run state, that are waiting to be attached to Users.  Default value is set by engine. |
| **state**  string | Should the VM pool be present/absent.  Note that when `state` is *absent* all VMs in VM pool are stopped and removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **template**  string | Name of the template, which will be used to create VM pool. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **type**  string | Type of the VM pool. Either manual or automatic.  `manual` - The administrator is responsible for explicitly returning the virtual machine to the pool. The virtual machine reverts to the original base image after the administrator returns it to the pool.  `Automatic` - When the virtual machine is shut down, it automatically reverts to its base image and is returned to the virtual machine pool.  Default value is set by engine.  **Choices:**   - `"manual"` - `"automatic"` |
| **vm**  dictionary | For creating vm pool without editing template.  Note: You can use `vm` only for creating vm pool. |
| **cloud_init**  string | Dictionary with values for Unix-like Virtual Machine initialization using cloud init.  `host_name` - Hostname to be set to Virtual Machine when deployed.  `timezone` - Timezone to be set to Virtual Machine when deployed.  `user_name` - Username to be used to set password to Virtual Machine when deployed.  `root_password` - Password to be set for user specified by `user_name` parameter.  `authorized_ssh_keys` - Use this SSH keys to login to Virtual Machine.  `regenerate_ssh_keys` - If *True* SSH keys will be regenerated on Virtual Machine.  `custom_script` - Cloud-init script which will be executed on Virtual Machine when deployed. This is appended to the end of the cloud-init script generated by any other options. For further information, refer to cloud-init User-Data documentation.  `dns_servers` - DNS servers to be configured on Virtual Machine, maximum of two, space-separated.  `dns_search` - DNS search domains to be configured on Virtual Machine.  `nic_boot_protocol` - Set boot protocol of the network interface of Virtual Machine. Can be one of `none`, `dhcp` or `static`.  `nic_ip_address` - If boot protocol is static, set this IP address to network interface of Virtual Machine.  `nic_netmask` - If boot protocol is static, set this netmask to network interface of Virtual Machine.  `nic_gateway` - If boot protocol is static, set this gateway to network interface of Virtual Machine.  `nic_name` - Set name to network interface of Virtual Machine. |
| **comment**  string | Comment of the Virtual Machine. |
| **memory**  string | Amount of memory of the Virtual Machine. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  Default value is set by engine. |
| **memory_guaranteed**  string | Amount of minimal guaranteed memory of the Virtual Machine. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  `memory_guaranteed` parameter can’t be lower than `memory` parameter.  Default value is set by engine. |
| **memory_max**  string | Upper bound of virtual machine memory up to which memory hot-plug can be performed. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  Default value is set by engine. |
| **nics**  string | List of NICs, which should be attached to Virtual Machine. NIC is described by following dictionary.  `name` - Name of the NIC.  `profile_name` - Profile name where NIC should be attached.  `interface` - Type of the network interface. One of following *virtio*, *e1000*, *rtl8139*, default is *virtio*.  `mac_address` - Custom MAC address of the network interface, by default it’s obtained from MAC pool.  NOTE - This parameter is used only when `state` is *running* or *present* and is able to only create NICs.  To manage NICs of the VM in more depth please use ovirt.ovirt.ovirt_nics module instead. |
| **smartcard_enabled**  boolean | If *true*, use smart card authentication.  **Choices:**   - `false` - `true` |
| **sso**  boolean | *True* enable Single Sign On by Guest Agent, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **timezone**  string | Sets time zone offset of the guest hardware clock.  For example `Etc/GMT` |
| **vm_count**  integer | Number of VMs in the pool.  Default value is set by engine. |
| **vm_per_user**  integer | Maximum number of VMs a single user can attach to from this pool.  Default value is set by engine. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_vmpool_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_vmpool_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Create VM pool from template
  ovirt.ovirt.ovirt_vmpool:
    cluster: mycluster
    name: myvmpool
    template: rhel7
    vm_count: 2
    prestarted: 2
    vm_per_user: 1

- name: Remove vmpool, note that all VMs in pool will be stopped and removed
  ovirt.ovirt.ovirt_vmpool:
    state: absent
    name: myvmpool

- name: Change Pool Name
  ovirt.ovirt.ovirt_vmpool:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_pool_name"

- name: Create vm pool and override the pool values
  ovirt.ovirt.ovirt_vmpool:
    cluster: mycluster
    name: vmpool
    template: blank
    vm_count: 2
    prestarted: 1
    vm_per_user: 1
    vm:
      memory: 4GiB
      memory_guaranteed: 4GiB
      memory_max: 10GiB
      comment: vncomment
      cloud_init:
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
      nics:
        - name: nicname
          interface: virtio
          profile_name: network
```

## [Return Values](ovirt_vmpool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the VM pool which is managed  **Returned:** On success if VM pool is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **vm_pool**  dictionary | Dictionary of all the VM pool attributes. VM pool attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/vm_pool>.  **Returned:** On success if VM pool is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
