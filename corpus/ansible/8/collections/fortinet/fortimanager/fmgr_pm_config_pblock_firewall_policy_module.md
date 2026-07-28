---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy module – Configure IPv4/IPv6 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pm_config_pblock_firewall_policy_module.html
fetched_at: 2026-07-28T02:16:01+00:00
---
# fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy module – Configure IPv4/IPv6 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_pm_config_pblock_firewall_policy_module.md#synopsis)
- [Parameters](fmgr_pm_config_pblock_firewall_policy_module.md#parameters)
- [Notes](fmgr_pm_config_pblock_firewall_policy_module.md#notes)
- [Examples](fmgr_pm_config_pblock_firewall_policy_module.md#examples)
- [Return Values](fmgr_pm_config_pblock_firewall_policy_module.md#return-values)

## [Synopsis](fmgr_pm_config_pblock_firewall_policy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pm_config_pblock_firewall_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pblock**  string / required | the parameter (pblock) in requested url |
| **pm_config_pblock_firewall_policy**  dictionary | the top level parameters set |
| **_policy_block**  integer | Assigned policy block. |
| **action**  string | Policy action  **Choices:**   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` - `"redirect"` - `"isolate"` |
| **anti-replay**  string | Enable/disable anti-replay check.  **Choices:**   - `"disable"` - `"enable"` |
| **app-category**  any | (list) no description |
| **app-group**  any | (list) no description |
| **application**  any | (list) no description |
| **application-list**  string | Name of an existing Application list. |
| **auth-cert**  string | HTTPS server certificate for policy authentication. |
| **auth-path**  string | Enable/disable authentication-based routing.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-redirect-addr**  string | HTTP-to-HTTPS redirect address for firewall authentication. |
| **auto-asic-offload**  string | Enable/disable policy traffic ASIC offloading.  **Choices:**   - `"disable"` - `"enable"` |
| **av-profile**  string | Name of an existing Antivirus profile. |
| **best-route**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **block-notification**  string | Enable/disable block notification.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal-exempt**  string | Enable to exempt some users from the captive portal.  **Choices:**   - `"disable"` - `"enable"` |
| **capture-packet**  string | Enable/disable capture packets.  **Choices:**   - `"disable"` - `"enable"` |
| **casb-profile**  string | Name of an existing CASB profile. |
| **cgn-eif**  string | Enable/Disable CGN endpoint independent filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eim**  string | Enable/Disable CGN endpoint independent mapping  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-log-server-grp**  string | NP log server group name |
| **cgn-resource-quota**  integer | resource quota |
| **cgn-session-quota**  integer | session quota |
| **cifs-profile**  string | Name of an existing CIFS profile. |
| **comments**  string | Comment. |
| **custom-log-fields**  any | (list) no description |
| **decrypted-traffic-mirror**  string | Decrypted traffic mirror. |
| **delay-tcp-npu-session**  string | Enable TCP NPU session delay to guarantee packet order of 3-way handshake.  **Choices:**   - `"disable"` - `"enable"` |
| **devices**  any | (list) no description |
| **diffserv-copy**  string | Enable to copy packets DiffServ values from sessions original direction to its reply direction.  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-forward**  string | Enable to change packets DiffServ values to the specified diffservcode-forward value.  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | Enable to change packets reverse  **Choices:**   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | Change packets DiffServ to this value. |
| **diffservcode-rev**  string | Change packets reverse |
| **disclaimer**  string | Enable/disable user authentication disclaimer.  **Choices:**   - `"disable"` - `"enable"` - `"user"` - `"domain"` - `"policy"` |
| **dlp-profile**  string | Name of an existing DLP profile. |
| **dlp-sensor**  string | Name of an existing DLP sensor. |
| **dnsfilter-profile**  string | Name of an existing DNS filter profile. |
| **dscp-match**  string | Enable DSCP check.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-negate**  string | Enable negated DSCP match.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-value**  string | DSCP value. |
| **dsri**  string | Enable DSRI to ignore HTTP server responses.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr**  any | (list) no description |
| **dstaddr-negate**  string | When enabled dstaddr/dstaddr6 specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr6**  any | (list) no description |
| **dstaddr6-negate**  string | When enabled dstaddr6 specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstintf**  any | (list) no description |
| **dynamic-shaping**  string | Enable/disable dynamic RADIUS defined traffic shaping.  **Choices:**   - `"disable"` - `"enable"` |
| **email-collect**  string | Enable/disable email collection.  **Choices:**   - `"disable"` - `"enable"` |
| **emailfilter-profile**  string | Name of an existing email filter profile. |
| **fec**  string | Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.  **Choices:**   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | Name of an existing file-filter profile. |
| **firewall-session-dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  **Choices:**   - `"check-all"` - `"check-new"` |
| **fixedport**  string | Enable to prevent source NAT from changing a sessions source port.  **Choices:**   - `"disable"` - `"enable"` |
| **fsso**  string | Enable/disable Fortinet Single Sign-On.  **Choices:**   - `"disable"` - `"enable"` |
| **fsso-agent-for-ntlm**  string | FSSO agent to use for NTLM authentication. |
| **fsso-groups**  any | (list) no description |
| **geoip-anycast**  string | Enable/disable recognition of anycast IP addresses using the geography IP database.  **Choices:**   - `"disable"` - `"enable"` |
| **geoip-match**  string | Match geography address based either on its physical location or registered location.  **Choices:**   - `"physical-location"` - `"registered-location"` |
| **global-label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  any | (list) no description |
| **gtp-profile**  string | GTP profile. |
| **http-policy-redirect**  string | Redirect HTTP  **Choices:**   - `"disable"` - `"enable"` |
| **icap-profile**  string | Name of an existing ICAP profile. |
| **identity-based-route**  string | Name of identity-based routing rule. |
| **inbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | Policy inspection mode  **Choices:**   - `"proxy"` - `"flow"` |
| **internet-service**  string | Enable/disable use of Internet Services for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list) no description |
| **internet-service-custom-group**  any | (list) no description |
| **internet-service-group**  any | (list) no description |
| **internet-service-id**  any | (list) no description |
| **internet-service-name**  any | (list) no description |
| **internet-service-negate**  string | When enabled internet-service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src**  string | Enable/disable use of Internet Services in source for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  any | (list) no description |
| **internet-service-src-custom-group**  any | (list) no description |
| **internet-service-src-group**  any | (list) no description |
| **internet-service-src-id**  any | (list) no description |
| **internet-service-src-name**  any | (list) no description |
| **internet-service-src-negate**  string | When enabled internet-service-src specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service6**  string | Enable/disable use of IPv6 Internet Services for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service6-custom**  any | (list) no description |
| **internet-service6-custom-group**  any | (list) no description |
| **internet-service6-group**  any | (list) no description |
| **internet-service6-name**  any | (list) no description |
| **internet-service6-negate**  string | When enabled internet-service6 specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service6-src**  string | Enable/disable use of IPv6 Internet Services in source for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service6-src-custom**  any | (list) no description |
| **internet-service6-src-custom-group**  any | (list) no description |
| **internet-service6-src-group**  any | (list) no description |
| **internet-service6-src-name**  any | (list) no description |
| **internet-service6-src-negate**  string | When enabled internet-service6-src specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **ip-version-type**  string | IP version of the policy. |
| **ippool**  string | Enable to use IP Pools for source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sensor**  string | Name of an existing IPS sensor. |
| **ips-voip-filter**  string | Name of an existing VoIP |
| **label**  string | Label for the policy that appears when the GUI is in Section View mode. |
| **learning-mode**  string | Enable to allow everything, but log all of the meaningful data for security information gathering.  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic**  string | Enable or disable logging.  **Choices:**   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Record logs when a session starts.  **Choices:**   - `"disable"` - `"enable"` |
| **match-vip**  string | Enable to match packets that have had their destination addresses changed by a VIP.  **Choices:**   - `"disable"` - `"enable"` |
| **match-vip-only**  string | Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | Name of an existing MMS profile. |
| **name**  string / required | Policy name. |
| **nat**  string | Enable/disable source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  **Choices:**   - `"disable"` - `"enable"` |
| **nat64**  string | Enable/disable NAT64.  **Choices:**   - `"disable"` - `"enable"` |
| **natinbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **natip**  string | Policy-based IPsec VPN |
| **natoutbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **network-service-dynamic**  any | (list) no description |
| **network-service-src-dynamic**  any | (list) no description |
| **np-acceleration**  string | Enable/disable UTM Network Processor acceleration.  **Choices:**   - `"disable"` - `"enable"` |
| **ntlm**  string | Enable/disable NTLM authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **ntlm-enabled-browsers**  any | (list) no description |
| **ntlm-guest**  string | Enable/disable NTLM guest user access.  **Choices:**   - `"disable"` - `"enable"` |
| **outbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **passive-wan-health-measurement**  string | Enable/disable passive WAN health measurement.  **Choices:**   - `"disable"` - `"enable"` |
| **pcp-inbound**  string | Enable/disable PCP inbound DNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **pcp-outbound**  string | Enable/disable PCP outbound SNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **pcp-poolname**  any | (list) no description |
| **per-ip-shaper**  string | Per-IP traffic shaper. |
| **permit-any-host**  string | Accept UDP packets from any host.  **Choices:**   - `"disable"` - `"enable"` |
| **permit-stun-host**  string | Accept UDP packets from any Session Traversal Utilities for NAT  **Choices:**   - `"disable"` - `"enable"` |
| **pfcp-profile**  string | PFCP profile. |
| **policy-behaviour-type**  string | Behaviour of the policy. |
| **policy-expiry**  string | Enable/disable policy expiry.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-expiry-date**  string | Policy expiry date |
| **policy-expiry-date-utc**  string | Policy expiry date and time, in epoch format. |
| **policy-offload**  string | Enable/Disable hardware session setup for CGNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **policyid**  integer | Policy ID |
| **poolname**  any | (list) no description |
| **poolname6**  any | (list) no description |
| **profile-group**  string | Name of profile group. |
| **profile-protocol-options**  string | Name of an existing Protocol options profile. |
| **profile-type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **radius-mac-auth-bypass**  string | Enable MAC authentication bypass.  **Choices:**   - `"disable"` - `"enable"` |
| **redirect-url**  string | URL users are directed to after seeing and accepting the disclaimer or authenticating. |
| **replacemsg-override-group**  string | Override the default replacement message group for this policy. |
| **reputation-direction**  string | Direction of the initial traffic for reputation to take effect.  **Choices:**   - `"source"` - `"destination"` |
| **reputation-direction6**  string | Direction of the initial traffic for IPv6 reputation to take effect.  **Choices:**   - `"source"` - `"destination"` |
| **reputation-minimum**  integer | Minimum Reputation to take action. |
| **reputation-minimum6**  integer | IPv6 Minimum Reputation to take action. |
| **rsso**  string | Enable/disable RADIUS single sign-on  **Choices:**   - `"disable"` - `"enable"` |
| **rtp-addr**  any | (list) no description |
| **rtp-nat**  string | Enable Real Time Protocol  **Choices:**   - `"disable"` - `"enable"` |
| **scan-botnet-connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Schedule name. |
| **schedule-timeout**  string | Enable to force current sessions to end when the schedule object times out.  **Choices:**   - `"disable"` - `"enable"` |
| **sctp-filter-profile**  string | Name of an existing SCTP filter profile. |
| **send-deny-packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  **Choices:**   - `"disable"` - `"enable"` |
| **service**  any | (list) no description |
| **service-negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **session-ttl**  any | (int or str) TTL in seconds for sessions accepted by this policy |
| **sgt**  any | (list) no description |
| **sgt-check**  string | Enable/disable security group tags  **Choices:**   - `"disable"` - `"enable"` |
| **spamfilter-profile**  string | Name of an existing Spam filter profile. |
| **src-vendor-mac**  any | (list) no description |
| **srcaddr**  any | (list) no description |
| **srcaddr-negate**  string | When enabled srcaddr/srcaddr6 specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr6**  any | (list) no description |
| **srcaddr6-negate**  string | When enabled srcaddr6 specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcintf**  any | (list) no description |
| **ssh-filter-profile**  string | Name of an existing SSH filter profile. |
| **ssh-policy-redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror**  string | Enable to copy decrypted SSL traffic to a FortiGate interface  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror-intf**  any | (list) no description |
| **ssl-ssh-profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-mss-receiver**  integer | Receiver TCP maximum segment size |
| **tcp-mss-sender**  integer | Sender TCP maximum segment size |
| **tcp-session-without-syn**  string | Enable/disable creation of TCP session without SYN flag.  **Choices:**   - `"all"` - `"data-only"` - `"disable"` |
| **tcp-timeout-pid**  string | TCP timeout profile ID |
| **timeout-send-rst**  string | Enable/disable sending RST packets when TCP sessions expire.  **Choices:**   - `"disable"` - `"enable"` |
| **tos**  string | ToS |
| **tos-mask**  string | Non-zero bit positions are used for comparison while zero bit positions are ignored. |
| **tos-negate**  string | Enable negated TOS match.  **Choices:**   - `"disable"` - `"enable"` |
| **traffic-shaper**  string | Traffic shaper. |
| **traffic-shaper-reverse**  string | Reverse traffic shaper. |
| **udp-timeout-pid**  string | UDP timeout profile ID |
| **url-category**  any | (list) no description |
| **users**  any | (list) no description |
| **utm-status**  string | Enable to add one or more security profiles  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **videofilter-profile**  string | Name of an existing VideoFilter profile. |
| **virtual-patch-profile**  string | Name of an existing virtual-patch profile. |
| **vlan-cos-fwd**  integer | VLAN forward direction user priority |
| **vlan-cos-rev**  integer | VLAN reverse direction user priority |
| **vlan-filter**  string | Set VLAN filters. |
| **voip-profile**  string | Name of an existing VoIP profile. |
| **vpntunnel**  string | Policy-based IPsec VPN |
| **waf-profile**  string | Name of an existing Web application firewall profile. |
| **wanopt**  string | Enable/disable WAN optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **wanopt-detection**  string | WAN optimization auto-detection mode.  **Choices:**   - `"active"` - `"passive"` - `"off"` |
| **wanopt-passive-opt**  string | WAN optimization passive mode options.  **Choices:**   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt-peer**  string | WAN optimization peer. |
| **wanopt-profile**  string | WAN optimization profile. |
| **wccp**  string | Enable/disable forwarding traffic matching this policy to a configured WCCP server.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache**  string | Enable/disable web cache.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache-https**  string | Enable/disable web cache for HTTPS.  **Choices:**   - `"disable"` - `"ssl-server"` - `"any"` - `"enable"` |
| **webfilter-profile**  string | Name of an existing Web filter profile. |
| **webproxy-forward-server**  string | Webproxy forward server name. |
| **webproxy-profile**  string | Webproxy profile name. |
| **wsso**  string | Enable/disable WiFi Single Sign On  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-device-ownership**  string | Enable/disable zero trust device ownership.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-ems-tag**  any | (list) no description |
| **ztna-ems-tag-secondary**  any | (list) no description |
| **ztna-geo-tag**  any | (list) no description |
| **ztna-policy-redirect**  string | Redirect ZTNA traffic to matching Access-Proxy proxy-policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-status**  string | Enable/disable zero trust access.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-tags-match-logic**  string | ZTNA tag matching logic.  **Choices:**   - `"or"` - `"and"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pm_config_pblock_firewall_policy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pm_config_pblock_firewall_policy_module.md#id4)

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
    - name: Configure IPv4/IPv6 policies.
      fmgr_pm_config_pblock_firewall_policy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: <value in [present, absent]>
        pm_config_pblock_firewall_policy:
          _policy_block: <integer>
          action: <value in [deny, accept, ipsec, ...]>
          anti-replay: <value in [disable, enable]>
          application-list: <string>
          auth-cert: <string>
          auth-path: <value in [disable, enable]>
          auth-redirect-addr: <string>
          auto-asic-offload: <value in [disable, enable]>
          av-profile: <string>
          block-notification: <value in [disable, enable]>
          captive-portal-exempt: <value in [disable, enable]>
          capture-packet: <value in [disable, enable]>
          cifs-profile: <string>
          comments: <string>
          custom-log-fields: <list or string>
          decrypted-traffic-mirror: <string>
          delay-tcp-npu-session: <value in [disable, enable]>
          diffserv-forward: <value in [disable, enable]>
          diffserv-reverse: <value in [disable, enable]>
          diffservcode-forward: <string>
          diffservcode-rev: <string>
          disclaimer: <value in [disable, enable, user, ...]>
          dlp-profile: <string>
          dnsfilter-profile: <string>
          dsri: <value in [disable, enable]>
          dstaddr: <list or string>
          dstaddr-negate: <value in [disable, enable]>
          dstaddr6: <list or string>
          dstintf: <list or string>
          dynamic-shaping: <value in [disable, enable]>
          email-collect: <value in [disable, enable]>
          emailfilter-profile: <string>
          fec: <value in [disable, enable]>
          file-filter-profile: <string>
          firewall-session-dirty: <value in [check-all, check-new]>
          fixedport: <value in [disable, enable]>
          fsso-agent-for-ntlm: <string>
          fsso-groups: <list or string>
          geoip-anycast: <value in [disable, enable]>
          geoip-match: <value in [physical-location, registered-location]>
          global-label: <string>
          groups: <list or string>
          gtp-profile: <string>
          http-policy-redirect: <value in [disable, enable]>
          icap-profile: <string>
          identity-based-route: <string>
          inbound: <value in [disable, enable]>
          inspection-mode: <value in [proxy, flow]>
          internet-service: <value in [disable, enable]>
          internet-service-custom: <list or string>
          internet-service-custom-group: <list or string>
          internet-service-group: <list or string>
          internet-service-name: <list or string>
          internet-service-negate: <value in [disable, enable]>
          internet-service-src: <value in [disable, enable]>
          internet-service-src-custom: <list or string>
          internet-service-src-custom-group: <list or string>
          internet-service-src-group: <list or string>
          internet-service-src-name: <list or string>
          internet-service-src-negate: <value in [disable, enable]>
          ippool: <value in [disable, enable]>
          ips-sensor: <string>
          label: <string>
          logtraffic: <value in [disable, enable, all, ...]>
          logtraffic-start: <value in [disable, enable]>
          match-vip: <value in [disable, enable]>
          match-vip-only: <value in [disable, enable]>
          name: <string>
          nat: <value in [disable, enable]>
          nat46: <value in [disable, enable]>
          nat64: <value in [disable, enable]>
          natinbound: <value in [disable, enable]>
          natip: <string>
          natoutbound: <value in [disable, enable]>
          np-acceleration: <value in [disable, enable]>
          ntlm: <value in [disable, enable]>
          ntlm-enabled-browsers: <list or string>
          ntlm-guest: <value in [disable, enable]>
          outbound: <value in [disable, enable]>
          passive-wan-health-measurement: <value in [disable, enable]>
          per-ip-shaper: <string>
          permit-any-host: <value in [disable, enable]>
          permit-stun-host: <value in [disable, enable]>
          pfcp-profile: <string>
          policy-expiry: <value in [disable, enable]>
          policy-expiry-date: <string>
          policyid: <integer>
          poolname: <list or string>
          poolname6: <list or string>
          profile-group: <string>
          profile-protocol-options: <string>
          profile-type: <value in [single, group]>
          radius-mac-auth-bypass: <value in [disable, enable]>
          redirect-url: <string>
          replacemsg-override-group: <string>
          reputation-direction: <value in [source, destination]>
          reputation-minimum: <integer>
          rtp-addr: <list or string>
          rtp-nat: <value in [disable, enable]>
          schedule: <string>
          schedule-timeout: <value in [disable, enable]>
          sctp-filter-profile: <string>
          send-deny-packet: <value in [disable, enable]>
          service: <list or string>
          service-negate: <value in [disable, enable]>
          session-ttl: <integer or string>
          sgt: <list or integer>
          sgt-check: <value in [disable, enable]>
          src-vendor-mac: <list or string>
          srcaddr: <list or string>
          srcaddr-negate: <value in [disable, enable]>
          srcaddr6: <list or string>
          srcintf: <list or string>
          ssh-filter-profile: <string>
          ssh-policy-redirect: <value in [disable, enable]>
          ssl-ssh-profile: <string>
          status: <value in [disable, enable]>
          tcp-mss-receiver: <integer>
          tcp-mss-sender: <integer>
          tcp-session-without-syn: <value in [all, data-only, disable]>
          timeout-send-rst: <value in [disable, enable]>
          tos: <string>
          tos-mask: <string>
          tos-negate: <value in [disable, enable]>
          traffic-shaper: <string>
          traffic-shaper-reverse: <string>
          users: <list or string>
          utm-status: <value in [disable, enable]>
          uuid: <string>
          videofilter-profile: <string>
          vlan-cos-fwd: <integer>
          vlan-cos-rev: <integer>
          vlan-filter: <string>
          voip-profile: <string>
          vpntunnel: <string>
          waf-profile: <string>
          wanopt: <value in [disable, enable]>
          wanopt-detection: <value in [active, passive, off]>
          wanopt-passive-opt: <value in [default, transparent, non-transparent]>
          wanopt-peer: <string>
          wanopt-profile: <string>
          wccp: <value in [disable, enable]>
          webcache: <value in [disable, enable]>
          webcache-https: <value in [disable, ssl-server, any, ...]>
          webfilter-profile: <string>
          webproxy-forward-server: <string>
          webproxy-profile: <string>
          ztna-ems-tag: <list or string>
          ztna-geo-tag: <list or string>
          ztna-status: <value in [disable, enable]>
          policy-offload: <value in [disable, enable]>
          cgn-session-quota: <integer>
          tcp-timeout-pid: <string>
          udp-timeout-pid: <string>
          dlp-sensor: <string>
          cgn-eif: <value in [disable, enable]>
          cgn-log-server-grp: <string>
          cgn-resource-quota: <integer>
          cgn-eim: <value in [disable, enable]>
          mms-profile: <string>
          app-category: <list or string>
          internet-service-src-id: <list or string>
          rsso: <value in [disable, enable]>
          internet-service-id: <list or string>
          best-route: <value in [disable, enable]>
          fsso: <value in [disable, enable]>
          url-category: <list or string>
          app-group: <list or string>
          ssl-mirror-intf: <list or string>
          wsso: <value in [disable, enable]>
          ssl-mirror: <value in [disable, enable]>
          application: <list or integer>
          dscp-negate: <value in [disable, enable]>
          learning-mode: <value in [disable, enable]>
          devices: <list or string>
          dscp-value: <string>
          spamfilter-profile: <string>
          scan-botnet-connections: <value in [disable, block, monitor]>
          dscp-match: <value in [disable, enable]>
          diffserv-copy: <value in [disable, enable]>
          dstaddr6-negate: <value in [disable, enable]>
          internet-service6: <value in [disable, enable]>
          internet-service6-custom: <list or string>
          internet-service6-custom-group: <list or string>
          internet-service6-group: <list or string>
          internet-service6-name: <list or string>
          internet-service6-negate: <value in [disable, enable]>
          internet-service6-src: <value in [disable, enable]>
          internet-service6-src-custom: <list or string>
          internet-service6-src-custom-group: <list or string>
          internet-service6-src-group: <list or string>
          internet-service6-src-name: <list or string>
          internet-service6-src-negate: <value in [disable, enable]>
          network-service-dynamic: <list or string>
          network-service-src-dynamic: <list or string>
          reputation-direction6: <value in [source, destination]>
          reputation-minimum6: <integer>
          srcaddr6-negate: <value in [disable, enable]>
          ip-version-type: <string>
          ips-voip-filter: <string>
          pcp-inbound: <value in [disable, enable]>
          pcp-outbound: <value in [disable, enable]>
          pcp-poolname: <list or string>
          policy-behaviour-type: <string>
          policy-expiry-date-utc: <string>
          ztna-device-ownership: <value in [disable, enable]>
          ztna-ems-tag-secondary: <list or string>
          ztna-policy-redirect: <value in [disable, enable]>
          ztna-tags-match-logic: <value in [or, and]>
          casb-profile: <string>
          virtual-patch-profile: <string>
```

## [Return Values](fmgr_pm_config_pblock_firewall_policy_module.md#id5)

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
