---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.agent_job_category module – Configures a SQL Agent job category"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/agent_job_category_module.html
fetched_at: 2026-07-28T02:40:24+00:00
---
# lowlydba.sqlserver.agent_job_category module – Configures a SQL Agent job category

> **Note:**
>
> This module is part of the [lowlydba.sqlserver collection](https://galaxy.ansible.com/ui/repo/published/lowlydba/sqlserver/) (version 2.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install lowlydba.sqlserver`.
> You need further requirements to be able to use this module,
> see [Requirements](agent_job_category_module.md#ansible-collections-lowlydba-sqlserver-agent-job-category-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.agent_job_category`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](agent_job_category_module.md#synopsis)
- [Requirements](agent_job_category_module.md#requirements)
- [Parameters](agent_job_category_module.md#parameters)
- [Attributes](agent_job_category_module.md#attributes)
- [Examples](agent_job_category_module.md#examples)
- [Return Values](agent_job_category_module.md#return-values)

## [Synopsis](agent_job_category_module.md#id1)

- Configures a SQL Agent job category. Creates if it does not exist, else does nothing.

## [Requirements](agent_job_category_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](agent_job_category_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **category**  string / required | Name of the category. |
| **category_type**  string | The type of category.  **Choices:**   - `"LocalJob"` - `"MultiServerJob"` - `"None"` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](agent_job_category_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](agent_job_category_module.md#id5)

```yaml+jinja
- name: Create a maintenance job category
  lowlydba.sqlserver.agent_job_category:
    sql_instance: sql-01.myco.io
    category: "Index Maintenance"
```

## [Return Values](agent_job_category_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `New-DbaAgentJobCategory` or `Remove-DbaAgentJobCategory` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
