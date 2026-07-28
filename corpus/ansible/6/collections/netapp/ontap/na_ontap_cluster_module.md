---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_cluster module – NetApp ONTAP cluster - create a cluster and add/remove nodes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_cluster_module.html
fetched_at: 2026-07-28T00:12:09+00:00
---
# netapp.ontap.na_ontap_cluster module – NetApp ONTAP cluster - create a cluster and add/remove nodes.

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_cluster_module.md#ansible-collections-netapp-ontap-na-ontap-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_cluster`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_cluster_module.md#synopsis)
- [Requirements](na_ontap_cluster_module.md#requirements)
- [Parameters](na_ontap_cluster_module.md#parameters)
- [Notes](na_ontap_cluster_module.md#notes)
- [Examples](na_ontap_cluster_module.md#examples)

## [Synopsis](na_ontap_cluster_module.md#id1)

- Create ONTAP cluster.
- Add or remove cluster nodes using cluster_ip_address.
- Adding a node requires ONTAP 9.3 or better.
- Removing a node requires ONTAP 9.4 or better.

## [Requirements](na_ontap_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **cluster_contact**  string  added in netapp.ontap 19.11.0 | Cluster contact, only relevant if performing a modify action. |
| **cluster_ip_address**  string | intra cluster IP address of the node to be added or removed. |
| **cluster_location**  string  added in netapp.ontap 19.11.0 | Cluster location, only relevant if performing a modify action. |
| **cluster_name**  string | The name of the cluster to manage. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force**  boolean  added in netapp.ontap 21.13.0 | forcibly remove a node that is down and cannot be brought online to remove its shared resources.  Choices:   - `false` ← (default) - `true` |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **node_name**  string  added in netapp.ontap 20.9.0 | Name of the node to be added or removed from the cluster.  Be aware that when adding a node, ‘-’ are converted to ‘_’ by the ONTAP backend.  When creating a cluster, `node_name` is ignored.  When adding a node using `cluster_ip_address`, `node_name` is optional.  When used to remove a node, `cluster_ip_address` and `node_name` are mutually exclusive. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **single_node_cluster**  boolean  added in netapp.ontap 19.11.0 | Whether the cluster is a single node cluster. Ignored for 9.3 or older versions.  If present, it was observed that ‘Cluster’ interfaces were deleted, whatever the value with ZAPI.  Choices:   - `false` - `true` |
| **state**  string | Whether the specified cluster should exist (deleting a cluster is not supported).  Whether the node identified by its cluster_ip_address should be in the cluster or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **time_out**  integer  added in netapp.ontap 21.1.0 | time to wait for cluster creation in seconds.  Error out if task is not completed in defined time.  if 0, the request is asynchronous.  default is set to 3 minutes.  Default: `180` |
| **timezone**  dictionary  added in netapp.ontap 21.24.0 | timezone for the cluster. Only supported by REST. |
| **name**  string | The timezone name must be  A geographic region, usually expressed as area/location  Greenwich Mean Time (GMT) or the difference in hours from GMT  A valid alias; that is, a term defined by the standard to refer to a geographic region or GMT  A system-specific or other term not associated with a geographic region or GMT  full list of supported alias can be found here: <https://library.netapp.com/ecmdocs/ECMP1155590/html/GUID-D3B8A525-67A2-4BEE-99DB-EF52D6744B5F.html>  Only supported by REST |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](na_ontap_cluster_module.md#id4)

> **Note:**
>
> - supports REST and ZAPI
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_cluster_module.md#id5)

```yaml+jinja
- name: Create cluster
  netapp.ontap.na_ontap_cluster:
    state: present
    cluster_name: new_cluster
    time_out: 0
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Add node to cluster (Join cluster)
  netapp.ontap.na_ontap_cluster:
    state: present
    cluster_ip_address: 10.10.10.10
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Add node to cluster (Join cluster)
  netapp.ontap.na_ontap_cluster:
    state: present
    cluster_ip_address: 10.10.10.10
    node_name: my_preferred_node_name
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Create a 2 node cluster in one call
  netapp.ontap.na_ontap_cluster:
    state: present
    cluster_name: new_cluster
    cluster_ip_address: 10.10.10.10
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Remove node from cluster
  netapp.ontap.na_ontap_cluster:
    state: absent
    cluster_ip_address: 10.10.10.10
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Remove node from cluster
  netapp.ontap.na_ontap_cluster:
    state: absent
    node_name: node002
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: modify cluster
  netapp.ontap.na_ontap_cluster:
    state: present
    cluster_contact: testing
    cluster_location: testing
    cluster_name: "{{ netapp_cluster}}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
