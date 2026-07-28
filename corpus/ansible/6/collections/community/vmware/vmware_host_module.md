---
collection: ansible
version: "6"
title: "community.vmware.vmware_host module – Add, remove, or move an ESXi host to, from, or within vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_module.html
fetched_at: 2026-07-27T17:22:10+00:00
---
# community.vmware.vmware_host module – Add, remove, or move an ESXi host to, from, or within vCenter

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_host_module.md#ansible-collections-community-vmware-vmware-host-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_host`.

- [Synopsis](vmware_host_module.md#synopsis)
- [Requirements](vmware_host_module.md#requirements)
- [Parameters](vmware_host_module.md#parameters)
- [Notes](vmware_host_module.md#notes)
- [Examples](vmware_host_module.md#examples)
- [Return Values](vmware_host_module.md#return-values)

## [Synopsis](vmware_host_module.md#id1)

- This module can be used to add, reconnect, or remove an ESXi host to or from vCenter.
- This module can also be used to move an ESXi host to a cluster or folder, or vice versa, within the same datacenter.

## [Requirements](vmware_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- ssl
- socket
- hashlib

## [Parameters](vmware_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_connected**  boolean | If set to `True`, then the host should be connected as soon as it is added.  This parameter is ignored if state is set to a value other than `present`.  Choices:   - `false` - `true` ← (default) |
| **cluster_name**  aliases: cluster  string | Name of the cluster to add the host.  If `folder` is not set, then this parameter is required.  Aliases added in version 2.6. |
| **datacenter_name**  aliases: datacenter  string / required | Name of the datacenter to add the host.  Aliases added in version 2.6. |
| **esxi_hostname**  string / required | ESXi hostname to manage. |
| **esxi_password**  string | ESXi password.  Required for adding a host.  Optional for reconnect.  Unused for removing.  No longer a required parameter from version 2.5. |
| **esxi_ssl_thumbprint**  aliases: ssl_thumbprint  string | Specifying the hostsystem certificate’s thumbprint.  Use following command to get hostsystem certificate’s thumbprint -  # openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout  Only used if `fetch_thumbprint` isn’t set to `true`.  Default: `""` |
| **esxi_username**  string | ESXi username.  Required for adding a host.  Optional for reconnect. If both `esxi_username` and `esxi_password` are used  Unused for removing.  No longer a required parameter from version 2.5. |
| **fetch_ssl_thumbprint**  boolean | Fetch the thumbprint of the host’s SSL certificate.  This basically disables the host certificate verification (check if it was signed by a recognized CA).  Disable this option if you want to allow only hosts with valid certificates to be added to vCenter.  If this option is set to `false` and the certificate can’t be verified, an add or reconnect will fail.  Unused when `esxi_ssl_thumbprint` is set.  Optional for reconnect, but only used if `esxi_username` and `esxi_password` are used.  Unused for removing.  Choices:   - `false` - `true` ← (default) |
| **folder**  aliases: folder_name  string | Name of the folder under which host to add.  If `cluster_name` is not set, then this parameter is required.  For example, if there is a datacenter ‘dc1’ under folder called ‘Site1’ then, this value will be ‘/Site1/dc1/host’.  Here ‘host’ is an invisible folder under VMware Web Client.  Another example, if there is a nested folder structure like ‘/myhosts/india/pune’ under datacenter ‘dc2’, then `folder` value will be ‘/dc2/host/myhosts/india/pune’.  Other Examples: ‘/Site2/dc2/Asia-Cluster/host’ or ‘/dc3/Asia-Cluster/host’ |
| **force_connection**  boolean | Force the connection if the host is already being managed by another vCenter server.  Choices:   - `false` - `true` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **reconnect_disconnected**  boolean | Reconnect disconnected hosts.  This is only used if `state` is set to `present` and if the host already exists.  Choices:   - `false` - `true` ← (default) |
| **state**  string | If set to `present`, add the host if host is absent.  If set to `present`, update the location of the host if host already exists.  If set to `absent`, remove the host if host is present.  If set to `absent`, do nothing if host already does not exists.  If set to `add_or_reconnect`, add the host if it’s absent else reconnect it and update the location.  If set to `reconnect`, then reconnect the host if it’s present and update the location.  If set to `disconnected`, disconnect the host if the host already exists.  Choices:   - `"present"` ← (default) - `"absent"` - `"add_or_reconnect"` - `"reconnect"` - `"disconnected"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_module.md#id5)

```yaml+jinja
- name: Add ESXi Host to vCenter
  community.vmware.vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    cluster: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    state: present
  delegate_to: localhost

- name: Add ESXi Host to vCenter under a specific folder
  community.vmware.vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    folder: '/Site2/Asia-Cluster/host'
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    state: present
    add_connected: True
  delegate_to: localhost

- name: Reconnect ESXi Host (with username/password set)
  community.vmware.vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    cluster: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    state: reconnect
  delegate_to: localhost

- name: Reconnect ESXi Host (with default username/password)
  community.vmware.vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    cluster: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    state: reconnect
  delegate_to: localhost

- name: Add ESXi Host with SSL Thumbprint to vCenter
  community.vmware.vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
    cluster: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    esxi_ssl_thumbprint: "3C:A5:60:6F:7A:B7:C4:6C:48:28:3D:2F:A5:EC:A3:58:13:88:F6:DD"
    state: present
  delegate_to: localhost
```

## [Return Values](vmware_host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | metadata about the new host system added  Returned: on successful addition  Sample: `"Host already connected to vCenter 'vcenter01' in cluster 'cluster01'"` |

### Authors

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Maxime de Roucy (@tchernomax)
- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
