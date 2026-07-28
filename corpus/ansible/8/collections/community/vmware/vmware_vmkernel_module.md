---
collection: ansible
version: "8"
title: "community.vmware.vmware_vmkernel module – Manages a VMware VMkernel Adapter of an ESXi host."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vmkernel_module.html
fetched_at: 2026-07-28T02:01:23+00:00
---
# community.vmware.vmware_vmkernel module – Manages a VMware VMkernel Adapter of an ESXi host.

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
> To use it in a playbook, specify: `community.vmware.vmware_vmkernel`.

- [Synopsis](vmware_vmkernel_module.md#synopsis)
- [Parameters](vmware_vmkernel_module.md#parameters)
- [Notes](vmware_vmkernel_module.md#notes)
- [Examples](vmware_vmkernel_module.md#examples)
- [Return Values](vmware_vmkernel_module.md#return-values)

## [Synopsis](vmware_vmkernel_module.md#id1)

- This module can be used to manage the VMKernel adapters / VMKernel network interfaces of an ESXi host.
- The module assumes that the host is already configured with the Port Group in case of a vSphere Standard Switch (vSS).
- The module assumes that the host is already configured with the Distributed Port Group in case of a vSphere Distributed Switch (vDS).
- The module automatically migrates the VMKernel adapter from vSS to vDS or vice versa if present.

## [Parameters](vmware_vmkernel_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **device**  string | Search VMkernel adapter by device name.  The parameter is required only in case of `type` is set to `dhcp`. |
| **dvswitch_name**  aliases: dvswitch  string | The name of the vSphere Distributed Switch (vDS) where to add the VMKernel interface.  Required parameter only if `state` is set to `present`.  Optional parameter from version 2.8 and onwards. |
| **enable_ft**  boolean | Enable Fault Tolerance traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  **Choices:**   - `false` ← (default) - `true` |
| **enable_mgmt**  boolean | Enable Management traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  **Choices:**   - `false` ← (default) - `true` |
| **enable_provisioning**  boolean | Enable Provisioning traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  **Choices:**   - `false` ← (default) - `true` |
| **enable_replication**  boolean | Enable vSphere Replication traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  **Choices:**   - `false` ← (default) - `true` |
| **enable_replication_nfc**  boolean | Enable vSphere Replication NFC traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  **Choices:**   - `false` ← (default) - `true` |
| **enable_vmotion**  boolean | Enable vMotion traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  You cannot enable vMotion on an additional adapter if you already have an adapter with the vMotion TCP/IP stack configured.  **Choices:**   - `false` ← (default) - `true` |
| **enable_vsan**  boolean | Enable VSAN traffic on the VMKernel adapter.  This option is only allowed if the default TCP/IP stack is used.  **Choices:**   - `false` ← (default) - `true` |
| **esxi_hostname**  string / required | Name of ESXi host to which VMKernel is to be managed.  From version 2.5 onwards, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **mtu**  integer | The MTU for the VMKernel interface.  The default value of 1500 is valid from version 2.5 and onwards.  **Default:** `1500` |
| **network**  dictionary | A dictionary of network details.  **Default:** `{"tcpip_stack": "default", "type": "static"}` |
| **default_gateway**  string | Default gateway (Override default gateway for this adapter). |
| **ip_address**  string | Static IP address.  Required if `type` is set to `static`. |
| **subnet_mask**  string | Static netmask required.  Required if `type` is set to `static`. |
| **tcpip_stack**  string | The TCP/IP stack for the VMKernel interface.  **Choices:**   - `"default"` ← (default) - `"provisioning"` - `"vmotion"` - `"vxlan"` |
| **type**  string | Type of IP assignment.  **Choices:**   - `"static"` ← (default) - `"dhcp"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **portgroup_name**  aliases: portgroup  string / required | The name of the port group for the VMKernel interface. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, the VMKernel adapter will be created with the given specifications.  If set to `absent`, the VMKernel adapter will be removed.  If set to `present` and VMKernel adapter exists, the configurations will be updated.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vswitch_name**  aliases: vswitch  string | The name of the vSwitch where to add the VMKernel interface.  Required parameter only if `state` is set to `present`.  Optional parameter from version 2.5 and onwards. |

## [Notes](vmware_vmkernel_module.md#id3)

> **Note:**
>
> - The option `device` need to be used with DHCP because otherwise it’s not possible to check if a VMkernel device is already present
> - You can only change from DHCP to static, and vSS to vDS, or vice versa, in one step, without creating a new device, with `device` specified.
> - You can only create the VMKernel adapter on a vDS if authenticated to vCenter and not if authenticated to ESXi.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vmkernel_module.md#id4)

```yaml+jinja
-  name: Add Management vmkernel port using static network type
   community.vmware.vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      esxi_hostname: '{{ esxi_hostname }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0001
      network:
        type: 'static'
        ip_address: 192.168.127.10
        subnet_mask: 255.255.255.0
      state: present
      enable_mgmt: true
   delegate_to: localhost

-  name: Add Management vmkernel port using DHCP network type
   community.vmware.vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      esxi_hostname: '{{ esxi_hostname }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0002
      state: present
      network:
        type: 'dhcp'
      enable_mgmt: true
   delegate_to: localhost

-  name: Change IP allocation from static to dhcp
   community.vmware.vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      esxi_hostname: '{{ esxi_hostname }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0002
      state: present
      device: vmk1
      network:
        type: 'dhcp'
      enable_mgmt: true
   delegate_to: localhost

-  name: Delete VMkernel port
   community.vmware.vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      esxi_hostname: '{{ esxi_hostname }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0002
      state: absent
   delegate_to: localhost

-  name: Add Management vmkernel port to Distributed Switch
   community.vmware.vmware_vmkernel:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      esxi_hostname: '{{ esxi_hostname }}'
      dvswitch_name: dvSwitch1
      portgroup_name: dvPG_0001
      network:
        type: 'static'
        ip_address: 192.168.127.10
        subnet_mask: 255.255.255.0
      state: present
      enable_mgmt: true
   delegate_to: localhost

-  name: Add vMotion vmkernel port with vMotion TCP/IP stack
   community.vmware.vmware_vmkernel:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      esxi_hostname: '{{ esxi_hostname }}'
      dvswitch_name: dvSwitch1
      portgroup_name: dvPG_0001
      network:
        type: 'static'
        ip_address: 192.168.127.10
        subnet_mask: 255.255.255.0
        tcpip_stack: vmotion
      state: present
   delegate_to: localhost
```

## [Return Values](vmware_vmkernel_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | metadata about VMKernel name  **Returned:** always  **Sample:** `{"changed": false, "device": "vmk1", "ipv4": "static", "ipv4_gw": "No override", "ipv4_ip": "192.168.1.15", "ipv4_sm": "255.255.255.0", "msg": "VMkernel Adapter already configured properly", "mtu": 9000, "services": "vMotion", "switch": "vDS"}` |

### Authors

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
