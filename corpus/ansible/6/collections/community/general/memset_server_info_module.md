---
collection: ansible
version: "6"
title: "community.general.memset_server_info module – Retrieve server information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/memset_server_info_module.html
fetched_at: 2026-07-27T17:10:55+00:00
---
# community.general.memset_server_info module – Retrieve server information

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.memset_server_info`.

- [Synopsis](memset_server_info_module.md#synopsis)
- [Parameters](memset_server_info_module.md#parameters)
- [Notes](memset_server_info_module.md#notes)
- [Examples](memset_server_info_module.md#examples)
- [Return Values](memset_server_info_module.md#return-values)

## [Synopsis](memset_server_info_module.md#id1)

- Retrieve server information.
- This module was called `memset_server_facts` before Ansible 2.9. The usage did not change.

## [Parameters](memset_server_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The API key obtained from the Memset control panel. |
| **name**  string / required | The server product name (i.e. `testyaa1`). |

## [Notes](memset_server_info_module.md#id3)

> **Note:**
>
> - An API key generated via the Memset customer control panel is needed with the following minimum scope - *server.info*.

## [Examples](memset_server_info_module.md#id4)

```yaml+jinja
- name: Get details for testyaa1
  community.general.memset_server_info:
    name: testyaa1
    api_key: 5eb86c9896ab03919abcf03857163741
  delegate_to: localhost
```

## [Return Values](memset_server_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **memset_api**  complex | Info from the Memset API  Returned: always |
| **backups**  boolean | Whether this server has a backup service.  Returned: always  Sample: `true` |
| **control_panel**  string | Whether the server has a control panel (i.e. cPanel).  Returned: always  Sample: `"cpanel"` |
| **data_zone**  string | The data zone the server is in.  Returned: always  Sample: `"Memset Public Cloud"` |
| **expiry_date**  string | Current expiry date of the server.  Returned: always  Sample: `"2018-08-10"` |
| **firewall_rule_group**  dictionary | Details about the firewall group this server is in.  Returned: always  Sample: `{"default_outbound_policy": "RETURN", "name": "testyaa-fw1", "nickname": "testyaa cPanel rules", "notes": "", "public": false, "rules": {"51d7db54d39c3544ef7c48baa0b9944f": {"action": "ACCEPT", "comment": "", "dest_ip6s": "any", "dest_ips": "any", "dest_ports": "any", "direction": "Inbound", "ip_version": "any", "ordering": 2, "protocols": "icmp", "rule_group_name": "testyaa-fw1", "rule_id": "51d7db54d39c3544ef7c48baa0b9944f", "source_ip6s": "any", "source_ips": "any", "source_ports": "any"}}}` |
| **firewall_type**  string | The type of firewall the server has (i.e. self-managed, managed).  Returned: always  Sample: `"managed"` |
| **host_name**  string | The server’s hostname.  Returned: always  Sample: `"testyaa1.miniserver.com"` |
| **ignore_monitoring_off**  boolean | When true, Memset won’t remind the customer that monitoring is disabled.  Returned: always  Sample: `true` |
| **ips**  list / elements=string | List of dictionaries of all IP addresses assigned to the server.  Returned: always  Sample: `[{"address": "1.2.3.4", "bytes_in_today": 1000.0, "bytes_in_yesterday": 2000.0, "bytes_out_today": 1000.0, "bytes_out_yesterday": 2000.0}]` |
| **monitor**  boolean | Whether the server has monitoring enabled.  Returned: always  Sample: `true` |
| **monitoring_level**  string | The server’s monitoring level (i.e. basic).  Returned: always  Sample: `"basic"` |
| **name**  string | Server name (same as the service name).  Returned: always  Sample: `"testyaa1"` |
| **network_zones**  list / elements=string | The network zone(s) the server is in.  Returned: always  Sample: `["reading"]` |
| **nickname**  string | Customer-set nickname for the server.  Returned: always  Sample: `"database server"` |
| **no_auto_reboot**  boolean | Whether or not to reboot the server if monitoring detects it down.  Returned: always  Sample: `true` |
| **no_nrpe**  boolean | Whether Memset should use NRPE to monitor this server.  Returned: always  Sample: `true` |
| **os**  string | The server’s Operating System.  Returned: always  Sample: `"debian_stretch_64"` |
| **penetration_patrol**  string | Intrusion detection support level for this server.  Returned: always  Sample: `"managed"` |
| **penetration_patrol_alert_level**  integer | The alert level at which notifications are sent.  Returned: always  Sample: `10` |
| **primary_ip**  string | Server’s primary IP.  Returned: always  Sample: `"1.2.3.4"` |
| **renewal_price_amount**  string | Renewal cost for the server.  Returned: always  Sample: `"30.00"` |
| **renewal_price_currency**  string | Currency for renewal payments.  Returned: always  Sample: `"GBP"` |
| **renewal_price_vat**  string | VAT rate for renewal payments  Returned: always  Sample: `"20"` |
| **start_date**  string | Server’s start date.  Returned: always  Sample: `"2013-04-10"` |
| **status**  string | Current status of the server (i.e. live, onhold).  Returned: always  Sample: `"LIVE"` |
| **support_level**  string | Support level included with the server.  Returned: always  Sample: `"managed"` |
| **type**  string | What this server is (i.e. dedicated)  Returned: always  Sample: `"miniserver"` |
| **vlans**  dictionary | Dictionary of tagged and untagged VLANs this server is in.  Returned: always  Sample: `{"tagged": [], "untagged": ["testyaa-vlan1", "testyaa-vlan2"]}` |
| **vulnscan**  string | Vulnerability scanning level.  Returned: always  Sample: `"basic"` |

### Authors

- Simon Weald (@glitchcrab)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
