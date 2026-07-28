---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_policy module – Configure IPv4 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_policy_module.html
fetched_at: 2026-07-28T02:15:36+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_policy module – Configure IPv4 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_policy`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pkg_firewall_policy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_policy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_policy_module.md#notes)
- [Examples](fmgr_pkg_firewall_policy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_policy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_policy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_policy**  dictionary | the top level parameters set |
| **_policy_block**  integer | Assigned policy block. |
| **action**  string | Policy action  **Choices:**   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` - `"redirect"` - `"isolate"` |
| **anti-replay**  string | Enable/disable anti-replay check.  **Choices:**   - `"disable"` - `"enable"` |
| **app-category**  any | (list or str) Application category ID list. |
| **app-group**  any | (list or str) Application group names. |
| **application**  any | (list) Application ID list. |
| **application-list**  string | Name of an existing Application list. |
| **auth-cert**  string | HTTPS server certificate for policy authentication. |
| **auth-path**  string | Enable/disable authentication-based routing.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-redirect-addr**  string | HTTP-to-HTTPS redirect address for firewall authentication. |
| **auto-asic-offload**  string | Enable/disable offloading security profile processing to CP processors.  **Choices:**   - `"disable"` - `"enable"` |
| **av-profile**  string | Name of an existing Antivirus profile. |
| **best-route**  string | Enable/disable the use of best route.  **Choices:**   - `"disable"` - `"enable"` |
| **block-notification**  string | Enable/disable block notification.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal-exempt**  string | Enable to exempt some users from the captive portal.  **Choices:**   - `"disable"` - `"enable"` |
| **capture-packet**  string | Enable/disable capture packets.  **Choices:**   - `"disable"` - `"enable"` |
| **casb-profile**  string | Name of an existing CASB profile. |
| **casi-profile**  string | CASI profile. |
| **cgn-eif**  string | Enable/Disable CGN endpoint independent filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eim**  string | Enable/Disable CGN endpoint independent mapping  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-log-server-grp**  string | NP log server group name |
| **cgn-resource-quota**  integer | resource quota |
| **cgn-session-quota**  integer | session quota |
| **cifs-profile**  string | Name of an existing CIFS profile. |
| **comments**  any | (dict or str) no description |
| **custom-log-fields**  any | (list or str) Custom fields to append to log messages for this policy. |
| **decrypted-traffic-mirror**  string | Decrypted traffic mirror. |
| **delay-tcp-npu-session**  string | Enable TCP NPU session delay to guarantee packet order of 3-way handshake.  **Choices:**   - `"disable"` - `"enable"` |
| **delay-tcp-npu-sessoin**  string | Enable/disable TCP NPU session delay in order to guarantee packet order of 3-way handshake.  **Choices:**   - `"disable"` - `"enable"` |
| **devices**  any | (list or str) Names of devices or device groups that can be matched by the policy. |
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
| **dstaddr**  any | (list or str) Destination address and address group names. |
| **dstaddr-negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr6**  any | (list or str) Destination IPv6 address name and address group names. |
| **dstaddr6-negate**  string | When enabled dstaddr6 specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstintf**  any | (list or str) Outgoing |
| **dynamic-shaping**  string | Enable/disable dynamic RADIUS defined traffic shaping.  **Choices:**   - `"disable"` - `"enable"` |
| **email-collect**  string | Enable/disable email collection.  **Choices:**   - `"disable"` - `"enable"` |
| **emailfilter-profile**  string | Name of an existing email filter profile. |
| **fec**  string | Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.  **Choices:**   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | Name of an existing file-filter profile. |
| **firewall-session-dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  **Choices:**   - `"check-all"` - `"check-new"` |
| **fixedport**  string | Enable to prevent source NAT from changing a sessions source port.  **Choices:**   - `"disable"` - `"enable"` |
| **fsso**  string | Enable/disable Fortinet Single Sign-On.  **Choices:**   - `"disable"` - `"enable"` |
| **fsso-agent-for-ntlm**  string | FSSO agent to use for NTLM authentication. |
| **fsso-groups**  any | (list or str) Names of FSSO groups. |
| **geoip-anycast**  string | Enable/disable recognition of anycast IP addresses using the geography IP database.  **Choices:**   - `"disable"` - `"enable"` |
| **geoip-match**  string | Match geography address based either on its physical location or registered location.  **Choices:**   - `"physical-location"` - `"registered-location"` |
| **global-label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  any | (list or str) Names of user groups that can authenticate with this policy. |
| **gtp-profile**  string | GTP profile. |
| **http-policy-redirect**  string | Redirect HTTP  **Choices:**   - `"disable"` - `"enable"` |
| **icap-profile**  string | Name of an existing ICAP profile. |
| **identity-based-route**  string | Name of identity-based routing rule. |
| **inbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | Policy inspection mode  **Choices:**   - `"proxy"` - `"flow"` |
| **internet-service**  string | Enable/disable use of Internet Services for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list or str) Custom Internet Service Name. |
| **internet-service-custom-group**  any | (list or str) Custom Internet Service group name. |
| **internet-service-group**  any | (list or str) Internet Service group name. |
| **internet-service-id**  any | (list or str) Internet Service ID. |
| **internet-service-name**  any | (list or str) Internet Service name. |
| **internet-service-negate**  string | When enabled internet-service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src**  string | Enable/disable use of Internet Services in source for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  any | (list or str) Custom Internet Service source name. |
| **internet-service-src-custom-group**  any | (list or str) Custom Internet Service source group name. |
| **internet-service-src-group**  any | (list or str) Internet Service source group name. |
| **internet-service-src-id**  any | (list or str) Internet Service source ID. |
| **internet-service-src-name**  any | (list or str) Internet Service source name. |
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
| **logtraffic-start**  string | Record logs when a session starts and ends.  **Choices:**   - `"disable"` - `"enable"` |
| **match-vip**  string | Enable to match packets that have had their destination addresses changed by a VIP.  **Choices:**   - `"disable"` - `"enable"` |
| **match-vip-only**  string | Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | Name of an existing MMS profile. |
| **name**  string | Policy name. |
| **nat**  string | Enable/disable source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  **Choices:**   - `"disable"` - `"enable"` |
| **nat64**  string | Enable/disable NAT64.  **Choices:**   - `"disable"` - `"enable"` |
| **natinbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **natip**  string | Policy-based IPsec VPN |
| **natoutbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **network-service-dynamic**  any | (list) no description |
| **network-service-src-dynamic**  any | (list) no description |
| **np-accelation**  string | Enable/disable UTM Network Processor acceleration.  **Choices:**   - `"disable"` - `"enable"` |
| **np-acceleration**  string | Enable/disable UTM Network Processor acceleration.  **Choices:**   - `"disable"` - `"enable"` |
| **ntlm**  string | Enable/disable NTLM authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **ntlm-enabled-browsers**  any | (list) HTTP-User-Agent value of supported browsers. |
| **ntlm-guest**  string | Enable/disable NTLM guest user access.  **Choices:**   - `"disable"` - `"enable"` |
| **object position**  list / elements=string | no description |
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
| **policyid**  integer / required | Policy ID. |
| **poolname**  any | (list or str) IP Pool names. |
| **poolname6**  any | (list or str) IPv6 pool names. |
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
| **rtp-addr**  any | (list or str) Address names if this is an RTP NAT policy. |
| **rtp-nat**  string | Enable Real Time Protocol  **Choices:**   - `"disable"` - `"enable"` |
| **scan-botnet-connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Schedule name. |
| **schedule-timeout**  string | Enable to force current sessions to end when the schedule object times out.  **Choices:**   - `"disable"` - `"enable"` |
| **sctp-filter-profile**  string | Name of an existing SCTP filter profile. |
| **send-deny-packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  **Choices:**   - `"disable"` - `"enable"` |
| **service**  any | (list or str) Service and service group names. |
| **service-negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **session-ttl**  any | (int or str) Session TTL in seconds for sessions accepted by this policy. |
| **sgt**  any | (list) no description |
| **sgt-check**  string | Enable/disable security group tags  **Choices:**   - `"disable"` - `"enable"` |
| **spamfilter-profile**  string | Name of an existing Spam filter profile. |
| **src-vendor-mac**  any | (list or str) Vendor MAC source ID. |
| **srcaddr**  any | (list or str) Source address and address group names. |
| **srcaddr-negate**  string | When enabled srcaddr specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr6**  any | (list or str) Source IPv6 address name and address group names. |
| **srcaddr6-negate**  string | When enabled srcaddr6 specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcintf**  any | (list or str) Incoming |
| **ssh-filter-profile**  string | Name of an existing SSH filter profile. |
| **ssh-policy-redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror**  string | Enable to copy decrypted SSL traffic to a FortiGate interface  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror-intf**  any | (list or str) SSL mirror interface name. |
| **ssl-ssh-profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **tags**  string | Names of object-tags applied to this policy. |
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
| **url-category**  any | (list or str) URL category ID list. |
| **users**  any | (list or str) Names of individual users that can authenticate with this policy. |
| **utm-status**  string | Enable to add one or more security profiles  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **videofilter-profile**  string | Name of an existing VideoFilter profile. |
| **virtual-patch-profile**  string | Name of an existing virtual-patch profile. |
| **vlan-cos-fwd**  integer | VLAN forward direction user priority |
| **vlan-cos-rev**  integer | VLAN reverse direction user priority |
| **vlan-filter**  string | Set VLAN filters. |
| **voip-profile**  string | Name of an existing VoIP profile. |
| **vpn_dst_node**  list / elements=dictionary | Vpn_Dst_Node. |
| **host**  string | Host. |
| **seq**  integer | Seq. |
| **subnet**  string | Subnet. |
| **vpn_src_node**  list / elements=dictionary | Vpn_Src_Node. |
| **host**  string | Host. |
| **seq**  integer | Seq. |
| **subnet**  string | Subnet. |
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
| **ztna-ems-tag**  any | (list or str) Source ztna-ems-tag names. |
| **ztna-ems-tag-secondary**  any | (list) no description |
| **ztna-geo-tag**  any | (list or str) Source ztna-geo-tag names. |
| **ztna-policy-redirect**  string | Redirect ZTNA traffic to matching Access-Proxy proxy-policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-status**  string | Enable/disable zero trust access.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-tags-match-logic**  string | ZTNA tag matching logic.  **Choices:**   - `"or"` - `"and"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_policy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_policy_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure IPv4 policies.
     fmgr_pkg_firewall_policy:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_policy:
           action: accept #<value in [deny, accept, ipsec, ...]>
           comments: ansible-comment
           dstaddr: all
           dstintf: any
           #name: ansible-test-policy
           nat: disable
           policyid: 1
           schedule: always
           service: ALL
           srcaddr: all
           srcintf: any
           status: disable

- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the IPv4 policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_policy'
           params:
               adom: 'ansible'
               pkg: 'ansible' # package name
               policy: 'your_value'
```

## [Return Values](fmgr_pkg_firewall_policy_module.md#id5)

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
