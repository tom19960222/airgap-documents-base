---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_securitygroup_rule module – Manages security group rules on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_securitygroup_rule_module.html
fetched_at: 2026-07-28T00:15:45+00:00
---
# ngine_io.cloudstack.cs_securitygroup_rule module – Manages security group rules on Apache CloudStack based clouds.

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
> see [Requirements](cs_securitygroup_rule_module.md#ansible-collections-ngine-io-cloudstack-cs-securitygroup-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_securitygroup_rule`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_securitygroup_rule_module.md#synopsis)
- [Requirements](cs_securitygroup_rule_module.md#requirements)
- [Parameters](cs_securitygroup_rule_module.md#parameters)
- [Notes](cs_securitygroup_rule_module.md#notes)
- [Examples](cs_securitygroup_rule_module.md#examples)
- [Return Values](cs_securitygroup_rule_module.md#return-values)

## [Synopsis](cs_securitygroup_rule_module.md#id1)

- Add and remove security group rules.

## [Requirements](cs_securitygroup_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_securitygroup_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidr**  string | CIDR (full notation) to be used for security group rule.  Default: `"0.0.0.0/0"` |
| **end_port**  integer | End port for this rule. Required if *protocol=tcp* or *protocol=udp*, but *start_port* will be used if not set. |
| **icmp_code**  integer | Error code for this icmp message. Required if *protocol=icmp*. |
| **icmp_type**  integer | Type of the icmp message being sent. Required if *protocol=icmp*. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the security group to be created in. |
| **protocol**  string | Protocol of the security group rule.  Choices:   - `"tcp"` ← (default) - `"udp"` - `"icmp"` - `"ah"` - `"esp"` - `"gre"` |
| **security_group**  string / required | Name of the security group the rule is related to. The security group must be existing. |
| **start_port**  aliases: port  integer | Start port for this rule. Required if *protocol=tcp* or *protocol=udp*. |
| **state**  string | State of the security group rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | Ingress or egress security group rule.  Choices:   - `"ingress"` ← (default) - `"egress"` |
| **user_security_group**  string | Security group this rule is based of. |

## [Notes](cs_securitygroup_rule_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_securitygroup_rule_module.md#id5)

```yaml+jinja
---
- name: allow inbound port 80/tcp from 1.2.3.4 added to security group 'default'
  ngine_io.cloudstack.cs_securitygroup_rule:
    security_group: default
    port: 80
    cidr: 1.2.3.4/32

- name: allow tcp/udp outbound added to security group 'default'
  ngine_io.cloudstack.cs_securitygroup_rule:
    security_group: default
    type: egress
    start_port: 1
    end_port: 65535
    protocol: '{{ item }}'
  with_items:
  - tcp
  - udp

- name: allow inbound icmp from 0.0.0.0/0 added to security group 'default'
  ngine_io.cloudstack.cs_securitygroup_rule:
    security_group: default
    protocol: icmp
    icmp_code: -1
    icmp_type: -1

- name: remove rule inbound port 80/tcp from 0.0.0.0/0 from security group 'default'
  ngine_io.cloudstack.cs_securitygroup_rule:
    security_group: default
    port: 80
    state: absent

- name: allow inbound port 80/tcp from security group web added to security group 'default'
  ngine_io.cloudstack.cs_securitygroup_rule:
    security_group: default
    port: 80
    user_security_group: web
```

## [Return Values](cs_securitygroup_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cidr**  string | CIDR of the rule.  Returned: success and cidr is defined  Sample: `"0.0.0.0/0"` |
| **end_port**  integer | end port of the rule.  Returned: success  Sample: `80` |
| **id**  string | UUID of the of the rule.  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **protocol**  string | protocol of the rule.  Returned: success  Sample: `"tcp"` |
| **security_group**  string | security group of the rule.  Returned: success  Sample: `"default"` |
| **start_port**  integer | start port of the rule.  Returned: success  Sample: `80` |
| **type**  string | type of the rule.  Returned: success  Sample: `"ingress"` |
| **user_security_group**  string | user security group of the rule.  Returned: success and user_security_group is defined  Sample: `"default"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
