---
collection: ansible
version: "6"
title: "How to configure the VMware tools of a running virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/vm_tool_configuration.html
fetched_at: 2026-07-27T16:41:05+00:00
---
# How to configure the VMware tools of a running virtual machine

- [Introduction](vm_tool_configuration.md#introduction)
- [Scenario requirements](vm_tool_configuration.md#scenario-requirements)
- [How to change the upgrade policy](vm_tool_configuration.md#how-to-change-the-upgrade-policy)

  - [Change the upgrade policy to MANUAL](vm_tool_configuration.md#change-the-upgrade-policy-to-manual)

    - [Result](vm_tool_configuration.md#result)
  - [Change the upgrade policy to UPGRADE_AT_POWER_CYCLE](vm_tool_configuration.md#change-the-upgrade-policy-to-upgrade-at-power-cycle)

    - [Result](vm_tool_configuration.md#id1)

## [Introduction](vm_tool_configuration.md#id2)

This section show you how to collection information from a running virtual machine.

## [Scenario requirements](vm_tool_configuration.md#id3)

You’ve already followed [How to run a virtual machine](run_a_vm.md#vmware-rest-run-a-vm) and your virtual machine runs VMware Tools.

## [How to change the upgrade policy](vm_tool_configuration.md#id4)

### [Change the upgrade policy to MANUAL](vm_tool_configuration.md#id5)

You can adjust the VMware Tools upgrade policy with the `vcenter_vm_tools` module.

```YAML+Jinja
- name: Change vm-tools upgrade policy to MANUAL
  vmware.vmware_rest.vcenter_vm_tools:
    vm: '{{ test_vm1_info.id }}'
    upgrade_policy: MANUAL
  register: _result
```

#### [Result](vm_tool_configuration.md#id6)

```YAML+Jinja
{
    "id": null,
    "changed": true
}
```

### [Change the upgrade policy to UPGRADE_AT_POWER_CYCLE](vm_tool_configuration.md#id7)

```YAML+Jinja
- name: Change vm-tools upgrade policy to UPGRADE_AT_POWER_CYCLE
  vmware.vmware_rest.vcenter_vm_tools:
    vm: '{{ test_vm1_info.id }}'
    upgrade_policy: UPGRADE_AT_POWER_CYCLE
  register: _result
```

#### [Result](vm_tool_configuration.md#id8)

```YAML+Jinja
{
    "id": null,
    "changed": true
}
```
