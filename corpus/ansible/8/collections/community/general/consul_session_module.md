---
collection: ansible
version: "8"
title: "community.general.consul_session module – Manipulate consul sessions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/consul_session_module.html
fetched_at: 2026-07-28T01:45:14+00:00
---
# community.general.consul_session module – Manipulate consul sessions

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](consul_session_module.md#ansible-collections-community-general-consul-session-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.consul_session`.

- [Synopsis](consul_session_module.md#synopsis)
- [Requirements](consul_session_module.md#requirements)
- [Parameters](consul_session_module.md#parameters)
- [Attributes](consul_session_module.md#attributes)
- [Examples](consul_session_module.md#examples)

## [Synopsis](consul_session_module.md#id1)

- Allows the addition, modification and deletion of sessions in a consul cluster. These sessions can then be used in conjunction with key value pairs to implement distributed locks. In depth documentation for working with sessions can be found at <http://www.consul.io/docs/internals/sessions.html>

Aliases: clustering.consul.consul_session

## [Requirements](consul_session_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](consul_session_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **behavior**  string | The optional behavior that can be attached to the session when it is created. This controls the behavior when a session is invalidated.  **Choices:**   - `"delete"` - `"release"` ← (default) |
| **checks**  list / elements=string | Checks that will be used to verify the session health. If all the checks fail, the session will be invalidated and any locks associated with the session will be release and can be acquired once the associated lock delay has expired. |
| **datacenter**  string | The name of the datacenter in which the session exists or should be created. |
| **delay**  integer | The optional lock delay that can be attached to the session when it is created. Locks for invalidated sessions ar blocked from being acquired until this delay has expired. Durations are in seconds.  **Default:** `15` |
| **host**  string | The host of the consul agent defaults to localhost.  **Default:** `"localhost"` |
| **id**  string | ID of the session, required when `state` is either `info` or `remove`. |
| **name**  string | The name that should be associated with the session. Required when `state=node` is used. |
| **node**  string | The name of the node that with which the session will be associated. by default this is the name of the agent. |
| **port**  integer | The port on which the consul agent is running.  **Default:** `8500` |
| **scheme**  string | The protocol scheme on which the consul agent is running.  **Default:** `"http"` |
| **state**  string | Whether the session should be present i.e. created if it doesn’t exist, or absent, removed if present. If created, the `id` for the session is returned in the output. If `absent`, `id` is required to remove the session. Info for a single session, all the sessions for a node or all available sessions can be retrieved by specifying `info`, `node` or `list` for the `state`; for `node` or `info`, the node `name` or session `id` is required as parameter.  **Choices:**   - `"absent"` - `"info"` - `"list"` - `"node"` - `"present"` ← (default) |
| **token**  string  *added in community.general 5.6.0* | The token key identifying an ACL rule set that controls access to the key value pair. |
| **ttl**  integer  *added in community.general 5.4.0* | Specifies the duration of a session in seconds (between 10 and 86400). |
| **validate_certs**  boolean | Whether to verify the TLS certificate of the consul agent.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](consul_session_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](consul_session_module.md#id5)

```yaml+jinja
- name: Register basic session with consul
  community.general.consul_session:
    name: session1

- name: Register a session with an existing check
  community.general.consul_session:
    name: session_with_check
    checks:
      - existing_check_name

- name: Register a session with lock_delay
  community.general.consul_session:
    name: session_with_delay
    delay: 20s

- name: Retrieve info about session by id
  community.general.consul_session:
    id: session_id
    state: info

- name: Retrieve active sessions
  community.general.consul_session:
    state: list

- name: Register session with a ttl
  community.general.consul_session:
    name: session-with-ttl
    ttl: 600  # sec
```

### Authors

- Steve Gargan (@sgargan)
- Håkon Lerring (@Hakon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
