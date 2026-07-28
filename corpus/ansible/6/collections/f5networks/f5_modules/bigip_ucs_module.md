---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_ucs module – Manage upload, installation, and removal of UCS files"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_ucs_module.html
fetched_at: 2026-07-27T17:27:59+00:00
---
# f5networks.f5_modules.bigip_ucs module – Manage upload, installation, and removal of UCS files

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ucs`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_ucs_module.md#synopsis)
- [Parameters](bigip_ucs_module.md#parameters)
- [Notes](bigip_ucs_module.md#notes)
- [Examples](bigip_ucs_module.md#examples)

## [Synopsis](bigip_ucs_module.md#id1)

- Manage the upload, installation, and removal of UCS files on a BIG-IP system. A user configuration set (UCS) is a backup file that contains BIG-IP configuration data that can be used to fully restore a BIG-IP system in the event of a failure or RMA replacement.

## [Parameters](bigip_ucs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | If `yes`, the system uploads the file every time and replaces the file on the device. If `no`, the file is only uploaded if it does not already exist. Generally should only be `yes` in cases where you believe the image was corrupted during upload.  Choices:   - `false` ← (default) - `true` |
| **include_chassis_level_config**  boolean | During restoration of the UCS file, includes chassis level configuration that is shared among boot volume sets. For example, the cluster default configuration.  Choices:   - `false` - `true` |
| **no_license**  boolean | Performs a full restore of the UCS file and all the files it contains, with the exception of the license file. The option must be used to restore a UCS on RMA (Returned Materials Authorization) devices.  Choices:   - `false` - `true` |
| **no_platform_check**  boolean | Bypasses the platform check and allows installation of a UCS that was created using a different platform. By default (without this option), installation of a UCS created from a different platform is not allowed.  Choices:   - `false` - `true` |
| **passphrase**  string | Specifies the passphrase that is necessary to load the specified UCS file. |
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
| **reset_trust**  boolean | When specified, the device and trust domain certs and keys are not loaded from the UCS. Instead, a new set is generated.  Choices:   - `false` - `true` |
| **state**  string | When `installed`, ensures the UCS is uploaded and installed on the system. When `present`, ensures the UCS is uploaded. When `absent`, the UCS is removed from the system. When `installed`, the uploading of the UCS is idempotent, however the installation of that configuration is not idempotent.  Choices:   - `"absent"` - `"installed"` - `"present"` ← (default) |
| **ucs**  string / required | The path to the UCS file to install. The parameter must be provided if the `state` is either `installed` or `activated`. When `state` is `absent`, the full path for this parameter is ignored and only the filename is used to select a UCS for removal. Therefore you could specify `/foo/bar/test.ucs` and this module would only look for `test.ucs`. |

## [Notes](bigip_ucs_module.md#id3)

> **Note:**
>
> - Only the most basic checks are performed by this module. Other checks and considerations need to be taken into account. See <https://support.f5.com/kb/en-us/solutions/public/11000/300/sol11318.html>
> - This module does not handle devices with the FIPS 140 HSM.
> - This module does not handle BIG-IPs systems on the 6400, 6800, 8400, or 8800 hardware platforms.
> - This module does not verify the new or replaced SSH keys from the UCS file are synchronized between the BIG-IP system and the SCCP.
> - This module does not support the ‘rma’ option.
> - This module does not support restoring a UCS archive on a BIG-IP 1500, 3400, 4100, 6400, 6800, or 8400 hardware platforms other than the system from which the backup was created.
> - The UCS restore operation restores the full configuration only if the hostname of the target system matches the hostname on which the UCS archive was created. If the hostname does not match, only the shared configuration is restored. You can ensure hostnames match by using the `bigip_hostname` Ansible module in a task before using this module.
> - This module does not support re-licensing a BIG-IP restored from a UCS.
> - This module does not support restoring encrypted archives on replacement RMA unit.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ucs_module.md#id4)

```yaml+jinja
- name: Upload UCS
  bigip_ucs:
    ucs: /root/bigip.localhost.localdomain.ucs
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Install (upload, install) UCS.
  bigip_ucs:
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Install (upload, install) UCS without installing the license portion
  bigip_ucs:
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    no_license: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Install (upload, install) UCS except the license, and bypassing the platform check
  bigip_ucs:
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    no_license: yes
    no_platform_check: yes
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Install (upload, install) UCS using a passphrase necessary to load the UCS
  bigip_ucs:
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    passphrase: MyPassphrase1234
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove uploaded UCS file
  bigip_ucs:
    ucs: bigip.localhost.localdomain.ucs
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
