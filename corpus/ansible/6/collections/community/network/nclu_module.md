---
collection: ansible
version: "6"
title: "community.network.nclu module – Configure network interfaces using NCLU"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/nclu_module.html
fetched_at: 2026-07-27T17:18:58+00:00
---
# community.network.nclu module – Configure network interfaces using NCLU

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.nclu`.

- [Synopsis](nclu_module.md#synopsis)
- [Parameters](nclu_module.md#parameters)
- [Notes](nclu_module.md#notes)
- [Examples](nclu_module.md#examples)
- [Return Values](nclu_module.md#return-values)

## [Synopsis](nclu_module.md#id1)

- Interface to the Network Command Line Utility, developed to make it easier to configure operating systems running ifupdown2 and Quagga, such as Cumulus Linux. Command documentation is available at <https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Network-Command-Line-Utility-NCLU/>

## [Parameters](nclu_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **abort**  boolean | Boolean. When true, perform a ‘net abort’ before the block. This cleans out any uncommitted changes in the buffer. Mutually exclusive with *atomic*.  Choices:   - `false` ← (default) - `true` |
| **atomic**  boolean | When true, equivalent to both *commit* and *abort* being true. Mutually exclusive with *commit* and *atomic*.  Choices:   - `false` ← (default) - `true` |
| **commands**  string | A list of strings containing the net commands to run. Mutually exclusive with *template*. |
| **commit**  boolean | When true, performs a ‘net commit’ at the end of the block. Mutually exclusive with *atomic*.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Commit description that will be recorded to the commit log if *commit* or *atomic* are true.  Default: `"Ansible-originated commit"` |
| **template**  string | A single, multi-line string with jinja2 formatting. This string will be broken by lines, and each line will be run through net. Mutually exclusive with *commands*. |

## [Notes](nclu_module.md#id3)

> **Note:**
>
> - Supports check_mode. Note that when using check_mode, *abort* is always true.

## [Examples](nclu_module.md#id4)

```yaml+jinja
- name: Add two interfaces without committing any changes
  community.network.nclu:
    commands:
        - add int swp1
        - add int swp2

- name: Modify hostname to Cumulus-1 and commit the change
  community.network.nclu:
    commands:
        - add hostname Cumulus-1
    commit: true

- name: Add 48 interfaces and commit the change.
  community.network.nclu:
    template: |
        {% for iface in range(1,49) %}
        add int swp{{iface}}
        {% endfor %}
    commit: true
    description: "Ansible - add swps1-48"

- name: Fetch Status Of Interface
  community.network.nclu:
    commands:
        - show interface swp1
  register: output

- name: Print Status Of Interface
  ansible.builtin.debug:
    var: output

- name: Fetch Details From All Interfaces In JSON Format
  community.network.nclu:
    commands:
        - show interface json
  register: output

- name: Print Interface Details
  ansible.builtin.debug:
    var: output["msg"]

- name: Atomically add an interface
  community.network.nclu:
    commands:
        - add int swp1
    atomic: true
    description: "Ansible - add swp1"

- name: Remove IP address from interface swp1
  community.network.nclu:
    commands:
        - del int swp1 ip address 1.1.1.1/24

- name: Configure BGP AS and add 2 EBGP neighbors using BGP Unnumbered
  community.network.nclu:
    commands:
        - add bgp autonomous-system 65000
        - add bgp neighbor swp51 interface remote-as external
        - add bgp neighbor swp52 interface remote-as external
    commit: true

- name: Configure BGP AS and Add 2 EBGP neighbors Using BGP Unnumbered via Template
  community.network.nclu:
    template: |
      {% for neighbor in range(51,53) %}
      add bgp neighbor swp{{neighbor}} interface remote-as external
      add bgp autonomous-system 65000
      {% endfor %}
    atomic: true

- name: Check BGP Status
  community.network.nclu:
    commands:
        - show bgp summary json
  register: output

- name: Print BGP Status In JSON
  ansible.builtin.debug:
    var: output["msg"]
```

## [Return Values](nclu_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | whether the interface was changed  Returned: changed  Sample: `true` |
| **msg**  string | human-readable report of success or failure  Returned: always  Sample: `"interface bond0 config updated"` |

### Authors

- Cumulus Networks (@isharacomix)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
