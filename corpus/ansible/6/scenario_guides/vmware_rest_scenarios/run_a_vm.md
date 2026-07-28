---
collection: ansible
version: "6"
title: "How to run a virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/run_a_vm.html
fetched_at: 2026-07-27T16:43:19+00:00
---
# How to run a virtual machine

- [Introduction](run_a_vm.md#introduction)
- [Power information](run_a_vm.md#power-information)

  - [Result](run_a_vm.md#result)
- [How to start a virtual machine](run_a_vm.md#how-to-start-a-virtual-machine)

  - [Result](run_a_vm.md#id1)
- [How to wait until my virtual machine is ready](run_a_vm.md#how-to-wait-until-my-virtual-machine-is-ready)

  - [Result](run_a_vm.md#id2)

## [Introduction](run_a_vm.md#id3)

This section covers the power management of your virtual machine.

## [Power information](run_a_vm.md#id4)

Use `vcenter_vm_power_info` to know the power state of the VM.

```YAML+Jinja
- name: Get guest power information
  vmware.vmware_rest.vcenter_vm_power_info:
    vm: '{{ test_vm1_info.id }}'
  register: _result
```

### [Result](run_a_vm.md#id5)

```YAML+Jinja
{
    "value": {
        "state": "POWERED_ON"
    },
    "changed": false
}
```

## [How to start a virtual machine](run_a_vm.md#id6)

Use the `vcenter_vm_power` module to start your VM:

```YAML+Jinja
- name: Turn the power of the VM on
  vmware.vmware_rest.vcenter_vm_power:
    state: start
    vm: '{{ test_vm1_info.id }}'
```

### [Result](run_a_vm.md#id7)

```YAML+Jinja
{
    "changed": false
}
```

## [How to wait until my virtual machine is ready](run_a_vm.md#id8)

If your virtual machine runs VMware Tools, you can build a loop
around the `center_vm_tools_info` module:

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

### [Result](run_a_vm.md#id9)

```YAML+Jinja
{
    "value": {
        "auto_update_supported": false,
        "upgrade_policy": "MANUAL",
        "install_attempt_count": 0,
        "version_status": "UNMANAGED",
        "version_number": 10346,
        "run_state": "RUNNING",
        "version": "10346",
        "install_type": "OPEN_VM_TOOLS"
    },
    "changed": false
}
```
