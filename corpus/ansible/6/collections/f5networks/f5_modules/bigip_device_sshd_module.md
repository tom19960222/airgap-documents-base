---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_device_sshd module – Manage the SSHD settings of a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_device_sshd_module.html
fetched_at: 2026-07-27T17:26:32+00:00
---
# f5networks.f5_modules.bigip_device_sshd module – Manage the SSHD settings of a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_sshd`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_sshd_module.md#synopsis)
- [Parameters](bigip_device_sshd_module.md#parameters)
- [Notes](bigip_device_sshd_module.md#notes)
- [Examples](bigip_device_sshd_module.md#examples)
- [Return Values](bigip_device_sshd_module.md#return-values)

## [Synopsis](bigip_device_sshd_module.md#id1)

- Manage the SSHD (secure shell daemon) settings of a BIG-IP.

## [Parameters](bigip_device_sshd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow**  list / elements=string | If you have enabled SSH access, specifies the IP address or address range for other systems that can use SSH to communicate with this system.  To specify all addresses, use the value `all`.  An IP address can be specified, such as 172.27.1.10.  IP ranges can be specified, such as 172.27.\*.\* or 172.27.0.0/255.255.0.0.  To remove SSH access, specify an empty list or an empty string. |
| **banner**  string | Whether to enable the banner or not.  Choices:   - `"enabled"` - `"disabled"` |
| **banner_text**  string | Specifies the text to include on the pre-login banner, which displays when a user attempts to login to the system using SSH. |
| **inactivity_timeout**  integer | Specifies the number of seconds before inactivity causes an SSH session to log out. |
| **log_level**  string | Specifies the minimum SSHD message level to include in the system log.  Choices:   - `"debug"` - `"debug1"` - `"debug2"` - `"debug3"` - `"error"` - `"fatal"` - `"info"` - `"quiet"` - `"verbose"` |
| **login**  string | When checked `enabled`, specifies the system accepts SSH communication.  Choices:   - `"enabled"` - `"disabled"` |
| **port**  integer | Port on which you want the SSH daemon to run. |
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

## [Notes](bigip_device_sshd_module.md#id3)

> **Note:**
>
> - Requires BIG-IP version 12.0.0 or greater
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_sshd_module.md#id4)

```yaml+jinja
- name: Set the banner for the SSHD service from a string
  bigip_device_sshd:
    banner: enabled
    banner_text: banner text goes here
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set the banner for the SSHD service from a file
  bigip_device_sshd:
    banner: enabled
    banner_text: "{{ lookup('file', '/path/to/file') }}"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set the SSHD service to run on port 2222
  bigip_device_sshd:
    port: 2222
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_device_sshd_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allow**  list / elements=string | If you have enabled SSH access, specifies the IP address or address range for other systems that can use SSH to communicate with this system.  Returned: changed  Sample: `["192.0.2.*"]` |
| **banner**  string | Whether the banner is enabled or not.  Returned: changed  Sample: `"True"` |
| **banner_text**  string | Specifies the text included on the pre-login banner which displays when a user attempts to login to the system using SSH.  Returned: changed and success  Sample: `"This is a corporate device. Connecting to it without..."` |
| **inactivity_timeout**  integer | The number of seconds before inactivity causes an SSH session to log out.  Returned: changed  Sample: `10` |
| **log_level**  string | The minimum SSHD message level to include in the system log.  Returned: changed  Sample: `"debug"` |
| **login**  boolean | Specifies whether the system accepts SSH communications or not.  Returned: changed  Sample: `true` |
| **port**  integer | Port on which you want the SSH daemon to run.  Returned: changed  Sample: `22` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
