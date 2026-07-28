---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_simple_gateway_facts module – Get simple-gateway objects facts on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_simple_gateway_facts_module.html
fetched_at: 2026-07-28T01:17:58+00:00
---
# check_point.mgmt.cp_mgmt_simple_gateway_facts module – Get simple-gateway objects facts on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_simple_gateway_facts`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_simple_gateway_facts_module.md#synopsis)
- [Parameters](cp_mgmt_simple_gateway_facts_module.md#parameters)
- [Examples](cp_mgmt_simple_gateway_facts_module.md#examples)

## [Synopsis](cp_mgmt_simple_gateway_facts_module.md#id1)

- Get simple-gateway objects facts on Check Point devices.
- All operations are performed over Web Services API.
- This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter ‘name’.

## [Parameters](cp_mgmt_simple_gateway_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **limit**  integer | No more than that many results will be returned. This parameter is relevant only for getting few objects. |
| **name**  string | Object name. This parameter is relevant only for getting a specific object. |
| **offset**  integer | Skip that many results before beginning to return them. This parameter is relevant only for getting few objects. |
| **order**  list / elements=dictionary | Sorts results by the given field. By default the results are sorted in the ascending order by name. This parameter is relevant only for getting few objects. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **show_membership**  boolean | Indicates whether to calculate and show “groups” field for every object in reply.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |

## [Examples](cp_mgmt_simple_gateway_facts_module.md#id3)

```yaml+jinja
- name: show-simple-gateway
  cp_mgmt_simple_gateway_facts:
    name: gw1

- name: show-simple-gateways
  cp_mgmt_simple_gateway_facts:
    details_level: standard
    limit: 50
    offset: 0
```

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
