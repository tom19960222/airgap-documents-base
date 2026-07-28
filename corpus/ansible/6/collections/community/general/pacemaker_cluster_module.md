---
collection: ansible
version: "6"
title: "community.general.pacemaker_cluster module – Manage pacemaker clusters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pacemaker_cluster_module.html
fetched_at: 2026-07-27T17:11:39+00:00
---
# community.general.pacemaker_cluster module – Manage pacemaker clusters

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.pacemaker_cluster`.

- [Synopsis](pacemaker_cluster_module.md#synopsis)
- [Parameters](pacemaker_cluster_module.md#parameters)
- [Examples](pacemaker_cluster_module.md#examples)
- [Return Values](pacemaker_cluster_module.md#return-values)

## [Synopsis](pacemaker_cluster_module.md#id1)

- This module can manage a pacemaker cluster and nodes from Ansible using the pacemaker cli.

## [Parameters](pacemaker_cluster_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Force the change of the cluster state  Choices:   - `false` - `true` ← (default) |
| **node**  string | Specify which node of the cluster you want to manage. None == the cluster status itself, ‘all’ == check the status of all nodes. |
| **state**  string | Indicate desired state of the cluster  Choices:   - `"cleanup"` - `"offline"` - `"online"` - `"restart"` |
| **timeout**  integer | Timeout when the module should considered that the action has failed  Default: `300` |

## [Examples](pacemaker_cluster_module.md#id3)

```yaml+jinja
---
- name: Set cluster Online
  hosts: localhost
  gather_facts: false
  tasks:
  - name: Get cluster state
    community.general.pacemaker_cluster:
      state: online
```

## [Return Values](pacemaker_cluster_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | true if the cluster state has changed  Returned: always |
| **out**  string | The output of the current state of the cluster. It return a list of the nodes state.  Returned: always  Sample: `"out: [[\"  overcloud-controller-0\", \" Online\"]]}"` |
| **rc**  boolean | exit code of the module  Returned: always |

### Authors

- Mathieu Bultel (@matbu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
