---
collection: ansible
version: "6"
title: "awx.awx.workflow_job_template module – create, update, or destroy Automation Platform Controller workflow job templates."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/workflow_job_template_module.html
fetched_at: 2026-07-27T16:45:36+00:00
---
# awx.awx.workflow_job_template module – create, update, or destroy Automation Platform Controller workflow job templates.

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
> To use it in a playbook, specify: `awx.awx.workflow_job_template`.

- [Synopsis](workflow_job_template_module.md#synopsis)
- [Parameters](workflow_job_template_module.md#parameters)
- [Notes](workflow_job_template_module.md#notes)
- [Examples](workflow_job_template_module.md#examples)

## [Synopsis](workflow_job_template_module.md#id1)

- Create, update, or destroy Automation Platform Controller workflow job templates.
- Replaces the deprecated tower_workflow_template module.
- Use workflow_job_template_node after this, or use the workflow_nodes parameter to build the workflow’s graph

## [Parameters](workflow_job_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_simultaneous**  boolean | Allow simultaneous runs of the workflow job template.  Choices:   - `false` - `true` |
| **ask_inventory_on_launch**  boolean | Prompt user for inventory on launch of this workflow job template  Choices:   - `false` - `true` |
| **ask_labels_on_launch**  aliases: ask_labels  boolean | Prompt user for labels on launch.  Choices:   - `false` - `true` |
| **ask_limit_on_launch**  boolean | Prompt user for limit on launch of this workflow job template  Choices:   - `false` - `true` |
| **ask_scm_branch_on_launch**  boolean | Prompt user for SCM branch on launch of this workflow job template  Choices:   - `false` - `true` |
| **ask_skip_tags_on_launch**  aliases: ask_skip_tags  boolean | Prompt user for job tags to skip on launch.  Choices:   - `false` - `true` |
| **ask_tags_on_launch**  aliases: ask_tags  boolean | Prompt user for job tags on launch.  Choices:   - `false` - `true` |
| **ask_variables_on_launch**  boolean | Prompt user for `extra_vars` on launch.  Choices:   - `false` - `true` |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **copy_from**  string | Name or id to copy the workflow job template from.  This will copy an existing workflow job template and change any parameters supplied.  The new workflow job template name will be the one provided in the name parameter.  The organization parameter is not used in this, to facilitate copy from one organization to another.  Provide the id or use the lookup plugin to provide the id if multiple workflow job templates share the same name. |
| **description**  string | Optional description of this workflow job template. |
| **destroy_current_nodes**  aliases: destroy_current_schema  boolean | Set in order to destroy current workflow_nodes on the workflow.  This option is used for full workflow update, if not used, nodes not described in workflow will persist and keep current associations and links.  Choices:   - `false` ← (default) - `true` |
| **extra_vars**  dictionary | Variables which will be made available to jobs ran inside the workflow. |
| **inventory**  string | Inventory applied as a prompt, assuming job template prompts for inventory |
| **job_tags**  string | Comma separated list of the tags to use for the job template. |
| **labels**  list / elements=string | The labels applied to this job template  Must be created with the labels module first. This will error if the label has not been created. |
| **limit**  string | Limit applied as a prompt, assuming job template prompts for limit |
| **name**  string / required | Name of this workflow job template. |
| **new_name**  string | Setting this option will change the existing name. |
| **notification_templates_approvals**  list / elements=string | list of notifications to send on approval |
| **notification_templates_error**  list / elements=string | list of notifications to send on error |
| **notification_templates_started**  list / elements=string | list of notifications to send on start |
| **notification_templates_success**  list / elements=string | list of notifications to send on success |
| **organization**  string | Organization the workflow job template exists in.  Used to help lookup the object, cannot be modified using this module.  If not provided, will lookup by name only, which does not work with duplicates. |
| **scm_branch**  string | SCM branch applied as a prompt, assuming job template prompts for SCM branch |
| **skip_tags**  string | Comma separated list of the tags to skip for the job template. |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **survey_enabled**  boolean | Setting that variable will prompt the user for job type on the workflow launch.  Choices:   - `false` - `true` |
| **survey_spec**  aliases: survey  dictionary | The definition of the survey associated to the workflow. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **webhook_credential**  string | Personal Access Token for posting back the status to the service API |
| **webhook_service**  string | Service that webhook requests will be accepted from  Choices:   - `"github"` - `"gitlab"` |
| **workflow_nodes**  aliases: schema  list / elements=dictionary | A json list of nodes and their coresponding options. The following suboptions describe a single node. |
| **all_parents_must_converge**  boolean | If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node  Choices:   - `false` - `true` |
| **diff_mode**  boolean | Run diff mode, applied as a prompt, if job template prompts for diff mode  Choices:   - `false` - `true` |
| **execution_environment**  dictionary | Name of Execution Environment to be applied to job as launch-time prompts. |
| **name**  string | Name of Execution Environment to be applied to job as launch-time prompts.  Uniqueness is not handled rigorously. |
| **extra_data**  dictionary | Variables to apply at launch time.  Will only be accepted if job template prompts for vars or has a survey asking for those vars.  Default: `{}` |
| **forks**  integer | The number of parallel or simultaneous processes to use while executing the playbook, if job template prompts for forks |
| **identifier**  string / required | An identifier for this node that is unique within its workflow.  It is copied to workflow job nodes corresponding to this node. |
| **inventory**  string | Inventory applied as a prompt, if job template prompts for inventory |
| **job_slice_count**  integer | The number of jobs to slice into at runtime, if job template prompts for job slices. Will cause the Job Template to launch a workflow if value is greater than 1.  Default: `1` |
| **job_tags**  string | Job tags applied as a prompt, if job template prompts for job tags |
| **job_type**  string | Job type applied as a prompt, if job template prompts for job type  Choices:   - `"run"` - `"check"` |
| **limit**  string | Limit to act on, applied as a prompt, if job template prompts for limit |
| **related**  dictionary | Related items to this workflow node. |
| **always_nodes**  list / elements=string | Nodes that will run after this node completes.  List of node identifiers. |
| **identifier**  string | Identifier of Node that will run after this node completes given this option. |
| **credentials**  list / elements=string | Credentials to be applied to job as launch-time prompts.  List of credential names.  Uniqueness is not handled rigorously. |
| **name**  string | Name Credentials to be applied to job as launch-time prompts. |
| **organization**  dictionary | Name of key for use in model for organizational reference |
| **name**  string | The organization of the credentials exists in. |
| **failure_nodes**  list / elements=string | Nodes that will run after this node on failure.  List of node identifiers. |
| **identifier**  string | Identifier of Node that will run after this node completes given this option. |
| **instance_groups**  list / elements=string | Instance groups to be applied to job as launch-time prompts.  List of Instance group names.  Uniqueness is not handled rigorously. |
| **name**  string | Name of Instance groups to be applied to job as launch-time prompts. |
| **labels**  list / elements=string | Labels to be applied to job as launch-time prompts.  List of Label names.  Uniqueness is not handled rigorously. |
| **name**  string | Name Labels to be applied to job as launch-time prompts. |
| **organization**  dictionary | Name of key for use in model for organizational reference |
| **name**  string | The organization of the label node exists in. |
| **success_nodes**  list / elements=string | Nodes that will run after this node on success.  List of node identifiers. |
| **identifier**  string | Identifier of Node that will run after this node completes given this option. |
| **scm_branch**  string | SCM branch applied as a prompt, if job template prompts for SCM branch |
| **skip_tags**  string | Tags to skip, applied as a prompt, if job tempalte prompts for job tags |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Maximum time in seconds to wait for a job to finish (server-side), if job template prompts for timeout. |
| **unified_job_template**  dictionary | Name of unified job template to run in the workflow.  Can be a job template, project sync, inventory source sync, etc.  Omit if creating an approval node (not yet implemented). |
| **description**  string | Optional description of this workflow approval template. |
| **inventory**  dictionary | Name of key for use in model for organizational reference  Only Valid and used if referencing an inventory sync  This parameter is mutually exclusive with suboption `organization`. |
| **organization**  dictionary | Name of key for use in model for organizational reference |
| **name**  string | The organization of the inventory the node exists in.  Used for looking up the job template or project, not a direct model field. |
| **name**  string | Name of unified job template to run in the workflow.  Can be a job template, project, inventory source, etc. |
| **organization**  dictionary | Name of key for use in model for organizational reference  Only Valid and used if referencing a job template or project sync  This parameter is mutually exclusive with suboption `inventory`. |
| **name**  string | The organization of the job template or project sync the node exists in.  Used for looking up the job template or project sync, not a direct model field. |
| **timeout**  integer | The amount of time (in seconds) to wait before Approval is canceled. A value of 0 means no timeout.  Only Valid and used if referencing an Approval Node  Default: `0` |
| **type**  string | Name of unified job template type to run in the workflow.  Can be a job_template, project, inventory_source, system_job_template, workflow_approval, workflow_job_template. |
| **verbosity**  string | Verbosity applied as a prompt, if job template prompts for verbosity  Choices:   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |

## [Notes](workflow_job_template_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](workflow_job_template_module.md#id4)

```yaml+jinja
- name: Create a workflow job template
  workflow_job_template:
    name: example-workflow
    description: created by Ansible Playbook
    organization: Default

- name: Create a workflow job template with workflow nodes in template
  awx.awx.workflow_job_template:
    name: example-workflow
    inventory: Demo Inventory
    extra_vars: {'foo': 'bar', 'another-foo': {'barz': 'bar2'}}
    workflow_nodes:
      - identifier: node101
        unified_job_template:
          name: example-project
          inventory:
            organization:
              name: Default
          type: inventory_source
        related:
          success_nodes: []
          failure_nodes:
            - identifier: node201
          always_nodes: []
          credentials: []
      - identifier: node201
        unified_job_template:
          organization:
            name: Default
          name: job template 1
          type: job_template
        credentials: []
        related:
          success_nodes:
            - identifier: node301
          failure_nodes: []
          always_nodes: []
          credentials: []
      - identifier: node202
        unified_job_template:
          organization:
            name: Default
          name: example-project
          type: project
        related:
          success_nodes: []
          failure_nodes: []
          always_nodes: []
          credentials: []
      - identifier: node301
        all_parents_must_converge: false
        unified_job_template:
          organization:
            name: Default
          name: job template 2
          type: job_template
        related:
          success_nodes: []
          failure_nodes: []
          always_nodes: []
          credentials: []
  register: result

- name: Copy a workflow job template
  workflow_job_template:
    name: copy-workflow
    copy_from: example-workflow
    organization: Foo

- name: Create a workflow job template with workflow nodes in template
  awx.awx.workflow_job_template:
    name: example-workflow
    inventory: Demo Inventory
    extra_vars: {'foo': 'bar', 'another-foo': {'barz': 'bar2'}}
    workflow_nodes:
      - identifier: node101
        unified_job_template:
          name: example-project
          inventory:
            organization:
              name: Default
          type: inventory_source
        related:
          success_nodes: []
          failure_nodes:
            - identifier: node201
          always_nodes: []
          credentials: []
      - identifier: node201
        unified_job_template:
          organization:
            name: Default
          name: job template 1
          type: job_template
        credentials: []
        related:
          success_nodes:
            - identifier: node301
          failure_nodes: []
          always_nodes: []
          credentials: []
      - identifier: node202
        unified_job_template:
          organization:
            name: Default
          name: example-project
          type: project
        related:
          success_nodes: []
          failure_nodes: []
          always_nodes: []
          credentials: []
      - identifier: node301
        all_parents_must_converge: false
        unified_job_template:
          organization:
            name: Default
          name: job template 2
          type: job_template
        execution_environment:
            name: My EE
        related:
          credentials:
              - name: cyberark
                organization:
                    name: Default
          instance_groups:
              - name: SunCavanaugh Cloud
              - name: default
          labels:
              - name: Custom Label
              - name: Another Custom Label
                organization:
                    name: Default
  register: result
```

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
