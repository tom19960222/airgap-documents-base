---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_alerts module – NetApp E-Series manage email notification settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_alerts_module.html
fetched_at: 2026-07-28T00:13:50+00:00
---
# netapp_eseries.santricity.na_santricity_alerts module – NetApp E-Series manage email notification settings

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_alerts`.

- [Synopsis](na_santricity_alerts_module.md#synopsis)
- [Parameters](na_santricity_alerts_module.md#parameters)
- [Notes](na_santricity_alerts_module.md#notes)
- [Examples](na_santricity_alerts_module.md#examples)
- [Return Values](na_santricity_alerts_module.md#return-values)

## [Synopsis](na_santricity_alerts_module.md#id1)

- Certain E-Series systems have the capability to send email notifications on potentially critical events.
- This module will allow the owner of the system to specify email recipients for these messages.

## [Parameters](na_santricity_alerts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **contact**  string | Allows the owner to specify some free-form contact information to be included in the emails.  This is typically utilized to provide a contact phone number. |
| **recipients**  list / elements=string | The email addresses that will receive the email notifications.  Required when *state=enabled*. |
| **sender**  string | This is the sender that the recipient will see. It doesn’t necessarily need to be a valid email account.  Required when *state=enabled*. |
| **server**  string | A fully qualified domain name, IPv4 address, or IPv6 address of a mail server.  To use a fully qualified domain name, you must configure a DNS server on both controllers using **ERROR while parsing**: While parsing M() at index 97: Module name “na_santricity_mgmt_interface” is not a FQCN. - Required when *state=enabled*. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string | Enable/disable the sending of email-based alerts.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **test**  boolean | When a change is detected in the configuration, a test email will be sent.  This may take a few minutes to process.  Only applicable if *state=enabled*.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_alerts_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - Alertable messages are a subset of messages shown by the Major Event Log (MEL), of the storage-system. Examples of alertable messages include drive failures, failed controllers, loss of redundancy, and other warning/critical events.
> - This API is currently only supported with the Embedded Web Services API v2.0 and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_alerts_module.md#id4)

```yaml+jinja
- name: Enable email-based alerting
  na_santricity_alerts:
    state: enabled
    sender: noreply@example.com
    server: mail@example.com
    contact: "Phone: 1-555-555-5555"
    recipients:
        - name1@example.com
        - name2@example.com
    api_url: "10.1.1.1:8443"
    api_username: "admin"
    api_password: "myPass"

- name: Disable alerting
  na_santricity_alerts:
    state: disabled
    api_url: "10.1.1.1:8443"
    api_username: "admin"
    api_password: "myPass"
```

## [Return Values](na_santricity_alerts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"The settings have been updated."` |

### Authors

- Michael Price (@lmprice)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
