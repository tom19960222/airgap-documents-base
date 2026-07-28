---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_snmp_user module – SNMP user configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_snmp_user_module.html
fetched_at: 2026-07-28T02:29:28+00:00
---
# fortinet.fortios.fortios_system_snmp_user module – SNMP user configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_snmp_user_module.md#ansible-collections-fortinet-fortios-fortios-system-snmp-user-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_snmp_user`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_snmp_user_module.md#synopsis)
- [Requirements](fortios_system_snmp_user_module.md#requirements)
- [Parameters](fortios_system_snmp_user_module.md#parameters)
- [Notes](fortios_system_snmp_user_module.md#notes)
- [Examples](fortios_system_snmp_user_module.md#examples)
- [Return Values](fortios_system_snmp_user_module.md#return-values)

## [Synopsis](fortios_system_snmp_user_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system_snmp feature and user category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_snmp_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_snmp_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_snmp_user**  dictionary | SNMP user configuration. |
| **auth_proto**  string | Authentication protocol.  **Choices:**   - `"md5"` - `"sha"` - `"sha224"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **auth_pwd**  string | Password for authentication protocol. |
| **events**  list / elements=string | SNMP notifications (traps) to send.  **Choices:**   - `"cpu-high"` - `"mem-low"` - `"log-full"` - `"intf-ip"` - `"vpn-tun-up"` - `"vpn-tun-down"` - `"ha-switch"` - `"ha-hb-failure"` - `"ips-signature"` - `"ips-anomaly"` - `"av-virus"` - `"av-oversize"` - `"av-pattern"` - `"av-fragmented"` - `"fm-if-change"` - `"fm-conf-change"` - `"bgp-established"` - `"bgp-backward-transition"` - `"ha-member-up"` - `"ha-member-down"` - `"ent-conf-change"` - `"av-conserve"` - `"av-bypass"` - `"av-oversize-passed"` - `"av-oversize-blocked"` - `"ips-pkg-update"` - `"ips-fail-open"` - `"faz-disconnect"` - `"faz"` - `"wc-ap-up"` - `"wc-ap-down"` - `"fswctl-session-up"` - `"fswctl-session-down"` - `"load-balance-real-server-down"` - `"device-new"` - `"per-cpu-high"` - `"dhcp"` - `"pool-usage"` - `"ospf-nbr-state-change"` - `"ospf-virtnbr-state-change"` - `"temperature-high"` - `"voltage-alert"` - `"power-supply-failure"` - `"fan-failure"` |
| **ha_direct**  string | Enable/disable direct management of HA cluster members.  **Choices:**   - `"enable"` - `"disable"` |
| **mib_view**  string | SNMP access control MIB view. Source system.snmp.mib-view.name. |
| **name**  string / required | SNMP user name. |
| **notify_hosts**  list / elements=string | SNMP managers to send notifications (traps) to. |
| **notify_hosts6**  list / elements=string | IPv6 SNMP managers to send notifications (traps) to. |
| **priv_proto**  string | Privacy (encryption) protocol.  **Choices:**   - `"aes"` - `"des"` - `"aes256"` - `"aes256cisco"` |
| **priv_pwd**  string | Password for privacy (encryption) protocol. |
| **queries**  string | Enable/disable SNMP queries for this user.  **Choices:**   - `"enable"` - `"disable"` |
| **query_port**  integer | SNMPv3 query port . |
| **security_level**  string | Security level for message authentication and encryption.  **Choices:**   - `"no-auth-no-priv"` - `"auth-no-priv"` - `"auth-priv"` |
| **source_ip**  string | Source IP for SNMP trap. |
| **source_ipv6**  string | Source IPv6 for SNMP trap. |
| **status**  string | Enable/disable this SNMP user.  **Choices:**   - `"enable"` - `"disable"` |
| **trap_lport**  integer | SNMPv3 local trap port . |
| **trap_rport**  integer | SNMPv3 trap remote port . |
| **trap_status**  string | Enable/disable traps for this SNMP user.  **Choices:**   - `"enable"` - `"disable"` |
| **vdoms**  list / elements=dictionary | SNMP access control VDOMs. |
| **name**  string / required | VDOM name. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_snmp_user_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_snmp_user_module.md#id5)

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
  - name: SNMP user configuration.
    fortios_system_snmp_user:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_snmp_user:
        auth_proto: "md5"
        auth_pwd: "<your_own_value>"
        events: "cpu-high"
        ha_direct: "enable"
        mib_view: "<your_own_value> (source system.snmp.mib-view.name)"
        name: "default_name_8"
        notify_hosts: "<your_own_value>"
        notify_hosts6: "<your_own_value>"
        priv_proto: "aes"
        priv_pwd: "<your_own_value>"
        queries: "enable"
        query_port: "161"
        security_level: "no-auth-no-priv"
        source_ip: "84.230.14.43"
        source_ipv6: "<your_own_value>"
        status: "enable"
        trap_lport: "162"
        trap_rport: "162"
        trap_status: "enable"
        vdoms:
         -
            name: "default_name_23 (source system.vdom.name)"
```

## [Return Values](fortios_system_snmp_user_module.md#id6)

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
