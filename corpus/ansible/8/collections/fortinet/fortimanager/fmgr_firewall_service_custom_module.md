---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_service_custom module – Configure custom services."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_service_custom_module.html
fetched_at: 2026-07-28T02:12:48+00:00
---
# fortinet.fortimanager.fmgr_firewall_service_custom module – Configure custom services.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_service_custom`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_service_custom_module.md#synopsis)
- [Parameters](fmgr_firewall_service_custom_module.md#parameters)
- [Notes](fmgr_firewall_service_custom_module.md#notes)
- [Examples](fmgr_firewall_service_custom_module.md#examples)
- [Return Values](fmgr_firewall_service_custom_module.md#return-values)

## [Synopsis](fmgr_firewall_service_custom_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_service_custom_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_service_custom**  dictionary | the top level parameters set |
| **app-category**  any | (list) Application category ID. |
| **app-service-type**  string | Application service type.  **Choices:**   - `"disable"` - `"app-id"` - `"app-category"` |
| **application**  any | (list) Application ID. |
| **category**  string | Service category. |
| **check-reset-range**  string | Configure the type of ICMP error message verification.  **Choices:**   - `"disable"` - `"default"` - `"strict"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  any | (dict or str) no description |
| **explicit-proxy**  string | Enable/disable explicit web proxy service.  **Choices:**   - `"disable"` - `"enable"` |
| **fabric-object**  string | Security Fabric global object setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fqdn**  string | Fully qualified domain name. |
| **global-object**  integer | Global Object. |
| **helper**  string | Helper name.  **Choices:**   - `"disable"` - `"auto"` - `"ftp"` - `"tftp"` - `"ras"` - `"h323"` - `"tns"` - `"mms"` - `"sip"` - `"pptp"` - `"rtsp"` - `"dns-udp"` - `"dns-tcp"` - `"pmap"` - `"rsh"` - `"dcerpc"` - `"mgcp"` - `"gtp-c"` - `"gtp-u"` - `"gtp-b"` - `"pfcp"` |
| **icmpcode**  integer | ICMP code. |
| **icmptype**  integer | ICMP type. |
| **iprange**  string | Start and end of the IP range associated with service. |
| **name**  string / required | Custom service name. |
| **protocol**  string | Protocol type based on IANA numbers.  **Choices:**   - `"ICMP"` - `"IP"` - `"TCP/UDP/SCTP"` - `"ICMP6"` - `"HTTP"` - `"FTP"` - `"CONNECT"` - `"SOCKS"` - `"ALL"` - `"SOCKS-TCP"` - `"SOCKS-UDP"` |
| **protocol-number**  integer | IP protocol number. |
| **proxy**  string | Enable/disable web proxy service.  **Choices:**   - `"disable"` - `"enable"` |
| **sctp-portrange**  string | Multiple SCTP port ranges. |
| **session-ttl**  any | (int or str) Session TTL |
| **tcp-halfclose-timer**  integer | Wait time to close a TCP session waiting for an unanswered FIN packet |
| **tcp-halfopen-timer**  integer | Wait time to close a TCP session waiting for an unanswered open session packet |
| **tcp-portrange**  string | Multiple TCP port ranges. |
| **tcp-rst-timer**  integer | Set the length of the TCP CLOSE state in seconds |
| **tcp-timewait-timer**  integer | Set the length of the TCP TIME-WAIT state in seconds |
| **udp-idle-timer**  integer | UDP half close timeout |
| **udp-portrange**  string | Multiple UDP port ranges. |
| **visibility**  string | Enable/disable the visibility of the service on the GUI.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_service_custom_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_service_custom_module.md#id4)

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
   - name: Configure custom services.
     fmgr_firewall_service_custom:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_service_custom:
           app-service-type: disable #<value in [disable, app-id, app-category]>
           color: 1
           comment: 'comment'
           helper: auto #<value in [disable, auto, ftp, ...]>
           name: 'ansible-test'
           protocol: ALL #<value in [ICMP, IP, TCP/UDP/SCTP, ...]>
           proxy: enable #<value in [disable, enable]>
           visibility: enable #<value in [disable, enable]>
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
   - name: retrieve all the custom services
     fmgr_fact:
       facts:
           selector: 'firewall_service_custom'
           params:
               adom: 'ansible'
               custom: 'your_value'
```

## [Return Values](fmgr_firewall_service_custom_module.md#id5)

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
