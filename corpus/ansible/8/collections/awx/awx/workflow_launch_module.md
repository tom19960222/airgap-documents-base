---
collection: ansible
version: "8"
title: "awx.awx.workflow_launch module – Run a workflow in Automation Platform Controller"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/workflow_launch_module.html
fetched_at: 2026-07-28T01:11:49+00:00
---
# awx.awx.workflow_launch module – Run a workflow in Automation Platform Controller

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
> To use it in a playbook, specify: `awx.awx.workflow_launch`.

- [Synopsis](workflow_launch_module.md#synopsis)
- [Parameters](workflow_launch_module.md#parameters)
- [Notes](workflow_launch_module.md#notes)
- [Examples](workflow_launch_module.md#examples)
- [Return Values](workflow_launch_module.md#return-values)

## [Synopsis](workflow_launch_module.md#id1)

- Launch an Automation Platform Controller workflows. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_workflow_launch

## [Parameters](workflow_launch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **extra_vars**  dictionary | Any extra vars required to launch the job. |
| **interval**  float | The interval to request an update from the controller.  **Default:** `2.0` |
| **inventory**  string | Inventory name, ID, or named URL to use for the job ran with this workflow, only used if prompt for inventory is set. |
| **limit**  string | Limit to use for the *job_template*. |
| **name**  aliases: workflow_template  string / required | The name of the workflow template to run. |
| **organization**  string | Organization name, ID, or named URL the workflow job template exists in.  Used to help lookup the object, cannot be modified using this module.  If not provided, will lookup by name only, which does not work with duplicates. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **scm_branch**  string | A specific branch of the SCM project to run the template on.  This is only applicable if your project allows for branch override. |
| **timeout**  integer | If waiting for the workflow to complete this will abort after this amount of seconds |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **wait**  boolean | Wait for the workflow to complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](workflow_launch_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](workflow_launch_module.md#id4)

```yaml+jinja
- name: Launch a workflow with a timeout of 10 seconds
  workflow_launch:
    workflow_template: "Test Workflow"
    timeout: 10

- name: Launch a Workflow with extra_vars without waiting
  workflow_launch:
    workflow_template: "Test workflow"
    extra_vars:
      var1: My First Variable
      var2: My Second Variable
    wait: False
```

## [Return Values](workflow_launch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **job_info**  dictionary | dictionary containing information about the workflow executed  **Returned:** If workflow launched |

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
