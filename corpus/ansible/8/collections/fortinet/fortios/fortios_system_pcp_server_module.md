---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_pcp_server module – Configure PCP server information in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_pcp_server_module.html
fetched_at: 2026-07-28T02:28:53+00:00
---
# fortinet.fortios.fortios_system_pcp_server module – Configure PCP server information in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_pcp_server_module.md#ansible-collections-fortinet-fortios-fortios-system-pcp-server-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_pcp_server`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_pcp_server_module.md#synopsis)
- [Requirements](fortios_system_pcp_server_module.md#requirements)
- [Parameters](fortios_system_pcp_server_module.md#parameters)
- [Notes](fortios_system_pcp_server_module.md#notes)
- [Examples](fortios_system_pcp_server_module.md#examples)
- [Return Values](fortios_system_pcp_server_module.md#return-values)

## [Synopsis](fortios_system_pcp_server_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and pcp_server category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_pcp_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_pcp_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_pcp_server**  dictionary | Configure PCP server information. |
| **pools**  list / elements=dictionary | Configure PCP pools. |
| **allow_opcode**  list / elements=string | Allowed PCP opcode.  **Choices:**   - `"map"` - `"peer"` - `"announce"` |
| **announcement_count**  integer | Number of multicast announcements. |
| **arp_reply**  string | Enable to respond to ARP requests for external IP .  **Choices:**   - `"disable"` - `"enable"` |
| **client_mapping_limit**  integer | Mapping limit per client (0 - 65535). |
| **client_subnet**  list / elements=dictionary | Subnets from which PCP requests are accepted. |
| **subnet**  string / required | Client subnets. |
| **description**  string | Description. |
| **ext_intf**  string | External interface name. Source system.interface.name. |
| **extip**  string | IP address or address range on the external interface that you want to map to an address on the internal network. |
| **extport**  string | Incoming port number range that you want to map to a port number on the internal network. |
| **id**  integer | ID. |
| **intl_intf**  list / elements=dictionary | Internal interface name. |
| **interface_name**  string / required | Interface name. Source system.interface.name. |
| **mapping_filter_limit**  integer | Filter limit per mapping (0 - 5). |
| **maximal_lifetime**  integer | Maximal lifetime of a PCP mapping in seconds (3600 - 604800). |
| **minimal_lifetime**  integer | Minimal lifetime of a PCP mapping in seconds (60 - 300). |
| **multicast_announcement**  string | Enable/disable multicast announcements.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | PCP pool name. |
| **recycle_delay**  integer | Minimum delay (in seconds) the PCP Server will wait before recycling mappings that have expired (0 - 3600). |
| **third_party**  string | Allow/disallow third party option.  **Choices:**   - `"allow"` - `"disallow"` |
| **third_party_subnet**  list / elements=dictionary | Subnets from which third party requests are accepted. |
| **subnet**  string / required | Third party subnets. |
| **status**  string | Enable/disable PCP server.  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_pcp_server_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_pcp_server_module.md#id5)

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
  - name: Configure PCP server information.
    fortios_system_pcp_server:
      vdom:  "{{ vdom }}"
      system_pcp_server:
        pools:
         -
            allow_opcode: "map"
            announcement_count: "3"
            arp_reply: "disable"
            client_mapping_limit: "0"
            client_subnet:
             -
                subnet: "<your_own_value>"
            description: "<your_own_value>"
            ext_intf: "<your_own_value> (source system.interface.name)"
            extip: "<your_own_value>"
            extport: "<your_own_value>"
            id:  "14"
            intl_intf:
             -
                interface_name: "<your_own_value> (source system.interface.name)"
            mapping_filter_limit: "1"
            maximal_lifetime: "86400"
            minimal_lifetime: "120"
            multicast_announcement: "enable"
            name: "default_name_21"
            recycle_delay: "0"
            third_party: "allow"
            third_party_subnet:
             -
                subnet: "<your_own_value>"
        status: "enable"
```

## [Return Values](fortios_system_pcp_server_module.md#id6)

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
