---
collection: ansible
version: "8"
title: "Ansible for VMware Concepts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/docsite/vmware_scenarios/vmware_concepts.html
fetched_at: 2026-07-28T03:00:57+00:00
---
# Ansible for VMware Concepts

Some of these concepts are common to all uses of Ansible, including VMware automation; some are specific to VMware. You need to understand them to use Ansible for VMware automation. This introduction provides the background you need to follow the [scenarios](https://docs.ansible.com/ansible/2.9/scenario_guides/vmware_scenarios/vmware_scenarios.html#vmware-scenarios "(in Ansible v2.9)") in this guide.

- [Control Node](vmware_concepts.md#control-node)
- [Delegation](vmware_concepts.md#delegation)
- [Modules](vmware_concepts.md#modules)
- [Playbooks](vmware_concepts.md#playbooks)
- [pyVmomi](vmware_concepts.md#pyvmomi)

## [Control Node](vmware_concepts.md#id2)

Any machine with Ansible installed. You can run commands and playbooks, invoking `/usr/bin/ansible` or `/usr/bin/ansible-playbook`, from any control node. You can use any computer that has Python installed on it as a control node - laptops, shared desktops, and servers can all run Ansible. However, you cannot use a Windows machine as a control node. You can have multiple control nodes.

## [Delegation](vmware_concepts.md#id3)

Delegation allows you to select the system that executes a given task. If you do not have `pyVmomi` installed on your control node, use the `delegate_to` keyword on VMware-specific tasks to execute them on any host where you have `pyVmomi` installed.

## [Modules](vmware_concepts.md#id4)

The units of code Ansible executes. Each module has a particular use, from creating virtual machines on vCenter to managing distributed virtual switches in the vCenter environment. You can invoke a single module with a task, or invoke several different modules in a playbook.

## [Playbooks](vmware_concepts.md#id5)

Ordered lists of tasks, saved so you can run those tasks in that order repeatedly. Playbooks can include variables as well as tasks. Playbooks are written in YAML and are easy to read, write, share and understand.

## [pyVmomi](vmware_concepts.md#id6)

Ansible VMware modules are written on top of [pyVmomi](https://github.com/vmware/pyvmomi). `pyVmomi` is the official Python SDK for the VMware vSphere API that allows user to manage ESX, ESXi, and vCenter infrastructure.

You need to install this Python SDK on host from where you want to invoke VMware automation. For example, if you are using control node then `pyVmomi` must be installed on control node.

If you are using any `delegate_to` host which is different from your control node then you need to install `pyVmomi` on that `delegate_to` node.

You can install pyVmomi using pip:

```bash
$ pip install pyvmomi
```
