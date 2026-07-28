---
collection: ansible
version: "6"
title: "community.general.taiga_issue module – Creates/deletes an issue in a Taiga Project Management Platform"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/taiga_issue_module.html
fetched_at: 2026-07-27T17:13:33+00:00
---
# community.general.taiga_issue module – Creates/deletes an issue in a Taiga Project Management Platform

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
> see [Requirements](taiga_issue_module.md#ansible-collections-community-general-taiga-issue-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.taiga_issue`.

- [Synopsis](taiga_issue_module.md#synopsis)
- [Requirements](taiga_issue_module.md#requirements)
- [Parameters](taiga_issue_module.md#parameters)
- [Notes](taiga_issue_module.md#notes)
- [Examples](taiga_issue_module.md#examples)

## [Synopsis](taiga_issue_module.md#id1)

- Creates/deletes an issue in a Taiga Project Management Platform (<https://taiga.io>).
- An issue is identified by the combination of project, issue subject and issue type.
- This module implements the creation or deletion of issues (not the update).

## [Requirements](taiga_issue_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-taiga

## [Parameters](taiga_issue_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attachment**  path | Path to a file to be attached to the issue. |
| **attachment_description**  string | A string describing the file to be attached to the issue.  Default: `""` |
| **description**  string | The issue description.  Default: `""` |
| **issue_type**  string / required | The issue type. Must exist previously. |
| **priority**  string | The issue priority. Must exist previously.  Default: `"Normal"` |
| **project**  string / required | Name of the project containing the issue. Must exist previously. |
| **severity**  string | The issue severity. Must exist previously.  Default: `"Normal"` |
| **state**  string | Whether the issue should be present or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | The issue status. Must exist previously.  Default: `"New"` |
| **subject**  string / required | The issue subject. |
| **tags**  list / elements=string | A lists of tags to be assigned to the issue.  Default: `[]` |
| **taiga_host**  string | The hostname of the Taiga instance.  Default: `"https://api.taiga.io"` |

## [Notes](taiga_issue_module.md#id4)

> **Note:**
>
> - The authentication is achieved either by the environment variable TAIGA_TOKEN or by the pair of environment variables TAIGA_USERNAME and TAIGA_PASSWORD

## [Examples](taiga_issue_module.md#id5)

```yaml+jinja
- name: Create an issue in the my hosted Taiga environment and attach an error log
  community.general.taiga_issue:
    taiga_host: https://mytaigahost.example.com
    project: myproject
    subject: An error has been found
    issue_type: Bug
    priority: High
    status: New
    severity: Important
    description: An error has been found. Please check the attached error log for details.
    attachment: /path/to/error.log
    attachment_description: Error log file
    tags:
      - Error
      - Needs manual check
    state: present

- name: Deletes the previously created issue
  community.general.taiga_issue:
    taiga_host: https://mytaigahost.example.com
    project: myproject
    subject: An error has been found
    issue_type: Bug
    state: absent
```

### Authors

- Alejandro Guirao (@lekum)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
