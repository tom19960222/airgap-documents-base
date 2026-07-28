---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_address module – Configure IPv4 addresses in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_address_module.html
fetched_at: 2026-07-28T02:24:14+00:00
---
# fortinet.fortios.fortios_firewall_address module – Configure IPv4 addresses in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_address_module.md#ansible-collections-fortinet-fortios-fortios-firewall-address-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_address`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_address_module.md#synopsis)
- [Requirements](fortios_firewall_address_module.md#requirements)
- [Parameters](fortios_firewall_address_module.md#parameters)
- [Notes](fortios_firewall_address_module.md#notes)
- [Examples](fortios_firewall_address_module.md#examples)
- [Return Values](fortios_firewall_address_module.md#return-values)

## [Synopsis](fortios_firewall_address_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and address category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_address**  dictionary | Configure IPv4 addresses. |
| **allow_routing**  string | Enable/disable use of this address in the static route configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **associated_interface**  string | Network interface associated with address. Source system.interface.name system.zone.name. |
| **cache_ttl**  integer | Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds. |
| **clearpass_spt**  string | SPT (System Posture Token) value.  **Choices:**   - `"unknown"` - `"healthy"` - `"quarantine"` - `"checkup"` - `"transient"` - `"infected"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **country**  string | IP addresses associated to a specific country. |
| **end_ip**  string | Final IP address (inclusive) in the range for the address. |
| **end_mac**  string | Last MAC address in the range. |
| **epg_name**  string | Endpoint group name. |
| **fabric_object**  string | Security Fabric global object setting.  **Choices:**   - `"enable"` - `"disable"` |
| **filter**  string | Match criteria filter. |
| **fqdn**  string | Fully Qualified Domain Name address. |
| **fsso_group**  list / elements=dictionary | FSSO group(s). |
| **name**  string / required | FSSO group name. Source user.adgrp.name. |
| **hw_model**  string | Dynamic address matching hardware model. |
| **hw_vendor**  string | Dynamic address matching hardware vendor. |
| **interface**  string | Name of interface whose IP address is to be used. Source system.interface.name. |
| **list**  list / elements=dictionary | IP address list. |
| **ip**  string / required | IP. |
| **net_id**  string | Network ID. |
| **obj_id**  string | Object ID. |
| **macaddr**  list / elements=dictionary | Multiple MAC address ranges. |
| **macaddr**  string / required | MAC address ranges <start>[-<end>] separated by space. |
| **name**  string / required | Address name. |
| **node_ip_only**  string | Enable/disable collection of node addresses only in Kubernetes.  **Choices:**   - `"enable"` - `"disable"` |
| **obj_id**  string | Object ID for NSX. |
| **obj_tag**  string | Tag of dynamic address object. |
| **obj_type**  string | Object type.  **Choices:**   - `"ip"` - `"mac"` |
| **organization**  string | Organization domain name (Syntax: organization/domain). |
| **os**  string | Dynamic address matching operating system. |
| **policy_group**  string | Policy group name. |
| **route_tag**  integer | route-tag address. |
| **sdn**  string | SDN. Source system.sdn-connector.name.  **Choices:**   - `"aci"` - `"aws"` - `"azure"` - `"gcp"` - `"nsx"` - `"nuage"` - `"oci"` - `"openstack"` |
| **sdn_addr_type**  string | Type of addresses to collect.  **Choices:**   - `"private"` - `"public"` - `"all"` |
| **sdn_tag**  string | SDN Tag. |
| **start_ip**  string | First IP address (inclusive) in the range for the address. |
| **start_mac**  string | First MAC address in the range. |
| **sub_type**  string | Sub-type of address.  **Choices:**   - `"sdn"` - `"clearpass-spt"` - `"fsso"` - `"ems-tag"` - `"fortivoice-tag"` - `"fortinac-tag"` - `"fortipolicy-tag"` - `"swc-tag"` - `"device-identification"` |
| **subnet**  string | IP address and subnet mask of address. |
| **subnet_name**  string | Subnet name. |
| **sw_version**  string | Dynamic address matching software version. |
| **tag_detection_level**  string | Tag detection level of dynamic address object. |
| **tag_type**  string | Tag type of dynamic address object. |
| **tagging**  list / elements=dictionary | Config object tagging. |
| **category**  string | Tag category. Source system.object-tagging.category. |
| **name**  string / required | Tagging entry name. |
| **tags**  list / elements=dictionary | Tags. |
| **name**  string / required | Tag name. Source system.object-tagging.tags.name. |
| **tenant**  string | Tenant. |
| **type**  string | Type of address.  **Choices:**   - `"ipmask"` - `"iprange"` - `"fqdn"` - `"geography"` - `"wildcard"` - `"dynamic"` - `"interface-subnet"` - `"mac"` - `"route-tag"` - `"wildcard-fqdn"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **visibility**  string | Enable/disable address visibility in the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **wildcard**  string | IP address and wildcard netmask. |
| **wildcard_fqdn**  string | Fully Qualified Domain Name with wildcard characters. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_address_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_address_module.md#id5)

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
  - name: Configure IPv4 addresses.
    fortios_firewall_address:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_address:
        allow_routing: "enable"
        associated_interface: "<your_own_value> (source system.interface.name system.zone.name)"
        cache_ttl: "0"
        clearpass_spt: "unknown"
        color: "0"
        comment: "Comment."
        country: "<your_own_value>"
        end_ip: "<your_own_value>"
        end_mac: "<your_own_value>"
        epg_name: "<your_own_value>"
        fabric_object: "enable"
        filter: "<your_own_value>"
        fqdn: "<your_own_value>"
        fsso_group:
         -
            name: "default_name_17 (source user.adgrp.name)"
        hw_model: "<your_own_value>"
        hw_vendor: "<your_own_value>"
        interface: "<your_own_value> (source system.interface.name)"
        list:
         -
            ip: "<your_own_value>"
            net_id: "<your_own_value>"
            obj_id: "<your_own_value>"
        macaddr:
         -
            macaddr: "<your_own_value>"
        name: "default_name_27"
        node_ip_only: "enable"
        obj_id: "<your_own_value>"
        obj_tag: "<your_own_value>"
        obj_type: "ip"
        organization: "<your_own_value>"
        os: "<your_own_value>"
        policy_group: "<your_own_value>"
        route_tag: "0"
        sdn: "aci"
        sdn_addr_type: "private"
        sdn_tag: "<your_own_value>"
        start_ip: "<your_own_value>"
        start_mac: "<your_own_value>"
        sub_type: "sdn"
        subnet: "<your_own_value>"
        subnet_name: "<your_own_value>"
        sw_version: "<your_own_value>"
        tag_detection_level: "<your_own_value>"
        tag_type: "<your_own_value>"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_49"
            tags:
             -
                name: "default_name_51 (source system.object-tagging.tags.name)"
        tenant: "<your_own_value>"
        type: "ipmask"
        uuid: "<your_own_value>"
        visibility: "enable"
        wildcard: "<your_own_value>"
        wildcard_fqdn: "<your_own_value>"
```

## [Return Values](fortios_firewall_address_module.md#id6)

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
