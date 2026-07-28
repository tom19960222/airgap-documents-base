---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_header_policy module – Configure IPv4/IPv6 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_header_policy_module.html
fetched_at: 2026-07-28T02:15:49+00:00
---
# fortinet.fortimanager.fmgr_pkg_header_policy module – Configure IPv4/IPv6 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_header_policy`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_pkg_header_policy_module.md#synopsis)
- [Parameters](fmgr_pkg_header_policy_module.md#parameters)
- [Notes](fmgr_pkg_header_policy_module.md#notes)
- [Examples](fmgr_pkg_header_policy_module.md#examples)
- [Return Values](fmgr_pkg_header_policy_module.md#return-values)

## [Synopsis](fmgr_pkg_header_policy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_header_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_header_policy**  dictionary | the top level parameters set |
| **_policy_block**  integer | Assigned policy block. |
| **access-proxy**  any | (list) no description |
| **action**  string | no description  **Choices:**   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` - `"redirect"` - `"isolate"` |
| **active-auth-method**  string | no description  **Choices:**   - `"ntlm"` - `"basic"` - `"digest"` - `"form"` |
| **anti-replay**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **app-category**  any | (list or str) no description |
| **app-group**  any | (list or str) no description |
| **application**  any | (list) no description |
| **application-charts**  list / elements=string | no description  **Choices:**   - `"top10-app"` - `"top10-p2p-user"` - `"top10-media-user"` |
| **application-list**  string | no description |
| **auth-cert**  string | no description |
| **auth-method**  string | no description  **Choices:**   - `"basic"` - `"digest"` - `"ntlm"` - `"fsae"` - `"form"` - `"fsso"` - `"rsso"` |
| **auth-path**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **auth-portal**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **auth-redirect-addr**  string | no description |
| **auto-asic-offload**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **av-profile**  string | no description |
| **bandwidth**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **best-route**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **block-notification**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal-exempt**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **capture-packet**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **casb-profile**  string | Name of an existing CASB profile. |
| **casi-profile**  any | (list or str) no description |
| **central-nat**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eif**  string | Enable/Disable CGN endpoint independent filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eim**  string | Enable/Disable CGN endpoint independent mapping  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-log-server-grp**  any | (list or str) NP log server group name |
| **cgn-resource-quota**  integer | resource quota |
| **cgn-session-quota**  integer | session quota |
| **cifs-profile**  string | no description |
| **client-reputation**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **client-reputation-mode**  string | no description  **Choices:**   - `"learning"` - `"monitoring"` |
| **comments**  any | (dict or str) no description |
| **custom-log-fields**  any | (list or str) no description |
| **decrypted-traffic-mirror**  string | no description |
| **deep-inspection-options**  any | (list or str) no description |
| **delay-tcp-npu-session**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **delay-tcp-npu-sessoin**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **device-detection-portal**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **device-ownership**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **devices**  any | (list or str) no description |
| **diffserv-copy**  string | Enable to copy packets DiffServ values from sessions original direction to its reply direction.  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-forward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | no description |
| **diffservcode-rev**  string | no description |
| **disclaimer**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"user"` - `"domain"` - `"policy"` |
| **dlp-profile**  string | Name of an existing DLP profile. |
| **dlp-sensor**  any | (list or str) no description |
| **dnsfilter-profile**  string | no description |
| **dponly**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-match**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-value**  string | no description |
| **dsri**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr**  any | (list or str) no description |
| **dstaddr-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr6**  any | (list or str) no description |
| **dstaddr6-negate**  string | When enabled dstaddr6 specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstintf**  any | (list or str) no description |
| **dynamic-bypass**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic-profile**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic-profile-access**  list / elements=string | no description  **Choices:**   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"im"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"ssh"` |
| **dynamic-profile-fallthrough**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic-profile-group**  any | (list or str) no description |
| **dynamic-shaping**  string | Enable/disable dynamic RADIUS defined traffic shaping.  **Choices:**   - `"disable"` - `"enable"` |
| **email-collect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **email-collection-portal**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **emailfilter-profile**  string | no description |
| **endpoint-check**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **endpoint-compliance**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **endpoint-keepalive-interface**  any | (list or str) no description |
| **endpoint-profile**  any | (list or str) no description |
| **extended-log**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **failed-connection**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fall-through-unauthenticated**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fec**  string | Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.  **Choices:**   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | no description |
| **firewall-session-dirty**  string | no description  **Choices:**   - `"check-all"` - `"check-new"` |
| **fixedport**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **force-proxy**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **forticlient-compliance-devices**  list / elements=string | no description  **Choices:**   - `"windows-pc"` - `"mac"` - `"iphone-ipad"` - `"android"` |
| **forticlient-compliance-enforcement-portal**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fsae**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fsae-server-for-ntlm**  any | (list or str) no description |
| **fsso**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fsso-agent-for-ntlm**  string | no description |
| **fsso-groups**  any | (list or str) no description |
| **geo-location**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **geoip-anycast**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **geoip-match**  string | no description  **Choices:**   - `"physical-location"` - `"registered-location"` |
| **global-label**  string | no description |
| **groups**  any | (list or str) no description |
| **gtp-profile**  string | no description |
| **http-policy-redirect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **http-tunnel-auth**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ia-profile**  any | (list) no description |
| **icap-profile**  string | no description |
| **identity-based**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **identity-based-policy**  list / elements=dictionary | no description |
| **action**  string | no description  **Choices:**   - `"deny"` - `"accept"` |
| **application-charts**  list / elements=string | no description  **Choices:**   - `"top10-app"` - `"top10-p2p-user"` - `"top10-media-user"` |
| **application-list**  string | no description |
| **av-profile**  string | no description |
| **capture-packet**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **deep-inspection-options**  string | no description |
| **devices**  string | no description |
| **dlp-sensor**  string | no description |
| **dstaddr**  string | no description |
| **dstaddr-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **endpoint-compliance**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **groups**  string | no description |
| **icap-profile**  string | no description |
| **id**  integer | no description |
| **ips-sensor**  string | no description |
| **logtraffic**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-app**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic-start**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | no description |
| **per-ip-shaper**  string | no description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  **Choices:**   - `"single"` - `"group"` |
| **replacemsg-group**  string | no description |
| **schedule**  string | no description |
| **send-deny-packet**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **service**  string | no description |
| **service-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **spamfilter-profile**  string | no description |
| **sslvpn-portal**  string | no description |
| **sslvpn-realm**  string | no description |
| **traffic-shaper**  string | no description |
| **traffic-shaper-reverse**  string | no description |
| **users**  string | no description |
| **utm-status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **voip-profile**  string | no description |
| **webfilter-profile**  string | no description |
| **identity-based-route**  string | no description |
| **identity-from**  string | no description  **Choices:**   - `"auth"` - `"device"` |
| **implicit-proxy-detection**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **inbound**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  **Choices:**   - `"proxy"` - `"flow"` |
| **internet-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list or str) no description |
| **internet-service-custom-group**  any | (list or str) no description |
| **internet-service-group**  any | (list or str) no description |
| **internet-service-id**  any | (list or str) no description |
| **internet-service-name**  any | (list or str) no description |
| **internet-service-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  any | (list or str) no description |
| **internet-service-src-custom-group**  any | (list or str) no description |
| **internet-service-src-group**  any | (list or str) no description |
| **internet-service-src-id**  any | (list or str) no description |
| **internet-service-src-name**  any | (list or str) no description |
| **internet-service-src-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
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
| **ip-based**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ip-version-type**  string | IP version of the policy. |
| **ippool**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sensor**  string | no description |
| **ips-voip-filter**  string | Name of an existing VoIP |
| **isolator-profile**  any | (list) no description |
| **isolator-server**  any | (list) no description |
| **label**  string | no description |
| **learning-mode**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **log-http-transaction**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **log-unmatched-traffic**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-app**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic-start**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **match-vip**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **match-vip-only**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **max-session-per-user**  integer | no description |
| **mms-profile**  any | (list or str) no description |
| **name**  string | no description |
| **nat**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  **Choices:**   - `"disable"` - `"enable"` |
| **nat64**  string | Enable/disable NAT64.  **Choices:**   - `"disable"` - `"enable"` |
| **natinbound**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **natip**  string | no description |
| **natoutbound**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **network-service-dynamic**  any | (list) no description |
| **network-service-src-dynamic**  any | (list) no description |
| **np-accelation**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **np-acceleration**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ntlm**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ntlm-enabled-browsers**  any | (list) no description |
| **ntlm-guest**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **outbound**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **pass-through**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **passive-wan-health-measurement**  string | Enable/disable passive WAN health measurement.  **Choices:**   - `"disable"` - `"enable"` |
| **pcp-inbound**  string | Enable/disable PCP inbound DNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **pcp-outbound**  string | Enable/disable PCP outbound SNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **pcp-poolname**  any | (list) no description |
| **per-ip-shaper**  string | no description |
| **permit-any-host**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **permit-stun-host**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **pfcp-profile**  string | PFCP profile. |
| **policy-behaviour-type**  string | Behaviour of the policy. |
| **policy-expiry**  string | Enable/disable policy expiry.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-expiry-date**  string | Policy expiry date |
| **policy-expiry-date-utc**  string | Policy expiry date and time, in epoch format. |
| **policy-offload**  string | Enable/Disable hardware session setup for CGNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **policyid**  integer / required | no description |
| **poolname**  any | (list or str) no description |
| **poolname6**  any | (list or str) no description |
| **profile-group**  string | no description |
| **profile-protocol-options**  string | no description |
| **profile-type**  string | no description  **Choices:**   - `"single"` - `"group"` |
| **radius-mac-auth-bypass**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **redirect-url**  string | no description |
| **replacemsg-group**  any | (list or str) no description |
| **replacemsg-override-group**  string | no description |
| **reputation-direction**  string | no description  **Choices:**   - `"source"` - `"destination"` |
| **reputation-direction6**  string | Direction of the initial traffic for IPv6 reputation to take effect.  **Choices:**   - `"source"` - `"destination"` |
| **reputation-minimum**  integer | no description |
| **reputation-minimum6**  integer | IPv6 Minimum Reputation to take action. |
| **require-tfa**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **reverse-cache**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **rsso**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **rtp-addr**  any | (list or str) no description |
| **rtp-nat**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **scan-botnet-connections**  string | no description  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | no description |
| **schedule-timeout**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sctp-filter-profile**  string | Name of an existing SCTP filter profile. |
| **send-deny-packet**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **service**  any | (list or str) no description |
| **service-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **session-ttl**  any | (int or str) no description |
| **sessions**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sgt**  any | (list) no description |
| **sgt-check**  string | Enable/disable security group tags  **Choices:**   - `"disable"` - `"enable"` |
| **spamfilter-profile**  any | (list or str) no description |
| **src-vendor-mac**  any | (list or str) no description |
| **srcaddr**  any | (list or str) no description |
| **srcaddr-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr6**  any | (list or str) no description |
| **srcaddr6-negate**  string | When enabled srcaddr6 specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcintf**  any | (list or str) no description |
| **ssh-filter-profile**  string | no description |
| **ssh-policy-check**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ssh-policy-redirect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror-intf**  any | (list or str) no description |
| **ssl-ssh-profile**  string | no description |
| **sslvpn-auth**  string | no description  **Choices:**   - `"any"` - `"local"` - `"radius"` - `"ldap"` - `"tacacs+"` |
| **sslvpn-ccert**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-cipher**  string | no description  **Choices:**   - `"any"` - `"high"` - `"medium"` |
| **sso-auth-method**  string | no description  **Choices:**   - `"fsso"` - `"rsso"` |
| **status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **tags**  any | (list or str) no description |
| **tcp-mss-receiver**  integer | no description |
| **tcp-mss-sender**  integer | no description |
| **tcp-reset**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-session-without-syn**  string | no description  **Choices:**   - `"all"` - `"data-only"` - `"disable"` |
| **tcp-timeout-pid**  any | (list) no description |
| **timeout-send-rst**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **tos**  string | no description |
| **tos-mask**  string | no description |
| **tos-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **traffic-shaper**  string | no description |
| **traffic-shaper-reverse**  string | no description |
| **transaction-based**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **transparent**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | no description  **Choices:**   - `"explicit-web"` - `"transparent"` - `"explicit-ftp"` - `"ssh-tunnel"` - `"ssh"` - `"wanopt"` - `"access-proxy"` |
| **udp-timeout-pid**  any | (list) no description |
| **url-category**  any | (list or str) no description |
| **users**  any | (list or str) no description |
| **utm-inspection-mode**  string | no description  **Choices:**   - `"proxy"` - `"flow"` |
| **utm-status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | no description |
| **uuid-idx**  integer | no description |
| **vendor-mac**  any | (list or str) no description |
| **videofilter-profile**  string | Name of an existing VideoFilter profile. |
| **virtual-patch-profile**  string | Name of an existing virtual-patch profile. |
| **vlan-cos-fwd**  integer | no description |
| **vlan-cos-rev**  integer | no description |
| **vlan-filter**  string | no description |
| **voip-profile**  string | no description |
| **vpntunnel**  string | no description |
| **waf-profile**  string | no description |
| **wanopt**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wanopt-detection**  string | no description  **Choices:**   - `"active"` - `"passive"` - `"off"` |
| **wanopt-passive-opt**  string | no description  **Choices:**   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt-peer**  string | no description |
| **wanopt-profile**  string | no description |
| **wccp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **web-auth-cookie**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **webcache**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **webcache-https**  string | no description  **Choices:**   - `"disable"` - `"ssl-server"` - `"any"` - `"enable"` |
| **webfilter-profile**  string | no description |
| **webproxy-forward-server**  string | no description |
| **webproxy-profile**  string | no description |
| **wsso**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-device-ownership**  string | Enable/disable zero trust device ownership.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-ems-tag**  any | (list or str) Source ztna-ems-tag names. |
| **ztna-ems-tag-secondary**  any | (list) no description |
| **ztna-geo-tag**  any | (list or str) Source ztna-geo-tag names. |
| **ztna-policy-redirect**  string | Redirect ZTNA traffic to matching Access-Proxy proxy-policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-status**  string | Enable/disable zero trust access.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-tags-match-logic**  string | no description  **Choices:**   - `"or"` - `"and"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_header_policy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_header_policy_module.md#id4)

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
   - name: Configure IPv4 header policies.
     fmgr_pkg_header_policy:
        bypass_validation: False
        pkg: ansible
        state: present
        pkg_header_policy:
           action: accept #<value in [deny, accept, ipsec, ...]>
           comments: 'ansible-comment'
           dstaddr: gall
           dstintf: any
           name: ansible-test-header
           policyid: 1073741826 # must larger than 2^30(1074741824), since header/footer policy is a special policy
           schedule: galways
           service: gALL
           srcaddr: gall
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
   - name: retrieve all the IPv4 header policies
     fmgr_fact:
       facts:
           selector: 'pkg_header_policy'
           params:
               pkg: 'ansible'
               policy: 'your_value'
```

## [Return Values](fmgr_pkg_header_policy_module.md#id5)

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
