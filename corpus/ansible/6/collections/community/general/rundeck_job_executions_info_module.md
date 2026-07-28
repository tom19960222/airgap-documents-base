---
collection: ansible
version: "6"
title: "community.general.rundeck_job_executions_info module – Query executions for a Rundeck job"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rundeck_job_executions_info_module.html
fetched_at: 2026-07-27T17:12:48+00:00
---
# community.general.rundeck_job_executions_info module – Query executions for a Rundeck job

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.rundeck_job_executions_info`.

New in community.general 3.8.0

- [Synopsis](rundeck_job_executions_info_module.md#synopsis)
- [Parameters](rundeck_job_executions_info_module.md#parameters)
- [Examples](rundeck_job_executions_info_module.md#examples)
- [Return Values](rundeck_job_executions_info_module.md#return-values)

## [Synopsis](rundeck_job_executions_info_module.md#id1)

- This module gets the list of executions for a specified Rundeck job.

## [Parameters](rundeck_job_executions_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | Rundeck User API Token. |
| **api_version**  integer | Rundeck API version to be used.  API version must be at least 14.  Default: `39` |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  Choices:   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **job_id**  string / required | The job unique ID. |
| **max**  integer | Max results to return.  Default: `20` |
| **offset**  integer | The start point to return the results.  Default: `0` |
| **status**  string | The job status to filter.  Choices:   - `"succeeded"` - `"failed"` - `"aborted"` - `"running"` |
| **url**  string / required | Rundeck instance URL. |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](rundeck_job_executions_info_module.md#id3)

```yaml+jinja
- name: Get Rundeck job executions info
  community.general.rundeck_job_executions_info:
    url: "https://rundeck.example.org"
    api_version: 39
    api_token: "mytoken"
    job_id: "xxxxxxxxxxxxxxxxx"
  register: rundeck_job_executions_info

- name: Show Rundeck job executions info
  ansible.builtin.debug:
    var: rundeck_job_executions_info.executions
```

## [Return Values](rundeck_job_executions_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **executions**  list / elements=dictionary | Job executions list.  Returned: always  Sample: `[{"argstring": "-exit_code 0", "date-ended": {"date": "2021-10-06T13:05:18Z", "unixtime": 1633525518386}, "date-started": {"date": "2021-10-06T13:05:15Z", "unixtime": 1633525515026}, "description": "Plugin[com.batix.rundeck.plugins.AnsiblePlaybookInlineWorkflowStep, nodeStep: false]", "executionType": "user", "href": "https://rundeck.example.org/api/39/execution/1", "id": 1, "job": {"averageDuration": 6381, "description": "", "group": "", "href": "https://rundeck.example.org/api/39/job/697af0c4-72d3-4c15-86a3-b5bfe3c6cb6a", "id": "697af0c4-72d3-4c15-86a3-b5bfe3c6cb6a", "name": "Test", "options": {"exit_code": "0"}, "permalink": "https://rundeck.example.org/project/myproject/job/show/697af0c4-72d3-4c15-86a3-b5bfe3c6cb6a", "project": "myproject"}, "permalink": "https://rundeck.example.org/project/myproject/execution/show/1", "project": "myproject", "serverUUID": "5b9a1438-fa3a-457e-b254-8f3d70338068", "status": "succeeded", "user": "admin"}]` |
| **paging**  dictionary | Results pagination info.  Returned: success  Sample: `{"count": 20, "max": 20, "offset": 0, "total": 100}` |
| **count**  integer | Number of results in the response.  Returned: success |
| **max**  integer | Maximum number of results per page.  Returned: success |
| **offset**  integer | Offset from first of all results.  Returned: success |
| **total**  integer | Total number of results.  Returned: success |

### Authors

- Phillipe Smith (@phsmith)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
