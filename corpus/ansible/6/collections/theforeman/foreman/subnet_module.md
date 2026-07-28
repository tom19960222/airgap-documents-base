---
collection: ansible
version: "6"
title: "theforeman.foreman.subnet module – Manage Subnets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/subnet_module.html
fetched_at: 2026-07-28T00:21:12+00:00
---
# theforeman.foreman.subnet module – Manage Subnets

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](subnet_module.md#ansible-collections-theforeman-foreman-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.subnet`.

New in theforeman.foreman 1.0.0

- [Synopsis](subnet_module.md#synopsis)
- [Requirements](subnet_module.md#requirements)
- [Parameters](subnet_module.md#parameters)
- [Examples](subnet_module.md#examples)
- [Return Values](subnet_module.md#return-values)

## [Synopsis](subnet_module.md#id1)

- Create, update, and delete Subnets

## [Requirements](subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- ipaddress
- requests

## [Parameters](subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bmc_proxy**  string  added in theforeman.foreman 2.1.0 | BMC Smart proxy for this subnet |
| **boot_mode**  string | Boot mode used by hosts in this subnet  Choices:   - `"DHCP"` ← (default) - `"Static"` |
| **cidr**  integer | CIDR prefix length; Required if *network_type=IPv4* and no *mask* provided |
| **description**  string | Description of the subnet |
| **dhcp_proxy**  string | DHCP Smart proxy for this subnet |
| **discovery_proxy**  string | Discovery Smart proxy for this subnet  This option is only available if the discovery plugin is installed. |
| **dns_primary**  string | Primary DNS server for this subnet |
| **dns_proxy**  string | Reverse DNS Smart proxy for this subnet |
| **dns_secondary**  string | Secondary DNS server for this subnet |
| **domains**  list / elements=string | List of DNS domains the subnet should assigned to |
| **externalipam_group**  string  added in theforeman.foreman 1.5.0 | External IPAM group for this subnet.  Only relevant if *ipam=External IPAM*. |
| **externalipam_proxy**  string | External IPAM proxy for this subnet.  Only relevant if *ipam=External IPAM*. |
| **from_ip**  string | First IP address of the host IP allocation pool |
| **gateway**  string | Subnet gateway IP address |
| **httpboot_proxy**  string | HTTP Boot Smart proxy for this subnet |
| **ipam**  string | IPAM mode for this subnet  Choices:   - `"DHCP"` ← (default) - `"Internal DB"` - `"Random DB"` - `"EUI-64"` - `"External IPAM"` - `"None"` |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **mask**  string | Subnet netmask. Required if *network_type=IPv4* and no *cidr* prefix length provided |
| **mtu**  integer | MTU |
| **name**  string / required | Subnet name |
| **network**  string / required | Subnet IP address |
| **network_type**  string | Subnet type  Choices:   - `"IPv4"` ← (default) - `"IPv6"` |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **parameters**  list / elements=dictionary | Subnet specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  Choices:   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **remote_execution_proxies**  list / elements=string | Remote execution Smart proxies for this subnet  This option is only available if the remote_execution plugin is installed.  This will always report *changed=true* when used with *remote_execution < 4.1.0*, due to a bug in the plugin. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **template_proxy**  string | Template Smart proxy for this subnet |
| **tftp_proxy**  string | TFTP Smart proxy for this subnet |
| **to_ip**  string | Last IP address of the host IP allocation pool |
| **updated_name**  string | New subnet name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **vlanid**  integer | VLAN ID |

## [Examples](subnet_module.md#id4)

```yaml+jinja
- name: My subnet
  theforeman.foreman.subnet:
    name: "My subnet"
    description: "My description"
    network: "192.168.0.0"
    mask: "255.255.255.192"
    gateway: "192.168.0.1"
    from_ip: "192.168.0.2"
    to_ip: "192.168.0.42"
    boot_mode: "Static"
    dhcp_proxy: "smart-proxy1.foo.example.com"
    tftp_proxy: "smart-proxy1.foo.example.com"
    dns_proxy: "smart-proxy2.foo.example.com"
    template_proxy: "smart-proxy2.foo.example.com"
    vlanid: 452
    mtu: 9000
    domains:
    - "foo.example.com"
    - "bar.example.com"
    organizations:
    - "Example Org"
    locations:
    - "Toulouse"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](subnet_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **subnets**  list / elements=dictionary | List of subnets.  Returned: success |

### Authors

- Baptiste Agasse (@bagasse)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
