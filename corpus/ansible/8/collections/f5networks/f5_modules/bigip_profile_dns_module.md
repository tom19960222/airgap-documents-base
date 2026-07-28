---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_dns module – Manage DNS profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_dns_module.html
fetched_at: 2026-07-28T02:06:58+00:00
---
# f5networks.f5_modules.bigip_profile_dns module – Manage DNS profiles on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_dns`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_dns_module.md#synopsis)
- [Parameters](bigip_profile_dns_module.md#parameters)
- [Notes](bigip_profile_dns_module.md#notes)
- [Examples](bigip_profile_dns_module.md#examples)
- [Return Values](bigip_profile_dns_module.md#return-values)

## [Synopsis](bigip_profile_dns_module.md#id1)

- Manage DNS profiles on a BIG-IP. There are many DNS profiles options, each with their own adjustments to the standard `dns` profile. Users of this module should be aware that many of the configurable options have no module default. Instead, the default is assigned by the BIG-IP system itself which, in most cases, is acceptable.

## [Parameters](bigip_profile_dns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cache_name**  string | Specifies the user-created cache the system uses to cache DNS responses.  When you select a cache for the system to use, you must also set `enable_dns_cache` to `true` |
| **enable_cache**  boolean | Specifies whether the system caches DNS responses.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  When `true`, the BIG-IP system caches DNS responses handled by the virtual servers associated with this profile. When you enable this setting, you must also specify a value for `cache_name`.  When `false`, the BIG-IP system does not cache DNS responses handled by the virtual servers associated with this profile. However, the profile retains the association with the DNS cache in the `cache_name` parameter. Disable this setting when you want to debug the system.  **Choices:**   - `false` - `true` |
| **enable_dns_express**  boolean | Specifies whether the DNS Express engine is enabled.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The DNS Express engine receives zone transfers from the authoritative DNS server for the zone. If the `enable_zone_transfer` setting is also `true` on this profile, the DNS Express engine also responds to zone transfer requests made by the nameservers configured as zone transfer clients for the DNS Express zone.  **Choices:**   - `false` - `true` |
| **enable_dns_firewall**  boolean | Specifies whether the DNS firewall is enabled.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **enable_dnssec**  boolean | Specifies whether the system signs responses with DNSSEC keys and replies to DNSSEC specific queries (for example, DNSKEY query type).  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **enable_gtm**  boolean | Specifies whether the system uses Global Traffic Manager (now BIG-IP DNS) to manage the response.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **enable_zone_transfer**  boolean | Specifies whether the system answers zone transfer requests for a DNS zone created on the system.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The `enable_dns_express` and `enable_zone_transfer` settings on a DNS profile affect how the system responds to zone transfer requests.  When the `enable_dns_express` and `enable_zone_transfer` settings are both `true`, if a zone transfer request matches a DNS Express zone, DNS Express answers the request.  When the `enable_dns_express` setting is `no` and the `enable_zone_transfer` setting is `true`, the BIG-IP system processes zone transfer requests based on the last action and answers the request from local BIND or a pool member.  **Choices:**   - `false` - `true` |
| **name**  string / required | Specifies the name of the DNS profile. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `dns` profile. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **process_recursion_desired**  boolean | Specifies whether to process client-side DNS packets with Recursion Desired set in the header.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  If set to `false`, processing of the packet is subject to the unhandled-query-action option.  **Choices:**   - `false` - `true` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **unhandled_query_action**  string | Specifies the action to take when a query does not match a Wide IP or a DNS Express Zone.  When `allow`, the BIG-IP system forwards queries to a DNS server or pool member. If a pool is not associated with a listener and the Use BIND Server on BIG-IP setting is set to Enabled, requests are forwarded to the local BIND server.  When `drop`, the BIG-IP system does not respond to the query.  When `reject`, the BIG-IP system returns the query with the REFUSED return code.  When `hint`, the BIG-IP system returns the query with a list of root name servers.  When `no-error`, the BIG-IP system returns the query with the NOERROR return code.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `"allow"` - `"drop"` - `"reject"` - `"hint"` - `"no-error"` |
| **use_local_bind**  boolean | Specifies whether the system forwards non-wide IP queries to the local BIND server on the BIG-IP system.  For best performance, disable this setting when using a DNS cache.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |

## [Notes](bigip_profile_dns_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_dns_module.md#id4)

```yaml+jinja
- name: Create a DNS profile
  bigip_profile_dns:
    name: foo
    enable_dns_express: false
    enable_dnssec: false
    enable_gtm: false
    process_recursion_desired: false
    use_local_bind: false
    enable_dns_firewall: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_dns_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cache_name**  string | Name of the cache used by DNS.  **Returned:** changed  **Sample:** `"/Common/cache1"` |
| **enable_cache**  boolean | Whether DNS caching is enabled or not.  **Returned:** changed  **Sample:** `false` |
| **enable_dns_express**  boolean | Whether DNS Express is enabled on the resource or not.  **Returned:** changed  **Sample:** `true` |
| **enable_dns_firewall**  boolean | Whether DNS firewall capability is enabled or not.  **Returned:** changed  **Sample:** `false` |
| **enable_dnssec**  boolean | Whether DNSSEC is enabled on the resource or not.  **Returned:** changed  **Sample:** `false` |
| **enable_gtm**  boolean | Whether GTM is used to manage the resource or not.  **Returned:** changed  **Sample:** `true` |
| **enable_zone_transfer**  boolean | Whether zone transfer are enabled on the resource or not.  **Returned:** changed  **Sample:** `false` |
| **process_recursion_desired**  boolean | Whether client-side DNS packets are processed with Recursion Desired set.  **Returned:** changed  **Sample:** `true` |
| **unhandled_query_action**  string | What to do with unhandled queries  **Returned:** changed  **Sample:** `"allow"` |
| **use_local_bind**  boolean | Whether non-wide IP queries are forwarded to the local BIND server or not.  **Returned:** changed  **Sample:** `false` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
