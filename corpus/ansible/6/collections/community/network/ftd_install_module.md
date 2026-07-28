---
collection: ansible
version: "6"
title: "community.network.ftd_install module – Installs FTD pkg image on the firewall"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ftd_install_module.html
fetched_at: 2026-07-27T17:18:38+00:00
---
# community.network.ftd_install module – Installs FTD pkg image on the firewall

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](ftd_install_module.md#ansible-collections-community-network-ftd-install-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.ftd_install`.

- [Synopsis](ftd_install_module.md#synopsis)
- [Requirements](ftd_install_module.md#requirements)
- [Parameters](ftd_install_module.md#parameters)
- [Notes](ftd_install_module.md#notes)
- [Examples](ftd_install_module.md#examples)
- [Return Values](ftd_install_module.md#return-values)

## [Synopsis](ftd_install_module.md#id1)

- Provisioning module for FTD devices that installs ROMMON image (if needed) and FTD pkg image on the firewall.
- Can be used with `httpapi` and `local` connection types. The `httpapi` is preferred, the `local` connection should be used only when the device cannot be accessed via REST API.

## [Requirements](ftd_install_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.5
- firepower-kickstart

## [Parameters](ftd_install_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **console_ip**  string / required | IP address of a terminal server.  Used to set up an SSH connection with device’s console port through the terminal server. |
| **console_password**  string / required | Password to login on a terminal server. |
| **console_port**  string / required | Device’s port on a terminal server. |
| **console_username**  string / required | Username to login on a terminal server. |
| **device_gateway**  string | Device gateway of management interface.  If not specified and connection is ‘httpapi`, the module tries to fetch the existing value via REST API.  For ‘local’ connection type, this parameter is mandatory. |
| **device_hostname**  string / required | Hostname of the device as appears in the prompt (e.g., ‘firepower-5516’). |
| **device_ip**  string | Device IP address of management interface.  If not specified and connection is ‘httpapi`, the module tries to fetch the existing value via REST API.  For ‘local’ connection type, this parameter is mandatory. |
| **device_model**  string | Platform model of the device (e.g., ‘Cisco ASA5506-X Threat Defense’).  If not specified and connection is ‘httpapi`, the module tries to fetch the device model via REST API.  For ‘local’ connection type, this parameter is mandatory.  Choices:   - `"Cisco ASA5506-X Threat Defense"` - `"Cisco ASA5508-X Threat Defense"` - `"Cisco ASA5516-X Threat Defense"` - `"Cisco Firepower 2110 Threat Defense"` - `"Cisco Firepower 2120 Threat Defense"` - `"Cisco Firepower 2130 Threat Defense"` - `"Cisco Firepower 2140 Threat Defense"` |
| **device_netmask**  string | Device netmask of management interface.  If not specified and connection is ‘httpapi`, the module tries to fetch the existing value via REST API.  For ‘local’ connection type, this parameter is mandatory. |
| **device_new_password**  string | New device password to set after image installation.  If not specified, current password from `device_password` property is reused.  Not applicable for ASA5500-X series devices. |
| **device_password**  string / required | Password to login on the device. |
| **device_sudo_password**  string | Root password for the device. If not specified, `device_password` is used. |
| **device_username**  string | Username to login on the device.  Defaulted to ‘admin’ if not specified.  Default: `"admin"` |
| **dns_server**  string | DNS IP address of management interface.  If not specified and connection is ‘httpapi`, the module tries to fetch the existing value via REST API.  For ‘local’ connection type, this parameter is mandatory. |
| **force_install**  boolean | Forces the FTD image to be installed even when the same version is already installed on the firewall.  By default, the module stops execution when the target version is installed in the device.  Choices:   - `false` ← (default) - `true` |
| **image_file_location**  string / required | Path to the FTD pkg image on the server to be downloaded.  FTP, SCP, SFTP, TFTP, or HTTP protocols are usually supported, but may depend on the device model. |
| **image_version**  string / required | Version of FTD image to be installed.  Helps to compare target and current FTD versions to prevent unnecessary reinstalls. |
| **rommon_file_location**  string / required | Path to the boot (ROMMON) image on TFTP server.  Only TFTP is supported. |
| **search_domains**  string | Search domains delimited by comma.  Defaulted to ‘cisco.com’ if not specified.  Default: `"cisco.com"` |

## [Notes](ftd_install_module.md#id4)

> **Note:**
>
> - Requires `firepower-kickstart` library that should be installed separately and requires Python >= 3.5.
> - On localhost, Ansible can be still run with Python >= 2.7, but the interpreter for this particular module must be Python >= 3.5.
> - Python interpreter for the module can overwritten in `ansible_python_interpreter` variable.

## [Examples](ftd_install_module.md#id5)

```yaml+jinja
- name: Install image v6.3.0 on FTD 5516
  community.network.ftd_install:
    device_hostname: firepower
    device_password: pass
    device_ip: 192.168.0.1
    device_netmask: 255.255.255.0
    device_gateway: 192.168.0.254
    dns_server: 8.8.8.8

    console_ip: 10.89.0.0
    console_port: 2004
    console_username: console_user
    console_password: console_pass

    rommon_file_location: 'tftp://10.89.0.11/installers/ftd-boot-9.10.1.3.lfbff'
    image_file_location: 'https://10.89.0.11/installers/ftd-6.3.0-83.pkg'
    image_version: 6.3.0-83
```

## [Return Values](ftd_install_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The message saying whether the image was installed or explaining why the installation failed.  Returned: always |

### Authors

- Cisco Systems, Inc. (@annikulin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
