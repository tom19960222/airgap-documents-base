---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_volume module – NetApp Element Software Manage Volumes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_volume_module.html
fetched_at: 2026-07-28T02:41:32+00:00
---
# netapp.elementsw.na_elementsw_volume module – NetApp Element Software Manage Volumes

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/ui/repo/published/netapp/elementsw/) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_volume_module.md#ansible-collections-netapp-elementsw-na-elementsw-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_volume`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_volume_module.md#synopsis)
- [Requirements](na_elementsw_volume_module.md#requirements)
- [Parameters](na_elementsw_volume_module.md#parameters)
- [Notes](na_elementsw_volume_module.md#notes)
- [Examples](na_elementsw_volume_module.md#examples)
- [Return Values](na_elementsw_volume_module.md#return-values)

## [Synopsis](na_elementsw_volume_module.md#id1)

- Create, destroy, or update volumes on ElementSW

## [Requirements](na_elementsw_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access**  string | Access allowed for the volume.  readOnly Only read operations are allowed.  readWrite Reads and writes are allowed.  locked No reads or writes are allowed.  replicationTarget Identify a volume as the target volume for a paired set of volumes.  If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source.  **Choices:**   - `"readOnly"` - `"readWrite"` - `"locked"` - `"replicationTarget"` |
| **account_id**  string / required | Account ID for the owner of this volume.  It accepts Account_id or Account_name |
| **attributes**  dictionary | A YAML dictionary of attributes that you would like to apply on this volume. |
| **enable512e**  aliases: enable512emulation  boolean | Required when `state=present`  Should the volume provide 512-byte sector emulation?  **Choices:**   - `false` - `true` |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **name**  string / required | The name of the volume to manage.  It accepts volume_name or volume_id |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **qos**  dictionary | Initial quality of service settings for this volume. Configure as dict in playbooks. |
| **qos_policy_name**  string | Quality of service policy for this volume.  It can be a name or an id.  Mutually exclusive with `qos` option. |
| **size**  integer | The size of the volume in (size_unit).  Required when `state = present`. |
| **size_unit**  string | The unit used to interpret the size parameter.  **Choices:**   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **state**  string | Whether the specified volume should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_volume_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_volume_module.md#id5)

```yaml+jinja
- name: Create Volume
  na_elementsw_volume:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: AnsibleVol
    qos: {minIOPS: 1000, maxIOPS: 20000, burstIOPS: 50000}
    account_id: 3
    enable512e: False
    size: 1
    size_unit: gb

- name: Update Volume
  na_elementsw_volume:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: AnsibleVol
    account_id: 3
    access: readWrite

- name: Delete Volume
  na_elementsw_volume:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    name: AnsibleVol
    account_id: 2
```

## [Return Values](na_elementsw_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
