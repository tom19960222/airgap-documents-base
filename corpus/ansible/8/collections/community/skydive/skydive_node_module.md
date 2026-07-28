---
collection: ansible
version: "8"
title: "community.skydive.skydive_node module – Module which add nodes to Skydive topology"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/skydive/skydive_node_module.html
fetched_at: 2026-07-28T01:59:21+00:00
---
# community.skydive.skydive_node module – Module which add nodes to Skydive topology

> **Note:**
>
> This module is part of the [community.skydive collection](https://galaxy.ansible.com/ui/repo/published/community/skydive/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.skydive`.
> You need further requirements to be able to use this module,
> see [Requirements](skydive_node_module.md#ansible-collections-community-skydive-skydive-node-module-requirements) for details.
>
> To use it in a playbook, specify: `community.skydive.skydive_node`.

- [Synopsis](skydive_node_module.md#synopsis)
- [Requirements](skydive_node_module.md#requirements)
- [Parameters](skydive_node_module.md#parameters)
- [Notes](skydive_node_module.md#notes)
- [Examples](skydive_node_module.md#examples)

## [Synopsis](skydive_node_module.md#id1)

- This module handles adding node to the Skydive topology.

## [Requirements](skydive_node_module.md#id2)

The below requirements are needed on the host that executes this module.

- skydive-client

## [Parameters](skydive_node_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | To define host for the node. |
| **metadata**  string | To define metadata for the node. |
| **name**  string / required | To define name for the node. |
| **node_type**  string / required | To define type for the node. |
| **provider**  string | A dict object containing connection details. |
| **endpoint**  string / required | Specifies the hostname/address along with the port as `localhost:8082`for connecting to the remote instance of SKYDIVE client over the REST API. |
| **insecure**  boolean | Ignore SSL certification verification.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **ssl**  boolean | Specifies the ssl parameter that decides if the connection type shall be http or https.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string | Configures the username to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **seed**  string | used to generate the UUID of the node  **Default:** `""` |
| **state**  string | State of the Skydive Node. If value is *present* new node will be created else if it is *absent* it will be deleted.  **Choices:**   - `"present"` ← (default) - `"update"` - `"absent"` |

## [Notes](skydive_node_module.md#id4)

> **Note:**
>
> - This module must be run locally, which can be achieved by specifying `connection: local`.

## [Examples](skydive_node_module.md#id5)

```yaml+jinja
- name: create tor node
  community.skydive.skydive_node:
    name: TOR
    node_type: fabric
    seed: TOR1
    metadata:
      Model: Cisco 5300
    state: present
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: update tor node
  community.skydive.skydive_node:
    name: TOR
    node_type: host
    seed: TOR1
    metadata:
      Model: Cisco 3400
    state: update
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: Delete the tor node
  community.skydive.skydive_node:
    name: TOR
    node_type: host
    seed: TOR1
    metadata:
      Model: Cisco 3400
    state: absent
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin
```

### Authors

- Sumit Jaiswal (@sjaiswal)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/skydive/issues)
- [Repository (Sources)](https://github.com/ansible-collections/skydive)
