---
collection: ansible
version: "8"
title: "Introduction to Ansible for VMware"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/docsite/vmware_scenarios/vmware_intro.html
fetched_at: 2026-07-28T03:00:56+00:00
---
# Introduction to Ansible for VMware

- [Introduction](vmware_intro.md#introduction)
- [Requirements](vmware_intro.md#requirements)
- [vmware_guest module](vmware_intro.md#vmware-guest-module)

## [Introduction](vmware_intro.md#id2)

Ansible provides various modules to manage VMware infrastructure, which includes datacenter, cluster,
host system and virtual machine.

## [Requirements](vmware_intro.md#id3)

Ansible VMware modules are written on top of [pyVmomi](https://github.com/vmware/pyvmomi).
pyVmomi is the Python SDK for the VMware vSphere API that allows user to manage ESX, ESXi,
and vCenter infrastructure. You can install pyVmomi using pip (you may need to use pip3, depending on your OS/distro):

```bash
$ pip install pyvmomi
```

Ansible VMware modules leveraging latest vSphere(6.0+) features are using [vSphere Automation Python SDK](https://github.com/vmware/vsphere-automation-sdk-python). The vSphere Automation Python SDK also has client libraries, documentation, and sample code for VMware Cloud on AWS Console APIs, NSX VMware Cloud on AWS integration APIs, VMware Cloud on AWS site recovery APIs, NSX-T APIs.

You can install vSphere Automation Python SDK using pip:

```bash
$ pip install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git
```

Note:
:   Installing vSphere Automation Python SDK also installs `pyvmomi`. A separate installation of `pyvmomi` is not required.

## [vmware_guest module](vmware_intro.md#id4)

The [vmware_guest](../../vmware_guest_module.md#ansible-collections-community-vmware-vmware-guest-module) module manages various operations related to virtual machines in the given ESXi or vCenter server.

> **See also:**
>
> [pyVmomi](https://github.com/vmware/pyvmomi)
> :   The GitHub Page of pyVmomi
>
> [pyVmomi Issue Tracker](https://github.com/vmware/pyvmomi/issues)
> :   The issue tracker for the pyVmomi project
>
> [govc](https://github.com/vmware/govmomi/tree/master/govc)
> :   govc is a vSphere CLI built on top of govmomi
>
> [Working with playbooks](../../../../../playbook_guide/playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
