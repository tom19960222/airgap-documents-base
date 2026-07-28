---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dnsfilter_profile module – Configure DNS domain filter profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dnsfilter_profile_module.html
fetched_at: 2026-07-28T02:09:23+00:00
---
# fortinet.fortimanager.fmgr_dnsfilter_profile module – Configure DNS domain filter profiles.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dnsfilter_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dnsfilter_profile_module.md#synopsis)
- [Parameters](fmgr_dnsfilter_profile_module.md#parameters)
- [Notes](fmgr_dnsfilter_profile_module.md#notes)
- [Examples](fmgr_dnsfilter_profile_module.md#examples)
- [Return Values](fmgr_dnsfilter_profile_module.md#return-values)

## [Synopsis](fmgr_dnsfilter_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dnsfilter_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dnsfilter_profile**  dictionary | the top level parameters set |
| **block-action**  string | Action to take for blocked domains.  **Choices:**   - `"block"` - `"redirect"` - `"block-sevrfail"` |
| **block-botnet**  string | Enable/disable blocking botnet C&C DNS lookups.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **dns-translation**  list / elements=dictionary | Dns-Translation. |
| **addr-type**  string | DNS translation type  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **dst**  string | IPv4 address or subnet on the external network to substitute for the resolved address in DNS query replies. |
| **dst6**  string | IPv6 address or subnet on the external network to substitute for the resolved address in DNS query replies. |
| **id**  integer | ID. |
| **netmask**  string | If src and dst are subnets rather than single IP addresses, enter the netmask for both src and dst. |
| **prefix**  integer | If src6 and dst6 are subnets rather than single IP addresses, enter the prefix for both src6 and dst6 |
| **src**  string | IPv4 address or subnet on the internal network to compare with the resolved address in DNS query replies. |
| **src6**  string | IPv6 address or subnet on the internal network to compare with the resolved address in DNS query replies. |
| **status**  string | Enable/disable this DNS translation entry.  **Choices:**   - `"disable"` - `"enable"` |
| **domain-filter**  dictionary | no description |
| **domain-filter-table**  integer | DNS domain filter table ID. |
| **external-ip-blocklist**  any | (list or str) One or more external IP block lists. |
| **ftgd-dns**  dictionary | no description |
| **filters**  list / elements=dictionary | Filters. |
| **action**  string | Action to take for DNS requests matching the category.  **Choices:**   - `"monitor"` - `"block"` |
| **category**  string | Category number. |
| **id**  integer | ID number. |
| **log**  string | Enable/disable DNS filter logging for this DNS profile.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | FortiGuard DNS filter options.  **Choices:**   - `"error-allow"` - `"ftgd-disable"` |
| **log-all-domain**  string | Enable/disable logging of all domains visited  **Choices:**   - `"disable"` - `"enable"` |
| **log-all-url**  string | Enable/disable log all URLs visited.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Profile name. |
| **redirect-portal**  string | IP address of the SDNS redirect portal. |
| **redirect-portal6**  string | IPv6 address of the SDNS redirect portal. |
| **safe-search**  string | Enable/disable Google, Bing, and YouTube safe search.  **Choices:**   - `"disable"` - `"enable"` |
| **sdns-domain-log**  string | Enable/disable domain filtering and botnet domain logging.  **Choices:**   - `"disable"` - `"enable"` |
| **sdns-ftgd-err-log**  string | Enable/disable FortiGuard SDNS rating error logging.  **Choices:**   - `"disable"` - `"enable"` |
| **sdns-url-log**  string | Enable/disable logging of URL filtering and botnet domains.  **Choices:**   - `"disable"` - `"enable"` |
| **transparent-dns-database**  any | (list) no description |
| **urlfilter**  dictionary | no description |
| **urlfilter-table**  integer | DNS URL filter table ID. |
| **youtube-restrict**  string | Set safe search for YouTube restriction level.  **Choices:**   - `"strict"` - `"moderate"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dnsfilter_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dnsfilter_profile_module.md#id4)

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
   - name: Configure DNS domain filter profiles.
     fmgr_dnsfilter_profile:
        bypass_validation: False
        adom: ansible
        state: present
        dnsfilter_profile:
           block-action: redirect
           block-botnet: disable
           comment: 'ansible-test-comment'
           log-all-domain: disable
           name: 'ansible-test'

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
   - name: retrieve all the profiles
     fmgr_fact:
       facts:
           selector: 'dnsfilter_profile'
           params:
               adom: 'ansible'
               profile: 'your_value'
```

## [Return Values](fmgr_dnsfilter_profile_module.md#id5)

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
