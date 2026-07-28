---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_dns_cache_resolver module – Manage DNS resolver cache configuration on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_dns_cache_resolver_module.html
fetched_at: 2026-07-27T17:26:35+00:00
---
# f5networks.f5_modules.bigip_dns_cache_resolver module – Manage DNS resolver cache configuration on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_dns_cache_resolver`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_dns_cache_resolver_module.md#synopsis)
- [Parameters](bigip_dns_cache_resolver_module.md#parameters)
- [Notes](bigip_dns_cache_resolver_module.md#notes)
- [Examples](bigip_dns_cache_resolver_module.md#examples)
- [Return Values](bigip_dns_cache_resolver_module.md#return-values)

## [Synopsis](bigip_dns_cache_resolver_module.md#id1)

- Manage the DNS resolver cache configuration on BIG-IP devices.

## [Parameters](bigip_dns_cache_resolver_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **answer_default_zones**  boolean | Specifies whether the system answers DNS queries for the default zones localhost, reverse 127.0.0.1 and ::1, and AS112.  When creating a new cache resolver, if this parameter is not specified, the default is `no`.  Choices:   - `false` - `true` |
| **forward_zones**  any | Forward zones associated with the cache.  To remove all forward zones, specify a value of `none`. |
| **name**  string | Specifies an FQDN for the forward zone. |
| **nameservers**  list / elements=dictionary | Specifies the IP address and service port of a recursive nameserver that answers DNS queries for the zone when the response cannot be found in the DNS cache. |
| **address**  string | Address of recursive nameserver. |
| **port**  integer | Port of recursive nameserver.  When specifying new nameservers, if this value is not provided, the default is `53`. |
| **name**  string / required | Specifies the name of the cache. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **route_domain**  string | Specifies the route domain the resolver uses for outbound traffic. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_dns_cache_resolver_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_dns_cache_resolver_module.md#id4)

```yaml+jinja
- name: Create a DNS resolver cache
  bigip_dns_cache:
    name: foo
    answer_default_zones: yes
    forward_zones:
      - name: foo.bar.com
        nameservers:
          - address: 1.2.3.4
            port: 53
          - address: 5.6.7.8
    route_domain: 0
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_dns_cache_resolver_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **param1**  boolean | The new param1 value of the resource.  Returned: changed  Sample: `true` |
| **param2**  string | The new param2 value of the resource.  Returned: changed  Sample: `"Foo is bar"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
