---
collection: ansible
version: "8"
title: "community.windows.win_firewall_rule module – Windows firewall automation"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_firewall_rule_module.html
fetched_at: 2026-07-28T02:01:56+00:00
---
# community.windows.win_firewall_rule module – Windows firewall automation

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_firewall_rule`.

- [Synopsis](win_firewall_rule_module.md#synopsis)
- [Parameters](win_firewall_rule_module.md#parameters)
- [Notes](win_firewall_rule_module.md#notes)
- [See Also](win_firewall_rule_module.md#see-also)
- [Examples](win_firewall_rule_module.md#examples)

## [Synopsis](win_firewall_rule_module.md#id1)

- Allows you to create/remove/update firewall rules.

## [Parameters](win_firewall_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | What to do with the items this rule is for.  Defaults to `allow` when creating a new rule.  **Choices:**   - `"allow"` - `"block"` |
| **description**  string | Description for the firewall rule. |
| **direction**  string | Whether this rule is for inbound or outbound traffic.  Defaults to `in` when creating a new rule.  **Choices:**   - `"in"` - `"out"` |
| **enabled**  aliases: enable  boolean | Whether this firewall rule is enabled or disabled.  Defaults to `true` when creating a new rule.  **Choices:**   - `false` - `true` |
| **group**  string | The group name for the rule.  If *name* is not specified then the module will set the firewall options for all the rules in this group. |
| **icmp_type_code**  list / elements=string | The ICMP types and codes for the rule.  This is only valid when *protocol* is `icmpv4` or `icmpv6`.  Each entry follows the format `type:code` where `type` is the type number and `code` is the code number for that type or `*` for all codes.  Set the value to just `*` to apply the rule for all ICMP type codes.  See <https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml> for a list of ICMP types and the codes that apply to them. |
| **localip**  string | The local ip address this rule applies to.  Set to `any` to apply to all local ip addresses.  Defaults to `any` when creating a new rule. |
| **localport**  string | The local port this rule applies to.  Set to `any` to apply to all local ports.  Defaults to `any` when creating a new rule.  Must have *protocol* set |
| **name**  string | The rule’s display name.  This is required unless *group* is specified. |
| **profiles**  aliases: profile  list / elements=string | The profile this rule applies to.  Defaults to `domain,private,public` when creating a new rule. |
| **program**  string | The program this rule applies to.  Set to `any` to apply to all programs.  Defaults to `any` when creating a new rule. |
| **protocol**  string | The protocol this rule applies to.  Set to `any` to apply to all services.  Defaults to `any` when creating a new rule. |
| **remoteip**  string | The remote ip address/range this rule applies to.  Set to `any` to apply to all remote ip addresses.  Defaults to `any` when creating a new rule. |
| **remoteport**  string | The remote port this rule applies to.  Set to `any` to apply to all remote ports.  Defaults to `any` when creating a new rule.  Must have *protocol* set |
| **service**  string | The service this rule applies to.  Set to `any` to apply to all services.  Defaults to `any` when creating a new rule. |
| **state**  string | Should this rule be added or removed.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](win_firewall_rule_module.md#id3)

> **Note:**
>
> - Multiple firewall rules can share the same *name*, if there are multiple matches then the module will set the user defined options for each matching rule.

## [See Also](win_firewall_rule_module.md#id4)

> **See also:**
>
> [community.windows.win_firewall](win_firewall_module.md#ansible-collections-community-windows-win-firewall-module)
> :   Enable or disable the Windows Firewall.

## [Examples](win_firewall_rule_module.md#id5)

```yaml+jinja
- name: Firewall rule to allow SMTP on TCP port 25
  community.windows.win_firewall_rule:
    name: SMTP
    localport: 25
    action: allow
    direction: in
    protocol: tcp
    state: present
    enabled: yes

- name: Firewall rule to allow RDP on TCP port 3389
  community.windows.win_firewall_rule:
    name: Remote Desktop
    localport: 3389
    action: allow
    direction: in
    protocol: tcp
    profiles: private
    state: present
    enabled: yes

- name: Firewall rule to be created for application group
  community.windows.win_firewall_rule:
    name: SMTP
    group: application
    localport: 25
    action: allow
    direction: in
    protocol: tcp
    state: present
    enabled: yes

- name: Enable all the Firewall rules in application group
  win_firewall_rule:
    group: application
    enabled: yes

- name: Firewall rule to allow port range
  community.windows.win_firewall_rule:
    name: Sample port range
    localport: 5000-5010
    action: allow
    direction: in
    protocol: tcp
    state: present
    enabled: yes

- name: Firewall rule to allow ICMP v4 echo (ping)
  community.windows.win_firewall_rule:
    name: ICMP Allow incoming V4 echo request
    enabled: yes
    state: present
    profiles: private
    action: allow
    direction: in
    protocol: icmpv4
    icmp_type_code:
    - '8:*'

- name: Firewall rule to alloc ICMP v4 on all type codes
  community.windows.win_firewall_rule:
    name: ICMP Allow incoming V4 echo request
    enabled: yes
    state: present
    profiles: private
    action: allow
    direction: in
    protocol: icmpv4
    icmp_type_code: '*'
```

### Authors

- Artem Zinenko (@ar7z1)
- Timothy Vandenbrande (@TimothyVandenbrande)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
