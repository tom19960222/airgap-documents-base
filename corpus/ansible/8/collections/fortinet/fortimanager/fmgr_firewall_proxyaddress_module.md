---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_proxyaddress module – Web proxy address configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_proxyaddress_module.html
fetched_at: 2026-07-28T02:12:42+00:00
---
# fortinet.fortimanager.fmgr_firewall_proxyaddress module – Web proxy address configuration.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_proxyaddress`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_proxyaddress_module.md#synopsis)
- [Parameters](fmgr_firewall_proxyaddress_module.md#parameters)
- [Notes](fmgr_firewall_proxyaddress_module.md#notes)
- [Examples](fmgr_firewall_proxyaddress_module.md#examples)
- [Return Values](fmgr_firewall_proxyaddress_module.md#return-values)

## [Synopsis](fmgr_firewall_proxyaddress_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_proxyaddress_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_proxyaddress**  dictionary | the top level parameters set |
| **_image-base64**  string | _Image-Base64. |
| **application**  any | (list) no description |
| **case-sensitivity**  string | Enable to make the pattern case sensitive.  **Choices:**   - `"disable"` - `"enable"` |
| **category**  any | (list or str) FortiGuard category ID. |
| **color**  integer | Integer value to determine the color of the icon in the GUI |
| **comment**  string | Optional comments. |
| **header**  string | HTTP header name as a regular expression. |
| **header-group**  list / elements=dictionary | Header-Group. |
| **case-sensitivity**  string | Case sensitivity in pattern.  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | HTTP header regular expression. |
| **header-name**  string | HTTP header. |
| **id**  integer | ID. |
| **header-name**  string | Name of HTTP header. |
| **host**  string | Address object for the host. |
| **host-regex**  string | Host name as a regular expression. |
| **method**  list / elements=string | HTTP request methods to be used.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"connect"` |
| **name**  string / required | Address name. |
| **path**  string | URL path as a regular expression. |
| **query**  string | Match the query part of the URL as a regular expression. |
| **referrer**  string | Enable/disable use of referrer field in the HTTP header to match the address.  **Choices:**   - `"disable"` - `"enable"` |
| **tagging**  list / elements=dictionary | Tagging. |
| **category**  string | Tag category. |
| **name**  string | Tagging entry name. |
| **tags**  any | (list) Tags. |
| **tags**  string | Names of object-tags |
| **type**  string | Proxy address type.  **Choices:**   - `"host-regex"` - `"url"` - `"category"` - `"method"` - `"ua"` - `"header"` - `"src-advanced"` - `"dst-advanced"` - `"url-list"` - `"saas"` |
| **ua**  list / elements=string | Names of browsers to be used as user agent.  **Choices:**   - `"chrome"` - `"ms"` - `"firefox"` - `"safari"` - `"other"` - `"ie"` - `"edge"` |
| **ua-max-ver**  string | Maximum version of the user agent specified in dotted notation. |
| **ua-min-ver**  string | Minimum version of the user agent specified in dotted notation. |
| **uuid**  string | Universally Unique Identifier |
| **visibility**  string | Enable/disable visibility of the object in the GUI.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_proxyaddress_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_proxyaddress_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the proxy addresses
     fmgr_fact:
       facts:
           selector: 'firewall_proxyaddress'
           params:
               adom: 'ansible'
               proxy-address: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Web proxy address configuration.
     fmgr_firewall_proxyaddress:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_proxyaddress:
           case-sensitivity: disable
           color: 1
           comment: 'ansible-comment'
           name: 'ansible-test'
```

## [Return Values](fmgr_firewall_proxyaddress_module.md#id5)

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
