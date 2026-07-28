---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_extender_controller_dataplan module – FortiExtender dataplan configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_extender_controller_dataplan_module.html
fetched_at: 2026-07-28T02:23:59+00:00
---
# fortinet.fortios.fortios_extender_controller_dataplan module – FortiExtender dataplan configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_extender_controller_dataplan_module.md#ansible-collections-fortinet-fortios-fortios-extender-controller-dataplan-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_extender_controller_dataplan`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_extender_controller_dataplan_module.md#synopsis)
- [Requirements](fortios_extender_controller_dataplan_module.md#requirements)
- [Parameters](fortios_extender_controller_dataplan_module.md#parameters)
- [Notes](fortios_extender_controller_dataplan_module.md#notes)
- [Examples](fortios_extender_controller_dataplan_module.md#examples)
- [Return Values](fortios_extender_controller_dataplan_module.md#return-values)

## [Synopsis](fortios_extender_controller_dataplan_module.md#id3)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify extender_controller feature and dataplan category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_extender_controller_dataplan_module.md#id4)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_extender_controller_dataplan_module.md#id5)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **extender_controller_dataplan**  dictionary | FortiExtender dataplan configuration. |
| **APN**  string | APN configuration. |
| **apn**  string | APN configuration. |
| **auth_type**  string | Authentication type.  **Choices:**   - `"none"` - `"pap"` - `"chap"` |
| **billing_date**  integer | Billing day of the month (1 - 31). |
| **capacity**  integer | Capacity in MB (0 - 102400000). |
| **carrier**  string | Carrier configuration. |
| **iccid**  string | ICCID configuration. |
| **modem_id**  string | Dataplan”s modem specifics, if any.  **Choices:**   - `"modem1"` - `"modem2"` - `"all"` |
| **monthly_fee**  integer | Monthly fee of dataplan (0 - 100000, in local currency). |
| **name**  string / required | FortiExtender data plan name. |
| **overage**  string | Enable/disable dataplan overage detection.  **Choices:**   - `"disable"` - `"enable"` |
| **password**  string | Password. |
| **PDN**  string | PDN type.  **Choices:**   - `"ipv4-only"` - `"ipv6-only"` - `"ipv4-ipv6"` |
| **pdn**  string | PDN type.  **Choices:**   - `"ipv4-only"` - `"ipv6-only"` - `"ipv4-ipv6"` |
| **preferred_subnet**  integer | Preferred subnet mask (0 - 32). |
| **private_network**  string | Enable/disable dataplan private network support.  **Choices:**   - `"disable"` - `"enable"` |
| **signal_period**  integer | Signal period (600 to 18000 seconds). |
| **signal_threshold**  integer | Signal threshold. Specify the range between 50 - 100, where 50/100 means -50/-100 dBm. |
| **slot**  string | SIM slot configuration.  **Choices:**   - `"sim1"` - `"sim2"` |
| **type**  string | Type preferences configuration.  **Choices:**   - `"carrier"` - `"slot"` - `"iccid"` - `"generic"` |
| **username**  string | Username. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_extender_controller_dataplan_module.md#id6)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_extender_controller_dataplan_module.md#id7)

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
  - name: FortiExtender dataplan configuration.
    fortios_extender_controller_dataplan:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      extender_controller_dataplan:
        apn: "<your_own_value>"
        APN: "<your_own_value>"
        auth_type: "none"
        billing_date: "1"
        capacity: "0"
        carrier: "<your_own_value>"
        iccid: "<your_own_value>"
        modem_id: "modem1"
        monthly_fee: "0"
        name: "default_name_12"
        overage: "disable"
        password: "<your_own_value>"
        pdn: "ipv4-only"
        PDN: "ipv4-only"
        preferred_subnet: "32"
        private_network: "disable"
        signal_period: "3600"
        signal_threshold: "100"
        slot: "sim1"
        type: "carrier"
        username: "<your_own_value>"
```

## [Return Values](fortios_extender_controller_dataplan_module.md#id8)

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
