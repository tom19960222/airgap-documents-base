---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_initiators module – Manage Element SW initiators"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_initiators_module.html
fetched_at: 2026-07-28T00:11:50+00:00
---
# netapp.elementsw.na_elementsw_initiators module – Manage Element SW initiators

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
> see [Requirements](na_elementsw_initiators_module.md#ansible-collections-netapp-elementsw-na-elementsw-initiators-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_initiators`.

New in netapp.elementsw 2.8.0

- [Synopsis](na_elementsw_initiators_module.md#synopsis)
- [Requirements](na_elementsw_initiators_module.md#requirements)
- [Parameters](na_elementsw_initiators_module.md#parameters)
- [Notes](na_elementsw_initiators_module.md#notes)
- [Examples](na_elementsw_initiators_module.md#examples)
- [Return Values](na_elementsw_initiators_module.md#return-values)

## [Synopsis](na_elementsw_initiators_module.md#id1)

- Manage Element Software initiators that allow external clients access to volumes.

## [Requirements](na_elementsw_initiators_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_initiators_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **initiators**  list / elements=dictionary | A list of objects containing characteristics of each initiator. |
| **alias**  string | The friendly name assigned to this initiator. |
| **attributes**  dictionary | A set of JSON attributes to assign to this initiator. |
| **initiator_id**  integer | The numeric ID of the initiator. |
| **name**  string / required | The name of the initiator. |
| **volume_access_group_id**  integer | volumeAccessGroupID to which this initiator belongs. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified initiator should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_initiators_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_initiators_module.md#id5)

```yaml+jinja
- name: Manage initiators
  tags:
  - na_elementsw_initiators
  na_elementsw_initiators:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    initiators:
    - name: a
      alias: a1
      initiator_id: 1
      volume_access_group_id: 1
      attributes: {"key": "value"}
    - name: b
      alias: b2
      initiator_id: 2
      volume_access_group_id: 2
  state: present
```

## [Return Values](na_elementsw_initiators_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
