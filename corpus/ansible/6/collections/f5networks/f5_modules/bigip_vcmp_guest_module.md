---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_vcmp_guest module – Manages vCMP guests on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_vcmp_guest_module.html
fetched_at: 2026-07-27T17:28:01+00:00
---
# f5networks.f5_modules.bigip_vcmp_guest module – Manages vCMP guests on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_vcmp_guest`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_vcmp_guest_module.md#synopsis)
- [Parameters](bigip_vcmp_guest_module.md#parameters)
- [Notes](bigip_vcmp_guest_module.md#notes)
- [Examples](bigip_vcmp_guest_module.md#examples)
- [Return Values](bigip_vcmp_guest_module.md#return-values)

## [Synopsis](bigip_vcmp_guest_module.md#id1)

- Manages vCMP (Virtual Clustered Multiprocessing) guests on a BIG-IP. This functionality only exists on actual hardware and must be enabled by provisioning `vcmp` with the `bigip_provision` module.

## [Parameters](bigip_vcmp_guest_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allowed_slots**  list / elements=string | Contains those slots to which the guest is allowed to be assigned.  When the host determines which slots this guest should be assigned, only slots in this list are considered.  This is a good way to force guests to be assigned only to particular slots, or, by configuring disjoint `allowed_slots` on two guests, that those guests are never assigned to the same slot.  By default, this list includes every available slot in the cluster. This means the guest may be assigned to any slot by default. |
| **cores_per_slot**  integer | Specifies the number of cores the system allocates to the guest.  Each core represents a portion of CPU and memory. Therefore, the amount of memory allocated per core is directly tied to the amount of CPU. This amount of memory varies per hardware platform type.  The number you can specify depends on the type of hardware you have.  In the event of a reboot, the system persists the guest to the same slot on which it ran prior to the reboot. |
| **delete_virtual_disk**  boolean | When `state` is `absent`, the system additionally deletes the virtual disk associated with the vCMP guest. By default, this value is `no`.  Choices:   - `false` ← (default) - `true` |
| **initial_hotfix**  string | Specifies the hotfix ISO image file which is applied on top of the base image. |
| **initial_image**  string | Specifies the base software release ISO image file for installing the TMOS hypervisor instance and any licensed BIG-IP modules onto the guest’s virtual disk. When creating a new guest, this parameter is required. Ensure this image is present on the VCMP host and not only on the VCMP guest. Also, the file reference for this image should be the one present on the host and not on the guest. |
| **mgmt_address**  string | Specifies the IP address and subnet or subnet mask you use to access the guest when you want to manage a module running within the guest. This parameter is required if the `mgmt_network` parameter is `bridged`.  When creating a new guest, if you do not specify a network or network mask, a default of `/24` (`255.255.255.0`) is used. |
| **mgmt_network**  string | Specifies the method by which the management address is used in the vCMP guest.  When `bridged`, specifies the guest can communicate with the vCMP host’s management network.  When `isolated`, specifies the guest is isolated from the vCMP host’s management network. In this case, the only way a guest can communicate with the vCMP host is through the console port or through a self IP address on the guest that allows traffic through port 22.  When `host only`, prevents the guest from installing images and hotfixes other than those provided by the hypervisor.  If the guest setting is `isolated` or `host only`, the `mgmt_address` does not apply.  For mode changing, changing `bridged` to `isolated` causes the vCMP host to remove all of the guest’s management interfaces from its bridged management network. This immediately disconnects the guest’s VMs from the physical management network. Changing `isolated` to `bridged` causes the vCMP host to dynamically add the guest’s management interfaces to the bridged management network. This immediately connects all of the guest’s VMs to the physical management network. Changing this property while the guest is in the `configured` or `provisioned` state has no immediate effect.  Choices:   - `"bridged"` - `"isolated"` - `"host only"` |
| **mgmt_route**  string | Specifies the gateway address for the `mgmt_address`.  If this value is not specified when creating a new guest, it is set to `none`.  The value `none` can be used during an update to remove this value. |
| **min_number_of_slots**  integer | Specifies the minimum number of slots the guest must be assigned to in order to deploy.  This field dictates the number of slots to which the guest must be assigned.  At the end of any allocation attempt, if the guest is not assigned to at least this many slots, the attempt fails and the change that initiated it is reverted.  A guest’s `min_number_of_slots` value cannot be greater than its `number_of_slots`. |
| **name**  string / required | The name of the vCMP guest to manage. |
| **number_of_slots**  integer | Specifies the number of slots for the system to use when creating the guest.  This value dictates how many cores a guest is allocated from each slot to which it is assigned.  Possible values are dependent on the type of blades being used in this cluster.  The default value depends on the type of blades being used in this cluster. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **state**  string | The state of the vCMP guest on the system. Each state implies the actions of all states before it.  When `configured`, guarantees the vCMP guest exists with the provided attributes. Additionally, ensures the vCMP guest is turned off.  When `disabled`, behaves the same way as `configured`, it is just a more user-friendly name.  When `provisioned`, ensures the guest is created and installed. This state does not start the guest; use `deployed` for that purpose. This state is one step beyond `present`, as `present` does not install the guest; only sets up the configuration for it to be installed.  When `present`, ensures the guest is properly provisioned and starts the guest so that it is in a running state.  When `absent`, removes the vCMP from the system.  Choices:   - `"configured"` - `"disabled"` - `"provisioned"` - `"present"` ← (default) - `"absent"` |
| **vlans**  list / elements=string | VLANs the guest uses to communicate with other guests, the host, and with the external network. The available VLANs in the list are those that are currently configured on the vCMP host.  The order of these VLANs is not important and is ignored. This module orders the VLANs automatically. Therefore, if you deliberately re-order them in subsequent tasks, this module does **not** register a change. |

## [Notes](bigip_vcmp_guest_module.md#id3)

> **Note:**
>
> - This module can take a lot of time to deploy vCMP guests. This is an intrinsic limitation of the vCMP system, because it is booting real VMs on the BIG-IP device. This boot time is very similar in length to the time it takes to boot VMs on any other virtualization platform; public or private.
> - When BIG-IP starts, the VMs are booted sequentially; not in parallel. This means it is not unusual for a vCMP host with many guests to take a long time (60+ minutes) to reboot and bring all the guests online. The BIG-IP chassis will be available before all vCMP guests are online.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_vcmp_guest_module.md#id4)

```yaml+jinja
- name: Create a vCMP guest
  bigip_vcmp_guest:
    name: foo
    mgmt_network: bridge
    mgmt_address: 10.20.30.40/24
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a vCMP guest with specific VLANs
  bigip_vcmp_guest:
    name: foo
    mgmt_network: bridge
    mgmt_address: 10.20.30.40/24
    vlans:
      - vlan1
      - vlan2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove vCMP guest and disk
  bigip_vcmp_guest:
    name: guest1
    state: absent
    delete_virtual_disk: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  register: result
```

## [Return Values](bigip_vcmp_guest_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vlans**  list / elements=string | The VLANs assigned to the vCMP guest, in their full path format.  Returned: changed  Sample: `["/Common/vlan1", "/Common/vlan2"]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
