---
collection: ansible
version: "8"
title: "awx.awx.project_update module – Update a Project in Automation Platform Controller"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/project_update_module.html
fetched_at: 2026-07-28T01:11:41+00:00
---
# awx.awx.project_update module – Update a Project in Automation Platform Controller

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
> To use it in a playbook, specify: `awx.awx.project_update`.

- [Synopsis](project_update_module.md#synopsis)
- [Parameters](project_update_module.md#parameters)
- [Notes](project_update_module.md#notes)
- [Examples](project_update_module.md#examples)
- [Return Values](project_update_module.md#return-values)

## [Synopsis](project_update_module.md#id1)

- Update a Automation Platform Controller Project. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_project_update

## [Parameters](project_update_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **interval**  float | The interval to request an update from the controller.  **Default:** `2.0` |
| **name**  aliases: project  string / required | The name or id of the project to update. |
| **organization**  string | Organization name, ID, or named URL the project exists in.  Used to help lookup the object, cannot be modified using this module.  If not provided, will lookup by name only, which does not work with duplicates. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **timeout**  integer | If waiting for the project to update this will abort after this amount of seconds |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **wait**  boolean | Wait for the project to update.  If scm revision has not changed module will return not changed.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](project_update_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](project_update_module.md#id4)

```yaml+jinja
- name: Launch a project with a timeout of 10 seconds
  project_update:
    project: "Networking Project"
    timeout: 10

- name: Launch a Project with extra_vars without waiting
  project_update:
    project: "Networking Project"
    wait: False
```

## [Return Values](project_update_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  integer | project id of the updated project  **Returned:** success  **Sample:** `86` |
| **status**  string | status of the updated project  **Returned:** success  **Sample:** `"pending"` |

### Authors

- Sean Sullivan (@sean-m-sullivan)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
