---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_network_feed module – Manages network-feed objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_network_feed_module.html
fetched_at: 2026-07-28T01:16:54+00:00
---
# check_point.mgmt.cp_mgmt_network_feed module – Manages network-feed objects on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_network_feed`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_network_feed_module.md#synopsis)
- [Parameters](cp_mgmt_network_feed_module.md#parameters)
- [Examples](cp_mgmt_network_feed_module.md#examples)
- [Return Values](cp_mgmt_network_feed_module.md#return-values)

## [Synopsis](cp_mgmt_network_feed_module.md#id1)

- Manages network-feed objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_network_feed_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **certificate_id**  string | Certificate SHA-1 fingerprint to access the feed. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **custom_header**  list / elements=dictionary | Headers to allow different authentication methods with the URL. |
| **header_name**  string | The name of the HTTP header we wish to add. |
| **header_value**  string | The name of the HTTP value we wish to add. |
| **data_column**  integer | Number of the column that contains the feed’s data. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **feed_format**  string | Feed file format.  **Choices:**   - `"Flat List"` - `"JSON"` |
| **feed_type**  string | Feed type to be enforced.  **Choices:**   - `"Domain"` - `"IP Address"` - `"IP Address/Domain"` |
| **feed_url**  string | URL of the feed. URL should be written as http or https. |
| **fields_delimiter**  string | The delimiter that separates between the columns in the feed. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_lines_that_start_with**  string | A prefix that will determine which lines to ignore. |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **json_query**  string | JQ query to be parsed. |
| **name**  string / required | Object name. |
| **password**  string | password for authenticating with the URL. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **update_interval**  integer | Interval in minutes for updating the feed on the Security Gateway. |
| **use_gateway_proxy**  boolean | Use the gateway’s proxy for retrieving the feed.  **Choices:**   - `false` - `true` |
| **username**  string | username for authenticating with the URL. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_network_feed_module.md#id3)

```yaml+jinja
- name: add-network-feed
  cp_mgmt_network_feed:
    custom_header:
    - header_name: header1
      header_value: value1
    - header_name: header2
      header_value: value2
    data_column: 1
    feed_format: Flat List
    feed_type: IP Address
    feed_url: https://www.feedsresource.com/resource
    fields_delimiter: "     "
    ignore_lines_that_start_with: '!'
    name: network_feed
    password: feed_password
    state: present
    update_interval: 60
    use_gateway_proxy: false
    username: feed_username

- name: set-network-feed
  cp_mgmt_network_feed:
    custom_header:
    - header_name: new_header
      header_value: new_value
    data_column: 1
    feed_format: Flat List
    feed_type: IP Address
    feed_url: https://www.feedsresource.com/new_resource
    fields_delimiter: ','
    ignore_lines_that_start_with: '!'
    name: network_feed
    password: new_password
    state: present
    update_interval: 60
    use_gateway_proxy: false
    username: new_username

- name: delete-network-feed
  cp_mgmt_network_feed:
    name: network_feed
    state: absent
```

## [Return Values](cp_mgmt_network_feed_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_network_feed**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
