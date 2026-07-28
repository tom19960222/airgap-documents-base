---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_ddns module – Configure DDNS in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_ddns_module.html
fetched_at: 2026-07-28T02:28:07+00:00
---
# fortinet.fortios.fortios_system_ddns module – Configure DDNS in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_ddns_module.md#ansible-collections-fortinet-fortios-fortios-system-ddns-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_ddns`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_ddns_module.md#synopsis)
- [Requirements](fortios_system_ddns_module.md#requirements)
- [Parameters](fortios_system_ddns_module.md#parameters)
- [Notes](fortios_system_ddns_module.md#notes)
- [Examples](fortios_system_ddns_module.md#examples)
- [Return Values](fortios_system_ddns_module.md#return-values)

## [Synopsis](fortios_system_ddns_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and ddns category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_ddns_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_ddns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_ddns**  dictionary | Configure DDNS. |
| **addr_type**  string | Address type of interface address in DDNS update.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **bound_ip**  string | Bound IP address. |
| **clear_text**  string | Enable/disable use of clear text connections.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns_auth**  string | Enable/disable TSIG authentication for your DDNS server.  **Choices:**   - `"disable"` - `"tsig"` |
| **ddns_domain**  string | Your fully qualified domain name. For example, yourname.ddns.com. |
| **ddns_key**  string | DDNS update key (base 64 encoding). |
| **ddns_keyname**  string | DDNS update key name. |
| **ddns_password**  string | DDNS password. |
| **ddns_server**  string | Select a DDNS service provider.  **Choices:**   - `"dyndns.org"` - `"dyns.net"` - `"tzo.com"` - `"vavic.com"` - `"dipdns.net"` - `"now.net.cn"` - `"dhs.org"` - `"easydns.com"` - `"genericDDNS"` - `"FortiGuardDDNS"` - `"noip.com"` |
| **ddns_server_addr**  list / elements=dictionary | Generic DDNS server IP/FQDN list. |
| **addr**  string / required | IP address or FQDN of the server. |
| **ddns_server_ip**  string | Generic DDNS server IP. |
| **ddns_sn**  string | DDNS Serial Number. |
| **ddns_ttl**  integer | Time-to-live for DDNS packets. |
| **ddns_username**  string | DDNS user name. |
| **ddns_zone**  string | Zone of your domain name (for example, DDNS.com). |
| **ddnsid**  integer / required | DDNS ID. see <a href=’#notes’>Notes</a>. |
| **monitor_interface**  list / elements=dictionary | Monitored interface. |
| **interface_name**  string / required | Interface name. Source system.interface.name. |
| **server_type**  string | Address type of the DDNS server.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **ssl_certificate**  string | Name of local certificate for SSL connections. Source certificate.local.name. |
| **update_interval**  integer | DDNS update interval (60 - 2592000 sec, 0 means default). |
| **use_public_ip**  string | Enable/disable use of public IP address.  **Choices:**   - `"disable"` - `"enable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_ddns_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the ddnsid instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_ddns_module.md#id5)

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
  - name: Configure DDNS.
    fortios_system_ddns:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_ddns:
        addr_type: "ipv4"
        bound_ip: "<your_own_value>"
        clear_text: "disable"
        ddns_auth: "disable"
        ddns_domain: "<your_own_value>"
        ddns_key: "<your_own_value>"
        ddns_keyname: "<your_own_value>"
        ddns_password: "<your_own_value>"
        ddns_server: "dyndns.org"
        ddns_server_addr:
         -
            addr: "<your_own_value>"
        ddns_server_ip: "<your_own_value>"
        ddns_sn: "<your_own_value>"
        ddns_ttl: "300"
        ddns_username: "<your_own_value>"
        ddns_zone: "<your_own_value>"
        ddnsid: "<you_own_value>"
        monitor_interface:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        server_type: "ipv4"
        ssl_certificate: "<your_own_value> (source certificate.local.name)"
        update_interval: "300"
        use_public_ip: "disable"
```

## [Return Values](fortios_system_ddns_module.md#id6)

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
