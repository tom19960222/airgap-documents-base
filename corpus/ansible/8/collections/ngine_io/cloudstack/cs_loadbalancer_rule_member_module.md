---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_loadbalancer_rule_member module – Manages load balancer rule members on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_loadbalancer_rule_member_module.html
fetched_at: 2026-07-28T02:45:59+00:00
---
# ngine_io.cloudstack.cs_loadbalancer_rule_member module – Manages load balancer rule members on Apache CloudStack based clouds.

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
> see [Requirements](cs_loadbalancer_rule_member_module.md#ansible-collections-ngine-io-cloudstack-cs-loadbalancer-rule-member-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_loadbalancer_rule_member`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_loadbalancer_rule_member_module.md#synopsis)
- [Requirements](cs_loadbalancer_rule_member_module.md#requirements)
- [Parameters](cs_loadbalancer_rule_member_module.md#parameters)
- [Notes](cs_loadbalancer_rule_member_module.md#notes)
- [Examples](cs_loadbalancer_rule_member_module.md#examples)
- [Return Values](cs_loadbalancer_rule_member_module.md#return-values)

## [Synopsis](cs_loadbalancer_rule_member_module.md#id1)

- Add and remove load balancer rule members.

## [Requirements](cs_loadbalancer_rule_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_loadbalancer_rule_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the rule is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the rule is related to. |
| **ip_address**  aliases: public_ip  string | Public IP address from where the network traffic will be load balanced from.  Only needed to find the rule if *name* is not unique. |
| **name**  string / required | The name of the load balancer rule. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the firewall rule is related to. |
| **state**  string | Should the VMs be present or absent from the rule.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vms**  aliases: vm  list / elements=string / required | List of VMs to assign to or remove from the rule. |
| **zone**  string | Name of the zone in which the rule should be located.  Required when the LB provider is ElasticLoadBalancerVm |

## [Notes](cs_loadbalancer_rule_member_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_loadbalancer_rule_member_module.md#id5)

```yaml+jinja
- name: Add VMs to an existing load balancer
  ngine_io.cloudstack.cs_loadbalancer_rule_member:
    name: balance_http
    vms:
      - web01
      - web02

- name: Remove a VM from an existing load balancer
  ngine_io.cloudstack.cs_loadbalancer_rule_member:
    name: balance_http
    vms:
      - web01
      - web02
    state: absent

# Rolling upgrade of hosts
- hosts: webservers
  serial: 1
  pre_tasks:
    - name: Remove from load balancer
      ngine_io.cloudstack.cs_loadbalancer_rule_member:
        name: balance_http
        vm: "{{ ansible_hostname }}"
        state: absent
  tasks:
    # Perform update
  post_tasks:
    - name: Add to load balancer
      ngine_io.cloudstack.cs_loadbalancer_rule_member:
        name: balance_http
        vm: "{{ ansible_hostname }}"
        state: present
```

## [Return Values](cs_loadbalancer_rule_member_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the rule is related to.  **Returned:** success  **Sample:** `"example account"` |
| **algorithm**  string | Load balancer algorithm used.  **Returned:** success  **Sample:** `"source"` |
| **cidr**  string | CIDR to forward traffic from.  **Returned:** success  **Sample:** `"0.0.0.0/0"` |
| **description**  string | Description of the rule.  **Returned:** success  **Sample:** `"http load balancer rule"` |
| **domain**  string | Domain the rule is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the rule.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **name**  string | Name of the rule.  **Returned:** success  **Sample:** `"http-lb"` |
| **private_port**  integer | Private IP address.  **Returned:** success  **Sample:** `80` |
| **project**  string | Name of project the rule is related to.  **Returned:** success  **Sample:** `"Production"` |
| **protocol**  string | Protocol of the rule.  **Returned:** success  **Sample:** `"tcp"` |
| **public_ip**  string | Public IP address.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **public_port**  integer | Public port.  **Returned:** success  **Sample:** `80` |
| **state**  string | State of the rule.  **Returned:** success  **Sample:** `"Add"` |
| **tags**  list / elements=string | List of resource tags associated with the rule.  **Returned:** success  **Sample:** `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **vms**  list / elements=string | Rule members.  **Returned:** success  **Sample:** `["[ \"web01\"", " \"web02\" ]"]` |
| **zone**  string | Name of zone the rule is related to.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- Darren Worrall (@dazworrall)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
