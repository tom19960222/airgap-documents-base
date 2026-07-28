---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_address6_dynamicmapping module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_address6_dynamicmapping_module.html
fetched_at: 2026-07-27T17:30:48+00:00
---
# fortinet.fortimanager.fmgr_firewall_address6_dynamicmapping module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_address6_dynamicmapping`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_address6_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_firewall_address6_dynamicmapping_module.md#parameters)
- [Notes](fmgr_firewall_address6_dynamicmapping_module.md#notes)
- [Examples](fmgr_firewall_address6_dynamicmapping_module.md#examples)
- [Return Values](fmgr_firewall_address6_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_firewall_address6_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_address6_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address6**  string / required | the parameter (address6) in requested url |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_address6_dynamicmapping**  dictionary | the top level parameters set |
| **_image-base64**  string | no description |
| **_scope**  list / elements=string | description |
| **name**  string | no description |
| **vdom**  string | no description |
| **cache-ttl**  integer | no description |
| **color**  integer | no description |
| **comment**  string | no description |
| **country**  string | no description |
| **end-ip**  string | no description |
| **end-mac**  string | no description |
| **fabric-object**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fqdn**  string | no description |
| **global-object**  integer | no description |
| **host**  string | no description |
| **host-type**  string | no description  Choices:   - `"any"` - `"specific"` |
| **ip6**  string | no description |
| **macaddr**  string | description |
| **obj-id**  string | no description |
| **sdn**  string | no description  Choices:   - `"nsx"` |
| **start-ip**  string | no description |
| **start-mac**  string | no description |
| **subnet-segment**  list / elements=string | description |
| **name**  string | no description |
| **type**  string | no description  Choices:   - `"any"` - `"specific"` |
| **value**  string | no description |
| **tags**  string | no description |
| **template**  string | no description |
| **type**  string | no description  Choices:   - `"ipprefix"` - `"iprange"` - `"nsx"` - `"dynamic"` - `"fqdn"` - `"template"` - `"mac"` - `"geography"` |
| **uuid**  string | no description |
| **visibility**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_address6_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_address6_dynamicmapping_module.md#id4)

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
   - name: Configure dynamic mappings of IPv6 address
     fmgr_firewall_address6_dynamicmapping:
        bypass_validation: False
        adom: ansible
        address6: 'ansible-test' # name
        state: present
        firewall_address6_dynamicmapping:
           _scope:
             -
                 name: FGT_AWS # need a valid device name
                 vdom: root # need a valid vdom name under the device
           cache-ttl: 0
           color: 22
           comment: 'ansible-test-comment'
           end-ip: '::100'
           host: '::'
           host-type: any #<value in [any, specific]>
           ip6: '::/128'
           start-ip: '::'
           type: iprange #<value in [ipprefix, iprange, nsx, ...]>
           visibility: enable

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
   - name: retrieve all the dynamic mappings of IPv6 address
     fmgr_fact:
       facts:
           selector: 'firewall_address6_dynamicmapping'
           params:
               adom: 'ansible'
               address6: 'ansible-test' # name
               dynamic_mapping: 'your_value'
```

## [Return Values](fmgr_firewall_address6_dynamicmapping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
