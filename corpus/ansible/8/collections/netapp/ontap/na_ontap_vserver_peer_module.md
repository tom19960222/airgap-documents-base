---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_vserver_peer module – NetApp ONTAP Vserver peering"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_vserver_peer_module.html
fetched_at: 2026-07-28T02:43:41+00:00
---
# netapp.ontap.na_ontap_vserver_peer module – NetApp ONTAP Vserver peering

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
> see [Requirements](na_ontap_vserver_peer_module.md#ansible-collections-netapp-ontap-na-ontap-vserver-peer-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_vserver_peer`.

New in netapp.ontap 2.7.0

- [Synopsis](na_ontap_vserver_peer_module.md#synopsis)
- [Requirements](na_ontap_vserver_peer_module.md#requirements)
- [Parameters](na_ontap_vserver_peer_module.md#parameters)
- [Notes](na_ontap_vserver_peer_module.md#notes)
- [Examples](na_ontap_vserver_peer_module.md#examples)

## [Synopsis](na_ontap_vserver_peer_module.md#id1)

- Create/Delete vserver peer

## [Requirements](na_ontap_vserver_peer_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_vserver_peer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **applications**  list / elements=string | List of applications which can make use of the peering relationship.  FlexCache supported from ONTAP 9.5 onwards. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **dest_hostname**  string | DEPRECATED - please use `peer_options`.  Destination hostname or IP address.  Required for creating the vserver peer relationship with a remote cluster. |
| **dest_password**  string | DEPRECATED - please use `peer_options`.  Destination password.  Optional if this is same as source password. |
| **dest_username**  string | DEPRECATED - please use `peer_options`.  Destination username.  Optional if this is same as source username. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **local_name_for_peer**  string | Specifies local name of the peer Vserver in the relationship.  Use this if you see “Error creating vserver peer … Vserver name conflicts with one of the following”. |
| **local_name_for_source**  string | Specifies local name of the source Vserver in the relationship.  Use this if you see “Error accepting vserver peer … System generated a name for the peer Vserver because of a naming conflict”. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **peer_cluster**  string | Specifies name of the peer Cluster.  Required for creating the vserver peer relationship with a remote cluster |
| **peer_options**  dictionary  *added in netapp.ontap 21.8.0* | IP address and connection options for the peer system.  If any if these options is not specified, the corresponding source option is used. |
| **cert_filepath**  string | path to SSL client cert file (.pem). |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  **Choices:**   - `false` - `true` |
| **key_filepath**  string | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **use_rest**  string | REST API if supported by the target system for all the resources and attributes the module requires. Otherwise will revert to ZAPI.  always – will always use the REST API  never – will always use the ZAPI  auto – will try to use the REST Api |
| **username**  aliases: user  string | Username when using basic authentication. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` |
| **peer_vserver**  string / required | Specifies name of the peer Vserver in the relationship. |
| **state**  string | Whether the specified vserver peer should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Specifies name of the source Vserver in the relationship. |

## [Notes](na_ontap_vserver_peer_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_vserver_peer_module.md#id5)

```yaml+jinja
- name: Source vserver peer create
  netapp.ontap.na_ontap_vserver_peer:
    state: present
    peer_vserver: ansible2
    peer_cluster: ansibleCluster
    local_name_for_peer: peername
    local_name_for_source: sourcename
    vserver: ansible
    applications: ['snapmirror']
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    peer_options:
      hostname: "{{ netapp_dest_hostname }}"

- name: vserver peer delete
  netapp.ontap.na_ontap_vserver_peer:
    state: absent
    peer_vserver: ansible2
    vserver: ansible
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Source vserver peer create - different credentials
  netapp.ontap.na_ontap_vserver_peer:
    state: present
    peer_vserver: ansible2
    peer_cluster: ansibleCluster
    local_name_for_peer: peername
    local_name_for_source: sourcename
    vserver: ansible
    applications: ['snapmirror']
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    peer_options:
      hostname: "{{ netapp_dest_hostname }}"
      cert_filepath: "{{ cert_filepath }}"
      key_filepath: "{{ key_filepath }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
