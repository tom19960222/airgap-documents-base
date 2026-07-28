---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_prefix_lists module – Manage prefix-lists attributes of interfaces on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_prefix_lists_module.html
fetched_at: 2026-07-28T02:39:50+00:00
---
# junipernetworks.junos.junos_prefix_lists module – Manage prefix-lists attributes of interfaces on Junos devices.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_prefix_lists_module.md#ansible-collections-junipernetworks-junos-junos-prefix-lists-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_prefix_lists`.

New in junipernetworks.junos 2.1.0

- [Synopsis](junos_prefix_lists_module.md#synopsis)
- [Requirements](junos_prefix_lists_module.md#requirements)
- [Parameters](junos_prefix_lists_module.md#parameters)
- [Notes](junos_prefix_lists_module.md#notes)
- [Examples](junos_prefix_lists_module.md#examples)

## [Synopsis](junos_prefix_lists_module.md#id1)

- Manage prefix-lists attributes of interfaces on Junos network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: prefix_lists

## [Requirements](junos_prefix_lists_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_prefix_lists_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided link BGP address family dictionary. |
| **address_prefixes**  list / elements=string | Specify address prefixes. |
| **dynamic_db**  boolean | Enable object to exist in dynamic DB.  **Choices:**   - `false` - `true` |
| **name**  string / required | Specify the name of the prefix-list. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show policy-options**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_prefix_lists_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_prefix_lists_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
#
# [edit]

- name: Merge Junos prefix  lists
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: Internal
        address_prefixes:
          - 172.16.1.32
          - 172.16.3.32
      - name: Test1
        dynamic_db: true
      - name: Test2
        address_prefixes:
          - 172.16.2.32
          - 172.16.7.32
          - 172.16.9.32
    state: merged

# Task Output
# -------------
#
# before: []
# commands:
# - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# - "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item><nc:name>172.16.1.32</nc:name>"
# - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
# - "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list><nc:name>Test1</nc:name>"
# - "<nc:dynamic-db/></nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name>"
# - "<nc:prefix-list-item><nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
# - "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name></nc:prefix-list-item>"
# - "<nc:prefix-list-item><nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
# - "</nc:prefix-list></nc:policy-options>"
# after:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.2.32/32
#   - 172.16.7.32/32
#   - 172.16.9.32/32
#   name: Test2

# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Gather Junos prefix-lists
  junipernetworks.junos.junos_prefix_lists:
    state: gathered

# Task Output
# -------------
#
# gathered:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.2.32/32
#   - 172.16.7.32/32
#   - 172.16.9.32/32
#   name: Test2

# Using replaced

# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Replace existing Junos prefix-lists configuration with provided config
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: Test2
        address_prefixes:
          - 172.16.4.32
          - 172.16.8.32
          - 172.16.9.32"
    state: replaced

# Task Output
# -------------
#
# before:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.2.32/32
#   - 172.16.7.32/32
#   - 172.16.9.32/32
#   name: Test2
# commands:
# - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# - <nc:prefix-list delete="delete"><nc:name>Test2</nc:name></nc:prefix-list>
# - "<nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item><nc:name>172.16.4.32</nc:name>"
# - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.8.32</nc:name>"
# - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.9.32</nc:name>"
# - "</nc:prefix-list-item></nc:prefix-list></nc:policy-options>"
# after:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.4.32/32
#   - 172.16.8.32/32
#   - 172.16.9.32/32
#   name: Test2

# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.4.32/32;
#     172.16.8.32/32;
#     172.16.9.32/32;
# }

# Using overridden

# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.4.32/32;
#     172.16.8.32/32;
#     172.16.9.32/32;
# }

- name: Override Junos prefix-lists configuration with provided configuration
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: Test2
        address_prefixes:
          - 172.16.4.32/28
          - 172.16.8.32/28
          - 172.16.9.32/28
    state: overridden

# Task Output
# -------------
#
# before:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.4.32/32
#   - 172.16.8.32/32
#   - 172.16.9.32/32
#   name: Test2
# commands:
# - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# - <nc:prefix-list delete="delete"><nc:name>Internal</nc:name>
# - </nc:prefix-list><nc:prefix-list delete="delete"><nc:name>Test1</nc:name>
# - </nc:prefix-list><nc:prefix-list delete="delete"><nc:name>Test2</nc:name>
# - "</nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item>"
# - "<nc:name>172.16.4.32/28</nc:name></nc:prefix-list-item><nc:prefix-list-item>"
# - "<nc:name>172.16.8.32/28</nc:name></nc:prefix-list-item><nc:prefix-list-item>"
# - "<nc:name>172.16.9.32/28</nc:name></nc:prefix-list-item></nc:prefix-list></nc:policy-options>"
# after:
# - address_prefixes:
#   - 172.16.4.32/28
#   - 172.16.8.32/28
#   - 172.16.9.32/28
#   name: Test2

# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Test2 {
#     172.16.4.32/28;
#     172.16.8.32/28;
#     172.16.9.32/28;
# }

# Using deleted

# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Delete provided prefix-lists
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: "Test1"
      - name: "Test2"
    state: deleted

# Task Output
# -------------
#
# before:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.2.32/32
#   - 172.16.7.32/32
#   - 172.16.9.32/32
#   name: Test2
# commands:
# - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# - <nc:prefix-list delete="delete"><nc:name>Test1</nc:name></nc:prefix-list>
# - <nc:prefix-list delete="delete"><nc:name>Test2</nc:name></nc:prefix-list></nc:policy-options>
# after:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal

# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
#

# Using deleted without specifying config

# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Delete complete Junos prefix-lists configuration
  junipernetworks.junos.junos_prefix_lists:
    state: deleted

# Task Output
# -------------
#
# before:
# - address_prefixes:
#   - 172.16.1.32/32
#   - 172.16.3.32/32
#   name: Internal
# - dynamic_db: true
#   name: Test1
# - address_prefixes:
#   - 172.16.2.32/32
#   - 172.16.7.32/32
#   - 172.16.9.32/32
#   name: Test2
# commands:
# - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# - <nc:prefix-list delete="delete"/></nc:policy-options>
# after: []

# After state
# -----------
#
# vagrant@vsrx# show policy-options
#
# [edit]

# Using parsed

# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <policy-options>
#         <prefix-list>
#             <name>64510</name>
#         </prefix-list>
#         <prefix-list>
#             <name>64500</name>
#             <dynamic-db/>
#             <prefix-list-item>
#                 <name>172.16.1.16/28</name>
#             </prefix-list-item>
#             <prefix-list-item>
#                 <name>172.16.1.32/28</name>
#             </prefix-list-item>
#         </prefix-list>
#     </policy-options>
#     </configuration>
# </rpc-reply>

- name: Parse running prefix-lists configuration
  junipernetworks.junos.junos_prefix_lists:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Task Output
# -------------
# parsed:
# - name: '64510'
# - address_prefixes:
#   - 172.16.1.16/28
#   - 172.16.1.32/28
#   dynamic_db: true
#   name: '64500'

# Using rendered

- name: Render the xml for provided  configuration
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: Internal
        address_prefixes:
          - 172.16.1.32
          - 172.16.3.32
      - name: Test1
        dynamic_db: true
      - name: Test2
        address_prefixes:
          - 172.16.2.32
          - 172.16.7.32
          - 172.16.9.32
    state: rendered

# Task Output
# -------------
# rendered:
# - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# - "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item><nc:name>172.16.1.32</nc:name>"
# - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
# - "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list><nc:name>Test1</nc:name>"
# - "<nc:dynamic-db/></nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name>"
# - "<nc:prefix-list-item><nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
# - "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name></nc:prefix-list-item>"
# - "<nc:prefix-list-item><nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
# - "</nc:prefix-list></nc:policy-options>"
```

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
