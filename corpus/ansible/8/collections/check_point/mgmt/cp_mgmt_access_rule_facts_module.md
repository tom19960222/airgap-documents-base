---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_access_rule_facts module – Get access-rule objects facts on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_access_rule_facts_module.html
fetched_at: 2026-07-28T01:15:39+00:00
---
# check_point.mgmt.cp_mgmt_access_rule_facts module – Get access-rule objects facts on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_access_rule_facts`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_access_rule_facts_module.md#synopsis)
- [Parameters](cp_mgmt_access_rule_facts_module.md#parameters)
- [Examples](cp_mgmt_access_rule_facts_module.md#examples)

## [Synopsis](cp_mgmt_access_rule_facts_module.md#id1)

- Get access-rule objects facts on Check Point devices.
- All operations are performed over Web Services API.
- This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter ‘name’.

## [Parameters](cp_mgmt_access_rule_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dereference_group_members**  boolean | Indicates whether to dereference “members” field by details level for every object in reply.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **filter**  string | Search expression to filter the rulebase. The provided text should be exactly the same as it would be given in Smart Console. The logical operators in the expression (‘AND’, ‘OR’) should be provided in capital letters. If an operator is not used, the default OR operator applies. |
| **filter_settings**  dictionary | Sets filter preferences. |
| **packet_search_settings**  dictionary | When ‘search-mode’ is set to ‘packet’, this object allows to set the packet search preferences. |
| **expand_group_members**  boolean | When true, if the search expression contains a UID or a name of a group object, results will include rules that match on at least one member of the group.  **Choices:**   - `false` - `true` |
| **expand_group_with_exclusion_members**  boolean | When true, if the search expression contains a UID or a name of a group-with-exclusion object, results will include rules that match at least one member of the “include” part and is not a member of the “except” part.  **Choices:**   - `false` - `true` |
| **match_on_any**  boolean | Whether to match on ‘Any’ object.  **Choices:**   - `false` - `true` |
| **match_on_group_with_exclusion**  boolean | Whether to match on a group-with-exclusion.  **Choices:**   - `false` - `true` |
| **match_on_negate**  boolean | Whether to match on a negated cell.  **Choices:**   - `false` - `true` |
| **search_mode**  string | When set to ‘general’, both the Full Text Search and Packet Search are enabled. In this mode, Packet Search will not match on ‘Any’ object, a negated cell or a group-with-exclusion. When the search-mode is set to ‘packet’, by default, the match on ‘Any’ object, a negated cell or a group-with-exclusion are enabled. packet-search-settings may be provided to change the default behavior.  **Choices:**   - `"general"` - `"packet"` |
| **hits_settings**  dictionary | N/A |
| **from_date**  string | Format, ‘YYYY-MM-DD’, ‘YYYY-mm-ddThh:mm:ss’. |
| **target**  string | Target gateway name or UID. |
| **to_date**  string | Format, ‘YYYY-MM-DD’, ‘YYYY-mm-ddThh:mm:ss’. |
| **layer**  string | Layer that the rule belongs to identified by the name or UID. |
| **limit**  integer | No more than that many results will be returned. This parameter is relevant only for getting few objects. |
| **name**  string | Object name. Should be unique in the domain. |
| **offset**  integer | Skip that many results before beginning to return them. This parameter is relevant only for getting few objects. |
| **order**  list / elements=dictionary | Sorts results by the given field. By default the results are sorted in the ascending order by name. This parameter is relevant only for getting few objects. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **package**  string | Name of the package. |
| **show_as_ranges**  boolean | When true, the source, destination and services & applications parameters are displayed as ranges of IP addresses and port numbers rather than network objects.<br /> Objects that are not represented using IP addresses or port numbers are presented as objects.<br /> In addition, the response of each rule does not contain the parameters, source, source-negate, destination, destination-negate, service and service-negate, but instead it contains the parameters, source-ranges, destination-ranges and service-ranges.<br /><br /> Note, Requesting to show rules as ranges is limited up to 20 rules per request, otherwise an error is returned. If you wish to request more rules, use the offset and limit parameters to limit your request.  **Choices:**   - `false` - `true` |
| **show_hits**  boolean | N/A  **Choices:**   - `false` - `true` |
| **show_membership**  boolean | Indicates whether to calculate and show “groups” field for every object in reply.  **Choices:**   - `false` - `true` |
| **use_object_dictionary**  boolean | N/A  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |

## [Examples](cp_mgmt_access_rule_facts_module.md#id3)

```yaml+jinja
- name: show-access-rule
  cp_mgmt_access_rule_facts:
    layer: Network
    name: Rule 1

- name: show-access-rulebase
  cp_mgmt_access_rule_facts:
    details_level: standard
    limit: 20
    name: Network
    offset: 0
    use_object_dictionary: true
```

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
