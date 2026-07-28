---
collection: ansible
version: "8"
title: "community.vmware.vmware_dvswitch_info module – Gathers info dvswitch configurations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_dvswitch_info_module.html
fetched_at: 2026-07-28T01:59:58+00:00
---
# community.vmware.vmware_dvswitch_info module – Gathers info dvswitch configurations

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
> To use it in a playbook, specify: `community.vmware.vmware_dvswitch_info`.

- [Synopsis](vmware_dvswitch_info_module.md#synopsis)
- [Parameters](vmware_dvswitch_info_module.md#parameters)
- [Notes](vmware_dvswitch_info_module.md#notes)
- [Examples](vmware_dvswitch_info_module.md#examples)
- [Return Values](vmware_dvswitch_info_module.md#return-values)

## [Synopsis](vmware_dvswitch_info_module.md#id1)

- This module can be used to gather information about dvswitch configurations.

## [Parameters](vmware_dvswitch_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **folder**  string | Specify a folder location of dvswitch to gather information from.  Examples:  folder: /datacenter1/network  folder: datacenter1/network  folder: /datacenter1/network/folder1  folder: datacenter1/network/folder1  folder: /folder1/datacenter1/network  folder: folder1/datacenter1/network  folder: /folder1/datacenter1/network/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  If not specified, all properties are retrieved (deeply).  Results are returned in a structure identical to the vsphere API.  Example:  properties: [  “summary.name”,  “summary.numPorts”,  “config.maxMtu”,  “overallStatus”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1  **Choices:**   - `"summary"` ← (default) - `"vsphere"` |
| **switch_name**  aliases: switch, dvswitch  string | Name of a dvswitch to look for.  If `switch_name` not specified gather all dvswitch information. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_dvswitch_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvswitch_info_module.md#id4)

```yaml+jinja
- name: Gather all registered dvswitch
  community.vmware.vmware_dvswitch_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: dvswitch_info

- name: Gather info about specific dvswitch
  community.vmware.vmware_dvswitch_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    switch_name: DVSwitch01
  delegate_to: localhost
  register: dvswitch_info

- name: Gather info from folder about specific dvswitch
  community.vmware.vmware_dvswitch_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /datacenter1/network/F01
    switch_name: DVSwitch02
  delegate_to: localhost
  register: dvswitch_info

- name: Gather some info from a dvswitch using the vSphere API output schema
  community.vmware.vmware_dvswitch_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    schema: vsphere
    properties:
      - summary.name
      - summary.numPorts
      - config.maxMtu
      - overallStatus
    switch_name: DVSwitch01
  register: dvswitch_info
```

## [Return Values](vmware_dvswitch_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distributed_virtual_switches**  list / elements=string | list of dictionary of dvswitch and their information  **Returned:** always  **Sample:** `[{"configure": {"folder": "network", "hosts": ["esxi-test-02.local", "esxi-test-01.local"], "settings": {"healthCheck": {"TeamingHealthCheckConfig": false, "VlanMtuHealthCheckConfig": false}, "netflow": {"activeFlowTimeout": 60, "collectorIpAddress": "", "collectorPort": 0, "idleFlowTimeout": 15, "internalFlowsOnly": false, "observationDomainId": 0, "samplingRate": 0, "switchIpAddress": null}, "privateVlan": [], "properties": {"administratorContact": {"contact": null, "name": null}, "advanced": {"maxMtu": 1500, "multicastFilteringMode": "legacyFiltering"}, "discoveryProtocol": {"operation": "listen", "protocol": "cdp"}, "general": {"ioControl": true, "name": "DVSwitch01", "numPorts": 10, "numUplinks": 1, "vendor": "VMware, Inc.", "version": "6.6.0"}}}}, "uuid": "50 30 99 9c a7 60 8a 4f-05 9f e7 b5 da df 8f 17"}]` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
