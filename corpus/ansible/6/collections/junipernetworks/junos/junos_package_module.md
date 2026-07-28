---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_package module – Installs packages on remote devices running Junos"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_package_module.html
fetched_at: 2026-07-27T17:54:32+00:00
---
# junipernetworks.junos.junos_package module – Installs packages on remote devices running Junos

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_package_module.md#ansible-collections-junipernetworks-junos-junos-package-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_package`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_package_module.md#synopsis)
- [Requirements](junos_package_module.md#requirements)
- [Parameters](junos_package_module.md#parameters)
- [Notes](junos_package_module.md#notes)
- [Examples](junos_package_module.md#examples)

## [Synopsis](junos_package_module.md#id1)

- This module can install new and updated packages on remote devices running Junos. The module will compare the specified package with the one running on the remote device and install the specified version if there is a mismatch

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_package_module.md#id2)

The below requirements are needed on the host that executes this module.

- junos-eznc
- ncclient (>=v0.5.2)

## [Parameters](junos_package_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | The *force* argument instructs the module to bypass the package version check and install the packaged identified in *src* on the remote device.  Choices:   - `false` ← (default) - `true` |
| **force_host**  boolean | The *force_host* argument controls the way software package or bundle is added on remote JUNOS host and is applicable for JUNOS QFX5100 device. If the value is set to `True` it will ignore any warnings while adding the host software package or bundle.  Choices:   - `false` ← (default) - `true` |
| **issu**  boolean | The *issu* argument is a boolean flag when set to `True` allows unified in-service software upgrade (ISSU) feature which enables you to upgrade between two different Junos OS releases with no disruption on the control plane and with minimal disruption of traffic.  Choices:   - `false` ← (default) - `true` |
| **no_copy**  boolean | The *no_copy* argument is responsible for instructing the remote device on where to install the package from. When enabled, the package is transferred to the remote device prior to installing.  Choices:   - `false` ← (default) - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **reboot**  boolean | In order for a package to take effect, the remote device must be restarted. When enabled, this argument will instruct the module to reboot the device once the updated package has been installed. If disabled or the remote package does not need to be changed, the device will not be started.  Choices:   - `false` - `true` ← (default) |
| **src**  aliases: package  path / required | The *src* argument specifies the path to the source package to be installed on the remote device in the advent of a version mismatch. The *src* argument can be either a localized path or a full path to the package file to install. |
| **ssh_config**  path | The `ssh_config` argument is path to the SSH configuration file. This can be used to load SSH information from a configuration file. If this option is not given by default ~/.ssh/config is queried. |
| **ssh_private_key_file**  path | The `ssh_private_key_file` argument is path to the SSH private key file. This can be used if you need to provide a private key rather than loading the key into the ssh-key-ring/environment |
| **validate**  boolean | The *validate* argument is responsible for instructing the remote device to skip checking the current device configuration compatibility with the package being installed. When set to false validation is not performed.  Choices:   - `false` - `true` ← (default) |
| **version**  string | The *version* argument can be used to explicitly specify the version of the package that should be installed on the remote device. If the *version* argument is not specified, then the version is extracts from the *src* filename. |

## [Notes](junos_package_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Works with `local` connections only.
> - Since this module uses junos-eznc to establish connection with junos device the netconf configuration parameters needs to be passed using module options for example `ssh_config` unlike other junos modules that uses `netconf` connection type.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_package_module.md#id5)

```yaml+jinja
# the required set of connection arguments have been purposely left off
# the examples for brevity

- name: install local package on remote device
  junipernetworks.junos.junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz

- name: install local package on remote device without rebooting
  junipernetworks.junos.junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz
    reboot: no

- name: install local package on remote device with jumpost
  junipernetworks.junos.junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz
    ssh_config: /home/user/customsshconfig
```

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
