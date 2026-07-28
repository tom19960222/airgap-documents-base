---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_central_snat_map module – Configure IPv4 and IPv6 central SNAT policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_central_snat_map_module.html
fetched_at: 2026-07-27T17:40:45+00:00
---
# fortinet.fortios.fortios_firewall_central_snat_map module – Configure IPv4 and IPv6 central SNAT policies in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_firewall_central_snat_map_module.md#ansible-collections-fortinet-fortios-fortios-firewall-central-snat-map-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_central_snat_map`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_central_snat_map_module.md#synopsis)
- [Requirements](fortios_firewall_central_snat_map_module.md#requirements)
- [Parameters](fortios_firewall_central_snat_map_module.md#parameters)
- [Notes](fortios_firewall_central_snat_map_module.md#notes)
- [Examples](fortios_firewall_central_snat_map_module.md#examples)
- [Return Values](fortios_firewall_central_snat_map_module.md#return-values)

## [Synopsis](fortios_firewall_central_snat_map_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and central_snat_map category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_central_snat_map_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_central_snat_map_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **action**  string | the action indiactor to move an object in the list  Choices:   - `"move"` |
| **after**  string | mkey of target identifier |
| **before**  string | mkey of target identifier |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_central_snat_map**  dictionary | Configure IPv4 and IPv6 central SNAT policies. |
| **comments**  string | Comment. |
| **dst_addr**  list / elements=dictionary | IPv4 Destination address. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **dst_addr6**  list / elements=dictionary | IPv6 Destination address. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **dstintf**  list / elements=dictionary | Destination interface name from available interfaces. |
| **name**  string | Interface name. Source system.interface.name system.zone.name. |
| **nat**  string | Enable/disable source NAT.  Choices:   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  Choices:   - `"enable"` - `"disable"` |
| **nat64**  string | Enable/disable NAT64.  Choices:   - `"enable"` - `"disable"` |
| **nat_ippool**  list / elements=dictionary | Name of the IP pools to be used to translate addresses from available IP Pools. |
| **name**  string | IP pool name. Source firewall.ippool.name. |
| **nat_ippool6**  list / elements=dictionary | IPv6 pools to be used for source NAT. |
| **name**  string | IPv6 pool name. Source firewall.ippool6.name. |
| **nat_port**  string | Translated port or port range (1 to 65535, 0 means any port). |
| **orig_addr**  list / elements=dictionary | IPv4 Original address. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **orig_addr6**  list / elements=dictionary | IPv6 Original address. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **orig_port**  string | Original TCP port (1 to 65535, 0 means any port). |
| **policyid**  integer / required | Policy ID. |
| **protocol**  integer | Integer value for the protocol type (0 - 255). |
| **srcintf**  list / elements=dictionary | Source interface name from available interfaces. |
| **name**  string | Interface name. Source system.interface.name system.zone.name. |
| **status**  string | Enable/disable the active status of this policy.  Choices:   - `"enable"` - `"disable"` |
| **type**  string | IPv4/IPv6 source NAT.  Choices:   - `"ipv4"` - `"ipv6"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **self**  string | mkey of self identifier |
| **state**  string | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_central_snat_map_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks
> - Adjust object order by moving self after(before) another.
> - Only one of [after, before] must be specified when action is moving an object.

## [Examples](fortios_firewall_central_snat_map_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure IPv4 and IPv6 central SNAT policies.
    fortios_firewall_central_snat_map:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_central_snat_map:
        comments: "<your_own_value>"
        dst_addr:
         -
            name: "default_name_5 (source firewall.address.name firewall.addrgrp.name)"
        dst_addr6:
         -
            name: "default_name_7 (source firewall.address6.name firewall.addrgrp6.name)"
        dstintf:
         -
            name: "default_name_9 (source system.interface.name system.zone.name)"
        nat: "disable"
        nat_ippool:
         -
            name: "default_name_12 (source firewall.ippool.name)"
        nat_ippool6:
         -
            name: "default_name_14 (source firewall.ippool6.name)"
        nat_port: "<your_own_value>"
        nat46: "enable"
        nat64: "enable"
        orig_addr:
         -
            name: "default_name_19 (source firewall.address.name firewall.addrgrp.name)"
        orig_addr6:
         -
            name: "default_name_21 (source firewall.address6.name firewall.addrgrp6.name)"
        orig_port: "<your_own_value>"
        policyid: "0"
        protocol: "0"
        srcintf:
         -
            name: "default_name_26 (source system.interface.name system.zone.name)"
        status: "enable"
        type: "ipv4"
        uuid: "<your_own_value>"

  - name: move firewall.central_snat_map
    fortios_firewall_central_snat_map:
      vdom:  "root"
      action: "move"
      self: "<mkey of self identifier>"
      after: "<mkey of target identifier>"
     #before: "<mkey of target identifier>"
```

## [Return Values](fortios_firewall_central_snat_map_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
