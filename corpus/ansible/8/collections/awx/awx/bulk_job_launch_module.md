---
collection: ansible
version: "8"
title: "awx.awx.bulk_job_launch module – Bulk job launch in Automation Platform Controller"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/bulk_job_launch_module.html
fetched_at: 2026-07-28T01:11:23+00:00
---
# awx.awx.bulk_job_launch module – Bulk job launch in Automation Platform Controller

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.bulk_job_launch`.

- [Synopsis](bulk_job_launch_module.md#synopsis)
- [Parameters](bulk_job_launch_module.md#parameters)
- [Notes](bulk_job_launch_module.md#notes)
- [Examples](bulk_job_launch_module.md#examples)
- [Return Values](bulk_job_launch_module.md#return-values)

## [Synopsis](bulk_job_launch_module.md#id1)

- Single-request bulk job launch in Automation Platform Controller.
- Creates a workflow where each node corresponds to an item specified in the jobs option.
- Any options specified at the top level will inherited by the launched jobs (if prompt on launch is enabled for those fields).
- Provides a way to submit many jobs at once to Controller.

## [Parameters](bulk_job_launch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **description**  string | Optional description of this bulk job. |
| **extra_vars**  dictionary | Any extra vars required to launch the job.  Extends the extra_data field at the individual job level. |
| **interval**  float | The interval to request an update from the controller.  **Default:** `2.0` |
| **inventory**  string | Inventory name, ID, or named URL to use for the jobs ran within the bulk job, only used if prompt for inventory is set. |
| **job_tags**  string | A comma-separated list of playbook tags to specify what parts of the playbooks should be executed. |
| **jobs**  list / elements=dictionary / required | List of jobs to create. |
| **credentials**  list / elements=integer | Credential IDs applied as a prompt, if job template prompts for credentials |
| **diff_mode**  boolean | Show the changes made by Ansible tasks where supported  **Choices:**   - `false` - `true` |
| **execution_environment**  integer | Execution environment ID applied as a prompt, if job template prompts for execution environments |
| **extra_data**  dictionary | Extra variables to apply at launch time, if job template prompts for extra variables  **Default:** `{}` |
| **forks**  integer | The number of parallel or simultaneous processes to use while executing the playbook, if job template prompts for forks |
| **identifier**  string | Identifier for the resulting workflow node that represents this job |
| **instance_groups**  list / elements=integer | Instance group IDs applied as a prompt, if job template prompts for instance groups |
| **inventory**  integer | Inventory ID applied as a prompt, if job template prompts for inventory |
| **job_slice_count**  integer | The number of jobs to slice into at runtime, if job template prompts for job slices.  Will cause the Job Template to launch a workflow if value is greater than 1.  **Default:** `1` |
| **job_tags**  string | Job tags applied as a prompt, if job template prompts for job tags |
| **job_type**  string | Job type applied as a prompt, if job template prompts for job type  **Choices:**   - `"run"` - `"check"` |
| **labels**  list / elements=integer | Label IDs to use for the job, if job template prompts for labels |
| **limit**  string | Limit to act on, applied as a prompt, if job template prompts for limit |
| **scm_branch**  string | SCM branch applied as a prompt, if job template prompts for SCM branch  This is only applicable if the project allows for branch override |
| **skip_tags**  string | Tags to skip, applied as a prompt, if job template prompts for job tags |
| **timeout**  integer | Maximum time in seconds to wait for a job to finish (server-side), if job template prompts for timeout. |
| **unified_job_template**  integer / required | Job template ID to use when launching. |
| **verbosity**  integer | Verbosity level for this ad hoc command run  **Choices:**   - `0` - `1` - `2` - `3` - `4` - `5` |
| **limit**  string | Limit to use for the bulk job. |
| **name**  string | The name of the bulk job that is created |
| **organization**  string | If not provided, will use the organization the user is in.  Required if the user belongs to more than one organization.  Affects who can see the resulting bulk job. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **scm_branch**  string | A specific branch of the SCM project to run the template on.  This is only applicable if the project allows for branch override. |
| **skip_tags**  string | A comma-separated list of playbook tags to skip certain tasks or parts of the playbooks to be executed. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **wait**  boolean | Wait for the bulk job to complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](bulk_job_launch_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](bulk_job_launch_module.md#id4)

```yaml+jinja
- name: Launch bulk jobs
  bulk_job_launch:
    name: My Bulk Job Launch
    jobs:
      - unified_job_template: 7
        skip_tags: foo
      - unified_job_template: 10
        limit: foo
        extra_data:
          food: carrot
          color: orange
    limit: bar
    credentials:
      - "My Credential"
      - "suplementary cred"
    extra_vars: # these override / extend extra_data at the job level
      food: grape
      animal: owl
    organization: Default
    inventory: Demo Inventory

- name: Launch bulk jobs with lookup plugin
  bulk_job_launch:
    name: My Bulk Job Launch
    jobs:
      - unified_job_template: 7
      - unified_job_template: "{{ lookup('awx.awx.controller_api', 'job_templates', query_params={'name': 'Demo Job Template'},
        return_ids=True, expect_one=True) }}"
```

## [Return Values](bulk_job_launch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **job_info**  dictionary | dictionary containing information about the bulk job executed  **Returned:** If bulk job launched |

### Authors

- Seth Foster (@fosterseth)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
