---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_network_acl_rule module – Manages network access control list (ACL) rules on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_network_acl_rule_module.html
fetched_at: 2026-07-28T02:46:08+00:00
---
# ngine_io.cloudstack.cs_network_acl_rule module – Manages network access control list (ACL) rules on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_network_acl_rule_module.md#ansible-collections-ngine-io-cloudstack-cs-network-acl-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_network_acl_rule`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_network_acl_rule_module.md#synopsis)
- [Requirements](cs_network_acl_rule_module.md#requirements)
- [Parameters](cs_network_acl_rule_module.md#parameters)
- [Notes](cs_network_acl_rule_module.md#notes)
- [Examples](cs_network_acl_rule_module.md#examples)
- [Return Values](cs_network_acl_rule_module.md#return-values)

## [Synopsis](cs_network_acl_rule_module.md#id1)

- Add, update and remove network ACL rules.

## [Requirements](cs_network_acl_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_network_acl_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the VPC is related to. |
| **action_policy**  aliases: action  string | Action policy of the rule.  **Choices:**   - `"allow"` ← (default) - `"deny"` |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidrs**  aliases: cidr  list / elements=string | CIDRs of the rule.  **Default:** `["0.0.0.0/0"]` |
| **domain**  string | Domain the VPC is related to. |
| **end_port**  integer | End port for this rule.  Considered if *protocol=tcp* or *protocol=udp*.  If not specified, equal *start_port*. |
| **icmp_code**  integer | Error code for this icmp message.  Considered if *protocol=icmp*. |
| **icmp_type**  integer | Type of the icmp message being sent.  Considered if *protocol=icmp*. |
| **network_acl**  aliases: acl  string / required | Name of the network ACL. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the VPC is related to. |
| **protocol**  string | Protocol of the rule  **Choices:**   - `"tcp"` ← (default) - `"udp"` - `"icmp"` - `"all"` - `"by_number"` |
| **protocol_number**  integer | Protocol number from 1 to 256 required if *protocol=by_number*. |
| **rule_position**  aliases: number  integer / required | The position of the network ACL rule. |
| **start_port**  aliases: port  integer | Start port for this rule.  Considered if *protocol=tcp* or *protocol=udp*. |
| **state**  string | State of the network ACL rule.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  If you want to delete all tags, set a empty list e.g. *tags: []*. |
| **traffic_type**  aliases: type  string | Traffic type of the rule.  **Choices:**   - `"ingress"` ← (default) - `"egress"` |
| **vpc**  string / required | VPC the network ACL is related to. |
| **zone**  string / required | Name of the zone the VPC related to. |

## [Notes](cs_network_acl_rule_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_network_acl_rule_module.md#id5)

```yaml+jinja
- name: create a network ACL rule, allow port 80 ingress
  ngine_io.cloudstack.cs_network_acl_rule:
    network_acl: web
    rule_position: 1
    vpc: my vpc
    zone: zone01
    traffic_type: ingress
    action_policy: allow
    port: 80
    cidr: 0.0.0.0/0

- name: create a network ACL rule, deny port range 8000-9000 ingress for 10.20.0.0/16 and 10.22.0.0/16
  ngine_io.cloudstack.cs_network_acl_rule:
    network_acl: web
    rule_position: 1
    vpc: my vpc
    zone: zone01
    traffic_type: ingress
    action_policy: deny
    start_port: 8000
    end_port: 9000
    cidrs:
    - 10.20.0.0/16
    - 10.22.0.0/16

- name: remove a network ACL rule
  ngine_io.cloudstack.cs_network_acl_rule:
    network_acl: web
    rule_position: 1
    vpc: my vpc
    zone: zone01
    state: absent
```

## [Return Values](cs_network_acl_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the network ACL rule is related to.  **Returned:** success  **Sample:** `"example account"` |
| **action_policy**  string | Action policy of the network ACL rule.  **Returned:** success  **Sample:** `"deny"` |
| **cidr**  string | CIDR of the network ACL rule.  **Returned:** success  **Sample:** `"0.0.0.0/0"` |
| **cidrs**  list / elements=string | CIDRs of the network ACL rule.  **Returned:** success  **Sample:** `["0.0.0.0/0"]` |
| **domain**  string | Domain the network ACL rule is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **end_port**  integer | End port of the network ACL rule.  **Returned:** success  **Sample:** `80` |
| **icmp_code**  integer | ICMP code of the network ACL rule.  **Returned:** success  **Sample:** `8` |
| **icmp_type**  integer | ICMP type of the network ACL rule.  **Returned:** success  **Sample:** `0` |
| **network_acl**  string | Name of the network ACL.  **Returned:** success  **Sample:** `"customer acl"` |
| **project**  string | Name of project the network ACL rule is related to.  **Returned:** success  **Sample:** `"Production"` |
| **protocol**  string | Protocol of the network ACL rule.  **Returned:** success  **Sample:** `"tcp"` |
| **protocol_number**  integer | Protocol number in case protocol is by number.  **Returned:** success  **Sample:** `8` |
| **rule_position**  integer | Position of the network ACL rule.  **Returned:** success  **Sample:** `1` |
| **start_port**  integer | Start port of the network ACL rule.  **Returned:** success  **Sample:** `80` |
| **state**  string | State of the network ACL rule.  **Returned:** success  **Sample:** `"Active"` |
| **tags**  list / elements=string | List of resource tags associated with the network ACL rule.  **Returned:** success  **Sample:** `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **traffic_type**  string | Traffic type of the network ACL rule.  **Returned:** success  **Sample:** `"ingress"` |
| **vpc**  string | VPC of the network ACL.  **Returned:** success  **Sample:** `"customer vpc"` |
| **zone**  string | Zone the VPC is related to.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
