---
collection: ansible
version: "6"
title: "community.skydive.skydive_edge module – Module to add edges to Skydive topology"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/skydive/skydive_edge_module.html
fetched_at: 2026-07-27T17:21:08+00:00
---
# community.skydive.skydive_edge module – Module to add edges to Skydive topology

> **Note:**
>
> This module is part of the [community.skydive collection](https://galaxy.ansible.com/community/skydive) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.skydive`.
> You need further requirements to be able to use this module,
> see [Requirements](skydive_edge_module.md#ansible-collections-community-skydive-skydive-edge-module-requirements) for details.
>
> To use it in a playbook, specify: `community.skydive.skydive_edge`.

- [Synopsis](skydive_edge_module.md#synopsis)
- [Requirements](skydive_edge_module.md#requirements)
- [Parameters](skydive_edge_module.md#parameters)
- [Notes](skydive_edge_module.md#notes)
- [Examples](skydive_edge_module.md#examples)

## [Synopsis](skydive_edge_module.md#id1)

- This module handles setting up edges between two nodes based on the relationship type to the Skydive topology.

## [Requirements](skydive_edge_module.md#id2)

The below requirements are needed on the host that executes this module.

- skydive-client

## [Parameters](skydive_edge_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **child_node**  string / required | To defined the second node of the link, it can be either an ID or a gremlin expression |
| **host**  string | To define the host of the node.  Default: `""` |
| **metadata**  string | To define metadata for the edge. |
| **parent_node**  string / required | To defined the first node of the link, it can be either an ID or a gremlin expression |
| **provider**  string | A dict object containing connection details. |
| **endpoint**  string / required | Specifies the hostname/address along with the port as `localhost:8082`for connecting to the remote instance of SKYDIVE client over the REST API. |
| **insecure**  boolean | Ignore SSL certification verification.  Choices:   - `false` ← (default) - `true` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **ssl**  boolean | Specifies the ssl parameter that decides if the connection type shall be http or https.  Choices:   - `false` ← (default) - `true` |
| **user**  string | Configures the username to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **relation_type**  string / required | To define relation type of the node *ownership, layer2, layer3*. |
| **state**  string | State of the Skydive Edge. If value is *present* new edge will be created else if it is *absent* it will be deleted.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](skydive_edge_module.md#id4)

> **Note:**
>
> - This module must be run locally, which can be achieved by specifying `connection: local`.

## [Examples](skydive_edge_module.md#id5)

```yaml+jinja
- name: create tor
  community.skydive.skydive_node:
    name: 'TOR'
    node_type: "fabric"
    seed: TOR
    metadata:
      Model: Cisco xxxx
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin
  register: tor_result

- name: create port 1
  community.skydive.skydive_node:
    name: 'PORT1'
    node_type: 'fabric'
    seed: PORT1
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin
  register: port1_result

- name: create port 2
  community.skydive.skydive_node:
    name: 'PORT2'
    node_type: 'fabric'
    seed: PORT2
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin
  register: port2_result

- name: link node tor and port 1
  community.skydive.skydive_edge:
    parent_node: "{{ tor_result.UUID }}"
    child_node: "{{ port1_result.UUID }}"
    relation_type: ownership
    state: present
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: link node tor and port 2
  community.skydive.skydive_edge:
    parent_node: "{{ tor_result.UUID }}"
    child_node: "{{ port2_result.UUID }}"
    relation_type: ownership
    state: present
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: update link node tor and port 1 relation
  community.skydive.skydive_edge:
    parent_node: "{{ tor_result.UUID }}"
    child_node: "{{ port2_result.UUID }}"
    relation_type: layer2
    state: upadte
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: Unlink tor and port 2
  community.skydive.skydive_edge:
    parent_node: "{{ tor_result.UUID }}"
    child_node: "{{ port2_result.UUID }}"
    relation_type: ownership
    state: absent
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: link tor and port 2 via Gremlin expression
  community.skydive.skydive_edge:
    parent_node: G.V().Has('Name', 'TOR')
    child_node: G.V().Has('Name', 'PORT2')
    relation_type: ownership
    state: present
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: Unlink tor and port 2 via Gremlin expression
  community.skydive.skydive_edge:
    parent_node: G.V().Has('Name', 'TOR')
    child_node: G.V().Has('Name', 'PORT2')
    relation_type: ownership
    state: absent
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin
```

### Authors

- Sumit Jaiswal (@sjaiswal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/skydive/issues)
[Repository (Sources)](https://github.com/ansible-collections/skydive)
