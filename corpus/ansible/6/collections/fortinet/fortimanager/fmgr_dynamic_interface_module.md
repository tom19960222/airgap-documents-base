---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_dynamic_interface module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_dynamic_interface_module.html
fetched_at: 2026-07-27T17:29:57+00:00
---
# fortinet.fortimanager.fmgr_dynamic_interface module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dynamic_interface`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dynamic_interface_module.md#synopsis)
- [Parameters](fmgr_dynamic_interface_module.md#parameters)
- [Notes](fmgr_dynamic_interface_module.md#notes)
- [Examples](fmgr_dynamic_interface_module.md#examples)
- [Return Values](fmgr_dynamic_interface_module.md#return-values)

## [Synopsis](fmgr_dynamic_interface_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dynamic_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **dynamic_interface**  dictionary | the top level parameters set |
| **color**  integer | no description |
| **default-mapping**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **defmap-intf**  string | no description |
| **defmap-intrazone-deny**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **defmap-zonemember**  string | no description |
| **description**  string | no description |
| **dynamic_mapping**  list / elements=string | no description |
| **_scope**  list / elements=string | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **egress-shaping-profile**  string | no description |
| **ingress-shaping-profile**  string | no description |
| **intrazone-deny**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **local-intf**  string | no description |
| **egress-shaping-profile**  string | no description |
| **ingress-shaping-profile**  string | no description |
| **name**  string | no description |
| **platform_mapping**  list / elements=string | no description |
| **egress-shaping-profile**  string | no description |
| **ingress-shaping-profile**  string | no description |
| **intf-zone**  string | no description |
| **intrazone-deny**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **single-intf**  string | no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **wildcard**  string | no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **wildcard-intf**  string | no description |
| **zone-only**  string | no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_dynamic_interface_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dynamic_interface_module.md#id4)

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
   - name: no description
     fmgr_dynamic_interface:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        dynamic_interface:
           color: <value of integer>
           default-mapping: <value in [disable, enable]>
           defmap-intf: <value of string>
           defmap-intrazone-deny: <value in [disable, enable]>
           defmap-zonemember: <value of string>
           description: <value of string>
           dynamic_mapping:
             -
                 _scope:
                   -
                       name: <value of string>
                       vdom: <value of string>
                 egress-shaping-profile: <value of string>
                 intrazone-deny: <value in [disable, enable]>
                 local-intf: <value of string>
                 ingress-shaping-profile: <value of string>
           egress-shaping-profile: <value of string>
           name: <value of string>
           single-intf: <value in [disable, enable]>
           ingress-shaping-profile: <value of string>
           platform_mapping:
             -
                 egress-shaping-profile: <value of string>
                 ingress-shaping-profile: <value of string>
                 intf-zone: <value of string>
                 intrazone-deny: <value in [disable, enable]>
                 name: <value of string>
           wildcard: <value in [disable, enable]>
           wildcard-intf: <value of string>
           zone-only: <value in [disable, enable]>
```

## [Return Values](fmgr_dynamic_interface_module.md#id5)

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
