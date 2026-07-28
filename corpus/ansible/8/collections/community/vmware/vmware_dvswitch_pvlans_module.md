---
collection: ansible
version: "8"
title: "community.vmware.vmware_dvswitch_pvlans module – Manage Private VLAN configuration of a Distributed Switch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_dvswitch_pvlans_module.html
fetched_at: 2026-07-28T02:00:01+00:00
---
# community.vmware.vmware_dvswitch_pvlans module – Manage Private VLAN configuration of a Distributed Switch

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
> To use it in a playbook, specify: `community.vmware.vmware_dvswitch_pvlans`.

- [Synopsis](vmware_dvswitch_pvlans_module.md#synopsis)
- [Parameters](vmware_dvswitch_pvlans_module.md#parameters)
- [Notes](vmware_dvswitch_pvlans_module.md#notes)
- [Examples](vmware_dvswitch_pvlans_module.md#examples)
- [Return Values](vmware_dvswitch_pvlans_module.md#return-values)

## [Synopsis](vmware_dvswitch_pvlans_module.md#id1)

- This module can be used to configure Private VLANs (PVLANs) on a Distributed Switch.

## [Parameters](vmware_dvswitch_pvlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **primary_pvlans**  list / elements=dictionary | A list of VLAN IDs that should be configured as Primary PVLANs.  If `primary_pvlans` isn’t specified, all PVLANs will be deleted if present.  Each member of the list requires primary_pvlan_id (int) set.  The secondary promiscuous PVLAN will be created automatically.  If `secondary_pvlans` isn’t specified, the primary PVLANs and each secondary promiscuous PVLAN will be created.  Please see examples for more information.  **Default:** `[]` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **secondary_pvlans**  list / elements=dictionary | A list of VLAN IDs that should be configured as Secondary PVLANs.  `primary_pvlans` need to be specified to create any Secondary PVLAN.  If `primary_pvlans` isn’t specified, all PVLANs will be deleted if present.  Each member of the list requires primary_pvlan_id (int), secondary_pvlan_id (int), and pvlan_type (str) to be set.  The type of the secondary PVLAN can be isolated or community. The secondary promiscuous PVLAN will be created automatically.  Please see examples for more information.  **Default:** `[]` |
| **switch**  aliases: dvswitch  string / required | The name of the Distributed Switch. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_dvswitch_pvlans_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvswitch_pvlans_module.md#id4)

```yaml+jinja
- name: Create PVLANs on a Distributed Switch
  community.vmware.vmware_dvswitch_pvlans:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    primary_pvlans:
      - primary_pvlan_id: 1
      - primary_pvlan_id: 4
    secondary_pvlans:
      - primary_pvlan_id: 1
        secondary_pvlan_id: 2
        pvlan_type: isolated
      - primary_pvlan_id: 1
        secondary_pvlan_id: 3
        pvlan_type: community
      - primary_pvlan_id: 4
        secondary_pvlan_id: 5
        pvlan_type: community
  delegate_to: localhost

- name: Create primary PVLAN and secondary promiscuous PVLAN on a Distributed Switch
  community.vmware.vmware_dvswitch_pvlans:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    primary_pvlans:
      - primary_pvlan_id: 1
  delegate_to: localhost

- name: Remove all PVLANs from a Distributed Switch
  community.vmware.vmware_dvswitch_pvlans:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    primary_pvlans: []
    secondary_pvlans: []
  delegate_to: localhost
```

## [Return Values](vmware_dvswitch_pvlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  **Returned:** always  **Sample:** `"{'changed': True, 'dvswitch': 'dvSwitch', 'private_vlans': [{'primary_pvlan_id': 1, 'pvlan_type': 'promiscuous', 'secondary_pvlan_id': 1}, {'primary_pvlan_id': 1, 'pvlan_type': 'isolated', 'secondary_pvlan_id': 2}, {'primary_pvlan_id': 1, 'pvlan_type': 'community', 'secondary_pvlan_id': 3}], 'private_vlans_previous': [], 'result': 'All private VLANs added'}"` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
