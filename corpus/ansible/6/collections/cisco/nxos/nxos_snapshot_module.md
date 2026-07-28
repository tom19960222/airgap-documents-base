---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_snapshot module – Manage snapshots of the running states of selected features."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_snapshot_module.html
fetched_at: 2026-07-27T17:02:21+00:00
---
# cisco.nxos.nxos_snapshot module – Manage snapshots of the running states of selected features.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_snapshot`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_snapshot_module.md#synopsis)
- [Parameters](nxos_snapshot_module.md#parameters)
- [Notes](nxos_snapshot_module.md#notes)
- [Examples](nxos_snapshot_module.md#examples)
- [Return Values](nxos_snapshot_module.md#return-values)

## [Synopsis](nxos_snapshot_module.md#id1)

- Create snapshots of the running states of selected features, add new show commands for snapshot creation, delete and compare existing snapshots.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Define what snapshot action the module would perform.  Choices:   - `"add"` - `"compare"` - `"create"` - `"delete"` - `"delete_all"` |
| **compare_option**  string | Snapshot options to be used when `action=compare`.  Choices:   - `"summary"` - `"ipv4routes"` - `"ipv6routes"` |
| **comparison_results_file**  string | Name of the file where snapshots comparison will be stored when `action=compare`. |
| **description**  string | Snapshot description to be used when `action=create`. |
| **element_key1**  string | Specify the tags used to distinguish among row entries, to be used when `action=add`. |
| **element_key2**  string | Specify the tags used to distinguish among row entries, to be used when `action=add`. |
| **path**  string | Specify the path of the file where new created snapshot or snapshots comparison will be stored, to be used when `action=create` and `save_snapshot_locally=true` or `action=compare`.  Default: `"./"` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for NX-API.  This option will be removed in a release after 2022-06-01.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_nxos.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *nxapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *nxapi*. The port value will default to the appropriate transport common port if none is provided in the task. (cli=22, http=80, https=443). |
| **ssh_keyfile**  string | Specifies the SSH key to use to authenticate the connection to the remote device. This argument is only used for the *cli* transport. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc). |
| **transport**  string | Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or nxapi.  Choices:   - `"cli"` ← (default) - `"nxapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=nxapi`, otherwise this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not nxapi, this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **row_id**  string | Specifies the tag of each row entry of the show command’s XML output, to be used when `action=add`. |
| **save_snapshot_locally**  boolean | Specify to locally store a new created snapshot, to be used when `action=create`.  Choices:   - `false` ← (default) - `true` |
| **section**  string | Used to name the show command output, to be used when `action=add`. |
| **show_command**  string | Specify a new show command, to be used when `action=add`. |
| **snapshot1**  string | First snapshot to be used when `action=compare`. |
| **snapshot2**  string | Second snapshot to be used when `action=compare`. |
| **snapshot_name**  string | Snapshot name, to be used when `action=create` or `action=delete`. |

## [Notes](nxos_snapshot_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `transport=cli` may cause timeout errors.
> - The `element_key1` and `element_key2` parameter specify the tags used to distinguish among row entries. In most cases, only the element_key1 parameter needs to specified to be able to distinguish among row entries.
> - `action=compare` will always store a comparison report on a local file.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_snapshot_module.md#id4)

```yaml+jinja
# Create a snapshot and store it locally
- cisco.nxos.nxos_snapshot:
    action: create
    snapshot_name: test_snapshot
    description: Done with Ansible
    save_snapshot_locally: true
    path: /home/user/snapshots/

# Delete a snapshot
- cisco.nxos.nxos_snapshot:
    action: delete
    snapshot_name: test_snapshot

# Delete all existing snapshots
- cisco.nxos.nxos_snapshot:
    action: delete_all

# Add a show command for snapshots creation
- cisco.nxos.nxos_snapshot:
    section: myshow
    show_command: show ip interface brief
    row_id: ROW_intf
    element_key1: intf-name

# Compare two snapshots
- cisco.nxos.nxos_snapshot:
    action: compare
    snapshot1: pre_snapshot
    snapshot2: post_snapshot
    comparison_results_file: compare_snapshots.txt
    compare_option: summary
    path: ../snapshot_reports/
```

## [Return Values](nxos_snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: verbose mode  Sample: `["snapshot create post_snapshot Post-snapshot"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
