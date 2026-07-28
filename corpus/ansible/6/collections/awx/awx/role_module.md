---
collection: ansible
version: "6"
title: "awx.awx.role module – grant or revoke an Automation Platform Controller role."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/role_module.html
fetched_at: 2026-07-27T16:45:33+00:00
---
# awx.awx.role module – grant or revoke an Automation Platform Controller role.

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
> To use it in a playbook, specify: `awx.awx.role`.

- [Synopsis](role_module.md#synopsis)
- [Parameters](role_module.md#parameters)
- [Notes](role_module.md#notes)
- [Examples](role_module.md#examples)

## [Synopsis](role_module.md#id1)

- Roles are used for access control, this module is for managing user access to server resources.
- Grant or revoke Automation Platform Controller roles to users. See <https://www.ansible.com/tower> for an overview.

## [Parameters](role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credential**  string | Credential the role acts on.  Deprecated, use ‘credentials’. |
| **credentials**  list / elements=string | Credential the role acts on. |
| **inventories**  list / elements=string | Inventory the role acts on. |
| **inventory**  string | Inventory the role acts on.  Deprecated, use ‘inventories’. |
| **job_template**  string | The job template the role acts on.  Deprecated, use ‘job_templates’. |
| **job_templates**  list / elements=string | The job template the role acts on. |
| **lookup_organization**  string | Organization the inventories, job templates, projects, or workflows the items exists in.  Used to help lookup the object, for organization roles see organization.  If not provided, will lookup by name only, which does not work with duplicates. |
| **organization**  string | Organization the role acts on.  Deprecated, use ‘organizations’. |
| **organizations**  list / elements=string | Organization the role acts on. |
| **project**  string | Project the role acts on.  Deprecated, use ‘projects’. |
| **projects**  list / elements=string | Project the role acts on. |
| **role**  string / required | The role type to grant/revoke.  Choices:   - `"admin"` - `"read"` - `"member"` - `"execute"` - `"adhoc"` - `"update"` - `"use"` - `"approval"` - `"auditor"` - `"project_admin"` - `"inventory_admin"` - `"credential_admin"` - `"workflow_admin"` - `"notification_admin"` - `"job_template_admin"` - `"execution_environment_admin"` |
| **state**  string | Desired state.  State of present indicates the user should have the role.  State of absent indicates the user should have the role taken away, if they have it.  Choices:   - `"present"` ← (default) - `"absent"` |
| **target_team**  string | Team that the role acts on.  For example, make someone a member or an admin of a team.  Members of a team implicitly receive the permissions that the team has.  Deprecated, use ‘target_teams’. |
| **target_teams**  list / elements=string | Team that the role acts on.  For example, make someone a member or an admin of a team.  Members of a team implicitly receive the permissions that the team has. |
| **team**  string | Team that receives the permissions specified by the role. |
| **user**  string | User that receives the permissions specified by the role. |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **workflow**  string | The workflow job template the role acts on.  Deprecated, use ‘workflows’. |
| **workflows**  list / elements=string | The workflow job template the role acts on. |

## [Notes](role_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](role_module.md#id4)

```yaml+jinja
- name: Add jdoe to the member role of My Team
  role:
    user: jdoe
    target_team: "My Team"
    role: member
    state: present

- name: Add Joe to multiple job templates and a workflow
  role:
    user: joe
    role: execute
    workflows:
      - test-role-workflow
    job_templates:
      - jt1
      - jt2
    state: present
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
