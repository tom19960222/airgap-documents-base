---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_qos_policy_group module – NetApp ONTAP manage policy group in Quality of Service."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_qos_policy_group_module.html
fetched_at: 2026-07-28T00:12:59+00:00
---
# netapp.ontap.na_ontap_qos_policy_group module – NetApp ONTAP manage policy group in Quality of Service.

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
> see [Requirements](na_ontap_qos_policy_group_module.md#ansible-collections-netapp-ontap-na-ontap-qos-policy-group-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_qos_policy_group`.

New in netapp.ontap 2.8.0

- [Synopsis](na_ontap_qos_policy_group_module.md#synopsis)
- [Requirements](na_ontap_qos_policy_group_module.md#requirements)
- [Parameters](na_ontap_qos_policy_group_module.md#parameters)
- [Notes](na_ontap_qos_policy_group_module.md#notes)
- [Examples](na_ontap_qos_policy_group_module.md#examples)

## [Synopsis](na_ontap_qos_policy_group_module.md#id1)

- Create, destroy, modify, or rename QoS policy group on NetApp ONTAP.

## [Requirements](na_ontap_qos_policy_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_qos_policy_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adaptive_qos_options**  dictionary  added in netapp.ontap 21.19.0 | Adaptive QoS policy-groups define measurable service level objectives (SLOs) that adjust based on the storage object used space and the storage object allocated space.  Only supported with REST. |
| **absolute_min_iops**  integer / required | Specifies the absolute minimum IOPS that is used as an override when the expected_iops is less than this value.  These floors are not guaranteed on non-AFF platforms or when FabricPool tiering policies are set. |
| **expected_iops**  integer / required | Expected IOPS. Specifies the minimum expected IOPS per TB allocated based on the storage object allocated size.  These floors are not guaranteed on non-AFF platforms or when FabricPool tiering policies are set. |
| **peak_iops**  integer / required | Peak IOPS. Specifies the maximum possible IOPS per TB allocated based on the storage object allocated size or the storage object used size. |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **fixed_qos_options**  dictionary  added in netapp.ontap 21.19.0 | Set Minimum and Maximum throughput defined by this policy.  Only supported with REST.  Required one of throughtput options when creating qos_policy. |
| **capacity_shared**  boolean | Whether the SLOs of the policy group are shared between the workloads or if the SLOs are applied separately to each workload.  Default value is False if not used in creating qos policy.  Choices:   - `false` - `true` |
| **max_throughput_iops**  integer | Maximum throughput defined by this policy. It is specified in terms of IOPS.  0 means no maximum throughput is enforced. |
| **max_throughput_mbps**  integer | Maximum throughput defined by this policy. It is specified in terms of Mbps.  0 means no maximum throughput is enforced. |
| **min_throughput_iops**  integer | Minimum throughput defined by this policy. It is specified in terms of IOPS.  0 means no minimum throughput is enforced.  These floors are not guaranteed on non-AFF platforms or when FabricPool tiering policies are set. |
| **min_throughput_mbps**  integer | Minimum throughput defined by this policy. It is specified in terms of Mbps.  0 means no minimum throughput is enforced.  Requires ONTAP 9.8 or later, and REST support. |
| **force**  boolean | Setting to ‘true’ forces the deletion of the workloads associated with the policy group along with the policy group.  Not supported with REST.  Choices:   - `false` - `true` |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string | Name of the existing policy group to be renamed to name. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **is_shared**  boolean  added in netapp.ontap 20.12.0 | Whether the SLOs of the policy group are shared between the workloads or if the SLOs are applied separately to each workload.  Not supported with REST, use `fixed_qos_options`.  Choices:   - `false` - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **max_throughput**  string | Maximum throughput defined by this policy.  Not supported with REST, use `fixed_qos_options`. |
| **min_throughput**  string | Minimum throughput defined by this policy.  Not supported with REST, use `fixed_qos_options`. |
| **name**  string / required | The name of the policy group to manage. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **state**  string | Whether the specified policy group should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_qos_policy_group_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_qos_policy_group_module.md#id5)

```yaml+jinja
- name: create qos policy group in ZAPI.
  netapp.ontap.na_ontap_qos_policy_group:
    state: present
    name: policy_1
    vserver: policy_vserver
    max_throughput: 800KB/s,800iops
    min_throughput: 100iops
    hostname: 10.193.78.30
    username: admin
    password: netapp1!
    use_rest: never

- name: modify qos policy group max throughput in ZAPI.
  netapp.ontap.na_ontap_qos_policy_group:
    state: present
    name: policy_1
    vserver: policy_vserver
    max_throughput: 900KB/s,800iops
    min_throughput: 100iops
    hostname: 10.193.78.30
    username: admin
    password: netapp1!
    use_rest: never

- name: delete qos policy group
  netapp.ontap.na_ontap_qos_policy_group:
    state: absent
    name: policy_1
    vserver: policy_vserver
    hostname: 10.193.78.30
    username: admin
    password: netapp1!

- name: create qos policy group in REST.
  netapp.ontap.na_ontap_qos_policy_group:
    state: present
    name: policy_1
    vserver: policy_vserver
    hostname: 10.193.78.30
    username: admin
    password: netapp1!
    use_rest: always
    fixed_qos_options:
      max_throughput_iops: 800
      max_throughput_mbps: 200
      min_throughput_iops: 500
      min_throughput_mbps: 100
      capacity_shared: True

- name: modify qos policy max_throughput in REST.
  netapp.ontap.na_ontap_qos_policy_group:
    state: present
    name: policy_1
    vserver: policy_vserver
    hostname: 10.193.78.30
    username: admin
    password: netapp1!
    use_rest: always
    fixed_qos_options:
      max_throughput_iops: 1000
      max_throughput_mbps: 300

- name: create adaptive qos policy group in REST.
  netapp.ontap.na_ontap_qos_policy_group:
    state: present
    name: adaptive_policy
    vserver: policy_vserver
    hostname: 10.193.78.30
    username: admin
    password: netapp1!
    use_rest: always
    adaptive_qos_options:
      absolute_min_iops: 100
      expected_iops: 200
      peak_iops: 500
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
