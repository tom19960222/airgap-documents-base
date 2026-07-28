---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_ldap module – NetApp E-Series manage LDAP integration to use for authentication"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_ldap_module.html
fetched_at: 2026-07-28T00:14:01+00:00
---
# netapp_eseries.santricity.na_santricity_ldap module – NetApp E-Series manage LDAP integration to use for authentication

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_ldap`.

- [Synopsis](na_santricity_ldap_module.md#synopsis)
- [Parameters](na_santricity_ldap_module.md#parameters)
- [Notes](na_santricity_ldap_module.md#notes)
- [Examples](na_santricity_ldap_module.md#examples)
- [Return Values](na_santricity_ldap_module.md#return-values)

## [Synopsis](na_santricity_ldap_module.md#id1)

- Configure an E-Series system to allow authentication via an LDAP server

## [Parameters](na_santricity_ldap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **bind_password**  string | This is the password for the bind user account.  Required when *bind_user* is specified. |
| **bind_user**  string | This is the user account that will be used for querying the LDAP server.  Required when *bind_password* is specified.  Example: CN=MyBindAcct,OU=ServiceAccounts,DC=example,DC=com |
| **group_attributes**  list / elements=string | The user attributes that should be considered for the group to role mapping.  Typically this is used with something like “memberOf”, and a user”s access is tested against group membership or lack thereof.  Default: `["memberOf"]` |
| **identifier**  string | This is a unique identifier for the configuration (for cases where there are multiple domains configured).  Default: `"default"` |
| **names**  list / elements=string | The domain name[s] that will be utilized when authenticating to identify which domain to utilize.  Default to use the DNS name of the *server*.  The only requirement is that the name[s] be resolvable.  Example: [user@example.com](mailto:user%40example.com) |
| **role_mappings**  dictionary | This is where you specify which groups should have access to what permissions for the storage-system.  For example, all users in group A will be assigned all 4 available roles, which will allow access to all the management functionality of the system (super-user). Those in group B only have the storage.monitor role, which will allow only read-only access.  This is specified as a mapping of regular expressions to a list of roles. See the examples.  The roles that will be assigned to to the group/groups matching the provided regex.  storage.admin allows users full read/write access to storage objects and operations.  storage.monitor allows users read-only access to storage objects and operations.  support.admin allows users access to hardware, diagnostic information, the Major Event Log, and other critical support-related functionality, but not the storage configuration.  security.admin allows users access to authentication/authorization configuration, as well as the audit log configuration, and certification management. |
| **search_base**  string | The search base is used to find group memberships of the user.  Example: ou=users,dc=example,dc=com |
| **server_url**  string | This is the LDAP server url.  The connection string should be specified as using the ldap or ldaps protocol along with the port information. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string | When *state==”present”* the defined LDAP domain will be added to the storage system.  When *state==”absent”* the domain specified will be removed from the storage system.  *state==”disabled”* will result in deleting all existing LDAP domains on the storage system.  Choices:   - `"present"` ← (default) - `"absent"` - `"disabled"` |
| **user_attribute**  string | This is the attribute we will use to match the provided username when a user attempts to authenticate.  Default: `"sAMAccountName"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_ldap_module.md#id3)

> **Note:**
>
> - Check mode is supported
> - This module allows you to define one or more LDAP domains identified uniquely by *identifier* to use for authentication. Authorization is determined by *role_mappings*, in that different groups of users may be given different (or no), access to certain aspects of the system and API.
> - The local user accounts will still be available if the LDAP server becomes unavailable/inaccessible.
> - Generally, you”ll need to get the details of your organization”s LDAP server before you”ll be able to configure the system for using LDAP authentication; every implementation is likely to be very different.
> - This API is currently only supported with the Embedded Web Services API v2.0 and higher, or the Web Services Proxy v3.0 and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_ldap_module.md#id4)

```yaml+jinja
- name: Disable LDAP authentication
  na_santricity_ldap:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: absent

- name: Remove the "default" LDAP domain configuration
  na_santricity_ldap:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: absent
    identifier: default

- name: Define a new LDAP domain, utilizing defaults where possible
  na_santricity_ldap:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: enabled
    bind_username: "CN=MyBindAccount,OU=ServiceAccounts,DC=example,DC=com"
    bind_password: "mySecretPass"
    server: "ldap://example.com:389"
    search_base: "OU=Users,DC=example,DC=com"
    role_mappings:
      ".*dist-dev-storage.*":
        - storage.admin
        - security.admin
        - support.admin
        - storage.monitor
```

## [Return Values](na_santricity_ldap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"The ldap settings have been updated."` |

### Authors

- Michael Price (@lmprice)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
