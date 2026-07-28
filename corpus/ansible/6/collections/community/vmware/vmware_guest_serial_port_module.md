---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_serial_port module – Manage serial ports on an existing VM"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_serial_port_module.html
fetched_at: 2026-07-27T17:22:03+00:00
---
# community.vmware.vmware_guest_serial_port module – Manage serial ports on an existing VM

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_serial_port`.

- [Synopsis](vmware_guest_serial_port_module.md#synopsis)
- [Parameters](vmware_guest_serial_port_module.md#parameters)
- [Notes](vmware_guest_serial_port_module.md#notes)
- [Examples](vmware_guest_serial_port_module.md#examples)
- [Return Values](vmware_guest_serial_port_module.md#return-values)

## [Synopsis](vmware_guest_serial_port_module.md#id1)

- This module can be used to manage serial ports on an existing VM

## [Parameters](vmware_guest_serial_port_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backings**  list / elements=dictionary / required | A list of backings for serial ports.  `backing_type` (str): is required to add or reconfigure or remove an existing serial port. |
| **backing_type**  aliases: type  string / required | Backing type is required for the serial ports to be added or reconfigured or removed. |
| **device_name**  string | Serial device absolutely path.  Required when *backing_type=device*. |
| **direction**  string | The direction of the connection.  Required when *backing_type=network*.  Choices:   - `"client"` ← (default) - `"server"` |
| **endpoint**  string | When you use serial port pipe backing to connect a virtual machine to another process, you must define the endpoints.  Required when *backing_type=pipe*.  Choices:   - `"client"` ← (default) - `"server"` |
| **file_path**  string | File path for the host file used in this backing. Fully qualified path is required, like <datastore_name>/<file_name>.  Required when *backing_type=file*. |
| **no_rx_loss**  boolean | Enables optimized data transfer over the pipe.  Required when *backing_type=pipe*.  Choices:   - `false` ← (default) - `true` |
| **pipe_name**  string | Pipe name for the host pipe.  Required when *backing_type=pipe*. |
| **service_uri**  string | Identifies the local host or a system on the network, depending on the value of *direction*.  If you use the virtual machine as a server, the URI identifies the host on which the virtual machine runs.  In this case, the host name part of the URI should be empty, or it should specify the address of the local host.  If you use the virtual machine as a client, the URI identifies the remote system on the network.  Required when *backing_type=network*. |
| **state**  string | `state` is required to identify whether we are adding, modifying or removing the serial port.  If `state` is set to `present`, a serial port will be added or modified.  If `state` is set to `absent`, an existing serial port will be removed.  If an existing serial port to modify or remove, `backing_type` and either of `service_uri` or `pipe_name` or `device_name` or `file_path` are required.  Choices:   - `"present"` ← (default) - `"absent"` |
| **yield_on_poll**  boolean | Enables CPU yield behavior.  Choices:   - `false` - `true` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage the serial ports, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_serial_port_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_serial_port_module.md#id4)

```yaml+jinja
# Create serial ports
- name: Create multiple serial ports with Backing type - network, pipe, device and file
  community.vmware.vmware_guest_serial_port:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "test_vm1"
    backings:
    - type: 'network'
      direction: 'client'
      service_uri: 'tcp://6000'
      yield_on_poll: True
    - type: 'pipe'
      pipe_name: 'serial_pipe'
      endpoint: 'client'
    - type: 'device'
      device_name: '/dev/char/serial/uart0'
    - type: 'file'
      file_path: '[datastore1]/file1'
      yield_on_poll:  True
    register: create_multiple_ports

# Modify existing serial port
- name: Modify Network backing type
  community.vmware.vmware_guest_serial_port:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: '{{ name }}'
    backings:
    - type: 'network'
      state: 'present'
      direction: 'server'
      service_uri: 'tcp://6000'
  delegate_to: localhost

# Remove serial port
- name: Remove pipe backing type
  community.vmware.vmware_guest_serial_port:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: '{{ name }}'
    backings:
    - type: 'pipe'
      state: 'absent'
  delegate_to: localhost
```

## [Return Values](vmware_guest_serial_port_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **serial_port_data**  dictionary | metadata about the virtual machine’s serial ports after managing them  Returned: always  Sample: `[{"backing_type": "network", "direction": "client", "service_uri": "tcp://6000"}, {"backing_type": "pipe", "direction": "server", "pipe_name": "serial pipe"}]` |

### Authors

- Anusha Hegde (@anusha94)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
