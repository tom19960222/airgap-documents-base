---
collection: ansible
version: "6"
title: "awx.awx.job_launch module – Launch an Ansible Job."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/job_launch_module.html
fetched_at: 2026-07-27T16:45:29+00:00
---
# awx.awx.job_launch module – Launch an Ansible Job.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.job_launch`.

- [Synopsis](job_launch_module.md#synopsis)
- [Parameters](job_launch_module.md#parameters)
- [Notes](job_launch_module.md#notes)
- [Examples](job_launch_module.md#examples)
- [Return Values](job_launch_module.md#return-values)

## [Synopsis](job_launch_module.md#id1)

- Launch an Automation Platform Controller jobs. See <https://www.ansible.com/tower> for an overview.

## [Parameters](job_launch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credential_passwords**  dictionary | Passwords for credentials which are set to prompt on launch |
| **credentials**  aliases: credential  list / elements=string | Credential to use for job, only used if prompt for credential is set. |
| **diff_mode**  boolean | Show the changes made by Ansible tasks where supported  Choices:   - `false` - `true` |
| **execution_environment**  string | Execution environment to use for the job, only used if prompt for execution environment is set. |
| **extra_vars**  dictionary | extra_vars to use for the Job Template.  ask_extra_vars needs to be set to True via job_template module when creating the Job Template. |
| **forks**  integer | Forks to use for the job, only used if prompt for forks is set. |
| **instance_groups**  list / elements=string | Instance groups to use for the job, only used if prompt for instance groups is set. |
| **interval**  float | The interval to request an update from the controller.  Default: `2.0` |
| **inventory**  string | Inventory to use for the job, only used if prompt for inventory is set. |
| **job_slice_count**  integer | Job slice count to use for the job, only used if prompt for job slice count is set. |
| **job_timeout**  integer | Timeout to use for the job, only used if prompt for timeout is set.  This parameter is sent through the API to the job. |
| **job_type**  string | Job_type to use for the job, only used if prompt for job_type is set.  Choices:   - `"run"` - `"check"` |
| **labels**  list / elements=string | Labels to use for the job, only used if prompt for labels is set. |
| **limit**  string | Limit to use for the *job_template*. |
| **name**  aliases: job_template  string / required | Name of the job template to use. |
| **organization**  string | Organization the job template exists in.  Used to help lookup the object, cannot be modified using this module.  If not provided, will lookup by name only, which does not work with duplicates. |
| **scm_branch**  string | A specific of the SCM project to run the template on.  This is only applicable if your project allows for branch override. |
| **skip_tags**  list / elements=string | Specific tags to skip from the playbook. |
| **tags**  list / elements=string | Specific tags to use for from playbook. |
| **timeout**  integer | If waiting for the job to complete this will abort after this amount of seconds. This happens on the module side. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **verbosity**  integer | Verbosity level for this job run  Choices:   - `0` - `1` - `2` - `3` - `4` - `5` |
| **wait**  boolean | Wait for the job to complete.  Choices:   - `false` ← (default) - `true` |

## [Notes](job_launch_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](job_launch_module.md#id4)

```yaml+jinja
- name: Launch a job
  job_launch:
    job_template: "My Job Template"
  register: job

- name: Launch a job template with extra_vars on remote controller instance
  job_launch:
    job_template: "My Job Template"
    extra_vars:
      var1: "My First Variable"
      var2: "My Second Variable"
      var3: "My Third Variable"
    job_type: run

- name: Launch a job with inventory and credential
  job_launch:
    job_template: "My Job Template"
    inventory: "My Inventory"
    credential: "My Credential"
  register: job
- name: Wait for job max 120s
  job_wait:
    job_id: "{{ job.id }}"
    timeout: 120
```

## [Return Values](job_launch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  integer | job id of the newly launched job  Returned: success  Sample: `86` |
| **status**  string | status of newly launched job  Returned: success  Sample: `"pending"` |

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
