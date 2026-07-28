---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_extender_controller_extender_profile module – FortiExtender extender profile configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_extender_controller_extender_profile_module.html
fetched_at: 2026-07-28T02:24:01+00:00
---
# fortinet.fortios.fortios_extender_controller_extender_profile module – FortiExtender extender profile configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_extender_controller_extender_profile_module.md#ansible-collections-fortinet-fortios-fortios-extender-controller-extender-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_extender_controller_extender_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_extender_controller_extender_profile_module.md#synopsis)
- [Requirements](fortios_extender_controller_extender_profile_module.md#requirements)
- [Parameters](fortios_extender_controller_extender_profile_module.md#parameters)
- [Notes](fortios_extender_controller_extender_profile_module.md#notes)
- [Examples](fortios_extender_controller_extender_profile_module.md#examples)
- [Return Values](fortios_extender_controller_extender_profile_module.md#return-values)

## [Synopsis](fortios_extender_controller_extender_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify extender_controller feature and extender_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_extender_controller_extender_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_extender_controller_extender_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **extender_controller_extender_profile**  dictionary | FortiExtender extender profile configuration. |
| **allowaccess**  list / elements=string | Control management access to the managed extender. Separate entries with a space.  **Choices:**   - `"ping"` - `"telnet"` - `"http"` - `"https"` - `"ssh"` - `"snmp"` |
| **bandwidth_limit**  integer | FortiExtender LAN extension bandwidth limit (Mbps). |
| **cellular**  dictionary | FortiExtender cellular configuration. |
| **controller_report**  dictionary | FortiExtender controller report configuration. |
| **interval**  integer | Controller report interval. |
| **signal_threshold**  integer | Controller report signal threshold. |
| **status**  string | FortiExtender controller report status.  **Choices:**   - `"disable"` - `"enable"` |
| **dataplan**  list / elements=dictionary | Dataplan names. |
| **name**  string / required | Dataplan name. Source extender-controller.dataplan.name. |
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
| **preferred_carrier**  string | Preferred carrier. |
| **redundant_intf**  string | Redundant interface. |
| **redundant_mode**  string | FortiExtender mode.  **Choices:**   - `"disable"` - `"enable"` |
| **sim1_pin**  string | SIM  **Choices:**   - `"disable"` - `"enable"` |
| **sim1_pin_code**  string | SIM |
| **sim2_pin**  string | SIM  **Choices:**   - `"disable"` - `"enable"` |
| **sim2_pin_code**  string | SIM |
| **sms_notification**  dictionary | FortiExtender cellular SMS notification configuration. |
| **alert**  dictionary | SMS alert list. |
| **data_exhausted**  string | Display string when data exhausted. |
| **fgt_backup_mode_switch**  string | Display string when FortiGate backup mode switched. |
| **low_signal_strength**  string | Display string when signal strength is low. |
| **mode_switch**  string | Display string when mode is switched. |
| **os_image_fallback**  string | Display string when falling back to a previous OS image. |
| **session_disconnect**  string | Display string when session disconnected. |
| **system_reboot**  string | Display string when system rebooted. |
| **receiver**  list / elements=dictionary | SMS notification receiver list. |
| **alert**  list / elements=string | Alert multi-options.  **Choices:**   - `"system-reboot"` - `"data-exhausted"` - `"session-disconnect"` - `"low-signal-strength"` - `"mode-switch"` - `"os-image-fallback"` - `"fgt-backup-mode-switch"` |
| **name**  string / required | FortiExtender SMS notification receiver name. |
| **phone_number**  string | Receiver phone number. Format: [+][country code][area code][local phone number]. For example, +16501234567. |
| **status**  string | SMS notification receiver status.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | FortiExtender SMS notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **enforce_bandwidth**  string | Enable/disable enforcement of bandwidth on LAN extension interface.  **Choices:**   - `"enable"` - `"disable"` |
| **extension**  string | Extension option.  **Choices:**   - `"wan-extension"` - `"lan-extension"` |
| **id**  integer | ID. |
| **lan_extension**  dictionary | FortiExtender lan extension configuration. |
| **backhaul**  list / elements=dictionary | LAN extension backhaul tunnel configuration. |
| **name**  string / required | FortiExtender LAN extension backhaul name. |
| **port**  string | FortiExtender uplink port.  **Choices:**   - `"wan"` - `"lte1"` - `"lte2"` - `"port1"` - `"port2"` - `"port3"` - `"port4"` - `"port5"` - `"sfp"` |
| **role**  string | FortiExtender uplink port.  **Choices:**   - `"primary"` - `"secondary"` |
| **weight**  integer | WRR weight parameter. |
| **backhaul_interface**  string | IPsec phase1 interface. Source system.interface.name. |
| **backhaul_ip**  string | IPsec phase1 IPv4/FQDN. Used to specify the external IP/FQDN when the FortiGate unit is behind a NAT device. |
| **ipsec_tunnel**  string | IPsec tunnel name. |
| **link_loadbalance**  string | LAN extension link load balance strategy.  **Choices:**   - `"activebackup"` - `"loadbalance"` |
| **login_password**  string | Set the managed extender”s administrator password. |
| **login_password_change**  string | Change or reset the administrator password of a managed extender (yes, default, or no).  **Choices:**   - `"yes"` - `"default"` - `"no"` |
| **model**  string | Model.  **Choices:**   - `"FX201E"` - `"FX211E"` - `"FX200F"` - `"FXA11F"` - `"FXE11F"` - `"FXA21F"` - `"FXE21F"` - `"FXA22F"` - `"FXE22F"` - `"FX212F"` - `"FX311F"` - `"FX312F"` - `"FX511F"` - `"FVG21F"` - `"FVA21F"` - `"FVG22F"` - `"FVA22F"` - `"FX04DA"` - `"FX04DN"` - `"FX04DI"` |
| **name**  string / required | FortiExtender profile name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_extender_controller_extender_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_extender_controller_extender_profile_module.md#id5)

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
  - name: FortiExtender extender profile configuration.
    fortios_extender_controller_extender_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      extender_controller_extender_profile:
        allowaccess: "ping"
        bandwidth_limit: "1024"
        cellular:
            controller_report:
                interval: "300"
                signal_threshold: "10"
                status: "disable"
            dataplan:
             -
                name: "default_name_11 (source extender-controller.dataplan.name)"
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
                preferred_carrier: "<your_own_value>"
                redundant_intf: "<your_own_value>"
                redundant_mode: "disable"
                sim1_pin: "disable"
                sim1_pin_code: "<your_own_value>"
                sim2_pin: "disable"
                sim2_pin_code: "<your_own_value>"
            sms_notification:
                alert:
                    data_exhausted: "<your_own_value>"
                    fgt_backup_mode_switch: "<your_own_value>"
                    low_signal_strength: "<your_own_value>"
                    mode_switch: "<your_own_value>"
                    os_image_fallback: "<your_own_value>"
                    session_disconnect: "<your_own_value>"
                    system_reboot: "<your_own_value>"
                receiver:
                 -
                    alert: "system-reboot"
                    name: "default_name_63"
                    phone_number: "<your_own_value>"
                    status: "disable"
                status: "disable"
        enforce_bandwidth: "enable"
        extension: "wan-extension"
        id:  "69"
        lan_extension:
            backhaul:
             -
                name: "default_name_72"
                port: "wan"
                role: "primary"
                weight: "1"
            backhaul_interface: "<your_own_value> (source system.interface.name)"
            backhaul_ip: "<your_own_value>"
            ipsec_tunnel: "<your_own_value>"
            link_loadbalance: "activebackup"
        login_password: "<your_own_value>"
        login_password_change: "yes"
        model: "FX201E"
        name: "default_name_83"
```

## [Return Values](fortios_extender_controller_extender_profile_module.md#id6)

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
