---
collection: ansible
version: "8"
title: "community.general.jenkins_job_info module – Get information about Jenkins jobs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jenkins_job_info_module.html
fetched_at: 2026-07-28T01:47:01+00:00
---
# community.general.jenkins_job_info module – Get information about Jenkins jobs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](jenkins_job_info_module.md#ansible-collections-community-general-jenkins-job-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jenkins_job_info`.

- [Synopsis](jenkins_job_info_module.md#synopsis)
- [Requirements](jenkins_job_info_module.md#requirements)
- [Parameters](jenkins_job_info_module.md#parameters)
- [Attributes](jenkins_job_info_module.md#attributes)
- [Examples](jenkins_job_info_module.md#examples)
- [Return Values](jenkins_job_info_module.md#return-values)

## [Synopsis](jenkins_job_info_module.md#id1)

- This module can be used to query information about which Jenkins jobs which already exists.
- This module was called `jenkins_job_facts` before Ansible 2.9. The usage did not change.

Aliases: web_infrastructure.jenkins_job_info

## [Requirements](jenkins_job_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-jenkins >= 0.4.12

## [Parameters](jenkins_job_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **color**  string | Only fetch jobs with the given status color. |
| **glob**  string | A shell glob of Jenkins job names to fetch information about. |
| **name**  string | Exact name of the Jenkins job to fetch information about. |
| **password**  string | Password to authenticate with the Jenkins server.  This is mutually exclusive with `token`. |
| **token**  string | API token used to authenticate with the Jenkins server.  This is mutually exclusive with `password`. |
| **url**  string | URL where the Jenkins server is accessible.  **Default:** `"http://localhost:8080"` |
| **user**  string | User to authenticate with the Jenkins server. |
| **validate_certs**  boolean | If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](jenkins_job_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](jenkins_job_info_module.md#id5)

```yaml+jinja
# Get all Jenkins jobs anonymously
- community.general.jenkins_job_info:
    user: admin
  register: my_jenkins_job_info

# Get all Jenkins jobs using basic auth
- community.general.jenkins_job_info:
    user: admin
    password: hunter2
  register: my_jenkins_job_info

# Get all Jenkins jobs using the token
- community.general.jenkins_job_info:
    user: admin
    token: abcdefghijklmnop
  register: my_jenkins_job_info

# Get info about a single job using basic auth
- community.general.jenkins_job_info:
    name: some-job-name
    user: admin
    password: hunter2
  register: my_jenkins_job_info

# Get info about a single job in a folder using basic auth
- community.general.jenkins_job_info:
    name: some-folder-name/some-job-name
    user: admin
    password: hunter2
  register: my_jenkins_job_info

# Get info about jobs matching a shell glob using basic auth
- community.general.jenkins_job_info:
    glob: some-job-*
    user: admin
    password: hunter2
  register: my_jenkins_job_info

# Get info about all failing jobs using basic auth
- community.general.jenkins_job_info:
    color: red
    user: admin
    password: hunter2
  register: my_jenkins_job_info

# Get info about passing jobs matching a shell glob using basic auth
- community.general.jenkins_job_info:
    name: some-job-*
    color: blue
    user: admin
    password: hunter2
  register: my_jenkins_job_info

- name: Get the info from custom URL with token and validate_certs=False
  community.general.jenkins_job_info:
    user: admin
    token: 126df5c60d66c66e3b75b11104a16a8a
    url: https://jenkins.example.com
    validate_certs: false
  register: my_jenkins_job_info
```

## [Return Values](jenkins_job_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **jobs**  list / elements=string | All jobs found matching the specified criteria  **Returned:** success  **Sample:** `[{"color": "blue", "fullname": "test-folder/test-job", "name": "test-job", "url": "http://localhost:8080/job/test-job/"}]` |

### Authors

- Chris St. Pierre (@stpierre)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
