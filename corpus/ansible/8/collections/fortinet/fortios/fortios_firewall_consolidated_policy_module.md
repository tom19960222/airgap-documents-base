---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_consolidated_policy module – Configure consolidated IPv4/IPv6 policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_consolidated_policy_module.html
fetched_at: 2026-07-28T02:24:21+00:00
---
# fortinet.fortios.fortios_firewall_consolidated_policy module – Configure consolidated IPv4/IPv6 policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_consolidated_policy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-consolidated-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_consolidated_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_consolidated_policy_module.md#synopsis)
- [Requirements](fortios_firewall_consolidated_policy_module.md#requirements)
- [Parameters](fortios_firewall_consolidated_policy_module.md#parameters)
- [Notes](fortios_firewall_consolidated_policy_module.md#notes)
- [Examples](fortios_firewall_consolidated_policy_module.md#examples)
- [Return Values](fortios_firewall_consolidated_policy_module.md#return-values)

## [Synopsis](fortios_firewall_consolidated_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall_consolidated feature and policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_consolidated_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_consolidated_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_consolidated_policy**  dictionary | Configure consolidated IPv4/IPv6 policies. |
| **action**  string | Policy action (allow/deny/ipsec).  **Choices:**   - `"accept"` - `"deny"` - `"ipsec"` |
| **application_list**  string | Name of an existing Application list. Source application.list.name. |
| **auto_asic_offload**  string | Enable/disable policy traffic ASIC offloading.  **Choices:**   - `"enable"` - `"disable"` |
| **av_profile**  string | Name of an existing Antivirus profile. Source antivirus.profile.name. |
| **captive_portal_exempt**  string | Enable exemption of some users from the captive portal.  **Choices:**   - `"enable"` - `"disable"` |
| **cifs_profile**  string | Name of an existing CIFS profile. Source cifs.profile.name. |
| **comments**  string | Comment. |
| **diffserv_forward**  string | Enable to change packet”s DiffServ values to the specified diffservcode-forward value.  **Choices:**   - `"enable"` - `"disable"` |
| **diffserv_reverse**  string | Enable to change packet”s reverse (reply) DiffServ values to the specified diffservcode-rev value.  **Choices:**   - `"enable"` - `"disable"` |
| **diffservcode_forward**  string | Change packet”s DiffServ to this value. |
| **diffservcode_rev**  string | Change packet”s reverse (reply) DiffServ to this value. |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. Source dnsfilter.profile.name. |
| **dstaddr4**  list / elements=dictionary | Destination IPv4 address name and address group names. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource .name. |
| **dstaddr6**  list / elements=dictionary | Destination IPv6 address name and address group names. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system .external-resource.name. |
| **dstaddr_negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  **Choices:**   - `"enable"` - `"disable"` |
| **dstintf**  list / elements=dictionary | Outgoing (egress) interface. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name. |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **fixedport**  string | Enable to prevent source NAT from changing a session”s source port.  **Choices:**   - `"enable"` - `"disable"` |
| **fsso_groups**  list / elements=dictionary | Names of FSSO groups. |
| **name**  string / required | Names of FSSO groups. Source user.adgrp.name. |
| **global_label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  list / elements=dictionary | Names of user groups that can authenticate with this policy. |
| **name**  string / required | Group name. Source user.group.name. |
| **http_policy_redirect**  string | Redirect HTTP(S) traffic to matching transparent web proxy policy.  **Choices:**   - `"enable"` - `"disable"` |
| **icap_profile**  string | Name of an existing ICAP profile. Source icap.profile.name. |
| **inbound**  string | Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.  **Choices:**   - `"enable"` - `"disable"` |
| **inspection_mode**  string | Policy inspection mode (Flow/proxy). Default is Flow mode.  **Choices:**   - `"proxy"` - `"flow"` |
| **internet_service**  string | Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service_custom**  list / elements=dictionary | Custom Internet Service name. |
| **name**  string / required | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_custom_group**  list / elements=dictionary | Custom Internet Service group name. |
| **name**  string / required | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string / required | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_id**  list / elements=dictionary | Internet Service ID. |
| **id**  integer / required | Internet Service ID. see <a href=’#notes’>Notes</a>. Source firewall.internet-service.id. |
| **internet_service_negate**  string | When enabled internet-service specifies what the service must NOT be.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service_src**  string | Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service_src_custom**  list / elements=dictionary | Custom Internet Service source name. |
| **name**  string / required | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_src_custom_group**  list / elements=dictionary | Custom Internet Service source group name. |
| **name**  string / required | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_src_group**  list / elements=dictionary | Internet Service source group name. |
| **name**  string / required | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_src_id**  list / elements=dictionary | Internet Service source ID. |
| **id**  integer / required | Internet Service ID. see <a href=’#notes’>Notes</a>. Source firewall.internet-service.id. |
| **internet_service_src_negate**  string | When enabled internet-service-src specifies what the service must NOT be.  **Choices:**   - `"enable"` - `"disable"` |
| **ippool**  string | Enable to use IP Pools for source NAT.  **Choices:**   - `"enable"` - `"disable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **logtraffic**  string | Enable or disable logging. Log all sessions or security profile sessions.  **Choices:**   - `"all"` - `"utm"` - `"disable"` |
| **logtraffic_start**  string | Record logs when a session starts.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_profile**  string | Name of an existing MMS profile. Source firewall.mms-profile.name. |
| **name**  string | Policy name. |
| **nat**  string | Enable/disable source NAT.  **Choices:**   - `"enable"` - `"disable"` |
| **outbound**  string | Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.  **Choices:**   - `"enable"` - `"disable"` |
| **per_ip_shaper**  string | Per-IP traffic shaper. Source firewall.shaper.per-ip-shaper.name. |
| **policyid**  integer / required | Policy ID (0 - 4294967294). see <a href=’#notes’>Notes</a>. |
| **poolname4**  list / elements=dictionary | IPv4 pool names. |
| **name**  string / required | IPv4 pool name. Source firewall.ippool.name. |
| **poolname6**  list / elements=dictionary | IPv6 pool names. |
| **name**  string / required | IPv6 pool name. Source firewall.ippool6.name. |
| **profile_group**  string | Name of profile group. Source firewall.profile-group.name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name. |
| **profile_type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **schedule**  string | Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **service**  list / elements=dictionary | Service and service group names. |
| **name**  string / required | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **service_negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"enable"` - `"disable"` |
| **session_ttl**  integer | TTL in seconds for sessions accepted by this policy (0 means use the system ). |
| **srcaddr4**  list / elements=dictionary | Source IPv4 address name and address group names. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name system.external-resource.name. |
| **srcaddr6**  list / elements=dictionary | Source IPv6 address name and address group names. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **srcaddr_negate**  string | When enabled srcaddr specifies what the source address must NOT be.  **Choices:**   - `"enable"` - `"disable"` |
| **srcintf**  list / elements=dictionary | Incoming (ingress) interface. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. Source ssh-filter.profile.name. |
| **ssh_policy_redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name. |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **tcp_mss_receiver**  integer | Receiver TCP maximum segment size (MSS). |
| **tcp_mss_sender**  integer | Sender TCP maximum segment size (MSS). |
| **traffic_shaper**  string | Traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **traffic_shaper_reverse**  string | Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **users**  list / elements=dictionary | Names of individual users that can authenticate with this policy. |
| **name**  string / required | User name. Source user.local.name. |
| **utm_status**  string | Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.  **Choices:**   - `"enable"` - `"disable"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **voip_profile**  string | Name of an existing VoIP profile. Source voip.profile.name. |
| **vpntunnel**  string | Policy-based IPsec VPN: name of the IPsec VPN Phase 1. Source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name. |
| **waf_profile**  string | Name of an existing Web application firewall profile. Source waf.profile.name. |
| **wanopt**  string | Enable/disable WAN optimization.  **Choices:**   - `"enable"` - `"disable"` |
| **wanopt_detection**  string | WAN optimization auto-detection mode.  **Choices:**   - `"active"` - `"passive"` - `"off"` |
| **wanopt_passive_opt**  string | WAN optimization passive mode options. This option decides what IP address will be used to connect to server.  **Choices:**   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt_peer**  string | WAN optimization peer. Source wanopt.peer.peer-host-id. |
| **wanopt_profile**  string | WAN optimization profile. Source wanopt.profile.name. |
| **webcache**  string | Enable/disable web cache.  **Choices:**   - `"enable"` - `"disable"` |
| **webcache_https**  string | Enable/disable web cache for HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter_profile**  string | Name of an existing Web filter profile. Source webfilter.profile.name. |
| **webproxy_forward_server**  string | Webproxy forward server name. Source web-proxy.forward-server.name web-proxy.forward-server-group.name. |
| **webproxy_profile**  string | Webproxy profile name. Source web-proxy.profile.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_consolidated_policy_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the policyid instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_consolidated_policy_module.md#id5)

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
  - name: Configure consolidated IPv4/IPv6 policies.
    fortios_firewall_consolidated_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_consolidated_policy:
        action: "accept"
        application_list: "<your_own_value> (source application.list.name)"
        auto_asic_offload: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        captive_portal_exempt: "enable"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        comments: "<your_own_value>"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dnsfilter_profile: "<your_own_value> (source dnsfilter.profile.name)"
        dstaddr_negate: "enable"
        dstaddr4:
         -
            name: "default_name_18 (source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource.name)"
        dstaddr6:
         -
            name: "default_name_20 (source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system.external-resource
              .name)"
        dstintf:
         -
            name: "default_name_22 (source system.interface.name system.zone.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        fixedport: "enable"
        fsso_groups:
         -
            name: "default_name_26 (source user.adgrp.name)"
        global_label: "<your_own_value>"
        groups:
         -
            name: "default_name_29 (source user.group.name)"
        http_policy_redirect: "enable"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        inbound: "enable"
        inspection_mode: "proxy"
        internet_service: "enable"
        internet_service_custom:
         -
            name: "default_name_36 (source firewall.internet-service-custom.name)"
        internet_service_custom_group:
         -
            name: "default_name_38 (source firewall.internet-service-custom-group.name)"
        internet_service_group:
         -
            name: "default_name_40 (source firewall.internet-service-group.name)"
        internet_service_id:
         -
            id:  "42 (source firewall.internet-service.id)"
        internet_service_negate: "enable"
        internet_service_src: "enable"
        internet_service_src_custom:
         -
            name: "default_name_46 (source firewall.internet-service-custom.name)"
        internet_service_src_custom_group:
         -
            name: "default_name_48 (source firewall.internet-service-custom-group.name)"
        internet_service_src_group:
         -
            name: "default_name_50 (source firewall.internet-service-group.name)"
        internet_service_src_id:
         -
            id:  "52 (source firewall.internet-service.id)"
        internet_service_src_negate: "enable"
        ippool: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        logtraffic: "all"
        logtraffic_start: "enable"
        mms_profile: "<your_own_value> (source firewall.mms-profile.name)"
        name: "default_name_59"
        nat: "enable"
        outbound: "enable"
        per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
        policyid: "<you_own_value>"
        poolname4:
         -
            name: "default_name_65 (source firewall.ippool.name)"
        poolname6:
         -
            name: "default_name_67 (source firewall.ippool6.name)"
        profile_group: "<your_own_value> (source firewall.profile-group.name)"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        profile_type: "single"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        service:
         -
            name: "default_name_73 (source firewall.service.custom.name firewall.service.group.name)"
        service_negate: "enable"
        session_ttl: "1382400"
        srcaddr_negate: "enable"
        srcaddr4:
         -
            name: "default_name_78 (source firewall.address.name firewall.addrgrp.name system.external-resource.name)"
        srcaddr6:
         -
            name: "default_name_80 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        srcintf:
         -
            name: "default_name_82 (source system.interface.name system.zone.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssh_policy_redirect: "enable"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        tcp_mss_receiver: "32767"
        tcp_mss_sender: "32767"
        traffic_shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        users:
         -
            name: "default_name_92 (source user.local.name)"
        utm_status: "enable"
        uuid: "<your_own_value>"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        vpntunnel: "<your_own_value> (source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name)"
        waf_profile: "<your_own_value> (source waf.profile.name)"
        wanopt: "enable"
        wanopt_detection: "active"
        wanopt_passive_opt: "default"
        wanopt_peer: "<your_own_value> (source wanopt.peer.peer-host-id)"
        wanopt_profile: "<your_own_value> (source wanopt.profile.name)"
        webcache: "enable"
        webcache_https: "disable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webproxy_forward_server: "<your_own_value> (source web-proxy.forward-server.name web-proxy.forward-server-group.name)"
        webproxy_profile: "<your_own_value> (source web-proxy.profile.name)"
```

## [Return Values](fortios_firewall_consolidated_policy_module.md#id6)

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
