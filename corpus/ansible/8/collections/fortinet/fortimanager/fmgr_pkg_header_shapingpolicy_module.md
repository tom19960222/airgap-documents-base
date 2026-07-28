---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_header_shapingpolicy module – Configure shaping policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_header_shapingpolicy_module.html
fetched_at: 2026-07-28T02:15:51+00:00
---
# fortinet.fortimanager.fmgr_pkg_header_shapingpolicy module – Configure shaping policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_header_shapingpolicy`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_pkg_header_shapingpolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_header_shapingpolicy_module.md#parameters)
- [Notes](fmgr_pkg_header_shapingpolicy_module.md#notes)
- [Examples](fmgr_pkg_header_shapingpolicy_module.md#examples)
- [Return Values](fmgr_pkg_header_shapingpolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_header_shapingpolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_header_shapingpolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_header_shapingpolicy**  dictionary | the top level parameters set |
| **app-category**  any | (list or str) no description |
| **app-group**  any | (list or str) no description |
| **application**  any | (list) no description |
| **class-id**  any | (int or str) no description |
| **class-id-reverse**  integer | no description |
| **comment**  string | no description |
| **cos**  string | VLAN CoS bit pattern. |
| **cos-mask**  string | VLAN CoS evaluated bits. |
| **diffserv-forward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | no description |
| **diffservcode-rev**  string | no description |
| **dstaddr**  any | (list or str) no description |
| **dstaddr6**  any | (list or str) no description |
| **dstintf**  any | (list or str) no description |
| **groups**  any | (list or str) no description |
| **id**  integer / required | no description |
| **internet-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-custom**  any | (list or str) no description |
| **internet-service-custom-group**  any | (list or str) no description |
| **internet-service-group**  any | (list or str) no description |
| **internet-service-id**  any | (list or str) no description |
| **internet-service-name**  any | (list or str) no description |
| **internet-service-src**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **internet-service-src-custom**  any | (list or str) no description |
| **internet-service-src-custom-group**  any | (list or str) no description |
| **internet-service-src-group**  any | (list or str) no description |
| **internet-service-src-id**  any | (list or str) no description |
| **internet-service-src-name**  any | (list or str) no description |
| **ip-version**  string | no description  **Choices:**   - `"4"` - `"6"` |
| **per-ip-shaper**  string | no description |
| **schedule**  string | no description |
| **service**  any | (list or str) no description |
| **service-type**  string | no description  **Choices:**   - `"service"` - `"internet-service"` |
| **srcaddr**  any | (list or str) no description |
| **srcaddr6**  any | (list or str) no description |
| **srcintf**  any | (list or str) no description |
| **status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **tos**  string | no description |
| **tos-mask**  string | no description |
| **tos-negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **traffic-shaper**  string | no description |
| **traffic-shaper-reverse**  string | no description |
| **traffic-type**  string | Traffic type.  **Choices:**   - `"forwarding"` - `"local-in"` - `"local-out"` |
| **url-category**  any | (list or str) no description |
| **users**  any | (list or str) no description |
| **uuid**  string | no description |
| **uuid-idx**  integer | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_header_shapingpolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_header_shapingpolicy_module.md#id4)

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
    - name: Configure shaping policies.
      fmgr_pkg_header_shapingpolicy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        pkg: <your own value>
        state: <value in [present, absent]>
        pkg_header_shapingpolicy:
          app-category: <list or string>
          app-group: <list or string>
          application: <list or integer>
          class-id: <integer or string>
          comment: <string>
          diffserv-forward: <value in [disable, enable]>
          diffserv-reverse: <value in [disable, enable]>
          diffservcode-forward: <string>
          diffservcode-rev: <string>
          dstaddr: <list or string>
          dstaddr6: <list or string>
          dstintf: <list or string>
          groups: <list or string>
          id: <integer>
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
          ip-version: <value in [4, 6]>
          per-ip-shaper: <string>
          schedule: <string>
          service: <list or string>
          srcaddr: <list or string>
          srcaddr6: <list or string>
          srcintf: <list or string>
          status: <value in [disable, enable]>
          tos: <string>
          tos-mask: <string>
          tos-negate: <value in [disable, enable]>
          traffic-shaper: <string>
          traffic-shaper-reverse: <string>
          url-category: <list or string>
          users: <list or string>
          uuid: <string>
          internet-service-name: <list or string>
          internet-service-src-name: <list or string>
          class-id-reverse: <integer>
          service-type: <value in [service, internet-service]>
          uuid-idx: <integer>
          cos: <string>
          cos-mask: <string>
          traffic-type: <value in [forwarding, local-in, local-out]>
```

## [Return Values](fmgr_pkg_header_shapingpolicy_module.md#id5)

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
