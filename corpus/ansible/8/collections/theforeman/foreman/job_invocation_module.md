---
collection: ansible
version: "8"
title: "theforeman.foreman.job_invocation module – Invoke Remote Execution Jobs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/job_invocation_module.html
fetched_at: 2026-07-28T02:56:10+00:00
---
# theforeman.foreman.job_invocation module – Invoke Remote Execution Jobs

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
> see [Requirements](job_invocation_module.md#ansible-collections-theforeman-foreman-job-invocation-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.job_invocation`.

New in theforeman.foreman 1.4.0

- [Synopsis](job_invocation_module.md#synopsis)
- [Requirements](job_invocation_module.md#requirements)
- [Parameters](job_invocation_module.md#parameters)
- [Attributes](job_invocation_module.md#attributes)
- [Examples](job_invocation_module.md#examples)
- [Return Values](job_invocation_module.md#return-values)

## [Synopsis](job_invocation_module.md#id1)

- Invoke and schedule Remote Execution Jobs

## [Requirements](job_invocation_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](job_invocation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bookmark**  string | Bookmark to infer the search query from |
| **command**  string | Command to be executed on host. Required for command templates |
| **concurrency_control**  dictionary | Control concurrency level and distribution over time |
| **concurrency_level**  integer | Maximum jobs to be executed at once |
| **time_span**  integer | Distribute tasks over given number of seconds  This is removed since foreman_remote_execution-11.0.0 |
| **description_format**  string | Override the description format from the template for this invocation only |
| **execution_timeout_interval**  integer | Override the timeout interval from the template for this invocation only |
| **inputs**  dictionary | Inputs to use |
| **job_template**  string / required | Job template to execute |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **randomized_ordering**  boolean | Whether to order the selected hosts randomly  **Choices:**   - `false` - `true` |
| **recurrence**  dictionary | Schedule a recurring job |
| **cron_line**  string | How often the job should occur, in the cron format |
| **end_time**  string | Perform no more executions after this time |
| **max_iteration**  integer | Repeat a maximum of N times |
| **purpose**  string | Designation of a special purpose |
| **scheduling**  dictionary | Schedule the job to start at a later time |
| **start_at**  string | Schedule the job for a future time |
| **start_before**  string | Indicates that the action should be cancelled if it cannot be started before this time. |
| **search_query**  string | Search query to identify hosts |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **ssh**  dictionary | ssh related options |
| **effective_user**  string | What user should be used to run the script (using sudo-like mechanisms)  Defaults to a template parameter or global setting |
| **targeting_type**  string | Dynamic query updates the search results before execution (useful for scheduled jobs)  **Choices:**   - `"static_query"` ← (default) - `"dynamic_query"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](job_invocation_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](job_invocation_module.md#id5)

```yaml+jinja
- name: "Run remote command on a single host once"
  theforeman.foreman.job_invocation:
    search_query: "name ^ (foreman.example.com)"
    command: 'ls'
    job_template: "Run Command - SSH Default"
    ssh:
      effective_user: "tester"

- name: "Run ansible command on active hosts once a day"
  theforeman.foreman.job_invocation:
    bookmark: 'active'
    command: 'pwd'
    job_template: "Run Command - Ansible Default"
    recurrence:
      cron_line: "30 2 * * *"
    concurrency_control:
      concurrency_level: 2
```

## [Return Values](job_invocation_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **job_invocations**  list / elements=dictionary | List of job invocations  **Returned:** success |

### Authors

- Peter Ondrejka (@pondrejk)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
