---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_proxy_systems module – NetApp E-Series manage SANtricity web services proxy storage arrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_proxy_systems_module.html
fetched_at: 2026-07-28T00:14:06+00:00
---
# netapp_eseries.santricity.na_santricity_proxy_systems module – NetApp E-Series manage SANtricity web services proxy storage arrays

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_proxy_systems`.

- [Synopsis](na_santricity_proxy_systems_module.md#synopsis)
- [Parameters](na_santricity_proxy_systems_module.md#parameters)
- [Notes](na_santricity_proxy_systems_module.md#notes)
- [Examples](na_santricity_proxy_systems_module.md#examples)
- [Return Values](na_santricity_proxy_systems_module.md#return-values)

## [Synopsis](na_santricity_proxy_systems_module.md#id1)

- Manage the arrays accessible via a NetApp Web Services Proxy for NetApp E-series storage arrays.

## [Parameters](na_santricity_proxy_systems_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_certificate**  boolean | Accept the storage system’s certificate automatically even when it is self-signed.  Use **ERROR while parsing**: While parsing M() at index 5: Module name “na_santricity_certificates” is not a FQCN to add certificates to SANtricity Web Services Proxy.  SANtricity Web Services Proxy will fail to add any untrusted storage system.  Choices:   - `false` - `true` ← (default) |
| **add_discovered_systems**  boolean | This flag will force all discovered storage systems to be added to SANtricity Web Services Proxy.  Choices:   - `false` ← (default) - `true` |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **password**  string | Default storage system password which will be used anytime when password has not been provided in the *systems* sub-options.  The storage system admin password will be set on the device itself with the provided admin password if it is not set. |
| **subnet_mask**  string | This is the IPv4 search range for discovering E-Series storage arrays.  IPv4 subnet mask specified in CIDR form. Example 192.168.1.0/24 would search the range 192.168.1.0 to 192.168.1.255.  Be sure to include all management paths in the search range. |
| **systems**  list / elements=string | List of storage system information which defines which systems should be added on SANtricity Web Services Proxy.  Accepts a simple serial number list or list of dictionary containing at minimum the serial or addresses key from the sub-option list.  Note that the serial number will be used as the storage system identifier when an identifier is not specified.  When *add_discovered_systems == False* and any system serial number not supplied that is discovered will be removed from the proxy.  Default: `[]` |
| **addresses**  list / elements=string | List of storage system’s IPv4 addresses.  Mutually exclusive with the sub-option serial. |
| **password**  string | This is the storage system admin password.  When not provided *default_password* will be used.  The storage system admin password will be set on the device itself with the provided admin password if it is not set. |
| **serial**  string | Storage system’s serial number which can be located on the top of every NetApp E-Series enclosure.  Include any leading zeros.  Mutually exclusive with the sub-option address. |
| **ssid**  string | This is the Web Services Proxy’s identifier for a storage system.  When ssid is not specified then either the serial or first controller IPv4 address will be used instead. |
| **tags**  dictionary | Optional meta tags to associate to the storage system |
| **tags**  dictionary | Default meta tags to associate with all storage systems if not otherwise specified in *systems* sub-options. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_proxy_systems_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_proxy_systems_module.md#id4)

```yaml+jinja
---
    - name: Add storage systems to SANtricity Web Services Proxy
      na_santricity_proxy_systems:
        api_url: "https://192.168.1.100:8443/devmgr/v2"
        api_username: "admin"
        api_password: "adminpass"
        validate_certs: true
        subnet_mask: 192.168.1.0/24
        password: password
        tags:
          tag: value
        accept_certificate: True
        systems:
          - ssid: "system1"
            serial: "056233035640"
            password: "asecretpassword"
            tags:
                use: corporate
                location: sunnyvale
          - ssid: "system2"
            addresses:
                - 192.168.1.100
                - 192.168.2.100     # Second is not be required. It will be discovered
            password: "anothersecretpassword"
          - serial: "021324673799"
          - "021637323454"
    - name: Add storage system to SANtricity Web Services Proxy with serial number list only. The serial numbers will be used to identify each system.
      na_santricity_proxy_systems:
        api_url: "https://192.168.1.100:8443/devmgr/v2"
        api_username: "admin"
        api_password: "adminpass"
        validate_certs: true
        subnet_mask: 192.168.1.0/24
        password: password
        accept_certificate: True
        systems:
          - "1144FG123018"
          - "721716500123"
          - "123540006043"
          - "112123001239"
    - name: Add all discovered storage system to SANtricity Web Services Proxy found in the IP address range 192.168.1.0 to 192.168.1.255.
      na_santricity_proxy_systems:
        api_url: "https://192.168.1.100:8443/devmgr/v2"
        api_username: "admin"
        api_password: "adminpass"
        validate_certs: true
        add_discovered_systems: True
        subnet_mask: 192.168.1.0/24
        password: password
        accept_certificate: True
```

## [Return Values](na_santricity_proxy_systems_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Description of actions performed.  Returned: always  Sample: `"Storage systems [system1, system2, 1144FG123018, 721716500123, 123540006043, 112123001239] were added."` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
