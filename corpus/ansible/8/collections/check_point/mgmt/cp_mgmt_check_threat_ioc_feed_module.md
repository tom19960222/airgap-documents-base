---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_check_threat_ioc_feed module – Check if a target can reach or parse a threat IOC feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters)."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_check_threat_ioc_feed_module.html
fetched_at: 2026-07-28T01:15:56+00:00
---
# check_point.mgmt.cp_mgmt_check_threat_ioc_feed module – Check if a target can reach or parse a threat IOC feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters).

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_check_threat_ioc_feed`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_check_threat_ioc_feed_module.md#synopsis)
- [Parameters](cp_mgmt_check_threat_ioc_feed_module.md#parameters)
- [Examples](cp_mgmt_check_threat_ioc_feed_module.md#examples)
- [Return Values](cp_mgmt_check_threat_ioc_feed_module.md#return-values)

## [Synopsis](cp_mgmt_check_threat_ioc_feed_module.md#id1)

- Check if a target can reach or parse a threat IOC feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters).
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_check_threat_ioc_feed_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **ioc_feed**  dictionary | threat ioc feed parameters. |
| **action**  string | The feed indicator’s action.  **Choices:**   - `"Prevent"` - `"Detect"` |
| **certificate_id**  string | Certificate SHA-1 fingerprint to access the feed. |
| **custom_comment**  integer | Custom IOC feed - the column number of comment. |
| **custom_confidence**  integer | Custom IOC feed - the column number of confidence. |
| **custom_header**  list / elements=dictionary | Custom HTTP headers. |
| **header_name**  string | The name of the HTTP header we wish to add. |
| **header_value**  string | The name of the HTTP value we wish to add. |
| **custom_name**  integer | Custom IOC feed - the column number of name. |
| **custom_severity**  integer | Custom IOC feed - the column number of severity. |
| **custom_type**  integer | Custom IOC feed - the column number of type in case a specific type is not chosen. |
| **custom_value**  integer | Custom IOC feed - the column number of value in case a specific type is chosen. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Sets whether this indicator feed is enabled.  **Choices:**   - `false` - `true` |
| **feed_type**  string | Feed type to be enforced.  **Choices:**   - `"any type"` - `"domain"` - `"ip address"` - `"md5"` - `"url"` - `"ip range"` - `"mail subject"` - `"mail from"` - `"mail to"` - `"mail reply to"` - `"mail cc"` - `"sha1"` - `"sha256"` |
| **feed_url**  string | URL of the feed. URL should be written as http or https. |
| **fields_delimiter**  string | The delimiter that separates between the columns in the feed. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_lines_that_start_with**  string | A prefix that will determine which lines to ignore. |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **name**  string | Object name. |
| **password**  string | password for authenticating with the URL. |
| **use_custom_feed_settings**  boolean | Set in order to configure a custom indicator feed.  **Choices:**   - `false` - `true` |
| **use_gateway_proxy**  boolean | Use the gateway’s proxy for retrieving the feed.  **Choices:**   - `false` - `true` |
| **username**  string | username for authenticating with the URL. |
| **targets**  list / elements=string | On what targets to execute this command. Targets may be identified by their name, or object unique identifier. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_check_threat_ioc_feed_module.md#id3)

```yaml+jinja
- name: check-threat-ioc-feed
  cp_mgmt_check_threat_ioc_feed:
    ioc_feed:
      name: existing_feed
    targets: corporate-gateway
```

## [Return Values](cp_mgmt_check_threat_ioc_feed_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_check_threat_ioc_feed**  dictionary | The checkpoint check-threat-ioc-feed output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
