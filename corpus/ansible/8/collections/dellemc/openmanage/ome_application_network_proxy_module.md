---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_network_proxy module – Updates the proxy configuration on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_network_proxy_module.html
fetched_at: 2026-07-28T02:04:21+00:00
---
# dellemc.openmanage.ome_application_network_proxy module – Updates the proxy configuration on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_application_network_proxy_module.md#ansible-collections-dellemc-openmanage-ome-application-network-proxy-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_network_proxy`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_application_network_proxy_module.md#synopsis)
- [Requirements](ome_application_network_proxy_module.md#requirements)
- [Parameters](ome_application_network_proxy_module.md#parameters)
- [Notes](ome_application_network_proxy_module.md#notes)
- [Examples](ome_application_network_proxy_module.md#examples)
- [Return Values](ome_application_network_proxy_module.md#return-values)

## [Synopsis](ome_application_network_proxy_module.md#id1)

- This module allows to configure a network proxy on OpenManage Enterprise.

## [Requirements](ome_application_network_proxy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_network_proxy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **enable_authentication**  boolean | Enable or disable proxy authentication.  If *enable_authentication* is true, *proxy_username* and *proxy_password* must be provided.  If *enable_authentication* is false, the proxy username and password are set to its default values.  **Choices:**   - `false` - `true` |
| **enable_proxy**  boolean / required | Enables or disables the HTTP proxy configuration.  If *enable proxy* is false, then the HTTP proxy configuration is set to its default value.  **Choices:**   - `false` - `true` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **ip_address**  string | Proxy server address.  This option is mandatory when *enable_proxy* is true. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **proxy_password**  string | Proxy server password.  This option is mandatory when *enable_authentication* is true. |
| **proxy_port**  integer | Proxy server’s port number.  This option is mandatory when *enable_proxy* is true. |
| **proxy_username**  string | Proxy server username.  This option is mandatory when *enable_authentication* is true. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_network_proxy_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module does not support `check_mode`.

## [Examples](ome_application_network_proxy_module.md#id5)

```yaml+jinja
---
- name: Update proxy configuration and enable authentication
  dellemc.openmanage.ome_application_network_proxy:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_proxy: true
    ip_address: "192.168.0.2"
    proxy_port: 444
    enable_authentication: true
    proxy_username: "proxy_username"
    proxy_password: "proxy_password"

- name: Reset proxy authentication
  dellemc.openmanage.ome_application_network_proxy:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_proxy: true
    ip_address: "192.168.0.2"
    proxy_port: 444
    enable_authentication: false

- name: Reset proxy configuration
  dellemc.openmanage.ome_application_network_proxy:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_proxy: false
```

## [Return Values](ome_application_network_proxy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because the input value for  PortNumber  is missing or an invalid value is entered.", "MessageArgs": ["PortNumber"], "MessageId": "CGEN6002", "RelatedProperties": [], "Resolution": "Enter a valid value and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the network proxy configuration change.  **Returned:** always  **Sample:** `"Successfully updated network proxy configuration."` |
| **proxy_configuration**  dictionary | Updated application network proxy configuration.  **Returned:** success  **Sample:** `{"EnableAuthentication": true, "EnableProxy": true, "IpAddress": "192.168.0.2", "Password": null, "PortNumber": 444, "Username": "root"}` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
