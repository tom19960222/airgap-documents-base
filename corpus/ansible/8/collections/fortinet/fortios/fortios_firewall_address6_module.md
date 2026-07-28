---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_address6 module – Configure IPv6 firewall addresses in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_address6_module.html
fetched_at: 2026-07-28T02:24:15+00:00
---
# fortinet.fortios.fortios_firewall_address6 module – Configure IPv6 firewall addresses in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_firewall_address6_module.md#ansible-collections-fortinet-fortios-fortios-firewall-address6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_address6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_address6_module.md#synopsis)
- [Requirements](fortios_firewall_address6_module.md#requirements)
- [Parameters](fortios_firewall_address6_module.md#parameters)
- [Notes](fortios_firewall_address6_module.md#notes)
- [Examples](fortios_firewall_address6_module.md#examples)
- [Return Values](fortios_firewall_address6_module.md#return-values)

## [Synopsis](fortios_firewall_address6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and address6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_address6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_address6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_address6**  dictionary | Configure IPv6 firewall addresses. |
| **cache_ttl**  integer | Minimal TTL of individual IPv6 addresses in FQDN cache. |
| **color**  integer | Integer value to determine the color of the icon in the GUI (range 1 to 32). |
| **comment**  string | Comment. |
| **country**  string | IPv6 addresses associated to a specific country. |
| **end_ip**  string | Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). |
| **end_mac**  string | Last MAC address in the range. |
| **epg_name**  string | Endpoint group name. |
| **fabric_object**  string | Security Fabric global object setting.  **Choices:**   - `"enable"` - `"disable"` |
| **fqdn**  string | Fully qualified domain name. |
| **host**  string | Host Address. |
| **host_type**  string | Host type.  **Choices:**   - `"any"` - `"specific"` |
| **ip6**  string | IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx). |
| **list**  list / elements=dictionary | IP address list. |
| **ip**  string / required | IP. |
| **net_id**  string | Network ID. |
| **obj_id**  string | Object ID. |
| **macaddr**  list / elements=dictionary | Multiple MAC address ranges. |
| **macaddr**  string / required | MAC address ranges <start>[-<end>] separated by space. |
| **name**  string / required | Address name. |
| **obj_id**  string | Object ID for NSX. |
| **route_tag**  integer | route-tag address. |
| **sdn**  string | SDN. Source system.sdn-connector.name.  **Choices:**   - `"nsx"` |
| **sdn_tag**  string | SDN Tag. |
| **start_ip**  string | First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). |
| **start_mac**  string | First MAC address in the range. |
| **subnet_segment**  list / elements=dictionary | IPv6 subnet segments. |
| **name**  string / required | Name. |
| **type**  string | Subnet segment type.  **Choices:**   - `"any"` - `"specific"` |
| **value**  string | Subnet segment value. |
| **tagging**  list / elements=dictionary | Config object tagging. |
| **category**  string | Tag category. Source system.object-tagging.category. |
| **name**  string / required | Tagging entry name. |
| **tags**  list / elements=dictionary | Tags. |
| **name**  string / required | Tag name. Source system.object-tagging.tags.name. |
| **template**  string | IPv6 address template. Source firewall.address6-template.name. |
| **tenant**  string | Tenant. |
| **type**  string | Type of IPv6 address object .  **Choices:**   - `"ipprefix"` - `"iprange"` - `"fqdn"` - `"geography"` - `"dynamic"` - `"template"` - `"mac"` - `"route-tag"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **visibility**  string | Enable/disable the visibility of the object in the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_address6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_address6_module.md#id5)

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
  - name: Configure IPv6 firewall addresses.
    fortios_firewall_address6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_address6:
        cache_ttl: "0"
        color: "0"
        comment: "Comment."
        country: "<your_own_value>"
        end_ip: "<your_own_value>"
        end_mac: "<your_own_value>"
        epg_name: "<your_own_value>"
        fabric_object: "enable"
        fqdn: "<your_own_value>"
        host: "myhostname"
        host_type: "any"
        ip6: "<your_own_value>"
        list:
         -
            ip: "<your_own_value>"
            net_id: "<your_own_value>"
            obj_id: "<your_own_value>"
        macaddr:
         -
            macaddr: "<your_own_value>"
        name: "default_name_21"
        obj_id: "<your_own_value>"
        route_tag: "0"
        sdn: "nsx"
        sdn_tag: "<your_own_value>"
        start_ip: "<your_own_value>"
        start_mac: "<your_own_value>"
        subnet_segment:
         -
            name: "default_name_29"
            type: "any"
            value: "<your_own_value>"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_34"
            tags:
             -
                name: "default_name_36 (source system.object-tagging.tags.name)"
        template: "<your_own_value> (source firewall.address6-template.name)"
        tenant: "<your_own_value>"
        type: "ipprefix"
        uuid: "<your_own_value>"
        visibility: "enable"
```

## [Return Values](fortios_firewall_address6_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
