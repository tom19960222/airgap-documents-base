---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_radius_dynamicmapping module – Configure RADIUS server entries."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_radius_dynamicmapping_module.html
fetched_at: 2026-07-28T02:21:13+00:00
---
# fortinet.fortimanager.fmgr_user_radius_dynamicmapping module – Configure RADIUS server entries.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_radius_dynamicmapping`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_user_radius_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_user_radius_dynamicmapping_module.md#parameters)
- [Notes](fmgr_user_radius_dynamicmapping_module.md#notes)
- [Examples](fmgr_user_radius_dynamicmapping_module.md#examples)
- [Return Values](fmgr_user_radius_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_user_radius_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_radius_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **radius**  string / required | the parameter (radius) in requested url |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **user_radius_dynamicmapping**  dictionary | the top level parameters set |
| **_scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **account-key-cert-field**  string | Define subject identity field in certificate for user access right checking.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **account-key-processing**  string | Account key processing operation.  **Choices:**   - `"same"` - `"strip"` |
| **accounting-server**  list / elements=dictionary | no description |
| **id**  integer | no description |
| **interface**  string | no description |
| **interface-select-method**  string | no description  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **port**  integer | no description |
| **secret**  any | (list) no description |
| **server**  string | no description |
| **source-ip**  string | no description |
| **status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **acct-all-servers**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **acct-interim-interval**  integer | no description |
| **all-usergroup**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **auth-type**  string | no description  **Choices:**   - `"pap"` - `"chap"` - `"ms_chap"` - `"ms_chap_v2"` - `"auto"` |
| **ca-cert**  string | CA of server to trust under TLS. |
| **call-station-id-type**  string | Calling & Called station identifier type configuration  **Choices:**   - `"legacy"` - `"IP"` - `"MAC"` |
| **class**  any | (list) no description |
| **client-cert**  string | Client certificate to use under TLS. |
| **delimiter**  string | Configure delimiter to be used for separating profile group names in the SSO attribute  **Choices:**   - `"plus"` - `"comma"` |
| **dp-carrier-endpoint-attribute**  string | no description  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **dp-carrier-endpoint-block-attribute**  string | no description  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **dp-context-timeout**  integer | no description |
| **dp-flush-ip-session**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dp-hold-time**  integer | no description |
| **dp-http-header**  string | no description |
| **dp-http-header-fallback**  string | no description  **Choices:**   - `"ip-header-address"` - `"default-profile"` |
| **dp-http-header-status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dp-http-header-suppress**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dp-log-dyn_flags**  list / elements=string | no description  **Choices:**   - `"none"` - `"protocol-error"` - `"profile-missing"` - `"context-missing"` - `"accounting-stop-missed"` - `"accounting-event"` - `"radiusd-other"` - `"endpoint-block"` |
| **dp-log-period**  integer | no description |
| **dp-mem-percent**  integer | no description |
| **dp-profile-attribute**  string | no description  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **dp-profile-attribute-key**  string | no description |
| **dp-radius-response**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dp-radius-server-port**  integer | no description |
| **dp-secret**  any | (list) no description |
| **dp-validate-request-secret**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic-profile**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **endpoint-translation**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-convert-hex**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-header**  string | no description |
| **ep-carrier-endpoint-header-suppress**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-prefix**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ep-carrier-endpoint-prefix-range-max**  integer | no description |
| **ep-carrier-endpoint-prefix-range-min**  integer | no description |
| **ep-carrier-endpoint-prefix-string**  string | no description |
| **ep-carrier-endpoint-source**  string | no description  **Choices:**   - `"http-header"` - `"cookie"` |
| **ep-ip-header**  string | no description |
| **ep-ip-header-suppress**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ep-missing-header-fallback**  string | no description  **Choices:**   - `"session-ip"` - `"policy-profile"` |
| **ep-profile-query-type**  string | no description  **Choices:**   - `"session-ip"` - `"extract-ip"` - `"extract-carrier-endpoint"` |
| **group-override-attr-type**  string | no description  **Choices:**   - `"filter-Id"` - `"class"` |
| **h3c-compatibility**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **interface**  string | no description |
| **interface-select-method**  string | no description  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **mac-case**  string | MAC authentication case  **Choices:**   - `"uppercase"` - `"lowercase"` |
| **mac-password-delimiter**  string | MAC authentication password delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-username-delimiter**  string | MAC authentication username delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **nas-id**  string | Custom NAS identifier. |
| **nas-id-type**  string | NAS identifier type configuration  **Choices:**   - `"legacy"` - `"custom"` - `"hostname"` |
| **nas-ip**  string | no description |
| **password-encoding**  string | no description  **Choices:**   - `"ISO-8859-1"` - `"auto"` |
| **password-renewal**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **radius-coa**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **radius-port**  integer | no description |
| **rsso**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-context-timeout**  integer | no description |
| **rsso-endpoint-attribute**  string | no description  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **rsso-endpoint-block-attribute**  string | no description  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **rsso-ep-one-ip-only**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-flush-ip-session**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-log-flags**  list / elements=string | no description  **Choices:**   - `"none"` - `"protocol-error"` - `"profile-missing"` - `"context-missing"` - `"accounting-stop-missed"` - `"accounting-event"` - `"radiusd-other"` - `"endpoint-block"` |
| **rsso-log-period**  integer | no description |
| **rsso-radius-response**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **rsso-radius-server-port**  integer | no description |
| **rsso-secret**  any | (list) no description |
| **rsso-validate-request-secret**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **secondary-secret**  any | (list) no description |
| **secondary-server**  string | no description |
| **secret**  any | (list) no description |
| **server**  string | no description |
| **server-identity-check**  string | Enable/disable RADIUS server identity check  **Choices:**   - `"disable"` - `"enable"` |
| **source-ip**  string | no description |
| **sso-attribute**  string | no description  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **sso-attribute-key**  string | no description |
| **sso-attribute-value-override**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **status-ttl**  integer | Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this per… |
| **switch-controller-acct-fast-framedip-detect**  integer | no description |
| **switch-controller-service-type**  list / elements=string | no description  **Choices:**   - `"login"` - `"framed"` - `"callback-login"` - `"callback-framed"` - `"outbound"` - `"administrative"` - `"nas-prompt"` - `"authenticate-only"` - `"callback-nas-prompt"` - `"call-check"` - `"callback-administrative"` |
| **tertiary-secret**  any | (list) no description |
| **tertiary-server**  string | no description |
| **timeout**  integer | no description |
| **tls-min-proto-version**  string | Minimum supported protocol version for TLS connections  **Choices:**   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1-3"` |
| **transport-protocol**  string | Transport protocol to be used  **Choices:**   - `"udp"` - `"tcp"` - `"tls"` |
| **use-group-for-profile**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **use-management-vdom**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **username-case-sensitive**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_radius_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_radius_dynamicmapping_module.md#id4)

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
   - name: Configure dynamic mappings of RADIUS server
     fmgr_user_radius_dynamicmapping:
        bypass_validation: False
        adom: ansible
        radius: ansible-test-radius # name
        state: present
        user_radius_dynamicmapping:
           _scope:
             -
                 name: FGT_AWS # need a valid device name
                 vdom: root # need a valid vdom name under the device
           server: ansible
           timeout: 100

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
   - name: retrieve all the dynamic mappings of RADIUS server
     fmgr_fact:
       facts:
           selector: 'user_radius_dynamicmapping'
           params:
               adom: 'ansible'
               radius: 'ansible-test-radius' # name
               dynamic_mapping: 'your_value'
```

## [Return Values](fmgr_user_radius_dynamicmapping_module.md#id5)

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
