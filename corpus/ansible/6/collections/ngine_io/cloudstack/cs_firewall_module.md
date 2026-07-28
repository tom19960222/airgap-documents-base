---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_firewall module – Manages firewall rules on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_firewall_module.html
fetched_at: 2026-07-28T00:15:26+00:00
---
# ngine_io.cloudstack.cs_firewall module – Manages firewall rules on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_firewall_module.md#ansible-collections-ngine-io-cloudstack-cs-firewall-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_firewall`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_firewall_module.md#synopsis)
- [Requirements](cs_firewall_module.md#requirements)
- [Parameters](cs_firewall_module.md#parameters)
- [Notes](cs_firewall_module.md#notes)
- [Examples](cs_firewall_module.md#examples)
- [Return Values](cs_firewall_module.md#return-values)

## [Synopsis](cs_firewall_module.md#id1)

- Creates and removes firewall rules.

## [Requirements](cs_firewall_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_firewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the firewall rule is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidrs**  aliases: cidr  list / elements=string | List of CIDRs (full notation) to be used for firewall rule.  Since version 2.5, it is a list of CIDR.  Default: `["0.0.0.0/0"]` |
| **domain**  string | Domain the firewall rule is related to. |
| **end_port**  integer | End port for this rule. Considered if *protocol=tcp* or *protocol=udp*.  If not specified, equal *start_port*. |
| **icmp_code**  integer | Error code for this icmp message.  Considered if *protocol=icmp*. |
| **icmp_type**  integer | Type of the icmp message being sent.  Considered if *protocol=icmp*. |
| **ip_address**  string | Public IP address the ingress rule is assigned to.  Required if *type=ingress*. |
| **network**  string | Network the egress rule is related to.  Required if *type=egress*. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the firewall rule is related to. |
| **protocol**  string | Protocol of the firewall rule.  `all` is only available if *type=egress*.  Choices:   - `"tcp"` ← (default) - `"udp"` - `"icmp"` - `"all"` |
| **start_port**  aliases: port  integer | Start port for this rule.  Considered if *protocol=tcp* or *protocol=udp*. |
| **state**  string | State of the firewall rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set an empty list e.g. *tags: []*. |
| **type**  string | Type of the firewall rule.  Choices:   - `"ingress"` ← (default) - `"egress"` |
| **zone**  string / required | Name of the zone in which the virtual machine is in. |

## [Notes](cs_firewall_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_firewall_module.md#id5)

```yaml+jinja
- name: Allow inbound port 80/tcp from 1.2.3.4 to 4.3.2.1
  ngine_io.cloudstack.cs_firewall:
    ip_address: 4.3.2.1
    zone: zone01
    port: 80
    cidr: 1.2.3.4/32

- name: Allow inbound tcp/udp port 53 to 4.3.2.1
  ngine_io.cloudstack.cs_firewall:
    ip_address: 4.3.2.1
    zone: zone01
    port: 53
    protocol: '{{ item }}'
  with_items:
  - tcp
  - udp

- name: Ensure firewall rule is removed
  ngine_io.cloudstack.cs_firewall:
    ip_address: 4.3.2.1
    zone: zone01
    start_port: 8000
    end_port: 8888
    cidr: 17.0.0.0/8
    state: absent

- name: Allow all outbound traffic
  ngine_io.cloudstack.cs_firewall:
    network: my_network
    zone: zone01
    type: egress
    protocol: all

- name: Allow only HTTP outbound traffic for an IP
  ngine_io.cloudstack.cs_firewall:
    network: my_network
    zone: zone01
    type: egress
    port: 80
    cidr: 10.101.1.20
```

## [Return Values](cs_firewall_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cidr**  string | CIDR string of the rule.  Returned: success  Sample: `"0.0.0.0/0"` |
| **cidrs**  list / elements=string | CIDR list of the rule.  Returned: success  Sample: `["0.0.0.0/0"]` |
| **end_port**  integer | End port of the rule.  Returned: success  Sample: `80` |
| **icmp_code**  integer | ICMP code of the rule.  Returned: success  Sample: `1` |
| **icmp_type**  integer | ICMP type of the rule.  Returned: success  Sample: `1` |
| **id**  string | UUID of the rule.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **ip_address**  string | IP address of the rule if `type=ingress`  Returned: success  Sample: `"10.100.212.10"` |
| **network**  string | Name of the network if `type=egress`  Returned: success  Sample: `"my_network"` |
| **protocol**  string | Protocol of the rule.  Returned: success  Sample: `"tcp"` |
| **start_port**  integer | Start port of the rule.  Returned: success  Sample: `80` |
| **type**  string | Type of the rule.  Returned: success  Sample: `"ingress"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
