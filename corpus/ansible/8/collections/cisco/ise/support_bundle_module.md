---
collection: ansible
version: "8"
title: "cisco.ise.support_bundle module – Resource module for Support Bundle"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/support_bundle_module.html
fetched_at: 2026-07-28T01:31:11+00:00
---
# cisco.ise.support_bundle module – Resource module for Support Bundle

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](support_bundle_module.md#ansible-collections-cisco-ise-support-bundle-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.support_bundle`.

New in cisco.ise 1.0.0

- [Synopsis](support_bundle_module.md#synopsis)
- [Requirements](support_bundle_module.md#requirements)
- [Parameters](support_bundle_module.md#parameters)
- [Notes](support_bundle_module.md#notes)
- [See Also](support_bundle_module.md#see-also)
- [Examples](support_bundle_module.md#examples)
- [Return Values](support_bundle_module.md#return-values)

## [Synopsis](support_bundle_module.md#id1)

- Manage operation create of the resource Support Bundle.
- This API allows the client to create a support bundle trigger configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](support_bundle_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](support_bundle_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Support Bundle’s description. |
| **hostName**  string | This parameter is hostName only, xxxx of xxxx.yyy.zz. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string | Resource Name. |
| **supportBundleIncludeOptions**  dictionary | Support Bundle’s supportBundleIncludeOptions. |
| **fromDate**  string | Date from where support bundle should include the logs. |
| **includeConfigDB**  boolean | Set to include Config DB in Support Bundle.  **Choices:**   - `false` - `true` |
| **includeCoreFiles**  boolean | Set to include Core files in Support Bundle.  **Choices:**   - `false` - `true` |
| **includeDebugLogs**  boolean | Set to include Debug logs in Support Bundle.  **Choices:**   - `false` - `true` |
| **includeLocalLogs**  boolean | Set to include Local logs in Support Bundle.  **Choices:**   - `false` - `true` |
| **includeSystemLogs**  boolean | Set to include System logs in Support Bundle.  **Choices:**   - `false` - `true` |
| **mntLogs**  boolean | Set to include Monitoring and troublshooting logs in Support Bundle.  **Choices:**   - `false` - `true` |
| **policyXml**  boolean | Set to include Policy XML in Support Bundle.  **Choices:**   - `false` - `true` |
| **toDate**  string | Date upto where support bundle should include the logs. |

## [Notes](support_bundle_module.md#id4)

> **Note:**
>
> - SDK Method used are support_bundle_trigger_configuration.SupportBundleTriggerConfiguration.create_support_bundle,
> - Paths used are post /ers/config/supportbundle,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](support_bundle_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for SupportBundleTriggerConfiguration](https://developer.cisco.com/docs/identity-services-engine/v1/#!supportbundle)
> :   Complete reference of the SupportBundleTriggerConfiguration API.

## [Examples](support_bundle_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.support_bundle:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    description: string
    hostName: string
    name: string
    supportBundleIncludeOptions:
      fromDate: string
      includeConfigDB: true
      includeCoreFiles: true
      includeDebugLogs: true
      includeLocalLogs: true
      includeSystemLogs: true
      mntLogs: true
      policyXml: true
      toDate: string
```

## [Return Values](support_bundle_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
