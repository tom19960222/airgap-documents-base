---
collection: ansible
version: "6"
title: "community.general.nomad_job_info module – Get Nomad Jobs info"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/nomad_job_info_module.html
fetched_at: 2026-07-27T17:11:07+00:00
---
# community.general.nomad_job_info module – Get Nomad Jobs info

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](nomad_job_info_module.md#ansible-collections-community-general-nomad-job-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.nomad_job_info`.

New in community.general 1.3.0

- [Synopsis](nomad_job_info_module.md#synopsis)
- [Requirements](nomad_job_info_module.md#requirements)
- [Parameters](nomad_job_info_module.md#parameters)
- [Notes](nomad_job_info_module.md#notes)
- [See Also](nomad_job_info_module.md#see-also)
- [Examples](nomad_job_info_module.md#examples)
- [Return Values](nomad_job_info_module.md#return-values)

## [Synopsis](nomad_job_info_module.md#id1)

- Get info for one Nomad job.
- List Nomad jobs.

## [Requirements](nomad_job_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-nomad

## [Parameters](nomad_job_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | Path of certificate for TLS/SSL. |
| **client_key**  path | Path of certificate’s private key for TLS/SSL. |
| **host**  string / required | FQDN of Nomad server. |
| **name**  string | Name of job for Get info.  If not specified, lists all jobs. |
| **namespace**  string | Namespace for Nomad. |
| **timeout**  integer | Timeout (in seconds) for the request to Nomad.  Default: `5` |
| **token**  string | ACL token for authentification. |
| **use_ssl**  boolean | Use TLS/SSL connection.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Enable TLS/SSL certificate validation.  Choices:   - `false` - `true` ← (default) |

## [Notes](nomad_job_info_module.md#id4)

> **Note:**
>
> - `check_mode` is supported.

## [See Also](nomad_job_info_module.md#id5)

> **See also:**
>
> [Nomad jobs documentation](https://www.nomadproject.io/api-docs/jobs/)
> :   Complete documentation for Nomad API jobs.

## [Examples](nomad_job_info_module.md#id6)

```yaml+jinja
- name: Get info for job awx
  community.general.nomad_job_info:
    host: localhost
    name: awx
  register: result

- name: List Nomad jobs
  community.general.nomad_job_info:
    host: localhost
  register: result
```

## [Return Values](nomad_job_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  list / elements=string | List with dictionary contains jobs info  Returned: success  Sample: `[{"Affinities": null, "AllAtOnce": false, "Constraints": null, "ConsulToken": "", "CreateIndex": 13, "Datacenters": ["dc1"], "Dispatched": false, "ID": "example", "JobModifyIndex": 13, "Meta": null, "ModifyIndex": 13, "Multiregion": null, "Name": "example", "Namespace": "default", "NomadTokenID": "", "ParameterizedJob": null, "ParentID": "", "Payload": null, "Periodic": null, "Priority": 50, "Region": "global", "Spreads": null, "Stable": false, "Status": "pending", "StatusDescription": "", "Stop": false, "SubmitTime": 1602244370615307000, "TaskGroups": [{"Affinities": null, "Constraints": null, "Count": 1, "EphemeralDisk": {"Migrate": false, "SizeMB": 300, "Sticky": false}, "Meta": null, "Migrate": {"HealthCheck": "checks", "HealthyDeadline": 300000000000, "MaxParallel": 1, "MinHealthyTime": 10000000000}, "Name": "cache", "Networks": null, "ReschedulePolicy": {"Attempts": 0, "Delay": 30000000000, "DelayFunction": "exponential", "Interval": 0, "MaxDelay": 3600000000000, "Unlimited": true}, "RestartPolicy": {"Attempts": 3, "Delay": 15000000000, "Interval": 1800000000000, "Mode": "fail"}, "Scaling": null, "Services": null, "ShutdownDelay": null, "Spreads": null, "StopAfterClientDisconnect": null, "Tasks": [{"Affinities": null, "Artifacts": null, "CSIPluginConfig": null, "Config": {"image": "redis:3.2", "port_map": [{"db": 6379.0}]}, "Constraints": null, "DispatchPayload": null, "Driver": "docker", "Env": null, "KillSignal": "", "KillTimeout": 5000000000, "Kind": "", "Leader": false, "Lifecycle": null, "LogConfig": {"MaxFileSizeMB": 10, "MaxFiles": 10}, "Meta": null, "Name": "redis", "Resources": {"CPU": 500, "Devices": null, "DiskMB": 0, "IOPS": 0, "MemoryMB": 256, "Networks": [{"CIDR": "", "DNS": null, "Device": "", "DynamicPorts": [{"HostNetwork": "default", "Label": "db", "To": 0, "Value": 0}], "IP": "", "MBits": 10, "Mode": "", "ReservedPorts": null}]}, "RestartPolicy": {"Attempts": 3, "Delay": 15000000000, "Interval": 1800000000000, "Mode": "fail"}, "Services": [{"AddressMode": "auto", "CanaryMeta": null, "CanaryTags": null, "Checks": [{"AddressMode": "", "Args": null, "CheckRestart": null, "Command": "", "Expose": false, "FailuresBeforeCritical": 0, "GRPCService": "", "GRPCUseTLS": false, "Header": null, "InitialStatus": "", "Interval": 10000000000, "Method": "", "Name": "alive", "Path": "", "PortLabel": "", "Protocol": "", "SuccessBeforePassing": 0, "TLSSkipVerify": false, "TaskName": "", "Timeout": 2000000000, "Type": "tcp"}], "Connect": null, "EnableTagOverride": false, "Meta": null, "Name": "redis-cache", "PortLabel": "db", "Tags": ["global", "cache"], "TaskName": ""}], "ShutdownDelay": 0, "Templates": null, "User": "", "Vault": null, "VolumeMounts": null}], "Update": {"AutoPromote": false, "AutoRevert": false, "Canary": 0, "HealthCheck": "checks", "HealthyDeadline": 180000000000, "MaxParallel": 1, "MinHealthyTime": 10000000000, "ProgressDeadline": 600000000000, "Stagger": 30000000000}, "Volumes": null}], "Type": "service", "Update": {"AutoPromote": false, "AutoRevert": false, "Canary": 0, "HealthCheck": "", "HealthyDeadline": 0, "MaxParallel": 1, "MinHealthyTime": 0, "ProgressDeadline": 0, "Stagger": 30000000000}, "VaultNamespace": "", "VaultToken": "", "Version": 0}]` |

### Authors

- FERREIRA Christophe (@chris93111)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
