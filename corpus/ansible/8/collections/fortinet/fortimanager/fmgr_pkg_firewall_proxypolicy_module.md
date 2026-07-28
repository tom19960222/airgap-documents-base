---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_proxypolicy module – Configure proxy policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_proxypolicy_module.html
fetched_at: 2026-07-28T02:15:42+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_proxypolicy module – Configure proxy policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_proxypolicy`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_pkg_firewall_proxypolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_proxypolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_proxypolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_proxypolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_proxypolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_proxypolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_proxypolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_proxypolicy**  dictionary | the top level parameters set |
| **access-proxy**  any | (list or str) Access Proxy. |
| **access-proxy6**  any | (list or str) no description |
| **action**  string | Accept or deny traffic matching the policy parameters.  **Choices:**   - `"accept"` - `"deny"` - `"redirect"` |
| **application-list**  string | Name of an existing Application list. |
| **av-profile**  string | Name of an existing Antivirus profile. |
| **block-notification**  string | Enable/disable block notification.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs-profile**  string | Name of an existing CIFS profile. |
| **comments**  string | Optional comments. |
| **decrypted-traffic-mirror**  string | Decrypted traffic mirror. |
| **device-ownership**  string | When enabled, the ownership enforcement will be done at policy level.  **Choices:**   - `"disable"` - `"enable"` |
| **disclaimer**  string | Web proxy disclaimer setting  **Choices:**   - `"disable"` - `"domain"` - `"policy"` - `"user"` |
| **dlp-profile**  string | Name of an existing DLP profile. |
| **dlp-sensor**  string | Name of an existing DLP sensor. |
| **dstaddr**  any | (list or str) Destination address objects. |
| **dstaddr-negate**  string | When enabled, destination addresses match against any address EXCEPT the specified destination addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr6**  any | (list or str) IPv6 destination address objects. |
| **dstintf**  any | (list or str) Destination interface names. |
| **emailfilter-profile**  string | Name of an existing email filter profile. |
| **file-filter-profile**  string | Name of an existing file-filter profile. |
| **global-label**  string | Global web-based manager visible label. |
| **groups**  any | (list or str) Names of group objects. |
| **http-tunnel-auth**  string | Enable/disable HTTP tunnel authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **icap-profile**  string | Name of an existing ICAP profile. |
| **internet-service**  string | Enable/disable use of Internet Services for this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list or str) Custom Internet Service name. |
| **internet-service-custom-group**  any | (list or str) Custom Internet Service group name. |
| **internet-service-group**  any | (list or str) Internet Service group name. |
| **internet-service-id**  any | (list or str) Internet Service ID. |
| **internet-service-name**  any | (list or str) Internet Service name. |
| **internet-service-negate**  string | When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sensor**  string | Name of an existing IPS sensor. |
| **label**  string | VDOM-specific GUI visible label. |
| **logtraffic**  string | Enable/disable logging traffic through the policy.  **Choices:**   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Enable/disable policy log traffic start.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | Name of an existing MMS profile. |
| **name**  string | Policy name. |
| **policyid**  integer / required | Policy ID. |
| **poolname**  any | (list or str) Name of IP pool object. |
| **profile-group**  string | Name of profile group. |
| **profile-protocol-options**  string | Name of an existing Protocol options profile. |
| **profile-type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **proxy**  string | Type of explicit proxy.  **Choices:**   - `"explicit-web"` - `"transparent-web"` - `"ftp"` - `"wanopt"` - `"ssh"` - `"ssh-tunnel"` - `"access-proxy"` |
| **redirect-url**  string | Redirect URL for further explicit web proxy processing. |
| **replacemsg-override-group**  string | Authentication replacement message override group. |
| **scan-botnet-connections**  string | Enable/disable scanning of connections to Botnet servers.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Name of schedule object. |
| **sctp-filter-profile**  string | Name of an existing SCTP filter profile. |
| **service**  any | (list or str) Name of service objects. |
| **service-negate**  string | When enabled, services match against any service EXCEPT the specified destination services.  **Choices:**   - `"disable"` - `"enable"` |
| **session-ttl**  any | (int or str) TTL in seconds for sessions accepted by this policy |
| **spamfilter-profile**  string | Name of an existing Spam filter profile. |
| **srcaddr**  any | (list or str) Source address objects |
| **srcaddr-negate**  string | When enabled, source addresses match against any address EXCEPT the specified source addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr6**  any | (list or str) IPv6 source address objects. |
| **srcintf**  any | (list or str) Source interface names. |
| **ssh-filter-profile**  string | Name of an existing SSH filter profile. |
| **ssh-policy-redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-ssh-profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable/disable the active status of the policy.  **Choices:**   - `"disable"` - `"enable"` |
| **tags**  string | Names of object-tags applied to address. |
| **transparent**  string | Enable to use the IP address of the client to connect to the server.  **Choices:**   - `"disable"` - `"enable"` |
| **users**  any | (list or str) Names of user objects. |
| **utm-status**  string | Enable the use of UTM profiles/sensors/lists.  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **videofilter-profile**  string | Name of an existing VideoFilter profile. |
| **voip-profile**  string | Name of an existing VoIP profile. |
| **waf-profile**  string | Name of an existing Web application firewall profile. |
| **webcache**  string | Enable/disable web caching.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache-https**  string | Enable/disable web caching for HTTPS  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | Name of an existing Web filter profile. |
| **webproxy-forward-server**  string | Name of web proxy forward server. |
| **webproxy-profile**  string | Name of web proxy profile. |
| **ztna-ems-tag**  any | (list or str) ZTNA EMS Tag names. |
| **ztna-tags-match-logic**  string | ZTNA tag matching logic.  **Choices:**   - `"or"` - `"and"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_proxypolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_proxypolicy_module.md#id4)

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
   - name: Configure proxy policies.
     fmgr_pkg_firewall_proxypolicy:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_proxypolicy:
           action: accept #<value in [accept, deny, redirect]>
           comments: ansible-comment
           dstaddr: all
           dstintf: any
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
   - name: retrieve all the proxy policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_proxypolicy'
           params:
               adom: 'ansible'
               proxy-policy: 'your_value'
               pkg: 'ansible' # package name
```

## [Return Values](fmgr_pkg_firewall_proxypolicy_module.md#id5)

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
