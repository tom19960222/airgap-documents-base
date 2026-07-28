---
collection: ansible
version: "8"
title: "cisco.meraki.networks_wireless_ssids module – Resource module for networks _wireless _ssids"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_wireless_ssids_module.html
fetched_at: 2026-07-28T01:35:49+00:00
---
# cisco.meraki.networks_wireless_ssids module – Resource module for networks _wireless _ssids

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
> You need further requirements to be able to use this module,
> see [Requirements](networks_wireless_ssids_module.md#ansible-collections-cisco-meraki-networks-wireless-ssids-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_wireless_ssids`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_wireless_ssids_module.md#synopsis)
- [Requirements](networks_wireless_ssids_module.md#requirements)
- [Parameters](networks_wireless_ssids_module.md#parameters)
- [Notes](networks_wireless_ssids_module.md#notes)
- [See Also](networks_wireless_ssids_module.md#see-also)
- [Examples](networks_wireless_ssids_module.md#examples)
- [Return Values](networks_wireless_ssids_module.md#return-values)

## [Synopsis](networks_wireless_ssids_module.md#id1)

- Manage operation update of the resource networks _wireless _ssids.
- Update the attributes of an MR SSID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_wireless_ssids_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_wireless_ssids_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activeDirectory**  dictionary | The current setting for Active Directory. Only valid if splashPage is ‘Password-protected with Active Directory’. |
| **credentials**  dictionary | (Optional) The credentials of the user account to be used by the AP to bind to your Active Directory server. The Active Directory account should have permissions on all your Active Directory servers. Only valid if the splashPage is ‘Password-protected with Active Directory’. |
| **logonName**  string | The logon name of the Active Directory account. |
| **password**  string | The password to the Active Directory user account. |
| **servers**  list / elements=dictionary | The Active Directory servers to be used for authentication. |
| **host**  string | IP address of your Active Directory server. |
| **port**  integer | (Optional) UDP port the Active Directory server listens on. By default, uses port 3268. |
| **adultContentFilteringEnabled**  boolean | Boolean indicating whether or not adult content will be blocked.  **Choices:**   - `false` - `true` |
| **apTagsAndVlanIds**  list / elements=dictionary | The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is ‘Bridge mode’ or ‘Layer 3 roaming’. |
| **tags**  list / elements=string | Array of AP tags. |
| **vlanId**  integer | Numerical identifier that is assigned to the VLAN. |
| **authMode**  string | The association control method for the SSID (‘open’, ‘open-enhanced’, ‘psk’, ‘open-with-radius’, ‘open-with-nac’, ‘8021x-meraki’, ‘8021x-nac’, ‘8021x-radius’, ‘8021x-google’, ‘8021x-localradius’, ‘ipsk-with-radius’ or ‘ipsk-without-radius’). |
| **availabilityTags**  list / elements=string | Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list. |
| **availableOnAllAps**  boolean | Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.  **Choices:**   - `false` - `true` |
| **bandSelection**  string | The client-serving radio frequencies of this SSID in the default indoor RF profile. (‘Dual band operation’, ‘5 GHz band only’ or ‘Dual band operation with Band Steering’). |
| **concentratorNetworkId**  string | The concentrator to use when the ipAssignmentMode is ‘Layer 3 roaming with a concentrator’ or ‘VPN’. |
| **defaultVlanId**  integer | The default VLAN ID used for ‘all other APs’. This param is only valid when the ipAssignmentMode is ‘Bridge mode’ or ‘Layer 3 roaming’. |
| **disassociateClientsOnVpnFailover**  boolean | Disassociate clients when ‘VPN’ concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is ‘VPN’.  **Choices:**   - `false` - `true` |
| **dnsRewrite**  dictionary | DNS servers rewrite settings. |
| **dnsCustomNameservers**  list / elements=string | User specified DNS servers (up to two servers). |
| **enabled**  boolean | Boolean indicating whether or not DNS server rewrite is enabled. If disabled, upstream DNS will be used.  **Choices:**   - `false` - `true` |
| **dot11r**  dictionary | The current setting for 802.11r. |
| **adaptive**  boolean | (Optional) Whether 802.11r is adaptive or not.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Whether 802.11r is enabled or not.  **Choices:**   - `false` - `true` |
| **dot11w**  dictionary | The current setting for Protected Management Frames (802.11w). |
| **enabled**  boolean | Whether 802.11w is enabled or not.  **Choices:**   - `false` - `true` |
| **required**  boolean | (Optional) Whether 802.11w is required or not.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Whether or not the SSID is enabled.  **Choices:**   - `false` - `true` |
| **encryptionMode**  string | The psk encryption mode for the SSID (‘wep’ or ‘wpa’). This param is only valid if the authMode is ‘psk’. |
| **enterpriseAdminAccess**  string | Whether or not an SSID is accessible by ‘enterprise’ administrators (‘access disabled’ or ‘access enabled’). |
| **gre**  dictionary | Ethernet over GRE settings. |
| **concentrator**  dictionary | The EoGRE concentrator’s settings. |
| **host**  string | The EoGRE concentrator’s IP or FQDN. This param is required when ipAssignmentMode is ‘Ethernet over GRE’. |
| **key**  integer | Optional numerical identifier that will add the GRE key field to the GRE header. Used to identify an individual traffic flow within a tunnel. |
| **ipAssignmentMode**  string | The client IP assignment mode (‘NAT mode’, ‘Bridge mode’, ‘Layer 3 roaming’, ‘Ethernet over GRE’, ‘Layer 3 roaming with a concentrator’ or ‘VPN’). |
| **lanIsolationEnabled**  boolean | Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is ‘Bridge mode’.  **Choices:**   - `false` - `true` |
| **ldap**  dictionary | The current setting for LDAP. Only valid if splashPage is ‘Password-protected with LDAP’. |
| **baseDistinguishedName**  string | The base distinguished name of users on the LDAP server. |
| **credentials**  dictionary | (Optional) The credentials of the user account to be used by the AP to bind to your LDAP server. The LDAP account should have permissions on all your LDAP servers. |
| **distinguishedName**  string | The distinguished name of the LDAP user account (example cn=user,dc=meraki,dc=com). |
| **password**  string | The password of the LDAP user account. |
| **serverCaCertificate**  dictionary | The CA certificate used to sign the LDAP server’s key. |
| **contents**  string | The contents of the CA certificate. Must be in PEM or DER format. |
| **servers**  list / elements=dictionary | The LDAP servers to be used for authentication. |
| **host**  string | IP address of your LDAP server. |
| **port**  integer | UDP port the LDAP server listens on. |
| **localRadius**  dictionary | The current setting for Local Authentication, a built-in RADIUS server on the access point. Only valid if authMode is ‘8021x-localradius’. |
| **cacheTimeout**  integer | The duration (in seconds) for which LDAP and OCSP lookups are cached. |
| **certificateAuthentication**  dictionary | The current setting for certificate verification. |
| **clientRootCaCertificate**  dictionary | The Client CA Certificate used to sign the client certificate. |
| **contents**  string | The contents of the Client CA Certificate. Must be in PEM or DER format. |
| **enabled**  boolean | Whether or not to use EAP-TLS certificate-based authentication to validate wireless clients.  **Choices:**   - `false` - `true` |
| **ocspResponderUrl**  string | (Optional) The URL of the OCSP responder to verify client certificate status. |
| **useLdap**  boolean | Whether or not to verify the certificate with LDAP.  **Choices:**   - `false` - `true` |
| **useOcsp**  boolean | Whether or not to verify the certificate with OCSP.  **Choices:**   - `false` - `true` |
| **passwordAuthentication**  dictionary | The current setting for password-based authentication. |
| **enabled**  boolean | Whether or not to use EAP-TTLS/PAP or PEAP-GTC password-based authentication via LDAP lookup.  **Choices:**   - `false` - `true` |
| **mandatoryDhcpEnabled**  boolean | If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won’t be able to associate.  **Choices:**   - `false` - `true` |
| **meraki_action_batch_retry_wait_time**  integer | meraki_action_batch_retry_wait_time (integer), action batch concurrency error retry wait time  **Default:** `60` |
| **meraki_api_key**  string / required | meraki_api_key (string), API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY |
| **meraki_base_url**  string | meraki_base_url (string), preceding all endpoint resources  **Default:** `"https://api.meraki.com/api/v1"` |
| **meraki_be_geo_id**  string | meraki_be_geo_id (string), optional partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID  **Default:** `""` |
| **meraki_caller**  string | meraki_caller (string), optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER  **Default:** `""` |
| **meraki_certificate_path**  string | meraki_certificate_path (string), path for TLS/SSL certificate verification if behind local proxy  **Default:** `""` |
| **meraki_inherit_logging_config**  boolean | meraki_inherit_logging_config (boolean), Inherits your own logger instance  **Choices:**   - `false` ← (default) - `true` |
| **meraki_log_file_prefix**  string | meraki_log_file_prefix (string), log file name appended with date and timestamp  **Default:** `"meraki_api_"` |
| **meraki_log_path**  string | log_path (string), path to output log; by default, working directory of script if not specified  **Default:** `""` |
| **meraki_maximum_retries**  integer | meraki_maximum_retries (integer), retry up to this many times when encountering 429s or other server-side errors  **Default:** `2` |
| **meraki_nginx_429_retry_wait_time**  integer | meraki_nginx_429_retry_wait_time (integer), Nginx 429 retry wait time  **Default:** `60` |
| **meraki_output_log**  boolean | meraki_output_log (boolean), create an output log file?  **Choices:**   - `false` - `true` ← (default) |
| **meraki_print_console**  boolean | meraki_print_console (boolean), print logging output to console?  **Choices:**   - `false` - `true` ← (default) |
| **meraki_requests_proxy**  string | meraki_requests_proxy (string), proxy server and port, if needed, for HTTPS  **Default:** `""` |
| **meraki_retry_4xx_error**  boolean | meraki_retry_4xx_error (boolean), retry if encountering other 4XX error (besides 429)?  **Choices:**   - `false` ← (default) - `true` |
| **meraki_retry_4xx_error_wait_time**  integer | meraki_retry_4xx_error_wait_time (integer), other 4XX error retry wait time  **Default:** `60` |
| **meraki_simulate**  boolean | meraki_simulate (boolean), simulate POST/PUT/DELETE calls to prevent changes?  **Choices:**   - `false` ← (default) - `true` |
| **meraki_single_request_timeout**  integer | meraki_single_request_timeout (integer), maximum number of seconds for each API call  **Default:** `60` |
| **meraki_suppress_logging**  boolean | meraki_suppress_logging (boolean), disable all logging? you’re on your own then!  **Choices:**   - `false` ← (default) - `true` |
| **meraki_use_iterator_for_get_pages**  boolean | meraki_use_iterator_for_get_pages (boolean), list\* methods will return an iterator with each object instead of a complete list with all items  **Choices:**   - `false` ← (default) - `true` |
| **meraki_wait_on_rate_limit**  boolean | meraki_wait_on_rate_limit (boolean), retry if 429 rate limit error encountered?  **Choices:**   - `false` - `true` ← (default) |
| **minBitrate**  float | The minimum bitrate in Mbps of this SSID in the default indoor RF profile. (‘1’, ‘2’, ‘5.5’, ‘6’, ‘9’, ‘11’, ‘12’, ‘18’, ‘24’, ‘36’, ‘48’ or ‘54’). |
| **name**  string | The name of the SSID. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **number**  string | Number path parameter. |
| **oauth**  dictionary | The OAuth settings of this SSID. Only valid if splashPage is ‘Google OAuth’. |
| **allowedDomains**  list / elements=string | (Optional) The list of domains allowed access to the network. |
| **perClientBandwidthLimitDown**  integer | The download bandwidth limit in Kbps. (0 represents no limit.). |
| **perClientBandwidthLimitUp**  integer | The upload bandwidth limit in Kbps. (0 represents no limit.). |
| **perSsidBandwidthLimitDown**  integer | The total download bandwidth limit in Kbps. (0 represents no limit.). |
| **perSsidBandwidthLimitUp**  integer | The total upload bandwidth limit in Kbps. (0 represents no limit.). |
| **psk**  string | The passkey for the SSID. This param is only valid if the authMode is ‘psk’. |
| **radiusAccountingEnabled**  boolean | Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is ‘open-with-radius’, ‘8021x-radius’ or ‘ipsk-with-radius’.  **Choices:**   - `false` - `true` |
| **radiusAccountingInterimInterval**  integer | The interval (in seconds) in which accounting information is updated and sent to the RADIUS accounting server. |
| **radiusAccountingServers**  list / elements=dictionary | The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is ‘open-with-radius’, ‘8021x-radius’ or ‘ipsk-with-radius’ and radiusAccountingEnabled is ‘true’. |
| **caCertificate**  string | Certificate used for authorization for the RADSEC Server. |
| **host**  string | IP address to which the APs will send RADIUS accounting messages. |
| **port**  integer | Port on the RADIUS server that is listening for accounting messages. |
| **radsecEnabled**  boolean | Use RADSEC (TLS over TCP) to connect to this RADIUS accounting server. Requires radiusProxyEnabled.  **Choices:**   - `false` - `true` |
| **secret**  string | Shared key used to authenticate messages between the APs and RADIUS server. |
| **radiusAttributeForGroupPolicies**  string | Specify the RADIUS attribute used to look up group policies (‘Filter-Id’, ‘Reply-Message’, ‘Airespace-ACL-Name’ or ‘Aruba-User-Role’). Access points must receive this attribute in the RADIUS Access-Accept message. |
| **radiusAuthenticationNasId**  string | The template of the NAS identifier to be used for RADIUS authentication (ex. $NODE_MAC$ $VAP_NUM$). |
| **radiusCalledStationId**  string | The template of the called station identifier to be used for RADIUS (ex. $NODE_MAC$ $VAP_NUM$). |
| **radiusCoaEnabled**  boolean | If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.  **Choices:**   - `false` - `true` |
| **radiusFailoverPolicy**  string | This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable (‘Deny access’ or ‘Allow access’). |
| **radiusFallbackEnabled**  boolean | Whether or not higher priority RADIUS servers should be retried after 60 seconds.  **Choices:**   - `false` - `true` |
| **radiusGuestVlanEnabled**  boolean | Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is ‘open-with-radius’ and addressing mode is not set to ‘isolated’ or ‘nat’ mode.  **Choices:**   - `false` - `true` |
| **radiusGuestVlanId**  integer | VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is ‘open-with-radius’ and addressing mode is not set to ‘isolated’ or ‘nat’ mode. |
| **radiusLoadBalancingPolicy**  string | This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts (‘Strict priority order’ or ‘Round robin’). |
| **radiusOverride**  boolean | If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is ‘NAT mode’.  **Choices:**   - `false` - `true` |
| **radiusProxyEnabled**  boolean | If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers.  **Choices:**   - `false` - `true` |
| **radiusServerAttemptsLimit**  integer | The maximum number of transmit attempts after which a RADIUS server is failed over (must be between 1-5). |
| **radiusServers**  list / elements=dictionary | The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is ‘open-with-radius’, ‘8021x-radius’ or ‘ipsk-with-radius’. |
| **caCertificate**  string | Certificate used for authorization for the RADSEC Server. |
| **host**  string | IP address of your RADIUS server. |
| **openRoamingCertificateId**  integer | The ID of the Openroaming Certificate attached to radius server. |
| **port**  integer | UDP port the RADIUS server listens on for Access-requests. |
| **radsecEnabled**  boolean | Use RADSEC (TLS over TCP) to connect to this RADIUS server. Requires radiusProxyEnabled.  **Choices:**   - `false` - `true` |
| **secret**  string | RADIUS client shared secret. |
| **radiusServerTimeout**  integer | The amount of time for which a RADIUS client waits for a reply from the RADIUS server (must be between 1-10 seconds). |
| **radiusTestingEnabled**  boolean | If true, Meraki devices will periodically send Access-Request messages to configured RADIUS servers using identity ‘meraki_8021x_test’ to ensure that the RADIUS servers are reachable.  **Choices:**   - `false` - `true` |
| **secondaryConcentratorNetworkId**  string | The secondary concentrator to use when the ipAssignmentMode is ‘VPN’. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. (‘disabled’ represents no secondary concentrator.). |
| **speedBurst**  dictionary | The SpeedBurst setting for this SSID’. |
| **enabled**  boolean | Boolean indicating whether or not to allow users to temporarily exceed the bandwidth limit for short periods while still keeping them under the bandwidth limit over time.  **Choices:**   - `false` - `true` |
| **splashGuestSponsorDomains**  list / elements=string | Array of valid sponsor email domains for sponsored guest splash type. |
| **splashPage**  string | The type of splash page for the SSID (‘None’, ‘Click-through splash page’, ‘Billing’, ‘Password-protected with Meraki RADIUS’, ‘Password-protected with custom RADIUS’, ‘Password-protected with Active Directory’, ‘Password-protected with LDAP’, ‘SMS authentication’, ‘Systems Manager Sentry’, ‘Facebook Wi-Fi’, ‘Google OAuth’, ‘Sponsored guest’, ‘Cisco ISE’ or ‘Google Apps domain’). This attribute is not supported for template children. |
| **useVlanTagging**  boolean | Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is ‘Bridge mode’ or ‘Layer 3 roaming’.  **Choices:**   - `false` - `true` |
| **visible**  boolean | Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true.  **Choices:**   - `false` - `true` |
| **vlanId**  integer | The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is ‘Layer 3 roaming with a concentrator’ or ‘VPN’. |
| **walledGardenEnabled**  boolean | Allow access to a configurable list of IP ranges, which users may access prior to sign-on.  **Choices:**   - `false` - `true` |
| **walledGardenRanges**  list / elements=string | Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. ‘192.168.1.1/24’, ‘192.168.37.10/32’, ‘www.yahoo.com’, ‘\*.google.com’). Meraki’s splash page is automatically included in your walled garden. |
| **wpaEncryptionMode**  string | The types of WPA encryption. (‘WPA1 only’, ‘WPA1 and WPA2’, ‘WPA2 only’, ‘WPA3 Transition Mode’, ‘WPA3 only’ or ‘WPA3 192-bit Security’). |

## [Notes](networks_wireless_ssids_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.update_network_wireless_ssid,
> - Paths used are put /networks/{networkId}/wireless/ssids/{number},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_wireless_ssids_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for wireless updateNetworkWirelessSsid](https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid)
> :   Complete reference of the updateNetworkWirelessSsid API.

## [Examples](networks_wireless_ssids_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.meraki.networks_wireless_ssids:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    enabled: true
    name: My SSID
    networkId: string
    number: string
```

## [Return Values](networks_wireless_ssids_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
