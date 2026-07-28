---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_gtm_wide_ip module – Manages F5 BIG-IP GTM Wide IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_gtm_wide_ip_module.html
fetched_at: 2026-07-28T02:06:24+00:00
---
# f5networks.f5_modules.bigip_gtm_wide_ip module – Manages F5 BIG-IP GTM Wide IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_wide_ip`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_wide_ip_module.md#synopsis)
- [Parameters](bigip_gtm_wide_ip_module.md#parameters)
- [Notes](bigip_gtm_wide_ip_module.md#notes)
- [Examples](bigip_gtm_wide_ip_module.md#examples)
- [Return Values](bigip_gtm_wide_ip_module.md#return-values)

## [Synopsis](bigip_gtm_wide_ip_module.md#id1)

- Manages the F5 BIG-IP GTM (now BIG-IP DNS) Wide IP.

## [Parameters](bigip_gtm_wide_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aliases**  list / elements=string | Specifies alternate domain names for the web site content you are load balancing.  You can use the same wildcard characters for aliases as you can for actual Wide IP names. |
| **irules**  list / elements=string | List of rules to be applied.  If you want to remove all existing iRules, specify a single empty value; `""`. See the documentation for an example. |
| **last_resort_pool**  string | Specifies which GTM pool for the system to use as the last resort pool for the Wide IP.  The valid pools for this parameter are those with the `type` specified in this module. |
| **name**  aliases: wide_ip  string / required | Wide IP name. This name must be formatted as a fully qualified domain name (FQDN). You can also use the alias `wide_ip` but this is deprecated and will be removed in a future Ansible version. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **persist_cidr_ipv4**  integer | Specifies a mask used to group IPv4 LDNS addresses. This feature allows one persistence record to be shared by LDNS addresses that match within this mask. |
| **persist_cidr_ipv6**  integer | Specifies a mask used to group IPv6 LDNS addresses. This feature allows one persistence record to be shared by LDNS addresses that match within this mask. |
| **persistence**  boolean | When `true`, ensures when a local DNS makes repetitive requests on behalf of a client, the system reconnects the client to the same resource as previous requests.  When `false`, ensures repetitive requests do not reconnect the client to the same resource.  **Choices:**   - `false` - `true` |
| **persistence_ttl**  integer | Specifies the time to maintain a connection between an local DNS and a particular virtual server. |
| **pool_lb_method**  aliases: lb_method  string | Specifies the load balancing method used to select a pool in this wide IP. This setting is relevant only when multiple pools are configured for a Wide IP.  **Choices:**   - `"round-robin"` - `"ratio"` - `"topology"` - `"global-availability"` |
| **pools**  list / elements=dictionary | The pools you want associated with the Wide IP.  If `ratio` is not provided when creating a new Wide IP, it will default to 1. |
| **name**  string / required | The name of the pool to include. |
| **order**  integer | Order of the pool in relation to other pools attached to this Wide IP.  Pool order is significant when the Global Availability load balancing method is used.  When `order` is not provided, the module assigns it value of `0`. |
| **ratio**  integer | Ratio for the pool.  The system uses this number with the Ratio load balancing method.  When `ratio` is not provided, the module assigns it value of `0`. |
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
| **state**  string | When `present` or `enabled`, ensures the Wide IP exists and is enabled.  When `absent`, ensures the Wide IP has been removed.  When `disabled`, ensures the Wide IP exists and is disabled.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"disabled"` - `"enabled"` |
| **type**  string / required | Specifies the type of Wide IP. GTM Wide IPs need to be keyed by query type in addition to name, because pool members need different attributes depending on the response RDATA they are meant to supply.  **Choices:**   - `"a"` - `"aaaa"` - `"cname"` - `"mx"` - `"naptr"` - `"srv"` |

## [Notes](bigip_gtm_wide_ip_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_wide_ip_module.md#id4)

```yaml+jinja
- name: Set lb method
  bigip_gtm_wide_ip:
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    type: a
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add iRules to the Wide IP
  bigip_gtm_wide_ip:
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    type: a
    irules:
      - irule1
      - irule2
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove one iRule from the Virtual Server
  bigip_gtm_wide_ip:
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    type: a
    irules:
      - irule1
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove all iRules from the Virtual Server
  bigip_gtm_wide_ip:
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    type: a
    irules: ""
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Assign a pool with ratio to the Wide IP
  bigip_gtm_wide_ip:
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    type: a
    pools:
      - name: pool1
        ratio: 100
        order: 2
      - name: pool1
        ratio: 100
        order: 1
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Assign a pool with persistence to the Wide IP
  bigip_gtm_wide_ip:
    pool_lb_method: round-robin
    name: my-wide-ip.example.com
    type: a
    pools:
      - name: pool1
        persistence: true
        persist_cidr_ipv4: 24
        persist_cidr_ipv6: 120
        persistence_ttl: 3500
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_wide_ip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **aliases**  list / elements=string | Aliases set on the Wide IP.  **Returned:** changed  **Sample:** `["alias1.foo.com", "*.wildcard.domain"]` |
| **irules**  list / elements=string | iRules set on the Wide IP.  **Returned:** changed  **Sample:** `["/Common/irule1", "/Common/irule2"]` |
| **lb_method**  string | The new load balancing method used by the Wide IP.  **Returned:** changed  **Sample:** `"topology"` |
| **persist_cidr_ipv4**  integer | Specifies a mask used to group IPv4 LDNS addresses.  **Returned:** changed  **Sample:** `32` |
| **persist_cidr_ipv6**  integer | Specifies a mask used to group IPv6 LDNS addresses.  **Returned:** changed  **Sample:** `128` |
| **persistence**  boolean | Whether pool connections will be persisted.  **Returned:** changed  **Sample:** `false` |
| **persistence_ttl**  integer | Specifies the persistence TTL between an local DNS and a particular virtual server.  **Returned:** changed  **Sample:** `3600` |
| **state**  string | The new state of the Wide IP.  **Returned:** changed  **Sample:** `"disabled"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
