---
collection: ansible
version: "6"
title: "community.general.mssql_script module – Execute SQL scripts on a MSSQL database"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/mssql_script_module.html
fetched_at: 2026-07-27T17:11:01+00:00
---
# community.general.mssql_script module – Execute SQL scripts on a MSSQL database

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](mssql_script_module.md#ansible-collections-community-general-mssql-script-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.mssql_script`.

New in community.general 4.0.0

- [Synopsis](mssql_script_module.md#synopsis)
- [Requirements](mssql_script_module.md#requirements)
- [Parameters](mssql_script_module.md#parameters)
- [Notes](mssql_script_module.md#notes)
- [Examples](mssql_script_module.md#examples)
- [Return Values](mssql_script_module.md#return-values)

## [Synopsis](mssql_script_module.md#id1)

- Execute SQL scripts on a MSSQL database.

## [Requirements](mssql_script_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pymssql

## [Parameters](mssql_script_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **login_host**  string / required | Host running the database. |
| **login_password**  string | The password used to authenticate with. |
| **login_port**  integer | Port of the MSSQL server. Requires *login_host* be defined as well.  Default: `1433` |
| **login_user**  string | The username used to authenticate with. |
| **name**  aliases: db  string | Database to run script against.  Default: `""` |
| **output**  string | With `default` each row will be returned as a list of values. See `query_results`.  Output format `dict` will return dictionary with the column names as keys. See `query_results_dict`.  `dict` requires named columns to be returned by each query otherwise an error is thrown.  Choices:   - `"dict"` - `"default"` ← (default) |
| **params**  dictionary | Parameters passed to the script as SQL parameters. (‘SELECT %(name)s”’ with `example: '{"name": "John Doe"}`.)’ |
| **script**  string / required | The SQL script to be executed.  Script can contain multiple SQL statements. Multiple Batches can be separated by `GO` command.  Each batch must return at least one result set. |

## [Notes](mssql_script_module.md#id4)

> **Note:**
>
> - Requires the pymssql Python package on the remote host. For Ubuntu, this is as easy as `pip install pymssql` (See [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).)

## [Examples](mssql_script_module.md#id5)

```yaml+jinja
- name: Check DB connection
  community.general.mssql_script:
    login_user: "{{ mssql_login_user }}"
    login_password: "{{ mssql_login_password }}"
    login_host: "{{ mssql_host }}"
    login_port: "{{ mssql_port }}"
    db: master
    script: "SELECT 1"

- name: Query with parameter
  community.general.mssql_script:
    login_user: "{{ mssql_login_user }}"
    login_password: "{{ mssql_login_password }}"
    login_host: "{{ mssql_host }}"
    login_port: "{{ mssql_port }}"
    script: |
      SELECT name, state_desc FROM sys.databases WHERE name = %(dbname)s
    params:
      dbname: msdb
  register: result_params
- assert:
    that:
      - result_params.query_results[0][0][0][0] == 'msdb'
      - result_params.query_results[0][0][0][1] == 'ONLINE'

- name: two batches with default output
  community.general.mssql_script:
    login_user: "{{ mssql_login_user }}"
    login_password: "{{ mssql_login_password }}"
    login_host: "{{ mssql_host }}"
    login_port: "{{ mssql_port }}"
    script: |
      SELECT 'Batch 0 - Select 0'
      SELECT 'Batch 0 - Select 1'
      GO
      SELECT 'Batch 1 - Select 0'
  register: result_batches
- assert:
    that:
      - result_batches.query_results | length == 2  # two batch results
      - result_batches.query_results[0] | length == 2  # two selects in first batch
      - result_batches.query_results[0][0] | length == 1  # one row in first select
      - result_batches.query_results[0][0][0] | length == 1  # one column in first row
      - result_batches.query_results[0][0][0][0] == 'Batch 0 - Select 0'  # each row contains a list of values.

- name: two batches with dict output
  community.general.mssql_script:
    login_user: "{{ mssql_login_user }}"
    login_password: "{{ mssql_login_password }}"
    login_host: "{{ mssql_host }}"
    login_port: "{{ mssql_port }}"
    output: dict
    script: |
      SELECT 'Batch 0 - Select 0' as b0s0
      SELECT 'Batch 0 - Select 1' as b0s1
      GO
      SELECT 'Batch 1 - Select 0' as b1s0
  register: result_batches_dict
- assert:
    that:
      - result_batches_dict.query_results_dict | length == 2  # two batch results
      - result_batches_dict.query_results_dict[0] | length == 2  # two selects in first batch
      - result_batches_dict.query_results_dict[0][0] | length == 1  # one row in first select
      - result_batches_dict.query_results_dict[0][0][0]['b0s0'] == 'Batch 0 - Select 0'  # column 'b0s0' of first row
```

## [Return Values](mssql_script_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **query_results**  list / elements=list | List of batches (queries separated by `GO` keyword).  Returned: success and *output=default*  Sample: `[[[["Batch 0 - Select 0"]], [["Batch 0 - Select 1"]]], [[["Batch 1 - Select 0"]]]]` |
| **queries**  list / elements=list | List of result sets of each query.  If a query returns no results, the results of this and all the following queries will not be included in the output.  Use the `GO` keyword in *script* to separate queries.  Returned: success |
| **rows**  list / elements=list | List of rows returned by query.  Returned: success |
| **column_value**  list / elements=string | List of column values.  Any non-standard JSON type is converted to string.  Returned: success, if output is default  Sample: `["Batch 0 - Select 0"]` |
| **query_results_dict**  list / elements=list | List of batches (queries separated by `GO` keyword).  Returned: success and *output=dict*  Sample: `[[[["Batch 0 - Select 0"]], [["Batch 0 - Select 1"]]], [[["Batch 1 - Select 0"]]]]` |
| **queries**  list / elements=list | List of result sets of each query.  If a query returns no results, the results of this and all the following queries will not be included in the output. Use ‘GO’ keyword to separate queries.  Returned: success |
| **rows**  list / elements=list | List of rows returned by query.  Returned: success |
| **column_dict**  dictionary | Dictionary of column names and values.  Any non-standard JSON type is converted to string.  Returned: success, if output is dict  Sample: `{"col_name": "Batch 0 - Select 0"}` |

### Authors

- Kris Budde (@kbudde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
