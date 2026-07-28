---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_smtp_server module – Manages smtp-server objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_smtp_server_module.html
fetched_at: 2026-07-28T01:18:01+00:00
---
# check_point.mgmt.cp_mgmt_smtp_server module – Manages smtp-server objects on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_smtp_server`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_smtp_server_module.md#synopsis)
- [Parameters](cp_mgmt_smtp_server_module.md#parameters)
- [Examples](cp_mgmt_smtp_server_module.md#examples)
- [Return Values](cp_mgmt_smtp_server_module.md#return-values)

## [Synopsis](cp_mgmt_smtp_server_module.md#id1)

- Manages smtp-server objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_smtp_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authentication**  boolean | Does the mail server requires authentication.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **encryption**  string | Encryption type.  **Choices:**   - `"none"` - `"ssl"` - `"tls"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **password**  string | A password for the SMTP server. |
| **port**  integer | The SMTP port to use. |
| **server**  string | The SMTP server address. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **username**  string | A username for the SMTP server. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_smtp_server_module.md#id3)

```yaml+jinja
- name: add-smtp-server
  cp_mgmt_smtp_server:
    encryption: none
    name: SMTP1
    port: '25'
    server: smtp.example.com
    state: present

- name: set-smtp-server
  cp_mgmt_smtp_server:
    name: SMTP
    port: '25'
    server: smtp.example.com
    state: present

- name: delete-smtp-server
  cp_mgmt_smtp_server:
    name: SMTP
    state: absent
```

## [Return Values](cp_mgmt_smtp_server_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_smtp_server**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
