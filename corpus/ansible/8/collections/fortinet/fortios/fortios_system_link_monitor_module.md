---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_link_monitor module – Configure Link Health Monitor in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_link_monitor_module.html
fetched_at: 2026-07-28T02:28:40+00:00
---
# fortinet.fortios.fortios_system_link_monitor module – Configure Link Health Monitor in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_link_monitor_module.md#ansible-collections-fortinet-fortios-fortios-system-link-monitor-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_link_monitor`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_link_monitor_module.md#synopsis)
- [Requirements](fortios_system_link_monitor_module.md#requirements)
- [Parameters](fortios_system_link_monitor_module.md#parameters)
- [Notes](fortios_system_link_monitor_module.md#notes)
- [Examples](fortios_system_link_monitor_module.md#examples)
- [Return Values](fortios_system_link_monitor_module.md#return-values)

## [Synopsis](fortios_system_link_monitor_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and link_monitor category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_link_monitor_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_link_monitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_link_monitor**  dictionary | Configure Link Health Monitor. |
| **addr_mode**  string | Address mode (IPv4 or IPv6).  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **class_id**  integer | Traffic class ID. Source firewall.traffic-class.class-id. |
| **diffservcode**  string | Differentiated services code point (DSCP) in the IP header of the probe packet. |
| **fail_weight**  integer | Threshold weight to trigger link failure alert. |
| **failtime**  integer | Number of retry attempts before the server is considered down (1 - 3600). |
| **gateway_ip**  string | Gateway IP address used to probe the server. |
| **gateway_ip6**  string | Gateway IPv6 address used to probe the server. |
| **ha_priority**  integer | HA election priority (1 - 50). |
| **http_agent**  string | String in the http-agent field in the HTTP header. |
| **http_get**  string | If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string. |
| **http_match**  string | String that you expect to see in the HTTP-GET requests of the traffic to be monitored. |
| **interval**  integer | Detection interval in milliseconds (20 - 3600 \* 1000 msec). |
| **name**  string / required | Link monitor name. |
| **packet_size**  integer | Packet size of a TWAMP test session (124/158 - 1024). |
| **password**  string | TWAMP controller password in authentication mode. |
| **port**  integer | Port number of the traffic to be used to monitor the server. |
| **probe_count**  integer | Number of most recent probes that should be used to calculate latency and jitter (5 - 30). |
| **probe_timeout**  integer | Time to wait before a probe packet is considered lost (20 - 5000 msec). |
| **protocol**  list / elements=string | Protocols used to monitor the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"https"` - `"twamp"` - `"ping6"` |
| **recoverytime**  integer | Number of successful responses received before server is considered recovered (1 - 3600). |
| **route**  list / elements=dictionary | Subnet to monitor. |
| **subnet**  string / required | IP and netmask (x.x.x.x/y). |
| **security_mode**  string | Twamp controller security mode.  **Choices:**   - `"none"` - `"authentication"` |
| **server**  list / elements=dictionary | IP address of the server(s) to be monitored. |
| **address**  string / required | Server address. |
| **server_config**  string | Mode of server configuration.  **Choices:**   - `"default"` - `"individual"` |
| **server_list**  list / elements=dictionary | Servers for link-monitor to monitor. |
| **dst**  string | IP address of the server to be monitored. |
| **id**  integer / required | Server ID. see <a href=’#notes’>Notes</a>. |
| **port**  integer | Port number of the traffic to be used to monitor the server. |
| **protocol**  list / elements=string | Protocols used to monitor the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"https"` - `"twamp"` |
| **weight**  integer | Weight of the monitor to this dst (0 - 255). |
| **server_type**  string | Server type (static or dynamic).  **Choices:**   - `"static"` - `"dynamic"` |
| **service_detection**  string | Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated.  **Choices:**   - `"enable"` - `"disable"` |
| **source_ip**  string | Source IP address used in packet to the server. |
| **source_ip6**  string | Source IPv6 address used in packet to the server. |
| **srcintf**  string | Interface that receives the traffic to be monitored. Source system.interface.name. |
| **status**  string | Enable/disable this link monitor.  **Choices:**   - `"enable"` - `"disable"` |
| **update_cascade_interface**  string | Enable/disable update cascade interface.  **Choices:**   - `"enable"` - `"disable"` |
| **update_policy_route**  string | Enable/disable updating the policy route.  **Choices:**   - `"enable"` - `"disable"` |
| **update_static_route**  string | Enable/disable updating the static route.  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_link_monitor_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_link_monitor_module.md#id5)

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
  - name: Configure Link Health Monitor.
    fortios_system_link_monitor:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_link_monitor:
        addr_mode: "ipv4"
        class_id: "0"
        diffservcode: "<your_own_value>"
        fail_weight: "0"
        failtime: "5"
        gateway_ip: "<your_own_value>"
        gateway_ip6: "<your_own_value>"
        ha_priority: "1"
        http_agent: "<your_own_value>"
        http_get: "<your_own_value>"
        http_match: "<your_own_value>"
        interval: "500"
        name: "default_name_15"
        packet_size: "124"
        password: "<your_own_value>"
        port: "0"
        probe_count: "30"
        probe_timeout: "500"
        protocol: "ping"
        recoverytime: "5"
        route:
         -
            subnet: "<your_own_value>"
        security_mode: "none"
        server:
         -
            address: "<your_own_value>"
        server_config: "default"
        server_list:
         -
            dst: "<your_own_value>"
            id:  "31"
            port: "0"
            protocol: "ping"
            weight: "0"
        server_type: "static"
        service_detection: "enable"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        srcintf: "<your_own_value> (source system.interface.name)"
        status: "enable"
        update_cascade_interface: "enable"
        update_policy_route: "enable"
        update_static_route: "enable"
```

## [Return Values](fortios_system_link_monitor_module.md#id6)

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
