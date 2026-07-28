---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_instant_clone module – Instant Clone VM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_instant_clone_module.html
fetched_at: 2026-07-28T02:00:15+00:00
---
# community.vmware.vmware_guest_instant_clone module – Instant Clone VM

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_instant_clone`.

- [Synopsis](vmware_guest_instant_clone_module.md#synopsis)
- [Parameters](vmware_guest_instant_clone_module.md#parameters)
- [Notes](vmware_guest_instant_clone_module.md#notes)
- [Examples](vmware_guest_instant_clone_module.md#examples)
- [Return Values](vmware_guest_instant_clone_module.md#return-values)

## [Synopsis](vmware_guest_instant_clone_module.md#id1)

- This module can be used for Creating a powered-on Instant Clone of a virtual machine.
- All variables and VMware object names are case sensitive.
- [community.vmware.vmware_guest](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) module is needed for creating a VM with poweredon state which would be used as a parent VM.
- [community.vmware.vmware_guest_powerstate](vmware_guest_powerstate_module.md#ansible-collections-community-vmware-vmware-guest-powerstate-module) module is also needed to poweroff the instant cloned module.
- The powered off VM would in turn be deleted by again using [community.vmware.vmware_guest](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) module.
- Thus [community.vmware.vmware_guest](vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) module is necessary for removing Instant Cloned VM when VMs being created in testing environment.
- Also GuestOS Customization has now been added with guestinfo_vars parameter.
- The Parent VM must have The Guest customization Engine for instant Clone to customize Guest OS.
- Only Linux Os in Parent VM enable support for native vSphere Guest Customization for Instant Clone in vSphere 7.

## [Parameters](vmware_guest_instant_clone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Name of the datacenter, where VM to be deployed. |
| **datastore**  string / required | The name of the datastore or the datastore cluster.  If datastore cluster name is specified, module will find the Storage DRS recommended datastore in that cluster. |
| **folder**  string | Destination folder, absolute path to deploy the cloned vm.  This parameter is case sensitive.  Examples:  folder: ha-datacenter/vm  folder: /datacenter1/vm |
| **guestinfo_vars**  list / elements=dictionary | Provides GuestOS Customization functionality in instant cloned VM.  A list of key value pairs that will be passed to the destination VM.  These pairs should be used to provide user-defined customization to differentiate the destination VM from the source VM. |
| **dns**  string | dns is used to set the dns in Instant Cloned Guest Operating System.. |
| **domain**  string | domain is used to set A fully qualified domain name (FQDN) or complete domain name for Instant Cloned Guest operating System. |
| **gateway**  string | netmask is used to set the netmask in Instant Cloned Guest Operating System. |
| **hostname**  string | hostname is used to obtain the DNS(Domain Name System) name and set the Guest system’s hostname. |
| **ipaddress**  string | ipaddress is used to set the ipaddress in Instant Cloned Guest Operating System. |
| **netmask**  string | netmask is used to set the netmask in Instant Cloned Guest Operating System. |
| **host**  aliases: esxi_hostname  string / required | Name of the ESX Host in datacenter in which to place cloned VM.  The host has to be a member of the cluster that contains the resource pool.  Required with *resource_pool* to find resource pool details. This will be used as additional information when there are resource pools with same name. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the vm instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `parent_vm` or `uuid` is not supplied. |
| **name**  aliases: vm_name  string / required | Name of the Cloned virtual machine. |
| **parent_vm**  string | Name of the parent virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string | Name of the resource pool in datacenter in which to place deployed VM.  Required if *cluster* is not specified.  For default or non-unique resource pool names, specify *host* and *cluster*.  `Resources` is the default name of resource pool. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the vm instance to clone from, this is VMware’s unique identifier.  This is a required parameter, if parameter `parent_vm` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vm_password**  string | The password used to login-in to the virtual machine.  Only required when using guest customization feature. |
| **vm_username**  string | The user to login-in to the virtual machine.  Only required when using guest customization feature. |
| **wait_vm_tools**  boolean | Whether waiting until vm tools start after rebooting an instant clone vm.  **Choices:**   - `false` - `true` ← (default) |
| **wait_vm_tools_timeout**  integer | Define a timeout (in seconds) for *the wait_vm_tools* parameter.  **Default:** `300` |

## [Notes](vmware_guest_instant_clone_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_instant_clone_module.md#id4)

```yaml+jinja
- name: Instant Clone a VM
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    folder: "{{ f0 }}"
    datastore: "{{ rw_datastore }}"
    datacenter: "{{ dc1 }}"
    host: "{{ esxi1 }}"
    name: "{{ Clone_vm }}"
    parent_vm: "{{ testvm_1 }}"
    resource_pool: "{{ test_resource_001 }}"
  register: vm_clone
  delegate_to: localhost

- name: set state to poweroff the Cloned VM
  community.vmware.vmware_guest_powerstate:
    validate_certs: false
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "cloned_vm_from_vm_cluster"
    folder: "{{ f0 }}"
    state: powered-off
  register: poweroff_instant_clone_from_vm_when_cluster
  delegate_to: localhost

- name: Clean VM
  community.vmware.vmware_guest:
    validate_certs: false
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "cloned_vm_from_vm_cluster"
    datacenter: "{{ dc1 }}"
    state: absent
  register: delete_instant_clone_from_vm_when_cluster
  ignore_errors: true
  delegate_to: localhost

- name: Instant Clone a VM with guest_customization
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vm_username: "root"
    vm_password: "SuperSecret"
    validate_certs: false
    folder: "{{ f0 }}"
    datastore: "{{ rw_datastore }}"
    datacenter: "{{ dc1 }}"
    host: "{{ esxi1 }}"
    guestinfo_vars:
      - hostname: "{{ guestinfo.ic.hostname }}"
        ipaddress: "{{ guestinfo.ic.ipaddress }}"
        netmask: "{{ guestinfo.ic.netmask }}"
        gateway: "{{ guestinfo.ic.gateway }}"
        dns: "{{ guestinfo.ic.dns }}"
        domain: "{{ guestinfo.ic.domain }}"
    name: "Instant_clone_guest_customize"
    parent_vm: "test_vm1"
    resource_pool: DC0_C0_RP1
  register: Instant_cloned_guest_customize
  delegate_to: localhost

- name: Instant Clone a VM when skipping optional params
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    name: "{{ Clone_vm }}"
    parent_vm: "{{ testvm_1 }}"
    datacenter: "{{ dc1 }}"
    datastore: "{{ rw_datastore }}"
    host: "{{ esxi1 }}"
  register: VM_clone_optional_arguments
  delegate_to: localhost

- name: Instant clone in check mode
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    folder: "{{ f0 }}"
    datastore: "{{ rw_datastore }}"
    datacenter: "{{ dc1 }}"
    host: "{{ esx1 }}"
    name: "{{ Clone_vm }}"
    parent_vm: "{{ testvm_2 }}"
    resource_pool: "{{ test_resource_001 }}"
  check_mode: true
  register: check_mode_clone
  delegate_to: localhost
- debug:
    var: check_mode_clone
```

## [Return Values](vmware_guest_instant_clone_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vm_info**  dictionary | metadata about the virtual machine  added instance_uuid from version 1.12.0  **Returned:** always  **Sample:** `{"datastore": "", "host": "", "instance_uuid": "", "vcenter": "", "vm_folder": "", "vm_name": ""}` |

### Authors

- Anant Chopra (@Anant99-sys)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
