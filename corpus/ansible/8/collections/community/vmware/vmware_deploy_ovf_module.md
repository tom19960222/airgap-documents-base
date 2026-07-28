---
collection: ansible
version: "8"
title: "community.vmware.vmware_deploy_ovf module – Deploys a VMware virtual machine from an OVF or OVA file, placed on file system or HTTP server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_deploy_ovf_module.html
fetched_at: 2026-07-28T01:59:51+00:00
---
# community.vmware.vmware_deploy_ovf module – Deploys a VMware virtual machine from an OVF or OVA file, placed on file system or HTTP server

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
> To use it in a playbook, specify: `community.vmware.vmware_deploy_ovf`.

- [Synopsis](vmware_deploy_ovf_module.md#synopsis)
- [Parameters](vmware_deploy_ovf_module.md#parameters)
- [Notes](vmware_deploy_ovf_module.md#notes)
- [Examples](vmware_deploy_ovf_module.md#examples)
- [Return Values](vmware_deploy_ovf_module.md#return-values)

## [Synopsis](vmware_deploy_ovf_module.md#id1)

- This module can be used to deploy a VMware VM from an OVF or OVA file, placed on file system or HTTP server

## [Parameters](vmware_deploy_ovf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_duplicates**  boolean | Whether or not to allow duplicate VM names. ESXi allows duplicates, vCenter may not.  **Choices:**   - `false` - `true` ← (default) |
| **cluster**  string | Cluster to deploy to.  This is a required parameter, if `esxi_hostname` is not set and `hostname` is set to the vCenter server.  `esxi_hostname` and `cluster` are mutually exclusive parameters.  This parameter is case sensitive. |
| **datacenter**  string | Datacenter to deploy to.  **Default:** `"ha-datacenter"` |
| **datastore**  string | Datastore to deploy to.  **Default:** `"datastore1"` |
| **deployment_option**  string | The key of the chosen deployment option. |
| **disk_provisioning**  string | Disk provisioning type.  **Choices:**   - `"flat"` - `"eagerZeroedThick"` - `"monolithicSparse"` - `"twoGbMaxExtentSparse"` - `"twoGbMaxExtentFlat"` - `"thin"` ← (default) - `"sparse"` - `"thick"` - `"seSparse"` - `"monolithicFlat"` |
| **enable_hidden_properties**  boolean  *added in community.vmware 3.11.0* | Enable source properties that are marked as ovf:userConfigurable=false  **Choices:**   - `false` ← (default) - `true` |
| **esxi_hostname**  string | The ESXi hostname where the virtual machine will run.  This is a required parameter, if `cluster` is not set and `hostname` is set to the vCenter server.  `esxi_hostname` and `cluster` are mutually exclusive parameters.  This parameter is case sensitive. |
| **fail_on_spec_warnings**  boolean | Cause the module to treat OVF Import Spec warnings as errors.  **Choices:**   - `false` ← (default) - `true` |
| **folder**  string | Absolute path of folder to place the virtual machine.  If not specified, defaults to the value of `datacenter.vmFolder`.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **inject_ovf_env**  boolean | Force the given properties to be inserted into an OVF Environment and injected through VMware Tools.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | Name of the VM to work with.  Virtual machine names in vCenter are not necessarily unique, which may be problematic. |
| **networks**  dictionary | `key: value` mapping of OVF network name, to the vCenter network name.  **Default:** `{"VM Network": "VM Network"}` |
| **ovf**  aliases: ova  path | Path to OVF or OVA file to deploy.  This is a required parameter, if `ovf` is not set and `url` parameter must be set.  `ovf` and `url` are mutually exclusive parameters. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **power_on**  boolean | Whether or not to power on the virtual machine after creation.  **Choices:**   - `false` - `true` ← (default) |
| **properties**  dictionary | The assignment of values to the properties found in the OVF as key value pairs. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string | Resource Pool to deploy to.  **Default:** `"Resources"` |
| **url**  string  *added in community.vmware 3.9.0* | URL for OVA file to deploy.  This is a required parameter, if `url` is not set and `ovf` parameter must be set.  `url` and `ovf` are mutually exclusive parameters. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the host to power on.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_ip_address**  boolean | Wait until vCenter detects an IP address for the VM.  This requires vmware-tools (vmtoolsd) to properly work after creation.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vmware_deploy_ovf_module.md#id3)

> **Note:**
>
> - For use https as source need enable in firewall incoming 443 port
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_deploy_ovf_module.md#id4)

```yaml+jinja
- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    ovf: /path/to/ubuntu-16.04-amd64.ovf
    wait_for_ip_address: true
  delegate_to: localhost

# Deploys a new VM named 'NewVM' in specific datacenter/cluster, with network mapping taken from variable and using ova template from an absolute path
- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: Datacenter1
    cluster: Cluster1
    datastore: vsandatastore
    name: NewVM
    networks: "{u'VM Network':u'{{ ProvisioningNetworkLabel }}'}"
    power_on: false
    ovf: /absolute/path/to/template/mytemplate.ova
  delegate_to: localhost

- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: Datacenter1
    esxi_hostname: test-server
    datastore: test-datastore
    ovf: /path/to/ubuntu-16.04-amd64.ovf
  delegate_to: localhost

- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    url: https://cloud-images.ubuntu.com/releases/xenial/release/ubuntu-16.04-server-cloudimg-amd64.ova
    wait_for_ip_address: true
  delegate_to: localhost
```

## [Return Values](vmware_deploy_ovf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the new virtual machine  **Returned:** always  **Sample:** `"None"` |

### Authors

- Alexander Nikitin (@ihumster)
- Matt Martz (@sivel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
