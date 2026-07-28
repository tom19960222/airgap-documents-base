---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_fastl4 module – Manages Fast L4 profiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_fastl4_module.html
fetched_at: 2026-07-28T02:06:58+00:00
---
# f5networks.f5_modules.bigip_profile_fastl4 module – Manages Fast L4 profiles

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_fastl4`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_fastl4_module.md#synopsis)
- [Parameters](bigip_profile_fastl4_module.md#parameters)
- [Notes](bigip_profile_fastl4_module.md#notes)
- [Examples](bigip_profile_fastl4_module.md#examples)
- [Return Values](bigip_profile_fastl4_module.md#return-values)

## [Synopsis](bigip_profile_fastl4_module.md#id1)

- Manages Fast L4 profiles. Using the FastL4 profile can increase virtual server performance and throughput for supported platforms by using the embedded Packet Velocity Acceleration (ePVA) chip to accelerate traffic.

## [Parameters](bigip_profile_fastl4_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_timeout**  string | Specifies a timeout for Late Binding.  This is the time limit for the client to provide the application data required to select a back-end server, meaning the maximum time the BIG-IP system waits for information about the sender and the target.  This information typically arrives at the beginning of the FIX logon packet.  When `0`, or `immediate`, allows for no time beyond the moment of the first packet transmission.  When `indefinite`, disables the limit. This allows the client unlimited time to send the sender and target information. |
| **description**  string | Description of the profile. |
| **explicit_flow_migration**  boolean | Specifies whether a qualified late-binding connection requires an explicit iRule command to migrate down to ePVA hardware.  When `false`, a late-binding connection migrates down to ePVA immediately after establishing the server-side connection.  When `true`, this parameter stops automatic migration to ePVA, and requires the iRule explicitly trigger ePVA processing by invoking the `release_flow` iRule command. This allows an iRule author to control when the connection uses the ePVA hardware.  **Choices:**   - `false` - `true` |
| **hardware_syn_cookie**  boolean | Enables or disables hardware SYN cookie support when PVA10 is present on the system.  **Choices:**   - `false` - `true` |
| **idle_timeout**  string | Specifies the length of time a connection is idle (has no traffic) before the connection is eligible for deletion.  When creating a new profile, if this parameter is not specified, the remote device will choose a default value appropriate for the profile, based on its `parent` profile.  When a number is specified, indicates the number of seconds the TCP connection can remain idle before the system deletes it.  When `indefinite`, specifies the system does not delete TCP connections regardless of how long they remain idle.  When `0`, or `immediate`, specifies the system deletes connections immediately when they become idle. |
| **ip_df_mode**  string | Specifies the Don’t Fragment (DF) bit setting in the IP Header of the outgoing TCP packet.  When `pmtu`, sets the outgoing IP Header DF bit based on IP pmtu setting.  When `preserve`, sets the outgoing Packet’s IP Header DF bit to be same as incoming IP Header DF bit.  When `set`, sets the outgoing packet’s IP Header DF bit.  When `clear`, clears the outgoing packet’s IP Header DF bit.  **Choices:**   - `"pmtu"` - `"preserve"` - `"set"` - `"clear"` |
| **ip_tos_to_client**  string | For IP traffic passing through the system to clients, specifies whether the system modifies the IP type-of-service (ToS) setting in an IP packet header.  May be a number between 0 and 255 (inclusive). When a number, specifies the IP ToS setting that the system inserts in the IP packet header.  When `pass-through`, specifies the IP ToS setting remains unchanged.  When `mimic`, specifies the system sets the ToS level of outgoing packets to the same ToS level of the most-recently received incoming packet. |
| **ip_tos_to_server**  string | For IP traffic passing through the system to back-end servers, specifies whether the system modifies the IP type-of-service (ToS) setting in an IP packet header.  May be a number between 0 and 255 (inclusive). When a number, specifies the IP ToS setting that the system inserts in the IP packet header.  When `pass-through`, specifies that IP ToS setting remains unchanged.  When `mimic`, specifies the system sets the ToS level of outgoing packets to the same ToS level of the most-recently received incoming packet. |
| **ip_ttl_mode**  string | Specifies the outgoing TCP packet’s IP Header TTL mode.  When `proxy`, sets the outgoing IP Header TTL value to 255/64 for IPv4/IPv6 respectively.  When `preserve`, sets the outgoing IP Header TTL value to be same as the incoming IP Header TTL value.  When `decrement`, sets the outgoing IP Header TTL value to be one less than the incoming TTL value.  When `set`, sets the outgoing IP Header TTL value to a specific value(as specified by `ip_ttl_v4` or `ip_ttl_v6`.  **Choices:**   - `"proxy"` - `"preserve"` - `"decrement"` - `"set"` |
| **ip_ttl_v4**  integer | Specifies the outgoing packet’s IP Header TTL value for IPv4 traffic.  The maximum TTL value is 255. |
| **ip_ttl_v6**  integer | Specifies the outgoing packet’s IP Header TTL value for IPv6 traffic.  The maximum TTL value is 255. |
| **keep_alive_interval**  integer | Specifies the keep-alive probe interval, in seconds. |
| **late_binding**  boolean | Enables intelligent selection of a back-end server or pool, using an iRule to make the selection.  Enabling `late_binding` on BIG-IP running TMOS 12.x branch requires software syn cookie is enabled.  **Choices:**   - `false` - `true` |
| **link_qos_to_client**  string | For IP traffic passing through the system to clients, specifies whether the system modifies the link quality-of-service (QoS) setting in an IP packet header.  The link QoS value prioritizes the IP packet relative to other Layer 2 traffic.  You can specify a number between 0 (lowest priority) and 7 (highest priority).  When a number, specifies the link QoS setting that the system inserts in the IP packet header.  When `pass-through`, specifies the link QoS setting remains unchanged. |
| **link_qos_to_server**  string | For IP traffic passing through the system to back-end servers, specifies whether the system modifies the link quality-of-service (QoS) setting in an IP packet header.  The link QoS value prioritizes the IP packet relative to other Layer 2 traffic.  You can specify a number between 0 (lowest priority) and 7 (highest priority).  When a number, specifies the link QoS setting that the system inserts in the IP packet header.  When `pass-through`, specifies the link QoS setting remains unchanged. |
| **loose_close**  boolean | When `true`, specifies the system closes a loosely-initiated connection when the system receives the first FIN packet from either the client or the server.  **Choices:**   - `false` - `true` |
| **loose_initialization**  boolean | When `true`, specifies the system initializes a connection when it receives any TCP packet, rather than requiring a SYN packet for connection initiation.  **Choices:**   - `false` - `true` |
| **mss_override**  integer | Specifies a maximum segment size (MSS) override for server-side connections.  Valid range is 256 to 9162 or 0 to disable. |
| **name**  string / required | Specifies the name of the profile. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `fastL4` profile. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **pva_acceleration**  string  *added in f5networks.f5_modules 1.3.0* | Specifies the Packet Velocity ASIC acceleration policy.  **Choices:**   - `"full"` - `"dedicated"` - `"partial"` - `"none"` |
| **reassemble_fragments**  boolean | When `true`, specifies the system reassembles IP fragments.  **Choices:**   - `false` - `true` |
| **receive_window_size**  integer | Specifies the amount of data the BIG-IP system can accept without acknowledging the server. |
| **reset_on_timeout**  boolean | When `true`, specifies the system sends a reset packet (RST) in addition to deleting the connection, when a connection exceeds the idle timeout value.  **Choices:**   - `false` - `true` |
| **rtt_from_client**  boolean | When `true`, specifies the system uses TCP timestamp options to measure the round-trip time to the client.  **Choices:**   - `false` - `true` |
| **rtt_from_server**  boolean | When `true`, specifies the system uses TCP timestamp options to measure the round-trip time to the server.  **Choices:**   - `false` - `true` |
| **server_sack**  boolean | Specifies whether the BIG-IP system processes Selective ACK (Sack) packets in cookie responses from the server.  **Choices:**   - `false` - `true` |
| **server_timestamp**  boolean | Specifies whether the BIG-IP system processes timestamp request packets in cookie responses from the server.  **Choices:**   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **syn_cookie_enable**  boolean  *added in f5networks.f5_modules 1.11.0* | Specifies whether or not to use SYN Cookie.  **Choices:**   - `false` - `true` |
| **syn_cookie_mss**  integer | Specifies a value that overrides the SYN cookie maximum segment size (MSS) value in the SYN-ACK packet that is returned to the client.  Valid values are 0, and values from 256 through 9162.  Parameter only available on TMOS 13.0.0 and higher. |
| **tcp_close_timeout**  string | Specifies the length of time a connection can remain idle before deletion. |
| **tcp_generate_isn**  boolean | When `true`, specifies the system generates initial sequence numbers for SYN packets, according to RFC 1948.  **Choices:**   - `false` - `true` |
| **tcp_handshake_timeout**  string | Specifies the acceptable duration for a TCP handshake (the maximum idle time between a client synchronization (SYN) and a client acknowledgment (ACK)). If the TCP handshake takes longer than the timeout, the system automatically closes the connection.  When a number, specifies how long the system can try to establish a TCP handshake before timing out.  When `disabled`, specifies the system does not apply a timeout to a TCP handshake.  When `indefinite`, specifies attempting a TCP handshake never times out. |
| **tcp_strip_sack**  boolean | When `true`, specifies the system blocks a TCP selective ACK SackOK option from passing to the server on an initiating SYN.  **Choices:**   - `false` - `true` |
| **tcp_time_wait_timeout**  integer | Specifies the number of milliseconds a connection is in the TIME-WAIT state before closing.  This parameter is only available on TMOS 13.0.0 and later. |
| **tcp_timestamp_mode**  string | Specifies the action the system should take on TCP timestamps.  **Choices:**   - `"preserve"` - `"rewrite"` - `"strip"` |
| **tcp_wscale_mode**  string | Specifies the action the system should take on TCP windows.  **Choices:**   - `"preserve"` - `"rewrite"` - `"strip"` |
| **timeout_recovery**  string | Specifies how to handle client-timeout errors for Late Binding.  Timeout errors may be caused by a DoS attack or a lossy connection.  When `disconnect`, causes the BIG-IP system to drop the connection.  When `fallback`, reverts the connection to normal FastL4 load-balancing, based on the client’s TCP header. This causes the BIG-IP system to choose a back-end server based only on the source address and port.  **Choices:**   - `"disconnect"` - `"fallback"` |

## [Notes](bigip_profile_fastl4_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_fastl4_module.md#id4)

```yaml+jinja
- name: Create a fastL4 profile
  bigip_profile_fastl4:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_fastl4_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **client_timeout**  string | The new client timeout value of the resource.  **Returned:** changed  **Sample:** `"True"` |
