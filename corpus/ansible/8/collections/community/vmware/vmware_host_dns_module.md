---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_dns module – Manage DNS configuration of an ESXi host system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_dns_module.html
fetched_at: 2026-07-28T02:00:36+00:00
---
# community.vmware.vmware_host_dns module – Manage DNS configuration of an ESXi host system

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
> To use it in a playbook, specify: `community.vmware.vmware_host_dns`.

- [Synopsis](vmware_host_dns_module.md#synopsis)
- [Parameters](vmware_host_dns_module.md#parameters)
- [Notes](vmware_host_dns_module.md#notes)
- [Examples](vmware_host_dns_module.md#examples)
- [Return Values](vmware_host_dns_module.md#return-values)

## [Synopsis](vmware_host_dns_module.md#id1)

- This module can be used to configure DNS for the default TCP/IP stack on an ESXi host system.

## [Parameters](vmware_host_dns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  This parameter is required if `esxi_hostname` is not specified and you connect to a vCenter.  Cannot be used when you connect directly to an ESXi host. |
| **device**  string | The VMkernel network adapter to obtain DNS settings from.  Needs to get its IP through DHCP, a static network configuration combined with a dynamic DNS configuration doesn’t work.  The parameter is only required in case of `type` is set to `dhcp`. |
| **dns_servers**  list / elements=string | A list of DNS servers to be used.  The order of the DNS servers is important as they are used consecutively in order. |
| **domain**  string | The domain name to be used for the ESXi host. |
| **esxi_hostname**  string | Name of the host system to work with.  This parameter is required if `cluster_name` is not specified and you connect to a vCenter.  Cannot be used when you connect directly to an ESXi host. |
| **host_name**  string | The hostname to be used for the ESXi host.  Cannot be used when configuring a complete cluster. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **search_domains**  list / elements=string | A list of domains to be searched through by the resolver. |
| **type**  string / required | Type of DNS assignment. Either `dhcp` or `static`.  A VMkernel adapter needs to be set to DHCP if `type` is set to `dhcp`.  **Choices:**   - `"dhcp"` - `"static"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **verbose**  boolean | Verbose output of the DNS server configuration change.  Explains if an DNS server was added, removed, or if the DNS server sequence was changed.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vmware_host_dns_module.md#id3)

> **Note:**
>
> - This module is a replacement for the module `vmware_dns_config`
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_dns_module.md#id4)

```yaml+jinja
- name: Configure DNS for an ESXi host
  community.vmware.vmware_host_dns:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    type: static
    host_name: esx01
    domain: example.local
    dns_servers:
      - 192.168.1.10
      - 192.168.1.11
    search_domains:
      - subdomain.example.local
      - example.local
  delegate_to: localhost

- name: Configure DNS for all ESXi hosts of a cluster
  community.vmware.vmware_host_dns:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    type: static
    domain: example.local
    dns_servers:
      - 192.168.1.10
      - 192.168.1.11
    search_domains:
      - subdomain.example.local
      - example.local
  delegate_to: localhost

- name: Configure DNS via DHCP for an ESXi host
  community.vmware.vmware_host_dns:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    type: dhcp
    device: vmk0
  delegate_to: localhost
```

## [Return Values](vmware_host_dns_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dns_config_result**  dictionary | metadata about host system’s DNS configuration  **Returned:** always  **Sample:** `{"esx01.example.local": {"changed": true, "dns_servers": ["192.168.1.10", "192.168.1.11"], "dns_servers_changed": ["192.168.1.12", "192.168.1.13"], "dns_servers_previous": ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13"], "domain": "example.local", "host_name": "esx01", "msg": "DNS servers and Search domains changed", "search_domains": ["subdomain.example.local", "example.local"], "search_domains_changed": ["subdomain.example.local"], "search_domains_previous": ["example.local"]}}` |

### Authors

- Christian Kotte (@ckotte)
- Mario Lenz (@mariolenz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
