---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_securitypolicy module – Configure NGFW IPv4/IPv6 application policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_securitypolicy_module.html
fetched_at: 2026-07-28T02:15:44+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_securitypolicy module – Configure NGFW IPv4/IPv6 application policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_securitypolicy`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_pkg_firewall_securitypolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_securitypolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_securitypolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_securitypolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_securitypolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_securitypolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_securitypolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_securitypolicy**  dictionary | the top level parameters set |
| **_policy_block**  integer | Assigned policy block. |
| **action**  string | Policy action  **Choices:**   - `"deny"` - `"accept"` |
| **app-category**  any | (list or str) Application category ID list. |
| **app-group**  any | (list or str) Application group names. |
| **application**  any | (list) Application ID list. |
| **application-list**  string | Name of an existing Application list. |
| **av-profile**  string | Name of an existing Antivirus profile. |
| **cifs-profile**  string | Name of an existing CIFS profile. |
| **comments**  string | Comment. |
| **dlp-profile**  string | Name of an existing DLP profile. |
| **dlp-sensor**  string | Name of an existing DLP sensor. |
| **dnsfilter-profile**  string | Name of an existing DNS filter profile. |
| **dstaddr**  any | (list or str) Destination IPv4 address name and address group names. |
| **dstaddr-negate**  string | When enabled dstaddr/dstaddr6 specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr4**  any | (list or str) Destination IPv4 address name and address group names. |
| **dstaddr6**  any | (list or str) Destination IPv6 address name and address group names. |
| **dstintf**  any | (list or str) Outgoing |
| **emailfilter-profile**  string | Name of an existing email filter profile. |
| **enforce-default-app-port**  string | Enable/disable default application port enforcement for allowed applications.  **Choices:**   - `"disable"` - `"enable"` |
| **file-filter-profile**  string | Name of an existing file-filter profile. |
| **fsso-groups**  any | (list or str) Names of FSSO groups. |
| **global-label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  any | (list or str) Names of user groups that can authenticate with this policy. |
| **icap-profile**  string | Name of an existing ICAP profile. |
| **internet-service**  string | Enable/disable use of Internet Services for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list or str) Custom Internet Service name. |
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
| **ips-sensor**  string | Name of an existing IPS sensor. |
| **learning-mode**  string | Enable to allow everything, but log all of the meaningful data for security information gathering.  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic**  string | Enable or disable logging.  **Choices:**   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Record logs when a session starts.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | Name of an existing MMS profile. |
| **name**  string / required | Policy name. |
| **nat46**  string | Enable/disable NAT46.  **Choices:**   - `"disable"` - `"enable"` |
| **nat64**  string | Enable/disable NAT64.  **Choices:**   - `"disable"` - `"enable"` |
| **policyid**  integer | Policy ID. |
| **profile-group**  string | Name of profile group. |
| **profile-protocol-options**  string | Name of an existing Protocol options profile. |
| **profile-type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **schedule**  string | Schedule name. |
| **sctp-filter-profile**  string | Name of an existing SCTP filter profile. |
| **send-deny-packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  **Choices:**   - `"disable"` - `"enable"` |
| **service**  any | (list or str) Service and service group names. |
| **service-negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr**  any | (list or str) Source IPv4 address name and address group names. |
| **srcaddr-negate**  string | When enabled srcaddr/srcaddr6 specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr4**  any | (list or str) Source IPv4 address name and address group names. |
| **srcaddr6**  any | (list or str) Source IPv6 address name and address group names. |
| **srcintf**  any | (list or str) Incoming |
| **ssh-filter-profile**  string | Name of an existing SSH filter profile. |
| **ssl-ssh-profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **url-category**  any | (list or str) URL category ID list. |
| **users**  any | (list or str) Names of individual users that can authenticate with this policy. |
| **utm-status**  string | Enable security profiles.  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **videofilter-profile**  string | Name of an existing VideoFilter profile. |
| **voip-profile**  string | Name of an existing VoIP profile. |
| **webfilter-profile**  string | Name of an existing Web filter profile. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_securitypolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_securitypolicy_module.md#id4)

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
    - name: Configure NGFW IPv4/IPv6 application policies.
      fmgr_pkg_firewall_securitypolicy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_securitypolicy:
          action: <value in [deny, accept]>
          app-category: <list or string>
          app-group: <list or string>
          application: <list or integer>
          application-list: <string>
          av-profile: <string>
          cifs-profile: <string>
          comments: <string>
          dlp-sensor: <string>
          dnsfilter-profile: <string>
          dstaddr4: <list or string>
          dstaddr6: <list or string>
          dstintf: <list or string>
          emailfilter-profile: <string>
          enforce-default-app-port: <value in [disable, enable]>
          groups: <list or string>
          icap-profile: <string>
          internet-service: <value in [disable, enable]>
          internet-service-custom: <list or string>
          internet-service-custom-group: <list or string>
          internet-service-group: <list or string>
          internet-service-id: <list or string>
          internet-service-negate: <value in [disable, enable]>
          internet-service-src: <value in [disable, enable]>
          internet-service-src-custom: <list or string>
          internet-service-src-custom-group: <list or string>
          internet-service-src-group: <list or string>
          internet-service-src-id: <list or string>
          internet-service-src-negate: <value in [disable, enable]>
          ips-sensor: <string>
          logtraffic: <value in [disable, all, utm]>
          logtraffic-start: <value in [disable, enable]>
          mms-profile: <string>
          name: <string>
          policyid: <integer>
          profile-group: <string>
          profile-protocol-options: <string>
          profile-type: <value in [single, group]>
          schedule: <string>
          service: <list or string>
          service-negate: <value in [disable, enable]>
          srcaddr4: <list or string>
          srcaddr6: <list or string>
          srcintf: <list or string>
          ssh-filter-profile: <string>
          ssl-ssh-profile: <string>
          status: <value in [disable, enable]>
          url-category: <list or string>
          users: <list or string>
          utm-status: <value in [disable, enable]>
          uuid: <string>
          voip-profile: <string>
          webfilter-profile: <string>
          fsso-groups: <list or string>
          global-label: <string>
          send-deny-packet: <value in [disable, enable]>
          dstaddr: <list or string>
          internet-service-name: <list or string>
          internet-service-src-name: <list or string>
          srcaddr: <list or string>
          dstaddr-negate: <value in [disable, enable]>
          file-filter-profile: <string>
          srcaddr-negate: <value in [disable, enable]>
          learning-mode: <value in [disable, enable]>
          videofilter-profile: <string>
          _policy_block: <integer>
          dlp-profile: <string>
          nat46: <value in [disable, enable]>
          nat64: <value in [disable, enable]>
          sctp-filter-profile: <string>
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
```

## [Return Values](fmgr_pkg_firewall_securitypolicy_module.md#id5)

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
