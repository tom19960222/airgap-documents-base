---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_ntp module – Manage NTP server configuration of an ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_ntp_module.html
fetched_at: 2026-07-27T17:22:26+00:00
---
# community.vmware.vmware_host_ntp module – Manage NTP server configuration of an ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_ntp`.

- [Synopsis](vmware_host_ntp_module.md#synopsis)
- [Parameters](vmware_host_ntp_module.md#parameters)
- [Notes](vmware_host_ntp_module.md#notes)
- [Examples](vmware_host_ntp_module.md#examples)
- [Return Values](vmware_host_ntp_module.md#return-values)

## [Synopsis](vmware_host_ntp_module.md#id1)

- This module can be used to configure, add or remove NTP servers from an ESXi host.
- If `state` is not given, the NTP servers will be configured in the exact sequence.
- User can specify an ESXi hostname or Cluster name. In case of cluster name, all ESXi hosts are updated.

## [Parameters](vmware_host_ntp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  This parameter is required if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  This parameter is required if `cluster_name` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **ntp_servers**  list / elements=string / required | IP or FQDN of NTP server(s).  This accepts a list of NTP servers. For multiple servers, please look at the examples. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | present: Add NTP server(s), if specified server(s) are absent else do nothing.  absent: Remove NTP server(s), if specified server(s) are present else do nothing.  Specified NTP server(s) will be configured if `state` isn’t specified.  Choices:   - `"present"` - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **verbose**  boolean | Verbose output of the configuration change.  Explains if an NTP server was added, removed, or if the NTP server sequence was changed.  Choices:   - `false` ← (default) - `true` |

## [Notes](vmware_host_ntp_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_ntp_module.md#id4)

```yaml+jinja
- name: Configure NTP servers for an ESXi Host
  community.vmware.vmware_host_ntp:
    hostname: vcenter01.example.local
    username: administrator@vsphere.local
    password: SuperSecretPassword
    esxi_hostname: esx01.example.local
    ntp_servers:
        - 0.pool.ntp.org
        - 1.pool.ntp.org
  delegate_to: localhost

- name: Set NTP servers for all ESXi Host in given Cluster
  community.vmware.vmware_host_ntp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: present
    ntp_servers:
        - 0.pool.ntp.org
        - 1.pool.ntp.org
  delegate_to: localhost

- name: Set NTP servers for an ESXi Host
  community.vmware.vmware_host_ntp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: present
    ntp_servers:
        - 0.pool.ntp.org
        - 1.pool.ntp.org
  delegate_to: localhost

- name: Remove NTP servers for an ESXi Host
  community.vmware.vmware_host_ntp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: absent
    ntp_servers:
        - bad.server.ntp.org
  delegate_to: localhost
```

## [Return Values](vmware_host_ntp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_ntp_status**  dictionary | metadata about host system’s NTP configuration  Returned: always  Sample: `{"esx01.example.local": {"ntp_servers": ["time3.example.local", "time4.example.local"], "ntp_servers_changed": ["time1.example.local", "time2.example.local", "time3.example.local", "time4.example.local"], "ntp_servers_previous": ["time1.example.local", "time2.example.local"]}, "esx02.example.local": {"ntp_servers_changed": ["time3.example.local"], "ntp_servers_current": ["time1.example.local", "time2.example.local", "time3.example.local"], "ntp_servers_previous": ["time1.example.local", "time2.example.local"], "state": "present"}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
