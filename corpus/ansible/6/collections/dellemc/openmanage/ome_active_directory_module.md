---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_active_directory module – Configure Active Directory groups to be used with Directory Services on OpenManage Enterprise and OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_active_directory_module.html
fetched_at: 2026-07-27T17:25:22+00:00
---
# dellemc.openmanage.ome_active_directory module – Configure Active Directory groups to be used with Directory Services on OpenManage Enterprise and OpenManage Enterprise Modular

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_active_directory_module.md#ansible-collections-dellemc-openmanage-ome-active-directory-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_active_directory`.

New in dellemc.openmanage 4.0.0

- [Synopsis](ome_active_directory_module.md#synopsis)
- [Requirements](ome_active_directory_module.md#requirements)
- [Parameters](ome_active_directory_module.md#parameters)
- [Notes](ome_active_directory_module.md#notes)
- [Examples](ome_active_directory_module.md#examples)
- [Return Values](ome_active_directory_module.md#return-values)

## [Synopsis](ome_active_directory_module.md#id1)

- This module allows to add, modify, and delete OpenManage Enterprise connection with Active Directory Service.

## [Requirements](ome_active_directory_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_active_directory_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **certificate_file**  path | Provide the full path of the SSL certificate.  The certificate should be a Root CA Certificate encoded in Base64 format.  This is applicable when *validate_certificate* is `yes`. |
| **domain_controller_lookup**  string | Select the Domain Controller Lookup method.  Choices:   - `"DNS"` ← (default) - `"MANUAL"` |
| **domain_controller_port**  integer | Domain controller port.  By default, Global Catalog Address port number 3269 is populated.  For the Domain Controller Access, enter 636 as the port number.  `NOTE`, Only LDAPS ports are supported.  Default: `3269` |
| **domain_password**  string | Provide the domain password.  This is applicable when *test_connection* is `yes`. |
| **domain_server**  list / elements=string | Enter the domain name or FQDN or IP address of the domain controller.  If *domain_controller_lookup* is `DNS`, enter the domain name to query DNS for the domain controllers.  If *domain_controller_lookup* is `MANUAL`, enter the FQDN or the IP address of the domain controller. The maximum number of Active Directory servers that can be added is three. |
| **domain_username**  string | Provide the domain username either in the UPN ([username@domain](mailto:username%40domain)) or NetBIOS (domain\\username) format.  This is applicable when *test_connection* is `yes`. |
| **group_domain**  string | Provide the group domain in the format `example.com` or `ou=org, dc=example, dc=com`. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **id**  integer | Provide the ID of the existing Active Directory service connection.  This is applicable for modification and deletion.  This is mutually exclusive with *name*. |
| **name**  string | Provide a name for the Active Directory connection.  This is applicable for creation and deletion.  This is mutually exclusive with *name*. |
| **network_timeout**  integer | Enter the network timeout duration in seconds.  The supported timeout duration range is 15 to 300 seconds.  Default: `120` |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **search_timeout**  integer | Enter the search timeout duration in seconds.  The supported timeout duration range is 15 to 300 seconds.  Default: `120` |
| **state**  string | `present` allows to create or modify an Active Directory service.  `absent` allows to delete a Active Directory service.  Choices:   - `"present"` ← (default) - `"absent"` |
| **test_connection**  boolean | Enables testing the connection to the domain controller.  The connection to the domain controller is tested with the provided Active Directory service details.  If test fails, module will error out.  If `yes`, *domain_username* and *domain_password* has to be provided.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certificate**  boolean | Enables validation of SSL certificate of the domain controller.  The module will always report change when this is `yes`.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_active_directory_module.md#id4)

> **Note:**
>
> - The module will always report change when *validate_certificate* is `yes`.
> - Run this module from a system that has direct access to OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_active_directory_module.md#id5)

```yaml+jinja
---
- name: Add Active Directory service using DNS lookup along with the test connection
  dellemc.openmanage.ome_active_directory:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: my_ad1
    domain_server:
      - domainname.com
    group_domain: domainname.com
    test_connection: yes
    domain_username: user@domainname
    domain_password: domain_password

- name: Add Active Directory service using IP address of the domain controller with certificate validation
  dellemc.openmanage.ome_active_directory:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: my_ad2
    domain_controller_lookup: MANUAL
    domain_server:
      - 192.68.20.181
    group_domain: domainname.com
    validate_certificate: yes
    certificate_file: "/path/to/certificate/file.cer"

- name: Modify domain controller IP address, network_timeout and group_domain
  dellemc.openmanage.ome_active_directory:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: my_ad2
    domain_controller_lookup: MANUAL
    domain_server:
      - 192.68.20.189
    group_domain: newdomain.in
    network_timeout: 150

- name: Delete Active Directory service
  dellemc.openmanage.ome_active_directory:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: my_ad2
    state: absent

- name: Test connection to existing Active Directory service with certificate validation
  dellemc.openmanage.ome_active_directory:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    name: my_ad2
    test_connection: yes
    domain_username: user@domainname
    domain_password: domain_password
    validate_certificate: yes
    certificate_file: "/path/to/certificate/file.cer"
```

## [Return Values](ome_active_directory_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **active_directory**  dictionary | The Active Directory that was added, modified or deleted by this module.  Returned: on change  Sample: `{"CertificateValidation": false, "DnsServer": [], "GroupDomain": "dellemcdomain.com", "Id": 21789, "Name": "ad_test", "NetworkTimeOut": 120, "Password": null, "SearchTimeOut": 120, "ServerName": ["192.168.20.181"], "ServerPort": 3269, "ServerType": "MANUAL"}` |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error_info": {"error": {"@Message.ExtendedInfo": [{"Message": "Unable to connect to the LDAP or AD server because the entered credentials are invalid.", "MessageArgs": [], "MessageId": "CSEC5002", "RelatedProperties": [], "Resolution": "Make sure the server input configuration are valid and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}}` |
| **msg**  string | Overall status of the Active Directory operation.  Returned: always  Sample: `"Successfully renamed the slot(s)."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
