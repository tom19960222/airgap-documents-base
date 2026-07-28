---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_quotas module – NetApp ONTAP Quotas"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_quotas_module.html
fetched_at: 2026-07-28T00:13:01+00:00
---
# netapp.ontap.na_ontap_quotas module – NetApp ONTAP Quotas

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
> see [Requirements](na_ontap_quotas_module.md#ansible-collections-netapp-ontap-na-ontap-quotas-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_quotas`.

New in netapp.ontap 2.8.0

- [Synopsis](na_ontap_quotas_module.md#synopsis)
- [Requirements](na_ontap_quotas_module.md#requirements)
- [Parameters](na_ontap_quotas_module.md#parameters)
- [Notes](na_ontap_quotas_module.md#notes)
- [Examples](na_ontap_quotas_module.md#examples)

## [Synopsis](na_ontap_quotas_module.md#id1)

- Set/Modify/Delete quota on ONTAP

## [Requirements](na_ontap_quotas_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_quotas_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activate_quota_on_change**  string  added in netapp.ontap 20.12.0 | Method to use to activate quota on a change.  Default value is ‘resize’ in ZAPI.  With REST, Changes to quota rule limits `file_limit`, `disk_limit`, `soft_file_limit`, and `soft_disk_limit` are applied automatically without requiring a quota resize operation.  Choices:   - `"resize"` - `"reinitialize"` - `"none"` |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **disk_limit**  string | The amount of disk space that is reserved for the target.  Expects a number followed with B (for bytes), KB, MB, GB, TB.  If the unit is not present KB is used by default.  Examples - 10MB, 20GB, 1TB, 20B, 10.  In REST, if limit is less than 1024 bytes, the value is rounded up to 1024 bytes.  use ‘-’ to reset disk limit. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **file_limit**  string | The number of files that the target can have.  use ‘-’ to reset file limit. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **perform_user_mapping**  aliases: user_mapping  boolean  added in netapp.ontap 20.12.0 | Whether quota management will perform user mapping for the user specified in quota-target.  User mapping can be specified only for a user quota rule.  Choices:   - `false` - `true` |
| **policy**  string | Name of the quota policy from which the quota rule should be obtained.  Only supported with ZAPI.  Multiple alternative quota policies (active and backup) are not supported in REST.  REST manages the quota rules of the active policy. |
| **qtree**  string | Name of the qtree for the quota.  For user or group rules, it can be the qtree name or “” if no qtree.  For tree type rules, this field must be “”.  Default: `""` |
| **quota_target**  string | The quota target of the type specified.  Required to create or modify a rule.  users and group takes quota_target value in REST.  For default user and group quota rules, the quota_target must be specified as “”. |
| **set_quota_status**  boolean | Whether the specified volume should have quota status on or off.  Choices:   - `false` - `true` |
| **soft_disk_limit**  string | The amount of disk space the target would have to exceed before a message is logged and an SNMP trap is generated.  See `disk_limit` for format description.  In REST, if limit is less than 1024 bytes, the value is rounded up to 1024 bytes.  use ‘-’ to reset soft disk limit. |
| **soft_file_limit**  string | The number of files the target would have to exceed before a message is logged and an SNMP trap is generated.  use ‘-’ to reset soft file limit. |
| **state**  string | Whether the specified quota should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **threshold**  string | The amount of disk space the target would have to exceed before a message is logged.  See `disk_limit` for format description.  Only supported with ZAPI. |
| **type**  string | The type of quota rule  Required to create or modify a rule.  Choices:   - `"user"` - `"group"` - `"tree"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **volume**  string / required | The name of the volume that the quota resides on. |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_quotas_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_quotas_module.md#id5)

```yaml+jinja
- name: Add/Set quota policy is supported only in ZAPI.
  na_ontap_quotas:
    state: present
    vserver: ansible
    volume: ansible
    quota_target: /vol/ansible
    type: user
    policy: ansible
    file_limit: 2
    disk_limit: 3
    set_quota_status: True
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Resize quota
  na_ontap_quotas:
    state: present
    vserver: ansible
    volume: ansible
    quota_target: /vol/ansible
    type: user
    policy: ansible
    file_limit: 2
    disk_limit: 3
    set_quota_status: True
    activate_quota_on_change: resize
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Reinitialize quota
  na_ontap_quotas:
    state: present
    vserver: ansible
    volume: ansible
    quota_target: /vol/ansible
    type: user
    policy: ansible
    file_limit: 2
    disk_limit: 3
    set_quota_status: True
    activate_quota_on_change: reinitialize
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: modify quota
  na_ontap_quotas:
    state: present
    vserver: ansible
    volume: ansible
    quota_target: /vol/ansible
    type: user
    policy: ansible
    file_limit: 2
    disk_limit: 3
    threshold: 3
    set_quota_status: False
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Delete quota
  na_ontap_quotas:
    state: absent
    vserver: ansible
    volume: ansible
    quota_target: /vol/ansible
    type: user
    policy: ansible
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Add/Set quota in REST.
  na_ontap_quotas:
    state: present
    vserver: ansible
    volume: ansible
    quota_target: "user1,user2"
    type: user
    file_limit: 2
    disk_limit: 3
    set_quota_status: True
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Modify quota reset file limit and modify disk limit.
  na_ontap_quotas:
    state: present
    vserver: ansible
    volume: ansible
    quota_target: "user1,user2"
    type: user
    file_limit: "-"
    disk_limit: 100
    set_quota_status: True
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
