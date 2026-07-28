---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_qos_policy module – NetApp Element Software create/modify/rename/delete QOS Policy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_qos_policy_module.html
fetched_at: 2026-07-28T00:11:53+00:00
---
# netapp.elementsw.na_elementsw_qos_policy module – NetApp Element Software create/modify/rename/delete QOS Policy

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/netapp/elementsw) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_qos_policy_module.md#ansible-collections-netapp-elementsw-na-elementsw-qos-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_qos_policy`.

New in netapp.elementsw 20.9.0

- [Synopsis](na_elementsw_qos_policy_module.md#synopsis)
- [Requirements](na_elementsw_qos_policy_module.md#requirements)
- [Parameters](na_elementsw_qos_policy_module.md#parameters)
- [Notes](na_elementsw_qos_policy_module.md#notes)
- [Examples](na_elementsw_qos_policy_module.md#examples)

## [Synopsis](na_elementsw_qos_policy_module.md#id1)

- Create, modify, rename, or delete QOS policy on Element Software Cluster.

## [Requirements](na_elementsw_qos_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_qos_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **debug**  boolean  added in netapp.elementsw 21.3.0 | report additional information when set to true.  Choices:   - `false` ← (default) - `true` |
| **from_name**  string | Name or id for the QOS policy to be renamed. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **name**  string / required | Name or id for the QOS policy. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **qos**  dictionary | The quality of service (QQOS) for the policy.  Required for create  Supported keys are minIOPS, maxIOPS, burstIOPS |
| **burstIOPS**  integer  added in netapp.elementsw 21.3.0 | The maximum number of IOPS allowed over a short period of time for the volume. |
| **maxIOPS**  integer  added in netapp.elementsw 21.3.0 | The maximum number of IOPS allowed for the volume. |
| **minIOPS**  integer  added in netapp.elementsw 21.3.0 | The minimum number of IOPS guaranteed for the volume. |
| **state**  string | Whether the specified QOS policy should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_qos_policy_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_qos_policy_module.md#id5)

```yaml+jinja
- name: Add QOS Policy
  na_elementsw_qos_policy:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: gold
    qos: {minIOPS: 1000, maxIOPS: 20000, burstIOPS: 50000}

- name: Modify QOS Policy
  na_elementsw_qos_policy:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    name: gold
    qos: {minIOPS: 100, maxIOPS: 5000, burstIOPS: 20000}

- name: Rename QOS Policy
  na_elementsw_qos_policy:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    from_name: gold
    name: silver

- name: Remove QOS Policy
  na_elementsw_qos_policy:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    name: silver
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
