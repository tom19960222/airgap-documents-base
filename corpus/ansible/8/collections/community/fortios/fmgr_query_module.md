---
collection: ansible
version: "8"
title: "community.fortios.fmgr_query module – Query FortiManager data objects for use in Ansible workflows."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_query_module.html
fetched_at: 2026-07-28T01:44:16+00:00
---
# community.fortios.fmgr_query module – Query FortiManager data objects for use in Ansible workflows.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_query`.

- [Synopsis](fmgr_query_module.md#synopsis)
- [Parameters](fmgr_query_module.md#parameters)
- [Notes](fmgr_query_module.md#notes)
- [Examples](fmgr_query_module.md#examples)
- [Return Values](fmgr_query_module.md#return-values)

## [Synopsis](fmgr_query_module.md#id1)

- Provides information on data objects within FortiManager so that playbooks can perform conditionals.

## [Parameters](fmgr_query_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **custom_dict**  string | ADVANCED USERS ONLY! REQUIRES KNOWLEDGE OF FMGR JSON API!  DICTIONARY JSON FORMAT ONLY – Custom dictionary/datagram to send to the endpoint. |
| **custom_endpoint**  string | ADVANCED USERS ONLY! REQUIRES KNOWLEDGE OF FMGR JSON API!  The HTTP Endpoint on FortiManager you wish to GET from. |
| **device_ip**  string | The IP of the device you want to query. |
| **device_serial**  string | The serial number of the device you want to query. |
| **device_unique_name**  string | The desired “friendly” name of the device you want to query. |
| **nodes**  string | A LIST of firewalls in the cluster you want to verify i.e. [“firewall_A”,”firewall_B”]. |
| **object**  string / required | The data object we wish to query (device, package, rule, etc). Will expand choices as improves.  **Choices:**   - `"device"` - `"cluster_nodes"` - `"task"` - `"custom"` |
| **task_id**  string | The ID of the task you wish to query status on. If left blank and object = ‘task’ a list of tasks are returned. |

## [Notes](fmgr_query_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_query_module.md#id4)

```yaml+jinja
- name: QUERY FORTIGATE DEVICE BY IP
  community.fortios.fmgr_query:
    object: "device"
    adom: "ansible"
    device_ip: "10.7.220.41"

- name: QUERY FORTIGATE DEVICE BY SERIAL
  community.fortios.fmgr_query:
    adom: "ansible"
    object: "device"
    device_serial: "FGVM000000117992"

- name: QUERY FORTIGATE DEVICE BY FRIENDLY NAME
  community.fortios.fmgr_query:
    adom: "ansible"
    object: "device"
    device_unique_name: "ansible-fgt01"

- name: VERIFY CLUSTER MEMBERS AND STATUS
  community.fortios.fmgr_query:
    adom: "ansible"
    object: "cluster_nodes"
    device_unique_name: "fgt-cluster01"
    nodes: ["ansible-fgt01", "ansible-fgt02", "ansible-fgt03"]

- name: GET STATUS OF TASK ID
  community.fortios.fmgr_query:
    adom: "ansible"
    object: "task"
    task_id: "3"

- name: USE CUSTOM TYPE TO QUERY AVAILABLE SCRIPTS
  community.fortios.fmgr_query:
    adom: "ansible"
    object: "custom"
    custom_endpoint: "/dvmdb/adom/ansible/script"
    custom_dict: { "type": "cli" }
```

## [Return Values](fmgr_query_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
