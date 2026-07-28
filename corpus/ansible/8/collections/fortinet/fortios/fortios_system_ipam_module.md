---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_ipam module – Configure IP address management services in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_ipam_module.html
fetched_at: 2026-07-28T02:28:33+00:00
---
# fortinet.fortios.fortios_system_ipam module – Configure IP address management services in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_ipam_module.md#ansible-collections-fortinet-fortios-fortios-system-ipam-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_ipam`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_ipam_module.md#synopsis)
- [Requirements](fortios_system_ipam_module.md#requirements)
- [Parameters](fortios_system_ipam_module.md#parameters)
- [Notes](fortios_system_ipam_module.md#notes)
- [Examples](fortios_system_ipam_module.md#examples)
- [Return Values](fortios_system_ipam_module.md#return-values)

## [Synopsis](fortios_system_ipam_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and ipam category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_ipam_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_ipam_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_ipam**  dictionary | Configure IP address management services. |
| **automatic_conflict_resolution**  string | Enable/disable automatic conflict resolution.  **Choices:**   - `"disable"` - `"enable"` |
| **manage_lan_addresses**  string | Enable/disable default management of LAN interface addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **manage_lan_extension_addresses**  string | Enable/disable default management of FortiExtender LAN extension interface addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **manage_ssid_addresses**  string | Enable/disable default management of FortiAP SSID addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **pool_subnet**  string | Configure IPAM pool subnet, Class A - Class B subnet. |
| **pools**  list / elements=dictionary | Configure IPAM pools. |
| **description**  string | Description. |
| **name**  string / required | IPAM pool name. |
| **subnet**  string | Configure IPAM pool subnet, Class A - Class B subnet. |
| **rules**  list / elements=dictionary | Configure IPAM allocation rules. |
| **description**  string | Description. |
| **device**  list / elements=dictionary | Configure serial number or wildcard of FortiGate to match. |
| **name**  string / required | FortiGate serial number or wildcard. |
| **dhcp**  string | Enable/disable DHCP server for matching IPAM interfaces.  **Choices:**   - `"enable"` - `"disable"` |
| **interface**  list / elements=dictionary | Configure name or wildcard of interface to match. |
| **name**  string / required | Interface name or wildcard. |
| **name**  string / required | IPAM rule name. |
| **pool**  list / elements=dictionary | Configure name of IPAM pool to use. |
| **name**  string / required | IPAM pool name. Source system.ipam.pools.name. |
| **role**  string | Configure role of interface to match.  **Choices:**   - `"any"` - `"lan"` - `"wan"` - `"dmz"` - `"undefined"` |
| **server_type**  string | Configure the type of IPAM server to use.  **Choices:**   - `"fabric-root"` - `"cloud"` |
| **status**  string | Enable/disable IP address management services.  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_ipam_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_ipam_module.md#id5)

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
  - name: Configure IP address management services.
    fortios_system_ipam:
      vdom:  "{{ vdom }}"
      system_ipam:
        automatic_conflict_resolution: "disable"
        manage_lan_addresses: "disable"
        manage_lan_extension_addresses: "disable"
        manage_ssid_addresses: "disable"
        pool_subnet: "<your_own_value>"
        pools:
         -
            description: "<your_own_value>"
            name: "default_name_10"
            subnet: "<your_own_value>"
        rules:
         -
            description: "<your_own_value>"
            device:
             -
                name: "default_name_15"
            dhcp: "enable"
            interface:
             -
                name: "default_name_18"
            name: "default_name_19"
            pool:
             -
                name: "default_name_21 (source system.ipam.pools.name)"
            role: "any"
        server_type: "fabric-root"
        status: "enable"
```

## [Return Values](fortios_system_ipam_module.md#id6)

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
