---
collection: ansible
version: "6"
title: "cisco.ise.support_bundle_download module – Resource module for Support Bundle Download"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/support_bundle_download_module.html
fetched_at: 2026-07-27T16:59:41+00:00
---
# cisco.ise.support_bundle_download module – Resource module for Support Bundle Download

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](support_bundle_download_module.md#ansible-collections-cisco-ise-support-bundle-download-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.support_bundle_download`.

New in cisco.ise 1.0.0

- [Synopsis](support_bundle_download_module.md#synopsis)
- [Requirements](support_bundle_download_module.md#requirements)
- [Parameters](support_bundle_download_module.md#parameters)
- [Notes](support_bundle_download_module.md#notes)
- [Examples](support_bundle_download_module.md#examples)
- [Return Values](support_bundle_download_module.md#return-values)

## [Synopsis](support_bundle_download_module.md#id2)

- Manage operation update of the resource Support Bundle Download.
- This API allows the client to upload a support bundle.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](support_bundle_download_module.md#id3)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](support_bundle_download_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **dirPath**  string | Directory absolute path. Defaults to the current working directory. |
| **fileName**  string | Support Bundle Download’s fileName. |
| **filename**  string | The filename used to save the download file. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **saveFile**  boolean | Enable or disable automatic file creation of raw response.  Choices:   - `false` - `true` |

## [Notes](support_bundle_download_module.md#id5)

> **Note:**
>
> - SDK Method used are support_bundle_download.SupportBundleDownload.download_support_bundle,
> - Paths used are put /ers/config/supportbundledownload,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](support_bundle_download_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.ise.support_bundle_download:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    dirPath: /tmp/downloads/
    fileName: string
    filename: download_filename.extension
    saveFile: true
```

## [Return Values](support_bundle_download_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"data": "filecontent", "dirpath": "download/directory", "filename": "filename", "path": "download/directory/filename"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
