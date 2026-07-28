---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_snmp_community module – Manages SNMP communities on a BIG-IP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_snmp_community_module.html
fetched_at: 2026-07-28T02:07:17+00:00
---
# f5networks.f5_modules.bigip_snmp_community module – Manages SNMP communities on a BIG-IP.

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_snmp_community`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_snmp_community_module.md#synopsis)
- [Parameters](bigip_snmp_community_module.md#parameters)
- [Notes](bigip_snmp_community_module.md#notes)
- [Examples](bigip_snmp_community_module.md#examples)
- [Return Values](bigip_snmp_community_module.md#return-values)

## [Synopsis](bigip_snmp_community_module.md#id1)

- Assists in managing Simple Network Management Protocol (SNMP) communities on a BIG-IP system. Different SNMP versions are supported by this module. Note the different parameters offered by this module, as different parameters work for different versions of SNMP. This is important if you are mixing versions `v2c` and `3`.

## [Parameters](bigip_snmp_community_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access**  string | Specifies the user’s access level to the MIB.  When creating a new community, if this parameter is not specified, the default is `ro`.  When `ro`, specifies the user can view the MIB, but cannot modify the MIB.  When `rw`, specifies the user can view and modify the MIB.  **Choices:**   - `"ro"` - `"rw"` - `"read-only"` - `"read-write"` |
| **community**  string | Specifies the community string (password) for access to the MIB.  This parameter is only relevant when `version` is `v1` or `v2c`. If `version` is something else, this parameter is ignored. |
| **ip_version**  string | Specifies whether the record applies to IPv4 or IPv6 addresses.  When creating a new community, if this value is not specified, the default is `4`.  This parameter is only relevant when `version` is `v1` or `v2c`. If `version` is something else, this parameter is ignored.  **Choices:**   - `"4"` - `"6"` |
| **name**  string | Name that identifies the SNMP community.  When `version` is `v1` or `v2c`, this parameter is required.  The name `public` is a reserved name on the BIG-IP. This module handles that name differently than others. Functionally, you should not see a difference. |
| **oid**  string | Specifies the object identifier (OID) for the record.  When `version` is `v3`, this parameter is required.  When `version` is either `v1` or `v2c`, if this value is specified, then `source` must not be set to `all`. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **port**  integer | Specifies the port for the trap destination.  This parameter is only relevant when `version` is `v1` or `v2c`. If `version` is something else, this parameter is ignored. |
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
| **snmp_auth_password**  string | Specifies the password for the user.  When creating a new SNMP `v3` community, this parameter is required.  This value must be at least 8 characters long. |
| **snmp_auth_protocol**  string | Specifies the authentication method for the user.  When `md5`, specifies the system uses the MD5 algorithm to authenticate the user.  When `sha`, specifies the secure hash algorithm (SHA) to authenticate the user.  When `none`, specifies the user does not require authentication.  When creating a new SNMP `v3` community, if this parameter is not specified, the default is `sha`.  **Choices:**   - `"md5"` - `"sha"` - `"none"` |
| **snmp_privacy_password**  string | Specifies the password for the user.  When creating a new SNMP `v3` community, this parameter is required.  This value must be at least 8 characters long. |
| **snmp_privacy_protocol**  string | Specifies the encryption protocol.  When `aes`, specifies the system encrypts the user information using AES (Advanced Encryption Standard).  When `des`, specifies the system encrypts the user information using DES (Data Encryption Standard).  When `none`, specifies the system does not encrypt the user information.  When creating a new SNMP `v3` community, if this parameter is not specified, the default is `aes`.  **Choices:**   - `"aes"` - `"des"` - `"none"` |
| **snmp_username**  string | Specifies the name of the user for whom you want to grant access to the SNMP v3 MIB.  This parameter is only relevant when `version` is `v3`. If `version` is something else, this parameter is ignored.  When creating a new SNMP `v3` community, this parameter is required.  This parameter cannot be changed once it has been set. |
| **source**  string | Specifies the source address for access to the MIB.  This parameter can accept a value of `all`.  If this parameter is not specified, the value is `all`.  This parameter is only relevant when `version` is `v1` or `v2c`. If `version` is something else, this parameter is ignored.  If `source` is set to `all`, it is not possible to specify an `oid`. This will raise an error.  You should provide this parameter when `state` is `absent`, so the correct community is removed. To remove the `public` SNMP community that comes with a BIG-IP, this parameter should be `default`. |
| **state**  string | When `present`, ensures the address list and entries exists.  When `absent`, ensures the address list is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` allows users to update passwords. `on_create` only sets the password for newly created resources.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **version**  string | Specifies to which SNMP version the trap destination applies.  **Choices:**   - `"v1"` - `"v2c"` ← (default) - `"v3"` |

## [Notes](bigip_snmp_community_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_snmp_community_module.md#id4)

```yaml+jinja
- name: Create an SMNP v2c read-only community
  bigip_snmp_community:
    name: foo
    version: v2c
    source: all
    oid: .1
    access: ro
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create an SMNP v3 read-write community
  bigip_snmp_community:
    name: foo
    version: v3
    snmp_username: foo
    snmp_auth_protocol: sha
    snmp_auth_password: secret
    snmp_privacy_protocol: aes
    snmp_privacy_password: secret
    oid: .1
    access: rw
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove the default 'public' SNMP community
  bigip_snmp_community:
    name: public
    source: default
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_snmp_community_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **access**  string | The new access level for the MIB.  **Returned:** changed  **Sample:** `"ro"` |
| **community**  string | The new community value.  **Returned:** changed  **Sample:** `"community1"` |
| **ip_version**  string | The new IP version value.  **Returned:** changed  **Sample:** `"0.1"` |
| **oid**  string | The new OID value.  **Returned:** changed  **Sample:** `"0.1"` |
| **snmp_auth_password**  string | The new password of the given snmp_username.  **Returned:** changed  **Sample:** `"secret1"` |
| **snmp_auth_protocol**  string | The new SNMP auth protocol.  **Returned:** changed  **Sample:** `"sha"` |
| **snmp_privacy_password**  string | The new password of the given snmp_username.  **Returned:** changed  **Sample:** `"secret2"` |
| **snmp_privacy_protocol**  string | The new SNMP privacy protocol.  **Returned:** changed  **Sample:** `"aes"` |
| **snmp_username**  string | The new SNMP username.  **Returned:** changed  **Sample:** `"user1"` |
| **source**  string | The new source address to access the MIB.  **Returned:** changed  **Sample:** `"1.1.1.1"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
