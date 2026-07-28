---
collection: ansible
version: "6"
title: "awx.awx.job_template module – create, update, or destroy Automation Platform Controller job templates."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/job_template_module.html
fetched_at: 2026-07-27T16:45:30+00:00
---
# awx.awx.job_template module – create, update, or destroy Automation Platform Controller job templates.

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
> To use it in a playbook, specify: `awx.awx.job_template`.

- [Synopsis](job_template_module.md#synopsis)
- [Parameters](job_template_module.md#parameters)
- [Notes](job_template_module.md#notes)
- [Examples](job_template_module.md#examples)

## [Synopsis](job_template_module.md#id1)

- Create, update, or destroy Automation Platform Controller job templates. See <https://www.ansible.com/tower> for an overview.

## [Parameters](job_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_simultaneous**  aliases: concurrent_jobs_enabled  boolean | Allow simultaneous runs of the job template.  Choices:   - `false` - `true` |
| **ask_credential_on_launch**  aliases: ask_credential  boolean | Prompt user for credential on launch.  Choices:   - `false` - `true` |
| **ask_diff_mode_on_launch**  aliases: ask_diff_mode  boolean | Prompt user to enable diff mode (show changes) to files when supported by modules.  Choices:   - `false` - `true` |
| **ask_execution_environment_on_launch**  aliases: ask_execution_environment  boolean | Prompt user for execution environment on launch.  Choices:   - `false` - `true` |
| **ask_forks_on_launch**  aliases: ask_forks  boolean | Prompt user for forks on launch.  Choices:   - `false` - `true` |
| **ask_instance_groups_on_launch**  aliases: ask_instance_groups  boolean | Prompt user for instance groups on launch.  Choices:   - `false` - `true` |
| **ask_inventory_on_launch**  aliases: ask_inventory  boolean | Prompt user for inventory on launch.  Choices:   - `false` - `true` |
| **ask_job_slice_count_on_launch**  aliases: ask_job_slice_count  boolean | Prompt user for job slice count on launch.  Choices:   - `false` - `true` |
| **ask_job_type_on_launch**  aliases: ask_job_type  boolean | Prompt user for job type on launch.  Choices:   - `false` - `true` |
| **ask_labels_on_launch**  aliases: ask_labels  boolean | Prompt user for labels on launch.  Choices:   - `false` - `true` |
| **ask_limit_on_launch**  aliases: ask_limit  boolean | Prompt user for a limit on launch.  Choices:   - `false` - `true` |
| **ask_scm_branch_on_launch**  boolean | Prompt user for (scm branch) on launch.  Choices:   - `false` - `true` |
| **ask_skip_tags_on_launch**  aliases: ask_skip_tags  boolean | Prompt user for job tags to skip on launch.  Choices:   - `false` - `true` |
| **ask_tags_on_launch**  aliases: ask_tags  boolean | Prompt user for job tags on launch.  Choices:   - `false` - `true` |
| **ask_timeout_on_launch**  aliases: ask_timeout  boolean | Prompt user for timeout on launch.  Choices:   - `false` - `true` |
| **ask_variables_on_launch**  aliases: ask_extra_vars  boolean | Prompt user for (extra_vars) on launch.  Choices:   - `false` - `true` |
| **ask_verbosity_on_launch**  aliases: ask_verbosity  boolean | Prompt user to choose a verbosity level on launch.  Choices:   - `false` - `true` |
| **become_enabled**  boolean | Activate privilege escalation.  Choices:   - `false` - `true` |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **copy_from**  string | Name or id to copy the job template from.  This will copy an existing job template and change any parameters supplied.  The new job template name will be the one provided in the name parameter.  The organization parameter is not used in this, to facilitate copy from one organization to another.  Provide the id or use the lookup plugin to provide the id if multiple job templates share the same name. |
| **credential**  string | Name of the credential to use for the job template.  Deprecated, use ‘credentials’. |
| **credentials**  list / elements=string | List of credentials to use for the job template. |
| **custom_virtualenv**  string | Local absolute file path containing a custom Python virtualenv to use.  Only compatible with older versions of AWX/Tower  Deprecated, will be removed in the future |
| **description**  string | Description to use for the job template. |
| **diff_mode**  aliases: diff_mode_enabled  boolean | Enable diff mode for the job template.  Choices:   - `false` - `true` |
| **execution_environment**  string | Execution Environment to use for the job template. |
| **extra_vars**  dictionary | Specify `extra_vars` for the template. |
| **force_handlers**  aliases: force_handlers_enabled  boolean | Enable forcing playbook handlers to run even if a task fails.  Choices:   - `false` ← (default) - `true` |
| **forks**  integer | The number of parallel or simultaneous processes to use while executing the playbook. |
| **host_config_key**  string | Allow provisioning callbacks using this host config key. |
| **instance_groups**  list / elements=string | list of Instance Groups for this Organization to run on. |
| **inventory**  string | Name of the inventory to use for the job template. |
| **job_slice_count**  integer | The number of jobs to slice into at runtime. Will cause the Job Template to launch a workflow if value is greater than 1.  Default: `1` |
| **job_tags**  string | Comma separated list of the tags to use for the job template. |
| **job_type**  string | The job type to use for the job template.  Choices:   - `"run"` - `"check"` |
| **labels**  list / elements=string | The labels applied to this job template  Must be created with the labels module first. This will error if the label has not been created. |
| **limit**  string | A host pattern to further constrain the list of hosts managed or affected by the playbook |
| **name**  string / required | Name to use for the job template. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **notification_templates_error**  list / elements=string | list of notifications to send on error |
| **notification_templates_started**  list / elements=string | list of notifications to send on start |
| **notification_templates_success**  list / elements=string | list of notifications to send on success |
| **organization**  string | Organization the job template exists in.  Used to help lookup the object, cannot be modified using this module.  The Organization is inferred from the associated project  If not provided, will lookup by name only, which does not work with duplicates.  Requires Automation Platform Version 3.7.0 or AWX 10.0.0 IS NOT backwards compatible with earlier versions. |
| **playbook**  string | Path to the playbook to use for the job template within the project provided. |
| **prevent_instance_group_fallback**  boolean | Prevent falling back to instance groups set on the associated inventory or organization  Choices:   - `false` - `true` |
| **project**  string | Name of the project to use for the job template. |
| **scm_branch**  string | Branch to use in job run. Project default used if blank. Only allowed if project allow_override field is set to true.  Default: `""` |
| **skip_tags**  string | Comma separated list of the tags to skip for the job template. |
| **start_at_task**  string | Start the playbook at the task matching this name. |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **survey_enabled**  boolean | Enable a survey on the job template.  Choices:   - `false` - `true` |
| **survey_spec**  dictionary | JSON/YAML dict formatted survey definition. |
| **timeout**  integer | Maximum time in seconds to wait for a job to finish (server-side). |
| **use_fact_cache**  aliases: fact_caching_enabled  boolean | Enable use of fact caching for the job template.  Choices:   - `false` - `true` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **vault_credential**  string | Name of the vault credential to use for the job template.  Deprecated, use ‘credentials’. |
| **verbosity**  integer | Control the output level Ansible produces as the playbook runs. 0 - Normal, 1 - Verbose, 2 - More Verbose, 3 - Debug, 4 - Connection Debug.  Choices:   - `0` ← (default) - `1` - `2` - `3` - `4` |
| **webhook_credential**  string | Personal Access Token for posting back the status to the service API |
| **webhook_service**  string | Service that webhook requests will be accepted from  Choices:   - `""` - `"github"` - `"gitlab"` |

## [Notes](job_template_module.md#id3)

> **Note:**
>
> - JSON for survey_spec can be found in the API Documentation. See <https://docs.ansible.com/ansible-tower/latest/html/towerapi/api_ref.html#/Job_Templates/Job_Templates_job_templates_survey_spec_create> for POST operation payload example.
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](job_template_module.md#id4)

```yaml+jinja
- name: Create Ping job template
  job_template:
    name: "Ping"
    job_type: "run"
    organization: "Default"
    inventory: "Local"
    project: "Demo"
    playbook: "ping.yml"
    credentials:
      - "Local"
    state: "present"
    controller_config_file: "~/tower_cli.cfg"
    survey_enabled: yes
    survey_spec: "{{ lookup('file', 'my_survey.json') }}"

- name: Add start notification to Job Template
  job_template:
    name: "Ping"
    notification_templates_started:
      - Notification1
      - Notification2

- name: Remove Notification1 start notification from Job Template
  job_template:
    name: "Ping"
    notification_templates_started:
      - Notification2

- name: Copy Job Template
  job_template:
    name: copy job template
    copy_from: test job template
    job_type: "run"
    inventory: Copy Foo Inventory
    project: test
    playbook: hello_world.yml
    state: "present"
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
