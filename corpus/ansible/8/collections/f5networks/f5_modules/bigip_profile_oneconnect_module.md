---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_oneconnect module – Manage OneConnect profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_oneconnect_module.html
fetched_at: 2026-07-28T02:07:02+00:00
---
# f5networks.f5_modules.bigip_profile_oneconnect module – Manage OneConnect profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_oneconnect`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_oneconnect_module.md#synopsis)
- [Parameters](bigip_profile_oneconnect_module.md#parameters)
- [Notes](bigip_profile_oneconnect_module.md#notes)
- [Examples](bigip_profile_oneconnect_module.md#examples)
- [Return Values](bigip_profile_oneconnect_module.md#return-values)

## [Synopsis](bigip_profile_oneconnect_module.md#id1)

- Manage OneConnect profiles on a BIG-IP system.

## [Parameters](bigip_profile_oneconnect_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the profile. |
| **idle_timeout_override**  string | Specifies the number of seconds a connection is idle before the connection flow is eligible for deletion.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  You may specify a number of seconds for the timeout override.  When `disabled`, specifies there is no timeout override for the connection.  When `indefinite`, specifies a connection may be idle with no timeout override. |
| **limit_type**  string | When `none`, simultaneous in-flight requests and responses over TCP connections to a pool member are counted toward the limit. This is the historical behavior.  When `idle`, idle connections will be dropped as the TCP connection limit is reached. For short intervals, during the overlap of the idle connection being dropped and the new connection being established, the TCP connection limit may be exceeded.  When `strict`, the TCP connection limit is honored with no exceptions. This means that idle connections will prevent new TCP connections from being made until they expire, even if they could otherwise be reused.  `strict` is not a recommended configuration except in very special cases with short expiration timeouts.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `"none"` - `"idle"` - `"strict"` |
| **maximum_age**  integer | Specifies the maximum number of seconds allowed for a connection in the connection reuse pool.  For any connection with an age higher than this value, the system removes that connection from the re-use pool.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **maximum_reuse**  integer | Specifies the maximum number of times that a server-side connection can be reused.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **maximum_size**  integer | Specifies the maximum number of connections the system holds in the connection reuse pool.  If the pool is already full, a server-side connection closes after the response is completed.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **name**  string / required | Specifies the name of the OneConnect profile. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `oneconnect` profile. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
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
| **share_pools**  boolean | Indicates connections may be shared not only within a virtual server, but also among similar virtual servers.  When `true`, all virtual servers that use the same OneConnect and other internal network profiles can share connections.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **source_mask**  string | Specifies a value the system applies to the source address to determine its eligibility for reuse.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  The system applies the value of this setting to the server-side source address to determine its eligibility for reuse.  A mask of `0` causes the system to share reused connections across all source addresses. A host mask of `32` causes the system to share only those reused connections originating from the same source address.  When you are using a SNAT or SNAT pool, the server-side source address is translated first and then the OneConnect mask is applied to the translated address. |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_profile_oneconnect_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_oneconnect_module.md#id4)

```yaml+jinja
- name: Create a OneConnect profile
  bigip_profile_oneconnect:
    name: foo
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_profile_oneconnect_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Description of the profile.  **Returned:** changed  **Sample:** `"My profile"` |
| **idle_timeout_override**  string | The new idle timeout override.  **Returned:** changed  **Sample:** `"disabled"` |
| **limit_type**  string | New limit type of the profile.  **Returned:** changed  **Sample:** `"idle"` |
| **maximum_age**  integer | Maximum number of seconds allowed for a connection in the connection reuse pool.  **Returned:** changed  **Sample:** `2000` |
| **maximum_reuse**  integer | Maximum number of times a server-side connection can be reused.  **Returned:** changed  **Sample:** `1000` |
| **maximum_size**  integer | Maximum number of connections the system holds in the connection reuse pool.  **Returned:** changed  **Sample:** `3000` |
| **share_pools**  boolean | Share connections among similar virtual servers.  **Returned:** changed  **Sample:** `true` |
| **source_mask**  string | Value the system applies to the source address to determine its eligibility for reuse.  **Returned:** changed  **Sample:** `"255.255.255.255"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
