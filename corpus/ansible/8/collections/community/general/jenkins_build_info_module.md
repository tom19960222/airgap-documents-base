---
collection: ansible
version: "8"
title: "community.general.jenkins_build_info module – Get information about Jenkins builds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jenkins_build_info_module.html
fetched_at: 2026-07-28T01:47:00+00:00
---
# community.general.jenkins_build_info module – Get information about Jenkins builds

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
> see [Requirements](jenkins_build_info_module.md#ansible-collections-community-general-jenkins-build-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jenkins_build_info`.

New in community.general 7.4.0

- [Synopsis](jenkins_build_info_module.md#synopsis)
- [Requirements](jenkins_build_info_module.md#requirements)
- [Parameters](jenkins_build_info_module.md#parameters)
- [Attributes](jenkins_build_info_module.md#attributes)
- [Examples](jenkins_build_info_module.md#examples)
- [Return Values](jenkins_build_info_module.md#return-values)

## [Synopsis](jenkins_build_info_module.md#id1)

- Get information about Jenkins builds with Jenkins REST API.

## [Requirements](jenkins_build_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-jenkins >= 0.4.12

## [Parameters](jenkins_build_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **build_number**  integer | An integer which specifies a build of a job.  If not specified the last build information will be returned. |
| **name**  string / required | Name of the Jenkins job to which the build belongs. |
| **password**  string | Password to authenticate with the Jenkins server. |
| **token**  string | API token used to authenticate with the Jenkins server. |
| **url**  string | URL of the Jenkins server.  **Default:** `"http://localhost:8080"` |
| **user**  string | User to authenticate with the Jenkins server. |

## [Attributes](jenkins_build_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](jenkins_build_info_module.md#id5)

```yaml+jinja
- name: Get information about a jenkins build using basic authentication
  community.general.jenkins_build_info:
    name: "test-check"
    build_number: 1
    user: admin
    password: asdfg
    url: http://localhost:8080

- name: Get information about a jenkins build anonymously
  community.general.jenkins_build_info:
    name: "stop-check"
    build_number: 3
    url: http://localhost:8080

- name: Get information about a jenkins build using token authentication
  community.general.jenkins_build_info:
    name: "delete-experiment"
    build_number: 30
    user: Jenkins
    token: abcdefghijklmnopqrstuvwxyz123456
    url: http://localhost:8080
```

## [Return Values](jenkins_build_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build_info**  dictionary | Build info of the jenkins job.  **Returned:** success |
| **name**  string | Name of the jenkins job.  **Returned:** success  **Sample:** `"test-job"` |
| **state**  string | State of the jenkins job.  **Returned:** success  **Sample:** `"present"` |
| **url**  string | URL to connect to the Jenkins server.  **Returned:** success  **Sample:** `"https://jenkins.mydomain.com"` |
| **user**  string | User used for authentication.  **Returned:** success  **Sample:** `"admin"` |

### Authors

- Juan Casanova (@juanmcasanova)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
