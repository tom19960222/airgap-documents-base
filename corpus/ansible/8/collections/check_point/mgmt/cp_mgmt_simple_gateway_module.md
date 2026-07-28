---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_simple_gateway module – Manages simple-gateway objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_simple_gateway_module.html
fetched_at: 2026-07-28T01:17:57+00:00
---
# check_point.mgmt.cp_mgmt_simple_gateway module – Manages simple-gateway objects on Check Point over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_simple_gateway`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_simple_gateway_module.md#synopsis)
- [Parameters](cp_mgmt_simple_gateway_module.md#parameters)
- [Examples](cp_mgmt_simple_gateway_module.md#examples)
- [Return Values](cp_mgmt_simple_gateway_module.md#return-values)

## [Synopsis](cp_mgmt_simple_gateway_module.md#id1)

- Manages simple-gateway objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_simple_gateway_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **anti_bot**  boolean | Anti-Bot blade enabled.  **Choices:**   - `false` - `true` |
| **anti_virus**  boolean | Anti-Virus blade enabled.  **Choices:**   - `false` - `true` |
| **application_control**  boolean | Application Control blade enabled.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **content_awareness**  boolean | Content Awareness blade enabled.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **firewall**  boolean | Firewall blade enabled.  **Choices:**   - `false` - `true` |
| **firewall_settings**  dictionary | N/A |
| **auto_calculate_connections_hash_table_size_and_memory_pool**  boolean | N/A  **Choices:**   - `false` - `true` |
| **auto_maximum_limit_for_concurrent_connections**  boolean | N/A  **Choices:**   - `false` - `true` |
| **connections_hash_size**  integer | N/A |
| **maximum_limit_for_concurrent_connections**  integer | N/A |
| **maximum_memory_pool_size**  integer | N/A |
| **memory_pool_size**  integer | N/A |
| **gateway_version**  string | Gateway platform version. |
| **groups**  list / elements=string | Collection of group identifiers. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | Network interfaces. When a gateway is updated with a new interfaces, the existing interfaces are removed. |
| **anti_spoofing**  boolean | N/A  **Choices:**   - `false` - `true` |
| **anti_spoofing_settings**  dictionary | N/A |
| **action**  string | If packets will be rejected (the Prevent option) or whether the packets will be monitored (the Detect option).  **Choices:**   - `"prevent"` - `"detect"` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv4_mask_length**  string | IPv4 network mask length. |
| **ipv4_network_mask**  string | IPv4 network address. |
| **ipv6_address**  string | IPv6 address. |
| **ipv6_mask_length**  string | IPv6 network mask length. |
| **ipv6_network_mask**  string | IPv6 network address. |
| **mask_length**  string | IPv4 or IPv6 network mask length. |
| **name**  string | Object name. |
| **network_mask**  string | IPv4 or IPv6 network mask. If both masks are required use ipv4-network-mask and ipv6-network-mask fields explicitly. Instead of providing mask itself it is possible to specify IPv4 or IPv6 mask length in mask-length field. If both masks length are required use ipv4-mask-length and ipv6-mask-length fields explicitly. |
| **security_zone**  boolean | N/A  **Choices:**   - `false` - `true` |
| **security_zone_settings**  dictionary | N/A |
| **auto_calculated**  boolean | Security Zone is calculated according to where the interface leads to.  **Choices:**   - `false` - `true` |
| **specific_zone**  string | Security Zone specified manually. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **topology**  string | N/A  **Choices:**   - `"automatic"` - `"external"` - `"internal"` |
| **topology_settings**  dictionary | N/A |
| **interface_leads_to_dmz**  boolean | Whether this interface leads to demilitarized zone (perimeter network).  **Choices:**   - `false` - `true` |
| **ip_address_behind_this_interface**  string | N/A  **Choices:**   - `"not defined"` - `"network defined by the interface ip and net mask"` - `"network defined by routing"` - `"specific"` |
| **specific_network**  string | Network behind this interface. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ips**  boolean | Intrusion Prevention System blade enabled.  **Choices:**   - `false` - `true` |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **logs_settings**  dictionary | N/A |
| **alert_when_free_disk_space_below**  boolean | N/A  **Choices:**   - `false` - `true` |
| **alert_when_free_disk_space_below_threshold**  integer | N/A |
| **alert_when_free_disk_space_below_type**  string | N/A  **Choices:**   - `"none"` - `"log"` - `"popup alert"` - `"mail alert"` - `"snmp trap alert"` - `"user defined alert no.1"` - `"user defined alert no.2"` - `"user defined alert no.3"` |
| **before_delete_keep_logs_from_the_last_days**  boolean | N/A  **Choices:**   - `false` - `true` |
| **before_delete_keep_logs_from_the_last_days_threshold**  integer | N/A |
| **before_delete_run_script**  boolean | N/A  **Choices:**   - `false` - `true` |
| **before_delete_run_script_command**  string | N/A |
| **delete_index_files_older_than_days**  boolean | N/A  **Choices:**   - `false` - `true` |
| **delete_index_files_older_than_days_threshold**  integer | N/A |
| **delete_index_files_when_index_size_above**  boolean | N/A  **Choices:**   - `false` - `true` |
| **delete_index_files_when_index_size_above_threshold**  integer | N/A |
| **delete_when_free_disk_space_below**  boolean | N/A  **Choices:**   - `false` - `true` |
| **delete_when_free_disk_space_below_threshold**  integer | N/A |
| **detect_new_citrix_ica_application_names**  boolean | N/A  **Choices:**   - `false` - `true` |
| **forward_logs_to_log_server**  boolean | N/A  **Choices:**   - `false` - `true` |
| **forward_logs_to_log_server_name**  string | N/A |
| **forward_logs_to_log_server_schedule_name**  string | N/A |
| **free_disk_space_metrics**  string | N/A  **Choices:**   - `"mbytes"` - `"percent"` |
| **perform_log_rotate_before_log_forwarding**  boolean | N/A  **Choices:**   - `false` - `true` |
| **reject_connections_when_free_disk_space_below_threshold**  boolean | N/A  **Choices:**   - `false` - `true` |
| **reserve_for_packet_capture_metrics**  string | N/A  **Choices:**   - `"percent"` - `"mbytes"` |
| **reserve_for_packet_capture_threshold**  integer | N/A |
| **rotate_log_by_file_size**  boolean | N/A  **Choices:**   - `false` - `true` |
| **rotate_log_file_size_threshold**  integer | N/A |
| **rotate_log_on_schedule**  boolean | N/A  **Choices:**   - `false` - `true` |
| **rotate_log_schedule_name**  string | N/A |
| **stop_logging_when_free_disk_space_below**  boolean | N/A  **Choices:**   - `false` - `true` |
| **stop_logging_when_free_disk_space_below_threshold**  integer | N/A |
| **turn_on_qos_logging**  boolean | N/A  **Choices:**   - `false` - `true` |
| **update_account_log_every**  integer | N/A |
| **name**  string / required | Object name. |
| **one_time_password**  string | N/A |
| **os_name**  string | Gateway platform operating system. |
| **save_logs_locally**  boolean | Save logs locally on the gateway.  **Choices:**   - `false` - `true` |
| **send_alerts_to_server**  list / elements=string | Server(s) to send alerts to. |
| **send_logs_to_backup_server**  list / elements=string | Backup server(s) to send logs to. |
| **send_logs_to_server**  list / elements=string | Server(s) to send logs to. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **threat_emulation**  boolean | Threat Emulation blade enabled.  **Choices:**   - `false` - `true` |
| **threat_extraction**  boolean | Threat Extraction blade enabled.  **Choices:**   - `false` - `true` |
| **url_filtering**  boolean | URL Filtering blade enabled.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **vpn**  boolean | VPN blade enabled.  **Choices:**   - `false` - `true` |
| **vpn_settings**  dictionary | Gateway VPN settings. |
| **maximum_concurrent_ike_negotiations**  integer | N/A |
| **maximum_concurrent_tunnels**  integer | N/A |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_simple_gateway_module.md#id3)

```yaml+jinja
- name: add-simple-gateway
  cp_mgmt_simple_gateway:
    ip_address: 192.0.2.1
    name: gw1
    state: present

- name: set-simple-gateway
  cp_mgmt_simple_gateway:
    anti_bot: true
    anti_virus: true
    application_control: true
    ips: true
    name: test_gateway
    state: present
    threat_emulation: true
    url_filtering: true

- name: delete-simple-gateway
  cp_mgmt_simple_gateway:
    name: gw1
    state: absent
```

## [Return Values](cp_mgmt_simple_gateway_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_simple_gateway**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
