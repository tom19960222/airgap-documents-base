---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy module – Configure consolidated IPv4/IPv6 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_consolidated_policy_module.html
fetched_at: 2026-07-28T02:15:15+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy module – Configure consolidated IPv4/IPv6 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_pkg_firewall_consolidated_policy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_consolidated_policy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_consolidated_policy_module.md#notes)
- [Examples](fmgr_pkg_firewall_consolidated_policy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_consolidated_policy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_consolidated_policy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_consolidated_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_consolidated_policy**  dictionary | the top level parameters set |
| **_policy_block**  integer | Assigned policy block. |
| **action**  string | Policy action  **Choices:**   - `"deny"` - `"accept"` - `"ipsec"` |
| **app-category**  any | (list or str) Application category ID list. |
| **app-group**  any | (list or str) Application group names. |
| **application**  any | (list) Application. |
| **application-list**  string | Name of an existing Application list. |
| **auto-asic-offload**  string | Enable/disable offloading security profile processing to CP processors.  **Choices:**   - `"disable"` - `"enable"` |
| **av-profile**  string | Name of an existing Antivirus profile. |
| **captive-portal-exempt**  string | Enable exemption of some users from the captive portal.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs-profile**  string | Name of an existing CIFS profile. |
| **comments**  string | Comment. |
| **diffserv-forward**  string | Enable to change packets DiffServ values to the specified diffservcode-forward value.  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | Enable to change packets reverse  **Choices:**   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | Change packets DiffServ to this value. |
| **diffservcode-rev**  string | Change packets reverse |
| **dlp-sensor**  string | Name of an existing DLP sensor. |
| **dnsfilter-profile**  string | Name of an existing DNS filter profile. |
| **dstaddr-negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr4**  any | (list or str) Destination IPv4 address name and address group names. |
| **dstaddr6**  any | (list or str) Destination IPv6 address name and address group names. |
| **dstintf**  any | (list or str) Outgoing |
| **emailfilter-profile**  string | Name of an existing email filter profile. |
| **fixedport**  string | Enable to prevent source NAT from changing a sessions source port.  **Choices:**   - `"disable"` - `"enable"` |
| **fsso-groups**  any | (list or str) Names of FSSO groups. |
| **global-label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  any | (list or str) Names of user groups that can authenticate with this policy. |
| **http-policy-redirect**  string | Redirect HTTP  **Choices:**   - `"disable"` - `"enable"` |
| **icap-profile**  string | Name of an existing ICAP profile. |
| **inbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | Policy inspection mode  **Choices:**   - `"proxy"` - `"flow"` |
| **internet-service**  string | Enable/disable use of Internet Services for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list or str) Custom Internet Service name. |
| **internet-service-custom-group**  any | (list or str) Custom Internet Service group name. |
| **internet-service-group**  any | (list or str) Internet Service group name. |
| **internet-service-id**  any | (list or str) Internet Service ID. |
| **internet-service-negate**  string | When enabled internet-service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src**  string | Enable/disable use of Internet Services in source for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  any | (list or str) Custom Internet Service source name. |
| **internet-service-src-custom-group**  any | (list or str) Custom Internet Service source group name. |
| **internet-service-src-group**  any | (list or str) Internet Service source group name. |
| **internet-service-src-id**  any | (list or str) Internet Service source ID. |
| **internet-service-src-negate**  string | When enabled internet-service-src specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **ippool**  string | Enable to use IP Pools for source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sensor**  string | Name of an existing IPS sensor. |
| **logtraffic**  string | Enable or disable logging.  **Choices:**   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Record logs when a session starts.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | Name of an existing MMS profile. |
| **name**  string / required | Policy name. |
| **nat**  string | Enable/disable source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **outbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **per-ip-shaper**  string | Per-IP traffic shaper. |
| **policyid**  integer | Policy ID |
| **poolname4**  any | (list or str) IPv4 pool names. |
| **poolname6**  any | (list or str) IPv6 pool names. |
| **profile-group**  string | Name of profile group. |
| **profile-protocol-options**  string | Name of an existing Protocol options profile. |
| **profile-type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **schedule**  string | Schedule name. |
| **service**  any | (list or str) Service and service group names. |
| **service-negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **session-ttl**  integer | TTL in seconds for sessions accepted by this policy |
| **srcaddr-negate**  string | When enabled srcaddr specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr4**  any | (list or str) Source IPv4 address name and address group names. |
| **srcaddr6**  any | (list or str) Source IPv6 address name and address group names. |
| **srcintf**  any | (list or str) Incoming |
| **ssh-filter-profile**  string | Name of an existing SSH filter profile. |
| **ssh-policy-redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-ssh-profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-mss-receiver**  integer | Receiver TCP maximum segment size |
| **tcp-mss-sender**  integer | Sender TCP maximum segment size |
| **traffic-shaper**  string | Traffic shaper. |
| **traffic-shaper-reverse**  string | Reverse traffic shaper. |
| **url-category**  any | (list or str) URL category ID list. |
| **users**  any | (list or str) Names of individual users that can authenticate with this policy. |
| **utm-status**  string | Enable to add one or more security profiles  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **voip-profile**  string | Name of an existing VoIP profile. |
| **vpntunnel**  string | Policy-based IPsec VPN |
| **waf-profile**  string | Name of an existing Web application firewall profile. |
| **wanopt**  string | Enable/disable WAN optimization.  **Choices:**   - `"disable"` - `"enable"` |
| **wanopt-detection**  string | WAN optimization auto-detection mode.  **Choices:**   - `"active"` - `"passive"` - `"off"` |
| **wanopt-passive-opt**  string | WAN optimization passive mode options.  **Choices:**   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt-peer**  string | WAN optimization peer. |
| **wanopt-profile**  string | WAN optimization profile. |
| **webcache**  string | Enable/disable web cache.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache-https**  string | Enable/disable web cache for HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | Name of an existing Web filter profile. |
| **webproxy-forward-server**  string | Webproxy forward server name. |
| **webproxy-profile**  string | Webproxy profile name. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_consolidated_policy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_consolidated_policy_module.md#id4)

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
    - name: Configure consolidated IPv4/IPv6 policies.
      fmgr_pkg_firewall_consolidated_policy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_consolidated_policy:
          action: <value in [deny, accept, ipsec]>
          app-category: <list or string>
          app-group: <list or string>
          application: <list or integer>
          application-list: <string>
          auto-asic-offload: <value in [disable, enable]>
          av-profile: <string>
          cifs-profile: <string>
          comments: <string>
          diffserv-forward: <value in [disable, enable]>
          diffserv-reverse: <value in [disable, enable]>
          diffservcode-forward: <string>
          diffservcode-rev: <string>
          dlp-sensor: <string>
          dnsfilter-profile: <string>
          dstaddr4: <list or string>
          dstaddr6: <list or string>
          dstintf: <list or string>
          emailfilter-profile: <string>
          fixedport: <value in [disable, enable]>
          groups: <list or string>
          http-policy-redirect: <value in [disable, enable]>
          icap-profile: <string>
          inbound: <value in [disable, enable]>
          inspection-mode: <value in [proxy, flow]>
          internet-service: <value in [disable, enable]>
          internet-service-custom: <list or string>
          internet-service-custom-group: <list or string>
          internet-service-group: <list or string>
          internet-service-id: <list or string>
          internet-service-src: <value in [disable, enable]>
          internet-service-src-custom: <list or string>
          internet-service-src-custom-group: <list or string>
          internet-service-src-group: <list or string>
          internet-service-src-id: <list or string>
          ippool: <value in [disable, enable]>
          ips-sensor: <string>
          logtraffic: <value in [disable, all, utm]>
          logtraffic-start: <value in [disable, enable]>
          mms-profile: <string>
          name: <string>
          nat: <value in [disable, enable]>
          outbound: <value in [disable, enable]>
          per-ip-shaper: <string>
          policyid: <integer>
          poolname4: <list or string>
          poolname6: <list or string>
          profile-group: <string>
          profile-protocol-options: <string>
          profile-type: <value in [single, group]>
          schedule: <string>
          service: <list or string>
          session-ttl: <integer>
          srcaddr4: <list or string>
          srcaddr6: <list or string>
          srcintf: <list or string>
          ssh-filter-profile: <string>
          ssh-policy-redirect: <value in [disable, enable]>
          ssl-ssh-profile: <string>
          status: <value in [disable, enable]>
          tcp-mss-receiver: <integer>
          tcp-mss-sender: <integer>
          traffic-shaper: <string>
          traffic-shaper-reverse: <string>
          url-category: <list or string>
          users: <list or string>
          utm-status: <value in [disable, enable]>
          uuid: <string>
          voip-profile: <string>
          vpntunnel: <string>
          waf-profile: <string>
          wanopt: <value in [disable, enable]>
          wanopt-detection: <value in [active, passive, off]>
          wanopt-passive-opt: <value in [default, transparent, non-transparent]>
          wanopt-peer: <string>
          wanopt-profile: <string>
          webcache: <value in [disable, enable]>
          webcache-https: <value in [disable, enable]>
          webfilter-profile: <string>
          webproxy-forward-server: <string>
          webproxy-profile: <string>
          captive-portal-exempt: <value in [disable, enable]>
          dstaddr-negate: <value in [disable, enable]>
          fsso-groups: <list or string>
          global-label: <string>
          internet-service-negate: <value in [disable, enable]>
          internet-service-src-negate: <value in [disable, enable]>
          service-negate: <value in [disable, enable]>
          srcaddr-negate: <value in [disable, enable]>
          _policy_block: <integer>
```

## [Return Values](fmgr_pkg_firewall_consolidated_policy_module.md#id5)

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
