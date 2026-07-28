---
collection: ansible
version: "6"
title: "ibm.qradar.qradar_analytics_rules module – Qradar Analytics Rules Management resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/qradar/qradar_analytics_rules_module.html
fetched_at: 2026-07-27T17:50:15+00:00
---
# ibm.qradar.qradar_analytics_rules module – Qradar Analytics Rules Management resource module

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ibm/qradar) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.qradar_analytics_rules`.

New in ibm.qradar 2.1.0

- [Synopsis](qradar_analytics_rules_module.md#synopsis)
- [Parameters](qradar_analytics_rules_module.md#parameters)
- [Examples](qradar_analytics_rules_module.md#examples)
- [Return Values](qradar_analytics_rules_module.md#return-values)

## [Synopsis](qradar_analytics_rules_module.md#id1)

- This module allows for modification, deletion, and checking of Analytics Rules in QRadar

## [Parameters](qradar_analytics_rules_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of Qradar Analytics Rules options |
| **enabled**  boolean | Check if the rule is enabled  Choices:   - `false` - `true` |
| **fields**  list / elements=string | List of params filtered from the Rule config  NOTE, this param is valid only via state GATHERED.  Choices:   - `"average_capacity"` - `"base_capacity"` - `"base_host_id"` - `"capacity_timestamp"` - `"creation_date"` - `"enabled"` - `"id"` - `"identifier"` - `"linked_rule_identifier"` - `"modification_date"` - `"name"` - `"origin"` - `"owner"` - `"type"` |
| **id**  integer | The sequence ID of the rule. |
| **name**  string | The name of the rule. |
| **owner**  string | Manage ownership of a QRadar Rule |
| **range**  string | Parameter to restrict the number of elements that are returned in the list to a specified range.  NOTE, this param is valid only via state GATHERED. |
| **state**  string | The state the configuration should be left in  The state *gathered* will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the *gathered* key within the result.  Choices:   - `"merged"` - `"gathered"` - `"deleted"` |

## [Examples](qradar_analytics_rules_module.md#id3)

```yaml+jinja
# Using MERGED state
# -------------------

- name: DISABLE Rule 'Ansible Example DDoS Rule'
  ibm.qradar.qradar_analytics_rules:
    config:
      name: 'Ansible Example DDOS Rule'
      enabled: false
    state: merged

# RUN output:
# -----------

#   qradar_analytics_rules:
#     after:
#       average_capacity: null
#       base_capacity: null
#       base_host_id: null
#       capacity_timestamp: null
#       creation_date: 1658929682568
#       enabled: false
#       id: 100443
#       identifier: ae5a1268-02a0-4976-84c5-dbcbcf854b9c
#       linked_rule_identifier: null
#       modification_date: 1658929682567
#       name: Ansible Example DDOS Rule
#       origin: USER
#       owner: admin
#       type: EVENT
#     before:
#       average_capacity: null
#       base_capacity: null
#       base_host_id: null
#       capacity_timestamp: null
#       creation_date: 1658929682568
#       enabled: true
#       id: 100443
#       identifier: ae5a1268-02a0-4976-84c5-dbcbcf854b9c
#       linked_rule_identifier: null
#       modification_date: 1658929682567
#       name: Ansible Example DDOS Rule
#       origin: USER
#       owner: admin
#       type: EVENT

# Using GATHERED state
# --------------------

- name:  Get information about the Rule named "Ansible Example DDOS Rule"
  ibm.qradar.qradar_analytics_rules:
    config:
      name: "Ansible Example DDOS Rule"
    state: gathered

# RUN output:
# -----------

#   gathered:
#     average_capacity: null
#     base_capacity: null
#     base_host_id: null
#     capacity_timestamp: null
#     creation_date: 1658918848694
#     enabled: true
#     id: 100443
#     identifier: d6d37942-ba28-438f-b909-120df643a992
#     linked_rule_identifier: null
#     modification_date: 1658918848692
#     name: Ansible Example DDOS Rule
#     origin: USER
#     owner: admin
#     type: EVENT

- name:  Get information about the Rule with ID 100443
  ibm.qradar.qradar_analytics_rules:
    config:
      id: 100443
    state: gathered

# RUN output:
# -----------

#   gathered:
#     average_capacity: null
#     base_capacity: null
#     base_host_id: null
#     capacity_timestamp: null
#     creation_date: 1658918848694
#     enabled: true
#     id: 100443
#     identifier: d6d37942-ba28-438f-b909-120df643a992
#     linked_rule_identifier: null
#     modification_date: 1658918848692
#     name: Ansible Example DDOS Rule
#     origin: USER
#     owner: admin
#     type: EVENT

- name: TO Get information about the Rule ID with a range
  ibm.qradar.qradar_analytics_rules:
  config:
    range: 100300-100500
    fields:
      - name
      - origin
      - owner
  state: gathered

# RUN output:
# -----------

# gathered:
#   - name: Devices with High Event Rates
#     origin: SYSTEM
#     owner: admin
#   - name: Excessive Database Connections
#     origin: SYSTEM
#     owner: admin
#   - name: 'Anomaly: Excessive Firewall Accepts Across Multiple Hosts'
#     origin: SYSTEM
#     owner: admin
#   - name: Excessive Firewall Denies from Single Source
#     origin: SYSTEM
#     owner: admin
#   - name: 'AssetExclusion: Exclude DNS Name By IP'
#     origin: SYSTEM
#     owner: admin
#   - name: 'AssetExclusion: Exclude DNS Name By MAC Address'
#     origin: SYSTEM
#     owner: admin

- name: Delete custom Rule by NAME
  ibm.qradar.qradar_analytics_rules:
    config:
      name: 'Ansible Example DDOS Rule'
    state: deleted

# RUN output:
# -----------

#   qradar_analytics_rules:
#     after: {}
#     before:
#       average_capacity: null
#       base_capacity: null
#       base_host_id: null
#       capacity_timestamp: null
#       creation_date: 1658929431239
#       enabled: true
#       id: 100444
#       identifier: 3c2cbd9d-d141-49fc-b5d5-29009a9b5308
#       linked_rule_identifier: null
#       modification_date: 1658929431238
#       name: Ansible Example DDOS Rule
#       origin: USER
#       owner: admin
#       type: EVENT

# Using DELETED state
# -------------------

- name: Delete custom Rule by ID
  ibm.qradar.qradar_analytics_rules:
    config:
      id: 100443
    state: deleted

# RUN output:
# -----------

#   qradar_analytics_rules:
#     after: {}
#     before:
#       average_capacity: null
#       base_capacity: null
#       base_host_id: null
#       capacity_timestamp: null
#       creation_date: 1658929431239
#       enabled: true
#       id: 100443
#       identifier: 3c2cbd9d-d141-49fc-b5d5-29009a9b5308
#       linked_rule_identifier: null
#       modification_date: 1658929431238
#       name: Ansible Example DDOS Rule
#       origin: USER
#       owner: admin
#       type: EVENT
```

## [Return Values](qradar_analytics_rules_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  Returned: when changed  Sample: `"The configuration returned will always be in the same format of the parameters above."` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format of the parameters above."` |

### Authors

- Ansible Security Automation Team (@justjais) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
