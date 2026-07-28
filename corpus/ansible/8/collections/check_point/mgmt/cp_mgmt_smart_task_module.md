---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_smart_task module – Manages smart-task objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_smart_task_module.html
fetched_at: 2026-07-28T01:17:59+00:00
---
# check_point.mgmt.cp_mgmt_smart_task module – Manages smart-task objects on Checkpoint over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_smart_task`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_smart_task_module.md#synopsis)
- [Parameters](cp_mgmt_smart_task_module.md#parameters)
- [Examples](cp_mgmt_smart_task_module.md#examples)
- [Return Values](cp_mgmt_smart_task_module.md#return-values)

## [Synopsis](cp_mgmt_smart_task_module.md#id1)

- Manages smart-task objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_smart_task_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  dictionary | The action to be run when the trigger is fired. |
| **run_script**  dictionary | When the trigger is fired, runs the configured Repository Script on the defined targets.<br>The trigger data is then passed to the script as the first parameter. The parameter is JSON encoded in Base64 format. |
| **repository_script**  string | Repository script that is executed when the trigger is fired., identified by the name or UID. |
| **targets**  list / elements=string | Targets to execute the script on. |
| **time_out**  integer | Script execution time-out in seconds. |
| **send_mail**  dictionary | When the trigger is fired, sends the configured email to the defined recipients. |
| **mail_settings**  dictionary | The required settings to send the mail by. |
| **attachment**  string | What file should be attached to the mail.  **Choices:**   - `"no attachment"` - `"changes report"` - `"policy installation report"` |
| **bcc_recipients**  string | A comma separated list of bcc recipient mail addresses. |
| **body**  string | The email body. |
| **cc_recipients**  string | A comma separated list of cc recipient mail addresses. |
| **recipients**  string | A comma separated list of recipient mail addresses. |
| **sender_email**  string | An email address to send the mail from. |
| **subject**  string | The email subject. |
| **smtp_server**  string | The UID or the name a preconfigured SMTP server object. |
| **send_web_request**  dictionary | When the trigger is fired, sends an HTTPS POST web request to the configured URL.<br>The trigger data will be passed along with the SmartTask’s custom data in the request’s payload. |
| **fingerprint**  string | The SHA1 fingerprint of the URL’s SSL certificate. Used to trust servers with self-signed SSL certificates. |
| **override_proxy**  boolean | Option to send to the web request via a proxy other than the Management’s Server proxy (if defined).  **Choices:**   - `false` - `true` |
| **proxy_url**  string | URL of the proxy used to send the request. |
| **shared_secret**  string | Shared secret that can be used by the target server to identify the Management Server.<br>The value will be sent as part of the request in the “X-chkp-shared-secret” header. |
| **time_out**  integer | Web Request time-out in seconds. |
| **url**  string | URL used for the web request. |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **custom_data**  string | Per SmartTask custom data in JSON format.<br>When the trigger is fired, the trigger data is converted to JSON. The custom data is then concatenated to the trigger data JSON. |
| **description**  string | Description of the SmartTask’s functionality and options. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Whether the SmartTask is enabled and will run when triggered.  **Choices:**   - `false` - `true` |
| **fail_open**  boolean | If the action fails to execute, whether to treat the execution failure as an error, or continue.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **trigger**  string | Trigger type associated with the SmartTask. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_smart_task_module.md#id3)

```yaml+jinja
- name: add-smart-task
  cp_mgmt_smart_task:
    action:
      run_script:
        repository_script: Session Name Validation Script
        time_out: 30
    custom_data: '{"session-name-format": "CR"}'
    description: Run a validation script that ensures that the a session name matches the expected name format as described in the Custom Data field.
    enabled: true
    name: Validate Session Name Before Publish
    state: present
    trigger: Before Publish

- name: set-smart-task
  cp_mgmt_smart_task:
    action:
      send_web_request:
        fingerprint: 3FDD902286DBF130EF4CEC7939EF81060AB0FEB6
        url: https://demo.example.com/policy-installation-reports
    custom_data: '{"mail-address": "example-admin@example-corp.com"}'
    description: Send policy installation results to the mail address specified in the Custom Data field using the corporate's dedicated web server.
    enabled: true
    name: Send Policy Installation Reports
    state: present
    trigger: After Install Policy

- name: delete-smart-task
  cp_mgmt_smart_task:
    name: Validate Session Name Before Publish
    state: absent
```

## [Return Values](cp_mgmt_smart_task_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_smart_task**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
