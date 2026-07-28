---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_radius module – Configure RADIUS server entries."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_radius_module.html
fetched_at: 2026-07-28T02:21:11+00:00
---
# fortinet.fortimanager.fmgr_user_radius module – Configure RADIUS server entries.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_radius`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_user_radius_module.md#synopsis)
- [Parameters](fmgr_user_radius_module.md#parameters)
- [Notes](fmgr_user_radius_module.md#notes)
- [Examples](fmgr_user_radius_module.md#examples)
- [Return Values](fmgr_user_radius_module.md#return-values)

## [Synopsis](fmgr_user_radius_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_radius_module.md#id2)

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
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **user_radius**  dictionary | the top level parameters set |
| **account-key-cert-field**  string | Define subject identity field in certificate for user access right checking.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **account-key-processing**  string | Account key processing operation.  **Choices:**   - `"same"` - `"strip"` |
| **accounting-server**  list / elements=dictionary | Accounting-Server. |
| **id**  integer | ID |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **port**  integer | RADIUS accounting port number. |
| **secret**  any | (list) Secret key. |
| **server**  string | no description |
| **source-ip**  string | Source IP address for communications to the RADIUS server. |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **acct-all-servers**  string | Enable/disable sending of accounting messages to all configured servers  **Choices:**   - `"disable"` - `"enable"` |
| **acct-interim-interval**  integer | Time in seconds between each accounting interim update message. |
| **all-usergroup**  string | Enable/disable automatically including this RADIUS server in all user groups.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-type**  string | Authentication methods/protocols permitted for this RADIUS server.  **Choices:**   - `"pap"` - `"chap"` - `"ms_chap"` - `"ms_chap_v2"` - `"auto"` |
| **ca-cert**  string | CA of server to trust under TLS. |
| **call-station-id-type**  string | Calling & Called station identifier type configuration  **Choices:**   - `"legacy"` - `"IP"` - `"MAC"` |
| **class**  any | (list) Class attribute name |
| **client-cert**  string | Client certificate to use under TLS. |
| **delimiter**  string | Configure delimiter to be used for separating profile group names in the SSO attribute  **Choices:**   - `"plus"` - `"comma"` |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **account-key-cert-field**  string | Define subject identity field in certificate for user access right checking.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **account-key-processing**  string | Account key processing operation.  **Choices:**   - `"same"` - `"strip"` |
| **accounting-server**  list / elements=dictionary | Accounting-Server. |
| **id**  integer | ID |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **port**  integer | RADIUS accounting port number. |
| **secret**  any | (list) Secret key. |
| **server**  string | no description |
| **source-ip**  string | Source IP address for communications to the RADIUS server. |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **acct-all-servers**  string | Enable/disable sending of accounting messages to all configured servers  **Choices:**   - `"disable"` - `"enable"` |
| **acct-interim-interval**  integer | Time in seconds between each accounting interim update message. |
| **all-usergroup**  string | Enable/disable automatically including this RADIUS server in all user groups.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-type**  string | Authentication methods/protocols permitted for this RADIUS server.  **Choices:**   - `"pap"` - `"chap"` - `"ms_chap"` - `"ms_chap_v2"` - `"auto"` |
| **ca-cert**  string | CA of server to trust under TLS. |
| **call-station-id-type**  string | Calling & Called station identifier type configuration  **Choices:**   - `"legacy"` - `"IP"` - `"MAC"` |
| **class**  any | (list) Class attribute name |
| **client-cert**  string | Client certificate to use under TLS. |
| **delimiter**  string | Configure delimiter to be used for separating profile group names in the SSO attribute  **Choices:**   - `"plus"` - `"comma"` |
| **dp-carrier-endpoint-attribute**  string | Dp-Carrier-Endpoint-Attribute.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **dp-carrier-endpoint-block-attribute**  string | Dp-Carrier-Endpoint-Block-Attribute.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **dp-context-timeout**  integer | Dp-Context-Timeout. |
| **dp-flush-ip-session**  string | Dp-Flush-Ip-Session.  **Choices:**   - `"disable"` - `"enable"` |
| **dp-hold-time**  integer | Dp-Hold-Time. |
| **dp-http-header**  string | Dp-Http-Header. |
| **dp-http-header-fallback**  string | Dp-Http-Header-Fallback.  **Choices:**   - `"ip-header-address"` - `"default-profile"` |
| **dp-http-header-status**  string | Dp-Http-Header-Status.  **Choices:**   - `"disable"` - `"enable"` |
| **dp-http-header-suppress**  string | Dp-Http-Header-Suppress.  **Choices:**   - `"disable"` - `"enable"` |
| **dp-log-dyn_flags**  list / elements=string | Dp-Log-Dyn_Flags.  **Choices:**   - `"none"` - `"protocol-error"` - `"profile-missing"` - `"context-missing"` - `"accounting-stop-missed"` - `"accounting-event"` - `"radiusd-other"` - `"endpoint-block"` |
| **dp-log-period**  integer | Dp-Log-Period. |
| **dp-mem-percent**  integer | Dp-Mem-Percent. |
| **dp-profile-attribute**  string | Dp-Profile-Attribute.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **dp-profile-attribute-key**  string | Dp-Profile-Attribute-Key. |
| **dp-radius-response**  string | Dp-Radius-Response.  **Choices:**   - `"disable"` - `"enable"` |
| **dp-radius-server-port**  integer | Dp-Radius-Server-Port. |
| **dp-secret**  any | (list) Dp-Secret. |
| **dp-validate-request-secret**  string | Dp-Validate-Request-Secret.  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic-profile**  string | Dynamic-Profile.  **Choices:**   - `"disable"` - `"enable"` |
| **endpoint-translation**  string | Endpoint-Translation.  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-convert-hex**  string | Ep-Carrier-Endpoint-Convert-Hex.  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-header**  string | Ep-Carrier-Endpoint-Header. |
| **ep-carrier-endpoint-header-suppress**  string | Ep-Carrier-Endpoint-Header-Suppress.  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-prefix**  string | Ep-Carrier-Endpoint-Prefix.  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-prefix-range-max**  integer | Ep-Carrier-Endpoint-Prefix-Range-Max. |
| **ep-carrier-endpoint-prefix-range-min**  integer | Ep-Carrier-Endpoint-Prefix-Range-Min. |
| **ep-carrier-endpoint-prefix-string**  string | Ep-Carrier-Endpoint-Prefix-String. |
| **ep-carrier-endpoint-source**  string | Ep-Carrier-Endpoint-Source.  **Choices:**   - `"http-header"` - `"cookie"` |
| **ep-ip-header**  string | Ep-Ip-Header. |
| **ep-ip-header-suppress**  string | Ep-Ip-Header-Suppress.  **Choices:**   - `"disable"` - `"enable"` |
| **ep-missing-header-fallback**  string | Ep-Missing-Header-Fallback.  **Choices:**   - `"session-ip"` - `"policy-profile"` |
| **ep-profile-query-type**  string | Ep-Profile-Query-Type.  **Choices:**   - `"session-ip"` - `"extract-ip"` - `"extract-carrier-endpoint"` |
| **group-override-attr-type**  string | Group-Override-Attr-Type.  **Choices:**   - `"filter-Id"` - `"class"` |
| **h3c-compatibility**  string | Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **mac-case**  string | MAC authentication case  **Choices:**   - `"uppercase"` - `"lowercase"` |
| **mac-password-delimiter**  string | MAC authentication password delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-username-delimiter**  string | MAC authentication username delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **nas-id**  string | Custom NAS identifier. |
| **nas-id-type**  string | NAS identifier type configuration  **Choices:**   - `"legacy"` - `"custom"` - `"hostname"` |
| **nas-ip**  string | IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes. |
| **password-encoding**  string | Password encoding.  **Choices:**   - `"ISO-8859-1"` - `"auto"` |
| **password-renewal**  string | Enable/disable password renewal.  **Choices:**   - `"disable"` - `"enable"` |
| **radius-coa**  string | Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after …  **Choices:**   - `"disable"` - `"enable"` |
| **radius-port**  integer | RADIUS service port number. |
| **rsso**  string | Enable/disable RADIUS based single sign on feature.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-context-timeout**  integer | Time in seconds before the logged out user is removed from the user context list of logged on users. |
| **rsso-endpoint-attribute**  string | RADIUS attributes used to extract the user end point identifer from the RADIUS Start record.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **rsso-endpoint-block-attribute**  string | RADIUS attributes used to block a user.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **rsso-ep-one-ip-only**  string | Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-flush-ip-session**  string | Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-log-flags**  list / elements=string | Events to log.  **Choices:**   - `"none"` - `"protocol-error"` - `"profile-missing"` - `"context-missing"` - `"accounting-stop-missed"` - `"accounting-event"` - `"radiusd-other"` - `"endpoint-block"` |
| **rsso-log-period**  integer | Time interval in seconds that group event log messages will be generated for dynamic profile events. |
| **rsso-radius-response**  string | Enable/disable sending RADIUS response packets after receiving Start and Stop records.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-radius-server-port**  integer | UDP port to listen on for RADIUS Start and Stop records. |
| **rsso-secret**  any | (list) RADIUS secret used by the RADIUS accounting server. |
| **rsso-validate-request-secret**  string | Enable/disable validating the RADIUS request shared secret in the Start or End record.  **Choices:**   - `"disable"` - `"enable"` |
| **secondary-secret**  any | (list) Secret key to access the secondary server. |
| **secondary-server**  string | no description |
| **secret**  any | (list) Pre-shared secret key used to access the primary RADIUS server. |
| **server**  string | Primary RADIUS server CN domain name or IP address. |
| **server-identity-check**  string | Enable/disable RADIUS server identity check  **Choices:**   - `"disable"` - `"enable"` |
| **source-ip**  string | Source IP address for communications to the RADIUS server. |
| **sso-attribute**  string | RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **sso-attribute-key**  string | Key prefix for SSO group value in the SSO attribute. |
| **sso-attribute-value-override**  string | Enable/disable override old attribute value with new value for the same endpoint.  **Choices:**   - `"disable"` - `"enable"` |
| **status-ttl**  integer | Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least … |
| **switch-controller-acct-fast-framedip-detect**  integer | Switch-Controller-Acct-Fast-Framedip-Detect. |
| **switch-controller-service-type**  list / elements=string | Switch-Controller-Service-Type.  **Choices:**   - `"login"` - `"framed"` - `"callback-login"` - `"callback-framed"` - `"outbound"` - `"administrative"` - `"nas-prompt"` - `"authenticate-only"` - `"callback-nas-prompt"` - `"call-check"` - `"callback-administrative"` |
| **tertiary-secret**  any | (list) Secret key to access the tertiary server. |
| **tertiary-server**  string | no description |
| **timeout**  integer | Time in seconds between re-sending authentication requests. |
| **tls-min-proto-version**  string | Minimum supported protocol version for TLS connections  **Choices:**   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1-3"` |
| **transport-protocol**  string | Transport protocol to be used  **Choices:**   - `"udp"` - `"tcp"` - `"tls"` |
| **use-group-for-profile**  string | Use-Group-For-Profile.  **Choices:**   - `"disable"` - `"enable"` |
| **use-management-vdom**  string | Enable/disable using management VDOM to send requests.  **Choices:**   - `"disable"` - `"enable"` |
| **username-case-sensitive**  string | Enable/disable case sensitive user names.  **Choices:**   - `"disable"` - `"enable"` |
| **group-override-attr-type**  string | RADIUS attribute type to override user group information.  **Choices:**   - `"filter-Id"` - `"class"` |
| **h3c-compatibility**  string | Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **mac-case**  string | MAC authentication case  **Choices:**   - `"uppercase"` - `"lowercase"` |
| **mac-password-delimiter**  string | MAC authentication password delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-username-delimiter**  string | MAC authentication username delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **name**  string / required | RADIUS server entry name. |
| **nas-id**  string | Custom NAS identifier. |
| **nas-id-type**  string | NAS identifier type configuration  **Choices:**   - `"legacy"` - `"custom"` - `"hostname"` |
| **nas-ip**  string | IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes. |
| **password-encoding**  string | Password encoding.  **Choices:**   - `"ISO-8859-1"` - `"auto"` |
| **password-renewal**  string | Enable/disable password renewal.  **Choices:**   - `"disable"` - `"enable"` |
| **radius-coa**  string | Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is au…  **Choices:**   - `"disable"` - `"enable"` |
| **radius-port**  integer | RADIUS service port number. |
| **rsso**  string | Enable/disable RADIUS based single sign on feature.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-context-timeout**  integer | Time in seconds before the logged out user is removed from the user context list of logged on users. |
| **rsso-endpoint-attribute**  string | RADIUS attributes used to extract the user end point identifer from the RADIUS Start record.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **rsso-endpoint-block-attribute**  string | RADIUS attributes used to block a user.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **rsso-ep-one-ip-only**  string | Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-flush-ip-session**  string | Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-log-flags**  list / elements=string | Events to log.  **Choices:**   - `"none"` - `"protocol-error"` - `"profile-missing"` - `"context-missing"` - `"accounting-stop-missed"` - `"accounting-event"` - `"radiusd-other"` - `"endpoint-block"` |
| **rsso-log-period**  integer | Time interval in seconds that group event log messages will be generated for dynamic profile events. |
| **rsso-radius-response**  string | Enable/disable sending RADIUS response packets after receiving Start and Stop records.  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-radius-server-port**  integer | UDP port to listen on for RADIUS Start and Stop records. |
| **rsso-secret**  any | (list) RADIUS secret used by the RADIUS accounting server. |
| **rsso-validate-request-secret**  string | Enable/disable validating the RADIUS request shared secret in the Start or End record.  **Choices:**   - `"disable"` - `"enable"` |
| **secondary-secret**  any | (list) Secret key to access the secondary server. |
| **secondary-server**  string | no description |
| **secret**  any | (list) Pre-shared secret key used to access the primary RADIUS server. |
| **server**  string | Primary RADIUS server CN domain name or IP address. |
| **server-identity-check**  string | Enable/disable RADIUS server identity check  **Choices:**   - `"disable"` - `"enable"` |
| **source-ip**  string | Source IP address for communications to the RADIUS server. |
| **sso-attribute**  string | RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **sso-attribute-key**  string | Key prefix for SSO group value in the SSO attribute. |
| **sso-attribute-value-override**  string | Enable/disable override old attribute value with new value for the same endpoint.  **Choices:**   - `"disable"` - `"enable"` |
| **status-ttl**  integer | Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this per… |
| **switch-controller-acct-fast-framedip-detect**  integer | Switch controller accounting message Framed-IP detection from DHCP snooping |
| **switch-controller-service-type**  list / elements=string | RADIUS service type.  **Choices:**   - `"login"` - `"framed"` - `"callback-login"` - `"callback-framed"` - `"outbound"` - `"administrative"` - `"nas-prompt"` - `"authenticate-only"` - `"callback-nas-prompt"` - `"call-check"` - `"callback-administrative"` |
| **tertiary-secret**  any | (list) Secret key to access the tertiary server. |
| **tertiary-server**  string | no description |
| **timeout**  integer | Time in seconds between re-sending authentication requests. |
| **tls-min-proto-version**  string | Minimum supported protocol version for TLS connections  **Choices:**   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1-3"` |
| **transport-protocol**  string | Transport protocol to be used  **Choices:**   - `"udp"` - `"tcp"` - `"tls"` |
| **use-management-vdom**  string | Enable/disable using management VDOM to send requests.  **Choices:**   - `"disable"` - `"enable"` |
| **username-case-sensitive**  string | Enable/disable case sensitive user names.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_radius_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_radius_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the RADIUS server entries
     fmgr_fact:
       facts:
           selector: 'user_radius'
           params:
               adom: 'ansible'
               radius: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure RADIUS server entries.
     fmgr_user_radius:
        bypass_validation: False
        adom: ansible
        state: present
        user_radius:
           name: ansible-test-radius
           server: ansible
           timeout: 200
```

## [Return Values](fmgr_user_radius_module.md#id5)

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
