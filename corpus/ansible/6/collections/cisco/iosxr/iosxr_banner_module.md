---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_banner module – Module to configure multiline banners."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_banner_module.html
fetched_at: 2026-07-27T16:55:36+00:00
---
# cisco.iosxr.iosxr_banner module – Module to configure multiline banners.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
> You need further requirements to be able to use this module,
> see [Requirements](iosxr_banner_module.md#ansible-collections-cisco-iosxr-iosxr-banner-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_banner`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_banner_module.md#synopsis)
- [Requirements](iosxr_banner_module.md#requirements)
- [Parameters](iosxr_banner_module.md#parameters)
- [Notes](iosxr_banner_module.md#notes)
- [Examples](iosxr_banner_module.md#examples)
- [Return Values](iosxr_banner_module.md#return-values)

## [Synopsis](iosxr_banner_module.md#id1)

- This module will configure both exec and motd banners on remote device running Cisco IOS XR. It allows playbooks to add or remove banner text from the running configuration.

## [Requirements](iosxr_banner_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient >= 0.5.3 when using netconf
- lxml >= 4.1.1 when using netconf

## [Parameters](iosxr_banner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies the type of banner to configure on remote device.  Choices:   - `"login"` - `"motd"` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Specifies the type of connection based transport.  Choices:   - `"cli"` ← (default) - `"netconf"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | Existential state of the configuration on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **text**  string | Banner text to be configured. Accepts multi line string, without empty lines. When using a multi line string, the first and last characters must be the start and end delimiters for the banner Requires *state=present*. |

## [Notes](iosxr_banner_module.md#id4)

> **Note:**
>
> - This module works with connection `network_cli` and `netconf`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_banner_module.md#id5)

```yaml+jinja
- name: configure the login banner
  cisco.iosxr.iosxr_banner:
    banner: login
    text: |
      @this is my login banner
      that contains a multiline
      string@
    state: present
- name: remove the motd banner
  cisco.iosxr.iosxr_banner:
    banner: motd
    state: absent
- name: Configure banner from file
  cisco.iosxr.iosxr_banner:
    banner: motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present
```

## [Return Values](iosxr_banner_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands sent to device with transport `cli`  Returned: always (empty list when no commands to send)  Sample: `["banner login", "@this is my login banner", "that contains a multiline", "string@"]` |
| **xml**  list / elements=string | NetConf rpc xml sent to device with transport `netconf`  Returned: always (empty list when no xml rpc to send)  Sample: `["<config xmlns:xc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <banners xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-infra-infra-cfg\"> <banner xc:operation=\"merge\"> <banner-name>motd</banner-name> <banner-text>Ansible banner example</banner-text> </banner> </banners> </config>"]` |

### Authors

- Trishna Guha (@trishnaguha)
- Kedar Kekan (@kedarX)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
