---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_rpc module – Runs an arbitrary RPC over NetConf on an Juniper JUNOS device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_rpc_module.html
fetched_at: 2026-07-27T17:54:35+00:00
---
# junipernetworks.junos.junos_rpc module – Runs an arbitrary RPC over NetConf on an Juniper JUNOS device

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
> see [Requirements](junos_rpc_module.md#ansible-collections-junipernetworks-junos-junos-rpc-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_rpc`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_rpc_module.md#synopsis)
- [Requirements](junos_rpc_module.md#requirements)
- [Parameters](junos_rpc_module.md#parameters)
- [Notes](junos_rpc_module.md#notes)
- [Examples](junos_rpc_module.md#examples)
- [Return Values](junos_rpc_module.md#return-values)

## [Synopsis](junos_rpc_module.md#id1)

- Sends a request to the remote device running JUNOS to execute the specified RPC using the NetConf transport. The reply is then returned to the playbook in the `xml` key. If an alternate output format is requested, the reply is transformed to the requested output.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_rpc_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_rpc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **args**  dictionary | The `args` argument provides a set of arguments for the RPC call and are encoded in the request message. This argument accepts a set of key=value arguments. |
| **attrs**  dictionary | The `attrs` arguments defines a list of attributes and their values to set for the RPC call. This accepts a dictionary of key-values. |
| **output**  string | The `output` argument specifies the desired output of the return data. This argument accepts one of `xml`, `text`, or `json`. For `json`, the JUNOS device must be running a version of software that supports native JSON output.  Choices:   - `"xml"` ← (default) - `"json"` - `"text"` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **rpc**  string / required | The `rpc` argument specifies the RPC call to send to the remote devices to be executed. The RPC Reply message is parsed and the contents are returned to the playbook. |

## [Notes](junos_rpc_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_rpc_module.md#id5)

```yaml+jinja
- name: collect interface information using rpc
  junipernetworks.junos.junos_rpc:
    rpc: get-interface-information
    args:
      interface-name: em0
      media: true

- name: get system information
  junipernetworks.junos.junos_rpc:
    rpc: get-system-information

- name: load configuration
  junipernetworks.junos.junos_rpc:
    rpc: load-configuration
    attrs:
      action: override
      url: /tmp/config.conf
```

## [Return Values](junos_rpc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  string | The rpc rely converted to the output format.  Returned: always |
| **output_lines**  list / elements=string | The text output split into lines for readability.  Returned: always |
| **xml**  string | The xml return string from the rpc request.  Returned: always |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
