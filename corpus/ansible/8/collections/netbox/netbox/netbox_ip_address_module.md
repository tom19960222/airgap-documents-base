---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_ip_address module – Creates or removes IP addresses from NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_ip_address_module.html
fetched_at: 2026-07-28T02:45:09+00:00
---
# netbox.netbox.netbox_ip_address module – Creates or removes IP addresses from NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_ip_address_module.md#ansible-collections-netbox-netbox-netbox-ip-address-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_ip_address`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_ip_address_module.md#synopsis)
- [Requirements](netbox_ip_address_module.md#requirements)
- [Parameters](netbox_ip_address_module.md#parameters)
- [Notes](netbox_ip_address_module.md#notes)
- [Examples](netbox_ip_address_module.md#examples)
- [Return Values](netbox_ip_address_module.md#return-values)

## [Synopsis](netbox_ip_address_module.md#id1)

- Creates or removes IP addresses from NetBox

## [Requirements](netbox_ip_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_ip_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the IP address configuration |
| **address**  string | Required if state is `present` |
| **assigned_object**  dictionary | Definition of the assigned object. |
| **device**  string | The device the interface is attached to. |
| **name**  string | The name of the interface |
| **virtual_machine**  string | The virtual machine the interface is attached to. |
| **comments**  string  *added in netbox.netbox 3.10.0* | Comments that may include additional information in regards to the IP Address |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | The description of the interface |
| **dns_name**  string | Hostname or FQDN |
| **family**  integer | (DEPRECATED) - NetBox now handles determining the IP family natively.  Specifies with address family the IP address belongs to  **Choices:**   - `4` - `6` |
| **interface**  any | The name and device of the interface that the IP address should be assigned to  Required if state is `present` and a prefix specified. |
| **nat_inside**  any | The inside IP address this IP is assigned to |
| **prefix**  any | With state `present`, if an interface is given, it will ensure  that an IP inside this prefix (and vrf, if given) is attached to this interface. Otherwise, it will get the next available IP of this prefix and attach it. With state `new`, it will force to get the next available IP in this prefix. If an interface is given, it will also force to attach it. Required if state is `present` or `new` when no address is given. Unused if an address is specified. |
| **role**  string | The role of the IP address  **Choices:**   - `"Loopback"` - `"Secondary"` - `"Anycast"` - `"VIP"` - `"VRRP"` - `"HSRP"` - `"GLBP"` - `"CARP"` |
| **status**  any | The status of the IP address |
| **tags**  list / elements=any | Any tags that the IP address may need to be associated with |
| **tenant**  any | The tenant that the device will be assigned to |
| **vrf**  any | VRF that IP address is associated with |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | Use `present`, `new` or `absent` for adding, force adding or removing.  `present` will check if the IP is already created, and return it if true. `new` will force to create it anyway (useful for anycasts, for example).  **Choices:**   - `"absent"` - `"new"` - `"present"` ← (default) |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_ip_address_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_ip_address_module.md#id5)

```yaml+jinja
- name: "Test NetBox IP address module"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create IP address within NetBox with only required information
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          address: 192.168.1.10
        state: present

    - name: Force to create (even if it already exists) the IP
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          address: 192.168.1.10
        state: new

    - name: Get a new available IP inside 192.168.1.0/24
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.1.0/24
        state: new

    - name: Delete IP address within netbox
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          address: 192.168.1.10
        state: absent

    - name: Create IP address with several specified options
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          address: 192.168.1.20
          vrf: Test
          tenant: Test Tenant
          status: Reserved
          role: Loopback
          description: Test description
          tags:
            - Schnozzberry
        state: present

    - name: Create IP address and assign a nat_inside IP
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          address: 192.168.1.30
          vrf: Test
          nat_inside:
            address: 192.168.1.20
            vrf: Test
          interface:
            name: GigabitEthernet1
            device: test100

    - name: Ensure that an IP inside 192.168.1.0/24 is attached to GigabitEthernet1
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.1.0/24
          vrf: Test
          interface:
            name: GigabitEthernet1
            device: test100
        state: present

    - name: Attach a new available IP of 192.168.1.0/24 to GigabitEthernet1
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.1.0/24
          vrf: Test
          interface:
            name: GigabitEthernet1
            device: test100
        state: new

    - name: Attach a new available IP of 192.168.1.0/24 to GigabitEthernet1 (NetBox 2.9+)
      netbox.netbox.netbox_ip_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.1.0/24
          vrf: Test
          assigned_object:
            name: GigabitEthernet1
            device: test100
        state: new
```

## [Return Values](netbox_ip_address_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ip_address**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Mikhail Yohman (@FragmentedPacket)
- Anthony Ruhier (@Anthony25)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
