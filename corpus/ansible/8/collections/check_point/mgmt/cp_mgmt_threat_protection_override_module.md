---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_threat_protection_override module – Edit existing object using object name or uid."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_threat_protection_override_module.html
fetched_at: 2026-07-28T01:18:15+00:00
---
# check_point.mgmt.cp_mgmt_threat_protection_override module – Edit existing object using object name or uid.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_threat_protection_override`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_threat_protection_override_module.md#synopsis)
- [Parameters](cp_mgmt_threat_protection_override_module.md#parameters)
- [Examples](cp_mgmt_threat_protection_override_module.md#examples)
- [Return Values](cp_mgmt_threat_protection_override_module.md#return-values)

## [Synopsis](cp_mgmt_threat_protection_override_module.md#id1)

- Edit existing object using object name or uid.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_threat_protection_override_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **comments**  string | Protection comments. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **follow_up**  boolean | Tag the protection with pre-defined follow-up flag.  **Choices:**   - `false` - `true` |
| **name**  string | Object name. |
| **overrides**  list / elements=dictionary | Overrides per profile for this protection<br> Note, Remove override for Core protections removes only the action’s override. Remove override for Threat Cloud protections removes the action, track and packet captures. |
| **action**  string | Protection action.  **Choices:**   - `"Threat Cloud: Inactive"` - `"Detect"` - `"Prevent <br> Core: Drop"` - `"Inactive"` - `"Accept"` |
| **capture_packets**  boolean | Capture packets.  **Choices:**   - `false` - `true` |
| **profile**  string | Profile name. |
| **track**  string | Tracking method for protection.  **Choices:**   - `"none"` - `"log"` - `"alert"` - `"mail"` - `"snmp trap"` - `"user alert"` - `"user alert 1"` - `"user alert 2"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_threat_protection_override_module.md#id3)

```yaml+jinja
- name: threat_protection_override
  cp_mgmt_threat_protection_override:
    name: FTP Commands
    overrides:
    - action: inactive
      capture_packets: true
      profile: New Profile 1
      track: None
    state: present
```

## [Return Values](cp_mgmt_threat_protection_override_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_threat_protection_override**  dictionary | The checkpoint threat_protection_override output.  **Returned:** always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
