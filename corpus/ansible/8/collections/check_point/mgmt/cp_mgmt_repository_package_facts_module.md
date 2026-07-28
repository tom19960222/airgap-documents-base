---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_repository_package_facts module – Get repository-package objects facts on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_repository_package_facts_module.html
fetched_at: 2026-07-28T01:17:03+00:00
---
# check_point.mgmt.cp_mgmt_repository_package_facts module – Get repository-package objects facts on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_repository_package_facts`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_repository_package_facts_module.md#synopsis)
- [Parameters](cp_mgmt_repository_package_facts_module.md#parameters)
- [Examples](cp_mgmt_repository_package_facts_module.md#examples)

## [Synopsis](cp_mgmt_repository_package_facts_module.md#id1)

- Get repository-package objects facts on Checkpoint devices.
- All operations are performed over Web Services API.
- This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter ‘name’.

## [Parameters](cp_mgmt_repository_package_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **limit**  integer | The maximal number of returned results. This parameter is relevant only for getting few objects. |
| **name**  string | Object name. This parameter is relevant only for getting a specific object. |
| **offset**  integer | Number of the results to initially skip. This parameter is relevant only for getting few objects. |
| **order**  list / elements=dictionary | Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order. This parameter is relevant only for getting few objects. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |

## [Examples](cp_mgmt_repository_package_facts_module.md#id3)

```yaml+jinja
- name: show-repository-package
  cp_mgmt_repository_package_facts:
    name: Check_Point_R80_20_JUMBO_HF_Bundle_T118_sk137592_Security_Gateway_and_Standalone_2_6_18_FULL.tgz

- name: show-repository-packages
  cp_mgmt_repository_package_facts:
    details_level: standard
    limit: 4
    offset: 0
```

### Authors

- Shiran Golzar (@chkp-shirango)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
