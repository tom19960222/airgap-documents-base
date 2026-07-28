---
collection: ansible
version: "8"
title: "theforeman.foreman.sync_plan module – Manage Sync Plans"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/sync_plan_module.html
fetched_at: 2026-07-28T02:56:46+00:00
---
# theforeman.foreman.sync_plan module – Manage Sync Plans

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](sync_plan_module.md#ansible-collections-theforeman-foreman-sync-plan-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.sync_plan`.

New in theforeman.foreman 1.0.0

- [Synopsis](sync_plan_module.md#synopsis)
- [Requirements](sync_plan_module.md#requirements)
- [Parameters](sync_plan_module.md#parameters)
- [Attributes](sync_plan_module.md#attributes)
- [Examples](sync_plan_module.md#examples)
- [Return Values](sync_plan_module.md#return-values)

## [Synopsis](sync_plan_module.md#id1)

- Manage sync plans

Aliases: katello_sync_plan

## [Requirements](sync_plan_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](sync_plan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cron_expression**  string | A cron expression as found in crontab files  This must be provided together with *interval=’custom cron’*. |
| **description**  string | Description of the sync plan |
| **enabled**  boolean / required | Whether the sync plan is active  **Choices:**   - `false` - `true` |
| **interval**  string / required | How often synchronization should run  **Choices:**   - `"hourly"` - `"daily"` - `"weekly"` - `"custom cron"` |
| **name**  string / required | Name of the sync plan |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **products**  list / elements=string | List of products to include in the sync plan |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **sync_date**  string / required | Start date and time of the first synchronization |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](sync_plan_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](sync_plan_module.md#id5)

```yaml+jinja
- name: "Create or update weekly RHEL sync plan"
  theforeman.foreman.sync_plan:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Weekly RHEL Sync"
    organization: "Default Organization"
    interval: "weekly"
    enabled: false
    sync_date: "2017-01-01 00:00:00 UTC"
    products:
      - 'Red Hat Enterprise Linux Server'
    state: present
```

## [Return Values](sync_plan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **sync_plans**  list / elements=dictionary | List of sync plans.  **Returned:** success |

### Authors

- Andrew Kofink (@akofink)
- Matthis Dellweg (@mdellweg) ATIX-AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
