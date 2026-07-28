---
collection: ansible
version: "6"
title: "Using VMware dynamic inventory plugin - Hostnames"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/docsite/vmware_scenarios/vmware_inventory_hostnames.html
fetched_at: 2026-07-28T00:25:15+00:00
---
# Using VMware dynamic inventory plugin - Hostnames

- [VMware dynamic inventory plugin - customizing hostnames](vmware_inventory_hostnames.md#vmware-dynamic-inventory-plugin-customizing-hostnames)

  - [Requirements](vmware_inventory_hostnames.md#requirements)
  - [What to expect](vmware_inventory_hostnames.md#what-to-expect)
  - [Troubleshooting](vmware_inventory_hostnames.md#troubleshooting)

## [VMware dynamic inventory plugin - customizing hostnames](vmware_inventory_hostnames.md#id2)

VMware inventory plugin allows you to configure hostnames using the `hostnames` configuration parameter.

In this scenario guide we will see how you configure hostnames from the given VMware guest in the inventory.

### [Requirements](vmware_inventory_hostnames.md#id3)

To use the VMware dynamic inventory plugins, you must install [pyVmomi](https://github.com/vmware/pyvmomi)
on your control node (the host running Ansible).

To include tag-related information for the virtual machines in your dynamic inventory, you also need the [vSphere Automation SDK](https://code.vmware.com/web/sdk/65/vsphere-automation-python), which supports REST API features such as tagging and content libraries, on your control node.
You can install the `vSphere Automation SDK` following [these instructions](https://github.com/vmware/vsphere-automation-sdk-python#installing-required-python-packages).

```bash
$ pip install pyvmomi
```

Starting in Ansible 2.10, the VMware dynamic inventory plugin is available in the `community.vmware` collection included Ansible.
To install the latest `community.vmware` collection:

```bash
$ ansible-galaxy collection install community.vmware
```

To use this VMware dynamic inventory plugin:

1. Enable it first by specifying the following in the `ansible.cfg` file:

```ini
[inventory]
enable_plugins = community.vmware.vmware_vm_inventory
```

2. Create a file that ends in `vmware.yml` or `vmware.yaml` in your working directory.

The `vmware_vm_inventory` inventory plugin takes in the same authentication information as any other VMware modules does.

Here’s an example of a valid inventory file with custom hostname for the given VMware guest:

```yaml
plugin: community.vmware.vmware_vm_inventory
strict: False
hostname: 10.65.223.31
username: administrator@vsphere.local
password: Esxi@123$%
validate_certs: False
with_tags: False
hostnames:
- config.name
```

Here, we have configured a custom hostname by setting the `hostnames` parameter to `config.name`. This will retrieve
the `config.name` property from the virtual machine and populate it in the inventory.

You can check all allowed properties for the given virtual machine at [Using Virtual machine attributes in VMware dynamic inventory plugin](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#vmware-inventory-vm-attributes "(in Ansible v5)").

Executing `ansible-inventory --list -i <filename>.vmware.yml` creates a list of the virtual machines that are ready to be configured using Ansible.

### [What to expect](vmware_inventory_hostnames.md#id4)

You will notice that instead of default behavior of representing the hostname as `config.name + _ + config.uuid`,
the inventory hosts show value as `config.name`.

```yaml
{
  "_meta": {
    "hostvars": {
        "template_001": {
            "config.name": "template_001",
            "guest.toolsRunningStatus": "guestToolsNotRunning",
            ...
            "guest.toolsStatus": "toolsNotInstalled",
            "name": "template_001"
        },
        "vm_8046": {
            "config.name": "vm_8046",
            "guest.toolsRunningStatus": "guestToolsNotRunning",
            ...
            "guest.toolsStatus": "toolsNotInstalled",
            "name": "vm_8046"
        },
    ...
}
```

### [Troubleshooting](vmware_inventory_hostnames.md#id5)

If the custom property specified in `hostnames` fails:

- Check if the values provided for username and password are correct.
- Make sure it is a valid property, see [Using Virtual machine attributes in VMware dynamic inventory plugin](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#vmware-inventory-vm-attributes "(in Ansible v5)").
- Use `strict: True` to get more information about the error.
- Please make sure that you are using latest version VMware collection.

> **See also:**
>
> [pyVmomi](https://github.com/vmware/pyvmomi)
> :   The GitHub Page of pyVmomi
>
> [pyVmomi Issue Tracker](https://github.com/vmware/pyvmomi/issues)
> :   The issue tracker for the pyVmomi project
>
> [vSphere Automation SDK GitHub Page](https://github.com/vmware/vsphere-automation-sdk-python)
> :   The GitHub Page of vSphere Automation SDK for Python
>
> [vSphere Automation SDK Issue Tracker](https://github.com/vmware/vsphere-automation-sdk-python/issues)
> :   The issue tracker for vSphere Automation SDK for Python
>
> [Using Virtual machine attributes in VMware dynamic inventory plugin](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#vmware-inventory-vm-attributes "(in Ansible v5)")
> :   Using Virtual machine attributes in VMware dynamic inventory plugin
>
> [Working with playbooks](../../../../../user_guide/playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
>
> [Using encrypted variables and files](../../../../../user_guide/vault.md#playbooks-vault)
> :   Using Vault in playbooks
