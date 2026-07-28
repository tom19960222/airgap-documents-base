---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_info module – Gather info about a single VM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_info_module.html
fetched_at: 2026-07-28T02:00:14+00:00
---
# community.vmware.vmware_guest_info module – Gather info about a single VM

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_info`.

- [Synopsis](vmware_guest_info_module.md#synopsis)
- [Parameters](vmware_guest_info_module.md#parameters)
- [Notes](vmware_guest_info_module.md#notes)
- [Examples](vmware_guest_info_module.md#examples)
- [Return Values](vmware_guest_info_module.md#return-values)

## [Synopsis](vmware_guest_info_module.md#id1)

- Gather information about a single VM on a VMware ESX cluster.

## [Parameters](vmware_guest_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Destination datacenter for the deploy operation |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is required if name is supplied.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the VM to work with  This is required if `uuid` or `moid` is not supplied. |
| **name_match**  string | If multiple VMs matching the name, use the first or last found  **Choices:**   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  If not specified, all properties are retrieved (deeply).  Results are returned in a structure identical to the vsphere API.  Example:  properties: [  “config.hardware.memoryMB”,  “config.hardware.numCPU”,  “guest.disk”,  “overallStatus”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1  **Choices:**   - `"summary"` ← (default) - `"vsphere"` |
| **tag_details**  boolean | If set `true`, detail information about ‘tags’ returned.  Without this flag, the ‘tags’ returns a list of tag names.  With this flag, the ‘tags’ returns a list of dict about tag information with additional details like category name, category id, and tag id.  This parameter is added to maintain backward compatability.  **Choices:**   - `false` ← (default) - `true` |
| **tags**  boolean | Whether to show tags or not.  If set `true`, shows tags information. Returns a list of tag names.  If set `false`, hides tags information.  vSphere Automation SDK is required.  **Choices:**   - `false` ← (default) - `true` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s unique identifier.  This is required if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_info_module.md#id4)

```yaml+jinja
- name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
  delegate_to: localhost
  register: info

- name: Gather some info from a guest using the vSphere API output schema
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
    schema: "vsphere"
    properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
  delegate_to: localhost
  register: info

- name: Gather some information about a guest using MoID
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
    schema: "vsphere"
    properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
  delegate_to: localhost
  register: vm_moid_info

- name: Gather Managed object ID (moid) from a guest using the vSphere API output schema for REST Calls
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
    schema: "vsphere"
    properties:
      - _moId
  delegate_to: localhost
  register: moid_info

- name: Gather detailed information about tags and category associated with the given VM
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
    tags: true
    tag_details: true
  register: detailed_tag_info
```

## [Return Values](vmware_guest_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the virtual machine  **Returned:** always  **Sample:** `{"advanced_settings": {}, "annotation": "", "current_snapshot": null, "customvalues": {}, "guest_consolidation_needed": false, "guest_question": null, "guest_tools_status": "guestToolsNotRunning", "guest_tools_version": "10247", "hw_cores_per_socket": 1, "hw_datastores": ["ds_226_3"], "hw_esxi_host": "10.76.33.226", "hw_eth0": {"addresstype": "assigned", "ipaddresses": null, "label": "Network adapter 1", "macaddress": "00:50:56:87:a5:9a", "macaddress_dash": "00-50-56-87-a5-9a", "portgroup_key": null, "portgroup_portkey": null, "summary": "VM Network"}, "hw_files": ["[ds_226_3] ubuntu_t/ubuntu_t.vmx", "[ds_226_3] ubuntu_t/ubuntu_t.nvram", "[ds_226_3] ubuntu_t/ubuntu_t.vmsd", "[ds_226_3] ubuntu_t/vmware.log", "[ds_226_3] u0001/u0001.vmdk"], "hw_folder": "/DC0/vm/Discovered virtual machine", "hw_guest_full_name": null, "hw_guest_ha_state": null, "hw_guest_id": null, "hw_interfaces": ["eth0"], "hw_is_template": false, "hw_memtotal_mb": 1024, "hw_name": "ubuntu_t", "hw_power_status": "poweredOff", "hw_processor_count": 1, "hw_product_uuid": "4207072c-edd8-3bd5-64dc-903fd3a0db04", "hw_version": "vmx-13", "instance_uuid": "5007769d-add3-1e12-f1fe-225ae2a07caf", "ipv4": null, "ipv6": null, "module_hw": true, "moid": "vm-42", "snapshots": [], "tags": ["backup"], "vimref": "vim.VirtualMachine:vm-42", "vnc": {}}` |

### Authors

- Loic Blot (@nerzhul)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
