---
collection: ansible
version: "6"
title: "ansible.builtin.junit callback – write playbook output to a JUnit file."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/junit_callback.html
fetched_at: 2026-07-27T16:44:14+00:00
---
# ansible.builtin.junit callback – write playbook output to a JUnit file.

> **Note:**
>
> This callback plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `junit` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same callback plugin name.

- [Callback plugin](junit_callback.md#callback-plugin)
- [Synopsis](junit_callback.md#synopsis)
- [Requirements](junit_callback.md#requirements)
- [Parameters](junit_callback.md#parameters)

## [Callback plugin](junit_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](junit_callback.md#id2)

- This callback writes playbook output to a JUnit formatted XML file.
- Tasks show up in the report as follows: ‘ok’: pass ‘failed’ with ‘EXPECTED FAILURE’ in the task name: pass ‘failed’ with ‘TOGGLE RESULT’ in the task name: pass ‘ok’ with ‘TOGGLE RESULT’ in the task name: failure ‘failed’ due to an exception: error ‘failed’ for other reasons: failure ‘skipped’: skipped

## [Requirements](junit_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- enable in configuration

## [Parameters](junit_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **fail_on_change**  string | Consider any tasks reporting “changed” as a junit test failure  Default: `false`  Configuration:   - Environment variable: [`JUNIT_FAIL_ON_CHANGE`](../../environment_variables.md#envvar-JUNIT_FAIL_ON_CHANGE) |
| **fail_on_ignore**  string | Consider failed tasks as a junit test failure even if ignore_on_error is set  Default: `false`  Configuration:   - Environment variable: [`JUNIT_FAIL_ON_IGNORE`](../../environment_variables.md#envvar-JUNIT_FAIL_ON_IGNORE) |
| **hide_task_arguments**  string  added in Ansible 2.8 | Hide the arguments for a task  Default: `false`  Configuration:   - Environment variable: [`JUNIT_HIDE_TASK_ARGUMENTS`](../../environment_variables.md#envvar-JUNIT_HIDE_TASK_ARGUMENTS) |
| **include_setup_tasks_in_report**  string | Should the setup tasks be included in the final report  Default: `true`  Configuration:   - Environment variable: [`JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT`](../../environment_variables.md#envvar-JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT) |
| **output_dir**  string | Directory to write XML files to.  Default: `"~/.ansible.log"`  Configuration:   - Environment variable: [`JUNIT_OUTPUT_DIR`](../../environment_variables.md#envvar-JUNIT_OUTPUT_DIR) |
| **replace_out_of_tree_path**  string  added in ansible-core 2.12.3 | Replace the directory portion of an out-of-tree relative task path with the given placeholder  Default: `"none"`  Configuration:   - Environment variable: [`JUNIT_REPLACE_OUT_OF_TREE_PATH`](../../environment_variables.md#envvar-JUNIT_REPLACE_OUT_OF_TREE_PATH) |
| **task_class**  string | Configure the output to be one class per yaml file  Default: `false`  Configuration:   - Environment variable: [`JUNIT_TASK_CLASS`](../../environment_variables.md#envvar-JUNIT_TASK_CLASS) |
| **task_relative_path**  string  added in Ansible 2.8 | Configure the output to use relative paths to given directory  Default: `"none"`  Configuration:   - Environment variable: [`JUNIT_TASK_RELATIVE_PATH`](../../environment_variables.md#envvar-JUNIT_TASK_RELATIVE_PATH) |
| **test_case_prefix**  string  added in Ansible 2.8 | Consider a task only as test case if it has this value as prefix. Additionally failing tasks are recorded as failed test cases.  Default: `"<empty>"`  Configuration:   - Environment variable: [`JUNIT_TEST_CASE_PREFIX`](../../environment_variables.md#envvar-JUNIT_TEST_CASE_PREFIX) |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
