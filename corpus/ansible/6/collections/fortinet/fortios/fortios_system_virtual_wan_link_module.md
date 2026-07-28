---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_virtual_wan_link module – Configure redundant internet connections using SD-WAN (formerly virtual WAN link) in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_virtual_wan_link_module.html
fetched_at: 2026-07-27T17:45:46+00:00
---
# fortinet.fortios.fortios_system_virtual_wan_link module – Configure redundant internet connections using SD-WAN (formerly virtual WAN link) in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_virtual_wan_link_module.md#ansible-collections-fortinet-fortios-fortios-system-virtual-wan-link-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_virtual_wan_link`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_virtual_wan_link_module.md#synopsis)
- [Requirements](fortios_system_virtual_wan_link_module.md#requirements)
- [Parameters](fortios_system_virtual_wan_link_module.md#parameters)
- [Notes](fortios_system_virtual_wan_link_module.md#notes)
- [Examples](fortios_system_virtual_wan_link_module.md#examples)
- [Return Values](fortios_system_virtual_wan_link_module.md#return-values)

## [Synopsis](fortios_system_virtual_wan_link_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and virtual_wan_link category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_virtual_wan_link_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_virtual_wan_link_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **system_virtual_wan_link**  dictionary | Configure redundant internet connections using SD-WAN (formerly virtual WAN link). |
| **fail_alert_interfaces**  list / elements=dictionary | Physical interfaces that will be alerted. |
| **name**  string | Physical interface name. Source system.interface.name. |
| **fail_detect**  string | Enable/disable SD-WAN Internet connection status checking (failure detection).  Choices:   - `"enable"` - `"disable"` |
| **health_check**  list / elements=dictionary | SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it. |
| **addr_mode**  string | Address mode (IPv4 or IPv6).  Choices:   - `"ipv4"` - `"ipv6"` |
| **diffservcode**  string | Differentiated services code point (DSCP) in the IP header of the probe packet. |
| **failtime**  integer | Number of failures before server is considered lost (1 - 3600). |
| **ha_priority**  integer | HA election priority (1 - 50). |
| **http_agent**  string | String in the http-agent field in the HTTP header. |
| **http_get**  string | URL used to communicate with the server if the protocol if the protocol is HTTP. |
| **http_match**  string | Response string expected from the server if the protocol is HTTP. |
| **interval**  integer | Status check interval in milliseconds, or the time between attempting to connect to the server (500 - 3600\*1000 msec). |
| **members**  list / elements=dictionary | Member sequence number list. |
| **seq_num**  integer | Member sequence number. Source system.virtual-wan-link.members.seq-num. |
| **name**  string | Status check or health check name. |
| **packet_size**  integer | Packet size of a twamp test session, |
| **password**  string | Twamp controller password in authentication mode |
| **port**  integer | Port number used to communicate with the server over the selected protocol. |
| **probe_packets**  string | Enable/disable transmission of probe packets.  Choices:   - `"disable"` - `"enable"` |
| **probe_timeout**  integer | Time to wait before a probe packet is considered lost (500 - 5000 msec). |
| **protocol**  string | Protocol used to determine if the FortiGate can communicate with the server.  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` - `"http"` - `"twamp"` - `"ping6"` |
| **recoverytime**  integer | Number of successful responses received before server is considered recovered (1 - 3600). |
| **security_mode**  string | Twamp controller security mode.  Choices:   - `"none"` - `"authentication"` |
| **server**  string | IP address or FQDN name of the server. |
| **sla**  list / elements=dictionary | Service level agreement (SLA). |
| **id**  integer | SLA ID. |
| **jitter_threshold**  integer | Jitter for SLA to make decision in milliseconds. (0 - 10000000). |
| **latency_threshold**  integer | Latency for SLA to make decision in milliseconds. (0 - 10000000). |
| **link_cost_factor**  list / elements=string | Criteria on which to base link selection.  Choices:   - `"latency"` - `"jitter"` - `"packet-loss"` |
| **packetloss_threshold**  integer | Packet loss for SLA to make decision in percentage. (0 - 100). |
| **sla_fail_log_period**  integer | Time interval in seconds that SLA fail log messages will be generated (0 - 3600). |
| **sla_pass_log_period**  integer | Time interval in seconds that SLA pass log messages will be generated (0 - 3600). |
| **threshold_alert_jitter**  integer | Alert threshold for jitter (ms). |
| **threshold_alert_latency**  integer | Alert threshold for latency (ms). |
| **threshold_alert_packetloss**  integer | Alert threshold for packet loss (percentage). |
| **threshold_warning_jitter**  integer | Warning threshold for jitter (ms). |
| **threshold_warning_latency**  integer | Warning threshold for latency (ms). |
| **threshold_warning_packetloss**  integer | Warning threshold for packet loss (percentage). |
| **update_cascade_interface**  string | Enable/disable update cascade interface.  Choices:   - `"enable"` - `"disable"` |
| **update_static_route**  string | Enable/disable updating the static route.  Choices:   - `"enable"` - `"disable"` |
| **load_balance_mode**  string | Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.  Choices:   - `"source-ip-based"` - `"weight-based"` - `"usage-based"` - `"source-dest-ip-based"` - `"measured-volume-based"` |
| **members**  list / elements=dictionary | FortiGate interfaces added to the virtual-wan-link. |
| **comment**  string | Comments. |
| **cost**  integer | Cost of this interface for services in SLA mode (0 - 4294967295). |
| **gateway**  string | The default gateway for this interface. Usually the default gateway of the Internet service provider that this interface is connected to. |
| **gateway6**  string | IPv6 gateway. |
| **ingress_spillover_threshold**  integer | Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN. |
| **interface**  string | Interface name. Source system.interface.name. |
| **priority**  integer | Priority of the interface (0 - 4294967295). Used for SD-WAN rules or priority rules. |
| **seq_num**  integer | Sequence number(1-255). |
| **source**  string | Source IP address used in the health-check packet to the server. |
| **source6**  string | Source IPv6 address used in the health-check packet to the server. |
| **spillover_threshold**  integer | Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN. |
| **status**  string | Enable/disable this interface in the SD-WAN.  Choices:   - `"disable"` - `"enable"` |
| **volume_ratio**  integer | Measured volume ratio (this value / sum of all values = percentage of link volume, 1 - 255). |
| **weight**  integer | Weight of this interface for weighted load balancing. (1 - 255) More traffic is directed to interfaces with higher weights. |
| **neighbor**  list / elements=dictionary | Create SD-WAN neighbor from BGP neighbor table to control route advertisements according to SLA status. |
| **health_check**  string | SD-WAN health-check name. Source system.virtual-wan-link.health-check.name. |
| **ip**  string | IP address of neighbor. Source router.bgp.neighbor.ip. |
| **member**  integer | Member sequence number. Source system.virtual-wan-link.members.seq-num. |
| **role**  string | Role of neighbor.  Choices:   - `"standalone"` - `"primary"` - `"secondary"` |
| **sla_id**  integer | SLA ID. |
| **neighbor_hold_boot_time**  integer | Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. (0 - 10000000). |
| **neighbor_hold_down**  string | Enable/disable hold switching from the secondary neighbor to the primary neighbor.  Choices:   - `"enable"` - `"disable"` |
| **neighbor_hold_down_time**  integer | Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. (0 - 10000000). |
| **service**  list / elements=dictionary | Create SD-WAN rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN. |
| **addr_mode**  string | Address mode (IPv4 or IPv6).  Choices:   - `"ipv4"` - `"ipv6"` |
| **bandwidth_weight**  integer | Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. |
| **default**  string | Enable/disable use of SD-WAN as default service.  Choices:   - `"enable"` - `"disable"` |
| **dscp_forward**  string | Enable/disable forward traffic DSCP tag.  Choices:   - `"enable"` - `"disable"` |
| **dscp_forward_tag**  string | Forward traffic DSCP tag. |
| **dscp_reverse**  string | Enable/disable reverse traffic DSCP tag.  Choices:   - `"enable"` - `"disable"` |
| **dscp_reverse_tag**  string | Reverse traffic DSCP tag. |
| **dst**  list / elements=dictionary | Destination address name. |
| **name**  string | Address or address group name. Source firewall.address.name firewall.addrgrp.name. |
| **dst6**  list / elements=dictionary | Destination address6 name. |
| **name**  string | Address6 or address6 group name. Source firewall.address6.name firewall.addrgrp6.name. |
| **dst_negate**  string | Enable/disable negation of destination address match.  Choices:   - `"enable"` - `"disable"` |
| **end_port**  integer | End destination port number. |
| **gateway**  string | Enable/disable SD-WAN service gateway.  Choices:   - `"enable"` - `"disable"` |
| **groups**  list / elements=dictionary | User groups. |
| **name**  string | Group name. Source user.group.name. |
| **health_check**  string | Health check. Source system.virtual-wan-link.health-check.name. |
| **hold_down_time**  integer | Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000). |
| **id**  integer | Priority rule ID (1 - 4000). |
| **input_device**  list / elements=dictionary | Source interface name. |
| **name**  string | Interface name. Source system.interface.name. |
| **input_device_negate**  string | Enable/disable negation of input device match.  Choices:   - `"enable"` - `"disable"` |
| **internet_service**  string | Enable/disable use of Internet service for application-based load balancing.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_app_ctrl**  list / elements=dictionary | Application control based Internet Service ID list. |
| **id**  integer | Application control based Internet Service ID. |
| **internet_service_app_ctrl_group**  list / elements=dictionary | Application control based Internet Service group list. |
| **name**  string | Application control based Internet Service group name. Source application.group.name. |
| **internet_service_ctrl**  list / elements=dictionary | Control-based Internet Service ID list. |
| **id**  integer | Control-based Internet Service ID. |
| **internet_service_ctrl_group**  list / elements=dictionary | Control-based Internet Service group list. |
| **name**  string | Control-based Internet Service group name. Source application.group.name. |
| **internet_service_custom**  list / elements=dictionary | Custom Internet service name list. |
| **name**  string | Custom Internet service name. Source firewall.internet-service-custom.name. |
| **internet_service_custom_group**  list / elements=dictionary | Custom Internet Service group list. |
| **name**  string | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_group**  list / elements=dictionary | Internet Service group list. |
| **name**  string | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_id**  list / elements=dictionary | Internet service ID list. |
| **id**  integer | Internet service ID. Source firewall.internet-service.id. |
| **jitter_weight**  integer | Coefficient of jitter in the formula of custom-profile-1. |
| **latency_weight**  integer | Coefficient of latency in the formula of custom-profile-1. |
| **link_cost_factor**  string | Link cost factor.  Choices:   - `"latency"` - `"jitter"` - `"packet-loss"` - `"inbandwidth"` - `"outbandwidth"` - `"bibandwidth"` - `"custom-profile-1"` |
| **link_cost_threshold**  integer | Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000). |
| **member**  integer | Member sequence number. Source system.virtual-wan-link.members.seq-num. |
| **mode**  string | Control how the priority rule sets the priority of interfaces in the SD-WAN.  Choices:   - `"auto"` - `"manual"` - `"priority"` - `"sla"` - `"load-balance"` |
| **name**  string | Priority rule name. |
| **packet_loss_weight**  integer | Coefficient of packet-loss in the formula of custom-profile-1. |
| **priority_members**  list / elements=dictionary | Member sequence number list. |
| **seq_num**  integer | Member sequence number. Source system.virtual-wan-link.members.seq-num. |
| **protocol**  integer | Protocol number. |
| **quality_link**  integer | Quality grade. |
| **role**  string | Service role to work with neighbor.  Choices:   - `"standalone"` - `"primary"` - `"secondary"` |
| **route_tag**  integer | IPv4 route map route-tag. |
| **sla**  list / elements=dictionary | Service level agreement (SLA). |
| **health_check**  string | Virtual WAN Link health-check. Source system.virtual-wan-link.health-check.name. |
| **id**  integer | SLA ID. |
| **sla_compare_method**  string | Method to compare SLA value for sla and load balance mode.  Choices:   - `"order"` - `"number"` |
| **src**  list / elements=dictionary | Source address name. |
| **name**  string | Address or address group name. Source firewall.address.name firewall.addrgrp.name. |
| **src6**  list / elements=dictionary | Source address6 name. |
| **name**  string | Address6 or address6 group name. Source firewall.address6.name firewall.addrgrp6.name. |
| **src_negate**  string | Enable/disable negation of source address match.  Choices:   - `"enable"` - `"disable"` |
| **standalone_action**  string | Enable/disable service when selected neighbor role is standalone while service role is not standalone.  Choices:   - `"enable"` - `"disable"` |
| **start_port**  integer | Start destination port number. |
| **status**  string | Enable/disable SD-WAN service.  Choices:   - `"enable"` - `"disable"` |
| **tos**  string | Type of service bit pattern. |
| **tos_mask**  string | Type of service evaluated bits. |
| **users**  list / elements=dictionary | User name. |
| **name**  string | User name. Source user.local.name. |
| **status**  string | Enable/disable SD-WAN.  Choices:   - `"disable"` - `"enable"` |
| **zone**  list / elements=dictionary | Configure SD-WAN zones. |
| **name**  string | Zone name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_virtual_wan_link_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_virtual_wan_link_module.md#id5)

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
  - name: Configure redundant internet connections using SD-WAN (formerly virtual WAN link).
    fortios_system_virtual_wan_link:
      vdom:  "{{ vdom }}"
      system_virtual_wan_link:
        fail_alert_interfaces:
         -
            name: "default_name_4 (source system.interface.name)"
        fail_detect: "enable"
        health_check:
         -
            addr_mode: "ipv4"
            diffservcode: "<your_own_value>"
            failtime: "1800"
            ha_priority: "25"
            http_agent: "<your_own_value>"
            http_get: "<your_own_value>"
            http_match: "<your_own_value>"
            interval: "1800000"
            members:
             -
                seq_num: "2147483647"
            name: "default_name_17"
            packet_size: "512"
            password: "<your_own_value>"
            port: "32767"
            probe_packets: "disable"
            probe_timeout: "2500"
            protocol: "ping"
            recoverytime: "1800"
            security_mode: "none"
            server: "192.168.100.40"
            sla:
             -
                id:  "28"
                jitter_threshold: "5000000"
                latency_threshold: "5000000"
                link_cost_factor: "latency"
                packetloss_threshold: "50"
            sla_fail_log_period: "1800"
            sla_pass_log_period: "1800"
            threshold_alert_jitter: "2147483647"
            threshold_alert_latency: "2147483647"
            threshold_alert_packetloss: "50"
            threshold_warning_jitter: "2147483647"
            threshold_warning_latency: "2147483647"
            threshold_warning_packetloss: "50"
            update_cascade_interface: "enable"
            update_static_route: "enable"
        load_balance_mode: "source-ip-based"
        members:
         -
            comment: "Comments."
            cost: "2147483647"
            gateway: "<your_own_value>"
            gateway6: "<your_own_value>"
            ingress_spillover_threshold: "8388000"
            interface: "<your_own_value> (source system.interface.name)"
            priority: "2147483647"
            seq_num: "127"
            source: "<your_own_value>"
            source6: "<your_own_value>"
            spillover_threshold: "8388000"
            status: "disable"
            volume_ratio: "127"
            weight: "127"
        neighbor:
         -
            health_check: "<your_own_value> (source system.virtual-wan-link.health-check.name)"
            ip: "<your_own_value> (source router.bgp.neighbor.ip)"
            member: "2147483647"
            role: "standalone"
            sla_id: "2147483647"
        neighbor_hold_boot_time: "5000000"
        neighbor_hold_down: "enable"
        neighbor_hold_down_time: "5000000"
        service:
         -
            addr_mode: "ipv4"
            bandwidth_weight: "5000000"
            default: "enable"
            dscp_forward: "enable"
            dscp_forward_tag: "<your_own_value>"
            dscp_reverse: "enable"
            dscp_reverse_tag: "<your_own_value>"
            dst:
             -
                name: "default_name_77 (source firewall.address.name firewall.addrgrp.name)"
            dst_negate: "enable"
            dst6:
             -
                name: "default_name_80 (source firewall.address6.name firewall.addrgrp6.name)"
            end_port: "32767"
            gateway: "enable"
            groups:
             -
                name: "default_name_84 (source user.group.name)"
            health_check: "<your_own_value> (source system.virtual-wan-link.health-check.name)"
            hold_down_time: "5000000"
            id:  "87"
            input_device:
             -
                name: "default_name_89 (source system.interface.name)"
            input_device_negate: "enable"
            internet_service: "enable"
            internet_service_app_ctrl:
             -
                id:  "93"
            internet_service_app_ctrl_group:
             -
                name: "default_name_95 (source application.group.name)"
            internet_service_ctrl:
             -
                id:  "97"
            internet_service_ctrl_group:
             -
                name: "default_name_99 (source application.group.name)"
            internet_service_custom:
             -
                name: "default_name_101 (source firewall.internet-service-custom.name)"
            internet_service_custom_group:
             -
                name: "default_name_103 (source firewall.internet-service-custom-group.name)"
            internet_service_group:
             -
                name: "default_name_105 (source firewall.internet-service-group.name)"
            internet_service_id:
             -
                id:  "107 (source firewall.internet-service.id)"
            jitter_weight: "5000000"
            latency_weight: "5000000"
            link_cost_factor: "latency"
            link_cost_threshold: "5000000"
            member: "2147483647"
            mode: "auto"
            name: "default_name_114"
            packet_loss_weight: "5000000"
            priority_members:
             -
                seq_num: "2147483647"
            protocol: "127"
            quality_link: "127"
            role: "standalone"
            route_tag: "2147483647"
            sla:
             -
                health_check: "<your_own_value> (source system.virtual-wan-link.health-check.name)"
                id:  "124"
            sla_compare_method: "order"
            src:
             -
                name: "default_name_127 (source firewall.address.name firewall.addrgrp.name)"
            src_negate: "enable"
            src6:
             -
                name: "default_name_130 (source firewall.address6.name firewall.addrgrp6.name)"
            standalone_action: "enable"
            start_port: "32767"
            status: "enable"
            tos: "<your_own_value>"
            tos_mask: "<your_own_value>"
            users:
             -
                name: "default_name_137 (source user.local.name)"
        status: "disable"
        zone:
         -
            name: "default_name_140"
```

## [Return Values](fortios_system_virtual_wan_link_module.md#id6)

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
