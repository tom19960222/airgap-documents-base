---
collection: ansible
version: "6"
title: "community.windows.win_listen_ports_facts module – Recopilates the facts of the listening ports of the machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_listen_ports_facts_module.html
fetched_at: 2026-07-27T17:23:35+00:00
---
# community.windows.win_listen_ports_facts module – Recopilates the facts of the listening ports of the machine

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_listen_ports_facts`.

New in community.windows 1.10.0

- [Synopsis](win_listen_ports_facts_module.md#synopsis)
- [Parameters](win_listen_ports_facts_module.md#parameters)
- [Notes](win_listen_ports_facts_module.md#notes)
- [See Also](win_listen_ports_facts_module.md#see-also)
- [Examples](win_listen_ports_facts_module.md#examples)
- [Return Values](win_listen_ports_facts_module.md#return-values)

## [Synopsis](win_listen_ports_facts_module.md#id1)

- Recopilates the information of the TCP and UDP ports of the machine and the related processes.
- State of the TCP ports could be filtered, as well as the format of the date when the parent process was launched.
- The module’s goal is to replicate the functionality of the linux module listen_ports_facts, mantaining the format of the said module.

## [Parameters](win_listen_ports_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **date_format**  string | The format of the date when the process that owns the port started.  The date specification is UFormat  Default: `"%c"` |
| **tcp_filter**  list / elements=string | Filter for the state of the TCP ports that will be recopilated.  Supports multiple states (Bound, Closed, CloseWait, Closing, DeleteTCB, Established, FinWait1, FinWait2, LastAck, Listen, SynReceived, SynSent and TimeWait), that can be used alone or combined. Note that the Bound state is only available on PowerShell version 4.0 or later.  Default: `["Listen"]` |

## [Notes](win_listen_ports_facts_module.md#id3)

> **Note:**
>
> - The generated data (tcp_listen and udp_listen) and the fields within follows the listen_ports_facts schema to achieve compatibility with the said module output, even though this module if capable of extracting ports with a state other than Listen

## [See Also](win_listen_ports_facts_module.md#id4)

> **See also:**
>
> [community.general.listen_ports_facts](../general/listen_ports_facts_module.md#ansible-collections-community-general-listen-ports-facts-module)
> :   Gather facts on processes listening on TCP and UDP ports.

## [Examples](win_listen_ports_facts_module.md#id5)

```yaml+jinja
- name: Recopilate ports facts
  community.windows.win_listen_ports_facts:

- name: Retrieve only ports with Closing and Established states
  community.windows.win_listen_ports_facts:
    tcp_filter:
        - Closing
        - Established

- name: Get ports facts with only the year within the date field
  community.windows.win_listen_ports_facts:
    date_format: '%Y'
```

## [Return Values](win_listen_ports_facts_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tcp_listen**  list / elements=dictionary | List of dicts with the detected TCP ports  Returned: success  Sample: `[{"address": "127.0.0.1", "name": "python", "pid": 5332, "port": 82, "protocol": "tcp", "stime": "Thu Nov 18 15:27:42 2021", "user": "SERVER\\Administrator"}]` |
| **udp_listen**  list / elements=dictionary | List of dicts with the detected UDP ports  Returned: success  Sample: `[{"address": "127.0.0.1", "name": "python", "pid": 5332, "port": 82, "protocol": "udp", "stime": "Thu Nov 18 15:27:42 2021", "user": "SERVER\\Administrator"}]` |

### Authors

- David Nieto (@david-ns)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
