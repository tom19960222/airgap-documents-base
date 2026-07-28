---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_dhcp6_server module – Configure DHCPv6 servers in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_dhcp6_server_module.html
fetched_at: 2026-07-28T02:28:09+00:00
---
# fortinet.fortios.fortios_system_dhcp6_server module – Configure DHCPv6 servers in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_dhcp6_server_module.md#ansible-collections-fortinet-fortios-fortios-system-dhcp6-server-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_dhcp6_server`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_dhcp6_server_module.md#synopsis)
- [Requirements](fortios_system_dhcp6_server_module.md#requirements)
- [Parameters](fortios_system_dhcp6_server_module.md#parameters)
- [Notes](fortios_system_dhcp6_server_module.md#notes)
- [Examples](fortios_system_dhcp6_server_module.md#examples)
- [Return Values](fortios_system_dhcp6_server_module.md#return-values)

## [Synopsis](fortios_system_dhcp6_server_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system_dhcp6 feature and server category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_dhcp6_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_dhcp6_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_dhcp6_server**  dictionary | Configure DHCPv6 servers. |
| **delegated_prefix_iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **dns_search_list**  string | DNS search list options.  **Choices:**   - `"delegated"` - `"specify"` |
| **dns_server1**  string | DNS server 1. |
| **dns_server2**  string | DNS server 2. |
| **dns_server3**  string | DNS server 3. |
| **dns_server4**  string | DNS server 4. |
| **dns_service**  string | Options for assigning DNS servers to DHCPv6 clients.  **Choices:**   - `"delegated"` - `"default"` - `"specify"` |
| **domain**  string | Domain name suffix for the IP addresses that the DHCP server assigns to clients. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | DHCP server can assign IP configurations to clients connected to this interface. Source system.interface.name. |
| **ip_mode**  string | Method used to assign client IP.  **Choices:**   - `"range"` - `"delegated"` |
| **ip_range**  list / elements=dictionary | DHCP IP range configuration. |
| **end_ip**  string | End of IP range. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **start_ip**  string | Start of IP range. |
| **lease_time**  integer | Lease time in seconds, 0 means unlimited. |
| **option1**  string | Option 1. |
| **option2**  string | Option 2. |
| **option3**  string | Option 3. |
| **prefix_mode**  string | Assigning a prefix from a DHCPv6 client or RA.  **Choices:**   - `"dhcp6"` - `"ra"` |
| **prefix_range**  list / elements=dictionary | DHCP prefix configuration. |
| **end_prefix**  string | End of prefix range. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **prefix_length**  integer | Prefix length. |
| **start_prefix**  string | Start of prefix range. |
| **rapid_commit**  string | Enable/disable allow/disallow rapid commit.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this DHCPv6 configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **subnet**  string | Subnet or subnet-id if the IP mode is delegated. |
| **upstream_interface**  string | Interface name from where delegated information is provided. Source system.interface.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_dhcp6_server_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_dhcp6_server_module.md#id5)

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
  - name: Configure DHCPv6 servers.
    fortios_system_dhcp6_server:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_dhcp6_server:
        delegated_prefix_iaid: "0"
        dns_search_list: "delegated"
        dns_server1: "<your_own_value>"
        dns_server2: "<your_own_value>"
        dns_server3: "<your_own_value>"
        dns_server4: "<your_own_value>"
        dns_service: "delegated"
        domain: "<your_own_value>"
        id:  "11"
        interface: "<your_own_value> (source system.interface.name)"
        ip_mode: "range"
        ip_range:
         -
            end_ip: "<your_own_value>"
            id:  "16"
            start_ip: "<your_own_value>"
        lease_time: "604800"
        option1: "<your_own_value>"
        option2: "<your_own_value>"
        option3: "<your_own_value>"
        prefix_mode: "dhcp6"
        prefix_range:
         -
            end_prefix: "<your_own_value>"
            id:  "25"
            prefix_length: "0"
            start_prefix: "<your_own_value>"
        rapid_commit: "disable"
        status: "disable"
        subnet: "<your_own_value>"
        upstream_interface: "<your_own_value> (source system.interface.name)"
```

## [Return Values](fortios_system_dhcp6_server_module.md#id6)

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
