---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_network module – Manage network adapters of specified virtual machine in given vCenter infrastructure"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_network_module.html
fetched_at: 2026-07-28T02:00:17+00:00
---
# community.vmware.vmware_guest_network module – Manage network adapters of specified virtual machine in given vCenter infrastructure

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_network`.

- [Synopsis](vmware_guest_network_module.md#synopsis)
- [Parameters](vmware_guest_network_module.md#parameters)
- [Notes](vmware_guest_network_module.md#notes)
- [Examples](vmware_guest_network_module.md#examples)
- [Return Values](vmware_guest_network_module.md#return-values)

## [Synopsis](vmware_guest_network_module.md#id1)

- This module is used to add, reconfigure, remove network adapter of given virtual machine.

## [Parameters](vmware_guest_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_guest_os_mtu_change**  boolean  *added in community.vmware 2.3.0* | Allows the guest OS to change the MTU on a SR-IOV network adapter.  This option is only compatible for SR-IOV network adapters.  **Choices:**   - `false` - `true` ← (default) |
| **cluster**  string | Name of cluster where VM belongs to. |
| **connected**  boolean | If NIC should be connected to the network.  **Choices:**   - `false` - `true` ← (default) |
| **datacenter**  string | Datacenter the VM belongs to.  **Default:** `"ha-datacenter"` |
| **device_type**  string | Type of virtual network device.  Valid choices are - `e1000`, `e1000e`, `pcnet32`, `vmxnet2`, `vmxnet3` (default), `sriov`, `pvrdma`.  **Default:** `"vmxnet3"` |
| **directpath_io**  boolean | Enable Universal Pass-through (UPT).  Only compatible with the `vmxnet3` device type.  **Choices:**   - `false` ← (default) - `true` |
| **esxi_hostname**  string | The hostname of the ESXi host where the VM belongs to. |
| **folder**  string | Folder location of given VM, this is only required when there’s multiple VM’s with the same name. |
| **force**  boolean | Force adapter creation even if an existing adapter is attached to the same network.  **Choices:**   - `false` ← (default) - `true` |
| **gather_network_info**  aliases: gather_network_facts  boolean | Return information about current guest network adapters.  **Choices:**   - `false` ← (default) - `true` |
| **guest_control**  boolean | Enables guest control over whether the connectable device is connected.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **label**  string | Label of the NIC that should be altered. `mac_address` or `label` should be set to get the corresponding device to reconfigure.  Alter the name of the network adapter. |
| **mac_address**  string | MAC address of the NIC that should be altered, if a MAC address is not supplied a new nic will be created.  Required when *state=absent*. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  Required if `uuid` or `name` is not supplied. |
| **name**  string | Name of virtual machine  Required if `uuid` or `moid` is not supplied. |
| **network_name**  string | Name of network in vSphere. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **physical_function_backing**  string  *added in community.vmware 2.3.0* | If set, specifies the PCI ID of the physical function to use as backing for a SR-IOV network adapter.  This option is only compatible for SR-IOV network adapters. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **pvrdma_device_protocol**  string  *added in community.vmware 3.3.0* | The PVRDMA device protocol used. Valid choices are - `rocev1`, `rocev2`.  This parameter is only used on the VM with hardware version >=14 and <= 19. |
| **start_connected**  boolean | If NIC should be connected to network on startup.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | NIC state.  When `state=present`, a nic will be added if a mac address or label does not previously exists or is unset.  When `state=absent`, the *mac_address* parameter has to be set.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **switch**  string | Name of the (dv)switch for destination network, this is only required for dvswitches. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | vm uuid  Required if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **virtual_function_backing**  string  *added in community.vmware 2.3.0* | If set, specifies the PCI ID of the physical function to use as backing for a SR-IOV network adapter.  This option is only compatible for SR-IOV network adapters. |
| **vlan_id**  integer | VLAN id associated with the network. |
| **wake_onlan**  boolean | Enable wake on LAN.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vmware_guest_network_module.md#id3)

> **Note:**
>
> - For backwards compatibility network_data is returned when using the gather_network_info parameter
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_network_module.md#id4)

```yaml+jinja
- name: change network for 00:50:56:11:22:33 on vm01.domain.fake
  community.vmware.vmware_guest_network:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: vm01.domain.fake
    mac_address: 00:50:56:11:22:33
    network_name: admin-network
    state: present

- name: add a nic on network with vlan id 2001 for 422d000d-2000-ffff-0000-b00000000000
  community.vmware.vmware_guest_network:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    uuid: 422d000d-2000-ffff-0000-b00000000000
    vlan_id: 2001

- name: remove nic with mac 00:50:56:11:22:33 from vm01.domain.fake
  community.vmware.vmware_guest_network:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    mac_address: 00:50:56:11:22:33
    name: vm01.domain.fake
    state: absent

- name: add multiple nics to vm01.domain.fake
  community.vmware.vmware_guest_network:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: vm01.domain.fake
    state: present
    vlan_id: "{{ item.vlan_id | default(omit) }}"
    network_name: "{{ item.network_name | default(omit) }}"
    connected: "{{ item.connected | default(omit) }}"
  loop:
    - vlan_id: 2000
      connected: false
    - network_name: guest-net
      connected: true
```

## [Return Values](vmware_guest_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network_data**  dictionary | For backwards compatibility, metadata about the virtual machine network adapters  **Returned:** when using gather_network_info parameter  **Sample:** `{"network_data": {"0": {"allow_guest_ctl": true, "connected": true, "device_type": "vmxnet3", "label": "Network adapter 2", "mac_addr": "00:50:56:AA:AA:AA", "mac_address": "00:50:56:AA:AA:AA", "name": "admin-net", "network_name": "admin-net", "start_connected": true, "switch": "vSwitch0", "unit_number": 8, "vlan_id": 10, "wake_onlan": false}, "1": {"allow_guest_ctl": true, "connected": true, "device_type": "vmxnet3", "label": "Network adapter 1", "mac_addr": "00:50:56:BB:BB:BB", "mac_address": "00:50:56:BB:BB:BB", "name": "guest-net", "network_name": "guest-net", "start_connected": true, "switch": "vSwitch0", "unit_number": 7, "vlan_id": 10, "wake_onlan": true}}}` |
| **network_info**  list / elements=string | metadata about the virtual machine network adapters  **Returned:** always  **Sample:** `{"network_info": [{"allow_guest_ctl": true, "connected": true, "device_type": "vmxnet3", "label": "Network adapter 2", "mac_address": "00:50:56:AA:AA:AA", "network_name": "admin-net", "start_connected": true, "switch": "vSwitch0", "unit_number": 8, "vlan_id": 10, "wake_onlan": false}, {"allow_guest_ctl": true, "connected": true, "device_type": "vmxnet3", "label": "Network adapter 1", "mac_address": "00:50:56:BB:BB:BB", "network_name": "guest-net", "start_connected": true, "switch": "vSwitch0", "unit_number": 7, "vlan_id": 10, "wake_onlan": true}]}` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
