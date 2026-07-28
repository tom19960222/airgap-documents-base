---
collection: ansible
version: "8"
title: "awx.awx.workflow_approval module – Approve an approval node in a workflow job."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/workflow_approval_module.html
fetched_at: 2026-07-28T01:11:47+00:00
---
# awx.awx.workflow_approval module – Approve an approval node in a workflow job.

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
> To use it in a playbook, specify: `awx.awx.workflow_approval`.

- [Synopsis](workflow_approval_module.md#synopsis)
- [Parameters](workflow_approval_module.md#parameters)
- [Notes](workflow_approval_module.md#notes)
- [Examples](workflow_approval_module.md#examples)

## [Synopsis](workflow_approval_module.md#id1)

- Approve an approval node in a workflow job. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_workflow_approval

## [Parameters](workflow_approval_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Type of action to take.  **Choices:**   - `"approve"` ← (default) - `"deny"` |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **interval**  float | The interval in sections, to request an update from the controller.  **Default:** `1.0` |
| **name**  string / required | Name of the Approval node to approve or deny. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **timeout**  integer | Maximum time in seconds to wait for a workflow job to to reach approval node.  **Default:** `10` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **workflow_job_id**  integer / required | ID of the workflow job to monitor for approval. |

## [Notes](workflow_approval_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](workflow_approval_module.md#id4)

```yaml+jinja
- name: Create a workflow approval node
  workflow_job_template_node:
    identifier: approval_test
    approval_node:
      name: approval_jt_name
      timeout: 900
    workflow: "Test Workflow"

- name: Launch the workflow with a timeout of 10 seconds
  workflow_launch:
    workflow_template: "Test Workflow"
    wait: False
  register: workflow

- name: Wait for approval node to activate and approve
  workflow_approval:
    workflow_job_id: "{{ workflow.id }}"
    name: approval_jt_name
    interval: 10
    timeout: 20
    action: deny
```

### Authors

- Sean Sullivan (@sean-m-sullivan)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
