---
collection: ansible
version: "6"
title: "community.network.pn_access_list_ip module – CLI command to add/remove access-list-ip"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_access_list_ip_module.html
fetched_at: 2026-07-27T17:19:15+00:00
---
# community.network.pn_access_list_ip module – CLI command to add/remove access-list-ip

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_access_list_ip`.

- [Synopsis](pn_access_list_ip_module.md#synopsis)
- [Parameters](pn_access_list_ip_module.md#parameters)
- [Examples](pn_access_list_ip_module.md#examples)
- [Return Values](pn_access_list_ip_module.md#return-values)

## [Synopsis](pn_access_list_ip_module.md#id1)

- This modules can be used to add and remove IPs associated with access list.

## [Parameters](pn_access_list_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_ip**  string | IP associated with the access list.  Default: `"::"` |
| **pn_name**  string | Access List Name. |
| **state**  string / required | State the action to perform. Use ‘present’ to add access-list-ip and ‘absent’ to remove access-list-ip.  Choices:   - `"present"` - `"absent"` |

## [Examples](pn_access_list_ip_module.md#id3)

```yaml+jinja
- name: Access list ip functionality
  community.network.pn_access_list_ip:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_ip: "172.16.3.1"
    state: "present"

- name: Access list ip functionality
  community.network.pn_access_list_ip:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_ip: "172.16.3.1"
    state: "absent"
```

## [Return Values](pn_access_list_ip_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the access-list-ip command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the access-list-ip command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
