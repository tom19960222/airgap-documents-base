---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy module – Identity-based policy."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.html
fetched_at: 2026-07-28T02:15:22+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy module – Identity-based policy.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **explicit-proxy-policy**  string / required | the parameter (explicit-proxy-policy) in requested url |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_explicitproxypolicy_identitybasedpolicy**  dictionary | the top level parameters set |
| **application-list**  string | Application list. |
| **av-profile**  string | Antivirus profile. |
| **casi-profile**  string | CASI profile. |
| **disclaimer**  string | Web proxy disclaimer setting.  **Choices:**   - `"disable"` - `"domain"` - `"policy"` - `"user"` |
| **dlp-sensor**  string | DLP sensor. |
| **groups**  string | Group name. |
| **icap-profile**  string | ICAP profile. |
| **id**  integer / required | ID. |
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
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#id4)

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
    - name: Identity-based policy.
      fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        explicit-proxy-policy: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_explicitproxypolicy_identitybasedpolicy:
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
```

## [Return Values](fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy_module.md#id5)

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
