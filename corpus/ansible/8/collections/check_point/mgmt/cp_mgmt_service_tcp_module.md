---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_service_tcp module – Manages service-tcp objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_service_tcp_module.html
fetched_at: 2026-07-28T01:17:21+00:00
---
# check_point.mgmt.cp_mgmt_service_tcp module – Manages service-tcp objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_service_tcp`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_service_tcp_module.md#synopsis)
- [Parameters](cp_mgmt_service_tcp_module.md#parameters)
- [Examples](cp_mgmt_service_tcp_module.md#examples)
- [Return Values](cp_mgmt_service_tcp_module.md#return-values)

## [Synopsis](cp_mgmt_service_tcp_module.md#id1)

- Manages service-tcp objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_service_tcp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggressive_aging**  dictionary | Sets short (aggressive) timeouts for idle connections. |
| **default_timeout**  integer | Default aggressive aging timeout in seconds. |
| **enable**  boolean | N/A  **Choices:**   - `false` - `true` |
| **timeout**  integer | Aggressive aging timeout in seconds. |
| **use_default_timeout**  boolean | N/A  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **groups**  list / elements=string | Collection of group identifiers. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **keep_connections_open_after_policy_installation**  boolean | Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.  **Choices:**   - `false` - `true` |
| **match_by_protocol_signature**  boolean | A value of true enables matching by the selected protocol’s signature - the signature identifies the protocol as genuine. Select this option to limit the port to the specified protocol. If the selected protocol does not support matching by signature, this field cannot be set to true.  **Choices:**   - `false` - `true` |
| **match_for_any**  boolean | Indicates whether this service is used when ‘Any’ is set as the rule’s service and there are several service objects with the same source port and protocol.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **override_default_settings**  boolean | Indicates whether this service is a Data Domain service which has been overridden.  **Choices:**   - `false` - `true` |
| **port**  string | The number of the port used to provide this service. To specify a port range, place a hyphen between the lowest and highest port numbers, for example 44-55. |
| **protocol**  string | Select the protocol type associated with the service, and by implication, the management server (if any) that enforces Content Security and Authentication for the service. Selecting a Protocol Type invokes the specific protocol handlers for each protocol type, thus enabling higher level of security by parsing the protocol, and higher level of connectivity by tracking dynamic actions (such as opening of ports). |
| **session_timeout**  integer | Time (in seconds) before the session times out. |
| **source_port**  string | Port number for the client side service. If specified, only those Source port Numbers will be Accepted, Dropped, or Rejected during packet inspection. Otherwise, the source port is not inspected. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **sync_connections_on_cluster**  boolean | Enables state-synchronized High Availability or Load Sharing on a ClusterXL or OPSEC-certified cluster.  **Choices:**   - `false` - `true` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **use_default_session_timeout**  boolean | Use default virtual session timeout.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_service_tcp_module.md#id3)

```yaml+jinja
- name: add-service-tcp
  cp_mgmt_service_tcp:
    aggressive_aging:
      enable: true
      timeout: 360
      use_default_timeout: false
    keep_connections_open_after_policy_installation: false
    match_for_any: true
    name: New_TCP_Service_1
    port: 5669
    session_timeout: 0
    state: present
    sync_connections_on_cluster: true

- name: set-service-tcp
  cp_mgmt_service_tcp:
    aggressive_aging:
      default_timeout: 3600
    color: green
    name: New_TCP_Service_1
    port: 5656
    state: present

- name: delete-service-tcp
  cp_mgmt_service_tcp:
    name: New_TCP_Service_1
    state: absent
```

## [Return Values](cp_mgmt_service_tcp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_service_tcp**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
