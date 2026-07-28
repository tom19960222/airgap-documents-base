---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_snmp_community module – SNMP community configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_snmp_community_module.html
fetched_at: 2026-07-28T02:29:25+00:00
---
# fortinet.fortios.fortios_system_snmp_community module – SNMP community configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_snmp_community_module.md#ansible-collections-fortinet-fortios-fortios-system-snmp-community-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_snmp_community`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_snmp_community_module.md#synopsis)
- [Requirements](fortios_system_snmp_community_module.md#requirements)
- [Parameters](fortios_system_snmp_community_module.md#parameters)
- [Notes](fortios_system_snmp_community_module.md#notes)
- [Examples](fortios_system_snmp_community_module.md#examples)
- [Return Values](fortios_system_snmp_community_module.md#return-values)

## [Synopsis](fortios_system_snmp_community_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system_snmp feature and community category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_snmp_community_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_snmp_community_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_snmp_community**  dictionary | SNMP community configuration. |
| **events**  list / elements=string | SNMP trap events.  **Choices:**   - `"cpu-high"` - `"mem-low"` - `"log-full"` - `"intf-ip"` - `"vpn-tun-up"` - `"vpn-tun-down"` - `"ha-switch"` - `"ha-hb-failure"` - `"ips-signature"` - `"ips-anomaly"` - `"av-virus"` - `"av-oversize"` - `"av-pattern"` - `"av-fragmented"` - `"fm-if-change"` - `"fm-conf-change"` - `"bgp-established"` - `"bgp-backward-transition"` - `"ha-member-up"` - `"ha-member-down"` - `"ent-conf-change"` - `"av-conserve"` - `"av-bypass"` - `"av-oversize-passed"` - `"av-oversize-blocked"` - `"ips-pkg-update"` - `"ips-fail-open"` - `"faz-disconnect"` - `"faz"` - `"wc-ap-up"` - `"wc-ap-down"` - `"fswctl-session-up"` - `"fswctl-session-down"` - `"load-balance-real-server-down"` - `"device-new"` - `"per-cpu-high"` - `"dhcp"` - `"pool-usage"` - `"ospf-nbr-state-change"` - `"ospf-virtnbr-state-change"` - `"temperature-high"` - `"voltage-alert"` - `"power-supply-failure"` - `"fan-failure"` |
| **hosts**  list / elements=dictionary | Configure IPv4 SNMP managers (hosts). |
| **ha_direct**  string | Enable/disable direct management of HA cluster members.  **Choices:**   - `"enable"` - `"disable"` |
| **host_type**  string | Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. No traps will be sent when IP type is subnet.  **Choices:**   - `"any"` - `"query"` - `"trap"` |
| **id**  integer / required | Host entry ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IPv4 address of the SNMP manager (host). |
| **source_ip**  string | Source IPv4 address for SNMP traps. |
| **hosts6**  list / elements=dictionary | Configure IPv6 SNMP managers. |
| **ha_direct**  string | Enable/disable direct management of HA cluster members.  **Choices:**   - `"enable"` - `"disable"` |
| **host_type**  string | Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both.  **Choices:**   - `"any"` - `"query"` - `"trap"` |
| **id**  integer / required | Host6 entry ID. see <a href=’#notes’>Notes</a>. |
| **ipv6**  string | SNMP manager IPv6 address prefix. |
| **source_ipv6**  string | Source IPv6 address for SNMP traps. |
| **id**  integer / required | Community ID. see <a href=’#notes’>Notes</a>. |
| **mib_view**  string | SNMP access control MIB view. Source system.snmp.mib-view.name. |
| **name**  string | Community name. |
| **query_v1_port**  integer | SNMP v1 query port . |
| **query_v1_status**  string | Enable/disable SNMP v1 queries.  **Choices:**   - `"enable"` - `"disable"` |
| **query_v2c_port**  integer | SNMP v2c query port . |
| **query_v2c_status**  string | Enable/disable SNMP v2c queries.  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable this SNMP community.  **Choices:**   - `"enable"` - `"disable"` |
| **trap_v1_lport**  integer | SNMP v1 trap local port . |
| **trap_v1_rport**  integer | SNMP v1 trap remote port . |
| **trap_v1_status**  string | Enable/disable SNMP v1 traps.  **Choices:**   - `"enable"` - `"disable"` |
| **trap_v2c_lport**  integer | SNMP v2c trap local port . |
| **trap_v2c_rport**  integer | SNMP v2c trap remote port . |
| **trap_v2c_status**  string | Enable/disable SNMP v2c traps.  **Choices:**   - `"enable"` - `"disable"` |
| **vdoms**  list / elements=dictionary | SNMP access control VDOMs. |
| **name**  string / required | VDOM name. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_snmp_community_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_snmp_community_module.md#id5)

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
  - name: SNMP community configuration.
    fortios_system_snmp_community:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_snmp_community:
        events: "cpu-high"
        hosts:
         -
            ha_direct: "enable"
            host_type: "any"
            id:  "7"
            ip: "<your_own_value>"
            source_ip: "84.230.14.43"
        hosts6:
         -
            ha_direct: "enable"
            host_type: "any"
            id:  "13"
            ipv6: "<your_own_value>"
            source_ipv6: "<your_own_value>"
        id:  "16"
        mib_view: "<your_own_value> (source system.snmp.mib-view.name)"
        name: "default_name_18"
        query_v1_port: "161"
        query_v1_status: "enable"
        query_v2c_port: "161"
        query_v2c_status: "enable"
        status: "enable"
        trap_v1_lport: "162"
        trap_v1_rport: "162"
        trap_v1_status: "enable"
        trap_v2c_lport: "162"
        trap_v2c_rport: "162"
        trap_v2c_status: "enable"
        vdoms:
         -
            name: "default_name_31 (source system.vdom.name)"
```

## [Return Values](fortios_system_snmp_community_module.md#id6)

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
