---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy module – Configure Explicit proxy policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_explicitproxypolicy_module.html
fetched_at: 2026-07-28T02:15:21+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy module – Configure Explicit proxy policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_pkg_firewall_explicitproxypolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_explicitproxypolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_explicitproxypolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_explicitproxypolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_explicitproxypolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_explicitproxypolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_explicitproxypolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_explicitproxypolicy**  dictionary | the top level parameters set |
| **action**  string | Policy action.  **Choices:**   - `"deny"` - `"accept"` |
| **active-auth-method**  string | Active authentication method.  **Choices:**   - `"ntlm"` - `"basic"` - `"digest"` - `"form"` - `"none"` - `"negotiate"` |
| **application-list**  string | Application list. |
| **av-profile**  string | Antivirus profile. |
| **casi-profile**  string | CASI profile. |
| **comments**  string | Comment. |
| **disclaimer**  string | Web proxy disclaimer setting.  **Choices:**   - `"disable"` - `"domain"` - `"policy"` - `"user"` |
| **dlp-sensor**  string | DLP sensor. |
| **dstaddr**  string | Destination address name. |
| **dstaddr-negate**  string | Enable/disable negated destination address match.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr6**  string | IPv6 destination address |
| **dstintf**  string | Destination interface name. |
| **global-label**  string | Label for global view. |
| **icap-profile**  string | ICAP profile. |
| **identity-based**  string | Enable/disable identity-based policy.  **Choices:**   - `"disable"` - `"enable"` |
| **identity-based-policy**  list / elements=dictionary | no description |
| **application-list**  string | Application list. |
| **av-profile**  string | Antivirus profile. |
| **casi-profile**  string | CASI profile. |
| **disclaimer**  string | Web proxy disclaimer setting.  **Choices:**   - `"disable"` - `"domain"` - `"policy"` - `"user"` |
| **dlp-sensor**  string | DLP sensor. |
| **groups**  string | Group name. |
| **icap-profile**  string | ICAP profile. |
| **id**  integer | ID. |
| **ips-sensor**  string | IPS sensor. |
| **logtraffic**  string | Enable/disable policy log traffic.  **Choices:**   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Enable/disable policy log traffic start.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | mms profile |
| **profile-group**  string | profile group |
| **profile-protocol-options**  string | Profile protocol options. |
| **profile-type**  string | profile type  **Choices:**   - `"single"` - `"group"` |
| **replacemsg-override-group**  string | Specify authentication replacement message override group. |
| **scan-botnet-connections**  string | Enable/disable scanning of connections to Botnet servers.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Schedule name. |
| **spamfilter-profile**  string | Spam filter profile. |
| **ssl-ssh-profile**  string | SSL SSH Profile. |
| **users**  string | User name. |
| **utm-status**  string | Enable AV/web/IPS protection profile.  **Choices:**   - `"disable"` - `"enable"` |
| **waf-profile**  string | Web application firewall profile. |
| **webfilter-profile**  string | Web filter profile. |
| **ip-based**  string | Enable/disable IP-based authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sensor**  string | IPS sensor. |
| **label**  string | Label for section view. |
| **logtraffic**  string | Enable/disable policy log traffic.  **Choices:**   - `"disable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Enable/disable policy log traffic start.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | mms profile |
| **policyid**  integer | Policy ID. |
| **profile-group**  string | profile group |
| **profile-protocol-options**  string | Profile protocol options. |
| **profile-type**  string | profile type  **Choices:**   - `"single"` - `"group"` |
| **proxy**  string | Explicit proxy type.  **Choices:**   - `"web"` - `"ftp"` - `"wanopt"` |
| **replacemsg-override-group**  string | Specify authentication replacement message override group. |
| **require-tfa**  string | Enable/disable requirement of 2-factor authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **scan-botnet-connections**  string | Enable/disable scanning of connections to Botnet servers.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Schedule name. |
| **service**  string | Service name. |
| **service-negate**  string | Enable/disable negated service match.  **Choices:**   - `"disable"` - `"enable"` |
| **spamfilter-profile**  string | Spam filter profile. |
| **srcaddr**  string | Source address name. |
| **srcaddr-negate**  string | Enable/disable negated source address match.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr6**  string | IPv6 source address |
| **ssl-ssh-profile**  string | SSL SSH Profile. |
| **sso-auth-method**  string | SSO authentication method.  **Choices:**   - `"fsso"` - `"rsso"` - `"none"` |
| **status**  string | Enable/disable policy status.  **Choices:**   - `"disable"` - `"enable"` |
| **tags**  string | Applied object tags. |
| **transaction-based**  string | Enable/disable transaction based authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **transparent**  string | Use IP address of client to connect to server.  **Choices:**   - `"disable"` - `"enable"` |
| **utm-status**  string | Enable AV/web/IPS protection profile.  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique IDentifier. |
| **waf-profile**  string | Web application firewall profile. |
| **web-auth-cookie**  string | Enable/disable Web authentication cookie.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache**  string | Enable/disable web cache.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache-https**  string | Enable/disable web cache for HTTPS.  **Choices:**   - `"disable"` - `"any"` - `"enable"` |
| **webfilter-profile**  string | Web filter profile. |
| **webproxy-forward-server**  string | Web proxy forward server. |
| **webproxy-profile**  string | Web proxy profile. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_explicitproxypolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_explicitproxypolicy_module.md#id4)

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
    - name: Configure Explicit proxy policies.
      fmgr_pkg_firewall_explicitproxypolicy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_explicitproxypolicy:
          action: <value in [deny, accept]>
          active-auth-method: <value in [ntlm, basic, digest, ...]>
          application-list: <string>
          av-profile: <string>
          casi-profile: <string>
          comments: <string>
          disclaimer: <value in [disable, domain, policy, ...]>
          dlp-sensor: <string>
          dstaddr: <string>
          dstaddr-negate: <value in [disable, enable]>
          dstaddr6: <string>
          dstintf: <string>
          global-label: <string>
          icap-profile: <string>
          identity-based: <value in [disable, enable]>
          identity-based-policy:
            -
              application-list: <string>
              av-profile: <string>
              casi-profile: <string>
              disclaimer: <value in [disable, domain, policy, ...]>
              dlp-sensor: <string>
              groups: <string>
              icap-profile: <string>
              id: <integer>
              ips-sensor: <string>
              logtraffic: <value in [disable, all, utm]>
              logtraffic-start: <value in [disable, enable]>
              mms-profile: <string>
              profile-group: <string>
              profile-protocol-options: <string>
              profile-type: <value in [single, group]>
              replacemsg-override-group: <string>
              scan-botnet-connections: <value in [disable, block, monitor]>
              schedule: <string>
              spamfilter-profile: <string>
              ssl-ssh-profile: <string>
              users: <string>
              utm-status: <value in [disable, enable]>
              waf-profile: <string>
              webfilter-profile: <string>
          ip-based: <value in [disable, enable]>
          ips-sensor: <string>
          label: <string>
          logtraffic: <value in [disable, all, utm]>
          logtraffic-start: <value in [disable, enable]>
          mms-profile: <string>
          policyid: <integer>
          profile-group: <string>
          profile-protocol-options: <string>
          profile-type: <value in [single, group]>
          proxy: <value in [web, ftp, wanopt]>
          replacemsg-override-group: <string>
          require-tfa: <value in [disable, enable]>
          scan-botnet-connections: <value in [disable, block, monitor]>
          schedule: <string>
          service: <string>
          service-negate: <value in [disable, enable]>
          spamfilter-profile: <string>
          srcaddr: <string>
          srcaddr-negate: <value in [disable, enable]>
          srcaddr6: <string>
          ssl-ssh-profile: <string>
          sso-auth-method: <value in [fsso, rsso, none]>
          status: <value in [disable, enable]>
          tags: <string>
          transaction-based: <value in [disable, enable]>
          transparent: <value in [disable, enable]>
          utm-status: <value in [disable, enable]>
          uuid: <string>
          waf-profile: <string>
          web-auth-cookie: <value in [disable, enable]>
          webcache: <value in [disable, enable]>
          webcache-https: <value in [disable, any, enable]>
          webfilter-profile: <string>
          webproxy-forward-server: <string>
          webproxy-profile: <string>
```

## [Return Values](fmgr_pkg_firewall_explicitproxypolicy_module.md#id5)

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
