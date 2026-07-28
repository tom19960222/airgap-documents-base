---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_np6 module – Configure NP6 attributes in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_np6_module.html
fetched_at: 2026-07-28T02:28:48+00:00
---
# fortinet.fortios.fortios_system_np6 module – Configure NP6 attributes in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_np6_module.md#ansible-collections-fortinet-fortios-fortios-system-np6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_np6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_np6_module.md#synopsis)
- [Requirements](fortios_system_np6_module.md#requirements)
- [Parameters](fortios_system_np6_module.md#parameters)
- [Notes](fortios_system_np6_module.md#notes)
- [Examples](fortios_system_np6_module.md#examples)
- [Return Values](fortios_system_np6_module.md#return-values)

## [Synopsis](fortios_system_np6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and np6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_np6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_np6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_np6**  dictionary | Configure NP6 attributes. |
| **fastpath**  string | Enable/disable NP6 offloading (also called fast path).  **Choices:**   - `"disable"` - `"enable"` |
| **fp_anomaly**  dictionary | NP6 IPv4 anomaly protection. trap-to-host forwards anomaly sessions to the CPU. |
| **icmp_csum_err**  string | Invalid IPv4 ICMP checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **icmp_frag**  string | Layer 3 fragmented packets that could be part of layer 4 ICMP anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **icmp_land**  string | ICMP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_csum_err**  string | Invalid IPv4 IP checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4_land**  string | Land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_optlsrr**  string | Loose source record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_optrr**  string | Record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_optsecurity**  string | Security option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_optssrr**  string | Strict source record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_optstream**  string | Stream option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_opttimestamp**  string | Timestamp option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_proto_err**  string | Invalid layer 4 protocol anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4_unknopt**  string | Unknown option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_daddr_err**  string | Destination address as unspecified or loopback address anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_land**  string | Land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_optendpid**  string | End point identification anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_opthomeaddr**  string | Home address option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_optinvld**  string | Invalid option anomalies.Invalid option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_optjumbo**  string | Jumbo options anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_optnsap**  string | Network service access point address option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_optralert**  string | Router alert option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_opttunnel**  string | Tunnel encapsulation limit option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_proto_err**  string | Layer 4 invalid protocol anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_saddr_err**  string | Source address as multicast anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6_unknopt**  string | Unknown option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_csum_err**  string | Invalid IPv4 TCP checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp_fin_noack**  string | TCP SYN flood with FIN flag set without ACK setting anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_fin_only**  string | TCP SYN flood with only FIN flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_land**  string | TCP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_no_flag**  string | TCP SYN flood with no flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_syn_data**  string | TCP SYN flood packets with data anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_syn_fin**  string | TCP SYN flood SYN/FIN flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp_winnuke**  string | TCP WinNuke anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **udp_csum_err**  string | Invalid IPv4 UDP checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp_land**  string | UDP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **garbage_session_collector**  string | Enable/disable garbage session collector.  **Choices:**   - `"disable"` - `"enable"` |
| **hpe**  dictionary | HPE configuration. |
| **arp_max**  integer | Maximum ARP packet rate (1K - 1G pps). |
| **enable_shaper**  string | Enable/Disable NPU Host Protection Engine(HPE) for packet type shaper.  **Choices:**   - `"disable"` - `"enable"` |
| **esp_max**  integer | Maximum ESP packet rate (1K - 1G pps). |
| **icmp_max**  integer | Maximum ICMP packet rate (1K - 1G pps). |
| **ip_frag_max**  integer | Maximum fragmented IP packet rate (1K - 1G pps). |
| **ip_others_max**  integer | Maximum IP packet rate for other packets (packet types that cannot be set with other options) (1K - 1G pps). |
| **l2_others_max**  integer | Maximum L2 packet rate for L2 packets that are not ARP packets (1K - 1G pps). |
| **pri_type_max**  integer | Maximum overflow rate of priority type traffic (1K - 1G pps). Includes L2: HA, 802.3ad LACP, heartbeats. L3: OSPF. L4_TCP: BGP. L4_UDP: IKE, SLBC, BFD. |
| **sctp_max**  integer | Maximum SCTP packet rate (1K - 1G pps). |
| **tcp_max**  integer | Maximum TCP packet rate (1K - 1G pps). |
| **tcpfin_rst_max**  integer | Maximum TCP carries FIN or RST flags packet rate (1K - 1G pps). |
| **tcpsyn_ack_max**  integer | Maximum TCP carries SYN and ACK flags packet rate (1K - 1G pps). |
| **tcpsyn_max**  integer | Maximum TCP SYN packet rate (1K - 1G pps). |
| **udp_max**  integer | Maximum UDP packet rate (1K - 1G pps). |
| **ipsec_ob_hash_function**  string | Set hash function for IPSec outbound.  **Choices:**   - `"global-hash"` - `"round-robin-global"` |
| **ipsec_outbound_hash**  string | Enable/disable hash function for IPsec outbound traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **low_latency_mode**  string | Enable/disable low latency mode.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Device Name. |
| **per_session_accounting**  string | Enable/disable per-session accounting.  **Choices:**   - `"disable"` - `"traffic-log-only"` - `"enable"` |
| **session_collector_interval**  integer | Set garbage session collection cleanup interval (1 - 100 sec). |
| **session_timeout_fixed**  string | {disable | enable} Toggle between using fixed or random timeouts for refreshing NP6 sessions.  **Choices:**   - `"disable"` - `"enable"` |
| **session_timeout_interval**  integer | Set the fixed timeout for refreshing NP6 sessions (0 - 1000 sec). |
| **session_timeout_random_range**  integer | Set the random timeout range for refreshing NP6 sessions (0 - 1000 sec). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_np6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_np6_module.md#id5)

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
  - name: Configure NP6 attributes.
    fortios_system_np6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_np6:
        fastpath: "disable"
        fp_anomaly:
            icmp_csum_err: "drop"
            icmp_frag: "allow"
            icmp_land: "allow"
            ipv4_csum_err: "drop"
            ipv4_land: "allow"
            ipv4_optlsrr: "allow"
            ipv4_optrr: "allow"
            ipv4_optsecurity: "allow"
            ipv4_optssrr: "allow"
            ipv4_optstream: "allow"
            ipv4_opttimestamp: "allow"
            ipv4_proto_err: "allow"
            ipv4_unknopt: "allow"
            ipv6_daddr_err: "allow"
            ipv6_land: "allow"
            ipv6_optendpid: "allow"
            ipv6_opthomeaddr: "allow"
            ipv6_optinvld: "allow"
            ipv6_optjumbo: "allow"
            ipv6_optnsap: "allow"
            ipv6_optralert: "allow"
            ipv6_opttunnel: "allow"
            ipv6_proto_err: "allow"
            ipv6_saddr_err: "allow"
            ipv6_unknopt: "allow"
            tcp_csum_err: "drop"
            tcp_fin_noack: "allow"
            tcp_fin_only: "allow"
            tcp_land: "allow"
            tcp_no_flag: "allow"
            tcp_syn_data: "allow"
            tcp_syn_fin: "allow"
            tcp_winnuke: "allow"
            udp_csum_err: "drop"
            udp_land: "allow"
        garbage_session_collector: "disable"
        hpe:
            arp_max: "200000"
            enable_shaper: "disable"
            esp_max: "200000"
            icmp_max: "200000"
            ip_frag_max: "200000"
            ip_others_max: "200000"
            l2_others_max: "200000"
            pri_type_max: "200000"
            sctp_max: "200000"
            tcp_max: "600000"
            tcpfin_rst_max: "600000"
            tcpsyn_ack_max: "600000"
            tcpsyn_max: "600000"
            udp_max: "600000"
        ipsec_ob_hash_function: "global-hash"
        ipsec_outbound_hash: "disable"
        low_latency_mode: "disable"
        name: "default_name_59"
        per_session_accounting: "disable"
        session_collector_interval: "64"
        session_timeout_fixed: "disable"
        session_timeout_interval: "40"
        session_timeout_random_range: "8"
```

## [Return Values](fortios_system_np6_module.md#id6)

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
