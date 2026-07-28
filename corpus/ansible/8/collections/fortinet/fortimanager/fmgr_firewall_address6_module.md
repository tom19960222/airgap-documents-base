---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_address6 module – Configure IPv6 firewall addresses."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_address6_module.html
fetched_at: 2026-07-28T02:11:28+00:00
---
# fortinet.fortimanager.fmgr_firewall_address6 module – Configure IPv6 firewall addresses.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_address6`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_address6_module.md#synopsis)
- [Parameters](fmgr_firewall_address6_module.md#parameters)
- [Notes](fmgr_firewall_address6_module.md#notes)
- [Examples](fmgr_firewall_address6_module.md#examples)
- [Return Values](fmgr_firewall_address6_module.md#return-values)

## [Synopsis](fmgr_firewall_address6_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_address6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_address6**  dictionary | the top level parameters set |
| **_image-base64**  string | _Image-Base64. |
| **cache-ttl**  integer | Minimal TTL of individual IPv6 addresses in FQDN cache. |
| **color**  integer | Integer value to determine the color of the icon in the GUI |
| **comment**  string | Comment. |
| **country**  string | IPv6 addresses associated to a specific country. |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_image-base64**  string | _Image-Base64. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **cache-ttl**  integer | Minimal TTL of individual IPv6 addresses in FQDN cache. |
| **color**  integer | Integer value to determine the color of the icon in the GUI |
| **comment**  string | Comment. |
| **country**  string | Country. |
| **end-ip**  string | Final IP address |
| **end-mac**  string | Last MAC address in the range. |
| **epg-name**  string | Endpoint group name. |
| **fabric-object**  string | Security Fabric global object setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fqdn**  string | Fully qualified domain name. |
| **global-object**  integer | Global-Object. |
| **host**  string | Host Address. |
| **host-type**  string | Host type.  **Choices:**   - `"any"` - `"specific"` |
| **ip6**  string | IPv6 address prefix |
| **macaddr**  any | (list) Macaddr. |
| **obj-id**  string | Object ID for NSX. |
| **route-tag**  integer | route-tag address. |
| **sdn**  string | SDN.  **Choices:**   - `"nsx"` |
| **sdn-tag**  string | SDN Tag. |
| **start-ip**  string | First IP address |
| **start-mac**  string | First MAC address in the range. |
| **subnet-segment**  list / elements=dictionary | Subnet-Segment. |
| **name**  string | Name. |
| **type**  string | Subnet segment type.  **Choices:**   - `"any"` - `"specific"` |
| **value**  string | Subnet segment value. |
| **tags**  any | (list or str) Tags. |
| **template**  string | IPv6 address template. |
| **tenant**  string | Tenant. |
| **type**  string | Type of IPv6 address object  **Choices:**   - `"ipprefix"` - `"iprange"` - `"nsx"` - `"dynamic"` - `"fqdn"` - `"template"` - `"mac"` - `"geography"` - `"route-tag"` |
| **uuid**  string | Universally Unique Identifier |
| **visibility**  string | Enable/disable the visibility of the object in the GUI.  **Choices:**   - `"disable"` - `"enable"` |
| **end-ip**  string | Final IP address |
| **end-mac**  string | Last MAC address in the range. |
| **epg-name**  string | Endpoint group name. |
| **fabric-object**  string | Security Fabric global object setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fqdn**  string | Fully qualified domain name. |
| **global-object**  integer | Global Object. |
| **host**  string | Host Address. |
| **host-type**  string | Host type.  **Choices:**   - `"any"` - `"specific"` |
| **ip6**  string | IPv6 address prefix |
| **list**  list / elements=dictionary | List. |
| **ip**  string | IP. |
| **net-id**  string | Network ID. |
| **obj-id**  string | Object ID. |
| **macaddr**  any | (list) Multiple MAC address ranges. |
| **name**  string / required | Address name. |
| **obj-id**  string | Object ID for NSX. |
| **profile-list**  list / elements=dictionary | no description |
| **profile-id**  integer | NSX service profile ID. |
| **route-tag**  integer | route-tag address. |
| **sdn**  string | SDN.  **Choices:**   - `"nsx"` |
| **sdn-tag**  string | SDN Tag. |
| **start-ip**  string | First IP address |
| **start-mac**  string | First MAC address in the range. |
| **subnet-segment**  list / elements=dictionary | Subnet-Segment. |
| **name**  string | Name. |
| **type**  string | Subnet segment type.  **Choices:**   - `"any"` - `"specific"` |
| **value**  string | Subnet segment value. |
| **tagging**  list / elements=dictionary | Tagging. |
| **category**  string | Tag category. |
| **name**  string | Tagging entry name. |
| **tags**  any | (list) Tags. |
| **tags**  string | Names of object-tags applied to address. |
| **template**  string | IPv6 address template. |
| **tenant**  string | Tenant. |
| **type**  string | Type of IPv6 address object  **Choices:**   - `"ipprefix"` - `"iprange"` - `"nsx"` - `"dynamic"` - `"fqdn"` - `"template"` - `"mac"` - `"geography"` - `"route-tag"` |
| **uuid**  string | Universally Unique Identifier |
| **visibility**  string | Enable/disable the visibility of the object in the GUI.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_address6_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_address6_module.md#id4)

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
   - name: retrieve all the IPv6 addresses
     fmgr_fact:
       facts:
           selector: 'firewall_address6'
           params:
               adom: 'ansible'
               address6: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure IPv6 firewall addresses.
     fmgr_firewall_address6:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_address6:
           host-type: any #<value in [any, specific]>
           ip6: '::/55'
           name: 'ansible-test'
           visibility: disable
```

## [Return Values](fmgr_firewall_address6_module.md#id5)

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
