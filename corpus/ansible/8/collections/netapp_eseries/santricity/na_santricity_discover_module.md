---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_discover module – NetApp E-Series discover E-Series storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_discover_module.html
fetched_at: 2026-07-28T02:44:07+00:00
---
# netapp_eseries.santricity.na_santricity_discover module – NetApp E-Series discover E-Series storage systems

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
> You need further requirements to be able to use this module,
> see [Requirements](na_santricity_discover_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-discover-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_discover`.

- [Synopsis](na_santricity_discover_module.md#synopsis)
- [Requirements](na_santricity_discover_module.md#requirements)
- [Parameters](na_santricity_discover_module.md#parameters)
- [Notes](na_santricity_discover_module.md#notes)
- [Examples](na_santricity_discover_module.md#examples)
- [Return Values](na_santricity_discover_module.md#return-values)

## [Synopsis](na_santricity_discover_module.md#id1)

- Module searches a subnet range and returns any available E-Series storage systems.

## [Requirements](na_santricity_discover_module.md#id2)

The below requirements are needed on the host that executes this module.

- ipaddress

## [Parameters](na_santricity_discover_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ports**  list / elements=string | This option specifies which ports to be tested during the discovery process.  The first usable port will be used in the returned API url.  **Default:** `[8443]` |
| **prefer_embedded**  boolean | Give preference to Web Services Embedded when an option exists for both Web Services Proxy and Embedded.  Web Services Proxy will be utilized when available by default.  **Choices:**   - `false` ← (default) - `true` |
| **proxy_password**  string | Web Service Proxy user password |
| **proxy_url**  string | Web Services Proxy REST API URL. Example <https://192.168.1.100:8443/devmgr/v2/> |
| **proxy_username**  string | Web Service Proxy username |
| **proxy_validate_certs**  boolean | Whether to validate Web Service Proxy SSL certificate  **Choices:**   - `false` - `true` ← (default) |
| **subnet_mask**  string / required | This is the IPv4 search range for discovering E-Series storage arrays.  IPv4 subnet mask specified in CIDR form. Example 192.168.1.0/24 would search the range 192.168.1.0 to 192.168.1.255.  Be sure to include all management paths in the search range. |

## [Notes](na_santricity_discover_module.md#id4)

> **Note:**
>
> - Only available for platforms E2800 or later (SANtricity Web Services Embedded REST API must be available).
> - All E-Series storage systems with SANtricity version 11.62 or later will be discovered.
> - Only E-Series storage systems without a set admin password running SANtricity versions prior to 11.62 will be discovered.
> - Use SANtricity Web Services Proxy to discover all systems regardless of SANricity version or password.

## [Examples](na_santricity_discover_module.md#id5)

```yaml+jinja
- name: Discover all E-Series storage systems on the network.
  na_santricity_discover:
    subnet_mask: 192.168.1.0/24
```

## [Return Values](na_santricity_discover_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **systems_found**  dictionary | Success message  **Returned:** on success  **Sample:** `"{\"012341234123\": { \"addresses\": [\"192.168.1.184\", \"192.168.1.185\"], \"api_urls\": [\"https://192.168.1.184:8443/devmgr/v2/\", \"https://192.168.1.185:8443/devmgr/v2/\"], \"label\": \"ExampleArray01\", \"proxy_ssid: \"\", \"proxy_required\": false}, \"012341234567\": { \"addresses\": [\"192.168.1.23\", \"192.168.1.24\"], \"api_urls\": [\"https://192.168.1.100:8443/devmgr/v2/\"], \"label\": \"ExampleArray02\", \"proxy_ssid\": \"array_ssid\", \"proxy_required\": true}}"` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
