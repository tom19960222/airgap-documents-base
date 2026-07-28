---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_vscan_on_demand_task module – NetApp ONTAP Vscan on demand task configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_vscan_on_demand_task_module.html
fetched_at: 2026-07-28T00:13:30+00:00
---
# netapp.ontap.na_ontap_vscan_on_demand_task module – NetApp ONTAP Vscan on demand task configuration.

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
> see [Requirements](na_ontap_vscan_on_demand_task_module.md#ansible-collections-netapp-ontap-na-ontap-vscan-on-demand-task-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_vscan_on_demand_task`.

New in netapp.ontap 2.8.0

- [Synopsis](na_ontap_vscan_on_demand_task_module.md#synopsis)
- [Requirements](na_ontap_vscan_on_demand_task_module.md#requirements)
- [Parameters](na_ontap_vscan_on_demand_task_module.md#parameters)
- [Notes](na_ontap_vscan_on_demand_task_module.md#notes)
- [Examples](na_ontap_vscan_on_demand_task_module.md#examples)

## [Synopsis](na_ontap_vscan_on_demand_task_module.md#id1)

- Configure on demand task for Vscan

## [Requirements](na_ontap_vscan_on_demand_task_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_vscan_on_demand_task_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **cross_junction**  boolean | Specifies whether the On-Demand task is allowed to cross volume junctions  This option is not supported with REST.  This option defaults to False for ZAPI.  Choices:   - `false` - `true` |
| **directory_recursion**  boolean | Specifies whether the On-Demand task is allowed to recursively scan through sub-directories.  This option is not supported with REST.  This option defaults to False for ZAPI.  Choices:   - `false` - `true` |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **file_ext_to_exclude**  list / elements=string | File-Extensions for which scanning must not be performed.  File whose extension matches with both inclusion and exclusion list is not considered for scanning. |
| **file_ext_to_include**  list / elements=string | File extensions for which scanning is considered.  The default value is ‘\*’, which means that all files are considered for scanning except those which are excluded from scanning.  File whose extension matches with both inclusion and exclusion list is not considered for scanning. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **max_file_size**  integer | Max file-size (in bytes) allowed for scanning. The default value of 10737418240 (10GB) is taken if not provided at the time of creating a task. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **paths_to_exclude**  list / elements=string | File-paths for which scanning must not be performed. |
| **report_directory**  string | Path from the vserver root where task report is created. The path must be a directory and provided in unix-format from the root of the Vserver.  Example /vol1/on-demand-reports. |
| **report_log_level**  string | Log level for the On-Demand report.  This option is not supported with REST.  This option defaults to ‘error’ for ZAPI.  Choices:   - `"verbose"` - `"info"` - `"error"` |
| **request_timeout**  string | Total request-service time-limit in seconds. If the virus-scanner does not respond within the provided time, scan will be timedout.  This option is not supported with REST. |
| **scan_files_with_no_ext**  boolean | Specifies whether files without any extension are considered for scanning or not.  Choices:   - `false` - `true` ← (default) |
| **scan_paths**  list / elements=string | List of paths that need to be scanned. The path must be provided in unix-format and from the root of the Vserver.  Example /vol1/large_files. |
| **scan_priority**  string | Priority of the On-Demand scan requests generated by this task.  This option is not supported with REST.  This option default to ‘low’ for ZAPI  Choices:   - `"low"` - `"normal"` |
| **schedule**  string | Schedule of the task. The task will be run as per the schedule.  For running the task immediately, vscan-on-demand-task-run api must be used after creating a task. |
| **state**  string | Whether a Vscan on demand task is present or not  Choices:   - `"present"` ← (default) - `"absent"` |
| **task_name**  string / required | Name of the task. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | the name of the data vserver to use. |

## [Notes](na_ontap_vscan_on_demand_task_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_vscan_on_demand_task_module.md#id5)

```yaml+jinja
- name: Create Vscan On Demand Task
  netapp.ontap.na_ontap_vscan_on_demand_task:
    state: present
    username: '{{ netapp_username }}'
    password: '{{ netapp_password }}'
    hostname: '{{ netapp_hostname }}'
    vserver: carchi-vsim2
    task_name: carchiOnDemand
    scan_paths: /
    report_directory: /
    file_ext_to_exclude: ['py', 'yml']
    max_file_size: 10737418241
    paths_to_exclude: ['/tmp', '/var']
    report_log_level: info
    request_timeout: 60

- name: Delete Vscan On Demand Task
  netapp.ontap.na_ontap_vscan_on_demand_task:
    state: absent
    username: '{{ netapp_username }}'
    password: '{{ netapp_password }}'
    hostname: '{{ netapp_hostname }}'
    vserver: carchi-vsim2
    task_name: carchiOnDemand
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
