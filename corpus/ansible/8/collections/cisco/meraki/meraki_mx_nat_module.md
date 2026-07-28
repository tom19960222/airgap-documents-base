---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mx_nat module – Manage NAT rules in Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mx_nat_module.html
fetched_at: 2026-07-28T01:32:39+00:00
---
# cisco.meraki.meraki_mx_nat module – Manage NAT rules in Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_nat`.

- [DEPRECATED](meraki_mx_nat_module.md#deprecated)
- [Synopsis](meraki_mx_nat_module.md#synopsis)
- [Parameters](meraki_mx_nat_module.md#parameters)
- [Notes](meraki_mx_nat_module.md#notes)
- [Examples](meraki_mx_nat_module.md#examples)
- [Return Values](meraki_mx_nat_module.md#return-values)
- [Status](meraki_mx_nat_module.md#status)

## [DEPRECATED](meraki_mx_nat_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.networks_appliance_firewall_one_to_many_nat_rules

## [Synopsis](meraki_mx_nat_module.md#id2)

- Allows for creation, management, and visibility of NAT rules (1:1, 1:many, port forwarding) within Meraki.

## [Parameters](meraki_mx_nat_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **one_to_many**  list / elements=dictionary | List of 1:many NAT rules. |
| **port_rules**  list / elements=dictionary | List of associated port rules. |
| **allowed_ips**  list / elements=string | Remote IP addresses or ranges that are permitted to access the internal resource via this port forwarding rule, or ‘any’. |
| **local_ip**  string | Local IP address to which traffic will be forwarded. |
| **local_port**  string | Destination port of the forwarded traffic that will be sent from the MX to the specified host on the LAN.  If you simply wish to forward the traffic without translating the port, this should be the same as the Public port. |
| **name**  string | A description of the rule. |
| **protocol**  string | Protocol to apply NAT rule to.  **Choices:**   - `"tcp"` - `"udp"` |
| **public_port**  string | Destination port of the traffic that is arriving on the WAN. |
| **public_ip**  string | The IP address that will be used to access the internal resource from the WAN. |
| **uplink**  string | The physical WAN interface on which the traffic will arrive.  **Choices:**   - `"both"` - `"internet1"` - `"internet2"` |
| **one_to_one**  list / elements=dictionary | List of 1:1 NAT rules. |
| **allowed_inbound**  list / elements=dictionary | The ports this mapping will provide access on, and the remote IPs that will be allowed access to the resource. |
| **allowed_ips**  list / elements=string | ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges, or ‘any’. |
| **destination_ports**  list / elements=string | List of ports or port ranges that will be forwarded to the host on the LAN. |
| **protocol**  string | Protocol to apply NAT rule to.  **Choices:**   - `"any"` ← (default) - `"icmp-ping"` - `"tcp"` - `"udp"` |
| **lan_ip**  string | The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN. |
| **name**  string | A descriptive name for the rule. |
| **public_ip**  string | The IP address that will be used to access the internal resource from the WAN. |
| **uplink**  string | The physical WAN interface on which the traffic will arrive.  **Choices:**   - `"both"` - `"internet1"` - `"internet2"` |
| **org_id**  string | ID of organization associated to a network. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **port_forwarding**  list / elements=dictionary | List of port forwarding rules. |
| **allowed_ips**  list / elements=string | List of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges (or any). |
| **lan_ip**  string | The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN. |
| **local_port**  integer | A port or port ranges that will receive the forwarded traffic from the WAN. |
| **name**  string | A descriptive name for the rule. |
| **protocol**  string | Protocol to forward traffic for.  **Choices:**   - `"tcp"` - `"udp"` |
| **public_port**  integer | A port or port ranges that will be forwarded to the host on the LAN. |
| **uplink**  string | The physical WAN interface on which the traffic will arrive.  **Choices:**   - `"both"` - `"internet1"` - `"internet2"` |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Create or modify an organization.  **Choices:**   - `"present"` ← (default) - `"query"` |
| **subset**  list / elements=string | Specifies which NAT components to query.  **Choices:**   - `"1:1"` - `"1:many"` - `"all"` ← (default) - `"port_forwarding"`   **Default:** `["all"]` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_mx_nat_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_nat_module.md#id5)

```yaml+jinja
- name: Query all NAT rules
  meraki_nat:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
    subset: all
  delegate_to: localhost

- name: Query 1:1 NAT rules
  meraki_nat:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
    subset: '1:1'
  delegate_to: localhost

- name: Create 1:1 rule
  meraki_nat:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    one_to_one:
      - name: Service behind NAT
        public_ip: 1.2.1.2
        lan_ip: 192.168.128.1
        uplink: internet1
        allowed_inbound:
          - protocol: tcp
            destination_ports:
              - 80
            allowed_ips:
              - 10.10.10.10
  delegate_to: localhost

- name: Create 1:many rule
  meraki_nat:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    one_to_many:
      - public_ip: 1.1.1.1
        uplink: internet1
        port_rules:
          - name: Test rule
            protocol: tcp
            public_port: 10
            local_ip: 192.168.128.1
            local_port: 11
            allowed_ips:
              - any
  delegate_to: localhost

- name: Create port forwarding rule
  meraki_nat:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    port_forwarding:
      - name: Test map
        lan_ip: 192.168.128.1
        uplink: both
        protocol: tcp
        allowed_ips:
          - 1.1.1.1
        public_port: 10
        local_port: 11
  delegate_to: localhost
```

## [Return Values](meraki_mx_nat_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the created or manipulated object.  **Returned:** success |
| **one_to_many**  complex | Information about 1:many NAT object.  **Returned:** success, when 1:many NAT object is in task |
| **rules**  complex | List of 1:many NAT rules.  **Returned:** success, when 1:many NAT object is in task |
| **portRules**  complex | List of NAT port rules.  **Returned:** success, when 1:many NAT object is in task |
| **allowedIps**  list / elements=string | List of IP addresses to be forwarded.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `["10.80.100.0/24"]` |
| **localIp**  string | Local IP address traffic will be forwarded.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"192.0.2.10"` |
| **localPort**  integer | Destination port to be forwarded to.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `443` |
| **name**  string | Name of NAT object.  **Returned:** success, when 1:many NAT object is in task  **Sample:** `"Web server behind NAT"` |
| **protocol**  string | Protocol to apply NAT rule to.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"tcp"` |
| **publicPort**  integer | Destination port of the traffic that is arriving on WAN.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `9443` |
| **publicIp**  string | Public IP address to be mapped.  **Returned:** success, when 1:many NAT object is in task  **Sample:** `"148.2.5.100"` |
| **uplink**  string | Internet port where rule is applied.  **Returned:** success, when 1:many NAT object is in task  **Sample:** `"internet1"` |
| **one_to_one**  complex | Information about 1:1 NAT object.  **Returned:** success, when 1:1 NAT object is in task |
| **rules**  complex | List of 1:1 NAT rules.  **Returned:** success, when 1:1 NAT object is in task |
| **allowedInbound**  complex | List of inbound forwarding rules.  **Returned:** success, when 1:1 NAT object is in task |
| **allowedIps**  list / elements=string | List of IP addresses to be forwarded.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `["10.80.100.0/24"]` |
| **destinationPorts**  string | Ports to apply NAT rule to.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"80"` |
| **protocol**  string | Protocol to apply NAT rule to.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"tcp"` |
| **lanIp**  string | Local IP address to be mapped.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"192.168.128.22"` |
| **name**  string | Name of NAT object.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"Web server behind NAT"` |
| **publicIp**  string | Public IP address to be mapped.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"148.2.5.100"` |
| **uplink**  string | Internet port where rule is applied.  **Returned:** success, when 1:1 NAT object is in task  **Sample:** `"internet1"` |
| **port_forwarding**  complex | Information about port forwarding rules.  **Returned:** success, when port forwarding is in task |
| **rules**  complex | List of port forwarding rules.  **Returned:** success, when port forwarding is in task |
| **allowedIps**  list / elements=string | List of IP addresses to be forwarded.  **Returned:** success, when port forwarding is in task  **Sample:** `["10.80.100.0/24"]` |
| **lanIp**  string | Local IP address to be mapped.  **Returned:** success, when port forwarding is in task  **Sample:** `"192.168.128.22"` |
| **localPort**  integer | Destination port to be forwarded to.  **Returned:** success, when port forwarding is in task  **Sample:** `443` |
| **name**  string | Name of NAT object.  **Returned:** success, when port forwarding is in task  **Sample:** `"Web server behind NAT"` |
| **protocol**  string | Protocol to apply NAT rule to.  **Returned:** success, when port forwarding is in task  **Sample:** `"tcp"` |
| **publicPort**  integer | Destination port of the traffic that is arriving on WAN.  **Returned:** success, when port forwarding is in task  **Sample:** `9443` |
| **uplink**  string | Internet port where rule is applied.  **Returned:** success, when port forwarding is in task  **Sample:** `"internet1"` |

## [Status](meraki_mx_nat_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mx_nat_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
