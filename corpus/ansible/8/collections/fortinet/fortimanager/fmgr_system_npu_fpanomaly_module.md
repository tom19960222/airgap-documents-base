---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_npu_fpanomaly module – NP6Lite anomaly protection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_npu_fpanomaly_module.html
fetched_at: 2026-07-28T02:19:21+00:00
---
# fortinet.fortimanager.fmgr_system_npu_fpanomaly module – NP6Lite anomaly protection

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_npu_fpanomaly`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_system_npu_fpanomaly_module.md#synopsis)
- [Parameters](fmgr_system_npu_fpanomaly_module.md#parameters)
- [Notes](fmgr_system_npu_fpanomaly_module.md#notes)
- [Examples](fmgr_system_npu_fpanomaly_module.md#examples)
- [Return Values](fmgr_system_npu_fpanomaly_module.md#return-values)

## [Synopsis](fmgr_system_npu_fpanomaly_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_npu_fpanomaly_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_npu_fpanomaly**  dictionary | the top level parameters set |
| **capwap-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **esp-minlen-err**  string | Invalid IPv4 ESP short packet anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **gre-csum-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **gtpu-plen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **icmp-csum-err**  string | Invalid IPv4 ICMP packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **icmp-frag**  string | Layer 3 fragmented packets that could be part of layer 4 ICMP anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **icmp-land**  string | ICMP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **icmp-minlen-err**  string | Invalid IPv4 ICMP short packet anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-csum-err**  string | Invalid IPv4 packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-ihl-err**  string | Invalid IPv4 header length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-land**  string | Land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-len-err**  string | Invalid IPv4 packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-opt-err**  string | Invalid IPv4 option parsing anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-optlsrr**  string | Loose source record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optrr**  string | Record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optsecurity**  string | Security option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optssrr**  string | Strict source record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optstream**  string | Stream option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-opttimestamp**  string | Timestamp option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-proto-err**  string | Invalid layer 4 protocol anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-ttlzero-err**  string | Invalid IPv4 TTL field zero anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-unknopt**  string | Unknown option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-ver-err**  string | Invalid IPv4 header version anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-daddr-err**  string | Destination address as unspecified or loopback address anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-len-err**  string | Invalid IPv6 packet chain extension header total length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-order-err**  string | Invalid IPv6 packet extension header ordering anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-ihl-err**  string | Invalid IPv6 packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-land**  string | Land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optendpid**  string | End point identification anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-opthomeaddr**  string | Home address option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optinvld**  string | Invalid option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optjumbo**  string | Jumbo options anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optnsap**  string | Network service access point address option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optralert**  string | Router alert option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-opttunnel**  string | Tunnel encapsulation limit option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-plen-zero**  string | Invalid IPv6 packet payload length zero anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-proto-err**  string | Layer 4 invalid protocol anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-saddr-err**  string | Source address as multicast anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-unknopt**  string | Unknown option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-ver-err**  string | Invalid IPv6 packet version anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **nvgre-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **sctp-clen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **sctp-crc-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **sctp-l4len-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-csum-err**  string | Invalid IPv4 TCP packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-fin-noack**  string | TCP SYN flood with FIN flag set without ACK setting anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-fin-only**  string | TCP SYN flood with only FIN flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-hlen-err**  string | Invalid IPv4 TCP header length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-hlenvsl4len-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-land**  string | TCP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-no-flag**  string | TCP SYN flood with no flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-plen-err**  string | Invalid IPv4 TCP packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-syn-data**  string | TCP SYN flood packets with data anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-syn-fin**  string | TCP SYN flood SYN/FIN flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-winnuke**  string | TCP WinNuke anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **udp-csum-err**  string | Invalid IPv4 UDP packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp-hlen-err**  string | Invalid IPv4 UDP packet header length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp-land**  string | UDP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **udp-len-err**  string | Invalid IPv4 UDP packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp-plen-err**  string | Invalid IPv4 UDP packet minimum length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udplite-cover-err**  string | Invalid IPv4 UDP-Lite packet coverage anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udplite-csum-err**  string | Invalid IPv4 UDP-Lite packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **uesp-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **unknproto-minlen-err**  string | Invalid IPv4 L4 unknown protocol short packet anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **vxlan-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_npu_fpanomaly_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_npu_fpanomaly_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: NP6Lite anomaly protection
      fmgr_system_npu_fpanomaly:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_npu_fpanomaly:
          esp-minlen-err: <value in [drop, trap-to-host]>
          icmp-csum-err: <value in [drop, trap-to-host]>
          icmp-minlen-err: <value in [drop, trap-to-host]>
          ipv4-csum-err: <value in [drop, trap-to-host]>
          ipv4-ihl-err: <value in [drop, trap-to-host]>
          ipv4-len-err: <value in [drop, trap-to-host]>
          ipv4-opt-err: <value in [drop, trap-to-host]>
          ipv4-ttlzero-err: <value in [drop, trap-to-host]>
          ipv4-ver-err: <value in [drop, trap-to-host]>
          ipv6-exthdr-len-err: <value in [drop, trap-to-host]>
          ipv6-exthdr-order-err: <value in [drop, trap-to-host]>
          ipv6-ihl-err: <value in [drop, trap-to-host]>
          ipv6-plen-zero: <value in [drop, trap-to-host]>
          ipv6-ver-err: <value in [drop, trap-to-host]>
          tcp-csum-err: <value in [drop, trap-to-host]>
          tcp-hlen-err: <value in [drop, trap-to-host]>
          tcp-plen-err: <value in [drop, trap-to-host]>
          udp-csum-err: <value in [drop, trap-to-host]>
          udp-hlen-err: <value in [drop, trap-to-host]>
          udp-len-err: <value in [drop, trap-to-host]>
          udp-plen-err: <value in [drop, trap-to-host]>
          udplite-cover-err: <value in [drop, trap-to-host]>
          udplite-csum-err: <value in [drop, trap-to-host]>
          unknproto-minlen-err: <value in [drop, trap-to-host]>
          tcp-fin-only: <value in [allow, drop, trap-to-host]>
          ipv4-optsecurity: <value in [allow, drop, trap-to-host]>
          ipv6-optralert: <value in [allow, drop, trap-to-host]>
          tcp-syn-fin: <value in [allow, drop, trap-to-host]>
          ipv4-proto-err: <value in [allow, drop, trap-to-host]>
          ipv6-saddr-err: <value in [allow, drop, trap-to-host]>
          icmp-frag: <value in [allow, drop, trap-to-host]>
          ipv4-optssrr: <value in [allow, drop, trap-to-host]>
          ipv6-opthomeaddr: <value in [allow, drop, trap-to-host]>
          udp-land: <value in [allow, drop, trap-to-host]>
          ipv6-optinvld: <value in [allow, drop, trap-to-host]>
          tcp-fin-noack: <value in [allow, drop, trap-to-host]>
          ipv6-proto-err: <value in [allow, drop, trap-to-host]>
          tcp-land: <value in [allow, drop, trap-to-host]>
          ipv4-unknopt: <value in [allow, drop, trap-to-host]>
          ipv4-optstream: <value in [allow, drop, trap-to-host]>
          ipv6-optjumbo: <value in [allow, drop, trap-to-host]>
          icmp-land: <value in [allow, drop, trap-to-host]>
          tcp-winnuke: <value in [allow, drop, trap-to-host]>
          ipv6-daddr-err: <value in [allow, drop, trap-to-host]>
          ipv4-land: <value in [allow, drop, trap-to-host]>
          ipv6-opttunnel: <value in [allow, drop, trap-to-host]>
          tcp-no-flag: <value in [allow, drop, trap-to-host]>
          ipv6-land: <value in [allow, drop, trap-to-host]>
          ipv4-optlsrr: <value in [allow, drop, trap-to-host]>
          ipv4-opttimestamp: <value in [allow, drop, trap-to-host]>
          ipv4-optrr: <value in [allow, drop, trap-to-host]>
          ipv6-optnsap: <value in [allow, drop, trap-to-host]>
          ipv6-unknopt: <value in [allow, drop, trap-to-host]>
          tcp-syn-data: <value in [allow, drop, trap-to-host]>
          ipv6-optendpid: <value in [allow, drop, trap-to-host]>
          gtpu-plen-err: <value in [drop, trap-to-host]>
          vxlan-minlen-err: <value in [drop, trap-to-host]>
          capwap-minlen-err: <value in [drop, trap-to-host]>
          gre-csum-err: <value in [drop, trap-to-host]>
          nvgre-minlen-err: <value in [drop, trap-to-host]>
          sctp-l4len-err: <value in [drop, trap-to-host]>
          tcp-hlenvsl4len-err: <value in [drop, trap-to-host]>
          sctp-crc-err: <value in [drop, trap-to-host]>
          sctp-clen-err: <value in [drop, trap-to-host]>
          uesp-minlen-err: <value in [drop, trap-to-host]>
```

## [Return Values](fmgr_system_npu_fpanomaly_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
