---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_job module – Module to manage jobs in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_job_module.html
fetched_at: 2026-07-28T02:49:37+00:00
---
# ovirt.ovirt.ovirt_job module – Module to manage jobs in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_job_module.md#ansible-collections-ovirt-ovirt-ovirt-job-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_job`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_job_module.md#synopsis)
- [Requirements](ovirt_job_module.md#requirements)
- [Parameters](ovirt_job_module.md#parameters)
- [Notes](ovirt_job_module.md#notes)
- [Examples](ovirt_job_module.md#examples)
- [Return Values](ovirt_job_module.md#return-values)

## [Synopsis](ovirt_job_module.md#id1)

- This module manage jobs in oVirt/RHV. It can also manage steps of the job.

## [Requirements](ovirt_job_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_job_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **description**  string / required | Description of the job.  When task with same description has already finished and you rerun taks it will create new job. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **state**  string | Should the job be `present`/`absent`/`failed`.  `started` is alias for `present`. `finished` is alias for `absent`. Same in the steps.  Note when `finished`/`failed` it will finish/fail all steps.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"started"` - `"finished"` - `"failed"` |
| **steps**  list / elements=dictionary | The steps of the job. |
| **description**  string / required | Description of the step. |
| **state**  string | Should the step be present/absent/failed.  Note when one step fail whole job will fail  Note when all steps are finished it will finish job.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"started"` - `"finished"` - `"failed"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_job_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_job_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Create job with two steps
  ovirt.ovirt.ovirt_job:
    description: job_name
    steps:
      - description: step_name_A
      - description: step_name_B

- name: Finish one step
  ovirt.ovirt.ovirt_job:
    description: job_name
    steps:
      - description: step_name_A
        state: finished

- name: When you fail one step whole job will stop
  ovirt.ovirt.ovirt_job:
    description: job_name
    steps:
      - description: step_name_B
        state: failed

- name: Finish all steps
  ovirt.ovirt.ovirt_job:
    description: job_name
    state: finished
```

## [Return Values](ovirt_job_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the job which is managed  **Returned:** On success if job is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **job**  dictionary | Dictionary of all the job attributes. Job attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/job>.  **Returned:** On success if job is found. |

### Authors

- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
