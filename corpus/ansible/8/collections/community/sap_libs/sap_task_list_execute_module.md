---
collection: ansible
version: "8"
title: "community.sap_libs.sap_task_list_execute module – Perform SAP Task list execution"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/sap_libs/sap_task_list_execute_module.html
fetched_at: 2026-07-28T01:59:18+00:00
---
# community.sap_libs.sap_task_list_execute module – Perform SAP Task list execution

> **Note:**
>
> This module is part of the [community.sap_libs collection](https://galaxy.ansible.com/ui/repo/published/community/sap_libs/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sap_libs`.
> You need further requirements to be able to use this module,
> see [Requirements](sap_task_list_execute_module.md#ansible-collections-community-sap-libs-sap-task-list-execute-module-requirements) for details.
>
> To use it in a playbook, specify: `community.sap_libs.sap_task_list_execute`.

New in community.sap_libs 0.1.0

- [Synopsis](sap_task_list_execute_module.md#synopsis)
- [Requirements](sap_task_list_execute_module.md#requirements)
- [Parameters](sap_task_list_execute_module.md#parameters)
- [Notes](sap_task_list_execute_module.md#notes)
- [Examples](sap_task_list_execute_module.md#examples)
- [Return Values](sap_task_list_execute_module.md#return-values)

## [Synopsis](sap_task_list_execute_module.md#id1)

- The [community.sap_libs.sap_task_list_execute](sap_task_list_execute_module.md#ansible-collections-community-sap-libs-sap-task-list-execute-module) module depends on `pyrfc` Python library (version 2.4.0 and upwards). Depending on distribution you are using, you may need to install additional packages to have these available.
- Tasks in the task list which requires manual activities will be confirmed automatically.
- This module will use the RFC package `STC_TM_API`.

## [Requirements](sap_task_list_execute_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrfc >= 2.4.0
- xmltodict

## [Parameters](sap_task_list_execute_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client**  string | The client number to connect to.  You must quote the value to ensure retaining the leading zeros.  **Default:** `"000"` |
| **conn_password**  string / required | The required password for the SAP system. |
| **conn_username**  string / required | The required username for the SAP system. |
| **host**  string / required | The required host for the SAP system. Can be either an FQDN or IP Address. |
| **sysnr**  string | The system number of the SAP system.  You must quote the value to ensure retaining the leading zeros.  **Default:** `"00"` |
| **task_parameters**  list / elements=dictionary | The tasks and the parameters for execution.  If the task list does not need any parameters, this could be empty.  If only specific tasks from the task list should be executed, the tasks even when no parameter is needed must be provided alongside with the module parameter *task_skip=true*. |
| **FIELDNAME**  string | The name of the field of the task. |
| **TASKNAME**  string / required | The name of the task in the task list. |
| **VALUE**  any | The value which have to be set. |
| **task_settings**  list / elements=string | Setting for the execution of the task list. This can be the following as in TCODE SE80 described. Check Mode `CHECKRUN`, Background Processing Active `BATCH` (this is the default value), Asynchronous Execution `ASYNC`, Trace Mode `TRACE`, Server Name `BATCH_TARGET`.  **Default:** `["BATCH"]` |
| **task_skip**  boolean | If this parameter is `true`, not defined tasks in *task_parameters* are skipped.  This could be the case when only certain tasks should run from the task list.  **Choices:**   - `false` ← (default) - `true` |
| **task_to_execute**  string / required | The task list which will be executed. |

## [Notes](sap_task_list_execute_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`. Always returns that the state has changed.

## [Examples](sap_task_list_execute_module.md#id5)

```yaml+jinja
# Pass in a message
- name: Test task execution
  community.sap_libs.sap_task_list_execute:
    conn_username: DDIC
    conn_password: Passwd1234
    host: 10.1.8.10
    sysnr: '01'
    client: '000'
    task_to_execute: SAP_BASIS_SSL_CHECK
    task_settings: batch

- name: Pass in input parameters
  community.sap_libs.sap_task_list_execute:
    conn_username: DDIC
    conn_password: Passwd1234
    host: 10.1.8.10
    sysnr: '00'
    client: '000'
    task_to_execute: SAP_BASIS_SSL_CHECK
    task_parameters :
      - { 'TASKNAME': 'CL_STCT_CHECK_SEC_CRYPTO', 'FIELDNAME': 'P_OPT2', 'VALUE': 'X' }
      - TASKNAME: CL_STCT_CHECK_SEC_CRYPTO
        FIELDNAME: P_OPT3
        VALUE: X
    task_settings: batch

# Exported environment variables
- name: Hint if module will fail with error message like ImportError libsapnwrfc.so...
  community.sap_libs.sap_task_list_execute:
    conn_username: DDIC
    conn_password: Passwd1234
    host: 10.1.8.10
    sysnr: '00'
    client: '000'
    task_to_execute: SAP_BASIS_SSL_CHECK
    task_settings: batch
  environment:
    SAPNWRFC_HOME: /usr/local/sap/nwrfcsdk
    LD_LIBRARY_PATH: /usr/local/sap/nwrfcsdk/lib
```

## [Return Values](sap_task_list_execute_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A small execution description.  **Returned:** always  **Sample:** `"Successful"` |
| **out**  list / elements=dictionary | A complete description of the executed tasks. If this is available.  **Returned:** on success  **Sample:** `["...", {"LOG": {"STCTM_S_LOG": [{"ACTIVITY": "U_CONFIG", "ACTIVITY_DESCR": "Configuration changed", "DETAILS": null, "EXEC_ID": "20210728184903.815739", "FIELD": null, "ID": "STC_TASK", "LOG_MSG_NO": "000000", "LOG_NO": null, "MESSAGE": "For radiobutton group ICM too many options are set; choose only one option", "MESSAGE_V1": "ICM", "MESSAGE_V2": null, "MESSAGE_V3": null, "MESSAGE_V4": null, "NUMBER": "048", "PARAMETER": null, "PERIOD": "M", "PERIOD_DESCR": "Maintenance", "ROW": "0", "SRC_LINE": "170", "SRC_OBJECT": "CL_STCTM_REPORT_UI            IF_STCTM_UI_TASK~SET_PARAMETERS", "SYSTEM": null, "TIMESTMP": "20210728184903", "TSTPNM": "DDIC", "TYPE": "E"}, "..."]}}]` |

### Authors

- Rainer Leber (@rainerleber)

### Collection links

- [Issue Tracker](https://github.com/sap-linuxlab/community.sap_libs)
- [Repository (Sources)](https://github.com/sap-linuxlab/community.sap_libs)
