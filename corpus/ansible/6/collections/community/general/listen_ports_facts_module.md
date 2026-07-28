---
collection: ansible
version: "6"
title: "community.general.listen_ports_facts module – Gather facts on processes listening on TCP and UDP ports"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/listen_ports_facts_module.html
fetched_at: 2026-07-27T17:10:33+00:00
---
# community.general.listen_ports_facts module – Gather facts on processes listening on TCP and UDP ports

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](listen_ports_facts_module.md#ansible-collections-community-general-listen-ports-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.listen_ports_facts`.

- [Synopsis](listen_ports_facts_module.md#synopsis)
- [Requirements](listen_ports_facts_module.md#requirements)
- [Parameters](listen_ports_facts_module.md#parameters)
- [Notes](listen_ports_facts_module.md#notes)
- [Examples](listen_ports_facts_module.md#examples)
- [Returned Facts](listen_ports_facts_module.md#returned-facts)

## [Synopsis](listen_ports_facts_module.md#id1)

- Gather facts on processes listening on TCP and UDP ports using the `netstat` or `ss` commands.
- This module currently supports Linux only.

## [Requirements](listen_ports_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- netstat or ss

## [Parameters](listen_ports_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **command**  string  added in community.general 4.1.0 | Override which command to use for fetching listen ports.  By default module will use first found supported command on the system (in alphanumerical order).  Choices:   - `"netstat"` - `"ss"` |
| **include_non_listening**  boolean  added in community.general 5.4.0 | Show both listening and non-listening sockets (for TCP this means established connections).  Adds the return values `state` and `foreign_address` to the returned facts.  Choices:   - `false` ← (default) - `true` |

## [Notes](listen_ports_facts_module.md#id4)

> **Note:**
>
> - `ss` returns all processes for each listen address and port.
>   This plugin will return each of them, so multiple entries for the same listen address and port are likely in results.

## [Examples](listen_ports_facts_module.md#id5)

```yaml+jinja
- name: Gather facts on listening ports
  community.general.listen_ports_facts:

- name: TCP whitelist violation
  ansible.builtin.debug:
    msg: TCP port {{ item.port }} by pid {{ item.pid }} violates the whitelist
  vars:
    tcp_listen_violations: "{{ ansible_facts.tcp_listen | selectattr('port', 'in', tcp_whitelist) | list }}"
    tcp_whitelist:
      - 22
      - 25
  loop: "{{ tcp_listen_violations }}"

- name: List TCP ports
  ansible.builtin.debug:
    msg: "{{ ansible_facts.tcp_listen  | map(attribute='port') | sort | list }}"

- name: List UDP ports
  ansible.builtin.debug:
    msg: "{{ ansible_facts.udp_listen | map(attribute='port') | sort | list }}"

- name: List all ports
  ansible.builtin.debug:
    msg: "{{ (ansible_facts.tcp_listen + ansible_facts.udp_listen) | map(attribute='port') | unique | sort | list }}"

- name: Gather facts on all ports and override which command to use
  community.general.listen_ports_facts:
    command: 'netstat'
    include_non_listening: true
```

## [Returned Facts](listen_ports_facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **tcp_listen**  list / elements=string | A list of processes that are listening on a TCP port.  Returned: if TCP servers were found |
| **address**  string | The address the server is listening on.  Returned: always  Sample: `"0.0.0.0"` |
| **foreign_address**  string  added in community.general 5.4.0 | The address of the remote end of the socket.  Returned: if *include_non_listening=true*  Sample: `"10.80.0.1"` |
| **name**  string | The name of the listening process.  Returned: if user permissions allow  Sample: `"mysqld"` |
| **pid**  integer | The pid of the listening process.  Returned: always  Sample: `1223` |
| **port**  integer | The port the server is listening on.  Returned: always  Sample: `3306` |
| **protocol**  string | The network protocol of the server.  Returned: always  Sample: `"tcp"` |
| **state**  string  added in community.general 5.4.0 | The state of the socket.  Returned: if *include_non_listening=true*  Sample: `"ESTABLISHED"` |
| **stime**  string | The start time of the listening process.  Returned: always  Sample: `"Thu Feb  2 13:29:45 2017"` |
| **user**  string | The user who is running the listening process.  Returned: always  Sample: `"mysql"` |
| **udp_listen**  list / elements=string | A list of processes that are listening on a UDP port.  Returned: if UDP servers were found |
| **address**  string | The address the server is listening on.  Returned: always  Sample: `"0.0.0.0"` |
| **foreign_address**  string  added in community.general 5.4.0 | The address of the remote end of the socket.  Returned: if *include_non_listening=true*  Sample: `"10.80.0.1"` |
| **name**  string | The name of the listening process.  Returned: if user permissions allow  Sample: `"rsyslogd"` |
| **pid**  integer | The pid of the listening process.  Returned: always  Sample: `609` |
| **port**  integer | The port the server is listening on.  Returned: always  Sample: `514` |
| **protocol**  string | The network protocol of the server.  Returned: always  Sample: `"udp"` |
| **state**  string  added in community.general 5.4.0 | The state of the socket. UDP is a connectionless protocol. Shows UCONN or ESTAB.  Returned: if *include_non_listening=true*  Sample: `"UCONN"` |
| **stime**  string | The start time of the listening process.  Returned: always  Sample: `"Thu Feb  2 13:29:45 2017"` |
| **user**  string | The user who is running the listening process.  Returned: always  Sample: `"root"` |

### Authors

- Nathan Davison (@ndavison)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
