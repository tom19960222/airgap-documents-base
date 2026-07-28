---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_http_compression module – Manage HTTP compression profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_http_compression_module.html
fetched_at: 2026-07-28T02:07:01+00:00
---
# f5networks.f5_modules.bigip_profile_http_compression module – Manage HTTP compression profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_http_compression`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_http_compression_module.md#synopsis)
- [Parameters](bigip_profile_http_compression_module.md#parameters)
- [Notes](bigip_profile_http_compression_module.md#notes)
- [Examples](bigip_profile_http_compression_module.md#examples)
- [Return Values](bigip_profile_http_compression_module.md#return-values)

## [Synopsis](bigip_profile_http_compression_module.md#id1)

- Manage HTTP compression profiles on a BIG-IP device.

## [Parameters](bigip_profile_http_compression_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **buffer_size**  integer | Maximum number of compressed bytes the system buffers before inserting a Content-Length header (which specifies the compressed size) into the response.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **content_type_include**  list / elements=string  *added in f5networks.f5_modules 1.15.0* | Specifies the list of the content types that are allowed. |
| **description**  string | Description of the HTTP compression profile. |
| **gzip_level**  integer | Specifies the degree to which the system compresses the content.  Higher compression levels cause the compression process to be slower.  Valid values are between 1 (least compression and fastest) to 9 (most compression and slowest).  **Choices:**   - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` |
| **gzip_memory_level**  integer | Number of kilobytes of memory the system uses for internal compression buffers when compressing a server response.  **Choices:**   - `1` - `2` - `4` - `8` - `16` - `32` - `64` - `128` - `256` |
| **gzip_window_size**  integer | Number of kilobytes in the window size the system uses when compressing a server response.  **Choices:**   - `1` - `2` - `4` - `8` - `16` - `32` - `64` - `128` |
| **name**  string / required | Specifies the name of the compression profile. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `httpcompression` profile. |
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
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_profile_http_compression_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_http_compression_module.md#id4)

```yaml+jinja
- name: Create an HTTP compression profile
  bigip_profile_http_compression:
    name: profile1
    description: Custom HTTP Compression Profile
    buffer_size: 131072
    gzip_level: 6
    gzip_memory_level: 16k
    gzip_window_size: 64k
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_http_compression_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **buffer_size**  integer | The new buffer size of the profile.  **Returned:** changed  **Sample:** `4096` |
| **description**  string | The new description of the resource.  **Returned:** changed  **Sample:** `"My custom profile"` |
| **gzip_level**  integer | The new GZIP level of the profile. Smaller is less compression.  **Returned:** changed  **Sample:** `2` |
| **gzip_memory_level**  integer | The new GZIP memory level of the profile, in KB.  **Returned:** changed  **Sample:** `16` |
| **gzip_window_size**  integer | The new GZIP window size of the profile, in KB.  **Returned:** changed  **Sample:** `64` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
