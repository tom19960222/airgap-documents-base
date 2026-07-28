---
collection: ansible
version: "8"
title: "community.hrobot.firewall module – Manage Hetzner’s dedicated server firewall"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hrobot/firewall_module.html
fetched_at: 2026-07-28T01:53:44+00:00
---
# community.hrobot.firewall module – Manage Hetzner’s dedicated server firewall

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/ui/repo/published/community/hrobot/) (version 1.8.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
> You need further requirements to be able to use this module,
> see [Requirements](firewall_module.md#ansible-collections-community-hrobot-firewall-module-requirements) for details.
>
> To use it in a playbook, specify: `community.hrobot.firewall`.

- [Synopsis](firewall_module.md#synopsis)
- [Requirements](firewall_module.md#requirements)
- [Parameters](firewall_module.md#parameters)
- [Attributes](firewall_module.md#attributes)
- [See Also](firewall_module.md#see-also)
- [Examples](firewall_module.md#examples)
- [Return Values](firewall_module.md#return-values)

## [Synopsis](firewall_module.md#id1)

- Manage Hetzner’s dedicated server firewall.
- Note that idempotency check for TCP flags simply compares strings and doesn’t try to interpret the rules. This might change in the future.

## [Requirements](firewall_module.md#id2)

The below requirements are needed on the host that executes this module.

- ipaddress

## [Parameters](firewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowlist_hos**  aliases: whitelist_hos  boolean | Whether Hetzner services have access.  **Choices:**   - `false` - `true` |
| **filter_ipv6**  boolean  *added in community.hrobot 1.8.0* | Whether to filter IPv6 traffic as well.  IPv4 traffic is always filtered, IPv6 traffic filtering needs to be explicitly enabled.  **Choices:**   - `false` - `true` |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **port**  string | Switch port of firewall.  **Choices:**   - `"main"` ← (default) - `"kvm"` |
| **rules**  dictionary | Firewall rules. |
| **input**  list / elements=dictionary | Input firewall rules. |
| **action**  string / required | Action if rule matches.  **Choices:**   - `"accept"` - `"discard"` |
| **dst_ip**  string | Destination IP address or subnet address.  CIDR notation. |
| **dst_port**  string | Destination port or port range. |
| **ip_version**  string | Internet protocol version.  Leave away to filter both protocols. Note that in that case, none of `rules.input[].dst_ip`, `rules.input[].src_ip`, or `rules.input[].protocol` can be specified. |
| **name**  string | Name of the firewall rule.  Note that Hetzner restricts the characters that can be used for rule names. At the moment, only letters `a-z`, `A-Z`, space, and the symbols `.`, `-`, `+`, `_`, and `@` are allowed. |
| **protocol**  string | Protocol above IP layer. |
| **src_ip**  string | Source IP address or subnet address.  CIDR notation. |
| **src_port**  string | Source port or port range. |
| **tcp_flags**  string | TCP flags or logical combination of flags.  Flags supported by Hetzner are `syn`, `fin`, `rst`, `psh` and `urg`.  They can be combined with `|` (logical or) and `&` (logical and).  See [the documentation](https://wiki.hetzner.de/index.php/Robot_Firewall/en#Parameter) for more information. |
| **output**  list / elements=dictionary  *added in community.hrobot 1.8.0* | Output firewall rules. |
| **action**  string / required | Action if rule matches.  **Choices:**   - `"accept"` - `"discard"` |
| **dst_ip**  string | Destination IP address or subnet address.  CIDR notation. |
| **dst_port**  string | Destination port or port range. |
| **ip_version**  string | Internet protocol version.  Leave away to filter both protocols. Note that in that case, none of `rules.output[].dst_ip`, `rules.output[].src_ip`, or `rules.output[].protocol` can be specified. |
| **name**  string | Name of the firewall rule.  Note that Hetzner restricts the characters that can be used for rule names. At the moment, only letters `a-z`, `A-Z`, space, and the symbols `.`, `-`, `+`, `_`, and `@` are allowed. |
| **protocol**  string | Protocol above IP layer. |
| **src_ip**  string | Source IP address or subnet address.  CIDR notation. |
| **src_port**  string | Source port or port range. |
| **tcp_flags**  string | TCP flags or logical combination of flags.  Flags supported by Hetzner are `syn`, `fin`, `rst`, `psh` and `urg`.  They can be combined with `|` (logical or) and `&` (logical and).  See [the documentation](https://wiki.hetzner.de/index.php/Robot_Firewall/en#Parameter) for more information. |
| **server_ip**  string | The server’s main IP address.  Exactly one of `server_ip` and `server_number` must be specified.  Note that Hetzner deprecated identifying the server’s firewall by the server’s main IP. Using this option can thus stop working at any time in the future. Use `server_number` instead. |
| **server_number**  integer  *added in community.hrobot 1.8.0* | The server’s number.  Exactly one of `server_ip` and `server_number` must be specified. |
| **state**  string | Status of the firewall.  Firewall is active if state is `present`, and disabled if state is `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Timeout (in seconds) for waiting for firewall to be configured.  **Default:** `180` |
| **update_timeout**  integer | Timeout to use when configuring the firewall.  Note that the API call returns before the firewall has been successfully set up.  **Default:** `30` |
| **wait_delay**  integer | Delay to wait (in seconds) before checking again whether the firewall has been configured.  **Default:** `10` |
| **wait_for_configured**  boolean | Whether to wait until the firewall has been successfully configured before determining what to do, and before returning from the module.  The API returns status `in progress` when the firewall is currently being configured. If this happens, the module will try again until the status changes to `active` or `disabled`.  Please note that there is a request limit. If you have to do multiple updates, it can be better to disable waiting, and regularly use [community.hrobot.firewall_info](firewall_info_module.md#ansible-collections-community-hrobot-firewall-info-module) to query status.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](firewall_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.hrobot.robot**  *added in community.hrobot 1.6.0* | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](firewall_module.md#id5)

> **See also:**
>
> [Firewall documentation](https://docs.hetzner.com/robot/dedicated-server/firewall/)
> :   Hetzner’s documentation on the stateless firewall for dedicated servers
>
> [community.hrobot.firewall_info](firewall_info_module.md#ansible-collections-community-hrobot-firewall-info-module)
> :   Retrieve information on firewall configuration.

## [Examples](firewall_module.md#id6)

```yaml+jinja
- name: Configure firewall for server with main IP 1.2.3.4
  community.hrobot.firewall:
    hetzner_user: foo
    hetzner_password: bar
    server_ip: 1.2.3.4
    state: present
    filter_ipv6: true
    allowlist_hos: true
    rules:
      input:
        - name: Allow ICMP protocol
          # This is needed so you can ping your server
          ip_version: ipv4
          protocol: icmp
          action: accept
          # Note that it is not possible to disable ICMP for IPv6
          # (https://robot.hetzner.com/doc/webservice/en.html#post-firewall-server-id)
        - name: Allow responses to incoming TCP connections
          protocol: tcp
          dst_port: '32768-65535'
          tcp_flags: ack
          action: accept
        - name: Allow restricted access from some known IPv4 addresses
          # Allow everything to ports 20-23 from 4.3.2.1/24 (IPv4 only)
          ip_version: ipv4
          src_ip: 4.3.2.1/24
          dst_port: '20-23'
          action: accept
        - name: Allow everything to port 443
          dst_port: '443'
          action: accept
        - name: Drop everything else
          action: discard
      output:
        - name: Accept everything
          action: accept
  register: result

- ansible.builtin.debug:
    msg: "{{ result }}"
```

## [Return Values](firewall_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **firewall**  dictionary | The firewall configuration.  **Returned:** success |
| **allowlist_hos**  boolean  *added in community.hrobot 1.2.0* | Whether Hetzner services have access.  **Returned:** success  **Sample:** `true` |
| **port**  string | Switch port of firewall.  `main` or `kvm`.  **Returned:** success  **Sample:** `"main"` |
| **rules**  dictionary | Firewall rules.  **Returned:** success |
| **input**  list / elements=dictionary | Input firewall rules.  **Returned:** success |
| **action**  string | Action if rule matches.  `accept` or `discard`.  **Returned:** success  **Can only return:**   - `"accept"` - `"discard"`   **Sample:** `"accept"` |
| **dst_ip**  string | Destination IP address or subnet address.  CIDR notation.  **Returned:** success  **Sample:** `"1.2.3.4/32"` |
| **dst_port**  string | Destination port or port range.  **Returned:** success  **Sample:** `"443"` |
| **ip_version**  string | Internet protocol version.  No value means the rule applies both to IPv4 and IPv6.  **Returned:** success  **Sample:** `"ipv4"` |
| **name**  string | Name of the firewall rule.  **Returned:** success  **Sample:** `"Allow HTTP access to server"` |
| **protocol**  string | Protocol above IP layer.  **Returned:** success  **Sample:** `"tcp"` |
| **src_ip**  string | Source IP address or subnet address.  CIDR notation.  **Returned:** success |
| **src_port**  string | Source port or port range.  **Returned:** success |
| **tcp_flags**  string | TCP flags or logical combination of flags.  **Returned:** success |
| **output**  list / elements=dictionary | Output firewall rules.  **Returned:** success |
| **action**  string | Action if rule matches.  `accept` or `discard`.  **Returned:** success  **Can only return:**   - `"accept"` - `"discard"`   **Sample:** `"accept"` |
| **dst_ip**  string | Destination IP address or subnet address.  CIDR notation.  **Returned:** success  **Sample:** `"1.2.3.4/32"` |
| **dst_port**  string | Destination port or port range.  **Returned:** success  **Sample:** `"443"` |
| **ip_version**  string | Internet protocol version.  No value means the rule applies both to IPv4 and IPv6.  **Returned:** success |
| **name**  string | Name of the firewall rule.  **Returned:** success  **Sample:** `"Allow HTTP access to server"` |
| **protocol**  string | Protocol above IP layer.  **Returned:** success  **Sample:** `"tcp"` |
| **src_ip**  string | Source IP address or subnet address.  CIDR notation.  **Returned:** success |
| **src_port**  string | Source port or port range.  **Returned:** success |
| **tcp_flags**  string | TCP flags or logical combination of flags.  **Returned:** success |
| **server_ip**  string | Server’s main IP address.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **server_number**  integer | Hetzner’s internal server number.  **Returned:** success  **Sample:** `12345` |
| **status**  string | Status of the firewall.  `active` or `disabled`.  Will be `in process` if the firewall is currently updated, and `wait_for_configured` is set to `false` or `timeout` to a too small value.  **Returned:** success  **Sample:** `"active"` |
| **whitelist_hos**  boolean | Whether Hetzner services have access.  Old name of return value `allowlist_hos`, will be removed eventually.  **Returned:** success  **Sample:** `true` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
- [Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-hrobot)
