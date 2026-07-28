---
collection: ansible
version: "6"
title: "community.vmware.vca_vapp module – Manages vCloud Air vApp instances."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vca_vapp_module.html
fetched_at: 2026-07-27T17:21:15+00:00
---
# community.vmware.vca_vapp module – Manages vCloud Air vApp instances.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vca_vapp_module.md#ansible-collections-community-vmware-vca-vapp-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vca_vapp`.

- [DEPRECATED](vca_vapp_module.md#deprecated)
- [Synopsis](vca_vapp_module.md#synopsis)
- [Requirements](vca_vapp_module.md#requirements)
- [Parameters](vca_vapp_module.md#parameters)
- [Notes](vca_vapp_module.md#notes)
- [Examples](vca_vapp_module.md#examples)
- [Status](vca_vapp_module.md#status)

## [DEPRECATED](vca_vapp_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Module depends upon deprecated version of Pyvcloud library.

Alternative:
:   Use <https://github.com/vmware/ansible-module-vcloud-director> instead.

## [Synopsis](vca_vapp_module.md#id2)

- This module will actively managed vCloud Air vApp instances. Instances can be created and deleted as well as both deployed and undeployed.

## [Requirements](vca_vapp_module.md#id3)

The below requirements are needed on the host that executes this module.

- pyvcloud <= 18.2.2

## [Parameters](vca_vapp_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_version**  string | The api version to be used with the vca  Default: `"5.7"` |
| **gateway_name**  string | The name of the gateway of the vdc where the rule should be added.  Default: `"gateway"` |
| **host**  string | The authentication host to be used when service type is vcd. |
| **instance_id**  string | The instance id in a vchs environment to be used for creating the vapp |
| **network_mode**  string | Configures the mode of the network connection.  Choices:   - `"pool"` ← (default) - `"dhcp"` - `"static"` |
| **network_name**  string | The name of the network that should be attached to the virtual machine in the vApp. The virtual network specified must already be created in the vCloud Air VDC. If the *state* is not ‘absent’ then the *network_name* argument must be provided. |
| **operation**  string | Specifies an operation to be performed on the vApp.  Choices:   - `"noop"` ← (default) - `"poweron"` - `"poweroff"` - `"suspend"` - `"shutdown"` - `"reboot"` - `"reset"` |
| **org**  string | The org to login to for creating vapp, mostly set when the service_type is vdc. |
| **password**  aliases: pass, passwd  string | The vCloud Air password to use during authentication |
| **service_type**  string | The type of service we are authenticating against  Choices:   - `"vca"` ← (default) - `"vchs"` - `"vcd"` |
| **state**  string | Configures the state of the vApp.  Choices:   - `"present"` ← (default) - `"absent"` - `"deployed"` - `"undeployed"` |
| **template_name**  string | The name of the vApp template to use to create the vApp instance. If the *state* is not `absent` then the *template_name* value must be provided. The *template_name* must be previously uploaded to the catalog specified by *catalog_name* |
| **username**  aliases: user  string | The vCloud Air username to use during authentication |
| **validate_certs**  aliases: verify_certs  boolean | If the certificates of the authentication is to be verified.  Choices:   - `false` - `true` ← (default) |
| **vapp_name**  string / required | The name of the vCloud Air vApp instance |
| **vdc_name**  string | The name of the virtual data center (VDC) where the vm should be created or contains the vAPP. |
| **vm_cpus**  string | The number of vCPUs to configure for the VM in the vApp. If the *vm_name* argument is provided, then this becomes a per VM setting otherwise it is applied to all VMs in the vApp. |
| **vm_memory**  string | The amount of memory in MB to allocate to VMs in the vApp. If the *vm_name* argument is provided, then this becomes a per VM setting otherwise it is applied to all VMs in the vApp. |
| **vm_name**  string | The name of the virtual machine instance in the vApp to manage. |

## [Notes](vca_vapp_module.md#id5)

> **Note:**
>
> - VMware sold their vCloud Air service in Q2 2017.
> - VMware made significant changes to the pyvcloud interface around this time. The `vca_vapp` module relies on now deprecated code.
> - Mileage with `vca_vapp` may vary as vCloud Director APIs advance.
> - A viable alternative maybe <https://github.com/vmware/ansible-module-vcloud-director>

## [Examples](vca_vapp_module.md#id6)

```yaml+jinja
- name: Creates a new vApp in a VCA instance
  community.vmware.vca_vapp:
    vapp_name: tower
    state: present
    template_name: 'Ubuntu Server 12.04 LTS (amd64 20150127)'
    vdc_name: VDC1
    instance_id: '<your instance id here>'
    username: '<your username here>'
    password: '<your password here>'
  delegate_to: localhost
```

## [Status](vca_vapp_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vca_vapp_module.md#deprecated).

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
