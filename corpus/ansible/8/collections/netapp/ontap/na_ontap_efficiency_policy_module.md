---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_efficiency_policy module – NetApp ONTAP manage efficiency policies (sis policies)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_efficiency_policy_module.html
fetched_at: 2026-07-28T02:41:54+00:00
---
# netapp.ontap.na_ontap_efficiency_policy module – NetApp ONTAP manage efficiency policies (sis policies)

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
> see [Requirements](na_ontap_efficiency_policy_module.md#ansible-collections-netapp-ontap-na-ontap-efficiency-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_efficiency_policy`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_efficiency_policy_module.md#synopsis)
- [Requirements](na_ontap_efficiency_policy_module.md#requirements)
- [Parameters](na_ontap_efficiency_policy_module.md#parameters)
- [Notes](na_ontap_efficiency_policy_module.md#notes)
- [Examples](na_ontap_efficiency_policy_module.md#examples)

## [Synopsis](na_ontap_efficiency_policy_module.md#id1)

- Create/Modify/Delete efficiency policies (sis policies)

## [Requirements](na_ontap_efficiency_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_efficiency_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **changelog_threshold_percent**  integer  *added in netapp.ontap 19.11.0* | Specifies the percentage at which the changelog will be processed for a threshold type of policy, tested once each hour. |
| **comment**  string | A brief description of the policy. |
| **duration**  string | The duration in hours for which the scheduled efficiency operation should run. After this time expires, the efficiency operation will be stopped even if the operation is incomplete. If ‘-’ is specified as the duration, the efficiency operation will run till it completes. Otherwise, the duration has to be an integer greater than 0. By default, the operation runs till it completes. |
| **enabled**  boolean | If the value is true, the efficiency policy is active in this cluster. If the value is false this policy will not be activated by the schedulers and hence will be inactive.  **Choices:**   - `false` - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **policy_name**  string / required | the name of the efficiency policy |
| **policy_type**  string | The policy type reflects the reason a volume using this policy will start processing a changelog.  (Changelog processing is identifying and eliminating duplicate blocks which were written since the changelog was last processed.)  threshold Changelog processing occurs once the changelog reaches a certain percent full.  scheduled Changelog processing will be triggered by time.  **Choices:**   - `"threshold"` - `"scheduled"` |
| **qos_policy**  string | QoS policy for the efficiency operation.  background efficiency operation will run in background with minimal or no impact on data serving client operations,  best-effort efficiency operations may have some impact on data serving client operations.  **Choices:**   - `"background"` - `"best_effort"` |
| **schedule**  string | Cron type job schedule name. When the associated policy is set on a volume, the efficiency operation will be triggered for the volume on this schedule.  These schedules can be created using the na_ontap_job_schedule module |
| **state**  string | Whether the specified efficiency policy should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_efficiency_policy_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_efficiency_policy_module.md#id5)

```yaml+jinja
- name: Create threshold efficiency policy
  netapp.ontap.na_ontap_efficiency_policy:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    vserver: ansible
    state: present
    policy_name: test
    comment: This policy is for x and y
    enabled: true
    policy_type: threshold
    qos_policy: background
    changelog_threshold_percent: 20

- name: Create Scheduled efficiency Policy
  netapp.ontap.na_ontap_efficiency_policy:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    vserver: ansible
    state: present
    policy_name: test2
    comment: This policy is for x and y
    enabled: true
    schedule: new_job_schedule
    duration: 1
    policy_type: scheduled
    qos_policy: background
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
