---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_threat_layers module – Manages THREAT LAYERS resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_threat_layers_module.html
fetched_at: 2026-07-28T01:18:13+00:00
---
# check_point.mgmt.cp_mgmt_threat_layers module – Manages THREAT LAYERS resource module

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_threat_layers`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_threat_layers_module.md#synopsis)
- [Parameters](cp_mgmt_threat_layers_module.md#parameters)
- [Examples](cp_mgmt_threat_layers_module.md#examples)
- [Return Values](cp_mgmt_threat_layers_module.md#return-values)

## [Synopsis](cp_mgmt_threat_layers_module.md#id1)

- This resource module allows for addition, deletion, or modification of CP Threat Layers.
- This resource module also takes care of gathering Threat Layers config facts

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cp_mgmt_threat_layers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of THREAT LAYERS options |
| **add_default_rule**  boolean | Indicates whether to include a default rule in the new layer.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **limit**  integer | The maximal number of returned results.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **name**  string | Object name. Must be unique in the domain. |
| **offset**  integer | Number of the results to initially skip.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **order**  list / elements=dictionary | Sorts results by the given field. By default the results are sorted in the ascending order by name. This parameter is relevant only for getting few objects.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **ASC**  string | Sorts results by the given field in ascending order. |
| **DESC**  string | Sorts results by the given field in descending order. |
| **round_trip**  string | If set to True, the round trip will filter out the module parameters from the response param, which will enable the user to fire the config request using the structured gathered data.  NOTE, this parameter makes relevance only with the GATHERED state, as for config states like, MERGED, REPLACED, and DELETED state it won’t make any config updates, as it’s not a module config parameter. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **state**  string | The state the configuration should be left in  The state *gathered* will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the *gathered* key within the result.  **Choices:**   - `"merged"` - `"replaced"` - `"gathered"` - `"deleted"` |

## [Examples](cp_mgmt_threat_layers_module.md#id3)

```yaml+jinja
# Using MERGED state
# -------------------

- name: To Add Merge Threat-Layers config
  cp_mgmt_threat_layers:
    state: merged
    config:
      name: New Layer 1
      add_default_rule: true
      tags:
        - test_threat_layer
      color: turquoise
      comments: test description
      ignore_warnings: false
      ignore_errors: false
      round_trip: true

# RUN output:
# -----------

# mgmt_threat_layers:
#   after:
#     color: turquoise
#     comments: test description
#     icon: ApplicationFirewall/rulebase
#     ips-layer: false
#     name: New Layer 1
#     tags:
#     - test_threat_layer
#   before: {}

# Using REPLACED state
# --------------------

- name: Replace Threat-layer config
  cp_mgmt_threat_layers:
    state: replaced
    config:
      name: New Layer 1
      add_default_rule: true
      tags:
        - test_threat_layer_replaced
      color: cyan
      comments: REPLACED description
      ignore_warnings: false
      ignore_errors: false
      round_trip: true

# RUN output:
# -----------

# mgmt_threat_layers:
#   after:
#     color: cyan
#     comments: REPLACED description
#     icon: ApplicationFirewall/rulebase
#     ips-layer: false
#     name: New Layer 1
#     tags:
#     - test_threat_layer_replaced
#   before:
#     color: turquoise
#     comments: test description
#     icon: ApplicationFirewall/rulebase
#     ips-layer: false
#     name: New Layer 1
#     tags:
#     - test_threat_layer

# Using GATHERED state
# --------------------

# 1. With Round Trip set to True

- name: To Gather threat-layer by Name
  cp_mgmt_threat_layers:
    config:
      name: New Layer 1
      round_trip: true
    state: gathered

# RUN output:
# -----------

# gathered:
#   color: turquoise
#   comments: test description
#   domain: SMC User
#   icon: ApplicationFirewall/rulebase
#   ips-layer: false
#   name: New Layer 1
#   read-only: false
#   tags:
#   - test_threat_layer
#   uid: 4dc060e2-0ed6-48c5-9b0f-3d2fbeb552ba

# 2. With Round Trip set to False which is the default behaviour

- name: To Gather threat-layer by Name
  cp_mgmt_threat_layers:
    config:
      name: New Layer 1
    state: gathered

# RUN output:
# -----------

# gathered:
#   color: turquoise
#   comments: test description
#   domain:
#     domain-type: domain
#     name: SMC User
#     uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#   icon: ApplicationFirewall/rulebase
#   ips-layer: false
#   meta-info:
#     creation-time:
#       iso-8601: 2022-11-21T07:30+0000
#       posix: 1669015820472
#     creator: admin
#     last-modifier: admin
#     last-modify-time:
#       iso-8601: 2022-11-21T07:30+0000
#       posix: 1669015821024
#     lock: unlocked
#     validation-state: ok
#   name: New Layer 1
#   read-only: false
#   tags:
#   - domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     name: test_threat_layer
#     type: tag
#     uid: 59f23149-ed5e-439f-9012-0cdf222a1c97
#   type: threat-layer
#   uid: ca196a80-fdc4-4e7b-8b25-e3eed125a25f

# 3. Gather ALL threat-layer config with DESC order filter

- name: To Gather ALL threat-layer and order by Name
  cp_mgmt_threat_layers:
    config:
      order:
        - DESC: name
    state: gathered

# RUN output:
# -----------

# gathered:
#   - color: black
#     comments: ''
#     domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     icon: ApplicationFirewall/sharedrulebase
#     ips-layer: true
#     meta-info:
#       creation-time:
#         iso-8601: 2020-01-20T09:43+0000
#         posix: 1579513387322
#       creator: System
#       last-modifier: System
#       last-modify-time:
#         iso-8601: 2020-01-20T09:43+0000
#         posix: 1579513387377
#       lock: unlocked
#       validation-state: ok
#     name: IPS
#     read-only: false
#     tags: []
#     type: threat-layer
#     uid: 90678011-1bcb-4296-8154-fa58c23ecf3b
#   - color: black
#     comments: ''
#     domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     icon: ApplicationFirewall/rulebase
#     ips-layer: false
#     meta-info:
#       creation-time:
#         iso-8601: 2020-01-20T09:43+0000
#         posix: 1579513386848
#       creator: System
#       last-modifier: System
#       last-modify-time:
#         iso-8601: 2020-01-20T09:43+0000
#         posix: 1579513387396
#       lock: unlocked
#       validation-state: ok
#     name: Standard Threat Prevention
#     read-only: false
#     tags: []
#     type: threat-layer
#     uid: 0dbe7c44-6d3f-4f28-8f2b-0e6790e57f8a

# Using DELETED state
# -------------------

- name: Delete Threat-layer config by Name and Layer
  cp_mgmt_threat_layers:
    config:
      layer: IPS
      name: First threat layer
      round_trip: true
    state: deleted

# RUN output:
# -----------

# mgmt_threat_layers:
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
#     name: First threat layer
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

## [Return Values](cp_mgmt_threat_layers_module.md#id4)

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
