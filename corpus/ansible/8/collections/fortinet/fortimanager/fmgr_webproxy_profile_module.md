---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_webproxy_profile module – Configure web proxy profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_webproxy_profile_module.html
fetched_at: 2026-07-28T02:22:57+00:00
---
# fortinet.fortimanager.fmgr_webproxy_profile module – Configure web proxy profiles.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_webproxy_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_webproxy_profile_module.md#synopsis)
- [Parameters](fmgr_webproxy_profile_module.md#parameters)
- [Notes](fmgr_webproxy_profile_module.md#notes)
- [Examples](fmgr_webproxy_profile_module.md#examples)
- [Return Values](fmgr_webproxy_profile_module.md#return-values)

## [Synopsis](fmgr_webproxy_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_webproxy_profile_module.md#id2)

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
| **webproxy_profile**  dictionary | the top level parameters set |
| **header-client-ip**  string | Action to take on the HTTP client-IP header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-front-end-https**  string | Action to take on the HTTP front-end-HTTPS header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-via-request**  string | Action to take on the HTTP via header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-via-response**  string | Action to take on the HTTP via header in forwarded responses  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-x-authenticated-groups**  string | Action to take on the HTTP x-authenticated-groups header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-x-authenticated-user**  string | Action to take on the HTTP x-authenticated-user header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-x-forwarded-client-cert**  string | Action to take on the HTTP x-forwarded-client-cert header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **header-x-forwarded-for**  string | Action to take on the HTTP x-forwarded-for header in forwarded requests  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **headers**  list / elements=dictionary | Headers. |
| **action**  string | Action when HTTP the header forwarded.  **Choices:**   - `"add-to-request"` - `"add-to-response"` - `"remove-from-request"` - `"remove-from-response"` - `"monitor-request"` - `"monitor-response"` |
| **add-option**  string | Configure options to append content to existing HTTP header or add new HTTP header.  **Choices:**   - `"append"` - `"new-on-not-found"` - `"new"` |
| **base64-encoding**  string | Enable/disable use of base64 encoding of HTTP content.  **Choices:**   - `"disable"` - `"enable"` |
| **content**  string | HTTP headers content. |
| **dstaddr**  any | (list or str) Destination address and address group names. |
| **dstaddr6**  any | (list or str) Destination address and address group names |
| **id**  integer | HTTP forwarded header id. |
| **name**  string | HTTP forwarded header name. |
| **protocol**  list / elements=string | Configure protocol  **Choices:**   - `"https"` - `"http"` |
| **log-header-change**  string | Enable/disable logging HTTP header changes.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Profile name. |
| **strip-encoding**  string | Enable/disable stripping unsupported encoding from the request header.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_webproxy_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_webproxy_profile_module.md#id4)

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
    - name: Configure web proxy profiles.
      fmgr_webproxy_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        webproxy_profile:
          header-client-ip: <value in [pass, add, remove]>
          header-front-end-https: <value in [pass, add, remove]>
          header-via-request: <value in [pass, add, remove]>
          header-via-response: <value in [pass, add, remove]>
          header-x-authenticated-groups: <value in [pass, add, remove]>
          header-x-authenticated-user: <value in [pass, add, remove]>
          header-x-forwarded-for: <value in [pass, add, remove]>
          headers:
            -
              action: <value in [add-to-request, add-to-response, remove-from-request, ...]>
              content: <string>
              id: <integer>
              name: <string>
              add-option: <value in [append, new-on-not-found, new]>
              base64-encoding: <value in [disable, enable]>
              dstaddr: <list or string>
              dstaddr6: <list or string>
              protocol:
                - https
                - http
          log-header-change: <value in [disable, enable]>
          name: <string>
          strip-encoding: <value in [disable, enable]>
          header-x-forwarded-client-cert: <value in [pass, add, remove]>
```

## [Return Values](fmgr_webproxy_profile_module.md#id5)

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
