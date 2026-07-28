---
collection: ansible
version: "8"
title: "community.general.riak module – This module handles some common Riak operations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/riak_module.html
fetched_at: 2026-07-28T01:50:00+00:00
---
# community.general.riak module – This module handles some common Riak operations

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.riak`.

- [Synopsis](riak_module.md#synopsis)
- [Parameters](riak_module.md#parameters)
- [Attributes](riak_module.md#attributes)
- [Examples](riak_module.md#examples)

## [Synopsis](riak_module.md#id1)

- This module can be used to join nodes to a cluster, check the status of the cluster.

Aliases: database.misc.riak

## [Parameters](riak_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **command**  string | The command you would like to perform against the cluster.  **Choices:**   - `"ping"` - `"kv_test"` - `"join"` - `"plan"` - `"commit"` |
| **config_dir**  path | The path to the riak configuration directory  **Default:** `"/etc/riak"` |
| **http_conn**  string | The ip address and port that is listening for Riak HTTP queries  **Default:** `"127.0.0.1:8098"` |
| **target_node**  string | The target node for certain operations (join, ping)  **Default:** `"riak@127.0.0.1"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_handoffs**  integer | Number of seconds to wait for handoffs to complete.  **Default:** `0` |
| **wait_for_ring**  integer | Number of seconds to wait for all nodes to agree on the ring.  **Default:** `0` |
| **wait_for_service**  string | Waits for a riak service to come online before continuing.  **Choices:**   - `"kv"` |

## [Attributes](riak_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](riak_module.md#id4)

```yaml+jinja
- name: "Join's a Riak node to another node"
  community.general.riak:
    command: join
    target_node: riak@10.1.1.1

- name: Wait for handoffs to finish. Use with async and poll.
  community.general.riak:
    wait_for_handoffs: true

- name: Wait for riak_kv service to startup
  community.general.riak:
    wait_for_service: kv
```

### Authors

- James Martin (@jsmartin)
- Drew Kerrigan (@drewkerrigan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
