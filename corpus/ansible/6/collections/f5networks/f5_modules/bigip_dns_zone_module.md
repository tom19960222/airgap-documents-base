---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_dns_zone module – Manage DNS zones on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_dns_zone_module.html
fetched_at: 2026-07-27T17:26:37+00:00
---
# f5networks.f5_modules.bigip_dns_zone module – Manage DNS zones on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_dns_zone`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_dns_zone_module.md#synopsis)
- [Parameters](bigip_dns_zone_module.md#parameters)
- [Notes](bigip_dns_zone_module.md#notes)
- [Examples](bigip_dns_zone_module.md#examples)
- [Return Values](bigip_dns_zone_module.md#return-values)

## [Synopsis](bigip_dns_zone_module.md#id1)

- Manage DNS zones on BIG-IP. The zones managed here are primarily used for configuring DNS Express on a BIG-IP. This module does not configure zones that are found in BIG-IP ZoneRunner.

## [Parameters](bigip_dns_zone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dns_express**  dictionary | DNS express related settings. |
| **allow_notify_from**  list / elements=string | Specifies the IP addresses from which the system accepts NOTIFY messages for this DNS Express zone. |
| **enabled**  boolean | Specifies the current status of the DNS Express zone.  Choices:   - `false` - `true` |
| **notify_action**  string | Specifies the action the system takes when a NOTIFY message is received for this DNS Express zone.  If a TSIG key is configured for the zone, the signature is only validated for `consume` and `repeat` actions.  When `consume`, the NOTIFY message is seen only by DNS Express.  When `bypass`, the NOTIFY message does not go to DNS Express, but instead goes to a back-end DNS server (subject to the value of the Unhandled Query Action configured in the DNS profile applied to the listener that handles the DNS request).  When `repeat`, the NOTIFY message goes to both DNS Express and any back-end DNS server.  Choices:   - `"consume"` - `"bypass"` - `"repeat"` |
| **response_policy**  boolean | Specifies whether this DNS Express zone is a DNS response policy zone (RPZ).  Choices:   - `false` - `true` |
| **server**  string | Specifies the back-end authoritative DNS server from which the BIG-IP system receives AXFR zone transfers for the DNS Express zone. |
| **verify_tsig**  boolean | Specifies whether the system verifies the identity of the authoritative nameserver that sends updated information for this DNS Express zone.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the DNS zone.  The name must begin with a letter and contain only letters, numbers, and the underscore character. |
| **nameservers**  list / elements=string | Specifies the DNS nameservers to which the system sends NOTIFY messages. |
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
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tsig_server_key**  string | Specifies the TSIG key the system uses to authenticate the back-end DNS authoritative server that sends AXFR zone transfers to the BIG-IP system. |

## [Notes](bigip_dns_zone_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_dns_zone_module.md#id4)

```yaml+jinja
- name: Create a DNS zone for DNS express
  bigip_dns_zone:
    name: zone.foo.com
    dns_express:
      enabled: yes
      server: dns-lab
      allow_notify_from:
        - 192.168.39.10
      notify_action: consume
      verify_tsig: no
      response_policy: no
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Disable DNS express zone, change server, and modify notify_action to bypass
  bigip_dns_zone:
    name: zone.foo.com
    dns_express:
      enabled: no
      server: foo1.server.com
      allow_notify_from:
        - 192.168.39.10
      notify_action: bypass
      verify_tsig: no
      response_policy: no
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add nameservers
  bigip_dns_zone:
    name: zone.foo.com
    nameservers:
      - foo1.nameserver.com
      - foo2.nameserver.com
      - foo3.nameserver.com
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove nameserver
  bigip_dns_zone:
    name: zone.foo.com
    nameservers:
      - foo1.nameserver.com
      - foo2.nameserver.com
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove all nameservers
  bigip_dns_zone:
    name: zone.foo.com
    nameservers: none
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add tsig_server_key
  bigip_dns_zone:
    name: zone.foo.com
    tsig_server_key: key1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove tsig_server_key
  bigip_dns_zone:
    name: zone.foo.com
    tsig_server_key: none
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove zone
  bigip_dns_zone:
    name: zone.foo.com
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_dns_zone_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allow_notify_from**  list / elements=string | The new DNS Express Allow NOTIFY From value.  Returned: changed  Sample: `["1.1.1.1", "2.2.2.2"]` |
| **enabled**  boolean | Whether the zone is enabled or not.  Returned: changed  Sample: `true` |
| **express_server**  string | The new DNS Express Server value.  Returned: changed  Sample: `"server1"` |
| **nameservers**  list / elements=string | The new Zone Transfer Clients Nameservers value.  Returned: changed  Sample: `["/Common/server1", "/Common/server2"]` |
| **notify_action**  string | The new DNS Express Notify Action value.  Returned: changed  Sample: `"consume"` |
| **response_policy**  boolean | The new DNS Express Response Policy value.  Returned: changed  Sample: `false` |
| **tsig_server_key**  string | The new TSIG Server Key value.  Returned: changed  Sample: `"/Common/key1"` |
| **verify_tsig**  boolean | The new DNS Express Verify Notify TSIG value.  Returned: changed  Sample: `true` |

### Authors

- Tim Rupp (@caphrim007)
- Greg Crosby (@crosbygw)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
