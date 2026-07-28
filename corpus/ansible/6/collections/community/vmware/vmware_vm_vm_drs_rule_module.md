---
collection: ansible
version: "6"
title: "community.vmware.vmware_vm_vm_drs_rule module – Configure VMware DRS Affinity rule for virtual machines in the given cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vm_vm_drs_rule_module.html
fetched_at: 2026-07-27T17:22:57+00:00
---
# community.vmware.vmware_vm_vm_drs_rule module – Configure VMware DRS Affinity rule for virtual machines in the given cluster

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
> To use it in a playbook, specify: `community.vmware.vmware_vm_vm_drs_rule`.

- [Synopsis](vmware_vm_vm_drs_rule_module.md#synopsis)
- [Parameters](vmware_vm_vm_drs_rule_module.md#parameters)
- [Notes](vmware_vm_vm_drs_rule_module.md#notes)
- [Examples](vmware_vm_vm_drs_rule_module.md#examples)
- [Return Values](vmware_vm_vm_drs_rule_module.md#return-values)

## [Synopsis](vmware_vm_vm_drs_rule_module.md#id1)

- This module can be used to configure VMware DRS Affinity rule for virtual machines in the given cluster.

## [Parameters](vmware_vm_vm_drs_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **affinity_rule**  boolean | If set to `True`, the DRS rule will be an Affinity rule.  If set to `False`, the DRS rule will be an Anti-Affinity rule.  Effective only if `state` is set to `present`.  Choices:   - `false` - `true` ← (default) |
| **cluster_name**  string / required | Desired cluster name where virtual machines are present for the DRS rule. |
| **drs_rule_name**  string / required | The name of the DRS rule to manage. |
| **enabled**  boolean | If set to `True`, the DRS rule will be enabled.  Effective only if `state` is set to `present`.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **mandatory**  boolean | If set to `True`, the DRS rule will be mandatory.  Effective only if `state` is set to `present`.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, then the DRS rule is created if not present.  If set to `present`, then the DRS rule is already present, it updates to the given configurations.  If set to `absent`, then the DRS rule is deleted if present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vms**  list / elements=string | List of virtual machines name for which DRS rule needs to be applied.  Required if `state` is set to `present`. |

## [Notes](vmware_vm_vm_drs_rule_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vm_vm_drs_rule_module.md#id4)

```yaml+jinja
- name: Create DRS Affinity Rule for VM-VM
  community.vmware.vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    cluster_name: "{{ cluster_name }}"
    vms:
        - vm1
        - vm2
    drs_rule_name: vm1-vm2-affinity-rule-001
    enabled: True
    mandatory: True
    affinity_rule: True
  delegate_to: localhost

- name: Create DRS Anti-Affinity Rule for VM-VM
  community.vmware.vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    cluster_name: "{{ cluster_name }}"
    enabled: True
    vms:
        - vm1
        - vm2
    drs_rule_name: vm1-vm2-affinity-rule-001
    mandatory: True
    affinity_rule: False
  delegate_to: localhost

- name: Delete DRS Affinity Rule for VM-VM
  community.vmware.vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    cluster_name: "{{ cluster_name }}"
    drs_rule_name: vm1-vm2-affinity-rule-001
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_vm_vm_drs_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | metadata about DRS VM and VM rule  Returned: when state is present  Sample: `{"rule_enabled": false, "rule_key": 20, "rule_mandatory": true, "rule_name": "drs_rule_0014", "rule_uuid": "525f3bc0-253f-825a-418e-2ec93bffc9ae", "rule_vms": ["VM_65", "VM_146"]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