| **description**  string | The new description.  **Returned:** changed  **Sample:** `"My description"` |
| **explicit_flow_migration**  boolean | The new flow migration setting.  **Returned:** changed  **Sample:** `true` |
| **hardware_syn_cookie**  boolean | Enables or disables hardware SYN cookie support when PVA10 is present on the system.  **Returned:** changed  **Sample:** `false` |
| **idle_timeout**  string | The new idle timeout setting.  **Returned:** changed  **Sample:** `"123"` |
| **ip_df_mode**  string | The new Don’t Fragment Flag (DF) setting.  **Returned:** changed  **Sample:** `"clear"` |
| **ip_tos_to_client**  string | The new IP ToS to Client setting.  **Returned:** changed  **Sample:** `"100"` |
| **ip_tos_to_server**  string | The new IP ToS to Server setting.  **Returned:** changed  **Sample:** `"100"` |
| **ip_ttl_mode**  string | The new Time To Live (TTL) setting.  **Returned:** changed  **Sample:** `"proxy"` |
| **ip_ttl_v4**  integer | The new Time To Live (TTL) v4 setting.  **Returned:** changed  **Sample:** `200` |
| **ip_ttl_v6**  integer | The new Time To Live (TTL) v6 setting.  **Returned:** changed  **Sample:** `200` |
| **keep_alive_interval**  integer | The new TCP Keep Alive Interval setting.  **Returned:** changed  **Sample:** `100` |
| **late_binding**  boolean | The new Late Binding setting.  **Returned:** changed  **Sample:** `true` |
| **link_qos_to_client**  string | The new Link QoS to Client setting.  **Returned:** changed  **Sample:** `"pass-through"` |
| **link_qos_to_server**  string | The new Link QoS to Server setting.  **Returned:** changed  **Sample:** `"123"` |
| **loose_close**  boolean | The new Loose Close setting.  **Returned:** changed  **Sample:** `false` |
| **loose_initialization**  boolean | The new Loose Initiation setting.  **Returned:** changed  **Sample:** `false` |
| **mss_override**  integer | The new Maximum Segment Size Override setting.  **Returned:** changed  **Sample:** `300` |
| **pva_acceleration**  string | Specifies the Packet Velocity ASIC acceleration policy.  **Returned:** changed  **Sample:** `"full"` |
| **reassemble_fragments**  boolean | The new Reassemble IP Fragments setting.  **Returned:** changed  **Sample:** `true` |
| **receive_window_size**  integer | The new Receive Window setting.  **Returned:** changed  **Sample:** `1024` |
| **reset_on_timeout**  boolean | The new Reset on Timeout setting.  **Returned:** changed  **Sample:** `false` |
| **rtt_from_client**  boolean | The new RTT from Client setting.  **Returned:** changed  **Sample:** `false` |
| **rtt_from_server**  boolean | The new RTT from Server setting.  **Returned:** changed  **Sample:** `false` |
| **server_sack**  boolean | The new Server Sack setting.  **Returned:** changed  **Sample:** `true` |
| **server_timestamp**  boolean | The new Server Timestamp setting.  **Returned:** changed  **Sample:** `true` |
| **syn_cookie_enable**  boolean | Specifies whether or not to use SYN Cookie.  **Returned:** changed  **Sample:** `false` |
| **syn_cookie_mss**  integer | The new SYN Cookie MSS setting.  **Returned:** changed  **Sample:** `1024` |
| **tcp_close_timeout**  string | The new TCP Close Timeout setting.  **Returned:** changed  **Sample:** `"100"` |
| **tcp_generate_isn**  boolean | The new Generate Initial Sequence Number setting.  **Returned:** changed  **Sample:** `false` |
| **tcp_handshake_timeout**  integer | The new TCP Handshake Timeout setting.  **Returned:** changed  **Sample:** `5` |
| **tcp_strip_sack**  boolean | The new Strip Sack OK setting.  **Returned:** changed  **Sample:** `false` |
| **tcp_time_wait_timeout**  integer | The new TCP Time Wait Timeout setting.  **Returned:** changed  **Sample:** `100` |
| **tcp_timestamp_mode**  string | The new TCP Timestamp Mode setting.  **Returned:** changed  **Sample:** `"rewrite"` |
| **tcp_wscale_mode**  string | The new TCP Window Scale Mode setting.  **Returned:** changed  **Sample:** `"strip"` |
| **timeout_recovery**  string | The new Timeout Recovery setting.  **Returned:** changed  **Sample:** `"fallback"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
