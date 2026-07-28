---
collection: ansible
version: "6"
title: "community.general.jenkins_job module – Manage jenkins jobs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/jenkins_job_module.html
fetched_at: 2026-07-27T17:10:12+00:00
---
# community.general.jenkins_job module – Manage jenkins jobs

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
> see [Requirements](jenkins_job_module.md#ansible-collections-community-general-jenkins-job-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jenkins_job`.

- [Synopsis](jenkins_job_module.md#synopsis)
- [Requirements](jenkins_job_module.md#requirements)
- [Parameters](jenkins_job_module.md#parameters)
- [Examples](jenkins_job_module.md#examples)
- [Return Values](jenkins_job_module.md#return-values)

## [Synopsis](jenkins_job_module.md#id1)

- Manage Jenkins jobs by using Jenkins REST API.

## [Requirements](jenkins_job_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-jenkins >= 0.4.12

## [Parameters](jenkins_job_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  string | config in XML format.  Required if job does not yet exist.  Mutually exclusive with *enabled*.  Considered if *state=present*. |
| **enabled**  boolean | Whether the job should be enabled or disabled.  Mutually exclusive with *config*.  Considered if *state=present*.  Choices:   - `false` - `true` |
| **name**  string / required | Name of the Jenkins job. |
| **password**  string | Password to authenticate with the Jenkins server. |
| **state**  string | Attribute that specifies if the job has to be created or deleted.  Choices:   - `"present"` ← (default) - `"absent"` |
| **token**  string | API token used to authenticate alternatively to password. |
| **url**  string | URL where the Jenkins server is accessible.  Default: `"http://localhost:8080"` |
| **user**  string | User to authenticate with the Jenkins server. |
| **validate_certs**  boolean  added in community.general 2.3.0 | If set to `false`, the SSL certificates will not be validated. This should only set to `false` used on personally controlled sites using self-signed certificates as it avoids verifying the source site.  The `python-jenkins` library only handles this by using the environment variable `PYTHONHTTPSVERIFY`.  Choices:   - `false` - `true` ← (default) |

## [Examples](jenkins_job_module.md#id4)

```yaml+jinja
- name: Create a jenkins job using basic authentication
  community.general.jenkins_job:
    config: "{{ lookup('file', 'templates/test.xml') }}"
    name: test
    password: admin
    url: http://localhost:8080
    user: admin

- name: Create a jenkins job using the token
  community.general.jenkins_job:
    config: "{{ lookup('template', 'templates/test.xml.j2') }}"
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    url: http://localhost:8080
    user: admin

- name: Delete a jenkins job using basic authentication
  community.general.jenkins_job:
    name: test
    password: admin
    state: absent
    url: http://localhost:8080
    user: admin

- name: Delete a jenkins job using the token
  community.general.jenkins_job:
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    state: absent
    url: http://localhost:8080
    user: admin

- name: Disable a jenkins job using basic authentication
  community.general.jenkins_job:
    name: test
    password: admin
    enabled: false
    url: http://localhost:8080
    user: admin

- name: Disable a jenkins job using the token
  community.general.jenkins_job:
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    enabled: false
    url: http://localhost:8080
    user: admin
```

## [Return Values](jenkins_job_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enabled**  boolean | Whether the jenkins job is enabled or not.  Returned: success  Sample: `true` |
| **name**  string | Name of the jenkins job.  Returned: success  Sample: `"test-job"` |
| **state**  string | State of the jenkins job.  Returned: success  Sample: `"present"` |
| **url**  string | Url to connect to the Jenkins server.  Returned: success  Sample: `"https://jenkins.mydomain.com"` |
| **user**  string | User used for authentication.  Returned: success  Sample: `"admin"` |

### Authors

- Sergio Millan Rodriguez (@sermilrod)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
