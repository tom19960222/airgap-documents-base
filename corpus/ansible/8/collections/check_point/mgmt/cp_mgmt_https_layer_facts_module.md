---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_https_layer_facts module – Get https-layer objects facts on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_https_layer_facts_module.html
fetched_at: 2026-07-28T01:16:28+00:00
---
# check_point.mgmt.cp_mgmt_https_layer_facts module – Get https-layer objects facts on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_https_layer_facts`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_https_layer_facts_module.md#synopsis)
- [Parameters](cp_mgmt_https_layer_facts_module.md#parameters)
- [Examples](cp_mgmt_https_layer_facts_module.md#examples)

## [Synopsis](cp_mgmt_https_layer_facts_module.md#id1)

- Get https-layer objects facts on Checkpoint devices.
- All operations are performed over Web Services API.
- This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter ‘name’.

## [Parameters](cp_mgmt_https_layer_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **filter**  string | Search expression to filter objects by. The provided text should be exactly the same as it would be given in SmartConsole Object Explorer. The logical operators in the expression (‘AND’, ‘OR’) should be provided in capital letters. The search involves both a IP search and a textual search in name, comment, tags etc. |
| **limit**  integer | The maximal number of returned results. This parameter is relevant only for getting few objects. |
| **name**  string | Object name. This parameter is relevant only for getting a specific object. |
| **offset**  integer | Number of the results to initially skip. This parameter is relevant only for getting few objects. |
| **order**  list / elements=dictionary | Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order. This parameter is relevant only for getting few objects. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |

## [Examples](cp_mgmt_https_layer_facts_module.md#id3)

```yaml+jinja
- name: show-https-layer
  cp_mgmt_https_layer_facts:
    name: New Layer 1

- name: show-https-layers
  cp_mgmt_https_layer_facts:
    details_level: standard
    limit: 50
    offset: 0
```

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
