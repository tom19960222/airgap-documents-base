---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_grid_identity_federation module – NetApp StorageGRID manage Grid identity federation."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_grid_identity_federation_module.html
fetched_at: 2026-07-28T02:43:51+00:00
---
# netapp.storagegrid.na_sg_grid_identity_federation module – NetApp StorageGRID manage Grid identity federation.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/ui/repo/published/netapp/storagegrid/) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_identity_federation`.

New in netapp.storagegrid 21.6.0

- [Synopsis](na_sg_grid_identity_federation_module.md#synopsis)
- [Parameters](na_sg_grid_identity_federation_module.md#parameters)
- [Notes](na_sg_grid_identity_federation_module.md#notes)
- [Examples](na_sg_grid_identity_federation_module.md#examples)
- [Return Values](na_sg_grid_identity_federation_module.md#return-values)

## [Synopsis](na_sg_grid_identity_federation_module.md#id1)

- Configure Grid Identity Federation within NetApp StorageGRID.
- If module is run with *check_mode*, a connectivity test will be performed using the supplied values without changing the configuration.
- This module is idempotent if *password* is not specified.

## [Parameters](na_sg_grid_identity_federation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **base_group_dn**  string | The Distinguished Name of the LDAP subtree to search for groups. |
| **base_user_dn**  string | The Distinguished Name of the LDAP subtree to search for users. |
| **ca_cert**  string | Custom certificate used to connect to the LDAP server.  If a custom certificate is not supplied, the operating system CA certificate will be used. |
| **hostname**  string | The hostname or IP address of the LDAP server. |
| **ldap_group_id_attribute**  string | The LDAP attribute which contains the group for a user.  Should be configured if *ldap_service_type=Other*. |
| **ldap_group_uuid_attribute**  string | The LDAP attribute which contains the group’s permanent unique identity.  Should be configured if *ldap_service_type=Other*. |
| **ldap_service_type**  string | The type of LDAP server.  **Choices:**   - `"Active Directory"` - `"OpenLDAP"` - `"Other"` |
| **ldap_user_id_attribute**  string | The LDAP attribute which contains the unique user name of a user.  Should be configured if *ldap_service_type=Other*. |
| **ldap_user_uuid_attribute**  string | The LDAP attribute which contains the permanent unique identity of a user.  Should be configured if *ldap_service_type=Other*. |
| **password**  string | The password associated with the username. |
| **port**  integer | The port used to connect to the LDAP server. Typically 389 for LDAP, or 636 for LDAPS. |
| **state**  string | Whether identity federation should be enabled or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tls**  string | Whether Transport Layer Security is used to connect to the LDAP server.  **Choices:**   - `"STARTTLS"` ← (default) - `"LDAPS"` - `"Disabled"` |
| **type**  string | The type of identity source.  Default is `ldap`.  **Default:** `"ldap"` |
| **username**  string | The username to bind to the LDAP server. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_identity_federation_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_identity_federation_module.md#id4)

```yaml+jinja
- name: test identity federation configuration
  netapp.storagegrid.na_sg_grid_identity_federation:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    ldap_service_type: "Active Directory"
    hostname: "ad.example.com"
    port: 389
    username: "binduser"
    password: "bindpass"
    base_group_dn: "DC=example,DC=com"
    base_user_dn: "DC=example,DC=com"
    tls: "Disabled"
  check_mode: yes

- name: configure identity federation with AD and TLS
  netapp.storagegrid.na_sg_grid_identity_federation:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    ldap_service_type: "Active Directory"
    hostname: "ad.example.com"
    port: 636
    username: "binduser"
    password: "bindpass"
    base_group_dn: "DC=example,DC=com"
    base_user_dn: "DC=example,DC=com"
    tls: "LDAPS"
    ca_cert: |
        -----BEGIN CERTIFICATE-----
        MIIC+jCCAeICCQDmn9Gow08LTzANBgkqhkiG9w0BAQsFADA/..swCQYDVQQGEwJV
        bXBsZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB..JFzNIXQEGnsgjV
        JGU4giuvOLOZ8Q3gyuUbkSUQDjmjpMR8PliwJ6iW2Ity89Dv..dl1TaIYI/ansyZ
        Uxk4YXeN6kUkrDtNxCg1McALzXVAfxMTtj2SFlLxne4Z6rX2..UyftQrfM13F1vY
        gK8dBPz+l+X/Uozo/xNm7gxe68p9le9/pcULst1CQn5/sPqq..kgWcSvlKUItu82
        lq3B2169rovdIaNdcvaQjMPhrDGo5rvLfMN35U3Hgbz41PL5..x2BcUE6/0ab5T4
        qKBxKa3t9twj+zpUqOzyL0PFfCE+SK5fEXAS1ow4eAcLN+eB..gR/PuvGAyIPCtE
        1+X4GrECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAFpO+04Ra..FMJPH6dBmzfb7l
        k04BWTvSlur6HiQdXY+oFQMJZzyI7MQ8v9HBIzS0ZAzYWLp4..VZhHmRxnrWyxVs
        u783V5YfQH2L4QnBDoiDefgxyfDs2PcoF5C+X9CGXmPqzst2..y/6tdOVJzdiA==
        -----END CERTIFICATE-----
```

## [Return Values](na_sg_grid_identity_federation_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID management identity source configuration.  **Returned:** success  **Sample:** `{"baseGroupDn": "DC=example,DC=com", "baseUserDn": "DC=example,DC=com", "caCert": "-----BEGIN CERTIFICATE----- abcdefghijkl123456780ABCDEFGHIJKL 123456/7890ABCDEFabcdefghijklABCD -----END CERTIFICATE----- ", "disable": false, "disableTLS": false, "enableLDAPS": false, "hostname": "10.1.2.3", "id": "00000000-0000-0000-0000-000000000000", "ldapServiceType": "Active Directory", "password": "********", "port": 389, "type": "ldap", "username": "MYDOMAIN\\Administrator"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
