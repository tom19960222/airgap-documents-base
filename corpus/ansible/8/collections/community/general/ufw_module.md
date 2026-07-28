---
collection: ansible
version: "8"
title: "community.general.ufw module – Manage firewall with UFW"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ufw_module.html
fetched_at: 2026-07-28T01:51:04+00:00
---
# community.general.ufw module – Manage firewall with UFW

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
> see [Requirements](ufw_module.md#ansible-collections-community-general-ufw-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ufw`.

- [Synopsis](ufw_module.md#synopsis)
- [Requirements](ufw_module.md#requirements)
- [Parameters](ufw_module.md#parameters)
- [Attributes](ufw_module.md#attributes)
- [Notes](ufw_module.md#notes)
- [Examples](ufw_module.md#examples)

## [Synopsis](ufw_module.md#id1)

- Manage firewall with UFW.

Aliases: system.ufw

## [Requirements](ufw_module.md#id2)

The below requirements are needed on the host that executes this module.

- `ufw` package

## [Parameters](ufw_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Add a comment to the rule. Requires UFW version >=0.35. |
| **default**  aliases: policy  string | Change the default policy for incoming or outgoing traffic.  **Choices:**   - `"allow"` - `"deny"` - `"reject"` |
| **delete**  boolean | Delete rule.  If `delete=true` and a value is provided for `insert`, then `insert` is ignored.  **Choices:**   - `false` ← (default) - `true` |
| **direction**  string | Select direction for a rule or default policy command. Mutually exclusive with `interface_in` and `interface_out`.  **Choices:**   - `"in"` - `"incoming"` - `"out"` - `"outgoing"` - `"routed"` |
| **from_ip**  aliases: from, src  string | Source IP address.  **Default:** `"any"` |
| **from_port**  string | Source port. |
| **insert**  integer | Insert the corresponding rule as rule number NUM.  Note that ufw numbers rules starting with 1.  If `delete=true` and a value is provided for `insert`, then `insert` is ignored. |
| **insert_relative_to**  string | Allows to interpret the index in `insert` relative to a position.  `zero` interprets the rule number as an absolute index (i.e. 1 is the first rule).  `first-ipv4` interprets the rule number relative to the index of the first IPv4 rule, or relative to the position where the first IPv4 rule would be if there is currently none.  `last-ipv4` interprets the rule number relative to the index of the last IPv4 rule, or relative to the position where the last IPv4 rule would be if there is currently none.  `first-ipv6` interprets the rule number relative to the index of the first IPv6 rule, or relative to the position where the first IPv6 rule would be if there is currently none.  `last-ipv6` interprets the rule number relative to the index of the last IPv6 rule, or relative to the position where the last IPv6 rule would be if there is currently none.  **Choices:**   - `"first-ipv4"` - `"first-ipv6"` - `"last-ipv4"` - `"last-ipv6"` - `"zero"` ← (default) |
| **interface**  aliases: if  string | Specify interface for the rule. The direction (in or out) used for the interface depends on the value of `direction`. See `interface_in` and `interface_out` for routed rules that needs to supply both an input and output interface. Mutually exclusive with `interface_in` and `interface_out`. |
| **interface_in**  aliases: if_in  string  *added in community.general 0.2.0* | Specify input interface for the rule. This is mutually exclusive with `direction` and `interface`. However, it is compatible with `interface_out` for routed rules. |
| **interface_out**  aliases: if_out  string  *added in community.general 0.2.0* | Specify output interface for the rule. This is mutually exclusive with `direction` and `interface`. However, it is compatible with `interface_in` for routed rules. |
| **log**  boolean | Log new connections matched to this rule  **Choices:**   - `false` ← (default) - `true` |
| **logging**  string | Toggles logging. Logged packets use the LOG_KERN syslog facility.  **Choices:**   - `"on"` - `"off"` - `"low"` - `"medium"` - `"high"` - `"full"` |
| **name**  aliases: app  string | Use profile located in `/etc/ufw/applications.d`. |
| **proto**  aliases: protocol  string | TCP/IP protocol.  **Choices:**   - `"any"` - `"tcp"` - `"udp"` - `"ipv6"` - `"esp"` - `"ah"` - `"gre"` - `"igmp"` |
| **route**  boolean | Apply the rule to routed/forwarded packets.  **Choices:**   - `false` ← (default) - `true` |
| **rule**  string | Add firewall rule  **Choices:**   - `"allow"` - `"deny"` - `"limit"` - `"reject"` |
| **state**  string | `enabled` reloads firewall and enables firewall on boot.  `disabled` unloads firewall and disables firewall on boot.  `reloaded` reloads firewall.  `reset` disables and resets firewall to installation defaults.  **Choices:**   - `"disabled"` - `"enabled"` - `"reloaded"` - `"reset"` |
| **to_ip**  aliases: dest, to  string | Destination IP address.  **Default:** `"any"` |
| **to_port**  aliases: port  string | Destination port. |

## [Attributes](ufw_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ufw_module.md#id5)

> **Note:**
>
> - See `man ufw` for more examples.

## [Examples](ufw_module.md#id6)

```yaml+jinja
- name: Allow everything and enable UFW
  community.general.ufw:
    state: enabled
    policy: allow

- name: Set logging
  community.general.ufw:
    logging: 'on'

# Sometimes it is desirable to let the sender know when traffic is
# being denied, rather than simply ignoring it. In these cases, use
# reject instead of deny. In addition, log rejected connections:
- community.general.ufw:
    rule: reject
    port: auth
    log: true

# ufw supports connection rate limiting, which is useful for protecting
# against brute-force login attacks. ufw will deny connections if an IP
# address has attempted to initiate 6 or more connections in the last
# 30 seconds. See  http://www.debian-administration.org/articles/187
# for details. Typical usage is:
- community.general.ufw:
    rule: limit
    port: ssh
    proto: tcp

# Allow OpenSSH. (Note that as ufw manages its own state, simply removing
# a rule=allow task can leave those ports exposed. Either use delete=true
# or a separate state=reset task)
- community.general.ufw:
    rule: allow
    name: OpenSSH

- name: Delete OpenSSH rule
  community.general.ufw:
    rule: allow
    name: OpenSSH
    delete: true

- name: Deny all access to port 53
  community.general.ufw:
    rule: deny
    port: '53'

- name: Allow port range 60000-61000
  community.general.ufw:
    rule: allow
    port: 60000:61000
    proto: tcp

- name: Allow all access to tcp port 80
  community.general.ufw:
    rule: allow
    port: '80'
    proto: tcp

- name: Allow all access from RFC1918 networks to this host
  community.general.ufw:
    rule: allow
    src: '{{ item }}'
  loop:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16

- name: Deny access to udp port 514 from host 1.2.3.4 and include a comment
  community.general.ufw:
    rule: deny
    proto: udp
    src: 1.2.3.4
    port: '514'
    comment: Block syslog

- name: Allow incoming access to eth0 from 1.2.3.5 port 5469 to 1.2.3.4 port 5469
  community.general.ufw:
    rule: allow
    interface: eth0
    direction: in
    proto: udp
    src: 1.2.3.5
    from_port: '5469'
    dest: 1.2.3.4
    to_port: '5469'

# Note that IPv6 must be enabled in /etc/default/ufw for IPv6 firewalling to work.
- name: Deny all traffic from the IPv6 2001:db8::/32 to tcp port 25 on this host
  community.general.ufw:
    rule: deny
    proto: tcp
    src: 2001:db8::/32
    port: '25'

- name: Deny all IPv6 traffic to tcp port 20 on this host
  # this should be the first IPv6 rule
  community.general.ufw:
    rule: deny
    proto: tcp
    port: '20'
    to_ip: "::"
    insert: 0
    insert_relative_to: first-ipv6

- name: Deny all IPv4 traffic to tcp port 20 on this host
  # This should be the third to last IPv4 rule
  # (insert: -1 addresses the second to last IPv4 rule;
  #  so the new rule will be inserted before the second
  #  to last IPv4 rule, and will be come the third to last
  #  IPv4 rule.)
  community.general.ufw:
    rule: deny
    proto: tcp
    port: '20'
    to_ip: "::"
    insert: -1
    insert_relative_to: last-ipv4

# Can be used to further restrict a global FORWARD policy set to allow
- name: Deny forwarded/routed traffic from subnet 1.2.3.0/24 to subnet 4.5.6.0/24
  community.general.ufw:
    rule: deny
    route: true
    src: 192.0.2.0/24
    dest: 198.51.100.0/24
```

### Authors

- Aleksey Ovcharenko (@ovcharenko)
- Jarno Keskikangas (@pyykkis)
- Ahti Kitsik (@ahtik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
