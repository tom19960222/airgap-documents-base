---
collection: ansible
version: "8"
title: "Awx.Awx"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/index.html
fetched_at: 2026-07-28T01:01:52+00:00
---
# Awx.Awx

Collection version 22.7.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible content that interacts with the AWX or Automation Platform Controller API.

**Author:**

- AWX Project Contributors <[awx-project@googlegroups.com](mailto:awx-project%40googlegroups.com)>

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)

## [Plugin Index](index.md#id2)

These are the plugins in the awx.awx collection:

### Modules

- [ad_hoc_command module](ad_hoc_command_module.md#ansible-collections-awx-awx-ad-hoc-command-module) – create, update, or destroy Automation Platform Controller ad hoc commands.
- [ad_hoc_command_cancel module](ad_hoc_command_cancel_module.md#ansible-collections-awx-awx-ad-hoc-command-cancel-module) – Cancel an Ad Hoc Command.
- [ad_hoc_command_wait module](ad_hoc_command_wait_module.md#ansible-collections-awx-awx-ad-hoc-command-wait-module) – Wait for Automation Platform Controller Ad Hoc Command to finish.
- [application module](application_module.md#ansible-collections-awx-awx-application-module) – create, update, or destroy Automation Platform Controller applications
- [bulk_host_create module](bulk_host_create_module.md#ansible-collections-awx-awx-bulk-host-create-module) – Bulk host create in Automation Platform Controller
- [bulk_job_launch module](bulk_job_launch_module.md#ansible-collections-awx-awx-bulk-job-launch-module) – Bulk job launch in Automation Platform Controller
- [controller_meta module](controller_meta_module.md#ansible-collections-awx-awx-controller-meta-module) – Returns metadata about the collection this module lives in.
- [credential module](credential_module.md#ansible-collections-awx-awx-credential-module) – create, update, or destroy Automation Platform Controller credential.
- [credential_input_source module](credential_input_source_module.md#ansible-collections-awx-awx-credential-input-source-module) – create, update, or destroy Automation Platform Controller credential input sources.
- [credential_type module](credential_type_module.md#ansible-collections-awx-awx-credential-type-module) – Create, update, or destroy custom Automation Platform Controller credential type.
- [execution_environment module](execution_environment_module.md#ansible-collections-awx-awx-execution-environment-module) – create, update, or destroy Execution Environments in Automation Platform Controller.
- [export module](export_module.md#ansible-collections-awx-awx-export-module) – export resources from Automation Platform Controller.
- [group module](group_module.md#ansible-collections-awx-awx-group-module) – create, update, or destroy Automation Platform Controller group.
- [host module](host_module.md#ansible-collections-awx-awx-host-module) – create, update, or destroy Automation Platform Controller host.
- [import module](import_module.md#ansible-collections-awx-awx-import-module) – import resources into Automation Platform Controller.
- [instance module](instance_module.md#ansible-collections-awx-awx-instance-module) – create, update, or destroy Automation Platform Controller instances.
- [instance_group module](instance_group_module.md#ansible-collections-awx-awx-instance-group-module) – create, update, or destroy Automation Platform Controller instance groups.
- [inventory module](inventory_module.md#ansible-collections-awx-awx-inventory-module) – create, update, or destroy Automation Platform Controller inventory.
- [inventory_source module](inventory_source_module.md#ansible-collections-awx-awx-inventory-source-module) – create, update, or destroy Automation Platform Controller inventory source.
- [inventory_source_update module](inventory_source_update_module.md#ansible-collections-awx-awx-inventory-source-update-module) – Update inventory source(s).
- [job_cancel module](job_cancel_module.md#ansible-collections-awx-awx-job-cancel-module) – Cancel an Automation Platform Controller Job.
- [job_launch module](job_launch_module.md#ansible-collections-awx-awx-job-launch-module) – Launch an Ansible Job.
- [job_list module](job_list_module.md#ansible-collections-awx-awx-job-list-module) – List Automation Platform Controller jobs.
- [job_template module](job_template_module.md#ansible-collections-awx-awx-job-template-module) – create, update, or destroy Automation Platform Controller job templates.
- [job_wait module](job_wait_module.md#ansible-collections-awx-awx-job-wait-module) – Wait for Automation Platform Controller job to finish.
- [label module](label_module.md#ansible-collections-awx-awx-label-module) – create, update, or destroy Automation Platform Controller labels.
- [license module](license_module.md#ansible-collections-awx-awx-license-module) – Set the license for Automation Platform Controller
- [notification_template module](notification_template_module.md#ansible-collections-awx-awx-notification-template-module) – create, update, or destroy Automation Platform Controller notification.
- [organization module](organization_module.md#ansible-collections-awx-awx-organization-module) – create, update, or destroy Automation Platform Controller organizations
- [project module](project_module.md#ansible-collections-awx-awx-project-module) – create, update, or destroy Automation Platform Controller projects
- [project_update module](project_update_module.md#ansible-collections-awx-awx-project-update-module) – Update a Project in Automation Platform Controller
- [role module](role_module.md#ansible-collections-awx-awx-role-module) – grant or revoke an Automation Platform Controller role.
- [schedule module](schedule_module.md#ansible-collections-awx-awx-schedule-module) – create, update, or destroy Automation Platform Controller schedules.
- [settings module](settings_module.md#ansible-collections-awx-awx-settings-module) – Modify Automation Platform Controller settings.
- [subscriptions module](subscriptions_module.md#ansible-collections-awx-awx-subscriptions-module) – Get subscription list
- [team module](team_module.md#ansible-collections-awx-awx-team-module) – create, update, or destroy Automation Platform Controller team.
- [token module](token_module.md#ansible-collections-awx-awx-token-module) – create, update, or destroy Automation Platform Controller tokens.
- [user module](user_module.md#ansible-collections-awx-awx-user-module) – create, update, or destroy Automation Platform Controller users.
- [workflow_approval module](workflow_approval_module.md#ansible-collections-awx-awx-workflow-approval-module) – Approve an approval node in a workflow job.
- [workflow_job_template module](workflow_job_template_module.md#ansible-collections-awx-awx-workflow-job-template-module) – create, update, or destroy Automation Platform Controller workflow job templates.
- [workflow_job_template_node module](workflow_job_template_node_module.md#ansible-collections-awx-awx-workflow-job-template-node-module) – create, update, or destroy Automation Platform Controller workflow job template nodes.
- [workflow_launch module](workflow_launch_module.md#ansible-collections-awx-awx-workflow-launch-module) – Run a workflow in Automation Platform Controller
- [workflow_node_wait module](workflow_node_wait_module.md#ansible-collections-awx-awx-workflow-node-wait-module) – Wait for a workflow node to finish.

### Inventory Plugins

- [controller inventory](controller_inventory.md#ansible-collections-awx-awx-controller-inventory) – Ansible dynamic inventory plugin for the Automation Platform Controller.

### Lookup Plugins

- [controller_api lookup](controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup) – Search the API for objects
- [schedule_rrule lookup](schedule_rrule_lookup.md#ansible-collections-awx-awx-schedule-rrule-lookup) – Generate an rrule string which can be used for Schedules
- [schedule_rruleset lookup](schedule_rruleset_lookup.md#ansible-collections-awx-awx-schedule-rruleset-lookup) – Generate an rruleset string

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
