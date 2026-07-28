---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_icap_profile module – Configure ICAP profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_icap_profile_module.html
fetched_at: 2026-07-28T02:14:47+00:00
---
# fortinet.fortimanager.fmgr_icap_profile module – Configure ICAP profiles.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_icap_profile`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_icap_profile_module.md#synopsis)
- [Parameters](fmgr_icap_profile_module.md#parameters)
- [Notes](fmgr_icap_profile_module.md#notes)
- [Examples](fmgr_icap_profile_module.md#examples)
- [Return Values](fmgr_icap_profile_module.md#return-values)

## [Synopsis](fmgr_icap_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_icap_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **icap_profile**  dictionary | the top level parameters set |
| **204-response**  string | Enable/disable allowance of 204 response from ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **204-size-limit**  integer | 204 response size limit to be saved by ICAP client in megabytes |
| **chunk-encap**  string | Enable/disable chunked encapsulation  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **extension-feature**  list / elements=string | no description  **Choices:**   - `"scan-progress"` |
| **file-transfer**  list / elements=string | no description  **Choices:**   - `"ssh"` - `"ftp"` |
| **file-transfer-failure**  string | Action to take if the ICAP server cannot be contacted when processing a file transfer.  **Choices:**   - `"error"` - `"bypass"` |
| **file-transfer-path**  string | Path component of the ICAP URI that identifies the file transfer processing service. |
| **file-transfer-server**  string | ICAP server to use for a file transfer. |
| **icap-block-log**  string | Enable/disable UTM log when infection found  **Choices:**   - `"disable"` - `"enable"` |
| **icap-headers**  list / elements=dictionary | Icap-Headers. |
| **base64-encoding**  string | Enable/disable use of base64 encoding of HTTP content.  **Choices:**   - `"disable"` - `"enable"` |
| **content**  string | HTTP header content. |
| **id**  integer | HTTP forwarded header ID. |
| **name**  string | HTTP forwarded header name. |
| **methods**  list / elements=string | The allowed HTTP methods that will be sent to ICAP server for further processing.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"other"` - `"connect"` |
| **name**  string / required | ICAP profile name. |
| **preview**  string | Enable/disable preview of data to ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **preview-data-length**  integer | Preview data length to be sent to ICAP server. |
| **replacemsg-group**  string | Replacement message group. |
| **request**  string | Enable/disable whether an HTTP request is passed to an ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **request-failure**  string | Action to take if the ICAP server cannot be contacted when processing an HTTP request.  **Choices:**   - `"error"` - `"bypass"` |
| **request-path**  string | Path component of the ICAP URI that identifies the HTTP request processing service. |
| **request-server**  string | ICAP server to use for an HTTP request. |
| **respmod-default-action**  string | Default action to ICAP response modification  **Choices:**   - `"bypass"` - `"forward"` |
| **respmod-forward-rules**  list / elements=dictionary | Respmod-Forward-Rules. |
| **action**  string | Action to be taken for ICAP server.  **Choices:**   - `"bypass"` - `"forward"` |
| **header-group**  list / elements=dictionary | Header-Group. |
| **case-sensitivity**  string | Enable/disable case sensitivity when matching header.  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | HTTP header regular expression. |
| **header-name**  string | HTTP header. |
| **id**  integer | ID. |
| **host**  string | Address object for the host. |
| **http-resp-status-code**  any | (list) HTTP response status code. |
| **name**  string | Address name. |
| **response**  string | Enable/disable whether an HTTP response is passed to an ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **response-failure**  string | Action to take if the ICAP server cannot be contacted when processing an HTTP response.  **Choices:**   - `"error"` - `"bypass"` |
| **response-path**  string | Path component of the ICAP URI that identifies the HTTP response processing service. |
| **response-req-hdr**  string | Enable/disable addition of req-hdr for ICAP response modification  **Choices:**   - `"disable"` - `"enable"` |
| **response-server**  string | ICAP server to use for an HTTP response. |
| **scan-progress-interval**  integer | Scan progress interval value. |
| **streaming-content-bypass**  string | Enable/disable bypassing of ICAP server for streaming content.  **Choices:**   - `"disable"` - `"enable"` |
| **timeout**  integer | Time |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_icap_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_icap_profile_module.md#id4)

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
    - name: Configure ICAP profiles.
      fmgr_icap_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        icap_profile:
          methods:
            - delete
            - get
            - head
            - options
            - post
            - put
            - trace
            - other
            - connect
          name: <string>
          replacemsg-group: <string>
          request: <value in [disable, enable]>
          request-failure: <value in [error, bypass]>
          request-path: <string>
          request-server: <string>
          response: <value in [disable, enable]>
          response-failure: <value in [error, bypass]>
          response-path: <string>
          response-server: <string>
          streaming-content-bypass: <value in [disable, enable]>
          icap-headers:
            -
              base64-encoding: <value in [disable, enable]>
              content: <string>
              id: <integer>
              name: <string>
          preview: <value in [disable, enable]>
          preview-data-length: <integer>
          response-req-hdr: <value in [disable, enable]>
          respmod-default-action: <value in [bypass, forward]>
          respmod-forward-rules:
            -
              action: <value in [bypass, forward]>
              header-group:
                -
                  case-sensitivity: <value in [disable, enable]>
                  header: <string>
                  header-name: <string>
                  id: <integer>
              host: <string>
              http-resp-status-code: <list or integer>
              name: <string>
          204-response: <value in [disable, enable]>
          204-size-limit: <integer>
          chunk-encap: <value in [disable, enable]>
          extension-feature:
            - scan-progress
          file-transfer:
            - ssh
            - ftp
          file-transfer-failure: <value in [error, bypass]>
          file-transfer-path: <string>
          file-transfer-server: <string>
          icap-block-log: <value in [disable, enable]>
          scan-progress-interval: <integer>
          timeout: <integer>
          comment: <string>
```

## [Return Values](fmgr_icap_profile_module.md#id5)

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
