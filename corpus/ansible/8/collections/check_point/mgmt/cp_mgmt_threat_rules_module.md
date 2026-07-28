---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_threat_rules module – Manages THREAT RULES resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_threat_rules_module.html
fetched_at: 2026-07-28T01:18:17+00:00
---
# check_point.mgmt.cp_mgmt_threat_rules module – Manages THREAT RULES resource module

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_threat_rules`.

New in check_point.mgmt 4.1.0

- [Synopsis](cp_mgmt_threat_rules_module.md#synopsis)
- [Parameters](cp_mgmt_threat_rules_module.md#parameters)
- [Examples](cp_mgmt_threat_rules_module.md#examples)
- [Return Values](cp_mgmt_threat_rules_module.md#return-values)

## [Synopsis](cp_mgmt_threat_rules_module.md#id1)

- This resource module allows for addition, deletion, or modification of CP Threat Rules.
- This resource module also takes care of gathering Threat Rules config facts

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cp_mgmt_threat_rules_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of ACCESS RULES options |
| **action**  string | Action-the enforced profile. |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **comments**  string | Comments string. |
| **destination**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **destination_negate**  boolean | True if negate is set for destination.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Enable/Disable the rule.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **install_on**  list / elements=string | Which Gateways identified by the name or UID to install the policy on. |
| **layer**  string | Layer that the rule belongs to identified by the name or UID. |
| **name**  string | Rule name. |
| **position**  string | Position in the rulebase.  The use of values “top” and “bottom” may not be idempotent. |
| **protected_scope**  list / elements=string | Collection of objects defining Protected Scope identified by the name or UID. |
| **protected_scope_negate**  boolean | True if negate is set for Protected Scope.  **Choices:**   - `false` - `true` |
| **service**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **service_negate**  boolean | True if negate is set for Service.  **Choices:**   - `false` - `true` |
| **source**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **source_negate**  boolean | True if negate is set for source.  **Choices:**   - `false` - `true` |
| **track**  string | Packet tracking. |
| **track_settings**  dictionary | Threat rule track settings. |
| **packet_capture**  boolean | Packet capture.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **state**  string | The state the configuration should be left in  The state *gathered* will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the *gathered* key within the result.  **Choices:**   - `"merged"` - `"replaced"` - `"gathered"` - `"deleted"` |

## [Examples](cp_mgmt_threat_rules_module.md#id3)

```yaml+jinja
# Using MERGED state
# -------------------

- name: To Add Merge Threat-Rules config
  cp_mgmt_threat_rules:
    state: merged
    config:
      comments: This is the THREAT RULE
      install_on: Policy Targets
      layer: IPS
      name: First threat rule
      position: 1
      protected_scope: All_Internet
      track: None

# RUN output:
# -----------

# mgmt_threat_rules:
#   after:
#     action: Optimized
#     comments: This is the THREAT RULE
#     destination:
#     - Any
#     destination_negate: false
#     enabled: true
#     install_on:
#     - Policy Targets
#     layer: 90678011-1bcb-4296-8154-fa58c23ecf3b
#     name: First threat rule
#     protected_scope:
#     - All_Internet
#     protected_scope_negate: false
#     service:
#     - Any
#     service_negate: false
#     source:
#     - Any
#     source_negate: false
#     track: None
#     track_settings:
#       packet_capture: true
#   before: {}

# Using REPLACED state
# --------------------

- name: Replace Threat-rule config
  cp_mgmt_threat_rules:
    config:
      comments: This is the REPLACED THREAT RULE
      install_on: Policy Targets
      layer: IPS
      name: First threat rule
      position: 1
      protected_scope: All_Internet
      track_settings:
        packet_capture: false
    state: replaced

# RUN output:
# -----------

# mgmt_threat_rules:
#   after:
#     action: Optimized
#     comments: This is the REPLACED THREAT RULE
#     destination:
#     - Any
#     destination_negate: false
#     enabled: true
#     install_on:
#     - Policy Targets
#     layer: 90678011-1bcb-4296-8154-fa58c23ecf3b
#     name: First threat rule
#     protected_scope:
#     - All_Internet
#     protected_scope_negate: false
#     service:
#     - Any
#     service_negate: false
#     source:
#     - Any
#     source_negate: false
#     track: None
#     track_settings:
#       packet_capture: false
#   before:
#     action: Optimized
#     comments: This is the THREAT RULE
#     destination:
#     - Any
#     destination_negate: false
#     enabled: true
#     install_on:
#     - Policy Targets
#     layer: 90678011-1bcb-4296-8154-fa58c23ecf3b
#     name: First threat rule
#     protected_scope:
#     - All_Internet
#     protected_scope_negate: false
#     service:
#     - Any
#     service_negate: false
#     source:
#     - Any
#     source_negate: false
#     track: None
#     track_settings:
#       packet_capture: true

# Using GATHERED state
# --------------------

- name: To Gather threat-rule by Name
  cp_mgmt_threat_rules:
    config:
      layer: IPS
      name: First threat rule
    state: gathered

# RUN output:
# -----------

# gathered:
#   action: Optimized
#   comments: This is the THREAT RULE
#   destination:
#   - Any
#   destination_negate: false
#   domain: SMC User
#   enabled: true
#   install_on:
#   - Policy Targets
#   layer: 90678011-1bcb-4296-8154-fa58c23ecf3b
#   name: First threat rule
#   protected_scope:
#   - All_Internet
#   protected_scope_negate: false
#   service:
#   - Any
#   service_negate: false
#   source:
#   - Any
#   source_negate: false
#   track: None
#   track_settings:
#     packet_capture: true
#   uid: ef832f64-fbe0-4b4e-85b8-8420911c449f

# Using DELETED state
# -------------------

- name: Delete Threat-rule config by Name and Layer
  cp_mgmt_threat_rules:
    config:
      layer: IPS
      name: First threat rule
    state: deleted

# RUN output:
# -----------

# mgmt_threat_rules:
#   after: {}
#   before:
#     action: Optimized
#     comments: This is the THREAT RULE
#     destination:
#     - Any
#     destination_negate: false
#     enabled: true
#     install_on:
#     - Policy Targets
#     layer: 90678011-1bcb-4296-8154-fa58c23ecf3b
#     name: First threat rule
#     protected_scope:
#     - All_Internet
#     protected_scope_negate: false
#     service:
#     - Any
#     service_negate: false
#     source:
#     - Any
#     source_negate: false
#     track: None
#     track_settings:
#       packet_capture: true
```

## [Return Values](cp_mgmt_threat_rules_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *deleted*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |

### Authors

- Ansible Team

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
