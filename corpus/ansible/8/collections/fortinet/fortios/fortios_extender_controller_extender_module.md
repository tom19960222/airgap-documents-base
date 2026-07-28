---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_extender_controller_extender module – Extender controller configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_extender_controller_extender_module.html
fetched_at: 2026-07-28T02:24:00+00:00
---
# fortinet.fortios.fortios_extender_controller_extender module – Extender controller configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_extender_controller_extender_module.md#ansible-collections-fortinet-fortios-fortios-extender-controller-extender-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_extender_controller_extender`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_extender_controller_extender_module.md#synopsis)
- [Requirements](fortios_extender_controller_extender_module.md#requirements)
- [Parameters](fortios_extender_controller_extender_module.md#parameters)
- [Notes](fortios_extender_controller_extender_module.md#notes)
- [Examples](fortios_extender_controller_extender_module.md#examples)
- [Return Values](fortios_extender_controller_extender_module.md#return-values)

## [Synopsis](fortios_extender_controller_extender_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify extender_controller feature and extender category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_extender_controller_extender_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_extender_controller_extender_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **extender_controller_extender**  dictionary | Extender controller configuration. |
| **aaa_shared_secret**  string | AAA shared secret. |
| **access_point_name**  string | Access point name(APN). |
| **admin**  string | FortiExtender Administration (enable or disable).  **Choices:**   - `"disable"` - `"discovered"` - `"enable"` |
| **allowaccess**  list / elements=string | Control management access to the managed extender. Separate entries with a space.  **Choices:**   - `"ping"` - `"telnet"` - `"http"` - `"https"` - `"ssh"` - `"snmp"` |
| **at_dial_script**  string | Initialization AT commands specific to the MODEM. |
| **authorized**  string | FortiExtender Administration (enable or disable).  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth_limit**  integer | FortiExtender LAN extension bandwidth limit (Mbps). |
| **billing_start_day**  integer | Billing start day. |
| **cdma_aaa_spi**  string | CDMA AAA SPI. |
| **cdma_ha_spi**  string | CDMA HA SPI. |
| **cdma_nai**  string | NAI for CDMA MODEMS. |
| **conn_status**  integer | Connection status. |
| **controller_report**  dictionary | FortiExtender controller report configuration. |
| **interval**  integer | Controller report interval. |
| **signal_threshold**  integer | Controller report signal threshold. |
| **status**  string | FortiExtender controller report status.  **Choices:**   - `"disable"` - `"enable"` |
| **description**  string | Description. |
| **device_id**  integer | Device ID. |
| **dial_mode**  string | Dial mode (dial-on-demand or always-connect).  **Choices:**   - `"dial-on-demand"` - `"always-connect"` |
| **dial_status**  integer | Dial status. |
| **enforce_bandwidth**  string | Enable/disable enforcement of bandwidth on LAN extension interface.  **Choices:**   - `"enable"` - `"disable"` |
| **ext_name**  string | FortiExtender name. |
| **extension_type**  string | Extension type for this FortiExtender.  **Choices:**   - `"wan-extension"` - `"lan-extension"` |
| **ha_shared_secret**  string | HA shared secret. |
| **id**  string | FortiExtender serial number. |
| **ifname**  string | FortiExtender interface name. Source system.interface.name. |
| **initiated_update**  string | Allow/disallow network initiated updates to the MODEM.  **Choices:**   - `"enable"` - `"disable"` |
| **login_password**  string | Set the managed extender”s administrator password. |
| **login_password_change**  string | Change or reset the administrator password of a managed extender (yes, default, or no).  **Choices:**   - `"yes"` - `"default"` - `"no"` |
| **mode**  string | FortiExtender mode.  **Choices:**   - `"standalone"` - `"redundant"` |
| **modem1**  dictionary | Configuration options for modem 1. |
| **auto_switch**  dictionary | FortiExtender auto switch configuration. |
| **dataplan**  string | Automatically switch based on data usage.  **Choices:**   - `"disable"` - `"enable"` |
| **disconnect**  string | Auto switch by disconnect.  **Choices:**   - `"disable"` - `"enable"` |
| **disconnect_period**  integer | Automatically switch based on disconnect period. |
| **disconnect_threshold**  integer | Automatically switch based on disconnect threshold. |
| **signal**  string | Automatically switch based on signal strength.  **Choices:**   - `"disable"` - `"enable"` |
| **switch_back**  list / elements=string | Auto switch with switch back multi-options.  **Choices:**   - `"time"` - `"timer"` |
| **switch_back_time**  string | Automatically switch over to preferred SIM/carrier at a specified time in UTC (HH:MM). |
| **switch_back_timer**  integer | Automatically switch over to preferred SIM/carrier after the given time (3600 - 2147483647 sec). |
| **conn_status**  integer | Connection status. |
| **default_sim**  string | Default SIM selection.  **Choices:**   - `"sim1"` - `"sim2"` - `"carrier"` - `"cost"` |
| **gps**  string | FortiExtender GPS enable/disable.  **Choices:**   - `"disable"` - `"enable"` |
| **ifname**  string | FortiExtender interface name. Source system.interface.name. |
| **preferred_carrier**  string | Preferred carrier. |
| **redundant_intf**  string | Redundant interface. |
| **redundant_mode**  string | FortiExtender mode.  **Choices:**   - `"disable"` - `"enable"` |
| **sim1_pin**  string | SIM  **Choices:**   - `"disable"` - `"enable"` |
| **sim1_pin_code**  string | SIM |
| **sim2_pin**  string | SIM  **Choices:**   - `"disable"` - `"enable"` |
| **sim2_pin_code**  string | SIM |
| **modem2**  dictionary | Configuration options for modem 2. |
| **auto_switch**  dictionary | FortiExtender auto switch configuration. |
| **dataplan**  string | Automatically switch based on data usage.  **Choices:**   - `"disable"` - `"enable"` |
| **disconnect**  string | Auto switch by disconnect.  **Choices:**   - `"disable"` - `"enable"` |
| **disconnect_period**  integer | Automatically switch based on disconnect period. |
| **disconnect_threshold**  integer | Automatically switch based on disconnect threshold. |
| **signal**  string | Automatically switch based on signal strength.  **Choices:**   - `"disable"` - `"enable"` |
| **switch_back**  list / elements=string | Auto switch with switch back multi-options.  **Choices:**   - `"time"` - `"timer"` |
| **switch_back_time**  string | Automatically switch over to preferred SIM/carrier at a specified time in UTC (HH:MM). |
| **switch_back_timer**  integer | Automatically switch over to preferred SIM/carrier after the given time (3600 - 2147483647 sec). |
| **conn_status**  integer | Connection status. |
| **default_sim**  string | Default SIM selection.  **Choices:**   - `"sim1"` - `"sim2"` - `"carrier"` - `"cost"` |
| **gps**  string | FortiExtender GPS enable/disable.  **Choices:**   - `"disable"` - `"enable"` |
| **ifname**  string | FortiExtender interface name. Source system.interface.name. |
| **preferred_carrier**  string | Preferred carrier. |
| **redundant_intf**  string | Redundant interface. |
| **redundant_mode**  string | FortiExtender mode.  **Choices:**   - `"disable"` - `"enable"` |
| **sim1_pin**  string | SIM  **Choices:**   - `"disable"` - `"enable"` |
| **sim1_pin_code**  string | SIM |
| **sim2_pin**  string | SIM  **Choices:**   - `"disable"` - `"enable"` |
| **sim2_pin_code**  string | SIM |
| **modem_passwd**  string | MODEM password. |
| **modem_type**  string | MODEM type (CDMA, GSM/LTE or WIMAX).  **Choices:**   - `"cdma"` - `"gsm/lte"` - `"wimax"` |
| **multi_mode**  string | MODEM mode of operation(3G,LTE,etc).  **Choices:**   - `"auto"` - `"auto-3g"` - `"force-lte"` - `"force-3g"` - `"force-2g"` |
| **name**  string / required | FortiExtender entry name. |
| **override_allowaccess**  string | Enable to override the extender profile management access configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_enforce_bandwidth**  string | Enable to override the extender profile enforce-bandwidth setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_login_password_change**  string | Enable to override the extender profile login-password (administrator password) setting.  **Choices:**   - `"enable"` - `"disable"` |
| **ppp_auth_protocol**  string | PPP authentication protocol (PAP,CHAP or auto).  **Choices:**   - `"auto"` - `"pap"` - `"chap"` |
| **ppp_echo_request**  string | Enable/disable PPP echo request.  **Choices:**   - `"enable"` - `"disable"` |
| **ppp_password**  string | PPP password. |
| **ppp_username**  string | PPP username. |
| **primary_ha**  string | Primary HA. |
| **profile**  string | FortiExtender profile configuration. Source extender-controller.extender-profile.name. |
| **quota_limit_mb**  integer | Monthly quota limit (MB). |
| **redial**  string | Number of redials allowed based on failed attempts.  **Choices:**   - `"none"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` |
| **redundant_intf**  string | Redundant interface. |
| **roaming**  string | Enable/disable MODEM roaming.  **Choices:**   - `"enable"` - `"disable"` |
| **role**  string | FortiExtender work role(Primary, Secondary, None).  **Choices:**   - `"none"` - `"primary"` - `"secondary"` |
| **secondary_ha**  string | Secondary HA. |
| **sim_pin**  string | SIM PIN. |
| **vdom**  integer | VDOM. |
| **wan_extension**  dictionary | FortiExtender wan extension configuration. |
| **modem1_extension**  string | FortiExtender interface name. Source system.interface.name. |
| **modem2_extension**  string | FortiExtender interface name. Source system.interface.name. |
| **wimax_auth_protocol**  string | WiMax authentication protocol(TLS or TTLS).  **Choices:**   - `"tls"` - `"ttls"` |
| **wimax_carrier**  string | WiMax carrier. |
| **wimax_realm**  string | WiMax realm. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_extender_controller_extender_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_extender_controller_extender_module.md#id5)

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
  - name: Extender controller configuration.
    fortios_extender_controller_extender:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      extender_controller_extender:
        aaa_shared_secret: "<your_own_value>"
        access_point_name: "<your_own_value>"
        admin: "disable"
        allowaccess: "ping"
        at_dial_script: "<your_own_value>"
        authorized: "disable"
        bandwidth_limit: "1024"
        billing_start_day: "14"
        cdma_aaa_spi: "<your_own_value>"
        cdma_ha_spi: "<your_own_value>"
        cdma_nai: "<your_own_value>"
        conn_status: "2147483647"
        controller_report:
            interval: "300"
            signal_threshold: "10"
            status: "disable"
        description: "<your_own_value>"
        device_id: "1024"
        dial_mode: "dial-on-demand"
        dial_status: "2147483647"
        enforce_bandwidth: "enable"
        ext_name: "<your_own_value>"
        extension_type: "wan-extension"
        ha_shared_secret: "<your_own_value>"
        id:  "27"
        ifname: "<your_own_value> (source system.interface.name)"
        initiated_update: "enable"
        login_password: "<your_own_value>"
        login_password_change: "yes"
        mode: "standalone"
        modem_passwd: "<your_own_value>"
        modem_type: "cdma"
        modem1:
            auto_switch:
                dataplan: "disable"
                disconnect: "disable"
                disconnect_period: "600"
                disconnect_threshold: "3"
                signal: "disable"
                switch_back: "time"
                switch_back_time: "<your_own_value>"
                switch_back_timer: "86400"
            conn_status: "0"
            default_sim: "sim1"
            gps: "disable"
            ifname: "<your_own_value> (source system.interface.name)"
            preferred_carrier: "<your_own_value>"
            redundant_intf: "<your_own_value>"
            redundant_mode: "disable"
            sim1_pin: "disable"
            sim1_pin_code: "<your_own_value>"
            sim2_pin: "disable"
            sim2_pin_code: "<your_own_value>"
        modem2:
            auto_switch:
                dataplan: "disable"
                disconnect: "disable"
                disconnect_period: "600"
                disconnect_threshold: "3"
                signal: "disable"
                switch_back: "time"
                switch_back_time: "<your_own_value>"
                switch_back_timer: "86400"
            conn_status: "0"
            default_sim: "sim1"
            gps: "disable"
            ifname: "<your_own_value> (source system.interface.name)"
            preferred_carrier: "<your_own_value>"
            redundant_intf: "<your_own_value>"
            redundant_mode: "disable"
            sim1_pin: "disable"
            sim1_pin_code: "<your_own_value>"
            sim2_pin: "disable"
            sim2_pin_code: "<your_own_value>"
        multi_mode: "auto"
        name: "default_name_78"
        override_allowaccess: "enable"
        override_enforce_bandwidth: "enable"
        override_login_password_change: "enable"
        ppp_auth_protocol: "auto"
        ppp_echo_request: "enable"
        ppp_password: "<your_own_value>"
        ppp_username: "<your_own_value>"
        primary_ha: "<your_own_value>"
        profile: "<your_own_value> (source extender-controller.extender-profile.name)"
        quota_limit_mb: "5242880"
        redial: "none"
        redundant_intf: "<your_own_value>"
        roaming: "enable"
        role: "none"
        secondary_ha: "<your_own_value>"
        sim_pin: "<your_own_value>"
        vdom: "0"
        wan_extension:
            modem1_extension: "<your_own_value> (source system.interface.name)"
            modem2_extension: "<your_own_value> (source system.interface.name)"
        wimax_auth_protocol: "tls"
        wimax_carrier: "<your_own_value>"
        wimax_realm: "<your_own_value>"
```

## [Return Values](fortios_extender_controller_extender_module.md#id6)

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
