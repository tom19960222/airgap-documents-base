---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_ipsec_policy module – Manage IPSec policies on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_ipsec_policy_module.html
fetched_at: 2026-07-27T17:27:02+00:00
---
# f5networks.f5_modules.bigip_ipsec_policy module – Manage IPSec policies on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ipsec_policy`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_ipsec_policy_module.md#synopsis)
- [Parameters](bigip_ipsec_policy_module.md#parameters)
- [Notes](bigip_ipsec_policy_module.md#notes)
- [Examples](bigip_ipsec_policy_module.md#examples)
- [Return Values](bigip_ipsec_policy_module.md#return-values)

## [Synopsis](bigip_ipsec_policy_module.md#id1)

- Manage IPSec policies on a BIG-IP device.

## [Parameters](bigip_ipsec_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_algorithm**  string | Specifies the algorithm to use for IKE authentication.  Choices:   - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` - `"aes-gcm128"` - `"aes-gcm192"` - `"aes-gcm256"` - `"aes-gmac128"` - `"aes-gmac192"` - `"aes-gmac256"` |
| **description**  string | Description of the policy |
| **encrypt_algorithm**  string | Specifies the algorithm to use for IKE encryption.  Choices:   - `"none"` - `"3des"` - `"aes128"` - `"aes192"` - `"aes256"` - `"aes-gmac256"` - `"aes-gmac192"` - `"aes-gmac128"` - `"aes-gcm256"` - `"aes-gcm192"` - `"aes-gcm256"` - `"aes-gcm128"` |
| **ipcomp**  string | Specifies whether to use IPComp encapsulation.  When `none`, specifies IPComp is disabled.  When `deflate`, specifies IPComp is enabled and uses the Deflate compression algorithm.  Choices:   - `"none"` - `"null"` - `"deflate"` |
| **ipv4_interface**  boolean | When `mode` is `interface`, indicates if the IPv4 `any` address should be used. By default `BIG-IP` assumes `any6` address for tunnel addresses when `mode` is `interface`.  This option takes effect only when `mode` is set to `interface`.  Choices:   - `false` - `true` |
| **kb_lifetime**  integer | Specifies the length of time before the IKE security association, in kilobytes. expires. |
| **lifetime**  integer | Specifies the length of time before the IKE security association expires, in minutes. |
| **mode**  string | Specifies the processing mode.  When `transport`, specifies a mode that encapsulates only the payload (adding an ESP header, trailer, and authentication tag).  When `tunnel`, specifies a mode that includes encapsulation of the header as well as the payload (adding a new IP header, in addition to adding an ESP header, trailer, and authentication tag). If you select this option, you must also provide IP addresses for the local and remote endpoints of the IPsec tunnel.  When `isession`, specifies the use of iSession over an IPsec tunnel. To use this option, you must also configure the iSession endpoints with IPsec in the Acceleration section of the user interface.  When `interface`, specifies the IPsec policy can be used in the tunnel profile for network interfaces.  Choices:   - `"transport"` - `"interface"` - `"isession"` - `"tunnel"` |
| **name**  string / required | Specifies the name of the IPSec policy. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **perfect_forward_secrecy**  string | Specifies the Diffie-Hellman group to use for IKE Phase 2 negotiation.  Choices:   - `"none"` - `"modp768"` - `"modp1024"` - `"modp1536"` - `"modp2048"` - `"modp3072"` - `"modp4096"` - `"modp6144"` - `"modp8192"` |
| **protocol**  string | Specifies the IPsec protocol.  Options include ESP (Encapsulating Security Protocol) or AH (Authentication Header).  Choices:   - `"esp"` - `"ah"` |
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
| **route_domain**  integer | Specifies the route domain, when `interface` is selected for the `mode` setting. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tunnel_local_address**  string | Specifies the local endpoint IP address of the IPsec tunnel.  This parameter is only valid when `mode` is `tunnel`. |
| **tunnel_remote_address**  string | Specifies the remote endpoint IP address of the IPsec tunnel.  This parameter is only valid when `mode` is `tunnel`. |

## [Notes](bigip_ipsec_policy_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ipsec_policy_module.md#id4)

```yaml+jinja
- name: Create a IPSec policy
  bigip_ipsec_policy:
    name: policy1
    mode: tunnel
    tunnel_local_address: 1.1.1.1
    tunnel_remote_address: 2.2.2.
    auth_algorithm: sha1
    encrypt_algorithm: 3des
    protocol: esp
    perfect_forward_secrecy: modp1024
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_ipsec_policy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auth_algorithm**  string | The new IKE Phase 2 Authentication Algorithm value.  Returned: changed  Sample: `"sha512"` |
| **description**  string | The new description value.  Returned: changed  Sample: `"My policy"` |
| **encrypt_algorithm**  string | The new IKE Phase 2 Encryption Algorithm value.  Returned: changed  Sample: `"aes256"` |
| **ipcomp**  string | The new IKE Phase 2 IPComp value.  Returned: changed  Sample: `"deflate"` |
| **kb_lifetime**  integer | The new IKE Phase 2 KB Lifetime value.  Returned: changed  Sample: `0` |
| **lifetime**  integer | The new IKE Phase 2 Lifetime value.  Returned: changed  Sample: `1440` |
| **mode**  string | The new Mode value.  Returned: changed  Sample: `"tunnel"` |
| **perfect_forward_secrecy**  string | The new IKE Phase 2 Perfect Forward Secrecy value.  Returned: changed  Sample: `"modp2048"` |
| **protocol**  string | The new IPsec Protocol value.  Returned: changed  Sample: `"ah"` |
| **route_domain**  integer | The new Route Domain value when in Tunnel mode.  Returned: changed  Sample: `2` |
| **tunnel_local_address**  string | The new Tunnel Local Address value.  Returned: changed  Sample: `"1.2.2.1"` |
| **tunnel_remote_address**  string | The new Tunnel Remote Address value.  Returned: changed  Sample: `"2.1.1.2"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
