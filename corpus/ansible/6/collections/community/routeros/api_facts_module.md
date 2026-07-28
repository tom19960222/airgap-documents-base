---
collection: ansible
version: "6"
title: "community.routeros.api_facts module – Collect facts from remote devices running MikroTik RouterOS using the API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/routeros/api_facts_module.html
fetched_at: 2026-07-27T17:20:52+00:00
---
# community.routeros.api_facts module – Collect facts from remote devices running MikroTik RouterOS using the API

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/community/routeros) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
> You need further requirements to be able to use this module,
> see [Requirements](api_facts_module.md#ansible-collections-community-routeros-api-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `community.routeros.api_facts`.

New in community.routeros 2.1.0

- [Synopsis](api_facts_module.md#synopsis)
- [Requirements](api_facts_module.md#requirements)
- [Parameters](api_facts_module.md#parameters)
- [Attributes](api_facts_module.md#attributes)
- [See Also](api_facts_module.md#see-also)
- [Examples](api_facts_module.md#examples)
- [Returned Facts](api_facts_module.md#returned-facts)

## [Synopsis](api_facts_module.md#id1)

- Collects a base set of device facts from a remote device that is running RouterOS. This module prepends all of the base network fact keys with `ansible_net_<fact>`. The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.
- As opposed to the [community.routeros.facts](facts_module.md#ansible-collections-community-routeros-facts-module) module, it uses the RouterOS API, similar to the [community.routeros.api](api_module.md#ansible-collections-community-routeros-api-module) module.

## [Requirements](api_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- librouteros
- Python >= 3.6 (for librouteros)

## [Parameters](api_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in community.routeros 1.2.0 | PEM formatted file that contains a CA certificate to be used for certificate validation.  See also *validate_cert_hostname*. Only used when *tls=true* and *validate_certs=true*. |
| **encoding**  string  added in community.routeros 2.1.0 | Use the specified encoding when communicating with the RouterOS device.  Default is `ASCII`. Note that `UTF-8` requires librouteros 3.2.1 or newer.  Default: `"ASCII"` |
| **force_no_cert**  boolean  added in community.routeros 2.4.0 | Set to `true` to connect without a certificate when *tls=true*.  See also *validate_certs*.  **Note:** this forces the use of anonymous Diffie-Hellman (ADH) ciphers. The protocol is susceptible to Man-in-the-Middle attacks, because the keys used in the exchange are not authenticated. Instead of simply connecting without a certificate to “make things work” have a look at *validate_certs* and *ca_path*.  Choices:   - `false` ← (default) - `true` |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include `all`, `hardware`, `interfaces`, and `routing`.  Can specify a list of values to include a larger subset. Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Default: `["all"]` |
| **hostname**  string / required | RouterOS hostname API. |
| **password**  string / required | RouterOS user password. |
| **port**  integer | RouterOS api port. If *tls* is set, port will apply to TLS/SSL connection.  Defaults are `8728` for the HTTP API, and `8729` for the HTTPS API. |
| **timeout**  integer  added in community.routeros 2.3.0 | Timeout for the request.  Default: `10` |
| **tls**  aliases: ssl  boolean | If is set TLS will be used for RouterOS API connection.  Choices:   - `false` ← (default) - `true` |
| **username**  string / required | RouterOS login user. |
| **validate_cert_hostname**  boolean  added in community.routeros 1.2.0 | Set to `true` to validate hostnames in certificates.  See also *validate_certs*. Only used when *tls=true* and *validate_certs=true*.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean  added in community.routeros 1.2.0 | Set to `false` to skip validation of TLS certificates.  See also *validate_cert_hostname*. Only used when *tls=true*.  **Note:** instead of simply deactivating certificate validations to “make things work”, please consider creating your own CA certificate and using it to sign certificates used for your router. You can tell the module about your CA certificate with the *ca_path* option.  Choices:   - `false` - `true` ← (default) |

## [Attributes](api_facts_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.routeros.api | Use `group/community.routeros.api` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts. |
| **platform** | Platform: RouterOS | Target OS/families that can be operated against. |

## [See Also](api_facts_module.md#id5)

> **See also:**
>
> [community.routeros.facts](facts_module.md#ansible-collections-community-routeros-facts-module)
> :   Collect facts from remote devices running MikroTik RouterOS.
>
> [community.routeros.api](api_module.md#ansible-collections-community-routeros-api-module)
> :   Ansible module for RouterOS API.
>
> [community.routeros.api_find_and_modify](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module)
> :   Find and modify information using the API.
>
> [community.routeros.api_info](api_info_module.md#ansible-collections-community-routeros-api-info-module)
> :   Retrieve information from API.
>
> [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module)
> :   Modify data at paths with API.
>
> [How to connect to RouterOS devices with the RouterOS API](docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide)
> :   How to connect to RouterOS devices with the RouterOS API

## [Examples](api_facts_module.md#id6)

```yaml+jinja
- name: Collect all facts from the device
  community.routeros.api_facts:
    hostname: 192.168.88.1
    username: admin
    password: password
    gather_subset: all

- name: Do not collect hardware facts
  community.routeros.api_facts:
    hostname: 192.168.88.1
    username: admin
    password: password
    gather_subset:
      - "!hardware"
```

## [Returned Facts](api_facts_module.md#id7)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_net_all_ipv4_addresses**  list / elements=string | All IPv4 addresses configured on the device.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_all_ipv6_addresses**  list / elements=string | All IPv6 addresses configured on the device.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_arch**  string | The CPU architecture of the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_bgp_instance**  dictionary | A dictionary with BGP instance information.  Returned: *gather_subset* contains `routing` |
| **ansible_net_bgp_peer**  dictionary | A dictionary with BGP peer information.  Returned: *gather_subset* contains `routing` |
| **ansible_net_bgp_vpnv4_route**  dictionary | A dictionary with BGP vpnv4 route information.  Returned: *gather_subset* contains `routing` |
| **ansible_net_cpu_load**  string | Current CPU load.  Returned: *gather_subset* contains `default` |
| **ansible_net_gather_subset**  list / elements=string | The list of fact subsets collected from the device.  Returned: always |
| **ansible_net_hostname**  string | The configured hostname of the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_interfaces**  dictionary | A hash of all interfaces running on the system.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_memfree_mb**  integer | The available free memory on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_memtotal_mb**  integer | The total memory on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_model**  string | The model name returned from the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_neighbors**  dictionary | The list of neighbors from the remote device.  Returned: *gather_subset* contains `interfaces` |
| **ansible_net_ospf_instance**  dictionary | A dictionary with OSPF instances.  Returned: *gather_subset* contains `routing` |
| **ansible_net_ospf_neighbor**  dictionary | A dictionary with OSPF neighbors.  Returned: *gather_subset* contains `routing` |
| **ansible_net_route**  dictionary | A dictionary for routes in all routing tables.  Returned: *gather_subset* contains `routing` |
| **ansible_net_serialnum**  string | The serial number of the remote device.  Returned: *gather_subset* contains `default` |
| **ansible_net_spacefree_mb**  dictionary | The available disk space on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_spacetotal_mb**  dictionary | The total disk space on the remote device in MiB.  Returned: *gather_subset* contains `hardware` |
| **ansible_net_uptime**  string | The uptime of the device.  Returned: *gather_subset* contains `default` |
| **ansible_net_version**  string | The operating system version running on the remote device.  Returned: *gather_subset* contains `default` |

### Authors

- Egor Zaitsev (@heuels)
- Nikolay Dachev (@NikolayDachev)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.routeros)
[Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-routeros)
