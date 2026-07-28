---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_modem module – Configure MODEM in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_modem_module.html
fetched_at: 2026-07-28T02:28:45+00:00
---
# fortinet.fortios.fortios_system_modem module – Configure MODEM in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_modem_module.md#ansible-collections-fortinet-fortios-fortios-system-modem-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_modem`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_modem_module.md#synopsis)
- [Requirements](fortios_system_modem_module.md#requirements)
- [Parameters](fortios_system_modem_module.md#parameters)
- [Notes](fortios_system_modem_module.md#notes)
- [Examples](fortios_system_modem_module.md#examples)
- [Return Values](fortios_system_modem_module.md#return-values)

## [Synopsis](fortios_system_modem_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and modem category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_modem_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_modem_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_modem**  dictionary | Configure MODEM. |
| **action**  string | Dial up/stop MODEM.  **Choices:**   - `"dial"` - `"stop"` - `"none"` |
| **altmode**  string | Enable/disable altmode for installations using PPP in China.  **Choices:**   - `"enable"` - `"disable"` |
| **authtype1**  list / elements=string | Allowed authentication types for ISP 1.  **Choices:**   - `"pap"` - `"chap"` - `"mschap"` - `"mschapv2"` |
| **authtype2**  list / elements=string | Allowed authentication types for ISP 2.  **Choices:**   - `"pap"` - `"chap"` - `"mschap"` - `"mschapv2"` |
| **authtype3**  list / elements=string | Allowed authentication types for ISP 3.  **Choices:**   - `"pap"` - `"chap"` - `"mschap"` - `"mschapv2"` |
| **auto_dial**  string | Enable/disable auto-dial after a reboot or disconnection.  **Choices:**   - `"enable"` - `"disable"` |
| **connect_timeout**  integer | Connection completion timeout (30 - 255 sec). |
| **dial_cmd1**  string | Dial command (this is often an ATD or ATDT command). |
| **dial_cmd2**  string | Dial command (this is often an ATD or ATDT command). |
| **dial_cmd3**  string | Dial command (this is often an ATD or ATDT command). |
| **dial_on_demand**  string | Enable/disable to dial the modem when packets are routed to the modem interface.  **Choices:**   - `"enable"` - `"disable"` |
| **distance**  integer | Distance of learned routes (1 - 255). |
| **dont_send_CR1**  string | Do not send CR when connected (ISP1).  **Choices:**   - `"enable"` - `"disable"` |
| **dont_send_CR2**  string | Do not send CR when connected (ISP2).  **Choices:**   - `"enable"` - `"disable"` |
| **dont_send_CR3**  string | Do not send CR when connected (ISP3).  **Choices:**   - `"enable"` - `"disable"` |
| **extra_init1**  string | Extra initialization string to ISP 1. |
| **extra_init2**  string | Extra initialization string to ISP 2. |
| **extra_init3**  string | Extra initialization string to ISP 3. |
| **holddown_timer**  integer | Hold down timer in seconds (1 - 60 sec). |
| **idle_timer**  integer | MODEM connection idle time (1 - 9999 min). |
| **interface**  string | Name of redundant interface. Source system.interface.name. |
| **lockdown_lac**  string | Allow connection only to the specified Location Area Code (LAC). |
| **mode**  string | Set MODEM operation mode to redundant or standalone.  **Choices:**   - `"standalone"` - `"redundant"` |
| **network_init**  string | AT command to set the Network name/type (AT+COPS=<mode>,[<format>,<oper>[,<AcT>]]). |
| **passwd1**  string | Password to access the specified dialup account. |
| **passwd2**  string | Password to access the specified dialup account. |
| **passwd3**  string | Password to access the specified dialup account. |
| **peer_modem1**  string | Specify peer MODEM type for phone1.  **Choices:**   - `"generic"` - `"actiontec"` - `"ascend_TNT"` |
| **peer_modem2**  string | Specify peer MODEM type for phone2.  **Choices:**   - `"generic"` - `"actiontec"` - `"ascend_TNT"` |
| **peer_modem3**  string | Specify peer MODEM type for phone3.  **Choices:**   - `"generic"` - `"actiontec"` - `"ascend_TNT"` |
| **phone1**  string | Phone number to connect to the dialup account (must not contain spaces, and should include standard special characters). |
| **phone2**  string | Phone number to connect to the dialup account (must not contain spaces, and should include standard special characters). |
| **phone3**  string | Phone number to connect to the dialup account (must not contain spaces, and should include standard special characters). |
| **pin_init**  string | AT command to set the PIN (AT+PIN=<pin>). |
| **ppp_echo_request1**  string | Enable/disable PPP echo-request to ISP 1.  **Choices:**   - `"enable"` - `"disable"` |
| **ppp_echo_request2**  string | Enable/disable PPP echo-request to ISP 2.  **Choices:**   - `"enable"` - `"disable"` |
| **ppp_echo_request3**  string | Enable/disable PPP echo-request to ISP 3.  **Choices:**   - `"enable"` - `"disable"` |
| **priority**  integer | Priority of learned routes (1 - 65535). |
| **redial**  string | Redial limit (1 - 10 attempts, none = redial forever).  **Choices:**   - `"none"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` |
| **reset**  integer | Number of dial attempts before resetting modem (0 = never reset). |
| **status**  string | Enable/disable Modem support (equivalent to bringing an interface up or down).  **Choices:**   - `"enable"` - `"disable"` |
| **traffic_check**  string | Enable/disable traffic-check.  **Choices:**   - `"enable"` - `"disable"` |
| **username1**  string | User name to access the specified dialup account. |
| **username2**  string | User name to access the specified dialup account. |
| **username3**  string | User name to access the specified dialup account. |
| **wireless_port**  integer | Enter wireless port number: 0 for default, 1 for first port, and so on (0 - 4294967295). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_modem_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_modem_module.md#id5)

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
  - name: Configure MODEM.
    fortios_system_modem:
      vdom:  "{{ vdom }}"
      system_modem:
        action: "dial"
        altmode: "enable"
        authtype1: "pap"
        authtype2: "pap"
        authtype3: "pap"
        auto_dial: "enable"
        connect_timeout: "90"
        dial_cmd1: "<your_own_value>"
        dial_cmd2: "<your_own_value>"
        dial_cmd3: "<your_own_value>"
        dial_on_demand: "enable"
        distance: "1"
        dont_send_CR1: "enable"
        dont_send_CR2: "enable"
        dont_send_CR3: "enable"
        extra_init1: "<your_own_value>"
        extra_init2: "<your_own_value>"
        extra_init3: "<your_own_value>"
        holddown_timer: "60"
        idle_timer: "5"
        interface: "<your_own_value> (source system.interface.name)"
        lockdown_lac: "<your_own_value>"
        mode: "standalone"
        network_init: "<your_own_value>"
        passwd1: "<your_own_value>"
        passwd2: "<your_own_value>"
        passwd3: "<your_own_value>"
        peer_modem1: "generic"
        peer_modem2: "generic"
        peer_modem3: "generic"
        phone1: "<your_own_value>"
        phone2: "<your_own_value>"
        phone3: "<your_own_value>"
        pin_init: "<your_own_value>"
        ppp_echo_request1: "enable"
        ppp_echo_request2: "enable"
        ppp_echo_request3: "enable"
        priority: "1"
        redial: "none"
        reset: "0"
        status: "enable"
        traffic_check: "enable"
        username1: "<your_own_value>"
        username2: "<your_own_value>"
        username3: "<your_own_value>"
        wireless_port: "0"
```

## [Return Values](fortios_system_modem_module.md#id6)

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
