---
collection: ansible
version: "6"
title: "community.network.netscaler_gslb_vserver module – Configure gslb vserver entities in Netscaler."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/netscaler_gslb_vserver_module.html
fetched_at: 2026-07-27T17:19:03+00:00
---
# community.network.netscaler_gslb_vserver module – Configure gslb vserver entities in Netscaler.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](netscaler_gslb_vserver_module.md#ansible-collections-community-network-netscaler-gslb-vserver-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.netscaler_gslb_vserver`.

- [Synopsis](netscaler_gslb_vserver_module.md#synopsis)
- [Requirements](netscaler_gslb_vserver_module.md#requirements)
- [Parameters](netscaler_gslb_vserver_module.md#parameters)
- [Notes](netscaler_gslb_vserver_module.md#notes)
- [Examples](netscaler_gslb_vserver_module.md#examples)

## [Synopsis](netscaler_gslb_vserver_module.md#id1)

- Configure gslb vserver entities in Netscaler.

## [Requirements](netscaler_gslb_vserver_module.md#id2)

The below requirements are needed on the host that executes this module.

- nitro python sdk

## [Parameters](netscaler_gslb_vserver_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **appflowlog**  string | Enable logging appflow flow information.  Choices:   - `"enabled"` - `"disabled"` |
| **backuplbmethod**  string | Backup load balancing method. Becomes operational if the primary load balancing method fails or cannot be used. Valid only if the primary method is based on either round-trip time (RTT) or static proximity.  Choices:   - `"ROUNDROBIN"` - `"LEASTCONNECTION"` - `"LEASTRESPONSETIME"` - `"SOURCEIPHASH"` - `"LEASTBANDWIDTH"` - `"LEASTPACKETS"` - `"STATICPROXIMITY"` - `"RTT"` - `"CUSTOMLOAD"` |
| **comment**  string | Any comments that you might want to associate with the GSLB virtual server. |
| **considereffectivestate**  string | If the primary state of all bound GSLB services is DOWN, consider the effective states of all the GSLB services, obtained through the Metrics Exchange Protocol (MEP), when determining the state of the GSLB virtual server. To consider the effective state, set the parameter to STATE_ONLY. To disregard the effective state, set the parameter to NONE.  The effective state of a GSLB service is the ability of the corresponding virtual server to serve traffic. The effective state of the load balancing virtual server, which is transferred to the GSLB service, is UP even if only one virtual server in the backup chain of virtual servers is in the UP state.  Choices:   - `"NONE"` - `"STATE_ONLY"` |
| **disabled**  boolean | When set to `yes` the GSLB Vserver state will be set to `disabled`.  When set to `no` the GSLB Vserver state will be set to `enabled`.  Note that due to limitations of the underlying NITRO API a `disabled` state change alone does not cause the module result to report a changed status.  Choices:   - `false` ← (default) - `true` |
| **disableprimaryondown**  string | Continue to direct traffic to the backup chain even after the primary GSLB virtual server returns to the UP state. Used when spillover is configured for the virtual server.  Choices:   - `"enabled"` - `"disabled"` |
| **dnsrecordtype**  string | DNS record type to associate with the GSLB virtual server’s domain name.  Default value: A  Possible values = A, AAAA, CNAME, NAPTR  Choices:   - `"A"` - `"AAAA"` - `"CNAME"` - `"NAPTR"` |
| **domain_bindings**  string | List of bindings for domains for this glsb vserver. |
| **cookietimeout**  string | Timeout, in minutes, for the GSLB site cookie. |
| **domainname**  string | Domain name for which to change the time to live (TTL) and/or backup service IP address. |
| **sitedomainttl**  string | TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server.  Minimum value = `1` |
| **ttl**  string | Time to live (TTL) for the domain. |
| **dynamicweight**  string | Specify if the appliance should consider the service count, service weights, or ignore both when using weight-based load balancing methods. The state of the number of services bound to the virtual server help the appliance to select the service.  Choices:   - `"SERVICECOUNT"` - `"SERVICEWEIGHT"` - `"DISABLED"` |
| **lbmethod**  string | Load balancing method for the GSLB virtual server.  Default value: LEASTCONNECTION  Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD  Choices:   - `"ROUNDROBIN"` - `"LEASTCONNECTION"` - `"LEASTRESPONSETIME"` - `"SOURCEIPHASH"` - `"LEASTBANDWIDTH"` - `"LEASTPACKETS"` - `"STATICPROXIMITY"` - `"RTT"` - `"CUSTOMLOAD"` |
| **mir**  string | Include multiple IP addresses in the DNS responses sent to clients.  Choices:   - `"enabled"` - `"disabled"` |
| **name**  string | Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or underscore `_` character, and must contain only ASCII alphanumeric, underscore `_`, hash `#`, period `.`, space, colon `:`, at `@`, equals `=`, and hyphen `-` characters. Can be changed after the virtual server is created.  Minimum length = 1 |
| **netmask**  string | IPv4 network mask for use in the SOURCEIPHASH load balancing method.  Minimum length = 1 |
| **nitro_pass**  string / required | The password with which to authenticate to the netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the nitro API objects.  Choices:   - `"http"` ← (default) - `"https"` |
| **nitro_timeout**  float | Time in seconds until a timeout error is thrown when establishing a new session with Netscaler  Default: `310.0` |
| **nitro_user**  string / required | The username with which to authenticate to the netscaler node. |
| **nsip**  string / required | The ip address of the netscaler appliance where the nitro API calls will be made.  The port can be specified with the colon (:). E.g. 192.168.1.1:555. |
| **persistenceid**  string | The persistence ID for the GSLB virtual server. The ID is a positive integer that enables GSLB sites to identify the GSLB virtual server, and is required if source IP address based or spill over based persistence is enabled on the virtual server.  Minimum value = `0`  Maximum value = `65535` |
| **persistencetype**  string | Use source IP address based persistence for the virtual server.  After the load balancing method selects a service for the first packet, the IP address received in response to the DNS query is used for subsequent requests from the same client.  Choices:   - `"SOURCEIP"` - `"NONE"` |
| **persistmask**  string | The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based persistence.  Minimum length = 1 |
| **save_config**  boolean | If `yes` the module will save the configuration on the netscaler node if it makes any changes.  The module will not save the configuration on the netscaler node if it made no changes.  Choices:   - `false` - `true` ← (default) |
| **service_bindings**  string | List of bindings for gslb services bound to this gslb virtual server. |
| **servicename**  string | Name of the GSLB service for which to change the weight. |
| **weight**  string | Weight to assign to the GSLB service. |
| **servicetype**  string | Protocol used by services bound to the virtual server.  Choices:   - `"HTTP"` - `"FTP"` - `"TCP"` - `"UDP"` - `"SSL"` - `"SSL_BRIDGE"` - `"SSL_TCP"` - `"NNTP"` - `"ANY"` - `"SIP_UDP"` - `"SIP_TCP"` - `"SIP_SSL"` - `"RADIUS"` - `"RDP"` - `"RTSP"` - `"MYSQL"` - `"MSSQL"` - `"ORACLE"` |
| **sobackupaction**  string | Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.  Choices:   - `"DROP"` - `"ACCEPT"` - `"REDIRECT"` |
| **somethod**  string | Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:  \* `CONNECTION` - Spillover occurs when the number of client connections exceeds the threshold.  \* `DYNAMICCONNECTION` - Spillover occurs when the number of client connections at the GSLB virtual server exceeds the sum of the maximum client (Max Clients) settings for bound GSLB services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of the bound GSLB services.  \* `BANDWIDTH` - Spillover occurs when the bandwidth consumed by the GSLB virtual server’s incoming and outgoing traffic exceeds the threshold.  \* `HEALTH` - Spillover occurs when the percentage of weights of the GSLB services that are UP drops below the threshold. For example, if services gslbSvc1, gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3 or gslbSvc2 and gslbSvc3 transition to DOWN.  \* `NONE` - Spillover does not occur.  Choices:   - `"CONNECTION"` - `"DYNAMICCONNECTION"` - `"BANDWIDTH"` - `"HEALTH"` - `"NONE"` |
| **sopersistence**  string | If spillover occurs, maintain source IP address based persistence for both primary and backup GSLB virtual servers.  Choices:   - `"enabled"` - `"disabled"` |
| **sopersistencetimeout**  string | Timeout for spillover persistence, in minutes.  Default value: `2`  Minimum value = `2`  Maximum value = `1440` |
| **sothreshold**  string | Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).  Minimum value = `1`  Maximum value = `4294967287` |
| **state**  string | The state of the resource being configured by the module on the netscaler node.  When present the resource will be created if needed and configured according to the module’s parameters.  When absent the resource will be deleted from the netscaler node.  Choices:   - `"absent"` - `"present"` ← (default) |
| **timeout**  string | Idle time, in minutes, after which a persistence entry is cleared.  Default value: `2`  Minimum value = `2`  Maximum value = `1440` |
| **tolerance**  string | Site selection tolerance, in milliseconds, for implementing the RTT load balancing method. If a site’s RTT deviates from the lowest RTT by more than the specified tolerance, the site is not considered when the NetScaler appliance makes a GSLB decision. The appliance implements the round robin method of global server load balancing between sites whose RTT values are within the specified tolerance. If the tolerance is 0 (zero), the appliance always sends clients the IP address of the site with the lowest RTT.  Minimum value = `0`  Maximum value = `100` |
| **v6netmasklen**  string | Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by the `SOURCEIPHASH` load balancing method.  Default value: `128`  Minimum value = `1`  Maximum value = `128` |
| **v6persistmasklen**  string | Number of bits to consider in an IPv6 source IP address when creating source IP address based persistence sessions.  Default value: `128`  Minimum value = `1`  Maximum value = `128` |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](netscaler_gslb_vserver_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Citrix NetScaler Network devices see <https://www.ansible.com/ansible-netscaler>.

## [Examples](netscaler_gslb_vserver_module.md#id5)

```yaml+jinja
# FIXME: Add examples
```

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
