---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_policy6 module – Configure IPv6 policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_policy6_module.html
fetched_at: 2026-07-27T17:41:19+00:00
---
# fortinet.fortios.fortios_firewall_policy6 module – Configure IPv6 policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_policy6_module.md#ansible-collections-fortinet-fortios-fortios-firewall-policy6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_policy6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_policy6_module.md#synopsis)
- [Requirements](fortios_firewall_policy6_module.md#requirements)
- [Parameters](fortios_firewall_policy6_module.md#parameters)
- [Notes](fortios_firewall_policy6_module.md#notes)
- [Examples](fortios_firewall_policy6_module.md#examples)
- [Return Values](fortios_firewall_policy6_module.md#return-values)

## [Synopsis](fortios_firewall_policy6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and policy6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_policy6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_policy6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_policy6**  dictionary | Configure IPv6 policies. |
| **action**  string | Policy action (allow/deny/ipsec).  Choices:   - `"accept"` - `"deny"` - `"ipsec"` |
| **anti_replay**  string | Enable/disable anti-replay check.  Choices:   - `"enable"` - `"disable"` |
| **app_category**  list / elements=dictionary | Application category ID list. |
| **id**  integer | Category IDs. |
| **app_group**  list / elements=dictionary | Application group names. |
| **name**  string | Application group names. Source application.group.name. |
| **application**  list / elements=dictionary | Application ID list. |
| **id**  integer | Application IDs. |
| **application_list**  string | Name of an existing Application list. Source application.list.name. |
| **auto_asic_offload**  string | Enable/disable policy traffic ASIC offloading.  Choices:   - `"enable"` - `"disable"` |
| **av_profile**  string | Name of an existing Antivirus profile. Source antivirus.profile.name. |
| **cifs_profile**  string | Name of an existing CIFS profile. Source cifs.profile.name. |
| **comments**  string | Comment. |
| **custom_log_fields**  list / elements=dictionary | Log field index numbers to append custom log fields to log messages for this policy. |
| **field_id**  string | Custom log field. Source log.custom-field.id. |
| **devices**  list / elements=dictionary | Names of devices or device groups that can be matched by the policy. |
| **name**  string | Device or group name. Source user.device.alias user.device-group.name user.device-category.name. |
| **diffserv_forward**  string | Enable to change packet”s DiffServ values to the specified diffservcode-forward value.  Choices:   - `"enable"` - `"disable"` |
| **diffserv_reverse**  string | Enable to change packet”s reverse (reply) DiffServ values to the specified diffservcode-rev value.  Choices:   - `"enable"` - `"disable"` |
| **diffservcode_forward**  string | Change packet”s DiffServ to this value. |
| **diffservcode_rev**  string | Change packet”s reverse (reply) DiffServ to this value. |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. Source dnsfilter.profile.name. |
| **dscp_match**  string | Enable DSCP check.  Choices:   - `"enable"` - `"disable"` |
| **dscp_negate**  string | Enable negated DSCP match.  Choices:   - `"enable"` - `"disable"` |
| **dscp_value**  string | DSCP value. |
| **dsri**  string | Enable DSRI to ignore HTTP server responses.  Choices:   - `"enable"` - `"disable"` |
| **dstaddr**  list / elements=dictionary | Destination address and address group names. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system .external-resource.name. |
| **dstaddr_negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **dstintf**  list / elements=dictionary | Outgoing (egress) interface. |
| **name**  string | Interface name. Source system.interface.name system.zone.name. |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **firewall_session_dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  Choices:   - `"check-all"` - `"check-new"` |
| **fixedport**  string | Enable to prevent source NAT from changing a session”s source port.  Choices:   - `"enable"` - `"disable"` |
| **fsso_groups**  list / elements=dictionary | Names of FSSO groups. |
| **name**  string | Names of FSSO groups. Source user.adgrp.name. |
| **global_label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  list / elements=dictionary | Names of user groups that can authenticate with this policy. |
| **name**  string | Group name. Source user.group.name. |
| **http_policy_redirect**  string | Redirect HTTP(S) traffic to matching transparent web proxy policy.  Choices:   - `"enable"` - `"disable"` |
| **icap_profile**  string | Name of an existing ICAP profile. Source icap.profile.name. |
| **inbound**  string | Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.  Choices:   - `"enable"` - `"disable"` |
| **inspection_mode**  string | Policy inspection mode (Flow/proxy). Default is Flow mode.  Choices:   - `"proxy"` - `"flow"` |
| **ippool**  string | Enable to use IP Pools for source NAT.  Choices:   - `"enable"` - `"disable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **label**  string | Label for the policy that appears when the GUI is in Section View mode. |
| **logtraffic**  string | Enable or disable logging. Log all sessions or security profile sessions.  Choices:   - `"all"` - `"utm"` - `"disable"` |
| **logtraffic_start**  string | Record logs when a session starts.  Choices:   - `"enable"` - `"disable"` |
| **mms_profile**  string | Name of an existing MMS profile. Source firewall.mms-profile.name. |
| **name**  string | Policy name. |
| **nat**  string | Enable/disable source NAT.  Choices:   - `"enable"` - `"disable"` |
| **natinbound**  string | Policy-based IPsec VPN: apply destination NAT to inbound traffic.  Choices:   - `"enable"` - `"disable"` |
| **natoutbound**  string | Policy-based IPsec VPN: apply source NAT to outbound traffic.  Choices:   - `"enable"` - `"disable"` |
| **np_acceleration**  string | Enable/disable UTM Network Processor acceleration.  Choices:   - `"enable"` - `"disable"` |
| **outbound**  string | Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.  Choices:   - `"enable"` - `"disable"` |
| **per_ip_shaper**  string | Per-IP traffic shaper. Source firewall.shaper.per-ip-shaper.name. |
| **policyid**  integer / required | Policy ID (0 - 4294967294). |
| **poolname**  list / elements=dictionary | IP Pool names. |
| **name**  string | IP pool name. Source firewall.ippool6.name. |
| **profile_group**  string | Name of profile group. Source firewall.profile-group.name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name. |
| **profile_type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  Choices:   - `"single"` - `"group"` |
| **replacemsg_override_group**  string | Override the default replacement message group for this policy. Source system.replacemsg-group.name. |
| **rsso**  string | Enable/disable RADIUS single sign-on (RSSO).  Choices:   - `"enable"` - `"disable"` |
| **schedule**  string | Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **send_deny_packet**  string | Enable/disable return of deny-packet.  Choices:   - `"enable"` - `"disable"` |
| **service**  list / elements=dictionary | Service and service group names. |
| **name**  string | Address name. Source firewall.service.custom.name firewall.service.group.name. |
| **service_negate**  string | When enabled service specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **session_ttl**  string | Session TTL in seconds for sessions accepted by this policy. 0 means use the system default session TTL. |
| **spamfilter_profile**  string | Name of an existing Spam filter profile. Source spamfilter.profile.name. |
| **srcaddr**  list / elements=dictionary | Source address and address group names. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **srcaddr_negate**  string | When enabled srcaddr specifies what the source address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **srcintf**  list / elements=dictionary | Incoming (ingress) interface. |
| **name**  string | Interface name. Source system.zone.name system.interface.name. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. Source ssh-filter.profile.name. |
| **ssh_policy_redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  Choices:   - `"enable"` - `"disable"` |
| **ssl_mirror**  string | Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring).  Choices:   - `"enable"` - `"disable"` |
| **ssl_mirror_intf**  list / elements=dictionary | SSL mirror interface name. |
| **name**  string | Interface name. Source system.zone.name system.interface.name. |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name. |
| **status**  string | Enable or disable this policy.  Choices:   - `"enable"` - `"disable"` |
| **tcp_mss_receiver**  integer | Receiver TCP maximum segment size (MSS). |
| **tcp_mss_sender**  integer | Sender TCP maximum segment size (MSS). |
| **tcp_session_without_syn**  string | Enable/disable creation of TCP session without SYN flag.  Choices:   - `"all"` - `"data-only"` - `"disable"` |
| **timeout_send_rst**  string | Enable/disable sending RST packets when TCP sessions expire.  Choices:   - `"enable"` - `"disable"` |
| **tos**  string | ToS (Type of Service) value used for comparison. |
| **tos_mask**  string | Non-zero bit positions are used for comparison while zero bit positions are ignored. |
| **tos_negate**  string | Enable negated TOS match.  Choices:   - `"enable"` - `"disable"` |
| **traffic_shaper**  string | Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **traffic_shaper_reverse**  string | Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **url_category**  list / elements=dictionary | URL category ID list. |
| **id**  integer | URL category ID. |
| **users**  list / elements=dictionary | Names of individual users that can authenticate with this policy. |
| **name**  string | Names of individual users that can authenticate with this policy. Source user.local.name. |
| **utm_status**  string | Enable AV/web/ips protection profile.  Choices:   - `"enable"` - `"disable"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **vlan_cos_fwd**  integer | VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest |
| **vlan_cos_rev**  integer | VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest |
| **vlan_filter**  string | Set VLAN filters. |
| **voip_profile**  string | Name of an existing VoIP profile. Source voip.profile.name. |
| **vpntunnel**  string | Policy-based IPsec VPN: name of the IPsec VPN Phase 1. Source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name. |
| **waf_profile**  string | Name of an existing Web application firewall profile. Source waf.profile.name. |
| **webcache**  string | Enable/disable web cache.  Choices:   - `"enable"` - `"disable"` |
| **webcache_https**  string | Enable/disable web cache for HTTPS.  Choices:   - `"disable"` - `"enable"` |
| **webfilter_profile**  string | Name of an existing Web filter profile. Source webfilter.profile.name. |
| **webproxy_forward_server**  string | Web proxy forward server name. Source web-proxy.forward-server.name web-proxy.forward-server-group.name. |
| **webproxy_profile**  string | Webproxy profile name. Source web-proxy.profile.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_policy6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_policy6_module.md#id5)

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
  - name: Configure IPv6 policies.
    fortios_firewall_policy6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_policy6:
        action: "accept"
        anti_replay: "enable"
        app_category:
         -
            id:  "6"
        app_group:
         -
            name: "default_name_8 (source application.group.name)"
        application:
         -
            id:  "10"
        application_list: "<your_own_value> (source application.list.name)"
        auto_asic_offload: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        comments: "<your_own_value>"
        custom_log_fields:
         -
            field_id: "<your_own_value> (source log.custom-field.id)"
        devices:
         -
            name: "default_name_19 (source user.device.alias user.device-group.name user.device-category.name)"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dnsfilter_profile: "<your_own_value> (source dnsfilter.profile.name)"
        dscp_match: "enable"
        dscp_negate: "enable"
        dscp_value: "<your_own_value>"
        dsri: "enable"
        dstaddr:
         -
            name: "default_name_31 (source firewall.address6.name firewall.addrgrp6.name firewall.vip6.name firewall.vipgrp6.name system.external-resource
              .name)"
        dstaddr_negate: "enable"
        dstintf:
         -
            name: "default_name_34 (source system.interface.name system.zone.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        firewall_session_dirty: "check-all"
        fixedport: "enable"
        fsso_groups:
         -
            name: "default_name_39 (source user.adgrp.name)"
        global_label: "<your_own_value>"
        groups:
         -
            name: "default_name_42 (source user.group.name)"
        http_policy_redirect: "enable"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        inbound: "enable"
        inspection_mode: "proxy"
        ippool: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        label: "<your_own_value>"
        logtraffic: "all"
        logtraffic_start: "enable"
        mms_profile: "<your_own_value> (source firewall.mms-profile.name)"
        name: "default_name_53"
        nat: "enable"
        natinbound: "enable"
        natoutbound: "enable"
        np_acceleration: "enable"
        outbound: "enable"
        per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
        policyid: "2147483647"
        poolname:
         -
            name: "default_name_62 (source firewall.ippool6.name)"
        profile_group: "<your_own_value> (source firewall.profile-group.name)"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        profile_type: "single"
        replacemsg_override_group: "<your_own_value> (source system.replacemsg-group.name)"
        rsso: "enable"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        send_deny_packet: "enable"
        service:
         -
            name: "default_name_71 (source firewall.service.custom.name firewall.service.group.name)"
        service_negate: "enable"
        session_ttl: "<your_own_value>"
        spamfilter_profile: "<your_own_value> (source spamfilter.profile.name)"
        srcaddr:
         -
            name: "default_name_76 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        srcaddr_negate: "enable"
        srcintf:
         -
            name: "default_name_79 (source system.zone.name system.interface.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssh_policy_redirect: "enable"
        ssl_mirror: "enable"
        ssl_mirror_intf:
         -
            name: "default_name_84 (source system.zone.name system.interface.name)"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        tcp_mss_receiver: "32767"
        tcp_mss_sender: "32767"
        tcp_session_without_syn: "all"
        timeout_send_rst: "enable"
        tos: "<your_own_value>"
        tos_mask: "<your_own_value>"
        tos_negate: "enable"
        traffic_shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        url_category:
         -
            id:  "97"
        users:
         -
            name: "default_name_99 (source user.local.name)"
        utm_status: "enable"
        uuid: "<your_own_value>"
        vlan_cos_fwd: "3"
        vlan_cos_rev: "3"
        vlan_filter: "<your_own_value>"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        vpntunnel: "<your_own_value> (source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name)"
        waf_profile: "<your_own_value> (source waf.profile.name)"
        webcache: "enable"
        webcache_https: "disable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webproxy_forward_server: "<your_own_value> (source web-proxy.forward-server.name web-proxy.forward-server-group.name)"
        webproxy_profile: "<your_own_value> (source web-proxy.profile.name)"
```

## [Return Values](fortios_firewall_policy6_module.md#id6)

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
