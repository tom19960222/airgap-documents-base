---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_snapmirror_policy module – NetApp ONTAP create, delete or modify SnapMirror policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_snapmirror_policy_module.html
fetched_at: 2026-07-28T00:13:14+00:00
---
# netapp.ontap.na_ontap_snapmirror_policy module – NetApp ONTAP create, delete or modify SnapMirror policies

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
> see [Requirements](na_ontap_snapmirror_policy_module.md#ansible-collections-netapp-ontap-na-ontap-snapmirror-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_snapmirror_policy`.

New in netapp.ontap 20.3.0

- [Synopsis](na_ontap_snapmirror_policy_module.md#synopsis)
- [Requirements](na_ontap_snapmirror_policy_module.md#requirements)
- [Parameters](na_ontap_snapmirror_policy_module.md#parameters)
- [Notes](na_ontap_snapmirror_policy_module.md#notes)
- [Examples](na_ontap_snapmirror_policy_module.md#examples)

## [Synopsis](na_ontap_snapmirror_policy_module.md#id1)

- NetApp ONTAP create, modify, or destroy the SnapMirror policy
- Add, modify and remove SnapMirror policy rules
- Following parameters are not supported in REST; ‘owner’, ‘restart’, ‘transfer_priority’, ‘tries’, ‘ignore_atime’, ‘common_snapshot_schedule’

## [Requirements](na_ontap_snapmirror_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_snapmirror_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **comment**  string | Specifies the SnapMirror policy comment. |
| **common_snapshot_schedule**  string | Specifies the common Snapshot copy schedule associated with the policy, only required for strict_sync_mirror and sync_mirror. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **ignore_atime**  boolean | Specifies whether incremental transfers will ignore files which have only their access time changed. Applies to SnapMirror vault relationships only.  Choices:   - `false` - `true` |
| **is_network_compression_enabled**  boolean | Specifies whether network compression is enabled for transfers.  Choices:   - `false` - `true` |
| **keep**  list / elements=integer  added in netapp.ontap 20.7.0 | SnapMirror policy rule retention count for snapshots created.  Required when defining policy rules. |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **owner**  string | Specifies the owner of the SnapMirror policy.  Choices:   - `"cluster_admin"` - `"vserver_admin"` |
| **password**  aliases: pass  string | Password for the specified user. |
| **policy_name**  string / required | Specifies the SnapMirror policy name. |
| **policy_type**  string | Specifies the SnapMirror policy type. Modifying the type of an existing SnapMirror policy is not supported  Choices:   - `"vault"` - `"async_mirror"` - `"mirror_vault"` - `"strict_sync_mirror"` - `"sync_mirror"` |
| **prefix**  list / elements=string  added in netapp.ontap 20.7.0 | SnapMirror policy rule prefix.  Optional when defining policy rules.  Set to ‘’ to not set or remove an existing custom prefix.  Prefix name should be unique within the policy.  When specifying a custom prefix, schedule must also be specified. |
| **restart**  string | Defines the behavior of SnapMirror if an interrupted transfer exists, applies to data protection only.  Choices:   - `"always"` - `"never"` - `"default"` |
| **schedule**  list / elements=string  added in netapp.ontap 20.7.0 | SnapMirror policy rule schedule.  Optional when defining policy rules.  Set to ‘’ to not set or remove a schedule.  When specifying a schedule a custom prefix can be set otherwise the prefix will be set to snapmirror_label. |
| **snapmirror_label**  list / elements=string  added in netapp.ontap 20.7.0 | SnapMirror policy rule label.  Required when defining policy rules.  Use an empty list to remove all user-defined rules. |
| **state**  string | Whether the specified SnapMirror policy should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **transfer_priority**  string | Specifies the priority at which a SnapMirror transfer runs.  Choices:   - `"low"` - `"normal"` |
| **tries**  string | Specifies the number of tries. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | Specifies the vserver for the SnapMirror policy. |

## [Notes](na_ontap_snapmirror_policy_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_snapmirror_policy_module.md#id5)

```yaml+jinja
- name: Create SnapMirror policy
  na_ontap_snapmirror_policy:
    state: present
    vserver: "SVM1"
    policy_name: "ansible_policy"
    policy_type: "mirror_vault"
    comment: "created by ansible"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Modify SnapMirror policy
  na_ontap_snapmirror_policy:
    state: present
    vserver: "SVM1"
    policy_name: "ansible_policy"
    policy_type: "async_mirror"
    transfer_priority: "low"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Create SnapMirror policy with basic rules
  na_ontap_snapmirror_policy:
    state: present
    vserver: "SVM1"
    policy_name: "ansible_policy"
    policy_type: "async_mirror"
    snapmirror_label: ['daily', 'weekly', 'monthly']
    keep: [7, 5, 12]
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Create SnapMirror policy with rules and schedules (no schedule for daily rule)
  na_ontap_snapmirror_policy:
    state: present
    vserver: "SVM1"
    policy_name: "ansible_policy"
    policy_type: "mirror_vault"
    snapmirror_label: ['daily', 'weekly', 'monthly']
    keep: [7, 5, 12]
    schedule: ['','weekly','monthly']
    prefix: ['','','monthly_mv']
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Modify SnapMirror policy with rules, remove existing schedules and prefixes
  na_ontap_snapmirror_policy:
    state: present
    vserver: "SVM1"
    policy_name: "ansible_policy"
    policy_type: "mirror_vault"
    snapmirror_label: ['daily', 'weekly', 'monthly']
    keep: [7, 5, 12]
    schedule: ['','','']
    prefix: ['','','']
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Modify SnapMirror policy, delete all rules (excludes builtin rules)
  na_ontap_snapmirror_policy:
    state: present
    vserver: "SVM1"
    policy_name: "ansible_policy"
    policy_type: "mirror_vault"
    snapmirror_label: []
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Delete SnapMirror policy
  na_ontap_snapmirror_policy:
    state: absent
    vserver: "SVM1"
    policy_type: "async_mirror"
    policy_name: "ansible_policy"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
