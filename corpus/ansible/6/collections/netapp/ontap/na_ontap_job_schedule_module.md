---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_job_schedule module – NetApp ONTAP Job Schedule"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_job_schedule_module.html
fetched_at: 2026-07-28T00:12:33+00:00
---
# netapp.ontap.na_ontap_job_schedule module – NetApp ONTAP Job Schedule

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
> see [Requirements](na_ontap_job_schedule_module.md#ansible-collections-netapp-ontap-na-ontap-job-schedule-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_job_schedule`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_job_schedule_module.md#synopsis)
- [Requirements](na_ontap_job_schedule_module.md#requirements)
- [Parameters](na_ontap_job_schedule_module.md#parameters)
- [Notes](na_ontap_job_schedule_module.md#notes)
- [Examples](na_ontap_job_schedule_module.md#examples)

## [Synopsis](na_ontap_job_schedule_module.md#id1)

- Create/Delete/Modify job-schedules on ONTAP

## [Requirements](na_ontap_job_schedule_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_job_schedule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **cluster**  string  added in netapp.ontap 21.22.0 | Defaults to local cluster.  In a MetroCluster configuration, user-created schedules owned by the local cluster are replicated to the partner cluster. Likewise, user-created schedules owned by the partner cluster are replicated to the local cluster.  Normally, only schedules owned by the local cluster can be created, modified, and deleted on the local cluster. However, when a MetroCluster configuration is in switchover, the cluster in switchover state can create, modify, and delete schedules owned by the partner cluster. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **job_days_of_month**  list / elements=integer  added in netapp.ontap 2.8.0 | The day(s) of the month when the job should be run. Job Manager cron scheduling day of month.  1 represents all days of a month from 1 to 31. Range is [-1..31] |
| **job_days_of_week**  list / elements=integer  added in netapp.ontap 2.8.0 | The day(s) in the week when the job should be run. Job Manager cron scheduling day of week.  Zero represents Sunday. -1 represents all days of a week. Range is [-1..6] |
| **job_hours**  list / elements=integer  added in netapp.ontap 2.8.0 | The hour(s) of the day when the job should be run. Job Manager cron scheduling hour.  1 represents all hours. Range is [-1..23] |
| **job_minutes**  list / elements=integer | The minute(s) of each hour when the job should be run. Job Manager cron scheduling minute.  1 represents all minutes. Range is [-1..59]  Required for create. |
| **job_months**  list / elements=integer  added in netapp.ontap 2.8.0 | The month(s) when the job should be run. Job Manager cron scheduling month.  1 represents all months. Range is [-1..12], 0 and 12 may or may not be supported, see `month_offset` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **month_offset**  integer  added in netapp.ontap 21.9.0 | whether January starts at 0 or 1. By default, ZAPI is using a 0..11 range, while REST is using 1..12.  default to 0 when using ZAPI, and to 1 when using REST.  when set to 0, a value of 12 or higher is rejected.  when set to 1, a value of 0 or of 13 or higher is rejected.  Choices:   - `0` - `1` |
| **name**  string / required | The name of the job-schedule to manage. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **state**  string | Whether the specified job schedule should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](na_ontap_job_schedule_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_job_schedule_module.md#id5)

```yaml+jinja
- name: Create Job for 11.30PM at 10th of every month
  netapp.ontap.na_ontap_job_schedule:
    state: present
    name: jobName
    job_minutes: 30
    job_hours: 23
    job_days_of_month: 10
    job_months: -1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Create Job for 11.30PM at 10th of January, April, July, October for ZAPI and REST
  netapp.ontap.na_ontap_job_schedule:
    state: present
    name: jobName
    job_minutes: 30
    job_hours: 23
    job_days_of_month: 10
    job_months: 1,4,7,10
    month_offset: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Create Job for 11.30PM at 10th of January, April, July, October for ZAPI and REST
  netapp.ontap.na_ontap_job_schedule:
    state: present
    name: jobName
    job_minutes: 30
    job_hours: 23
    job_days_of_month: 10
    job_months: 0,3,6,9
    month_offset: 0
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Create Job for 11.30PM at 10th of January when using REST and February when using ZAPI !!!
  netapp.ontap.na_ontap_job_schedule:
    state: present
    name: jobName
    job_minutes: 30
    job_hours: 23
    job_days_of_month: 10
    job_months: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: Delete Job
  netapp.ontap.na_ontap_job_schedule:
    state: absent
    name: jobName
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
