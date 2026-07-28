---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_gtp_ievalidation module – IE validation."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_gtp_ievalidation_module.html
fetched_at: 2026-07-28T02:11:55+00:00
---
# fortinet.fortimanager.fmgr_firewall_gtp_ievalidation module – IE validation.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_gtp_ievalidation`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_gtp_ievalidation_module.md#synopsis)
- [Parameters](fmgr_firewall_gtp_ievalidation_module.md#parameters)
- [Notes](fmgr_firewall_gtp_ievalidation_module.md#notes)
- [Examples](fmgr_firewall_gtp_ievalidation_module.md#examples)
- [Return Values](fmgr_firewall_gtp_ievalidation_module.md#return-values)

## [Synopsis](fmgr_firewall_gtp_ievalidation_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_gtp_ievalidation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_gtp_ievalidation**  dictionary | the top level parameters set |
| **apn-restriction**  string | Validate APN restriction.  **Choices:**   - `"disable"` - `"enable"` |
| **charging-gateway-addr**  string | Validate charging gateway address.  **Choices:**   - `"disable"` - `"enable"` |
| **charging-ID**  string | Validate charging ID.  **Choices:**   - `"disable"` - `"enable"` |
| **end-user-addr**  string | Validate end user address.  **Choices:**   - `"disable"` - `"enable"` |
| **gsn-addr**  string | Validate GSN address.  **Choices:**   - `"disable"` - `"enable"` |
| **imei**  string | Validate IMEI  **Choices:**   - `"disable"` - `"enable"` |
| **imsi**  string | Validate IMSI.  **Choices:**   - `"disable"` - `"enable"` |
| **mm-context**  string | Validate MM context.  **Choices:**   - `"disable"` - `"enable"` |
| **ms-tzone**  string | Validate MS time zone.  **Choices:**   - `"disable"` - `"enable"` |
| **ms-validated**  string | Validate MS validated.  **Choices:**   - `"disable"` - `"enable"` |
| **msisdn**  string | Validate MSISDN.  **Choices:**   - `"disable"` - `"enable"` |
| **nsapi**  string | Validate NSAPI.  **Choices:**   - `"disable"` - `"enable"` |
| **pdp-context**  string | Validate PDP context.  **Choices:**   - `"disable"` - `"enable"` |
| **qos-profile**  string | Validate Quality of Service  **Choices:**   - `"disable"` - `"enable"` |
| **rai**  string | Validate RAI.  **Choices:**   - `"disable"` - `"enable"` |
| **rat-type**  string | Validate RAT type.  **Choices:**   - `"disable"` - `"enable"` |
| **reordering-required**  string | Validate re-ordering required.  **Choices:**   - `"disable"` - `"enable"` |
| **selection-mode**  string | Validate selection mode.  **Choices:**   - `"disable"` - `"enable"` |
| **uli**  string | Validate user location information.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **gtp**  string / required | the parameter (gtp) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_gtp_ievalidation_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_gtp_ievalidation_module.md#id4)

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
    - name: IE validation.
      fmgr_firewall_gtp_ievalidation:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_ievalidation:
          apn-restriction: <value in [disable, enable]>
          charging-ID: <value in [disable, enable]>
          charging-gateway-addr: <value in [disable, enable]>
          end-user-addr: <value in [disable, enable]>
          gsn-addr: <value in [disable, enable]>
          imei: <value in [disable, enable]>
          imsi: <value in [disable, enable]>
          mm-context: <value in [disable, enable]>
          ms-tzone: <value in [disable, enable]>
          ms-validated: <value in [disable, enable]>
          msisdn: <value in [disable, enable]>
          nsapi: <value in [disable, enable]>
          pdp-context: <value in [disable, enable]>
          qos-profile: <value in [disable, enable]>
          rai: <value in [disable, enable]>
          rat-type: <value in [disable, enable]>
          reordering-required: <value in [disable, enable]>
          selection-mode: <value in [disable, enable]>
          uli: <value in [disable, enable]>
```

## [Return Values](fmgr_firewall_gtp_ievalidation_module.md#id5)

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
