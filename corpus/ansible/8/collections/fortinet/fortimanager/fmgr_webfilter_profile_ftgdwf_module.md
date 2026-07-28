---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_webfilter_profile_ftgdwf module – FortiGuard Web Filter settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_webfilter_profile_ftgdwf_module.html
fetched_at: 2026-07-28T02:22:48+00:00
---
# fortinet.fortimanager.fmgr_webfilter_profile_ftgdwf module – FortiGuard Web Filter settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_webfilter_profile_ftgdwf`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_webfilter_profile_ftgdwf_module.md#synopsis)
- [Parameters](fmgr_webfilter_profile_ftgdwf_module.md#parameters)
- [Notes](fmgr_webfilter_profile_ftgdwf_module.md#notes)
- [Examples](fmgr_webfilter_profile_ftgdwf_module.md#examples)
- [Return Values](fmgr_webfilter_profile_ftgdwf_module.md#return-values)

## [Synopsis](fmgr_webfilter_profile_ftgdwf_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_webfilter_profile_ftgdwf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **profile**  string / required | the parameter (profile) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **webfilter_profile_ftgdwf**  dictionary | the top level parameters set |
| **category-override**  string | Local categories take precedence over FortiGuard categories. |
| **exempt-quota**  any | (list or str) Do not stop quota for these categories. |
| **filters**  list / elements=dictionary | no description |
| **action**  string | Action to take for matches.  **Choices:**   - `"block"` - `"monitor"` - `"warning"` - `"authenticate"` |
| **auth-usr-grp**  any | (list or str) Groups with permission to authenticate. |
| **category**  string | Categories and groups the filter examines. |
| **id**  integer | ID number. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **override-replacemsg**  string | Override replacement message. |
| **warn-duration**  string | Duration of warnings. |
| **warning-duration-type**  string | Re-display warning after closing browser or after a timeout.  **Choices:**   - `"session"` - `"timeout"` |
| **warning-prompt**  string | Warning prompts in each category or each domain.  **Choices:**   - `"per-domain"` - `"per-category"` |
| **max-quota-timeout**  integer | Maximum FortiGuard quota used by single page view in seconds |
| **options**  list / elements=string | no description  **Choices:**   - `"error-allow"` - `"http-err-detail"` - `"rate-image-urls"` - `"strict-blocking"` - `"rate-server-ip"` - `"redir-block"` - `"connect-request-bypass"` - `"log-all-url"` - `"ftgd-disable"` |
| **ovrd**  any | (list or str) Allow web filter profile overrides. |
| **quota**  list / elements=dictionary | no description |
| **category**  any | (list or str) FortiGuard categories to apply quota to |
| **duration**  string | Duration of quota. |
| **id**  integer | ID number. |
| **override-replacemsg**  string | Override replacement message. |
| **type**  string | Quota type.  **Choices:**   - `"time"` - `"traffic"` |
| **unit**  string | Traffic quota unit of measurement.  **Choices:**   - `"B"` - `"KB"` - `"MB"` - `"GB"` |
| **value**  integer | Traffic quota value. |
| **rate-crl-urls**  string | Enable/disable rating CRL by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-css-urls**  string | Enable/disable rating CSS by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-image-urls**  string | Enable/disable rating images by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-javascript-urls**  string | Enable/disable rating JavaScript by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_webfilter_profile_ftgdwf_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_webfilter_profile_ftgdwf_module.md#id4)

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
    - name: FortiGuard Web Filter settings.
      fmgr_webfilter_profile_ftgdwf:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        profile: <your own value>
        webfilter_profile_ftgdwf:
          exempt-quota: <list or string>
          filters:
            -
              action: <value in [block, monitor, warning, ...]>
              auth-usr-grp: <list or string>
              category: <string>
              id: <integer>
              log: <value in [disable, enable]>
              override-replacemsg: <string>
              warn-duration: <string>
              warning-duration-type: <value in [session, timeout]>
              warning-prompt: <value in [per-domain, per-category]>
          max-quota-timeout: <integer>
          options:
            - error-allow
            - http-err-detail
            - rate-image-urls
            - strict-blocking
            - rate-server-ip
            - redir-block
            - connect-request-bypass
            - log-all-url
            - ftgd-disable
          ovrd: <list or string>
          quota:
            -
              category: <list or string>
              duration: <string>
              id: <integer>
              override-replacemsg: <string>
              type: <value in [time, traffic]>
              unit: <value in [B, KB, MB, ...]>
              value: <integer>
          rate-crl-urls: <value in [disable, enable]>
          rate-css-urls: <value in [disable, enable]>
          rate-image-urls: <value in [disable, enable]>
          rate-javascript-urls: <value in [disable, enable]>
          category-override: <string>
```

## [Return Values](fmgr_webfilter_profile_ftgdwf_module.md#id5)

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
