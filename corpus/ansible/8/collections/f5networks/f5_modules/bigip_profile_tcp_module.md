---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_tcp module – Manage TCP profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_tcp_module.html
fetched_at: 2026-07-28T02:07:06+00:00
---
# f5networks.f5_modules.bigip_profile_tcp module – Manage TCP profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_tcp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_tcp_module.md#synopsis)
- [Parameters](bigip_profile_tcp_module.md#parameters)
- [Notes](bigip_profile_tcp_module.md#notes)
- [Examples](bigip_profile_tcp_module.md#examples)
- [Return Values](bigip_profile_tcp_module.md#return-values)

## [Synopsis](bigip_profile_tcp_module.md#id1)

- Manage TCP profiles on a BIG-IP system. There are many TCP profiles, each with their own adjustments to the standard `tcp` profile. Users of this module should be aware that many of the available options have no module default. Instead, the default is assigned by the BIG-IP system itself which, in most cases, is acceptable.

## [Parameters](bigip_profile_tcp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delayed_acks**  boolean | When `true`, the system sends fewer than one ACK segment per data segment received.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **early_retransmit**  boolean | When `true`, the system uses early fast retransmits to reduce the recovery time for connections that are receive-buffer or user-data limited.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **idle_timeout**  string | Specifies the length of time a connection is idle (has no traffic) before the connection is eligible for deletion.  When creating a new profile, if this parameter is not specified, the remote device will choose a default value appropriate for the profile, based on its `parent` profile.  When a number is specified, indicates the number of seconds the TCP connection can remain idle before the system deletes it.  When `0`, or `indefinite`, specifies the system does not delete TCP connections regardless of how long they remain idle. |
| **initial_congestion_window_size**  integer | Specifies the initial congestion window size for connections to this destination. The actual window size is this value multiplied by the MSS for the same connection.  When set to `0`, the system uses the values specified in RFC2414.  The valid value range is 0 - 16 inclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **initial_receive_window_size**  integer | Specifies the initial receive window size for connections to this destination. The actual window size is this value multiplied by the MSS for the same connection.  When set to `0`, the system uses the Slow Start value.  The valid value range is 0 - 16 inclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **ip_tos_to_client**  string | Specifies the L3 Type of Service level the system inserts in TCP packets destined for clients.  When `pass-through`, the IP ToS setting remains unchanged.  When `mimic`, the system sets the ToS level of outgoing packets to the same ToS level of the most-recently received incoming packet.  When set as a number, the number indicates the IP ToS setting the system inserts in the IP packet header. Valid number range is 0 - 255 inclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **keep_alive_interval**  string  *added in f5networks.f5_modules 1.22.0* | Specifies how frequently the system sends data over an idle TCP connection, to determine whether the connection is still valid.  When creating a new profile, if this parameter is not specified, the remote device will choose a default value appropriate for the profile, based on its `parent` profile.  When `0`, or `indefinite`, specifies that the system does not send keep-alive communication. |
| **nagle**  string | When `enabled` the system applies Nagle’s algorithm to reduce the number of short segments on the network.  When `auto`, the use of Nagle’s algorithm is decided based on network conditions.  For interactive protocols such as Telnet, rlogin, or SSH, F5 recommends disabling this setting on high-latency networks, to improve application responsiveness.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `"auto"` - `"enabled"` - `"disabled"` |
| **name**  string / required | Specifies the name of the profile. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `tcp` profile. |
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
| **proxy_options**  boolean | When `true`, the system advertises an option, such as a time-stamp, to the server only if it was negotiated with the client.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **syn_rto_base**  integer | Specifies the initial RTO `Retransmission TimeOut` base multiplier for SYN retransmission, in `milliseconds`.  This value is modified by the exponential backoff table to select the interval for subsequent retransmissions.  The valid value range is 0 - 5000 inclusive.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **time_wait_recycle**  boolean | Specifies connections in a TIME-WAIT state are reused if a SYN packet (indicating a request for a new connection) is received.  When `false`, connections in a TIME-WAIT state remain unused for a specified length of time.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **time_wait_timeout**  string  *added in f5networks.f5_modules 1.3.0* | Specifies the number of milliseconds a connection is in the TIME-WAIT state before closing.  When `immediate`, the system closes the connection immediately after the connection enters the TIME-WAIT state.  When `indefinite` or `0`, the system does not close TCP connections regardless of how long they remain in the TIME-WAIT state.  The valid number range is from 0 to 600000 milliseconds.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |

## [Notes](bigip_profile_tcp_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_tcp_module.md#id4)

```yaml+jinja
- name: Create a TCP profile
  bigip_profile_tcp:
    name: foo
    parent: f5-tcp-progressive
    time_wait_recycle: false
    idle_timeout: 300
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_profile_tcp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **delayed_acks**  boolean | Specifies if the system sends fewer than one ACK segment per data segment received.  **Returned:** changed  **Sample:** `true` |
| **early_retransmit**  boolean | Specifies the use of early fast retransmits.  **Returned:** changed  **Sample:** `true` |
| **idle_timeout**  integer | The new idle timeout of the resource.  **Returned:** changed  **Sample:** `100` |
| **initial_congestion_window_size**  integer | Specifies the initial congestion window size for connections to this destination.  **Returned:** changed  **Sample:** `5` |
| **initial_receive_window_size**  integer | Specifies the initial receive window size for connections to this destination.  **Returned:** changed  **Sample:** `10` |
| **ip_tos_to_client**  string | Specifies the L3 Type of Service level that the system inserts in TCP packets destined for clients.  **Returned:** changed  **Sample:** `"mimic"` |
| **keep_alive_interval**  string | Specifies how frequently the system sends data over an idle TCP connection.  **Returned:** changed  **Sample:** `"indefinite"` |
| **nagle**  string | Specifies the use of Nagle’s algorithm.  **Returned:** changed  **Sample:** `"auto"` |
| **parent**  string | The new parent of the resource.  **Returned:** changed  **Sample:** `"f5-tcp-optimized"` |
| **proxy_options**  boolean | Specifies if the system advertises negotiated options to the server.  **Returned:** changed  **Sample:** `false` |
| **syn_rto_base**  integer | Specifies the initial Retransmission TimeOut base multiplier for SYN retransmission.  **Returned:** changed  **Sample:** `2000` |
| **time_wait_recycle**  boolean | Reuse connections in TIME-WAIT state.  **Returned:** changed  **Sample:** `true` |
| **time_wait_timeout**  string | Specifies the number of milliseconds that a connection is in the TIME-WAIT state before closing.  **Returned:** changed  **Sample:** `"immediate"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
