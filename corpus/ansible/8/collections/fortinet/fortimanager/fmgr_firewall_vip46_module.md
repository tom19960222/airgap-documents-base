---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_vip46 module – Configure IPv4 to IPv6 virtual IPs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_vip46_module.html
fetched_at: 2026-07-28T02:13:05+00:00
---
# fortinet.fortimanager.fmgr_firewall_vip46 module – Configure IPv4 to IPv6 virtual IPs.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_vip46`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_vip46_module.md#synopsis)
- [Parameters](fmgr_firewall_vip46_module.md#parameters)
- [Notes](fmgr_firewall_vip46_module.md#notes)
- [Examples](fmgr_firewall_vip46_module.md#examples)
- [Return Values](fmgr_firewall_vip46_module.md#return-values)

## [Synopsis](fmgr_firewall_vip46_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_vip46_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_vip46**  dictionary | the top level parameters set |
| **arp-reply**  string | Enable ARP reply.  **Choices:**   - `"disable"` - `"enable"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **arp-reply**  string | Enable ARP reply.  **Choices:**   - `"disable"` - `"enable"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **extip**  string | Start-external-IP [-end-external-IP]. |
| **extport**  string | External service port. |
| **id**  integer | Custom defined id. |
| **ldb-method**  string | Load balance method.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` |
| **mappedip**  string | Start-mapped-IP [-end mapped-IP]. |
| **mappedport**  string | Mapped service port. |
| **monitor**  any | (list or str) Health monitors. |
| **portforward**  string | Enable port forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **protocol**  string | Mapped port protocol.  **Choices:**   - `"tcp"` - `"udp"` |
| **server-type**  string | Server type.  **Choices:**   - `"http"` - `"tcp"` - `"udp"` - `"ip"` |
| **src-filter**  any | (list) Source IP filter |
| **srcintf-filter**  any | (list or str) Interfaces to which the VIP46 applies. |
| **type**  string | VIP type  **Choices:**   - `"static-nat"` - `"server-load-balance"` |
| **uuid**  string | Universally Unique Identifier |
| **extip**  string | Start-external-IP [-end-external-IP]. |
| **extport**  string | External service port. |
| **id**  integer | Custom defined id. |
| **ldb-method**  string | Load balance method.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` |
| **mappedip**  string | Start-mapped-IP [-end mapped-IP]. |
| **mappedport**  string | Mapped service port. |
| **monitor**  any | (list or str) Health monitors. |
| **name**  string / required | VIP46 name. |
| **portforward**  string | Enable port forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **protocol**  string | Mapped port protocol.  **Choices:**   - `"tcp"` - `"udp"` |
| **realservers**  list / elements=dictionary | Realservers. |
| **client-ip**  string | Restrict server to a client IP in this range. |
| **healthcheck**  string | Per server health check.  **Choices:**   - `"disable"` - `"enable"` - `"vip"` |
| **holddown-interval**  integer | Hold down interval. |
| **id**  integer | Real server ID. |
| **ip**  string | Mapped server IPv6. |
| **max-connections**  integer | Maximum number of connections allowed to server. |
| **monitor**  any | (list or str) Health monitors. |
| **port**  integer | Mapped server port. |
| **status**  string | Server administrative status.  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **weight**  integer | Weight. |
| **server-type**  string | Server type.  **Choices:**   - `"http"` - `"tcp"` - `"udp"` - `"ip"` |
| **src-filter**  any | (list) Source IP filter |
| **srcintf-filter**  any | (list or str) Interfaces to which the VIP46 applies. |
| **type**  string | VIP type  **Choices:**   - `"static-nat"` - `"server-load-balance"` |
| **uuid**  string | Universally Unique Identifier |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_vip46_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_vip46_module.md#id4)

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
   - name: retrieve all the IPv4 to IPv6 virtual IPs
     fmgr_fact:
       facts:
           selector: 'firewall_vip46'
           params:
               adom: 'ansible'
               vip46: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure IPv4 to IPv6 virtual IPs.
     fmgr_firewall_vip46:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_vip46:
           arp-reply: enable
           color: 1
           comment: 'ansible-comment'
           id: 1
           ldb-method: static #<value in [static, round-robin, weighted, ...]>
           name: 'ansible-test-vip46'
           protocol: tcp #<value in [tcp, udp]>
```

## [Return Values](fmgr_firewall_vip46_module.md#id5)

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
