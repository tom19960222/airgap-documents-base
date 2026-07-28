---
collection: ansible
version: "8"
title: "community.general.rundeck_job_run module – Run a Rundeck job"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rundeck_job_run_module.html
fetched_at: 2026-07-28T01:50:05+00:00
---
# community.general.rundeck_job_run module – Run a Rundeck job

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.rundeck_job_run`.

New in community.general 3.8.0

- [Synopsis](rundeck_job_run_module.md#synopsis)
- [Parameters](rundeck_job_run_module.md#parameters)
- [Attributes](rundeck_job_run_module.md#attributes)
- [Examples](rundeck_job_run_module.md#examples)
- [Return Values](rundeck_job_run_module.md#return-values)

## [Synopsis](rundeck_job_run_module.md#id1)

- This module runs a Rundeck job specified by ID.

Aliases: web_infrastructure.rundeck_job_run

## [Parameters](rundeck_job_run_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **abort_on_timeout**  boolean | Send a job abort request if exceeded the `wait_execution_timeout` specified.  **Choices:**   - `false` ← (default) - `true` |
| **api_token**  string / required | Rundeck User API Token. |
| **api_version**  integer | Rundeck API version to be used.  API version must be at least 14.  **Default:** `39` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **filter_nodes**  string | Filter the nodes where the jobs must run.  See <https://docs.rundeck.com/docs/manual/11-node-filters.html#node-filter-syntax>. |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **job_id**  string / required | The job unique ID. |
| **job_options**  dictionary | The job options for the steps.  Numeric values must be quoted. |
| **loglevel**  string | Log level configuration.  **Choices:**   - `"debug"` - `"verbose"` - `"info"` ← (default) - `"warn"` - `"error"` |
| **run_at_time**  string | Schedule the job execution to run at specific date and time.  ISO-8601 date and time format like `2021-10-05T15:45:00-03:00`. |
| **url**  string / required | Rundeck instance URL. |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **wait_execution**  boolean | Wait until the job finished the execution.  **Choices:**   - `false` - `true` ← (default) |
| **wait_execution_delay**  integer | Delay, in seconds, between job execution status check requests.  **Default:** `5` |
| **wait_execution_timeout**  integer | Job execution wait timeout in seconds.  If the timeout is reached, the job will be aborted.  Keep in mind that there is a sleep based on `wait_execution_delay` after each job status check.  **Default:** `120` |

## [Attributes](rundeck_job_run_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](rundeck_job_run_module.md#id4)

```yaml+jinja
- name: Run a Rundeck job
  community.general.rundeck_job_run:
    url: "https://rundeck.example.org"
    api_version: 39
    api_token: "mytoken"
    job_id: "xxxxxxxxxxxxxxxxx"
  register: rundeck_job_run

- name: Show execution info
  ansible.builtin.debug:
    var: rundeck_job_run.execution_info

- name: Run a Rundeck job with options
  community.general.rundeck_job_run:
    url: "https://rundeck.example.org"
    api_version: 39
    api_token: "mytoken"
    job_id: "xxxxxxxxxxxxxxxxx"
    job_options:
        option_1: "value_1"
        option_2: "value_3"
        option_3: "value_3"
  register: rundeck_job_run

- name: Run a Rundeck job with timeout, delay between status check and abort on timeout
  community.general.rundeck_job_run:
    url: "https://rundeck.example.org"
    api_version: 39
    api_token: "mytoken"
    job_id: "xxxxxxxxxxxxxxxxx"
    wait_execution_timeout: 30
    wait_execution_delay: 10
    abort_on_timeout: true
  register: rundeck_job_run

- name: Schedule a Rundeck job
  community.general.rundeck_job_run:
    url: "https://rundeck.example.org"
    api_version: 39
    api_token: "mytoken"
    job_id: "xxxxxxxxxxxxxxxxx"
    run_at_time: "2021-10-05T15:45:00-03:00"
  register: rundeck_job_schedule

- name: Fire-and-forget a Rundeck job
  community.general.rundeck_job_run:
    url: "https://rundeck.example.org"
    api_version: 39
    api_token: "mytoken"
    job_id: "xxxxxxxxxxxxxxxxx"
    wait_execution: false
  register: rundeck_job_run
```

## [Return Values](rundeck_job_run_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **execution_info**  dictionary | Rundeck job execution metadata.  **Returned:** always  **Sample:** `{"execution_info": {"argstring": "-exit_code 0", "date-ended": {"date": "2021-10-05T15:50:26Z", "unixtime": 1633449026358}, "date-started": {"date": "2021-10-05T15:50:20Z", "unixtime": 1633449020784}, "description": "sleep 5 && echo 'Test!' && exit ${option.exit_code}", "executionType": "user", "href": "https://rundeck.example.org/api/39/execution/1", "id": 1, "job": {"averageDuration": 4917, "description": "", "group": "", "href": "https://rundeck.example.org/api/39/job/697af0c4-72d3-4c15-86a3-b5bfe3c6cb6a", "id": "697af0c4-72d3-4c15-86a3-b5bfe3c6cb6a", "name": "Test", "options": {"exit_code": "0"}, "permalink": "https://rundeck.example.org/project/myproject/job/show/697af0c4-72d3-4c15-86a3-b5bfe3c6cb6a", "project": "myproject"}, "output": "Test!", "permalink": "https://rundeck.example.org/project/myproject/execution/show/1", "project": "myproject", "serverUUID": "5b9a1438-fa3a-457e-b254-8f3d70338068", "status": "succeeded", "successfulNodes": ["localhost"], "user": "admin"}, "msg": "Job execution succeeded!"}` |

### Authors

- Phillipe Smith (@phsmith)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
