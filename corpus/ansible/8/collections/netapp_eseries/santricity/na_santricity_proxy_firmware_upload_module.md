---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_proxy_firmware_upload module – NetApp E-Series manage proxy firmware uploads."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_proxy_firmware_upload_module.html
fetched_at: 2026-07-28T02:44:17+00:00
---
# netapp_eseries.santricity.na_santricity_proxy_firmware_upload module – NetApp E-Series manage proxy firmware uploads.

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_proxy_firmware_upload`.

- [Synopsis](na_santricity_proxy_firmware_upload_module.md#synopsis)
- [Parameters](na_santricity_proxy_firmware_upload_module.md#parameters)
- [Notes](na_santricity_proxy_firmware_upload_module.md#notes)
- [Examples](na_santricity_proxy_firmware_upload_module.md#examples)
- [Return Values](na_santricity_proxy_firmware_upload_module.md#return-values)

## [Synopsis](na_santricity_proxy_firmware_upload_module.md#id1)

- Ensure specific firmware versions are available on SANtricity Web Services Proxy.

## [Parameters](na_santricity_proxy_firmware_upload_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **firmware**  list / elements=string | List of paths and/or directories containing firmware/NVSRAM files.  All firmware/NVSRAM files that are not specified will be removed from the proxy if they exist. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_proxy_firmware_upload_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_proxy_firmware_upload_module.md#id4)

```yaml+jinja
- name: Ensure proxy has the expected firmware versions.
  na_santricity_proxy_firmware_upload:
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    firmware:
      - "path/to/firmware/dlp_files"
      - "path/to/nvsram.dlp"
      - "path/to/firmware.dlp"
```

## [Return Values](na_santricity_proxy_firmware_upload_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Status and version of firmware and NVSRAM.  **Returned:** always |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
