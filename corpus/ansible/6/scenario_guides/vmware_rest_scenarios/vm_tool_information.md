---
collection: ansible
version: "6"
title: "How to get information from a running virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/vm_tool_information.html
fetched_at: 2026-07-27T16:43:19+00:00
---
# How to get information from a running virtual machine

- [Introduction](vm_tool_information.md#introduction)
- [Scenario requirements](vm_tool_information.md#scenario-requirements)
- [How to collect information](vm_tool_information.md#how-to-collect-information)

  - [Filesystem](vm_tool_information.md#filesystem)

    - [Result](vm_tool_information.md#result)
  - [Guest identity](vm_tool_information.md#guest-identity)

    - [Result](vm_tool_information.md#id1)
  - [Network](vm_tool_information.md#network)

    - [Result](vm_tool_information.md#id2)
  - [Network interfaces](vm_tool_information.md#network-interfaces)

    - [Result](vm_tool_information.md#id3)
  - [Network routes](vm_tool_information.md#network-routes)

    - [Result](vm_tool_information.md#id4)

## [Introduction](vm_tool_information.md#id5)

This section shows you how to collection information from a running virtual machine.

## [Scenario requirements](vm_tool_information.md#id6)

You’ve already followed [How to run a virtual machine](run_a_vm.md#vmware-rest-run-a-vm) and your virtual machine runs VMware Tools.

## [How to collect information](vm_tool_information.md#id7)

In this example, we use the `vcenter_vm_guest_*` module to collect information about the associated resources.

### [Filesystem](vm_tool_information.md#id8)

Here we use `vcenter_vm_guest_localfilesystem_info` to retrieve the details
about the filesystem of the guest. In this example we also use a `retries`
loop. The VMware Tools may take a bit of time to start and by doing so, we give
the VM a bit more time.

```YAML+Jinja
- name: Get guest filesystem information
  vmware.vmware_rest.vcenter_vm_guest_localfilesystem_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
  until:
  - _result is not failed
  retries: 60
  delay: 5
```

#### [Result](vm_tool_information.md#id9)

```YAML+Jinja
{
    "value": [
        {
            "value": {
                "mappings": [],
                "free_space": 774766592,
                "capacity": 2515173376
            },
            "key": "/"
        }
    ],
    "changed": false
}
```

### [Guest identity](vm_tool_information.md#id10)

You can use `vcenter_vm_guest_identity_info` to get details like the OS family or the hostname of the running VM.

```YAML+Jinja
- name: Get guest identity information
  vmware.vmware_rest.vcenter_vm_guest_identity_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

#### [Result](vm_tool_information.md#id11)

```YAML+Jinja
{
    "value": {
        "full_name": {
            "args": [],
            "default_message": "Red Hat Fedora (64-bit)",
            "id": "vmsg.guestos.fedora64Guest.label"
        },
        "name": "FEDORA_64",
        "ip_address": "192.168.122.242",
        "family": "LINUX",
        "host_name": "localhost.localdomain"
    },
    "changed": false
}
```

### [Network](vm_tool_information.md#id12)

`vcenter_vm_guest_networking_info` will return the OS network configuration.

```YAML+Jinja
- name: Get guest networking information
  vmware.vmware_rest.vcenter_vm_guest_networking_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

#### [Result](vm_tool_information.md#id13)

```YAML+Jinja
{
    "value": {
        "dns": {
            "ip_addresses": [
                "10.0.2.3"
            ],
            "search_domains": [
                "localdomain"
            ]
        },
        "dns_values": {
            "domain_name": "localdomain",
            "host_name": "localhost.localdomain"
        }
    },
    "changed": false
}
```

### [Network interfaces](vm_tool_information.md#id14)

`vcenter_vm_guest_networking_interfaces_info` will return a list of NIC configurations.

See also [How to attach a VM to a network](vm_hardware_tuning.md#vmware-rest-attach-a-network).

```YAML+Jinja
- name: Get guest network interfaces information
  vmware.vmware_rest.vcenter_vm_guest_networking_interfaces_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

#### [Result](vm_tool_information.md#id15)

```YAML+Jinja
{
    "value": [
        {
            "mac_address": "00:50:56:b3:49:5c",
            "ip": {
                "ip_addresses": [
                    {
                        "ip_address": "192.168.122.242",
                        "prefix_length": 24,
                        "state": "PREFERRED"
                    },
                    {
                        "ip_address": "fe80::b8d0:511b:897f:65a2",
                        "prefix_length": 64,
                        "state": "UNKNOWN"
                    }
                ]
            },
            "nic": "4000"
        }
    ],
    "changed": false
}
```

### [Network routes](vm_tool_information.md#id16)

Use `vcenter_vm_guest_networking_routes_info` to explore the route table of your virtual machine.

```YAML+Jinja
- name: Get guest network routes information
  vmware.vmware_rest.vcenter_vm_guest_networking_routes_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

#### [Result](vm_tool_information.md#id17)

```YAML+Jinja
{
    "value": [
        {
            "gateway_address": "192.168.122.1",
            "interface_index": 0,
            "prefix_length": 0,
            "network": "0.0.0.0"
        },
        {
            "interface_index": 0,
            "prefix_length": 24,
            "network": "192.168.122.0"
        },
        {
            "interface_index": 0,
            "prefix_length": 64,
            "network": "fe80::"
        },
        {
            "interface_index": 0,
            "prefix_length": 128,
            "network": "fe80::b8d0:511b:897f:65a2"
        },
        {
            "interface_index": 0,
            "prefix_length": 8,
            "network": "ff00::"
        }
    ],
    "changed": false
}
```
