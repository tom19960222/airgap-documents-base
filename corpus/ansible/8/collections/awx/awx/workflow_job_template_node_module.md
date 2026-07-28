---
collection: ansible
version: "8"
title: "awx.awx.workflow_job_template_node module – create, update, or destroy Automation Platform Controller workflow job template nodes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/workflow_job_template_node_module.html
fetched_at: 2026-07-28T01:11:48+00:00
---
# awx.awx.workflow_job_template_node module – create, update, or destroy Automation Platform Controller workflow job template nodes.

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
> To use it in a playbook, specify: `awx.awx.workflow_job_template_node`.

- [Synopsis](workflow_job_template_node_module.md#synopsis)
- [Parameters](workflow_job_template_node_module.md#parameters)
- [Notes](workflow_job_template_node_module.md#notes)
- [Examples](workflow_job_template_node_module.md#examples)

## [Synopsis](workflow_job_template_node_module.md#id1)

- Create, update, or destroy Automation Platform Controller workflow job template nodes.
- Use this to build a graph for a workflow, which dictates what the workflow runs.
- You can create nodes first, and link them afterwards, and not worry about ordering. For failsafe referencing of a node, specify identifier, WFJT, and organization. With those specified, you can choose to modify or not modify any other parameter.

Aliases: tower_workflow_job_template_node

## [Parameters](workflow_job_template_node_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **all_parents_must_converge**  boolean | If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node  **Choices:**   - `false` - `true` |
| **always_nodes**  list / elements=string | Nodes that will run after this node completes.  List of node identifiers. |
| **approval_node**  dictionary | A dictionary of Name, description, and timeout values for the approval node.  This parameter is mutually exclusive with `unified_job_template`. |
| **description**  string | Optional description of this workflow approval template. |
| **name**  string / required | Name of this workflow approval template. |
| **timeout**  integer | The amount of time (in seconds) before the approval node expires and fails. |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credentials**  list / elements=string | Credential names, IDs, or named URLs to be applied to job as launch-time prompts.  List of credential names, IDs, or named URLs.  Uniqueness is not handled rigorously. |
| **diff_mode**  boolean | Run diff mode, applied as a prompt, if job template prompts for diff mode  **Choices:**   - `false` - `true` |
| **execution_environment**  string | Execution Environment name, ID, or named URL applied as a prompt, assuming job template prompts for execution environment |
| **extra_data**  dictionary | Variables to apply at launch time.  Will only be accepted if job template prompts for vars or has a survey asking for those vars. |
| **failure_nodes**  list / elements=string | Nodes that will run after this node on failure.  List of node identifiers. |
| **forks**  integer | Forks applied as a prompt, assuming job template prompts for forks |
| **identifier**  string / required | An identifier for this node that is unique within its workflow.  It is copied to workflow job nodes corresponding to this node. |
| **instance_groups**  list / elements=string | List of Instance Group names, IDs, or named URLs applied as a prompt, assuming job template prompts for instance groups |
| **inventory**  string | Name, ID, or named URL of the Inventory applied as a prompt, if job template prompts for inventory |
| **job_slice_count**  integer | Job Slice Count applied as a prompt, assuming job template prompts for job slice count |
| **job_tags**  string | Job tags applied as a prompt, if job template prompts for job tags |
| **job_type**  string | Job type applied as a prompt, if job template prompts for job type  **Choices:**   - `"run"` - `"check"` |
| **labels**  list / elements=string | List of labels applied as a prompt, assuming job template prompts for labels |
| **limit**  string | Limit to act on, applied as a prompt, if job template prompts for limit |
| **lookup_organization**  string | Organization name, ID, or named URL the inventories, job template, project, inventory source the unified_job_template exists in.  If not provided, will lookup by name only, which does not work with duplicates. |
| **organization**  string | The organization name, ID, or named URL of the workflow job template the node exists in.  Used for looking up the workflow, not a direct model field. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **scm_branch**  string | SCM branch applied as a prompt, if job template prompts for SCM branch |
| **skip_tags**  string | Tags to skip, applied as a prompt, if job tempalte prompts for job tags |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **success_nodes**  list / elements=string | Nodes that will run after this node on success.  List of node identifiers. |
| **timeout**  integer | Timeout applied as a prompt, assuming job template prompts for timeout |
| **unified_job_template**  string | Name of unified job template to run in the workflow.  Can be a job template, project, inventory source, etc.  Omit if creating an approval node.  This parameter is mutually exclusive with `approval_node`. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |
| **verbosity**  string | Verbosity applied as a prompt, if job template prompts for verbosity  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |
| **workflow_job_template**  aliases: workflow  string / required | The workflow job template name, ID, or named URL the node exists in.  Used for looking up the node, cannot be modified after creation. |

## [Notes](workflow_job_template_node_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](workflow_job_template_node_module.md#id4)

```yaml+jinja
- name: Create a node, follows workflow_job_template example
  workflow_job_template_node:
    identifier: my-first-node
    workflow: example-workflow
    unified_job_template: jt-for-node-use
    organization: Default  # organization of workflow job template
    extra_data:
      foo_key: bar_value

- name: Create parent node for prior node
  workflow_job_template_node:
    identifier: my-root-node
    workflow: example-workflow
    unified_job_template: jt-for-node-use
    organization: Default
    success_nodes:
      - my-first-node

- name: Create workflow with 2 Job Templates and an approval node in between
  block:
  - name: Create a workflow job template
    tower_workflow_job_template:
      name: my-workflow-job-template
      ask_scm_branch_on_launch: true
      organization: Default

  - name: Create 1st node
    tower_workflow_job_template_node:
      identifier: my-first-node
      workflow_job_template: my-workflow-job-template
      unified_job_template: some_job_template
      organization: Default

  - name: Create 2nd approval node
    tower_workflow_job_template_node:
      identifier: my-second-approval-node
      workflow_job_template: my-workflow-job-template
      organization: Default
      approval_node:
        description: "Do this?"
        name: my-second-approval-node
        timeout: 3600

  - name: Create 3rd node
    tower_workflow_job_template_node:
      identifier: my-third-node
      workflow_job_template: my-workflow-job-template
      unified_job_template: some_other_job_template
      organization: Default

  - name: Link 1st node to 2nd Approval node
    tower_workflow_job_template_node:
      identifier: my-first-node
      workflow_job_template: my-workflow-job-template
      organization: Default
      success_nodes:
        - my-second-approval-node

  - name: Link 2nd Approval Node 3rd node
    tower_workflow_job_template_node:
      identifier: my-second-approval-node
      workflow_job_template: my-workflow-job-template
      organization: Default
      success_nodes:
        - my-third-node
```

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
