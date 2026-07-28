---
collection: ansible
version: "8"
title: "awx.awx.job_wait module – Wait for Automation Platform Controller job to finish."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/job_wait_module.html
fetched_at: 2026-07-28T01:11:37+00:00
---
# awx.awx.job_wait module – Wait for Automation Platform Controller job to finish.

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
> To use it in a playbook, specify: `awx.awx.job_wait`.

- [Synopsis](job_wait_module.md#synopsis)
- [Parameters](job_wait_module.md#parameters)
- [Notes](job_wait_module.md#notes)
- [Examples](job_wait_module.md#examples)
- [Return Values](job_wait_module.md#return-values)

## [Synopsis](job_wait_module.md#id1)

- Wait for Automation Platform Controller job to finish and report success or failure. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_job_wait

## [Parameters](job_wait_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **interval**  float | The interval in sections, to request an update from the controller.  For backwards compatibility if unset this will be set to the average of min and max intervals  **Default:** `2.0` |
| **job_id**  integer / required | ID of the job to monitor. |
| **job_type**  string | Job type to wait for  **Choices:**   - `"project_updates"` - `"jobs"` ← (default) - `"inventory_updates"` - `"workflow_jobs"` |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **timeout**  integer | Maximum time in seconds to wait for a job to finish. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](job_wait_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](job_wait_module.md#id4)

```yaml+jinja
- name: Launch a job
  job_launch:
    job_template: "My Job Template"
  register: job

- name: Wait for job max 120s
  job_wait:
    job_id: "{{ job.id }}"
    timeout: 120
```

## [Return Values](job_wait_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  float | total time in seconds the job took to run  **Returned:** success  **Sample:** `10.879` |
| **finished**  string | timestamp of when the job finished running  **Returned:** success  **Sample:** `"2017-03-01T17:04:04.078782Z"` |
| **id**  integer | job id that is being waited on  **Returned:** success  **Sample:** `99` |
| **started**  string | timestamp of when the job started running  **Returned:** success  **Sample:** `"2017-03-01T17:03:53.200234Z"` |
| **status**  string | current status of job  **Returned:** success  **Sample:** `"successful"` |

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
