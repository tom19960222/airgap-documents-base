---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_access_layers module – Manages ACCESS LAYERS resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_access_layers_module.html
fetched_at: 2026-07-28T01:15:35+00:00
---
# check_point.mgmt.cp_mgmt_access_layers module – Manages ACCESS LAYERS resource module

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_access_layers`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_access_layers_module.md#synopsis)
- [Parameters](cp_mgmt_access_layers_module.md#parameters)
- [Examples](cp_mgmt_access_layers_module.md#examples)
- [Return Values](cp_mgmt_access_layers_module.md#return-values)

## [Synopsis](cp_mgmt_access_layers_module.md#id1)

- This resource module allows for addition, deletion, or modification of CP Access Layers.
- This resource module also takes care of gathering Access layer config facts

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cp_mgmt_access_layers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of ACCESS LAYERS options |
| **add_default_rule**  boolean | Indicates whether to include a cleanup rule in the new layer.  **Choices:**   - `false` - `true` |
| **applications_and_url_filtering**  boolean | Whether to enable Applications & URL Filtering blade on the layer.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **content_awareness**  boolean | Whether to enable Content Awareness blade on the layer.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **detect_using_x_forward_for**  boolean | Whether to use X-Forward-For HTTP header, which is added by the proxy server to keep track of the original source IP.  **Choices:**   - `false` - `true` |
| **firewall**  boolean | Whether to enable Firewall blade on the layer.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **implicit_cleanup_action**  string | The default “catch-all” action for traffic that does not match any explicit or implied rules in the layer.  **Choices:**   - `"drop"` - `"accept"` |
| **limit**  integer | The maximal number of returned results.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **mobile_access**  boolean | Whether to enable Mobile Access blade on the layer.  **Choices:**   - `false` - `true` |
| **name**  string | Object name. Must be unique in the domain. |
| **offset**  integer | Number of the results to initially skip.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **order**  list / elements=dictionary | Sorts results by the given field. By default the results are sorted in the ascending order by name. This parameter is relevant only for getting few objects.  NOTE, this parameter is a valid parameter only for the GATHERED state, for config states like, MERGED, REPLACED, and DELETED state it won’t be applicable. |
| **ASC**  string | Sorts results by the given field in ascending order. |
| **DESC**  string | Sorts results by the given field in descending order. |
| **round_trip**  boolean | If set to True, the round trip will filter out the module parameters from the response param, which will enable the user to fire the config request using the structured gathered data.  NOTE, this parameter makes relevance only with the GATHERED state, as for config states like, MERGED, REPLACED, and DELETED state it won’t make any config updates, as it’s not a module config parameter.  **Choices:**   - `false` - `true` |
| **shared**  boolean | Whether this layer is shared.  **Choices:**   - `false` - `true` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **state**  string | The state the configuration should be left in  The state *gathered* will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the *gathered* key within the result.  **Choices:**   - `"merged"` - `"replaced"` - `"gathered"` - `"deleted"` |

## [Examples](cp_mgmt_access_layers_module.md#id3)

```yaml+jinja
# Using MERGED state
# -------------------

- name: Merge Access-layer config
  cp_mgmt_access_layers:
    state: merged
    config:
      name: New Layer 1
      add_default_rule: true
      applications_and_url_filtering: true
      content_awareness: true
      detect_using_x_forward_for: false
      firewall: true
      implicit_cleanup_action: drop
      mobile_access: true
      shared: false
      tags:
      - test_layer
      color: aquamarine
      comments: test description
      details_level: full
      ignore_warnings: false
      ignore_errors: false
      round_trip: true

# RUN output:
# -----------

# mgmt_access_layers:
#   after:
#     applications_and_url_filtering: true
#     color: aquamarine
#     comments: test description
#     content_awareness: true
#     detect_using_x_forward_for: false
#     domain: SMC User
#     firewall: true
#     icon: ApplicationFirewall/rulebase
#     implicit_cleanup_action: drop
#     mobile_access: true
#     name: New Layer 1
#     shared: false
#     tags:
#     - test_layer
#     uid: eb74d7fe-81a6-4e6c-aedb-d2d6599f965e
#   before: {}

# Using REPLACED state
# --------------------

- name: Replace Access-layer config
  cp_mgmt_access_layers:
    state: replaced
    config:
      name: New Layer 1
      add_default_rule: true
      applications_and_url_filtering: true
      content_awareness: false
      detect_using_x_forward_for: false
      firewall: true
      implicit_cleanup_action: drop
      mobile_access: true
      shared: true
      tags:
      - test_layer_replaced
      color: cyan
      comments: test REPLACE description
      details_level: full
      ignore_warnings: false
      ignore_errors: false
      round_trip: true

