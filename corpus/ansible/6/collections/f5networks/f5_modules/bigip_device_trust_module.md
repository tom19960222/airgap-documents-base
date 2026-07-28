---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_device_trust module – Manage the trust relationships between BIG-IPs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_device_trust_module.html
fetched_at: 2026-07-27T17:26:35+00:00
---
# f5networks.f5_modules.bigip_device_trust module – Manage the trust relationships between BIG-IPs

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_trust`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_trust_module.md#synopsis)
- [Parameters](bigip_device_trust_module.md#parameters)
- [Notes](bigip_device_trust_module.md#notes)
- [Examples](bigip_device_trust_module.md#examples)
- [Return Values](bigip_device_trust_module.md#return-values)

## [Synopsis](bigip_device_trust_module.md#id1)

- Manage the trust relationships between BIG-IP systems. Devices, once peered, cannot be updated. If updating is needed, the peer must first be removed before it can be re-added to the trust.

## [Parameters](bigip_device_trust_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **peer_hostname**  string | The hostname you want to associate with the device. This value is used to easily distinguish this device in BIG-IP configuration.  When trusting a new device, if this parameter is not specified, the value of `peer_server` is used as a default. |
| **peer_password**  string | The password of the API username of the remote peer device you are trusting. If this value is not specified, then the value of `password`, or the environment variable `F5_PASSWORD` is used. |
| **peer_server**  string / required | The peer address to connect to and trust for synchronizing the configuration. This is typically the management address of the remote device, but may also be a Self IP address. |
| **peer_user**  string | The API username of the remote peer device you are trusting. Note that the CLI user cannot be used unless it too has an API account. If this value is not specified, then the value of `user`, or the environment variable `F5_USER` is used. |
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
| **state**  string | When `present`, ensures the specified devices are trusted.  When `absent`, removes the device trusts.  Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string | Specifies whether the device you are adding is a Peer or a Subordinate. The default is `peer`.  The difference between the two is a matter of mitigating risk of compromise.  A subordinate device cannot sign a certificate for another device.  In the case where the security of an authority device in a trust domain is compromised, the risk of compromise is minimized for any subordinate device.  Designating devices as subordinate devices is recommended for device groups with a large number of member devices, where the risk of compromise is high.  Choices:   - `"peer"` ← (default) - `"subordinate"` |

## [Notes](bigip_device_trust_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_trust_module.md#id4)

```yaml+jinja
- name: Add trusts for all peer devices to Active device
  bigip_device_trust:
    peer_server: "{{ item.ansible_host }}"
    peer_hostname: "{{ item.inventory_hostname }}"
    peer_user: "{{ item.bigip_username }}"
    peer_password: "{{ item.bigip_password }}"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  loop: hostvars
  when: inventory_hostname in groups['master']
  delegate_to: localhost
```

## [Return Values](bigip_device_trust_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **peer_hostname**  string | The remote hostname used to identify the trusted peer.  Returned: changed  Sample: `"test-bigip-02.localhost.localdomain"` |
| **peer_server**  string | The remote IP address of the trusted peer.  Returned: changed  Sample: `"10.0.2.15"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
