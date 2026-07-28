---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_igroup module – NetApp ONTAP iSCSI or FC igroup configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_igroup_module.html
fetched_at: 2026-07-28T02:42:19+00:00
---
# netapp.ontap.na_ontap_igroup module – NetApp ONTAP iSCSI or FC igroup configuration

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_igroup_module.md#ansible-collections-netapp-ontap-na-ontap-igroup-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_igroup`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_igroup_module.md#synopsis)
- [Requirements](na_ontap_igroup_module.md#requirements)
- [Parameters](na_ontap_igroup_module.md#parameters)
- [Notes](na_ontap_igroup_module.md#notes)
- [Examples](na_ontap_igroup_module.md#examples)

## [Synopsis](na_ontap_igroup_module.md#id1)

- Create/Delete/Rename Igroups and Modify initiators belonging to an igroup

## [Requirements](na_ontap_igroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_igroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bind_portset**  string | Name of a current portset to bind to the newly created igroup. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **force_remove_initiator**  aliases: allow_delete_while_mapped  boolean | Forcibly remove the initiator even if there are existing LUNs mapped to this initiator group.  This parameter should be used with caution.  **Choices:**   - `false` ← (default) - `true` |
| **from_name**  string  *added in netapp.ontap 2.7.0* | Name of igroup to rename to name. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **igroups**  list / elements=string  *added in netapp.ontap 21.3.0* | List of igroups to be mapped to the igroup.  For a modify operation, this list replaces the existing igroups, or existing initiators.  This module does not add or remove specific igroup(s) in an igroup.  Mutually exclusive with initiator_names (initiators) and initiator_objects.  Requires ONTAP 9.9 or newer. |
| **initiator_group_type**  aliases: protocol  string | Type of the initiator group.  Required when `state=present`.  **Choices:**   - `"fcp"` - `"iscsi"` - `"mixed"` |
| **initiator_names**  aliases: initiator, initiators  list / elements=string  *added in netapp.ontap 21.4.0* | List of initiators to be mapped to the igroup.  WWPN, WWPN Alias, or iSCSI name of Initiator to add or remove.  For a modify operation, this list replaces the existing initiators, or existing igroups.  This module does not add or remove specific initiator(s) in an igroup.  Mutually exclusive with igroups and initiator_objects.  This serves the same purpose as initiator_objects, but without the comment suboption. |
| **initiator_objects**  list / elements=dictionary  *added in netapp.ontap 21.4.0* | List of initiators to be mapped to the igroup, with an optional comment field.  WWPN, WWPN Alias, or iSCSI name of Initiator to add or remove.  For a modify operation, this list replaces the existing initiators, or existing igroups.  This module does not add or remove specific initiator(s) in an igroup.  Mutually exclusive with initiator_names (initiators) and igroups.  Requires ONTAP 9.9 with REST support. |
| **comment**  string | a more descriptive comment as the WWPN can be quite opaque. |
| **name**  string / required | name of the initiator. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  string / required | The name of the igroup to manage. |
| **ontapi**  integer | The ontap api version to use |
| **os_type**  aliases: ostype  string | OS type of the initiators within the group. |
| **password**  aliases: pass  string | Password for the specified user. |
| **state**  string | Whether the specified Igroup should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | The name of the vserver to use. |

## [Notes](na_ontap_igroup_module.md#id4)

> **Note:**
>
> - supports check mode.
> - supports ZAPI and REST.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_igroup_module.md#id5)

```yaml+jinja
- name: Create iSCSI Igroup
  netapp.ontap.na_ontap_igroup:
    state: present
    name: ansibleIgroup3
    initiator_group_type: iscsi
    os_type: linux
    initiator_names: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com,abc.com:redhat.com
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create iSCSI Igroup - ONTAP 9.9
  netapp.ontap.na_ontap_igroup:
    state: present
    name: ansibleIgroup3
    initiator_group_type: iscsi
    os_type: linux
    initiator_objects:
      - name: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com
        comment: for test only
      - name: abc.com:redhat.com
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create FC Igroup
  netapp.ontap.na_ontap_igroup:
    state: present
    name: ansibleIgroup4
    initiator_group_type: fcp
    os_type: linux
    initiator_names: 20:00:00:50:56:9f:19:82
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: rename Igroup
  netapp.ontap.na_ontap_igroup:
    state: present
    from_name: ansibleIgroup3
    name: testexamplenewname
    initiator_group_type: iscsi
    os_type: linux
    initiator_names: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify Igroup Initiators (replaces exisiting initiator_names)
  netapp.ontap.na_ontap_igroup:
    state: present
    name: ansibleIgroup3
    initiator_group_type: iscsi
    os_type: linux
    initiator: iqn.1994-05.com.redhat:scspa0395855001.rtp.openenglab.netapp.com
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete Igroup
  netapp.ontap.na_ontap_igroup:
    state: absent
    name: ansibleIgroup3
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
