---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_scp module – Transfer files from or to remote devices running Junos"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_scp_module.html
fetched_at: 2026-07-28T02:39:53+00:00
---
# junipernetworks.junos.junos_scp module – Transfer files from or to remote devices running Junos

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_scp_module.md#ansible-collections-junipernetworks-junos-junos-scp-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_scp`.

New in junipernetworks.junos 1.0.0

- [DEPRECATED](junos_scp_module.md#deprecated)
- [Synopsis](junos_scp_module.md#synopsis)
- [Requirements](junos_scp_module.md#requirements)
- [Parameters](junos_scp_module.md#parameters)
- [Notes](junos_scp_module.md#notes)
- [Examples](junos_scp_module.md#examples)
- [Return Values](junos_scp_module.md#return-values)
- [Status](junos_scp_module.md#status)

## [DEPRECATED](junos_scp_module.md#id1)

Removed in:
:   major release after 2025-01-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use [ansible.netcommon.net_get](../../ansible/netcommon/net_get_module.md#ansible-collections-ansible-netcommon-net-get-module), [ansible.netcommon.net_put](../../ansible/netcommon/net_put_module.md#ansible-collections-ansible-netcommon-net-put-module) instead.

## [Synopsis](junos_scp_module.md#id2)

- This module transfers files via SCP from or to remote devices running Junos.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: scp

## [Requirements](junos_scp_module.md#id3)

The below requirements are needed on the host that executes this module.

- junos-eznc
- ncclient (>=v0.5.2)

## [Parameters](junos_scp_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **dest**  path | The `dest` argument specifies the path in which to receive the files.  **Default:** `"."` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **recursive**  boolean | The `recursive` argument enables recursive transfer of files and directories.  **Choices:**   - `false` ← (default) - `true` |
| **remote_src**  boolean | The `remote_src` argument enables the download of files (*scp get*) from the remote device. The default behavior is to upload files (*scp put*) to the remote device.  **Choices:**   - `false` ← (default) - `true` |
| **src**  list / elements=path / required | The `src` argument takes a single path, or a list of paths to be transferred. The argument `recursive` must be `true` to transfer directories. |
| **ssh_config**  path | The `ssh_config` argument is path to the SSH configuration file. This can be used to load SSH information from a configuration file. If this option is not given by default ~/.ssh/config is queried. |
| **ssh_private_key_file**  path | The `ssh_private_key_file` argument is path to the SSH private key file. This can be used if you need to provide a private key rather than loading the key into the ssh-key-ring/environment |

## [Notes](junos_scp_module.md#id5)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vMX JUNOS version 17.3R1.10.
> - Works with `local` connections only.
> - Since this module uses junos-eznc to establish connection with junos device the netconf configuration parameters needs to be passed using module options for example `ssh_config` unlike other junos modules that uses `netconf` connection type.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_scp_module.md#id6)

```yaml+jinja
# the required set of connection arguments have been purposely left off
# the examples for brevity
- name: upload local file to home directory on remote device
  junipernetworks.junos.junos_scp:
    src: test.tgz

- name: upload local file to tmp directory on remote device
  junipernetworks.junos.junos_scp:
    src: test.tgz
    dest: /tmp/

- name: download file from remote device
  junipernetworks.junos.junos_scp:
    src: test.tgz
    remote_src: true

- name: ssh config file path for jumphost config
  junipernetworks.junos.junos_scp:
    src: test.tgz
    remote_src: true
    ssh_config: /home/user/customsshconfig
```

## [Return Values](junos_scp_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | always true  **Returned:** always |

## [Status](junos_scp_module.md#id8)

- This module will be removed in a major release after 2025-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](junos_scp_module.md#deprecated).

### Authors

- Christian Giese (@GIC-de)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
