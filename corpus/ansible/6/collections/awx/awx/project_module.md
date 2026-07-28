---
collection: ansible
version: "6"
title: "awx.awx.project module – create, update, or destroy Automation Platform Controller projects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/project_module.html
fetched_at: 2026-07-27T16:45:32+00:00
---
# awx.awx.project module – create, update, or destroy Automation Platform Controller projects

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.project`.

- [Synopsis](project_module.md#synopsis)
- [Parameters](project_module.md#parameters)
- [Notes](project_module.md#notes)
- [Examples](project_module.md#examples)

## [Synopsis](project_module.md#id1)

- Create, update, or destroy Automation Platform Controller projects. See <https://www.ansible.com/tower> for an overview.

## [Parameters](project_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_override**  aliases: scm_allow_override  boolean | Allow changing the SCM branch or revision in a job template that uses this project.  Choices:   - `false` - `true` |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **copy_from**  string | Name or id to copy the project from.  This will copy an existing project and change any parameters supplied.  The new project name will be the one provided in the name parameter.  The organization parameter is not used in this, to facilitate copy from one organization to another.  Provide the id or use the lookup plugin to provide the id if multiple projects share the same name. |
| **credential**  aliases: scm_credential  string | Name of the credential to use with this SCM resource. |
| **custom_virtualenv**  string | Local absolute file path containing a custom Python virtualenv to use.  Only compatible with older versions of AWX/Tower  Deprecated, will be removed in the future |
| **default_environment**  string | Default Execution Environment to use for jobs relating to the project. |
| **description**  string | Description to use for the project. |
| **interval**  float | The interval to request an update from the controller.  Requires wait.  Default: `2.0` |
| **local_path**  string | The server playbook directory for manual projects. |
| **name**  string / required | Name to use for the project. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **notification_templates_error**  list / elements=string | list of notifications to send on error |
| **notification_templates_started**  list / elements=string | list of notifications to send on start |
| **notification_templates_success**  list / elements=string | list of notifications to send on success |
| **organization**  string | Name of organization for project. |
| **scm_branch**  string | The branch to use for the SCM resource.  Default: `""` |
| **scm_clean**  boolean | Remove local modifications before updating.  Choices:   - `false` ← (default) - `true` |
| **scm_delete_on_update**  boolean | Remove the repository completely before updating.  Choices:   - `false` ← (default) - `true` |
| **scm_refspec**  string | The refspec to use for the SCM resource.  Default: `""` |
| **scm_track_submodules**  boolean | Track submodules latest commit on specified branch.  Choices:   - `false` ← (default) - `true` |
| **scm_type**  string | Type of SCM resource.  Choices:   - `"manual"` ← (default) - `"git"` - `"svn"` - `"insights"` - `"archive"` |
| **scm_update_cache_timeout**  integer | Cache Timeout to cache prior project syncs for a certain number of seconds. Only valid if scm_update_on_launch is to True, otherwise ignored.  Default: `0` |
| **scm_update_on_launch**  boolean | Before an update to the local repository before launching a job with this project.  Choices:   - `false` ← (default) - `true` |
| **scm_url**  string | URL of SCM resource. |
| **signature_validation_credential**  string | Name of the credential to use for signature validation.  If signature validation credential is provided, signature validation will be enabled. |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  aliases: job_timeout  integer | The amount of time (in seconds) to run before the SCM Update is canceled. A value of 0 means no timeout.  If waiting for the project to update this will abort after this amount of seconds  Default: `0` |
| **update_project**  boolean | Force project to update after changes.  Used in conjunction with wait, interval, and timeout.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **wait**  boolean | Provides option (True by default) to wait for completed project sync before returning  Can assure playbook files are populated so that job templates that rely on the project may be successfully created  Choices:   - `false` - `true` ← (default) |

## [Notes](project_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](project_module.md#id4)

```yaml+jinja
- name: Add project
  project:
    name: "Foo"
    description: "Foo bar project"
    organization: "test"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add Project with cache timeout
  project:
    name: "Foo"
    description: "Foo bar project"
    organization: "test"
    scm_update_on_launch: True
    scm_update_cache_timeout: 60
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Copy project
  project:
    name: copy
    copy_from: test
    description: Foo copy project
    organization: Foo
    state: present
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
