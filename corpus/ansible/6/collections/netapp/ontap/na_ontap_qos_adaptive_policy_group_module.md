---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_qos_adaptive_policy_group module – NetApp ONTAP Adaptive Quality of Service policy group."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_qos_adaptive_policy_group_module.html
fetched_at: 2026-07-28T00:12:58+00:00
---
# netapp.ontap.na_ontap_qos_adaptive_policy_group module – NetApp ONTAP Adaptive Quality of Service policy group.

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
> see [Requirements](na_ontap_qos_adaptive_policy_group_module.md#ansible-collections-netapp-ontap-na-ontap-qos-adaptive-policy-group-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_qos_adaptive_policy_group`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_qos_adaptive_policy_group_module.md#synopsis)
- [Requirements](na_ontap_qos_adaptive_policy_group_module.md#requirements)
- [Parameters](na_ontap_qos_adaptive_policy_group_module.md#parameters)
- [Notes](na_ontap_qos_adaptive_policy_group_module.md#notes)
- [Examples](na_ontap_qos_adaptive_policy_group_module.md#examples)

## [Synopsis](na_ontap_qos_adaptive_policy_group_module.md#id1)

- Create, destroy, modify, or rename an Adaptive QoS policy group on NetApp ONTAP. Module is based on the standard QoS policy group module.

## [Requirements](na_ontap_qos_adaptive_policy_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_qos_adaptive_policy_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **absolute_min_iops**  string | Absolute minimum IOPS defined by this policy. |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **expected_iops**  string | Minimum expected IOPS defined by this policy. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force**  boolean | Setting to ‘true’ forces the deletion of the workloads associated with the policy group along with the policy group.  Choices:   - `false` ← (default) - `true` |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string | Name of the existing policy group to be renamed to name. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **name**  string / required | The name of the policy group to manage. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **peak_iops**  string | Maximum possible IOPS per allocated or used TB|GB. |
| **peak_iops_allocation**  string | Whether peak_iops is specified by allocated or used space.  Choices:   - `"allocated_space"` - `"used_space"` ← (default) |
| **state**  string | Whether the specified policy group should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_qos_adaptive_policy_group_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_qos_adaptive_policy_group_module.md#id5)

```yaml+jinja
- name: create adaptive qos policy group
  netapp.ontap.na_ontap_qos_adaptive_policy_group:
    state: present
    name: aq_policy_1
    vserver: policy_vserver
    absolute_min_iops: 70IOPS
    expected_iops: 100IOPS/TB
    peak_iops: 250IOPS/TB
    peak_iops_allocation: allocated_space
    hostname: 10.193.78.30
    username: admin
    password: netapp1!

- name: modify adaptive qos policy group expected iops
  netapp.ontap.na_ontap_qos_adaptive_policy_group:
    state: present
    name: aq_policy_1
    vserver: policy_vserver
    absolute_min_iops: 70IOPS
    expected_iops: 125IOPS/TB
    peak_iops: 250IOPS/TB
    peak_iops_allocation: allocated_space
    hostname: 10.193.78.30
    username: admin
    password: netapp1!

- name: modify adaptive qos policy group peak iops allocation
  netapp.ontap.na_ontap_qos_adaptive_policy_group:
    state: present
    name: aq_policy_1
    vserver: policy_vserver
    absolute_min_iops: 70IOPS
    expected_iops: 125IOPS/TB
    peak_iops: 250IOPS/TB
    peak_iops_allocation: used_space
    hostname: 10.193.78.30
    username: admin
    password: netapp1!

- name: delete qos policy group
  netapp.ontap.na_ontap_qos_adaptive_policy_group:
    state: absent
    name: aq_policy_1
    vserver: policy_vserver
    hostname: 10.193.78.30
    username: admin
    password: netapp1!
```

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
