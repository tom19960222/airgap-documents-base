---
collection: ansible
version: "8"
title: "gluster.gluster.gluster_heal_info module – Gather information on self-heal or rebalance status"
source_url: https://docs.ansible.com/projects/ansible/8/collections/gluster/gluster/gluster_heal_info_module.html
fetched_at: 2026-07-28T02:31:38+00:00
---
# gluster.gluster.gluster_heal_info module – Gather information on self-heal or rebalance status

> **Note:**
>
> This module is part of the [gluster.gluster collection](https://galaxy.ansible.com/ui/repo/published/gluster/gluster/) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install gluster.gluster`.
> You need further requirements to be able to use this module,
> see [Requirements](gluster_heal_info_module.md#ansible-collections-gluster-gluster-gluster-heal-info-module-requirements) for details.
>
> To use it in a playbook, specify: `gluster.gluster.gluster_heal_info`.

- [Synopsis](gluster_heal_info_module.md#synopsis)
- [Requirements](gluster_heal_info_module.md#requirements)
- [Parameters](gluster_heal_info_module.md#parameters)
- [Examples](gluster_heal_info_module.md#examples)
- [Return Values](gluster_heal_info_module.md#return-values)

## [Synopsis](gluster_heal_info_module.md#id1)

- Gather facts about either self-heal or rebalance status.
- This module was called `gluster_heal_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [gluster.gluster.gluster_heal_info](gluster_heal_info_module.md#ansible-collections-gluster-gluster-gluster-heal-info-module) module no longer returns `ansible_facts`!

## [Requirements](gluster_heal_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- GlusterFS > 3.2

## [Parameters](gluster_heal_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: volume  string / required | The volume name. |
| **status_filter**  string | Determines which facts are to be returned.  If the `status_filter` is `self-heal`, status of self-heal, along with the number of files still in process are returned.  If the `status_filter` is `rebalance`, rebalance status is returned.  **Choices:**   - `"self-heal"` ← (default) - `"rebalance"` |

## [Examples](gluster_heal_info_module.md#id4)

```yaml+jinja
- name: Gather self-heal facts about all gluster hosts in the cluster
  gluster.gluster.gluster_heal_info:
    name: test_volume
    status_filter: self-heal
  register: self_heal_status
- debug:
    var: self_heal_status

- name: Gather rebalance facts about all gluster hosts in the cluster
  gluster.gluster.gluster_heal_info:
    name: test_volume
    status_filter: rebalance
  register: rebalance_status
- debug:
    var: rebalance_status
```

## [Return Values](gluster_heal_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **heal_info**  list / elements=string | List of files that still need healing process  **Returned:** On success |
| **name**  string | GlusterFS volume name  **Returned:** always |
| **rebalance_status**  list / elements=string | Status of rebalance operation  **Returned:** On success |
| **status_filter**  string | Whether self-heal or rebalance status is to be returned  **Returned:** always |

### Authors

- Devyani Kota (@devyanikota)

### Collection links

- [Issue Tracker](https://github.com/gluster/gluster-ansible-collection/issues)
- [Repository (Sources)](https://github.com/gluster/gluster-ansible-collection)
