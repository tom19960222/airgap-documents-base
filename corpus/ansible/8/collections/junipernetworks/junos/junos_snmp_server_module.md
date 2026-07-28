---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_snmp_server module – Manage SNMP server configuration on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_snmp_server_module.html
fetched_at: 2026-07-28T02:39:57+00:00
---
# junipernetworks.junos.junos_snmp_server module – Manage SNMP server configuration on Junos devices.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_snmp_server_module.md#ansible-collections-junipernetworks-junos-junos-snmp-server-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_snmp_server`.

New in junipernetworks.junos 2.9.0

- [Synopsis](junos_snmp_server_module.md#synopsis)
- [Requirements](junos_snmp_server_module.md#requirements)
- [Parameters](junos_snmp_server_module.md#parameters)
- [Notes](junos_snmp_server_module.md#notes)
- [Examples](junos_snmp_server_module.md#examples)
- [Return Values](junos_snmp_server_module.md#return-values)

## [Synopsis](junos_snmp_server_module.md#id1)

- This module manages SNMP server configuration on devices running Junos.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: snmp_server

## [Requirements](junos_snmp_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_snmp_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of SNMP server configuration. |
| **arp**  dictionary | Specify JVision arp setting. |
| **host_name_resolution**  boolean | Enable host name resolution.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set JVision arp.  **Choices:**   - `false` - `true` |
| **client_lists**  list / elements=dictionary | Specify client list. |
| **addresses**  list / elements=dictionary | Specify list of addresses/prefixes. |
| **address**  string | Specify address or prefix. |
| **restrict**  boolean | Deny access.  **Choices:**   - `false` - `true` |
| **name**  string | Specify client list name. |
| **communities**  list / elements=dictionary | Specify list of community string. |
| **authorization**  string | Specify Authorization type.  **Choices:**   - `"read-only"` - `"read-write"` |
| **client_list_name**  string | Specify the name of client list or prefix list. |
| **clients**  list / elements=dictionary | Specify List of source address prefix ranges to accept. |
| **address**  string | Specify address or prefix. |
| **restrict**  boolean | Deny access.  **Choices:**   - `false` - `true` |
| **logical_system**  list / elements=string | Use logical-system name for v1/v2c clients. |
| **name**  string | Specify name of the community. |
| **routing_instances**  list / elements=dictionary | Use routing-instance name for v1/v2c clients. |
| **client_list_name**  string | Specify the name of client list or prefix list. |
| **clients**  list / elements=dictionary | Specify List of source address prefix ranges to accept. |
| **address**  string | Specify address or prefix. |
| **restrict**  boolean | Deny access.  **Choices:**   - `false` - `true` |
| **name**  string | Specify routing-instances. |
| **view**  string | Specify view name. |
| **contact**  string | Specify contact information for administrator. |
| **customization**  dictionary | Customize SNMP behaviour based on knob. |
| **ether_stats_ifd_only**  boolean | To stop exposing IFLs as part of etherStatsTable.  **Choices:**   - `false` - `true` |
| **description**  string | System description. |
| **engine_id**  dictionary | Specify SNMPv3 engine ID |
| **local**  string | Local engine ID. |
| **use_default_ip_address**  boolean | Use default IP address for the engine ID.  **Choices:**   - `false` - `true` |
| **use_mac_address**  boolean | Uses management interface MAC Address for the engine ID.  **Choices:**   - `false` - `true` |
| **filter_duplicates**  boolean | Filter requests with duplicate source address/port and request ID.  **Choices:**   - `false` - `true` |
| **filter_interfaces**  dictionary | List of interfaces that needs to be filtered. |
| **all_internal_interfaces**  boolean | Filter all internal interfaces.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=string | Specify filter specified interfaces. |
| **set**  boolean | Set filter-interfaces.  **Choices:**   - `false` - `true` |
| **health_monitor**  dictionary | Specify health monitoring configuration. |
| **falling_threshold**  integer | Falling threshold applied to all monitored objects. |
| **idp**  boolean | IDP health monitor configuration.  **Choices:**   - `false` - `true` |
| **interval**  integer | Interval between samples. |
| **rising_threshold**  integer | Rising threshold applied to all monitored objects. |
| **set**  boolean | Set health-monitor configuration.  **Choices:**   - `false` - `true` |
| **if_count_with_filter_interfaces**  boolean | Filter interfaces config for ifNumber and ipv6Interfaces.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=string | Restrict SNMP requests to interfaces. |
| **location**  string | Specify physical location of system. |
| **logical_system_trap_filter**  boolean | Allow only logical-system specific traps.  **Choices:**   - `false` - `true` |
| **name**  string | System name override. |
| **nonvolatile**  dictionary | Configure the handling of nonvolatile SNMP Set requests. |
| **commit_delay**  integer | Delay between affirmative SNMP Set reply and start of commit (seconds). |
| **proxies**  list / elements=dictionary | SNMP proxy configuration. |
| **device_name**  string | Satellite/Proxied Device name or IP address. |
| **logical_system**  list / elements=string | Use logical-system name for v1/v2c clients. |
| **name**  string | Specify proxy name. |
| **routing_instances**  list / elements=dictionary | Use routing-instance name for v1/v2c clients. |
| **client_list_name**  string | Specify the name of client list or prefix list. |
| **clients**  list / elements=dictionary | Specify List of source address prefix ranges to accept. |
| **address**  string | Specify address or prefix. |
| **restrict**  boolean | Deny access.  **Choices:**   - `false` - `true` |
| **name**  string | Specify routing-instances. |
| **version_v1**  dictionary | Specify For v1 proxy configuration define snmp-community. |
| **no_default_comm_to_v3_config**  boolean | Specify No default snmp-community and v3 configuration.  **Choices:**   - `false` - `true` |
| **snmp_community**  string | Specify community name. |
| **version_v2c**  dictionary | For v2c proxy configuration define snmp-community. |
| **no_default_comm_to_v3_config**  boolean | Specify No default snmp-community and v3 configuration.  **Choices:**   - `false` - `true` |
| **snmp_community**  string | Specify community name. |
| **version_v3**  dictionary | For v3 proxy configuration define security-name. |
| **context**  boolean | pecify context name associated to this security-name.  **Choices:**   - `false` - `true` |
| **security_name**  string | Specify v3 security-name. |
| **rmon**  dictionary | Specify Remote Monitoring configuration. |
| **alarms**  list / elements=dictionary | RMON alarm entries. |
| **description**  string | General description of alarm (stored in alarmOwner). |
| **falling_event_index**  integer | Event triggered after falling threshold is crossed. |
| **falling_threshold**  integer | Specify falling-threshold. |
| **falling_threshold_interval**  integer | Interval between samples during falling-threshold test. |
| **id**  string | Specify alarm ID. |
| **interval**  integer | Interval between samples. |
| **request_type**  string | Type of SNMP request to issue for alarm.  **Choices:**   - `"get-next-request"` - `"get-request"` - `"walk-request"` |
| **rising_event_index**  integer | Event triggered after rising threshold is crossed. |
| **rising_threshold**  integer | The rising threshold. |
| **sample_type**  string | Method of sampling the selected variable.  **Choices:**   - `"absolute-value"` - `"delta-value"` |
| **startup_alarm**  string | The alarm that may be sent upon entry startup.  **Choices:**   - `"falling-alarm"` - `"rising-alarm"` - `"rising-or-falling-alarm"` |
| **syslog_subtag**  string | Tag to be added to syslog messages. |
| **variable**  string | OID of MIB variable to be monitored. |
| **events**  list / elements=dictionary | RMON event entries. |
| **community**  string | The community (trap group) for outgoing traps. |
| **description**  string | General description of event. |
| **id**  integer | Specify event ID. |
| **type**  string | The type of notification for this event.  **Choices:**   - `"log"` - `"log-and-trap"` - `"none"` - `"snmptrap"` |
| **set**  boolean | Set Remote monitoring configuration.  **Choices:**   - `false` - `true` |
| **routing_instance_access**  dictionary | SNMP routing-instance options. |
| **access_lists**  list / elements=string | Allow/Deny SNMP access to routing-instances. |
| **set**  boolean | Set routing_instance_access.  **Choices:**   - `false` - `true` |
| **snmp_v3**  dictionary | SNMPv3 configuration information. |
| **notify**  list / elements=dictionary | Used to select management targets for notifications as well as the type of notifications. |
| **name**  string | Specify notify name. |
| **tag**  string | Notifications will be sent to all targets configured with this tag. |
| **type**  string | Notification type. |
| **notify_filter**  list / elements=dictionary | Filters to apply to SNMP notifications. |
| **name**  string | Specify notify filter name. |
| **oids**  list / elements=dictionary | OID to include/exclude from notify filter. |
| **exclude**  boolean | Exclude this OID from the notify filtered.  **Choices:**   - `false` - `true` |
| **include**  boolean | Include this OID in the notify filter.  **Choices:**   - `false` - `true` |
| **oid**  string | Specify OID. |
| **snmp_community**  list / elements=dictionary | SNMP community and view-based access control model configuration. |
| **community_index**  string | Unique index value in this community table entry. |
| **community_name**  string | SNMPv1/v2c community name (default is same as community-index). |
| **context**  string | Context used when performing access control. |
| **security_name**  string | Security name used when performing access control. |
| **tag**  string | Tag identifier for set of targets allowed to use this community string. |
| **target_addresses**  list / elements=dictionary | Identifies notification targets as well as allowed management stations. |
| **address**  string | SNMP target address. |
| **address_mask**  string | Mask range of addresses for community string access control. |
| **logical_system**  string | Logical-system name for trap destination. |
| **name**  string | SNMP target address name. |
| **port**  integer | SNMP target port number. |
| **retry_count**  integer | Maximum retry count for confirmed SNMP notifications. |
| **routing_instance**  string | Routing instance for trap destination. |
| **tag_list**  string | SNMP tag list used to select target addresses. |
| **target_parameters**  string | SNMPv3 target parameter name in the target parameters table. |
| **timeout**  integer | Acknowledgment timeout for confirmed SNMP notifications (seconds). |
| **target_parameters**  list / elements=dictionary | SNMPv3 target parameter name in the target parameters table. |
| **name**  string | SNMPv3 target parameters name. |
| **notify_filter**  string | Notify filter with filter name to apply to notifications. |
| **parameters**  dictionary | Parameters used when sending notifications. |
| **message_processing_model**  string | The message processing model to be used when generating SNMP notifications.  **Choices:**   - `"v1"` - `"v2c"` - `"v3"` |
| **security_level**  string | Security-level used when generating SNMP notifications.  **Choices:**   - `"authentication"` - `"none"` - `"privacy"` |
| **security_model**  string | Security-model used when generating SNMP notifications.  **Choices:**   - `"usm"` - `"v1"` - `"v2c"` |
| **security_name**  string | Security name used when generating SNMP notifications. |
| **usm**  dictionary | User-based security model (USM) information. |
| **local_engine**  dictionary | Local engine user configuration. |
| **users**  list / elements=dictionary | SNMPv3 USM user information. |
| **authentication_md5**  dictionary | Configure MD5 authentication. |
| **key**  string | Encrypted key used for user authentication. |
| **password**  string | User’s authentication password |
| **authentication_none**  boolean | Set no authentication for the user.  **Choices:**   - `false` - `true` |
| **authentication_sha**  dictionary | Configure SHA authentication. |
| **key**  string | Encrypted key used for user authentication. |
| **password**  string | User’s authentication password |
| **name**  string | User name. |
| **privacy_3des**  dictionary | Configure Triple DES privacy. |
| **key**  string | Encrypted key used for user privacy. |
| **password**  string | User’s privacy password |
| **privacy_aes128**  dictionary | Configure AES128 privacy. |
| **key**  string | Encrypted key used for user privacy. |
| **password**  string | User’s privacy password |
| **privacy_des**  dictionary | Configure DES privacy. |
| **key**  string | Encrypted key used for user privacy. |
| **password**  string | User’s privacy password |
| **privacy_none**  boolean | Set no privacy for the user.  **Choices:**   - `false` - `true` |
| **remote_engine**  list / elements=dictionary | Remote engine user configuration. |
| **id**  string | Remote engine id. |
| **users**  list / elements=dictionary | SNMPv3 USM user information. |
| **authentication_md5**  dictionary | Configure MD5 authentication. |
| **key**  string | Encrypted key used for user authentication. |
| **password**  string | User’s authentication password |
| **authentication_none**  boolean | Set no authentication for the user.  **Choices:**   - `false` - `true` |
| **authentication_sha**  dictionary | Configure SHA authentication. |
| **key**  string | Encrypted key used for user authentication. |
| **password**  string | User’s authentication password |
| **name**  string | User name. |
| **privacy_3des**  dictionary | Configure Triple DES privacy. |
| **key**  string | Encrypted key used for user privacy. |
| **password**  string | User’s privacy password |
| **privacy_aes128**  dictionary | Configure AES128 privacy. |
| **key**  string | Encrypted key used for user privacy. |
| **password**  string | User’s privacy password |
| **privacy_des**  dictionary | Configure DES privacy. |
| **key**  string | Encrypted key used for user privacy. |
| **password**  string | User’s privacy password |
| **privacy_none**  boolean | Set no privacy for the user.  **Choices:**   - `false` - `true` |
| **subagent**  dictionary | SNMP subagent configuration. |
| **tcp**  dictionary | Allow SNMP subagent tcp connection. |
| **routing_instances_default**  boolean | Specify routing-instance name for tcp connection.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set SNMP subagent TCP.  **Choices:**   - `false` - `true` |
| **traceoptions**  dictionary | Configure trace options for SNMP. |
| **file**  dictionary | Specify trace file options. |
| **files**  integer | Specify maximum number of trace files. |
| **match**  string | Regular expression for lines to be logged. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  **Choices:**   - `false` - `true` |
| **size**  integer | Specify maximum trace file size. |
| **world_readable**  boolean | Allow any user to read the log file.  **Choices:**   - `false` - `true` |
| **flag**  dictionary | Specify flag traceoptions. |
| **all**  boolean | Trace everything.  **Choices:**   - `false` - `true` |
| **general**  boolean | Trace general events.  **Choices:**   - `false` - `true` |
| **interface_stats**  boolean | Trace interface statistics (logical and physical).  **Choices:**   - `false` - `true` |
| **nonvolatile_sets**  boolean | Nonvolatile SNMP set request handling.  **Choices:**   - `false` - `true` |
| **pdu**  boolean | Dump SNMP request/response packets.  **Choices:**   - `false` - `true` |
| **protocol_timeouts**  boolean | Trace SNMP request timeouts.  **Choices:**   - `false` - `true` |
| **routing_socket**  boolean | Trace routing socket calls.  **Choices:**   - `false` - `true` |
| **subagent**  boolean | Trace master-agent interations with sub-agents.  **Choices:**   - `false` - `true` |
| **timer**  boolean | Trace internal timer events.  **Choices:**   - `false` - `true` |
| **varbind_error**  boolean | Trace varbind errors.  **Choices:**   - `false` - `true` |
| **memory_trace**  dictionary | Memory tracing information. |
| **set**  boolean | set memory traceoptions.  **Choices:**   - `false` - `true` |
| **size**  integer | Specify Memory size reserved for tracing. |
| **no_remote_trace**  boolean | Disable remote tracing.  **Choices:**   - `false` - `true` |
| **trap_groups**  list / elements=dictionary | Specify SNMP trap options. |
| **categories**  dictionary | Specify Trap categories. |
| **authentication**  boolean | Specify Authentication failures.  **Choices:**   - `false` - `true` |
| **chassis**  boolean | Specify Chassis or environment notifications.  **Choices:**   - `false` - `true` |
| **chassis_cluster**  boolean | Specify Clustering notifications.  **Choices:**   - `false` - `true` |
| **configuration**  boolean | Configuration notifications.  **Choices:**   - `false` - `true` |
| **dot3oam_events**  boolean | Specify 802.3ah notifications.  **Choices:**   - `false` - `true` |
| **link**  boolean | Link up-down transitions.  **Choices:**   - `false` - `true` |
| **otn_alarms**  dictionary | OTN alarm trap subcategories. |
| **oc_lof**  boolean | Loss of frame alarm notifications.  **Choices:**   - `false` - `true` |
| **oc_lom**  boolean | Loss of multiframe alarm notification.  **Choices:**   - `false` - `true` |
| **oc_los**  boolean | Loss of signal alarm notification.  **Choices:**   - `false` - `true` |
| **odu_ais**  boolean | ODU Alarm indication signal alarm notification.  **Choices:**   - `false` - `true` |
| **odu_bbe_threshold**  boolean | ODU Background block error threshold alarm notification.  **Choices:**   - `false` - `true` |
| **odu_bdi**  boolean | ODU Backward defect indication alarm notification.  **Choices:**   - `false` - `true` |
| **odu_bdodu_es_threshold**  boolean | ODU Errored Second threshold alarm notification.  **Choices:**   - `false` - `true` |
| **odu_lck**  boolean | ODU Locked alarm notification.  **Choices:**   - `false` - `true` |
| **odu_oci**  boolean | ODU Open connection indicator alarm notifications.  **Choices:**   - `false` - `true` |
| **odu_rx_aps_change**  boolean | ODU Receive APS change notifications.  **Choices:**   - `false` - `true` |
| **odu_sd**  boolean | ODU Signal degrade alarm notifications.  **Choices:**   - `false` - `true` |
| **odu_ses_threshold**  boolean | ODU Severely Errored Second threshold alarm notification.  **Choices:**   - `false` - `true` |
| **odu_sf**  boolean | ODU Signal fail alarm notification.  **Choices:**   - `false` - `true` |
| **odu_ttim**  boolean | ODU Trace identification mismatch alarm notification.  **Choices:**   - `false` - `true` |
| **odu_uas_threshold**  boolean | ODU Unavailable Second threshold alarm notification.  **Choices:**   - `false` - `true` |
| **opu_ptm**  boolean | ODU Payload Type Mismatch alarm notification.  **Choices:**   - `false` - `true` |
| **otu_ais**  boolean | OTU Alarm indication signal alarm notification.  **Choices:**   - `false` - `true` |
| **otu_bbe_threshold**  boolean | OTU Background block error threshold alarm notification.  **Choices:**   - `false` - `true` |
| **otu_bdi**  boolean | OTU Backward defect indication alarm notification.  **Choices:**   - `false` - `true` |
| **otu_es_threshold**  boolean | OTU Errored Second threshold alarm notification.  **Choices:**   - `false` - `true` |
| **otu_fec_deg**  boolean | OTU Fec degraded errors alarm notification.  **Choices:**   - `false` - `true` |
| **otu_fec_exe**  boolean | OTU Fec excessive errors alarm notification.  **Choices:**   - `false` - `true` |
| **otu_iae**  boolean | OTU Incoming alignment error alarm notification.  **Choices:**   - `false` - `true` |
| **otu_sd**  boolean | OTU Signal degrade alarm notification.  **Choices:**   - `false` - `true` |
| **otu_ses_threshold**  boolean | OTU Severely Errored Second threshold alarm notification.  **Choices:**   - `false` - `true` |
| **otu_sf**  boolean | OTU Signal fail alarm notification.  **Choices:**   - `false` - `true` |
| **otu_ttim**  boolean | OTU Trace identification mismatch alarm notification.  **Choices:**   - `false` - `true` |
| **otu_uas_threshold**  boolean | OTU Unavailable Second threshold alarm notification.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set otn_alarms.  **Choices:**   - `false` - `true` |
| **wavelength_lock**  boolean | Wavelength lock alarm notification.  **Choices:**   - `false` - `true` |
| **remote_operations**  boolean | Remote operations.  **Choices:**   - `false` - `true` |
| **rmon_alarm**  boolean | RMON rising and falling alarms.  **Choices:**   - `false` - `true` |
| **routing**  boolean | Routing protocol notifications.  **Choices:**   - `false` - `true` |
| **services**  boolean | Services notifications.  **Choices:**   - `false` - `true` |
| **startup**  boolean | System warm and cold starts.  **Choices:**   - `false` - `true` |
| **vrrp_events**  boolean | VRRP notifications.  **Choices:**   - `false` - `true` |
| **destination_port**  integer | SNMP trap receiver port number |
| **logical_system**  list / elements=string | Use logical-system name for v1/v2c clients. |
| **name**  string | Specify trap group name. |
| **routing_instance**  string | Routing instance for trap destination. |
| **targets**  list / elements=string | Targets for trap messages |
| **version**  string | SNMP version.  **Choices:**   - `"all"` - `"v1"` - `"v2"` |
| **trap_options**  dictionary | SNMP trap options. |
| **agent_address**  dictionary | Agent address for v1 trap PDUs. |
| **outgoing_interface**  boolean | Use address on outgoing interfaces.  **Choices:**   - `false` - `true` |
| **context_oid**  boolean | Add context oid in varbind of all traps at the end.  **Choices:**   - `false` - `true` |
| **enterprise_oid**  boolean | Add snmpTrapEnterprise oid in varbind of all traps.  **Choices:**   - `false` - `true` |
| **logical_system**  list / elements=string | Use logical-system name for v1/v2c clients. |
| **routing_instance**  string | Specify routing-instance. |
| **set**  boolean | Set trap options.  **Choices:**   - `false` - `true` |
| **source_address**  dictionary | IPv4/IPv6 source address for trap PDUs. |
| **address**  string | Use specified address. |
| **lowest_loopback**  boolean | Use lowest address on loopback interfaces.  **Choices:**   - `false` - `true` |
| **views**  list / elements=dictionary | Define MIB views. |
| **name**  string | MIB view name. |
| **oids**  list / elements=dictionary | OID include/exclude list |
| **exclude**  boolean | Exclude this OID from the view.  **Choices:**   - `false` - `true` |
| **include**  boolean | Include this OID from the view.  **Choices:**   - `false` - `true` |
| **oid**  string | OID to include or exclude from view. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show system snmp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"overridden"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_snmp_server_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_snmp_server_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
- name: Merge provided SNMP configuration into running configuration.
  junipernetworks.junos.junos_snmp_server:
    config:
      arp:
        set: true
        host_name_resolution: true
      client_lists:   # ATTR-----2
        - name: cl1
          addresses:
            - address: "192.16.1.0/24"
            - address: "192.16.2.0/24"
            - address: "11.11.11.11"
              restrict: true
        - name: cl2
          addresses:
            - address: "192.16.4.0/24"
      routing_instance_access:  # ATTR-----3
        set: true
        access_lists:
          - "clv1"
          - "clv2"
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "arp": {
#             "host_name_resolution": true
#         },
#         "client_lists": [
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.1.0/24"
#                     },
#                     {
#                         "address": "192.16.2.0/24"
#                     },
#                     {
#                         "address": "11.11.11.11/32",
#                         "restrict": true
#                     }
#                 ],
#                 "name": "cl1"
#             },
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.4.0/24"
#                     }
#                 ],
#                 "name": "cl2"
#             }
#         ],
#         "routing_instance_access": {
#             "access_lists": [
#                 "clv1",
#                 "clv2"
#             ]
#         }
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#           "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#           "<nc:arp><nc:host-name-resolution/></nc:arp><nc:client-list><nc:name>cl1</nc:name>"
#           "<nc:client-address-list><nc:name>192.16.1.0/24</nc:name></nc:client-address-list>"
#           "<nc:client-address-list><nc:name>192.16.2.0/24</nc:name></nc:client-address-list><nc:client-address-list>"
#           "<nc:name>11.11.11.11</nc:name><nc:restrict/></nc:client-address-list></nc:client-list><nc:client-list>"
#           "<nc:name>cl2</nc:name><nc:client-address-list><nc:name>192.16.4.0/24</nc:name></nc:client-address-list>"
#           "</nc:client-list><nc:routing-instance-access><nc:access-list><nc:name>clv1</nc:name></nc:access-list>"
#           "<nc:access-list><nc:name>clv2</nc:name></nc:access-list></nc:routing-instance-access></nc:snmp>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show snmp
# client-list cl1 {
#     192.16.1.0/24;
#     192.16.2.0/24;
#     11.11.11.11/32 {
#         restrict;
#     }
# }
# client-list cl2 {
#     192.16.4.0/24;
# }
# routing-instance-access {
#     access-list {
#         clv1;
#         clv2;
#     }
# }
# arp {
#     host-name-resolution;
# }
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show snmp
# client-list cl1 {
#     192.16.1.0/24;
#     192.16.2.0/24;
#     11.11.11.11/32 {
#         restrict;
#     }
# }
# client-list cl2 {
#     192.16.4.0/24;
# }
# routing-instance-access {
#     access-list {
#         clv1;
#         clv2;
#     }
# }
# arp {
#     host-name-resolution;
# }
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }

- name: Replaced running SNMP server configuration with provided configuration
  junipernetworks.junos.junos_snmp_server:
    config:
      contact: "ansiblesupport11@redhat.com"
      customization:
        ether_stats_ifd_only: true
      description: "Local SNMP Server"
      engine_id:
        local: "local1"
        use_default_ip_address: true
        use_mac_address: true
      filter_duplicates: true
      filter_interfaces:
        set: true
        all_internal_interfaces: true
        interfaces:
          - "eth1"
          - "eth2"
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "contact": "ansiblesupport11@redhat.com",
#         "customization": {
#             "ether_stats_ifd_only": true
#         },
#         "description": "Local SNMP Server",
#         "engine_id": {
#             "use_mac_address": true
#         },
#         "filter_duplicates": true,
#         "filter_interfaces": {
#             "all_internal_interfaces": true,
#             "interfaces": [
#                 "eth1",
#                 "eth2"
#             ]
#         }
#     },
#     "before":
#      {
#         "arp": {
#             "host_name_resolution": true
#         },
#         "client_lists": [
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.1.0/24"
#                     },
#                     {
#                         "address": "192.16.2.0/24"
#                     },
#                     {
#                         "address": "11.11.11.11/32",
#                         "restrict": true
#                     }
#                 ],
#                 "name": "cl1"
#             },
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.4.0/24"
#                     }
#                 ],
#                 "name": "cl2"
#             }
#         ],
#         "routing_instance_access": {
#             "access_lists": [
#                 "clv1",
#                 "clv2"
#             ]
#         }
#     },
#     "changed": true,
#     "commands": [
#         "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"/>",
#         "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" delete="delete"/>",
#         "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:contact>ansiblesupport11@redhat.com</nc:contact><nc:customization>"
#         "<nc:ether-stats-ifd-only/></nc:customization><nc:description>Local SNMP Server</nc:description>"
#         "<nc:engine-id><nc:local>local1</nc:local><nc:use-default-ip-address/><nc:use-mac-address/>"
#         "</nc:engine-id><nc:filter-duplicates/><nc:filter-interfaces><nc:all-internal-interfaces/><nc:interfaces>"
#         "<nc:name>eth1</nc:name></nc:interfaces><nc:interfaces><nc:name>eth2</nc:name></nc:interfaces>"
#         "</nc:filter-interfaces></nc:snmp>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
# vagrant@vsrx# show snmp
# description "Local SNMP Server";
# contact "ansiblesupport11@redhat.com";
# filter-interfaces {
#     interfaces {
#         eth1;
#         eth2;
#     }
#     all-internal-interfaces;
# }
# filter-duplicates;
# engine-id {
#     use-mac-address;
# }
# customization {
#     ether-stats-ifd-only;
# }

# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show snmp
# client-list cl1 {
#     192.16.1.0/24;
#     192.16.2.0/24;
#     11.11.11.11/32 {
#         restrict;
#     }
# }
# client-list cl2 {
#     192.16.4.0/24;
# }
# routing-instance-access {
#     access-list {
#         clv1;
#         clv2;
#     }
# }
# arp {
#     host-name-resolution;
# }
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
- name: Override running SNMP server configuration with provided configuration
  junipernetworks.junos.junos_snmp_server:
    config:
      contact: "ansiblesupport11@redhat.com"
      customization:
        ether_stats_ifd_only: true
      description: "Local SNMP Server"
      engine_id:
        local: "local1"
        use_default_ip_address: true
        use_mac_address: true
      filter_duplicates: true
      filter_interfaces:
        set: true
        all_internal_interfaces: true
        interfaces:
          - "eth1"
          - "eth2"
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "contact": "ansiblesupport11@redhat.com",
#         "customization": {
#             "ether_stats_ifd_only": true
#         },
#         "description": "Local SNMP Server",
#         "engine_id": {
#             "use_mac_address": true
#         },
#         "filter_duplicates": true,
#         "filter_interfaces": {
#             "all_internal_interfaces": true,
#             "interfaces": [
#                 "eth1",
#                 "eth2"
#             ]
#         }
#     },
#     "before":
#      {
#         "arp": {
#             "host_name_resolution": true
#         },
#         "client_lists": [
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.1.0/24"
#                     },
#                     {
#                         "address": "192.16.2.0/24"
#                     },
#                     {
#                         "address": "11.11.11.11/32",
#                         "restrict": true
#                     }
#                 ],
#                 "name": "cl1"
#             },
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.4.0/24"
#                     }
#                 ],
#                 "name": "cl2"
#             }
#         ],
#         "routing_instance_access": {
#             "access_lists": [
#                 "clv1",
#                 "clv2"
#             ]
#         }
#     },
#     "changed": true,
#     "commands": [
#         "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"/>",
#         "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" delete="delete"/>",
#         "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:contact>ansiblesupport11@redhat.com</nc:contact><nc:customization>"
#         "<nc:ether-stats-ifd-only/></nc:customization><nc:description>Local SNMP Server</nc:description>"
#         "<nc:engine-id><nc:local>local1</nc:local><nc:use-default-ip-address/><nc:use-mac-address/>"
#         "</nc:engine-id><nc:filter-duplicates/><nc:filter-interfaces><nc:all-internal-interfaces/><nc:interfaces>"
#         "<nc:name>eth1</nc:name></nc:interfaces><nc:interfaces><nc:name>eth2</nc:name></nc:interfaces>"
#         "</nc:filter-interfaces></nc:snmp>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
# vagrant@vsrx# show snmp
# description "Local SNMP Server";
# contact "ansiblesupport11@redhat.com";
# filter-interfaces {
#     interfaces {
#         eth1;
#         eth2;
#     }
#     all-internal-interfaces;
# }
# filter-duplicates;
# engine-id {
#     use-mac-address;
# }
# customization {
#     ether-stats-ifd-only;
# }
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
# vagrant@vsrx# show snmp
# description "Local SNMP Server";
# contact "ansiblesupport11@redhat.com";
# filter-interfaces {
#     interfaces {
#         eth1;
#         eth2;
#     }
#     all-internal-interfaces;
# }
# filter-duplicates;
# engine-id {
#     use-mac-address;
# }
# customization {
#     ether-stats-ifd-only;
# }
#
- name: Delete running SNMP server configuration
  junipernetworks.junos.junos_snmp_server:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#         "contact": "ansiblesupport11@redhat.com",
#         "customization": {
#             "ether_stats_ifd_only": true
#         },
#         "description": "Local SNMP Server",
#         "engine_id": {
#             "use_mac_address": true
#         },
#         "filter_duplicates": true,
#         "filter_interfaces": {
#             "all_internal_interfaces": true,
#             "interfaces": [
#                 "eth1",
#                 "eth2"
#             ]
#         }
#     },
#     "changed": true,
#     "commands": [
#               "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"/>",
#               "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" delete="delete"/>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show routing-instances
# clv1 {
#     description clv1;
# }
# clv2 {
#     description clv2;
# }
# vagrant@vsrx# show snmp
# description "Local SNMP Server";
# contact "ansiblesupport11@redhat.com";
# filter-interfaces {
#     interfaces {
#         eth1;
#         eth2;
#     }
#     all-internal-interfaces;
# }
# filter-duplicates;
# engine-id {
#     use-mac-address;
# }
# customization {
#     ether-stats-ifd-only;
# }
#
- name: Gather running SNMP server configuration
  junipernetworks.junos.junos_snmp_server:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": {
#         "contact": "ansiblesupport11@redhat.com",
#         "customization": {
#             "ether_stats_ifd_only": true
#         },
#         "description": "Local SNMP Server",
#         "engine_id": {
#             "use_mac_address": true
#         },
#         "filter_duplicates": true,
#         "filter_interfaces": {
#             "all_internal_interfaces": true,
#             "interfaces": [
#                 "eth1",
#                 "eth2"
#             ]
#         }
#     },
#     "changed": false,
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_snmp_server:
    config:
      arp:
        set: true
        host_name_resolution: true
      routing_instance_access:  # ATTR-----3
        set: true
        access_lists:
          - "clv1"
          - "clv2"
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#           "<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#           "<nc:arp><nc:host-name-resolution/></nc:arp><nc:routing-instance-access>"
#           "<nc:access-list><nc:name>clv1</nc:name></nc:access-list><nc:access-list><nc:name>clv2</nc:name>"
#           "</nc:access-list></nc:routing-instance-access></nc:snmp>"
#     ]
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
#            <snmp>
#         <client-list>
#             <name>cl1</name>
#             <client-address-list>
#                 <name>192.16.1.0/24</name>
#             </client-address-list>
#             <client-address-list>
#                 <name>192.16.2.0/24</name>
#             </client-address-list>
#             <client-address-list>
#                 <name>11.11.11.11/32</name>
#                 <restrict/>
#             </client-address-list>
#         </client-list>
#         <client-list>
#             <name>cl2</name>
#             <client-address-list>
#                 <name>192.16.4.0/24</name>
#             </client-address-list>
#         </client-list>
#         <routing-instance-access>
#             <access-list>
#                 <name>clv1</name>
#             </access-list>
#             <access-list>
#                 <name>clv2</name>
#             </access-list>
#         </routing-instance-access>
#         <arp>
#             <host-name-resolution/>
#         </arp>
#     </snmp>
#     </system>
#     </configuration>
# </rpc-reply>
#
- name: Parse SNMP server running config
  junipernetworks.junos.junos_snmp_server:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#         "arp": {
#             "host_name_resolution": true
#         },
#         "client_lists": [
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.1.0/24"
#                     },
#                     {
#                         "address": "192.16.2.0/24"
#                     },
#                     {
#                         "address": "11.11.11.11/32",
#                         "restrict": true
#                     }
#                 ],
#                 "name": "cl1"
#             },
#             {
#                 "addresses": [
#                     {
#                         "address": "192.16.4.0/24"
#                     }
#                 ],
#                 "name": "cl2"
#             }
#         ],
#         "routing_instance_access": {
#             "access_lists": [
#                 "clv1",
#                 "clv2"
#             ]
#         }
#     }
#
#
```

## [Return Values](junos_snmp_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:arp><nc:host-name-resolution/></nc:arp><nc:routing-instance-access>\"", "<nc:snmp xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
