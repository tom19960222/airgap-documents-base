---
collection: ansible
version: "8"
title: "community.general.jenkins_build module – Manage jenkins builds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jenkins_build_module.html
fetched_at: 2026-07-28T01:46:59+00:00
---
# community.general.jenkins_build module – Manage jenkins builds

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
> see [Requirements](jenkins_build_module.md#ansible-collections-community-general-jenkins-build-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jenkins_build`.

New in community.general 2.2.0

- [Synopsis](jenkins_build_module.md#synopsis)
- [Requirements](jenkins_build_module.md#requirements)
- [Parameters](jenkins_build_module.md#parameters)
- [Attributes](jenkins_build_module.md#attributes)
- [Examples](jenkins_build_module.md#examples)
- [Return Values](jenkins_build_module.md#return-values)

## [Synopsis](jenkins_build_module.md#id1)

- Manage Jenkins builds with Jenkins REST API.

Aliases: web_infrastructure.jenkins_build

## [Requirements](jenkins_build_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-jenkins >= 0.4.12

## [Parameters](jenkins_build_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **args**  dictionary | A list of parameters to pass to the build. |
| **build_number**  integer | An integer which specifies a build of a job. Is required to remove a build from the queue. |
| **detach**  boolean  *added in community.general 7.4.0* | Enable detached mode to not wait for the build end.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the Jenkins job to build. |
| **password**  string | Password to authenticate with the Jenkins server. |
| **state**  string | Attribute that specifies if the build is to be created, deleted or stopped.  The `stopped` state has been added in community.general 3.3.0.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"stopped"` |
| **time_between_checks**  integer  *added in community.general 7.4.0* | Time in seconds to wait between requests to the Jenkins server.  This times must be higher than the configured quiet time for the job.  **Default:** `10` |
| **token**  string | API token used to authenticate with the Jenkins server. |
| **url**  string | URL of the Jenkins server.  **Default:** `"http://localhost:8080"` |
| **user**  string | User to authenticate with the Jenkins server. |

## [Attributes](jenkins_build_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](jenkins_build_module.md#id5)

```yaml+jinja
- name: Create a jenkins build using basic authentication
  community.general.jenkins_build:
    name: "test-check"
    args:
      cloud: "test"
      availability_zone: "test_az"
    state: present
    user: admin
    password: asdfg
    url: http://localhost:8080

- name: Stop a running jenkins build anonymously
  community.general.jenkins_build:
    name: "stop-check"
    build_number: 3
    state: stopped
    url: http://localhost:8080

- name: Delete a jenkins build using token authentication
  community.general.jenkins_build:
    name: "delete-experiment"
    build_number: 30
    state: absent
    user: Jenkins
    token: abcdefghijklmnopqrstuvwxyz123456
    url: http://localhost:8080
```

## [Return Values](jenkins_build_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build_info**  dictionary | Build info of the jenkins job.  **Returned:** success |
| **name**  string | Name of the jenkins job.  **Returned:** success  **Sample:** `"test-job"` |
| **state**  string | State of the jenkins job.  **Returned:** success  **Sample:** `"present"` |
| **url**  string | Url to connect to the Jenkins server.  **Returned:** success  **Sample:** `"https://jenkins.mydomain.com"` |
| **user**  string | User used for authentication.  **Returned:** success  **Sample:** `"admin"` |

### Authors

- Brett Milford (@brettmilford)
- Tong He (@unnecessary-username)
- Juan Casanova (@juanmcasanova)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
