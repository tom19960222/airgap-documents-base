---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_npu module – Configure NPU attributes in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_npu_module.html
fetched_at: 2026-07-28T02:28:49+00:00
---
# fortinet.fortios.fortios_system_npu module – Configure NPU attributes in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_npu_module.md#ansible-collections-fortinet-fortios-fortios-system-npu-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_npu`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_npu_module.md#synopsis)
- [Requirements](fortios_system_npu_module.md#requirements)
- [Parameters](fortios_system_npu_module.md#parameters)
- [Notes](fortios_system_npu_module.md#notes)
- [Examples](fortios_system_npu_module.md#examples)
- [Return Values](fortios_system_npu_module.md#return-values)

## [Synopsis](fortios_system_npu_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and npu category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_npu_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_npu_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_npu**  dictionary | Configure NPU attributes. |
| **capwap_offload**  string | Enable/disable offloading managed FortiAP and FortiLink CAPWAP sessions.  **Choices:**   - `"enable"` - `"disable"` |
| **dedicated_management_affinity**  string | Affinity setting for management daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **dedicated_management_cpu**  string | Enable to dedicate one CPU for GUI and CLI connections when NPs are busy.  **Choices:**   - `"enable"` - `"disable"` |
| **fastpath**  string | Enable/disable NP6 offloading (also called fast path).  **Choices:**   - `"disable"` - `"enable"` |
| **gtp_enhanced_cpu_range**  string | GTP enhanced CPU range option.  **Choices:**   - `"0"` - `"1"` - `"2"` |
| **gtp_enhanced_mode**  string | Enable/disable GTP enhanced mode.  **Choices:**   - `"enable"` - `"disable"` |
| **intf_shaping_offload**  string | Enable/disable NPU offload when doing interface-based traffic shaping according to the egress-shaping-profile.  **Choices:**   - `"enable"` - `"disable"` |
| **ipsec_dec_subengine_mask**  string | IPsec decryption subengine mask (0x1 - 0xff). |
| **ipsec_enc_subengine_mask**  string | IPsec encryption subengine mask (0x1 - 0xff). |
| **ipsec_inbound_cache**  string | Enable/disable IPsec inbound cache for anti-replay.  **Choices:**   - `"enable"` - `"disable"` |
| **ipsec_mtu_override**  string | Enable/disable NP6 IPsec MTU override.  **Choices:**   - `"disable"` - `"enable"` |
| **ipsec_over_vlink**  string | Enable/disable IPsec over vlink.  **Choices:**   - `"enable"` - `"disable"` |
| **isf_np_queues**  dictionary | Configure queues of switch port connected to NP6 XAUI on ingress path. |
| **cos0**  string | CoS profile name for CoS 0. Source system.isf-queue-profile.name. |
| **cos1**  string | CoS profile name for CoS 1. Source system.isf-queue-profile.name. |
| **cos2**  string | CoS profile name for CoS 2. Source system.isf-queue-profile.name. |
| **cos3**  string | CoS profile name for CoS 3. Source system.isf-queue-profile.name. |
| **cos4**  string | CoS profile name for CoS 4. Source system.isf-queue-profile.name. |
| **cos5**  string | CoS profile name for CoS 5. Source system.isf-queue-profile.name. |
| **cos6**  string | CoS profile name for CoS 6. Source system.isf-queue-profile.name. |
| **cos7**  string | CoS profile name for CoS 7. Source system.isf-queue-profile.name. |
| **lag_out_port_select**  string | Enable/disable LAG outgoing port selection based on incoming traffic port.  **Choices:**   - `"disable"` - `"enable"` |
| **mcast_session_accounting**  string | Enable/disable traffic accounting for each multicast session through TAE counter.  **Choices:**   - `"tpe-based"` - `"session-based"` - `"disable"` |
| **port_cpu_map**  list / elements=dictionary | Configure NPU interface to CPU core mapping. |
| **cpu_core**  string | The CPU core to map to an interface. |
| **interface**  string / required | The interface to map to a CPU core. |
| **port_npu_map**  list / elements=dictionary | Configure port to NPU group mapping. |
| **interface**  string / required | Set NPU interface port for NPU group mapping. |
| **npu_group_index**  integer | Mapping NPU group index. |
| **priority_protocol**  dictionary | Configure NPU priority protocol. |
| **bfd**  string | Enable/disable NPU BFD priority protocol.  **Choices:**   - `"enable"` - `"disable"` |
| **bgp**  string | Enable/disable NPU BGP priority protocol.  **Choices:**   - `"enable"` - `"disable"` |
| **slbc**  string | Enable/disable NPU SLBC priority protocol.  **Choices:**   - `"enable"` - `"disable"` |
| **qos_mode**  string | QoS mode on switch and NP.  **Choices:**   - `"disable"` - `"priority"` - `"round-robin"` |
| **rdp_offload**  string | Enable/disable RDP offload.  **Choices:**   - `"enable"` - `"disable"` |
| **session_denied_offload**  string | Enable/disable offloading of denied sessions. Requires ses-denied-traffic to be set.  **Choices:**   - `"disable"` - `"enable"` |
| **sse_backpressure**  string | Enable/disable SSE backpressure.  **Choices:**   - `"enable"` - `"disable"` |
| **strip_clear_text_padding**  string | Enable/disable stripping clear text padding.  **Choices:**   - `"enable"` - `"disable"` |
| **strip_esp_padding**  string | Enable/disable stripping ESP padding.  **Choices:**   - `"enable"` - `"disable"` |
| **sw_eh_hash**  dictionary | Configure switch enhanced hashing. |
| **computation**  string | Set hashing computation.  **Choices:**   - `"xor16"` - `"xor8"` - `"xor4"` - `"crc16"` |
| **destination_ip_lower_16**  string | Include/exclude destination IP address lower 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **destination_ip_upper_16**  string | Include/exclude destination IP address upper 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **destination_port**  string | Include/exclude destination port if TCP/UDP.  **Choices:**   - `"include"` - `"exclude"` |
| **ip_protocol**  string | Include/exclude IP protocol.  **Choices:**   - `"include"` - `"exclude"` |
| **netmask_length**  integer | Network mask length. |
| **source_ip_lower_16**  string | Include/exclude source IP address lower 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **source_ip_upper_16**  string | Include/exclude source IP address upper 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **source_port**  string | Include/exclude source port if TCP/UDP.  **Choices:**   - `"include"` - `"exclude"` |
| **sw_np_bandwidth**  string | Bandwidth from switch to NP.  **Choices:**   - `"0G"` - `"2G"` - `"4G"` - `"5G"` - `"6G"` - `"7G"` - `"8G"` - `"9G"` |
| **sw_tr_hash**  dictionary | Configure switch traditional hashing. |
| **draco15**  string | Enable/disable DRACO15 hashing.  **Choices:**   - `"enable"` - `"disable"` |
| **tcp_udp_port**  string | Include/exclude TCP/UDP source and destination port for unicast trunk traffic.  **Choices:**   - `"include"` - `"exclude"` |
| **uesp_offload**  string | Enable/disable UDP-encapsulated ESP offload .  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_npu_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_npu_module.md#id5)

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
  - name: Configure NPU attributes.
    fortios_system_npu:
      vdom:  "{{ vdom }}"
      system_npu:
        capwap_offload: "enable"
        dedicated_management_affinity: "<your_own_value>"
        dedicated_management_cpu: "enable"
        fastpath: "disable"
        gtp_enhanced_cpu_range: "0"
        gtp_enhanced_mode: "enable"
        intf_shaping_offload: "enable"
        ipsec_dec_subengine_mask: "<your_own_value>"
        ipsec_enc_subengine_mask: "<your_own_value>"
        ipsec_inbound_cache: "enable"
        ipsec_mtu_override: "disable"
        ipsec_over_vlink: "enable"
        isf_np_queues:
            cos0: "<your_own_value> (source system.isf-queue-profile.name)"
            cos1: "<your_own_value> (source system.isf-queue-profile.name)"
            cos2: "<your_own_value> (source system.isf-queue-profile.name)"
            cos3: "<your_own_value> (source system.isf-queue-profile.name)"
            cos4: "<your_own_value> (source system.isf-queue-profile.name)"
            cos5: "<your_own_value> (source system.isf-queue-profile.name)"
            cos6: "<your_own_value> (source system.isf-queue-profile.name)"
            cos7: "<your_own_value> (source system.isf-queue-profile.name)"
        lag_out_port_select: "disable"
        mcast_session_accounting: "tpe-based"
        port_cpu_map:
         -
            cpu_core: "<your_own_value>"
            interface: "<your_own_value>"
        port_npu_map:
         -
            interface: "<your_own_value>"
            npu_group_index: "0"
        priority_protocol:
            bfd: "enable"
            bgp: "enable"
            slbc: "enable"
        qos_mode: "disable"
        rdp_offload: "enable"
        session_denied_offload: "disable"
        sse_backpressure: "enable"
        strip_clear_text_padding: "enable"
        strip_esp_padding: "enable"
        sw_eh_hash:
            computation: "xor16"
            destination_ip_lower_16: "include"
            destination_ip_upper_16: "include"
            destination_port: "include"
            ip_protocol: "include"
            netmask_length: "32"
            source_ip_lower_16: "include"
            source_ip_upper_16: "include"
            source_port: "include"
        sw_np_bandwidth: "0G"
        sw_tr_hash:
            draco15: "enable"
            tcp_udp_port: "include"
        uesp_offload: "enable"
```

## [Return Values](fortios_system_npu_module.md#id6)

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
