---
collection: ansible
version: "6"
title: "community.vmware.vmware_vspan_session module – Create or remove a Port Mirroring session."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vspan_session_module.html
fetched_at: 2026-07-27T17:23:02+00:00
---
# community.vmware.vmware_vspan_session module – Create or remove a Port Mirroring session.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_vspan_session`.

- [Synopsis](vmware_vspan_session_module.md#synopsis)
- [Parameters](vmware_vspan_session_module.md#parameters)
- [Notes](vmware_vspan_session_module.md#notes)
- [Examples](vmware_vspan_session_module.md#examples)

## [Synopsis](vmware_vspan_session_module.md#id1)

- This module can be used to create, delete or edit different kind of port mirroring sessions.

## [Parameters](vmware_vspan_session_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description for the session. |
| **destination_port**  string | Destination port that received the mirrored packets.  Also any port designated in the value of this property can not match the source port in any of the Distributed Port Mirroring session. |
| **destination_vm**  dictionary | With this parameter it is possible, to add a NIC of a VM to a port mirroring session. |
| **name**  string | Name of the VM. |
| **nic_label**  string | Label of the network interface card to use. |
| **enabled**  boolean | Whether the session is enabled.  Choices:   - `false` - `true` ← (default) |
| **encapsulation_vlan_id**  integer | VLAN ID used to encapsulate the mirrored traffic. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **mirrored_packet_length**  integer | An integer that describes how much of each frame to mirror.  If unset, all of the frame would be mirrored.  Setting this property to a smaller value is useful when the consumer will look only at the headers.  The value cannot be less than 60. |
| **name**  string / required | Name of the session. |
| **normal_traffic_allowed**  boolean | Whether or not destination ports can send and receive “normal” traffic.  Setting this to false will make mirror ports be used solely for mirroring and not double as normal access ports.  Choices:   - `false` - `true` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **sampling_rate**  integer | Sampling rate of the session.  If its value is n, one of every n packets is mirrored.  Valid values are between 1 to 65535. |
| **session_type**  string | Select the mirroring type.  In `encapsulatedRemoteMirrorSource` session, Distributed Ports can be used as source entities, and IP address can be used as destination entities.  In `remoteMirrorDest` session, VLAN IDs can be used as source entities, and Distributed Ports can be used as destination entities.  In `remoteMirrorSource` session, Distributed Ports can be used as source entities, and uplink ports name can be used as destination entities.  In `dvPortMirror` session, Distributed Ports can be used as both source and destination entities.  Choices:   - `"encapsulatedRemoteMirrorSource"` - `"remoteMirrorDest"` - `"remoteMirrorSource"` - `"dvPortMirror"` ← (default) |
| **source_port_received**  string | Source port for which received packets are mirrored. |
| **source_port_transmitted**  string | Source port for which transmitted packets are mirrored. |
| **source_vm_received**  dictionary | With this parameter it is possible, to add a NIC of a VM to a port mirroring session. |
| **name**  string | Name of the VM. |
| **nic_label**  string | Label of the network interface card to use. |
| **source_vm_transmitted**  dictionary | With this parameter it is possible, to add a NIC of a VM to a port mirroring session. |
| **name**  string | Name of the VM. |
| **nic_label**  string | Label of the network interface card to use. |
| **state**  string / required | Create or remove the session.  Choices:   - `"present"` - `"absent"` |
| **strip_original_vlan**  boolean | Whether to strip the original VLAN tag.  If false, the original VLAN tag will be preserved on the mirrored traffic.  If `encapsulationVlanId` has been set and this property is false, the frames will be double tagged with the original VLAN ID as the inner tag.  Choices:   - `false` - `true` |
| **switch**  aliases: switch_name  string / required | The name of the distributed vSwitch on which to add or remove the mirroring session. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_vspan_session_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vspan_session_module.md#id4)

```yaml+jinja
- name: Create distributed mirroring session.
  community.vmware.vmware_vspan_session:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch_name: dvSwitch
    state: present
    name: Basic Session
    enabled: True
    description: "Example description"
    source_port_transmitted: 817
    source_port_received: 817
    destination_port: 815
  delegate_to: localhost

- name: Create remote destination mirroring session.
  community.vmware.vmware_vspan_session:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch_name: dvSwitch
    state: present
    name: Remote Session
    enabled: True
    description: "Example description"
    source_port_received: 105
    destination_port: 815
    session_type: "remoteMirrorDest"
  delegate_to: localhost

- name: Delete remote destination mirroring session.
  community.vmware.vmware_vspan_session:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch_name: dvSwitch
    state: absent
    name: Remote Session
  delegate_to: localhost
```

### Authors

- Peter Gyorgy (@gyorgypeter)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
