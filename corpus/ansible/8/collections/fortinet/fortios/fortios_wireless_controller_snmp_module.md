---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_snmp module – Configure SNMP in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_snmp_module.html
fetched_at: 2026-07-28T02:31:23+00:00
---
# fortinet.fortios.fortios_wireless_controller_snmp module – Configure SNMP in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_snmp_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-snmp-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_snmp`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_snmp_module.md#synopsis)
- [Requirements](fortios_wireless_controller_snmp_module.md#requirements)
- [Parameters](fortios_wireless_controller_snmp_module.md#parameters)
- [Notes](fortios_wireless_controller_snmp_module.md#notes)
- [Examples](fortios_wireless_controller_snmp_module.md#examples)
- [Return Values](fortios_wireless_controller_snmp_module.md#return-values)

## [Synopsis](fortios_wireless_controller_snmp_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and snmp category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_snmp_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_snmp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_snmp**  dictionary | Configure SNMP. |
| **community**  list / elements=dictionary | SNMP Community Configuration. |
| **hosts**  list / elements=dictionary | Configure IPv4 SNMP managers (hosts). |
| **id**  integer / required | Host entry ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IPv4 address of the SNMP manager (host). |
| **id**  integer / required | Community ID. see <a href=’#notes’>Notes</a>. |
| **name**  string | Community name. |
| **query_v1_status**  string | Enable/disable SNMP v1 queries.  **Choices:**   - `"enable"` - `"disable"` |
| **query_v2c_status**  string | Enable/disable SNMP v2c queries.  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable this SNMP community.  **Choices:**   - `"enable"` - `"disable"` |
| **trap_v1_status**  string | Enable/disable SNMP v1 traps.  **Choices:**   - `"enable"` - `"disable"` |
| **trap_v2c_status**  string | Enable/disable SNMP v2c traps.  **Choices:**   - `"enable"` - `"disable"` |
| **contact_info**  string | Contact Information. |
| **engine_id**  string | AC SNMP engineID string (maximum 24 characters). |
| **trap_high_cpu_threshold**  integer | CPU usage when trap is sent. |
| **trap_high_mem_threshold**  integer | Memory usage when trap is sent. |
| **user**  list / elements=dictionary | SNMP User Configuration. |
| **auth_proto**  string | Authentication protocol.  **Choices:**   - `"md5"` - `"sha"` |
| **auth_pwd**  string | Password for authentication protocol. |
| **name**  string / required | SNMP user name. |
| **notify_hosts**  list / elements=string | Configure SNMP User Notify Hosts. |
| **priv_proto**  string | Privacy (encryption) protocol.  **Choices:**   - `"aes"` - `"des"` - `"aes256"` - `"aes256cisco"` |
| **priv_pwd**  string | Password for privacy (encryption) protocol. |
| **queries**  string | Enable/disable SNMP queries for this user.  **Choices:**   - `"enable"` - `"disable"` |
| **security_level**  string | Security level for message authentication and encryption.  **Choices:**   - `"no-auth-no-priv"` - `"auth-no-priv"` - `"auth-priv"` |
| **status**  string | SNMP user enable.  **Choices:**   - `"enable"` - `"disable"` |
| **trap_status**  string | Enable/disable traps for this SNMP user.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_wireless_controller_snmp_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_snmp_module.md#id5)

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
  - name: Configure SNMP.
    fortios_wireless_controller_snmp:
      vdom:  "{{ vdom }}"
      wireless_controller_snmp:
        community:
         -
            hosts:
             -
                id:  "5"
                ip: "<your_own_value>"
            id:  "7"
            name: "default_name_8"
            query_v1_status: "enable"
            query_v2c_status: "enable"
            status: "enable"
            trap_v1_status: "enable"
            trap_v2c_status: "enable"
        contact_info: "<your_own_value>"
        engine_id: "<your_own_value>"
        trap_high_cpu_threshold: "80"
        trap_high_mem_threshold: "80"
        user:
         -
            auth_proto: "md5"
            auth_pwd: "<your_own_value>"
            name: "default_name_21"
            notify_hosts: "<your_own_value>"
            priv_proto: "aes"
            priv_pwd: "<your_own_value>"
            queries: "enable"
            security_level: "no-auth-no-priv"
            status: "enable"
            trap_status: "enable"
```

## [Return Values](fortios_wireless_controller_snmp_module.md#id6)

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
