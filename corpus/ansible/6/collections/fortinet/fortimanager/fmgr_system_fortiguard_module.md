---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_fortiguard module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_fortiguard_module.html
fetched_at: 2026-07-27T17:36:03+00:00
---
# fortinet.fortimanager.fmgr_system_fortiguard module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_fortiguard`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_fortiguard_module.md#synopsis)
- [Parameters](fmgr_system_fortiguard_module.md#parameters)
- [Notes](fmgr_system_fortiguard_module.md#notes)
- [Examples](fmgr_system_fortiguard_module.md#examples)
- [Return Values](fmgr_system_fortiguard_module.md#return-values)

## [Synopsis](fmgr_system_fortiguard_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_fortiguard_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_fortiguard**  dictionary | the top level parameters set |
| **antispam-cache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **antispam-cache-mpercent**  integer | no description |
| **antispam-cache-ttl**  integer | no description |
| **antispam-expiration**  integer | no description |
| **antispam-force-off**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **antispam-license**  integer | no description |
| **antispam-timeout**  integer | no description |
| **anycast-sdns-server-ip**  string | no description |
| **anycast-sdns-server-port**  integer | no description |
| **auto-join-forticloud**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ddns-server-ip**  string | no description |
| **ddns-server-ip6**  string | no description |
| **ddns-server-port**  integer | no description |
| **fortiguard-anycast**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortiguard-anycast-source**  string | no description  Choices:   - `"fortinet"` - `"aws"` - `"debug"` |
| **interface**  string | no description |
| **interface-select-method**  string | no description  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **load-balance-servers**  integer | no description |
| **outbreak-prevention-cache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbreak-prevention-cache-mpercent**  integer | no description |
| **outbreak-prevention-cache-ttl**  integer | no description |
| **outbreak-prevention-expiration**  integer | no description |
| **outbreak-prevention-force-off**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbreak-prevention-license**  integer | no description |
| **outbreak-prevention-timeout**  integer | no description |
| **persistent-connection**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **port**  string | no description  Choices:   - `"53"` - `"80"` - `"8888"` - `"443"` |
| **protocol**  string | no description  Choices:   - `"udp"` - `"http"` - `"https"` |
| **proxy-password**  string | no description |
| **proxy-server-ip**  string | no description |
| **proxy-server-port**  integer | no description |
| **proxy-username**  string | no description |
| **sandbox-region**  string | no description |
| **sdns-options**  list / elements=string | no description  Choices:   - `"include-question-section"` |
| **sdns-server-ip**  string | no description |
| **sdns-server-port**  integer | no description |
| **service-account-id**  string | no description |
| **source-ip**  string | no description |
| **source-ip6**  string | no description |
| **update-build-proxy**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **update-extdb**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **update-ffdb**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **update-server-location**  string | no description  Choices:   - `"any"` - `"usa"` - `"automatic"` - `"eu"` |
| **update-uwdb**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vdom**  string | no description |
| **videofilter-expiration**  integer | no description |
| **videofilter-license**  integer | no description |
| **webfilter-cache**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webfilter-cache-ttl**  integer | no description |
| **webfilter-expiration**  integer | no description |
| **webfilter-force-off**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webfilter-license**  integer | no description |
| **webfilter-timeout**  integer | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_fortiguard_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_fortiguard_module.md#id4)

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
     fmgr_system_fortiguard:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_fortiguard:
           antispam-cache: <value in [disable, enable]>
           antispam-cache-mpercent: <value of integer>
           antispam-cache-ttl: <value of integer>
           antispam-expiration: <value of integer>
           antispam-force-off: <value in [disable, enable]>
           antispam-license: <value of integer>
           antispam-timeout: <value of integer>
           auto-join-forticloud: <value in [disable, enable]>
           ddns-server-ip: <value of string>
           ddns-server-port: <value of integer>
           load-balance-servers: <value of integer>
           outbreak-prevention-cache: <value in [disable, enable]>
           outbreak-prevention-cache-mpercent: <value of integer>
           outbreak-prevention-cache-ttl: <value of integer>
           outbreak-prevention-expiration: <value of integer>
           outbreak-prevention-force-off: <value in [disable, enable]>
           outbreak-prevention-license: <value of integer>
           outbreak-prevention-timeout: <value of integer>
           port: <value in [53, 80, 8888, ...]>
           sdns-server-ip: <value of string>
           sdns-server-port: <value of integer>
           service-account-id: <value of string>
           source-ip: <value of string>
           source-ip6: <value of string>
           update-server-location: <value in [any, usa, automatic, ...]>
           webfilter-cache: <value in [disable, enable]>
           webfilter-cache-ttl: <value of integer>
           webfilter-expiration: <value of integer>
           webfilter-force-off: <value in [disable, enable]>
           webfilter-license: <value of integer>
           webfilter-timeout: <value of integer>
           protocol: <value in [udp, http, https]>
           proxy-password: <value of string>
           proxy-server-ip: <value of string>
           proxy-server-port: <value of integer>
           proxy-username: <value of string>
           sandbox-region: <value of string>
           fortiguard-anycast: <value in [disable, enable]>
           fortiguard-anycast-source: <value in [fortinet, aws, debug]>
           interface: <value of string>
           interface-select-method: <value in [auto, sdwan, specify]>
           sdns-options:
             - include-question-section
           anycast-sdns-server-ip: <value of string>
           anycast-sdns-server-port: <value of integer>
           persistent-connection: <value in [disable, enable]>
           update-build-proxy: <value in [disable, enable]>
           update-extdb: <value in [disable, enable]>
           update-ffdb: <value in [disable, enable]>
           update-uwdb: <value in [disable, enable]>
           videofilter-expiration: <value of integer>
           videofilter-license: <value of integer>
           ddns-server-ip6: <value of string>
           vdom: <value of string>
```

## [Return Values](fmgr_system_fortiguard_module.md#id5)

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
