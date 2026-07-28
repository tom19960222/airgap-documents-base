---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_syslog module – NetApp E-Series manage syslog settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_syslog_module.html
fetched_at: 2026-07-28T02:44:21+00:00
---
# netapp_eseries.santricity.na_santricity_syslog module – NetApp E-Series manage syslog settings

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_syslog`.

- [Synopsis](na_santricity_syslog_module.md#synopsis)
- [Parameters](na_santricity_syslog_module.md#parameters)
- [Notes](na_santricity_syslog_module.md#notes)
- [Examples](na_santricity_syslog_module.md#examples)
- [Return Values](na_santricity_syslog_module.md#return-values)

## [Synopsis](na_santricity_syslog_module.md#id1)

- Allow the syslog settings to be configured for an individual E-Series storage-system

## [Parameters](na_santricity_syslog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The syslog server’s IPv4 address or a fully qualified hostname.  All existing syslog configurations will be removed when *state=absent* and *address=None*. |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **components**  list / elements=string | The e-series logging components define the specific logs to transfer to the syslog server.  At the time of writing, ‘auditLog’ is the only logging component but more may become available.  **Default:** `["auditLog"]` |
| **port**  integer | This is the port the syslog server is using.  **Default:** `514` |
| **protocol**  string | This is the transmission protocol the syslog server’s using to receive syslog messages.  **Choices:**   - `"udp"` ← (default) - `"tcp"` - `"tls"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **state**  string | Add or remove the syslog server configuration for E-Series storage array.  Existing syslog server configuration will be removed or updated when its address matches *address*.  Fully qualified hostname that resolve to an IPv4 address that matches *address* will not be treated as a match.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **test**  boolean | This forces a test syslog message to be sent to the stated syslog server.  Only attempts transmission when *state=present*.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_syslog_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - This API is currently only supported with the Embedded Web Services API v2.12 (bundled with SANtricity OS 11.40.2) and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_syslog_module.md#id4)

```yaml+jinja
- name: Add two syslog server configurations to NetApp E-Series storage array.
  na_santricity_syslog:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: present
    address: "{{ item }}"
    port: 514
    protocol: tcp
    component: "auditLog"
  loop:
    - "192.168.1.1"
    - "192.168.1.100"
```

## [Return Values](na_santricity_syslog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** on success  **Sample:** `"The settings have been updated."` |
| **syslog**  boolean | True if syslog server configuration has been added to e-series storage array.  **Returned:** on success  **Sample:** `true` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
