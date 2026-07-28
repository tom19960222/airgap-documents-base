---
collection: ansible
version: "6"
title: "community.vmware.vmware_dvswitch_lacp module – Manage LACP configuration on a Distributed Switch"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_dvswitch_lacp_module.html
fetched_at: 2026-07-27T17:21:43+00:00
---
# community.vmware.vmware_dvswitch_lacp module – Manage LACP configuration on a Distributed Switch

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
> To use it in a playbook, specify: `community.vmware.vmware_dvswitch_lacp`.

- [Synopsis](vmware_dvswitch_lacp_module.md#synopsis)
- [Parameters](vmware_dvswitch_lacp_module.md#parameters)
- [Notes](vmware_dvswitch_lacp_module.md#notes)
- [Examples](vmware_dvswitch_lacp_module.md#examples)
- [Return Values](vmware_dvswitch_lacp_module.md#return-values)

## [Synopsis](vmware_dvswitch_lacp_module.md#id1)

- This module can be used to configure Link Aggregation Control Protocol (LACP) support mode and Link Aggregation Groups (LAGs).

## [Parameters](vmware_dvswitch_lacp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **link_aggregation_groups**  list / elements=dictionary | Can only be used if `lacp_support` is set to `enhanced`.  Default: `[]` |
| **load_balancing_mode**  string | Load balancing algorithm.  Valid values are as follows   - srcTcpUdpPort: Source TCP/UDP port number. - srcDestIpTcpUdpPortVlan: Source and destination IP, source and destination TCP/UDP port number and VLAN. - srcIpVlan: Source IP and VLAN. - srcDestTcpUdpPort: Source and destination TCP/UDP port number. - srcMac: Source MAC address. - destIp: Destination IP. - destMac: Destination MAC address. - vlan: VLAN only. - srcDestIp: Source and Destination IP. - srcIpTcpUdpPortVlan: Source IP, TCP/UDP port number and VLAN. - srcDestIpTcpUdpPort: Source and destination IP and TCP/UDP port number. - srcDestMac: Source and destination MAC address. - destIpTcpUdpPort: Destination IP and TCP/UDP port number. - srcPortId: Source Virtual Port Id. - srcIp: Source IP. - srcIpTcpUdpPort: Source IP and TCP/UDP port number. - destIpTcpUdpPortVlan: Destination IP, TCP/UDP port number and VLAN. - destTcpUdpPort: Destination TCP/UDP port number. - destIpVlan: Destination IP and VLAN. - srcDestIpVlan: Source and destination IP and VLAN.   Please see examples for more information.  Default: `"srcDestIpTcpUdpPortVlan"` |
| **mode**  string | The negotiating state of the uplinks/ports.  Choices:   - `"active"` - `"passive"` |
| **name**  string | Name of the LAG. |
| **uplink_number**  integer | Number of uplinks.  Can 1 to 30. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **support_mode**  string | The LACP support mode.  `basic`: One Link Aggregation Control Protocol group in the switch (singleLag).  `enhanced`: Multiple Link Aggregation Control Protocol groups in the switch (multipleLag).  Choices:   - `"basic"` ← (default) - `"enhanced"` |
| **switch**  aliases: dvswitch  string / required | The name of the Distributed Switch to manage. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_dvswitch_lacp_module.md#id3)

> **Note:**
>
> - You need to run the task two times if you want to remove all LAGs and change the support mode to ‘basic’
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvswitch_lacp_module.md#id4)

```yaml+jinja
- name: Enable enhanced mode on a Distributed Switch
  community.vmware.vmware_dvswitch_lacp:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    support_mode: enhanced
    validate_certs: "{{ validate_vcenter_certs }}"
  delegate_to: localhost
  loop_control:
    label: "{{ item.name }}"
  with_items: "{{ vcenter_distributed_switches }}"

- name: Enable enhanced mode and create two LAGs on a Distributed Switch
  community.vmware.vmware_dvswitch_lacp:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    support_mode: enhanced
    link_aggregation_groups:
        - name: lag1
          uplink_number: 2
          mode: active
          load_balancing_mode: srcDestIpTcpUdpPortVlan
        - name: lag2
          uplink_number: 2
          mode: passive
          load_balancing_mode: srcDestIp
    validate_certs: "{{ validate_vcenter_certs }}"
  delegate_to: localhost
  loop_control:
    label: "{{ item.name }}"
  with_items: "{{ vcenter_distributed_switches }}"
```

## [Return Values](vmware_dvswitch_lacp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  Returned: always  Sample: `"{'changed': True, 'dvswitch': 'dvSwitch', 'link_aggregation_groups': [{'load_balancing_mode': 'srcDestIpTcpUdpPortVlan', 'mode': 'active', 'name': 'lag1', 'uplink_number': 2}, {'load_balancing_mode': 'srcDestIp', 'mode': 'active', 'name': 'lag2', 'uplink_number': 2}], 'link_aggregation_groups_previous': [], 'result': 'lacp lags changed', 'support_mode': 'enhanced'}"` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
