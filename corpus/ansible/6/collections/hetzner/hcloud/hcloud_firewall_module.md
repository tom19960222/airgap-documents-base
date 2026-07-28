---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_firewall module – Create and manage firewalls on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_firewall_module.html
fetched_at: 2026-07-27T17:49:38+00:00
---
# hetzner.hcloud.hcloud_firewall module – Create and manage firewalls on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_firewall_module.md#ansible-collections-hetzner-hcloud-hcloud-firewall-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_firewall`.

- [Synopsis](hcloud_firewall_module.md#synopsis)
- [Requirements](hcloud_firewall_module.md#requirements)
- [Parameters](hcloud_firewall_module.md#parameters)
- [See Also](hcloud_firewall_module.md#see-also)
- [Examples](hcloud_firewall_module.md#examples)
- [Return Values](hcloud_firewall_module.md#return-values)

## [Synopsis](hcloud_firewall_module.md#id1)

- Create, update and manage firewalls on the Hetzner Cloud.

## [Requirements](hcloud_firewall_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_firewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Hetzner Cloud firewall to manage.  Only required if no firewall *name* is given |
| **labels**  dictionary | User-defined labels (key-value pairs) |
| **name**  string | The Name of the Hetzner Cloud firewall to manage.  Only required if no firewall *id* is given, or a firewall does not exist. |
| **rules**  list / elements=dictionary | List of rules the firewall should contain. |
| **description**  string | User defined description of this rule. |
| **destination_ips**  list / elements=string | List of CIDRs that are allowed within this rule  Default: `[]` |
| **direction**  string | The direction of the firewall rule.  Choices:   - `"in"` - `"out"` |
| **port**  string | The port of the firewall rule. |
| **protocol**  string | The protocol of the firewall rule.  Choices:   - `"icmp"` - `"tcp"` - `"udp"` - `"esp"` - `"gre"` |
| **source_ips**  list / elements=string | List of CIDRs that are allowed within this rule  Default: `[]` |
| **state**  string | State of the firewall.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_firewall_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_firewall_module.md#id5)

```yaml+jinja
- name: Create a basic firewall
  hcloud_firewall:
    name: my-firewall
    state: present

- name: Create a firewall with rules
  hcloud_firewall:
    name: my-firewall
    rules:
       - direction: in
         protocol: icmp
         source_ips:
           - 0.0.0.0/0
           - ::/0
         description: allow icmp in
    state: present

- name: Create a firewall with labels
  hcloud_firewall:
    name: my-firewall
    labels:
        key: value
        mylabel: 123
    state: present

- name: Ensure the firewall is absent (remove if needed)
  hcloud_firewall:
    name: my-firewall
    state: absent
```

## [Return Values](hcloud_firewall_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_firewall**  complex | The firewall instance  Returned: Always |
| **id**  integer | Numeric identifier of the firewall  Returned: always  Sample: `1937415` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: always |
| **name**  string | Name of the firewall  Returned: always  Sample: `"my firewall"` |
| **rules**  complex | List of Rules within this Firewall  Returned: always |
| **description**  string | User defined description of the Firewall Rule  Returned: always |
| **destination_ips**  list / elements=string | Source IPs of the Firewall  Returned: always |
| **direction**  string | Direction of the Firewall Rule  Returned: always  Sample: `"in"` |
| **port**  string | Port of the Firewall Rule, None/Null if protocol is icmp  Returned: always  Sample: `"in"` |
| **protocol**  string | Protocol of the Firewall Rule  Returned: always  Sample: `"icmp"` |
| **source_ips**  list / elements=string | Source IPs of the Firewall  Returned: always |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
