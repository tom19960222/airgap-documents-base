---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_vip64 module – Configure IPv6 to IPv4 virtual IPs in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_vip64_module.html
fetched_at: 2026-07-27T17:41:44+00:00
---
# fortinet.fortios.fortios_firewall_vip64 module – Configure IPv6 to IPv4 virtual IPs in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_vip64_module.md#ansible-collections-fortinet-fortios-fortios-firewall-vip64-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_vip64`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_vip64_module.md#synopsis)
- [Requirements](fortios_firewall_vip64_module.md#requirements)
- [Parameters](fortios_firewall_vip64_module.md#parameters)
- [Notes](fortios_firewall_vip64_module.md#notes)
- [Examples](fortios_firewall_vip64_module.md#examples)
- [Return Values](fortios_firewall_vip64_module.md#return-values)

## [Synopsis](fortios_firewall_vip64_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and vip64 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_vip64_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_vip64_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_vip64**  dictionary | Configure IPv6 to IPv4 virtual IPs. |
| **arp_reply**  string | Enable ARP reply.  Choices:   - `"disable"` - `"enable"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **extip**  string | Start-external-IPv6-address [-end-external-IPv6-address]. |
| **extport**  string | External service port. |
| **id**  integer | Custom defined id. |
| **ldb_method**  string | Load balance method.  Choices:   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` |
| **mappedip**  string | Start-mapped-IP [-end-mapped-IP]. |
| **mappedport**  string | Mapped service port. |
| **monitor**  list / elements=dictionary | Health monitors. |
| **name**  string | Health monitor name. Source firewall.ldb-monitor.name. |
| **name**  string / required | VIP64 name. |
| **portforward**  string | Enable port forwarding.  Choices:   - `"disable"` - `"enable"` |
| **protocol**  string | Mapped port protocol.  Choices:   - `"tcp"` - `"udp"` |
| **realservers**  list / elements=dictionary | Real servers. |
| **client_ip**  string | Restrict server to a client IP in this range. |
| **healthcheck**  string | Per server health check.  Choices:   - `"disable"` - `"enable"` - `"vip"` |
| **holddown_interval**  integer | Hold down interval. |
| **id**  integer | Real server ID. |
| **ip**  string | Mapped server IP. |
| **max_connections**  integer | Maximum number of connections allowed to server. |
| **monitor**  list / elements=dictionary | Health monitors. Source firewall.ldb-monitor.name. |
| **name**  string | Health monitor name. Source firewall.ldb-monitor.name. |
| **port**  integer | Mapped server port. |
| **status**  string | Server administrative status.  Choices:   - `"active"` - `"standby"` - `"disable"` |
| **weight**  integer | weight |
| **server_type**  string | Server type.  Choices:   - `"http"` - `"tcp"` - `"udp"` - `"ip"` |
| **src_filter**  list / elements=dictionary | Source IP6 filter (x:x:x:x:x:x:x:x/x). |
| **range**  string | Src-filter range. |
| **type**  string | VIP type: static NAT or server load balance.  Choices:   - `"static-nat"` - `"server-load-balance"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_vip64_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_vip64_module.md#id5)

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
  - name: Configure IPv6 to IPv4 virtual IPs.
    fortios_firewall_vip64:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_vip64:
        arp_reply: "disable"
        color: "0"
        comment: "Comment."
        extip: "<your_own_value>"
        extport: "<your_own_value>"
        id:  "8"
        ldb_method: "static"
        mappedip: "<your_own_value>"
        mappedport: "<your_own_value>"
        monitor:
         -
            name: "default_name_13 (source firewall.ldb-monitor.name)"
        name: "default_name_14"
        portforward: "disable"
        protocol: "tcp"
        realservers:
         -
            client_ip: "<your_own_value>"
            healthcheck: "disable"
            holddown_interval: "300"
            id:  "21"
            ip: "<your_own_value>"
            max_connections: "0"
            monitor:
             -
                name: "default_name_25 (source firewall.ldb-monitor.name)"
            port: "0"
            status: "active"
            weight: "1"
        server_type: "http"
        src_filter:
         -
            range: "<your_own_value>"
        type: "static-nat"
        uuid: "<your_own_value>"
```

## [Return Values](fortios_firewall_vip64_module.md#id6)

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
