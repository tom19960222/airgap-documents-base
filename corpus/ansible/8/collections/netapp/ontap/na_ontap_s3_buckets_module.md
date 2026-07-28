---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_s3_buckets module – NetApp ONTAP S3 Buckets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_s3_buckets_module.html
fetched_at: 2026-07-28T02:43:07+00:00
---
# netapp.ontap.na_ontap_s3_buckets module – NetApp ONTAP S3 Buckets

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
> see [Requirements](na_ontap_s3_buckets_module.md#ansible-collections-netapp-ontap-na-ontap-s3-buckets-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_s3_buckets`.

New in netapp.ontap 21.19.0

- [Synopsis](na_ontap_s3_buckets_module.md#synopsis)
- [Requirements](na_ontap_s3_buckets_module.md#requirements)
- [Parameters](na_ontap_s3_buckets_module.md#parameters)
- [Notes](na_ontap_s3_buckets_module.md#notes)
- [Examples](na_ontap_s3_buckets_module.md#examples)

## [Synopsis](na_ontap_s3_buckets_module.md#id1)

- Create, delete, or modify S3 buckets on NetApp ONTAP.

## [Requirements](na_ontap_s3_buckets_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_s3_buckets_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregates**  list / elements=string | List of aggregates names to use for the S3 bucket.  This option is not supported when *type=nas*. |
| **audit_event_selector**  dictionary | Audit event selector allows you to specify access and permission types to audit.  This option is not supported when *type=nas*. |
| **access**  string | specifies the type of event access to be audited, read-only, write-only or all (default is all).  **Choices:**   - `"read"` - `"write"` - `"all"` |
| **permission**  string | specifies the type of event permission to be audited, allow-only, deny-only or all (default is all).  **Choices:**   - `"allow"` - `"deny"` - `"all"` |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **comment**  string | Comment for the S3 bucket. |
| **constituents_per_aggregate**  integer | Number of constituents per aggregate.  This option is not supported when *type=nas*. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  string / required | The name of the S3 or NAS bucket. |
| **nas_path**  string  *added in netapp.ontap 22.7.0* | Specifies the NAS path to which the nas bucket corresponds to. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **policy**  dictionary | Access policy uses the Amazon Web Services (AWS) policy language syntax to allow S3 tenants to create access policies to their data |
| **statements**  list / elements=dictionary | Policy statements are built using this structure to specify permissions  Grant <Effect> to allow/deny <Principal> to perform <Action> on <Resource> when <Condition> applies |
| **actions**  list / elements=string | You can specify \* to mean all actions, or a list of one or more of the following  GetObject  PutObject  DeleteObject  ListBucket  GetBucketAcl  GetObjectAcl  ListBucketMultipartUploads  ListMultipartUploadParts |
| **conditions**  list / elements=dictionary | Conditions for when a policy is in effect. |
| **delimiters**  list / elements=string | The delimiter used to identify a prefix in a list of objects. |
| **max_keys**  list / elements=string | The maximum number of keys that can be returned in a request. |
| **operator**  string | The operator to use for the condition.  **Choices:**   - `"ip_address"` - `"not_ip_address"` - `"string_equals"` - `"string_not_equals"` - `"string_equals_ignore_case"` - `"string_not_equals_ignore_case"` - `"string_like"` - `"string_not_like"` - `"numeric_equals"` - `"numeric_not_equals"` - `"numeric_greater_than"` - `"numeric_greater_than_equals"` - `"numeric_less_than"` - `"numeric_less_than_equals"` |
| **prefixes**  list / elements=string | The prefixes of the objects that you want to list. |
| **source_ips**  list / elements=string | The source IP address of the request. |
| **usernames**  list / elements=string | The user names that you want to allow to access the bucket. |
| **effect**  string | The statement may allow or deny access  **Choices:**   - `"allow"` - `"deny"` |
| **principals**  list / elements=string | A list of one or more S3 users or groups. |
| **resources**  list / elements=string | The bucket and any object it contains.  The wildcard characters \* and ? can be used to form a regular expression for specifying a resource. |
| **sid**  string | Statement ID |
| **qos_policy**  dictionary | A policy group defines measurable service level objectives (SLOs) that apply to the storage objects with which the policy group is associated.  If you do not assign a policy group to a bucket, the system wil not monitor and control the traffic to it.  This option is not supported when *type=nas*. |
| **max_throughput_iops**  integer | The maximum throughput in IOPS. |
| **max_throughput_mbps**  integer | The maximum throughput in MBPS. |
| **min_throughput_iops**  integer | The minimum throughput in IOPS. |
| **min_throughput_mbps**  integer | The minimum throughput in MBPS. |
| **name**  string | The QoS policy group name. This is mutually exclusive with other QoS attributes. |
| **size**  integer | Size of the S3 bucket in bytes.  This option is not supported when *type=nas*. |
| **state**  string | Whether the specified S3 bucket should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string  *added in netapp.ontap 22.6.0* | Specifies the bucket type. Valid values are “s3”and “nas”.  **Choices:**   - `"s3"` - `"nas"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_s3_buckets_module.md#id4)

> **Note:**
>
> - module will try to set desired `audit_event_selector` if the bucket is not configured with audit_event_selector options, but may not take effect if there is no audit configuration present in vserver.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_s3_buckets_module.md#id5)

```yaml+jinja
- name: Create S3 bucket
  netapp.ontap.na_ontap_s3_buckets:
    state: present
    name: carchi-test-bucket
    comment: carchi8py was here
    size: 838860800
    vserver: ansibleSVM
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false
    use_rest: always

- name: Create S3 bucket with a policy
  netapp.ontap.na_ontap_s3_buckets:
    state: present
    name: carchi-test-bucket
    comment: carchi8py was here
    size: 838860800
    policy:
      statements:
        - sid: FullAccessToUser1
          resources:
            - bucket1
            - bucket1/*
          actions:
            - GetObject
            - PutObject
            - DeleteObject
            - ListBucket
          effect: allow
          conditions:
            - operator: ip_address
              max_keys:
                - 1000
              delimiters:
                - "/"
              source_ips:
                - 1.1.1.1
                - 1.2.2.0/24
              prefixes:
                - prex
              usernames:
                - user1
          principals:
            - user1
            - group/grp1
    vserver: ansibleSVM
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false
    use_rest: always

- name: Delete S3 bucket
  netapp.ontap.na_ontap_s3_buckets:
    state: absent
    name: carchi-test-bucket
    vserver: ansibleSVM
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false
    use_rest: always
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
