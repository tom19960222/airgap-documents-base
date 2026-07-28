---
collection: ansible
version: "8"
title: "How to run a virtual machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/docsite/vmware_rest_scenarios/vcenter/6_run_a_vm.html
fetched_at: 2026-07-28T03:01:13+00:00
---
# How to run a virtual machine

- Introduction
- Power information
- How to start a virtual machine
- How to wait until my virtual machine is ready

## Introduction

This section covers the power management of your virtual machine.

## Power information

Use `vcenter_vm_power_info` to know the power state of the VM.

```YAML+Jinja
- name: Get guest power information
  vmware.vmware_rest.vcenter_vm_power_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

response

```YAML+Jinja
{
    "changed": false,
    "value": {
        "clean_power_off": true,
        "state": "POWERED_OFF"
    }
}
```

## How to start a virtual machine

Use the `vcenter_vm_power` module to start your VM:

```YAML+Jinja
- name: Turn the power of the VM on
  vmware.vmware_rest.vcenter_vm_power:
    state: start
    vm: '{{ test_vm1_info.id }}'
```

response

```YAML+Jinja
{
    "changed": false,
    "value": {}
}
```

## How to wait until my virtual machine is ready

If your virtual machine runs VMware Tools, you can build a loop around
the `center_vm_tools_info` module:

```YAML+Jinja
- name: Wait until my VM is ready
  vmware.vmware_rest.vcenter_vm_tools_info:
    vm: '{{ test_vm1_info.id }}'
  register: vm_tools_info
  until:
  - vm_tools_info is not failed
  - vm_tools_info.value.run_state == "RUNNING"
  retries: 60
  delay: 5
```

response

```YAML+Jinja
{
    "attempts": 8,
    "changed": false,
    "value": {
        "auto_update_supported": false,
        "install_attempt_count": 0,
        "install_type": "OPEN_VM_TOOLS",
        "run_state": "RUNNING",
        "upgrade_policy": "MANUAL",
        "version": "10346",
        "version_number": 10346,
        "version_status": "UNMANAGED"
    }
}
```
