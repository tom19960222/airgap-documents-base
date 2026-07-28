---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_central_management module – Configure central management in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_central_management_module.html
fetched_at: 2026-07-27T17:44:15+00:00
---
# fortinet.fortios.fortios_system_central_management module – Configure central management in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_central_management_module.md#ansible-collections-fortinet-fortios-fortios-system-central-management-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_central_management`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_central_management_module.md#synopsis)
- [Requirements](fortios_system_central_management_module.md#requirements)
- [Parameters](fortios_system_central_management_module.md#parameters)
- [Notes](fortios_system_central_management_module.md#notes)
- [Examples](fortios_system_central_management_module.md#examples)
- [Return Values](fortios_system_central_management_module.md#return-values)

## [Synopsis](fortios_system_central_management_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and central_management category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_central_management_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_central_management_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **system_central_management**  dictionary | Configure central management. |
| **allow_monitor**  string | Enable/disable allowing the central management server to remotely monitor this FortiGate unit.  Choices:   - `"enable"` - `"disable"` |
| **allow_push_configuration**  string | Enable/disable allowing the central management server to push configuration changes to this FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **allow_push_firmware**  string | Enable/disable allowing the central management server to push firmware updates to this FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **allow_remote_firmware_upgrade**  string | Enable/disable remotely upgrading the firmware on this FortiGate from the central management server.  Choices:   - `"enable"` - `"disable"` |
| **ca_cert**  string | CA certificate to be used by FGFM protocol. |
| **enc_algorithm**  string | Encryption strength for communications between the FortiGate and central management.  Choices:   - `"default"` - `"high"` - `"low"` |
| **fmg**  string | IP address or FQDN of the FortiManager. |
| **fmg_source_ip**  string | IPv4 source address that this FortiGate uses when communicating with FortiManager. |
| **fmg_source_ip6**  string | IPv6 source address that this FortiGate uses when communicating with FortiManager. |
| **fmg_update_port**  string | Port used to communicate with FortiManager that is acting as a FortiGuard update server.  Choices:   - `"8890"` - `"443"` |
| **include_default_servers**  string | Enable/disable inclusion of public FortiGuard servers in the override server list.  Choices:   - `"enable"` - `"disable"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **local_cert**  string | Certificate to be used by FGFM protocol. |
| **mode**  string | Central management mode.  Choices:   - `"normal"` - `"backup"` |
| **schedule_config_restore**  string | Enable/disable allowing the central management server to restore the configuration of this FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **schedule_script_restore**  string | Enable/disable allowing the central management server to restore the scripts stored on this FortiGate.  Choices:   - `"enable"` - `"disable"` |
| **serial_number**  string | Serial number. |
| **server_list**  list / elements=dictionary | Additional severs that the FortiGate can use for updates (for AV, IPS, updates) and ratings (for web filter and antispam ratings) servers. |
| **addr_type**  string | Indicate whether the FortiGate communicates with the override server using an IPv4 address, an IPv6 address or a FQDN.  Choices:   - `"ipv4"` - `"ipv6"` - `"fqdn"` |
| **fqdn**  string | FQDN address of override server. |
| **id**  integer | ID. |
| **server_address**  string | IPv4 address of override server. |
| **server_address6**  string | IPv6 address of override server. |
| **server_type**  list / elements=string | FortiGuard service type.  Choices:   - `"update"` - `"rating"` - `"iot-query"` - `"iot-collect"` |
| **type**  string | Central management type.  Choices:   - `"fortimanager"` - `"fortiguard"` - `"none"` |
| **vdom**  string | Virtual domain (VDOM) name to use when communicating with FortiManager. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_central_management_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_central_management_module.md#id5)

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
  - name: Configure central management.
    fortios_system_central_management:
      vdom:  "{{ vdom }}"
      system_central_management:
        allow_monitor: "enable"
        allow_push_configuration: "enable"
        allow_push_firmware: "enable"
        allow_remote_firmware_upgrade: "enable"
        ca_cert: "<your_own_value>"
        enc_algorithm: "default"
        fmg: "<your_own_value>"
        fmg_source_ip: "<your_own_value>"
        fmg_source_ip6: "<your_own_value>"
        fmg_update_port: "8890"
        include_default_servers: "enable"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        local_cert: "<your_own_value>"
        mode: "normal"
        schedule_config_restore: "enable"
        schedule_script_restore: "enable"
        serial_number: "<your_own_value>"
        server_list:
         -
            addr_type: "ipv4"
            fqdn: "<your_own_value>"
            id:  "24"
            server_address: "<your_own_value>"
            server_address6: "<your_own_value>"
            server_type: "update"
        type: "fortimanager"
        vdom: "<your_own_value> (source system.vdom.name)"
```

## [Return Values](fortios_system_central_management_module.md#id6)

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
