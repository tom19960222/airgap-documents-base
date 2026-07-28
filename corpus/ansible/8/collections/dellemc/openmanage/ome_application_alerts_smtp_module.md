---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_alerts_smtp module – This module allows to configure SMTP or email configurations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_alerts_smtp_module.html
fetched_at: 2026-07-28T02:04:17+00:00
---
# dellemc.openmanage.ome_application_alerts_smtp module – This module allows to configure SMTP or email configurations

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
> see [Requirements](ome_application_alerts_smtp_module.md#ansible-collections-dellemc-openmanage-ome-application-alerts-smtp-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_alerts_smtp`.

New in dellemc.openmanage 4.3.0

- [Synopsis](ome_application_alerts_smtp_module.md#synopsis)
- [Requirements](ome_application_alerts_smtp_module.md#requirements)
- [Parameters](ome_application_alerts_smtp_module.md#parameters)
- [Notes](ome_application_alerts_smtp_module.md#notes)
- [Examples](ome_application_alerts_smtp_module.md#examples)
- [Return Values](ome_application_alerts_smtp_module.md#return-values)

## [Synopsis](ome_application_alerts_smtp_module.md#id1)

- This module allows to configure SMTP or email configurations on OpenManage Enterprise and OpenManage Enterprise Modular.

## [Requirements](ome_application_alerts_smtp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_alerts_smtp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **credentials**  dictionary | The credentials for the SMTP server |
| **password**  string / required | The password to access the SMTP server. |
| **username**  string / required | The username to access the SMTP server. |
| **destination_address**  string / required | The IP address or FQDN of the SMTP destination server. |
| **enable_authentication**  boolean / required | Enable or disable authentication to access the SMTP server.  The *credentials* are mandatory if *enable_authentication* is `True`.  The module will always report change when this is `True`.  **Choices:**   - `false` - `true` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **port_number**  integer | The port number of the SMTP destination server. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **use_ssl**  boolean | Use SSL to connect with the SMTP server.  **Choices:**   - `false` - `true` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_alerts_smtp_module.md#id4)

> **Note:**
>
> - The module will always report change when *enable_authentication* is `True`.
> - Run this module from a system that has direct access to Dell OpenManage Enterprise or OpenManage Enterprise Modular.
> - This module support `check_mode`.

## [Examples](ome_application_alerts_smtp_module.md#id5)

```yaml+jinja
---
- name: Update SMTP destination server configuration with authentication
  dellemc.openmanage.ome_application_alerts_smtp:
    hostname: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    destination_address: "localhost"
    port_number: 25
    use_ssl: true
    enable_authentication: true
    credentials:
      username: "username"
      password: "password"
- name: Update SMTP destination server configuration without authentication
  dellemc.openmanage.ome_application_alerts_smtp:
    hostname: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    destination_address: "localhost"
    port_number: 25
    use_ssl: false
    enable_authentication: false
```

## [Return Values](ome_application_alerts_smtp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to update the SMTP settings because the entered credential is invalid or empty.", "MessageArgs": [], "MessageId": "CAPP1106", "RelatedProperties": [], "Resolution": "Either enter valid credentials or disable the Use Credentials option and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the SMTP settings update.  **Returned:** always  **Sample:** `"Successfully updated the SMTP settings."` |
| **smtp_details**  dictionary | returned when SMTP settings are updated successfully.  **Returned:** success  **Sample:** `{"Credential": {"Password": null, "User": "admin"}, "DestinationAddress": "localhost", "PortNumber": 25, "UseCredentials": true, "UseSSL": false}` |

### Authors

- Sachin Apagundi(@sachin-apa)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
