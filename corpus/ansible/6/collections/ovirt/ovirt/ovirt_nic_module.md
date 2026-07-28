---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_nic module – Module to manage network interfaces of Virtual Machines in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_nic_module.html
fetched_at: 2026-07-28T00:17:39+00:00
---
# ovirt.ovirt.ovirt_nic module – Module to manage network interfaces of Virtual Machines in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ovirt/ovirt) (version 2.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_nic_module.md#ansible-collections-ovirt-ovirt-ovirt-nic-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_nic`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_nic_module.md#synopsis)
- [Requirements](ovirt_nic_module.md#requirements)
- [Parameters](ovirt_nic_module.md#parameters)
- [Notes](ovirt_nic_module.md#notes)
- [Examples](ovirt_nic_module.md#examples)
- [Return Values](ovirt_nic_module.md#return-values)

## [Synopsis](ovirt_nic_module.md#id1)

- Module to manage network interfaces of Virtual Machines in oVirt/RHV.

## [Requirements](ovirt_nic_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_nic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  Choices:   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  Choices:   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  Choices:   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **id**  string | ID of the nic to manage. |
| **interface**  string | Type of the network interface. For example e1000, pci_passthrough, rtl8139, rtl8139_virtio, spapr_vlan or virtio.  It’s required parameter when creating the new NIC. |
| **linked**  boolean | Defines if the NIC is linked to the virtual machine.  Choices:   - `false` - `true` |
| **mac_address**  string | Custom MAC address of the network interface, by default it’s obtained from MAC pool. |
| **name**  string / required | Name of the network interface to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **network**  string | Logical network to which the VM network interface should use, by default Empty network is used if network is not specified. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **profile**  string | Virtual network interface profile to be attached to VM network interface.  When not specified and network has only single profile it will be auto-selected, otherwise you must specify profile. |
| **state**  string | Should the Virtual Machine NIC be present/absent/plugged/unplugged.  Choices:   - `"absent"` - `"plugged"` - `"present"` ← (default) - `"unplugged"` |
| **template**  string | Name of the template to manage.  You must provide either `vm` parameter or `template` parameter. |
| **template_version**  integer  added in ovirt.ovirt 1.2.0 | Version number of the template. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **vm**  string | Name of the Virtual Machine to manage.  You must provide either `vm` parameter or `template` parameter. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_nic_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_nic_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Add NIC to VM
  ovirt.ovirt.ovirt_nic:
    state: present
    vm: myvm
    name: mynic
    interface: e1000
    mac_address: 00:1a:4a:16:01:56
    profile: ovirtmgmt
    network: ovirtmgmt

- name: Plug NIC to VM
  ovirt.ovirt.ovirt_nic:
    state: plugged
    vm: myvm
    name: mynic

- name: Unplug NIC from VM
  ovirt.ovirt.ovirt_nic:
    state: unplugged
    linked: false
    vm: myvm
    name: mynic

- name: Add NIC to template
  ovirt.ovirt.ovirt_nic:
    auth: "{{ ovirt_auth }}"
    state: present
    template: my_template
    name: nic1
    interface: virtio
    profile: ovirtmgmt
    network: ovirtmgmt

- name: Remove NIC from VM
  ovirt.ovirt.ovirt_nic:
    state: absent
    vm: myvm
    name: mynic

# Change NIC Name
- ovirt.ovirt.ovirt_nic:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_nic_name"
    vm: myvm
```

## [Return Values](ovirt_nic_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the network interface which is managed  Returned: On success if network interface is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **nic**  dictionary | Dictionary of all the network interface attributes. Network interface attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/nic>.  Returned: On success if network interface is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