# RUN output:
# -----------

# mgmt_access_layers:
#   after:
#     applications_and_url_filtering: true
#     color: cyan
#     comments: test REPLACE description
#     content_awareness: false
#     detect_using_x_forward_for: false
#     domain: SMC User
#     firewall: true
#     icon: ApplicationFirewall/sharedrulebase
#     implicit_cleanup_action: drop
#     mobile_access: true
#     name: New Layer 1
#     shared: true
#     tags:
#     - test_layer_replaced
#     uid: a4e2bbc1-ec94-4b85-9b00-07ad1279ac12
#   before:
#     applications_and_url_filtering: true
#     color: aquamarine
#     comments: test description
#     content_awareness: true
#     detect_using_x_forward_for: false
#     firewall: true
#     icon: ApplicationFirewall/rulebase
#     implicit_cleanup_action: drop
#     mobile_access: true
#     name: New Layer 1
#     shared: false
#     tags:
#     - test_layer

# Using GATHERED state
# --------------------

# 1. With Round Trip set to True

- name: Gather Access-layers config by Name
  cp_mgmt_access_layers:
    state: gathered
    config:
      name: New Layer 1
      round_trip: true

# RUN output:
# -----------

# gathered:
#   applications_and_url_filtering: true
#   color: aquamarine
#   comments: test description
#   content_awareness: true
#   detect_using_x_forward_for: false
#   domain: SMC User
#   firewall: true
#   icon: ApplicationFirewall/rulebase
#   implicit_cleanup_action: drop
#   mobile_access: true
#   name: New Layer 1
#   shared: false
#   tags:
#   - test_layer
#   uid: eb74d7fe-81a6-4e6c-aedb-d2d6599f965e

# 2. With Round Trip set to False which is the default behaviour

- name: Gather Access-layers config by Name
  cp_mgmt_access_layers:
    state: gathered
    config:
      name: New Layer 1

# RUN output:
# -----------

# gathered:
#   applications_and_url_filtering: true
#   color: turquoise
#   comments: test description
#   content_awareness: true
#   detect_using_x_forward_for: false
#   domain:
#     domain-type: domain
#     name: SMC User
#     uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#   firewall: true
#   icon: ApplicationFirewall/rulebase
#   implicit_cleanup_action: drop
#   meta-info:
#     creation-time:
#       iso-8601: 2022-11-21T07:34+0000
#       posix: 1669016073937
#     creator: admin
#     last-modifier: admin
#     last-modify-time:
#       iso-8601: 2022-11-21T07:34+0000
#       posix: 1669016074765
#     lock: unlocked
#     validation-state: ok
#   mobile_access: true
#   name: New Layer 1
#   read-only: false
#   shared: false
#   tags:
#   - domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     name: test_layer
#     type: tag
#     uid: 22cc8b0d-984f-47de-b1f6-276b3377eb0c
#   type: access-layer
#   uid: a54e47d3-22fc-4aff-90d9-f644aa4a1522

# 3. Gather ALL threat-layer config with DESC order filter

- name: To Gather ALL access-layer and order by Name
  cp_mgmt_access_layers:
    config:
      order:
        - DESC: name
    state: gathered

# RUN output:
# -----------

# gathered:
#   - domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     name: New Layer 1
#     type: access-layer
#     uid: a54e47d3-22fc-4aff-90d9-f644aa4a1522
#   - domain:
#       domain-type: domain
#       name: SMC User
#       uid: 41e821a0-3720-11e3-aa6e-0800200c9fde
#     name: Network
#     type: access-layer
#     uid: 63b7fe60-76d2-4287-bca5-21af87337b0a

# Using DELETED state
# -------------------

- name: Delete Access-layer config by Name
  cp_mgmt_access_layers:
    state: deleted
    config:
      name: New Layer 1

# RUN output:
# -----------

# mgmt_access_layers:
#   after: {}
#   before:
#     applications_and_url_filtering: true
#     color: cyan
#     comments: test REPLACE description
#     content_awareness: false
#     detect_using_x_forward_for: false
#     domain: SMC User
#     firewall: true
#     icon: ApplicationFirewall/sharedrulebase
#     implicit_cleanup_action: drop
#     mobile_access: true
#     name: New Layer 1
#     shared: true
#     tags:
#     - test_layer_replaced
#     uid: a4e2bbc1-ec94-4b85-9b00-07ad1279ac12
```

## [Return Values](cp_mgmt_access_layers_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *deleted*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |

### Authors

- Ansible Security Automation Team (@justjais) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
