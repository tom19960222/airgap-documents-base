---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_service_custom module – Configure custom services in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_service_custom_module.html
fetched_at: 2026-07-27T17:41:29+00:00
---
# fortinet.fortios.fortios_firewall_service_custom module – Configure custom services in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_service_custom_module.md#ansible-collections-fortinet-fortios-fortios-firewall-service-custom-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_service_custom`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_service_custom_module.md#synopsis)
- [Requirements](fortios_firewall_service_custom_module.md#requirements)
- [Parameters](fortios_firewall_service_custom_module.md#parameters)
- [Notes](fortios_firewall_service_custom_module.md#notes)
- [Examples](fortios_firewall_service_custom_module.md#examples)
- [Return Values](fortios_firewall_service_custom_module.md#return-values)

## [Synopsis](fortios_firewall_service_custom_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall_service feature and custom category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_service_custom_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_service_custom_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_service_custom**  dictionary | Configure custom services. |
| **app_category**  list / elements=dictionary | Application category ID. |
| **id**  integer | Application category id. |
| **app_service_type**  string | Application service type.  Choices:   - `"disable"` - `"app-id"` - `"app-category"` |
| **application**  list / elements=dictionary | Application ID. |
| **id**  integer | Application id. |
| **category**  string | Service category. Source firewall.service.category.name. |
| **check_reset_range**  string | Configure the type of ICMP error message verification.  Choices:   - `"disable"` - `"strict"` - `"default"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **fabric_object**  string | Security Fabric global object setting.  Choices:   - `"enable"` - `"disable"` |
| **fqdn**  string | Fully qualified domain name. |
| **helper**  string | Helper name.  Choices:   - `"auto"` - `"disable"` - `"ftp"` - `"tftp"` - `"ras"` - `"h323"` - `"tns"` - `"mms"` - `"sip"` - `"pptp"` - `"rtsp"` - `"dns-udp"` - `"dns-tcp"` - `"pmap"` - `"rsh"` - `"dcerpc"` - `"mgcp"` - `"gtp-c"` - `"gtp-u"` - `"gtp-b"` - `"pfcp"` |
| **icmpcode**  integer | ICMP code. |
| **icmptype**  integer | ICMP type. |
| **iprange**  string | Start and end of the IP range associated with service. |
| **name**  string / required | Custom service name. |
| **protocol**  string | Protocol type based on IANA numbers.  Choices:   - `"TCP/UDP/SCTP"` - `"ICMP"` - `"ICMP6"` - `"IP"` - `"HTTP"` - `"FTP"` - `"CONNECT"` - `"SOCKS-TCP"` - `"SOCKS-UDP"` - `"ALL"` |
| **protocol_number**  integer | IP protocol number. |
| **proxy**  string | Enable/disable web proxy service.  Choices:   - `"enable"` - `"disable"` |
| **sctp_portrange**  string | Multiple SCTP port ranges. |
| **session_ttl**  string | Session TTL (300 - 2764800, 0 = default). |
| **tcp_halfclose_timer**  integer | Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400 sec, 0 = default). |
| **tcp_halfopen_timer**  integer | Wait time to close a TCP session waiting for an unanswered open session packet (1 - 86400 sec, 0 = default). |
| **tcp_portrange**  string | Multiple TCP port ranges. |
| **tcp_rst_timer**  integer | Set the length of the TCP CLOSE state in seconds (5 - 300 sec, 0 = default). |
| **tcp_timewait_timer**  integer | Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default). |
| **udp_idle_timer**  integer | UDP half close timeout (0 - 86400 sec, 0 = default). |
| **udp_portrange**  string | Multiple UDP port ranges. |
| **visibility**  string | Enable/disable the visibility of the service on the GUI.  Choices:   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_service_custom_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_service_custom_module.md#id5)

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
  - name: Configure custom services.
    fortios_firewall_service_custom:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_service_custom:
        app_category:
         -
            id:  "4"
        app_service_type: "disable"
        application:
         -
            id:  "7"
        category: "<your_own_value> (source firewall.service.category.name)"
        check_reset_range: "disable"
        color: "0"
        comment: "Comment."
        fabric_object: "enable"
        fqdn: "<your_own_value>"
        helper: "auto"
        icmpcode: ""
        icmptype: ""
        iprange: "<your_own_value>"
        name: "default_name_18"
        protocol: "TCP/UDP/SCTP"
        protocol_number: "0"
        proxy: "enable"
        sctp_portrange: "<your_own_value>"
        session_ttl: "<your_own_value>"
        tcp_halfclose_timer: "0"
        tcp_halfopen_timer: "0"
        tcp_portrange: "<your_own_value>"
        tcp_rst_timer: "0"
        tcp_timewait_timer: "0"
        udp_idle_timer: "0"
        udp_portrange: "<your_own_value>"
        visibility: "enable"
```

## [Return Values](fortios_firewall_service_custom_module.md#id6)

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
