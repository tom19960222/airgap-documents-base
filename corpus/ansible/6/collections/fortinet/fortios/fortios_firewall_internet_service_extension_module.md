---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_internet_service_extension module – Configure Internet Services Extension in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_internet_service_extension_module.html
fetched_at: 2026-07-27T17:41:00+00:00
---
# fortinet.fortios.fortios_firewall_internet_service_extension module – Configure Internet Services Extension in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_internet_service_extension_module.md#ansible-collections-fortinet-fortios-fortios-firewall-internet-service-extension-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_internet_service_extension`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_internet_service_extension_module.md#synopsis)
- [Requirements](fortios_firewall_internet_service_extension_module.md#requirements)
- [Parameters](fortios_firewall_internet_service_extension_module.md#parameters)
- [Notes](fortios_firewall_internet_service_extension_module.md#notes)
- [Examples](fortios_firewall_internet_service_extension_module.md#examples)
- [Return Values](fortios_firewall_internet_service_extension_module.md#return-values)

## [Synopsis](fortios_firewall_internet_service_extension_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and internet_service_extension category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_internet_service_extension_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_internet_service_extension_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_internet_service_extension**  dictionary | Configure Internet Services Extension. |
| **comment**  string | Comment. |
| **disable_entry**  list / elements=dictionary | Disable entries in the Internet Service database. |
| **addr_mode**  string | Address mode (IPv4 or IPv6)  Choices:   - `"ipv4"` - `"ipv6"` |
| **id**  integer | Disable entry ID. |
| **ip6_range**  list / elements=dictionary | IPv6 ranges in the disable entry. |
| **end_ip6**  string | End IPv6 address. |
| **id**  integer | Disable entry range ID. |
| **start_ip6**  string | Start IPv6 address. |
| **ip_range**  list / elements=dictionary | IPv4 ranges in the disable entry. |
| **end_ip**  string | End IPv4 address. |
| **id**  integer | Disable entry range ID. |
| **start_ip**  string | Start IPv4 address. |
| **port_range**  list / elements=dictionary | Port ranges in the disable entry. |
| **end_port**  integer | Ending TCP/UDP/SCTP destination port (0 to 65535). |
| **id**  integer | Custom entry port range ID. |
| **start_port**  integer | Starting TCP/UDP/SCTP destination port (0 to 65535). |
| **protocol**  integer | Integer value for the protocol type as defined by IANA (0 - 255). |
| **entry**  list / elements=dictionary | Entries added to the Internet Service extension database. |
| **addr_mode**  string | Address mode (IPv4 or IPv6)  Choices:   - `"ipv4"` - `"ipv6"` |
| **dst**  list / elements=dictionary | Destination address or address group name. |
| **name**  string | Select the destination address or address group object from available options. Source firewall.address.name firewall .addrgrp.name. |
| **dst6**  list / elements=dictionary | Destination address6 or address6 group name. |
| **name**  string | Select the destination address6 or address group object from available options. Source . |
| **id**  integer | Entry ID(1-255). |
| **port_range**  list / elements=dictionary | Port ranges in the custom entry. |
| **end_port**  integer | Integer value for ending TCP/UDP/SCTP destination port in range (0 to 65535). |
| **id**  integer | Custom entry port range ID. |
| **start_port**  integer | Integer value for starting TCP/UDP/SCTP destination port in range (0 to 65535). |
| **protocol**  integer | Integer value for the protocol type as defined by IANA (0 - 255). |
| **id**  integer / required | Internet Service ID in the Internet Service database. Source firewall.internet-service.id. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_internet_service_extension_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_internet_service_extension_module.md#id5)

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
  - name: Configure Internet Services Extension.
    fortios_firewall_internet_service_extension:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_internet_service_extension:
        comment: "Comment."
        disable_entry:
         -
            addr_mode: "ipv4"
            id:  "6"
            ip_range:
             -
                end_ip: "<your_own_value>"
                id:  "9"
                start_ip: "<your_own_value>"
            ip6_range:
             -
                end_ip6: "<your_own_value>"
                id:  "13"
                start_ip6: "<your_own_value>"
            port_range:
             -
                end_port: "65535"
                id:  "17"
                start_port: "1"
            protocol: "0"
        entry:
         -
            addr_mode: "ipv4"
            dst:
             -
                name: "default_name_23 (source firewall.address.name firewall.addrgrp.name)"
            dst6:
             -
                name: "default_name_25 (source )"
            id:  "26"
            port_range:
             -
                end_port: "65535"
                id:  "29"
                start_port: "1"
            protocol: "0"
        id:  "32 (source firewall.internet-service.id)"
```

## [Return Values](fortios_firewall_internet_service_extension_module.md#id6)

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
