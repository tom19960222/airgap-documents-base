---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_admin_setting module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_admin_setting_module.html
fetched_at: 2026-07-27T17:35:36+00:00
---
# fortinet.fortimanager.fmgr_system_admin_setting module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_setting`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_admin_setting_module.md#synopsis)
- [Parameters](fmgr_system_admin_setting_module.md#parameters)
- [Notes](fmgr_system_admin_setting_module.md#notes)
- [Examples](fmgr_system_admin_setting_module.md#examples)
- [Return Values](fmgr_system_admin_setting_module.md#return-values)

## [Synopsis](fmgr_system_admin_setting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_admin_setting**  dictionary | the top level parameters set |
| **access-banner**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **admin-https-redirect**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **admin-login-max**  integer | no description  Default: `256` |
| **admin_server_cert**  string | no description  Default: `"server."` |
| **allow_register**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **auth-addr**  string | no description |
| **auth-port**  integer | no description  Default: `443` |
| **auto-update**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **banner-message**  string | no description |
| **central-ftgd-local-cat-id**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **chassis-mgmt**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **chassis-update-interval**  integer | no description  Default: `15` |
| **device_sync_status**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **gui-theme**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"blue"` ← (default) - `"green"` - `"red"` - `"melongene"` - `"spring"` - `"summer"` - `"autumn"` - `"winter"` - `"space"` - `"calla-lily"` - `"binary-tunnel"` - `"diving"` - `"dreamy"` - `"technology"` - `"landscape"` - `"twilight"` - `"canyon"` - `"northern-light"` - `"astronomy"` - `"fish"` - `"penguin"` - `"panda"` - `"polar-bear"` - `"parrot"` - `"cave"` - `"mountain"` - `"zebra"` - `"contrast-dark"` - `"circuit-board"` - `"mars"` - `"blue-sea"` |
| **http_port**  integer | no description  Default: `80` |
| **https_port**  integer | no description  Default: `443` |
| **idle_timeout**  integer | no description  Default: `15` |
| **idle_timeout_api**  integer | no description  Default: `900` |
| **idle_timeout_gui**  integer | no description  Default: `900` |
| **idle_timeout_sso**  integer | no description  Default: `900` |
| **install-ifpolicy-only**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **mgmt-addr**  string | no description |
| **mgmt-fqdn**  string | no description |
| **objects-force-deletion**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **offline_mode**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **preferred-fgfm-intf**  string | no description |
| **register_passwd**  string | no description |
| **sdwan-monitor-history**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **sdwan-skip-unmapped-input-device**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **shell-access**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **shell-password**  string | no description |
| **show-add-multiple**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show-adom-devman**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **show-checkbox-in-table**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show-device-import-export**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show-fct-manager**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show-hostname**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show_automatic_script**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show_grouping_script**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **show_schedule_script**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **show_tcl_script**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **traffic-shaping-history**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **unreg_dev_opt**  string | no description  no description  no description  no description  Choices:   - `"add_no_service"` - `"ignore"` - `"add_allow_service"` ← (default) |
| **webadmin_language**  string | no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"auto_detect"` ← (default) - `"english"` - `"simplified_chinese"` - `"traditional_chinese"` - `"japanese"` - `"korean"` - `"spanish"` - `"french"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_admin_setting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_setting_module.md#id4)

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
     fmgr_system_admin_setting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_admin_setting:
           access-banner: <value in [disable, enable]>
           admin-https-redirect: <value in [disable, enable]>
           admin-login-max: <value of integer>
           admin_server_cert: <value of string>
           allow_register: <value in [disable, enable]>
           auto-update: <value in [disable, enable]>
           banner-message: <value of string>
           chassis-mgmt: <value in [disable, enable]>
           chassis-update-interval: <value of integer>
           device_sync_status: <value in [disable, enable]>
           gui-theme: <value in [blue, green, red, ...]>
           http_port: <value of integer>
           https_port: <value of integer>
           idle_timeout: <value of integer>
           install-ifpolicy-only: <value in [disable, enable]>
           mgmt-addr: <value of string>
           mgmt-fqdn: <value of string>
           objects-force-deletion: <value in [disable, enable]>
           offline_mode: <value in [disable, enable]>
           register_passwd: <value of string>
           sdwan-monitor-history: <value in [disable, enable]>
           shell-access: <value in [disable, enable]>
           shell-password: <value of string>
           show-add-multiple: <value in [disable, enable]>
           show-adom-devman: <value in [disable, enable]>
           show-checkbox-in-table: <value in [disable, enable]>
           show-device-import-export: <value in [disable, enable]>
           show-hostname: <value in [disable, enable]>
           show_automatic_script: <value in [disable, enable]>
           show_grouping_script: <value in [disable, enable]>
           show_schedule_script: <value in [disable, enable]>
           show_tcl_script: <value in [disable, enable]>
           unreg_dev_opt: <value in [add_no_service, ignore, add_allow_service]>
           webadmin_language: <value in [auto_detect, english, simplified_chinese, ...]>
           show-fct-manager: <value in [disable, enable]>
           sdwan-skip-unmapped-input-device: <value in [disable, enable]>
           auth-addr: <value of string>
           auth-port: <value of integer>
           idle_timeout_api: <value of integer>
           idle_timeout_gui: <value of integer>
           central-ftgd-local-cat-id: <value in [disable, enable]>
           idle_timeout_sso: <value of integer>
           preferred-fgfm-intf: <value of string>
           traffic-shaping-history: <value in [disable, enable]>
```

## [Return Values](fmgr_system_admin_setting_module.md#id5)

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
