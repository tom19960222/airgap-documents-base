---
collection: ansible
version: "8"
title: "community.skydive.skydive_capture module – Module which manages flow capture on interfaces"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/skydive/skydive_capture_module.html
fetched_at: 2026-07-28T01:59:20+00:00
---
# community.skydive.skydive_capture module – Module which manages flow capture on interfaces

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
> see [Requirements](skydive_capture_module.md#ansible-collections-community-skydive-skydive-capture-module-requirements) for details.
>
> To use it in a playbook, specify: `community.skydive.skydive_capture`.

- [Synopsis](skydive_capture_module.md#synopsis)
- [Requirements](skydive_capture_module.md#requirements)
- [Parameters](skydive_capture_module.md#parameters)
- [Notes](skydive_capture_module.md#notes)
- [Examples](skydive_capture_module.md#examples)

## [Synopsis](skydive_capture_module.md#id1)

- This module manages flow capture on interfaces. The Gremlin expression is continuously evaluated which means that it is possible to define a capture on nodes that do not exist yet.
- It is useful when you want to start a capture on all OpenvSwitch whatever the number of Skydive agents you will start.
- While starting the capture, user can specify the capture name, capture description and capture type optionally.

## [Requirements](skydive_capture_module.md#id2)

The below requirements are needed on the host that executes this module.

- skydive-client

## [Parameters](skydive_capture_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **capture_name**  string | To define flow capture name.  **Default:** `""` |
| **description**  string | Configures a text string to be associated with the instance of this object.  **Default:** `""` |
| **extra_tcp_metric**  boolean | To define flow capture ExtraTCPMetric.  **Choices:**   - `false` ← (default) - `true` |
| **interface_name**  string | To define flow capture interface name. |
| **ip_defrag**  boolean | To define flow capture IPDefrag.  **Choices:**   - `false` ← (default) - `true` |
| **layer_key_mode**  string | To define flow capture Layer KeyMode.  **Default:** `"L2"` |
| **provider**  string | A dict object containing connection details. |
| **endpoint**  string / required | Specifies the hostname/address along with the port as `localhost:8082`for connecting to the remote instance of SKYDIVE client over the REST API. |
| **insecure**  boolean | Ignore SSL certification verification.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **ssl**  boolean | Specifies the ssl parameter that decides if the connection type shall be http or https.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string | Configures the username to use to authenticate the connection to the remote instance of SKYDIVE client. |
| **query**  string | It’s the complete gremlin query which the users can input, *G.V(*.Has(‘Name’, ‘eth0’, ‘Type’, ‘device’)), to create the capture. And, if the user directly inputs the gremlin query then user is not required to input any other module parameter as gremlin query takes care of creating the flow capture. |
| **reassemble_tcp**  boolean | To define flow capture ReassembleTCP.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the flow capture. If value is *present* flow capture will be created else if it is *absent* it will be deleted.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | To define flow capture interface type. |

## [Notes](skydive_capture_module.md#id4)

> **Note:**
>
> - This module must be run locally, which can be achieved by specifying `connection: local`.

## [Examples](skydive_capture_module.md#id5)

```yaml+jinja
- name: start a new flow capture directly from gremlin query
  community.skydive.skydive_capture:
    query: G.V().Has('Name', 'eth0', 'Type', 'device')
    state: present
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: stop the flow capture directly from gremlin query
  community.skydive.skydive_capture:
    query: G.V().Has('Name', 'eth0', 'Type', 'device')
    state: absent
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: start a new flow capture from user's input
  community.skydive.skydive_capture:
    interface_name: Node1
    type: myhost
    capture_name: test_capture
    description: test description
    extra_tcp_metric: true
    ip_defrag: true
    reassemble_tcp: true
    state: present
    provider:
      endpoint: localhost:8082
      username: admin
      password: admin

- name: stop the flow capture
  community.skydive.skydive_capture:
    interface_name: Node1
    type: myhost
    capture_name: test_capture
    description: test description
    extra_tcp_metric: true
    ip_defrag: true
    reassemble_tcp: true
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
