---
collection: ansible
version: "6"
title: "vmware.vmware_rest.vcenter_vm_hardware_serial module – Adds a virtual serial port to the virtual machine."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/vcenter_vm_hardware_serial_module.html
fetched_at: 2026-07-28T00:22:37+00:00
---
# vmware.vmware_rest.vcenter_vm_hardware_serial module – Adds a virtual serial port to the virtual machine.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/vmware/vmware_rest) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_hardware_serial_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-hardware-serial-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_hardware_serial`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_hardware_serial_module.md#synopsis)
- [Requirements](vcenter_vm_hardware_serial_module.md#requirements)
- [Parameters](vcenter_vm_hardware_serial_module.md#parameters)
- [Notes](vcenter_vm_hardware_serial_module.md#notes)
- [Examples](vcenter_vm_hardware_serial_module.md#examples)
- [Return Values](vcenter_vm_hardware_serial_module.md#return-values)

## [Synopsis](vcenter_vm_hardware_serial_module.md#id1)

- Adds a virtual serial port to the virtual machine.

## [Requirements](vcenter_vm_hardware_serial_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_hardware_serial_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_guest_control**  boolean | Flag indicating whether the guest can connect and disconnect the device.  Choices:   - `false` - `true` |
| **backing**  dictionary | Physical resource backing for the virtual serial port. Required with *state=[‘present’]*  Valid attributes are:  - `type` (str): The `backing_type` defines the valid backing types for a virtual serial port. ([‘present’])  This key is required with [‘present’].    - Accepted values:      - FILE     - HOST_DEVICE     - NETWORK_CLIENT     - NETWORK_SERVER     - PIPE_CLIENT     - PIPE_SERVER - `file` (str): Path of the file backing the virtual serial port. ([‘present’]) - `host_device` (str): Name of the device backing the virtual serial port. ([‘present’]) - `pipe` (str): Name of the pipe backing the virtual serial port. ([‘present’]) - `no_rx_loss` (bool): Flag that enables optimized data transfer over the pipe. When the value is true, the host buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss. ([‘present’]) - `network_location` (str): URI specifying the location of the network service backing the virtual serial port. <ul> <li>If [{@link](mailto:{%40link) #type} is [{@link](mailto:{%40link) BackingType#NETWORK_SERVER}, this field is the location used by clients to connect to this server. The hostname part of the URI should either be empty or should specify the address of the host on which the virtual machine is running.</li> <li>If [{@link](mailto:{%40link) #type} is [{@link](mailto:{%40link) BackingType#NETWORK_CLIENT}, this field is the location used by the virtual machine to connect to the remote server.</li> </ul> ([‘present’]) - `proxy` (str): Proxy service that provides network access to the network backing. If set, the virtual machine initiates a connection with the proxy service and forwards the traffic to the proxy. ([‘present’]) |
| **label**  string | The name of the item |
| **port**  string | Virtual serial port identifier. Required with *state=[‘absent’, ‘connect’, ‘disconnect’, ‘present’]* |
| **session_timeout**  float  added in vmware.vmware_rest 2.1.0 | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **start_connected**  boolean | Flag indicating whether the virtual device should be connected whenever the virtual machine is powered on.  Choices:   - `false` - `true` |
| **state**  string | Choices:   - `"absent"` - `"connect"` - `"disconnect"` - `"present"` ← (default) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vm**  string / required | Virtual machine identifier. This parameter is mandatory. |
| **yield_on_poll**  boolean | CPU yield behavior. If set to true, the virtual machine will periodically relinquish the processor if its sole task is polling the virtual serial port. The amount of time it takes to regain the processor will depend on the degree of other virtual machine activity on the host. This field may be modified at any time, and changes applied to a connected virtual serial port take effect immediately.  Choices:   - `false` - `true` |

## [Notes](vcenter_vm_hardware_serial_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_hardware_serial_module.md#id5)

```yaml+jinja
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Create a new serial port
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 2
    allow_guest_control: true

- name: Create another serial port with a label
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 2
    allow_guest_control: true

- name: Create an existing serial port (label)
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 1
    allow_guest_control: true

- name: Get an existing serial port (label)
  vmware.vmware_rest.vcenter_vm_hardware_serial_info:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 1
  register: serial_port_1

- name: Delete an existing serial port (port id)
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    port: '{{ serial_port_1.id }}'
    state: absent

- name: Delete an existing serial port (label)
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 2
    state: absent
```

## [Return Values](vcenter_vm_hardware_serial_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | moid of the resource  Returned: On success  Sample: `"9000"` |
| **value**  dictionary | Create an existing serial port (label)  Returned: On success  Sample: `{"allow_guest_control": 1, "backing": {"auto_detect": 1, "host_device": "", "type": "HOST_DEVICE"}, "label": "Serial port 1", "start_connected": 0, "state": "NOT_CONNECTED", "yield_on_poll": 0}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
[Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
