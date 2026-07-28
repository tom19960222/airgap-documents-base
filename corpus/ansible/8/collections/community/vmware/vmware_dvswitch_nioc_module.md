---
collection: ansible
version: "8"
title: "community.vmware.vmware_dvswitch_nioc module – Manage distributed switch Network IO Control"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_dvswitch_nioc_module.html
fetched_at: 2026-07-28T02:00:00+00:00
---
# community.vmware.vmware_dvswitch_nioc module – Manage distributed switch Network IO Control

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
> To use it in a playbook, specify: `community.vmware.vmware_dvswitch_nioc`.

- [Synopsis](vmware_dvswitch_nioc_module.md#synopsis)
- [Parameters](vmware_dvswitch_nioc_module.md#parameters)
- [Notes](vmware_dvswitch_nioc_module.md#notes)
- [Examples](vmware_dvswitch_nioc_module.md#examples)
- [Return Values](vmware_dvswitch_nioc_module.md#return-values)

## [Synopsis](vmware_dvswitch_nioc_module.md#id1)

- This module can be used to manage distributed switch Network IO Control configurations.

## [Parameters](vmware_dvswitch_nioc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resources**  list / elements=dictionary | List of dicts containing.  **Default:** `[]` |
| **limit**  integer | The maximum allowed usage for a traffic class belonging to this resource pool per host physical NIC.  **Default:** `-1` |
| **name**  string / required | Resource name.  **Choices:**   - `"faultTolerance"` - `"hbr"` - `"iSCSI"` - `"management"` - `"nfs"` - `"vdp"` - `"virtualMachine"` - `"vmotion"` - `"vsan"` - `"backupNfc"` - `"nvmetcp"` |
| **reservation**  integer | Ignored if NIOC version is set to version2  Amount of bandwidth resource that is guaranteed available to the host infrastructure traffic class.  If the utilization is less than the reservation, the extra bandwidth is used for other host infrastructure traffic class types.  Reservation is not allowed to exceed the value of limit, if limit is set.  Unit is Mbits/sec.  Ignored unless version is “version3”.  Amount of bandwidth resource that is guaranteed available to the host infrastructure traffic class.  **Default:** `0` |
| **shares**  integer | The number of shares allocated.  Ignored unless `shares_level` is “custom”. |
| **shares_level**  string | The allocation level  The level is a simplified view of shares.  Levels map to a pre-determined set of numeric values for shares.  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"custom"` |
| **state**  string | Enable or disable NIOC on the distributed switch.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **switch**  aliases: dvswitch  string / required | The name of the distributed switch. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | Network IO control version.  **Choices:**   - `"version2"` - `"version3"` |

## [Notes](vmware_dvswitch_nioc_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvswitch_nioc_module.md#id4)

```yaml+jinja
- name: Enable NIOC
  community.vmware.vmware_dvswitch_nioc:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    version: version3
    resources:
        - name: vmotion
          limit: -1
          reservation: 128
          shares_level: normal
        - name: vsan
          limit: -1
          shares_level: custom
          shares: 99
          reservation: 256
    state: present
  delegate_to: localhost

- name: Disable NIOC
  community.vmware.vmware_dvswitch_nioc:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    switch: dvSwitch
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_dvswitch_nioc_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dvswitch_nioc_status**  string | result of the changes  **Returned:** success |
| **resources_changed**  list / elements=string | list of resources which were changed  **Returned:** success  **Sample:** `["vmotion", "vsan"]` |

### Authors

- Joseph Andreatta (@vmwjoseph)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
