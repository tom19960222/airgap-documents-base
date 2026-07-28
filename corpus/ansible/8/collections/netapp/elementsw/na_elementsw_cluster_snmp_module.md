---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_cluster_snmp module – Configure Element SW Cluster SNMP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_cluster_snmp_module.html
fetched_at: 2026-07-28T02:41:22+00:00
---
# netapp.elementsw.na_elementsw_cluster_snmp module – Configure Element SW Cluster SNMP

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
> see [Requirements](na_elementsw_cluster_snmp_module.md#ansible-collections-netapp-elementsw-na-elementsw-cluster-snmp-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_cluster_snmp`.

New in netapp.elementsw 2.8.0

- [Synopsis](na_elementsw_cluster_snmp_module.md#synopsis)
- [Requirements](na_elementsw_cluster_snmp_module.md#requirements)
- [Parameters](na_elementsw_cluster_snmp_module.md#parameters)
- [Notes](na_elementsw_cluster_snmp_module.md#notes)
- [Examples](na_elementsw_cluster_snmp_module.md#examples)
- [Return Values](na_elementsw_cluster_snmp_module.md#return-values)

## [Synopsis](na_elementsw_cluster_snmp_module.md#id1)

- Configure Element Software cluster SNMP.

## [Requirements](na_elementsw_cluster_snmp_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_cluster_snmp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **networks**  dictionary | List of networks and what type of access they have to the SNMP servers running on the cluster nodes.  This parameter is required if SNMP v3 is disabled. |
| **access**  string | ro for read-only access.  rw for read-write access.  rosys for read-only access to a restricted set of system information.  **Choices:**   - `"ro"` - `"rw"` - `"rosys"` |
| **cidr**  integer | A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. |
| **community**  string | SNMP community string. |
| **network**  string | This parameter along with the cidr variable is used to control which network the access and community string apply to.  The special value of ‘default’ is used to specify an entry that applies to all networks.  The cidr mask is ignored when network value is either a host name or default. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **snmp_v3_enabled**  boolean | Which version of SNMP has to be enabled.  **Choices:**   - `false` - `true` |
| **state**  string | This module enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to this module.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |
| **usm_users**  dictionary | List of users and the type of access they have to the SNMP servers running on the cluster nodes.  This parameter is required if SNMP v3 is enabled. |
| **access**  string | rouser for read-only access.  rwuser for read-write access.  rosys for read-only access to a restricted set of system information.  **Choices:**   - `"rouser"` - `"rwuser"` - `"rosys"` |
| **name**  string | The name of the user. Must contain at least one character, but no more than 32 characters.  Blank spaces are not allowed. |
| **passphrase**  string | The passphrase of the user. Must be between 8 and 255 characters long (inclusive).  Blank spaces are not allowed.  Required if ‘secLevel’ is ‘priv.’ |
| **password**  string | The password of the user. Must be between 8 and 255 characters long (inclusive).  Blank spaces are not allowed.  Required if ‘secLevel’ is ‘auth’ or ‘priv.’ |
| **secLevel**  string | To define the security level of a user.  **Choices:**   - `"noauth"` - `"auth"` - `"priv"` |

## [Notes](na_elementsw_cluster_snmp_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_cluster_snmp_module.md#id5)

```yaml+jinja
- name: configure SnmpNetwork
  tags:
  - elementsw_cluster_snmp
  na_elementsw_cluster_snmp:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    snmp_v3_enabled: True
    usm_users:
      access: rouser
      name: testuser
      password: ChangeMe123
      passphrase: ChangeMe123
      secLevel: auth
    networks:
      access: ro
      cidr: 24
      community: TestNetwork
      network: 192.168.0.1

- name: Disable SnmpNetwork
  tags:
  - elementsw_cluster_snmp
  na_elementsw_cluster_snmp:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
```

## [Return Values](na_elementsw_cluster_snmp_module.md#id6)

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
