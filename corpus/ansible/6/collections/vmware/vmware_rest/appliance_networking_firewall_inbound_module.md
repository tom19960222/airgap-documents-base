---
collection: ansible
version: "6"
title: "vmware.vmware_rest.appliance_networking_firewall_inbound module – Set the ordered list of firewall rules to allow or deny traffic from one or more incoming IP addresses"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/appliance_networking_firewall_inbound_module.html
fetched_at: 2026-07-28T00:21:40+00:00
---
# vmware.vmware_rest.appliance_networking_firewall_inbound module – Set the ordered list of firewall rules to allow or deny traffic from one or more incoming IP addresses

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](appliance_networking_firewall_inbound_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-firewall-inbound-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.appliance_networking_firewall_inbound`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](appliance_networking_firewall_inbound_module.md#synopsis)
- [Requirements](appliance_networking_firewall_inbound_module.md#requirements)
- [Parameters](appliance_networking_firewall_inbound_module.md#parameters)
- [Notes](appliance_networking_firewall_inbound_module.md#notes)
- [Examples](appliance_networking_firewall_inbound_module.md#examples)
- [Return Values](appliance_networking_firewall_inbound_module.md#return-values)

## [Synopsis](appliance_networking_firewall_inbound_module.md#id1)

- Set the ordered list of firewall rules to allow or deny traffic from one or more incoming IP addresses. This overwrites the existing firewall rules and creates a new rule list. Within the list of traffic rules, rules are processed in order of appearance, from top to bottom. For example, the list of rules can be as follows: <table> <tr> <th>Address</th><th>Prefix</th><th>Interface Name</th><th>Policy</th> </tr> <tr> <td>10.112.0.1</td><td>0</td><td>\*</td><td>REJECT</td> </tr> <tr> <td>10.112.0.1</td><td>0</td><td>nic0</td><td>ACCEPT</td> </tr> </table> In the above example, the first rule drops all packets originating from 10.112.0.1 and<br> the second rule accepts all packets originating from 10.112.0.1 only on nic0. In effect, the second rule is always ignored which is not desired, hence the order has to be swapped. When a connection matches a firewall rule, further processing for the connection stops, and the appliance ignores any additional firewall rules you have set.

## [Requirements](appliance_networking_firewall_inbound_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](appliance_networking_firewall_inbound_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **rules**  list / elements=dictionary / required | List of address-based firewall rules. This parameter is mandatory.  Valid attributes are:  - `address` (str): IPv4 or IPv6 address. ([‘set’])  This key is required with [‘set’]. - `prefix` (int): CIDR prefix used to mask address. For example, an IPv4 prefix of 24 ignores the low-order 8 bits of address. ([‘set’])  This key is required with [‘set’]. - `policy` (str): `policy` Defines firewall rule policies. ([‘set’])  This key is required with [‘set’].    - Accepted values:      - ACCEPT     - IGNORE     - REJECT     - RETURN - `interface_name` (str): The interface to which this rule applies. An empty string indicates that the rule applies to all interfaces. ([‘set’]) |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | Choices:   - `"set"` ← (default) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](appliance_networking_firewall_inbound_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](appliance_networking_firewall_inbound_module.md#id5)

```yaml+jinja
- name: Ensure the rules parameter is mandatory
  vmware.vmware_rest.appliance_networking_firewall_inbound:
  register: result
  failed_when:
  - not(result.failed)
  - result.msg == 'missing required arguments: rules'

- name: Set a firewall rule
  vmware.vmware_rest.appliance_networking_firewall_inbound:
    rules:
    - address: 1.2.3.4
      prefix: 32
      policy: ACCEPT
  register: result
```

## [Return Values](appliance_networking_firewall_inbound_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_when_result**  integer | Ensure the rules parameter is mandatory  Returned: On success  Sample: `0` |
| **msg**  string | Ensure the rules parameter is mandatory  Returned: On success  Sample: `"missing required arguments: rules"` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
