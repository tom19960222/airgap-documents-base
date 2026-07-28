---
collection: ansible
version: "8"
title: "community.general.iptables_state module – Save iptables state into a file or restore it from a file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/iptables_state_module.html
fetched_at: 2026-07-28T01:46:52+00:00
---
# community.general.iptables_state module – Save iptables state into a file or restore it from a file

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
> see [Requirements](iptables_state_module.md#ansible-collections-community-general-iptables-state-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.iptables_state`.

New in community.general 1.1.0

- [Synopsis](iptables_state_module.md#synopsis)
- [Requirements](iptables_state_module.md#requirements)
- [Parameters](iptables_state_module.md#parameters)
- [Attributes](iptables_state_module.md#attributes)
- [Notes](iptables_state_module.md#notes)
- [Examples](iptables_state_module.md#examples)
- [Return Values](iptables_state_module.md#return-values)

## [Synopsis](iptables_state_module.md#id1)

- `iptables` is used to set up, maintain, and inspect the tables of IP packet filter rules in the Linux kernel.
- This module handles the saving and/or loading of rules. This is the same as the behaviour of the `iptables-save` and `iptables-restore` (or `ip6tables-save` and `ip6tables-restore` for IPv6) commands which this module uses internally.
- Modifying the state of the firewall remotely may lead to loose access to the host in case of mistake in new ruleset. This module embeds a rollback feature to avoid this, by telling the host to restore previous rules if a cookie is still there after a given delay, and all this time telling the controller to try to remove this cookie on the host through a new connection.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: system.iptables_state

## [Requirements](iptables_state_module.md#id2)

The below requirements are needed on the host that executes this module.

- iptables
- ip6tables

## [Parameters](iptables_state_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **counters**  boolean | Save or restore the values of all packet and byte counters.  When `true`, the module is not idempotent.  **Choices:**   - `false` ← (default) - `true` |
| **ip_version**  string | Which version of the IP protocol this module should apply to.  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` |
| **modprobe**  path | Specify the path to the `modprobe` program internally used by iptables related commands to load kernel modules.  By default, `/proc/sys/kernel/modprobe` is inspected to determine the executable’s path. |
| **noflush**  boolean | For `state=restored`, ignored otherwise.  If `false`, restoring iptables rules from a file flushes (deletes) all previous contents of the respective table(s). If `true`, the previous rules are left untouched (but policies are updated anyway, for all built-in chains).  **Choices:**   - `false` ← (default) - `true` |
| **path**  path / required | The file the iptables state should be saved to.  The file the iptables state should be restored from. |
| **state**  string / required | Whether the firewall state should be saved (into a file) or restored (from a file).  **Choices:**   - `"saved"` - `"restored"` |
| **table**  string | When `state=restored`, restore only the named table even if the input file contains other tables. Fail if the named table is not declared in the file.  When `state=saved`, restrict output to the specified table. If not specified, output includes all active tables.  **Choices:**   - `"filter"` - `"nat"` - `"mangle"` - `"raw"` - `"security"` |
| **wait**  integer | Wait N seconds for the xtables lock to prevent instant failure in case multiple instances of the program are running concurrently. |

## [Attributes](iptables_state_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller. |
| **async** | **Support:** **full** | Supports being used with the `async` keyword. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](iptables_state_module.md#id5)

> **Note:**
>
> - The rollback feature is not a module option and depends on task’s attributes. To enable it, the module must be played asynchronously, i.e. by setting task attributes `poll` to `0`, and `async` to a value less or equal to `ANSIBLE_TIMEOUT`. If `async` is greater, the rollback will still happen if it shall happen, but you will experience a connection timeout instead of more relevant info returned by the module after its failure.

## [Examples](iptables_state_module.md#id6)

```yaml+jinja
# This will apply to all loaded/active IPv4 tables.
- name: Save current state of the firewall in system file
  community.general.iptables_state:
    state: saved
    path: /etc/sysconfig/iptables

# This will apply only to IPv6 filter table.
- name: save current state of the firewall in system file
  community.general.iptables_state:
    ip_version: ipv6
    table: filter
    state: saved
    path: /etc/iptables/rules.v6

# This will load a state from a file, with a rollback in case of access loss
- name: restore firewall state from a file
  community.general.iptables_state:
    state: restored
    path: /run/iptables.apply
  async: "{{ ansible_timeout }}"
  poll: 0

# This will load new rules by appending them to the current ones
- name: restore firewall state from a file
  community.general.iptables_state:
    state: restored
    path: /run/iptables.apply
    noflush: true
  async: "{{ ansible_timeout }}"
  poll: 0

# This will only retrieve information
- name: get current state of the firewall
  community.general.iptables_state:
    state: saved
    path: /tmp/iptables
  check_mode: true
  changed_when: false
  register: iptables_state

- name: show current state of the firewall
  ansible.builtin.debug:
    var: iptables_state.initial_state
```

## [Return Values](iptables_state_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **applied**  boolean | Whether or not the wanted state has been successfully restored.  **Returned:** always  **Sample:** `true` |
| **initial_state**  list / elements=string | The current state of the firewall when module starts.  **Returned:** always  **Sample:** `["# Generated by xtables-save v1.8.2", "*filter", ":INPUT ACCEPT [0:0]", ":FORWARD ACCEPT [0:0]", ":OUTPUT ACCEPT [0:0]", "COMMIT", "# Completed"]` |
| **restored**  list / elements=string | The state the module restored, whenever it is finally applied or not.  **Returned:** always  **Sample:** `["# Generated by xtables-save v1.8.2", "*filter", ":INPUT DROP [0:0]", ":FORWARD DROP [0:0]", ":OUTPUT ACCEPT [0:0]", "-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT", "-A INPUT -m conntrack --ctstate INVALID -j DROP", "-A INPUT -i lo -j ACCEPT", "-A INPUT -p icmp -j ACCEPT", "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT", "COMMIT", "# Completed"]` |
| **saved**  list / elements=string | The iptables state the module saved.  **Returned:** always  **Sample:** `["# Generated by xtables-save v1.8.2", "*filter", ":INPUT ACCEPT [0:0]", ":FORWARD DROP [0:0]", ":OUTPUT ACCEPT [0:0]", "COMMIT", "# Completed"]` |
| **tables**  dictionary | The iptables we have interest for when module starts.  **Returned:** always  **Sample:** `{"filter": [":INPUT ACCEPT", ":FORWARD ACCEPT", ":OUTPUT ACCEPT", "-A INPUT -i lo -j ACCEPT", "-A INPUT -p icmp -j ACCEPT", "-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT", "-A INPUT -j REJECT --reject-with icmp-host-prohibited"], "nat": [":PREROUTING ACCEPT", ":INPUT ACCEPT", ":OUTPUT ACCEPT", ":POSTROUTING ACCEPT"]}` |
| **table**  list / elements=string | Policies and rules for all chains of the named table.  **Returned:** success |

### Authors

- quidame (@quidame)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
