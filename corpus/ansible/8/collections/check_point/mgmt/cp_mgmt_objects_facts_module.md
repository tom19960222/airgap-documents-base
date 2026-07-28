---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_objects_facts module – Get objects objects facts on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_objects_facts_module.html
fetched_at: 2026-07-28T01:16:56+00:00
---
# check_point.mgmt.cp_mgmt_objects_facts module – Get objects objects facts on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_objects_facts`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_objects_facts_module.md#synopsis)
- [Parameters](cp_mgmt_objects_facts_module.md#parameters)
- [Examples](cp_mgmt_objects_facts_module.md#examples)

## [Synopsis](cp_mgmt_objects_facts_module.md#id1)

- Get objects facts on Checkpoint devices.
- All operations are performed over Web Services API.
- This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter ‘name’.

## [Parameters](cp_mgmt_objects_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dereference_group_members**  boolean | Indicates whether to dereference “members” field by details level for every object in reply.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **filter**  string | Search expression to filter objects by. The provided text should be exactly the same as it would be given in Smart Console. The logical operators in the expression (‘AND’, ‘OR’) should be provided in capital letters. By default, the search involves both a textual search and a IP search. To use IP search only, set the “ip-only” parameter to true. |
| **ip_only**  boolean | If using “filter”, use this field to search objects by their IP address only, without involving the textual search.<br><br>IP search use cases<br>&nbsp;&nbsp;&nbsp;&nbsp; <ul><li>Full IPv4 address matches for,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Check Point Hosts and Gateways with exact IPv4 match or with interfaces which subnet contains the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - IPv4 Networks and IPv4 Address Ranges that contain the search address</li> <br>&nbsp;&nbsp;&nbsp;&nbsp; <li>Partial IPv4 address matches for,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Networks, Check Point Hosts and Gateways with IPv4 address that starts from the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Check Point Hosts and Gateways with interfaces which subnet address starts from the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - IPv4 Address Ranges with first address or last address that starts from the search address<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - IPv4 Networks and IPv4 Address Ranges that contain the network derived from the search address supplemented with missing octets (all zeroes)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Hosts, Check Point Hosts and Gateways with interfaces which subnet contains the network derived from the search address supplemented with missing octets (all zeroes)</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li>IPv6 address,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Not supported</li></ul><br><br> \* Check Point Host is a server of type Network Policy Management, Logging & Status, SmartEvent, etc.<br> \* When one IP address is checked to start from another (partial) IP address - only full octets are considered <br> \* Check Examples part for IP search examples.  **Choices:**   - `false` - `true` |
| **limit**  integer | The maximal number of returned results. This parameter is relevant only for getting a specific object. |
| **offset**  integer | Number of the results to initially skip. This parameter is relevant only for getting a specific object. |
| **order**  list / elements=dictionary | Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order. This parameter is relevant only for getting a specific object. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **show_membership**  boolean | Indicates whether to calculate and show “groups” field for every object in reply.  **Choices:**   - `false` - `true` |
| **type**  string | The objects’ type, e.g., host, service-tcp, network, address-range… |
| **uid**  string | Object unique identifier. |
| **uids**  list / elements=string | List of UIDs of the objects to retrieve. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |

## [Examples](cp_mgmt_objects_facts_module.md#id3)

```yaml+jinja
- name: show-objects
  cp_mgmt_objects_facts:
    limit: 50
    offset: 0
    order:
    - ASC: name
    type: group

- name: show-object
  cp_mgmt_objects_facts:
    uid: ef82887c-d08f-49a3-a18f-a376be633848
```

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
