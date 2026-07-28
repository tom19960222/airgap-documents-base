---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_file_copy module – Copy a file to a remote NXOS device."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_file_copy_module.html
fetched_at: 2026-07-28T01:38:39+00:00
---
# cisco.nxos.nxos_file_copy module – Copy a file to a remote NXOS device.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
> You need further requirements to be able to use this module,
> see [Requirements](nxos_file_copy_module.md#ansible-collections-cisco-nxos-nxos-file-copy-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_file_copy`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_file_copy_module.md#synopsis)
- [Requirements](nxos_file_copy_module.md#requirements)
- [Parameters](nxos_file_copy_module.md#parameters)
- [Notes](nxos_file_copy_module.md#notes)
- [Examples](nxos_file_copy_module.md#examples)
- [Return Values](nxos_file_copy_module.md#return-values)

## [Synopsis](nxos_file_copy_module.md#id1)

- This module supports two different workflows for copying a file to flash (or bootflash) on NXOS devices. Files can either be (1) pushed from the Ansible controller to the device or (2) pulled from a remote SCP file server to the device. File copies are initiated from the NXOS device to the remote SCP server. This module only supports the use of connection `network_cli` or `Cli` transport with connection `local`.

Aliases: file_copy

## [Requirements](nxos_file_copy_module.md#id2)

The below requirements are needed on the host that executes this module.

- paramiko or libssh (required when file_pull is False)
- scp (required when file_pull is False)

## [Parameters](nxos_file_copy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **connect_ssh_port**  integer | **Deprecated**  This option has been deprecated and will be removed in a release after 2024-06-01.  To maintain backwards compatibility, this option will continue to override the value of *ansible_port* until removed.   ---   SSH server port used for file transfer.  Only used when *file_pull* is `True`.  **Default:** `22` |
| **file_pull**  boolean | When (False) file is copied from the Ansible controller to the NXOS device.  When (True) file is copied from a remote SCP server to the NXOS device. In this mode, the file copy is initiated from the NXOS device.  If the file is already present on the device it will be overwritten and therefore the operation is NOT idempotent.  **Choices:**   - `false` ← (default) - `true` |
| **file_pull_compact**  boolean | When file_pull is True, this is used to compact nxos image files. This option can only be used with nxos image files.  When (file_pull is False), this is not used.  **Choices:**   - `false` ← (default) - `true` |
| **file_pull_kstack**  boolean | When file_pull is True, this can be used to speed up file copies when the nxos running image supports the use-kstack option.  When (file_pull is False), this is not used.  **Choices:**   - `false` ← (default) - `true` |
| **file_pull_protocol**  string | When file_pull is True, this can be used to define the transfer protocol for copying file from remote to the NXOS device.  When (file_pull is False), this is not used.  **Choices:**   - `"scp"` ← (default) - `"sftp"` - `"ftp"` - `"http"` - `"https"` - `"tftp"` |
| **file_pull_timeout**  integer | **Deprecated**  This option has been deprecated and will be removed in a release after 2024-06-01.  To maintain backwards compatibility, this option will continue to override the value of *ansible_command_timeout* until removed.   ---   Use this parameter to set timeout in seconds, when transferring large files or when the network is slow.  When (file_pull is False), this is not used.  **Default:** `300` |
| **file_system**  string | The remote file system on the nxos device. If omitted, devices that support a *file_system* parameter will use their default values.  **Default:** `"bootflash:"` |
| **local_file**  path | When (file_pull is False) this is the path to the local file on the Ansible controller. The local directory must exist.  When (file_pull is True) this is the target file name on the NXOS device. |
| **local_file_directory**  path | When (file_pull is True) file is copied from a remote SCP server to the NXOS device, and written to this directory on the NXOS device. If the directory does not exist, it will be created under the file_system. This is an optional parameter.  When (file_pull is False), this is not used. |
| **remote_file**  path | When (file_pull is False) this is the remote file path on the NXOS device. If omitted, the name of the local file will be used. The remote directory must exist.  When (file_pull is True) this is the full path to the file on the remote SCP server to be copied to the NXOS device. |
| **remote_scp_server**  string | The remote scp server address when file_pull is True. This is required if file_pull is True.  When (file_pull is False), this is not used. |
| **remote_scp_server_password**  string | The remote scp server password when file_pull is True. This is required if file_pull is True.  When (file_pull is False), this is not used. |
| **remote_scp_server_user**  string | The remote scp server username when file_pull is True. This is required if file_pull is True.  When (file_pull is False), this is not used. |
| **vrf**  string | The VRF used to pull the file. Useful when no vrf management is defined.  This option is not applicable for MDS switches.  **Default:** `"management"` |

## [Notes](nxos_file_copy_module.md#id4)

> **Note:**
>
> - Tested against NXOS 7.0(3)I2(5), 7.0(3)I4(6), 7.0(3)I5(3), 7.0(3)I6(1), 7.0(3)I7(3), 6.0(2)A8(8), 7.0(3)F3(4), 7.3(0)D1(1), 8.3(0), 9.2, 9.3
> - Limited Support for Cisco MDS
> - When pushing files (file_pull is False) to the NXOS device, feature scp-server must be enabled.
> - When pulling files (file_pull is True) to the NXOS device, feature scp-server is not required.
> - When pulling files (file_pull is True) to the NXOS device, no transfer will take place if the file is already present.
> - Check mode will tell you if the file would be copied.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_file_copy_module.md#id5)

```yaml+jinja
# File copy from ansible controller to nxos device
- name: copy from server to device
  cisco.nxos.nxos_file_copy:
    local_file: ./test_file.txt
    remote_file: test_file.txt

# Initiate file copy from the nxos device to transfer file from an SCP server back to the nxos device
- name: initiate file copy from device
  cisco.nxos.nxos_file_copy:
    file_pull: true
    local_file: xyz
    local_file_directory: dir1/dir2/dir3
    remote_file: /mydir/abc
    remote_scp_server: 192.168.0.1
    remote_scp_server_user: myUser
    remote_scp_server_password: myPassword
    vrf: management

# Initiate file copy from the nxos device to transfer file from a ftp server back to the nxos device.
# remote_scp_server_user and remote_scp_server_password are used to login to the FTP server.
- name: initiate file copy from device
  cisco.nxos.nxos_file_copy:
    file_pull: true
    file_pull_protocol: ftp
    local_file: xyz
    remote_file: /mydir/abc
    remote_scp_server: 192.168.0.1
    remote_scp_server_user: myUser
    remote_scp_server_password: myPassword
    vrf: management
```

## [Return Values](nxos_file_copy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Indicates whether or not the file was copied.  **Returned:** success  **Sample:** `true` |
| **local_file**  string | The path of the local file.  **Returned:** success  **Sample:** `"/path/to/local/file"` |
| **remote_file**  string | The path of the remote file.  **Returned:** success  **Sample:** `"/path/to/remote/file"` |
| **remote_scp_server**  string | The name of the scp server when file_pull is True.  **Returned:** success  **Sample:** `"fileserver.example.com"` |
| **transfer_status**  string | Whether a file was transferred to the nxos device.  **Returned:** success  **Sample:** `"Sent"` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)
- Rewritten as a plugin by (@mikewiebe)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
