---
collection: ansible
version: "8"
title: "theforeman.foreman.host module – Manage Hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/host_module.html
fetched_at: 2026-07-28T02:56:00+00:00
---
# theforeman.foreman.host module – Manage Hosts

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](host_module.md#ansible-collections-theforeman-foreman-host-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.host`.

New in theforeman.foreman 1.0.0

- [Synopsis](host_module.md#synopsis)
- [Requirements](host_module.md#requirements)
- [Parameters](host_module.md#parameters)
- [Attributes](host_module.md#attributes)
- [Examples](host_module.md#examples)
- [Return Values](host_module.md#return-values)

## [Synopsis](host_module.md#id1)

- Create, update, and delete Hosts

Aliases: foreman_host

## [Requirements](host_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activation_keys**  string | Activation Keys used for deployment.  Comma separated list.  Only available for Katello installations. |
| **architecture**  string | Architecture name |
| **build**  boolean | Whether or not to setup build context for the host  **Choices:**   - `false` - `true` |
| **comment**  string | Comment about the host. |
| **compute_attributes**  dictionary | Additional compute resource specific attributes.  When this parameter is set, the module will not be idempotent.  When you provide a *cluster* here and *compute_resource* is set, the cluster id will be automatically looked up. |
| **compute_profile**  string | Compute profile name |
| **compute_resource**  string | Compute resource name |
| **config_groups**  list / elements=string | Config groups list |
| **content_source**  string | Content Source (Smart Proxy with Content) name.  Only available for Katello installations. |
| **content_view**  string | Content view.  Only available for Katello installations. |
| **domain**  string | Domain name |
| **enabled**  boolean | Include this host within reporting  **Choices:**   - `false` - `true` |
| **environment**  string | Puppet environment name |
| **hostgroup**  string | Title of related hostgroup  Example: A child hostgroup *bar* within a parent hostgroup *foo* would have the title *foo/bar*. |
| **image**  string | The image to use when *provision_method=image*.  The *compute_resource* parameter is required to find the correct image. |
| **interfaces_attributes**  list / elements=dictionary  *added in theforeman.foreman 1.5.0* | Additional interfaces specific attributes. |
| **attached_devices**  list / elements=string | Identifiers of attached interfaces, e.g. [‘eth1’, ‘eth2’].  For bond interfaces those are the slaves.  Only for bond and bridges interfaces. |
| **attached_to**  string | Identifier of the interface to which this interface belongs, e.g. eth1.  Only for virtual interfaces. |
| **bond_options**  string | Space separated options, e.g. miimon=100.  Only for bond interfaces. |
| **compute_attributes**  dictionary | Additional compute resource specific attributes for the interface.  When this parameter is set, the module will not be idempotent.  When you provide a *network* here and *compute_resource* is set, the network id will be automatically looked up.  On oVirt/RHV *cluster* is required in the hosts *compute_attributes* for the lookup to work. |
| **domain**  string | Domain name  Required for primary interfaces on managed hosts. |
| **execution**  boolean | Should this interface be used for Remote Execution?  Each managed hosts should have one remote execution interface.  **Choices:**   - `false` - `true` |
| **identifier**  string | Device identifier, e.g. eth0 or eth1.1  You need to set one of *identifier*, *name* or *mac* to be able to update existing interfaces and make execution idempotent. |
| **ip**  string | IPv4 address of interface |
| **ip6**  string | IPv6 address of interface |
| **mac**  string | MAC address of interface. Required for managed interfaces on bare metal.  Please include leading zeros and separate nibbles by colons, otherwise the execution will not be idempotent.  Example EE:BB:01:02:03:04  You need to set one of *identifier*, *name* or *mac* to be able to update existing interfaces and make execution idempotent. |
| **managed**  boolean | Should this interface be managed via DHCP and DNS smart proxy and should it be configured during provisioning?  **Choices:**   - `false` - `true` |
| **mode**  string | Bond mode of the interface.  Only for bond interfaces.  **Choices:**   - `"balance-rr"` - `"active-backup"` - `"balance-xor"` - `"broadcast"` - `"802.3ad"` - `"balance-tlb"` - `"balance-alb"` |
| **mtu**  integer | MTU, this attribute has precedence over the subnet MTU. |
| **name**  string | Interface’s DNS name  You need to set one of *identifier*, *name* or *mac* to be able to update existing interfaces and make execution idempotent. |
| **password**  string | Password for BMC authentication.  Only for BMC interfaces. |
| **primary**  boolean | Should this interface be used for constructing the FQDN of the host?  Each managed hosts needs to have one primary interface.  **Choices:**   - `false` - `true` |
| **provider**  string | Interface provider, e.g. IPMI.  Only for BMC interfaces.  **Choices:**   - `"IPMI"` - `"Redfish"` - `"SSH"` |
| **provision**  boolean | Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)?  Each managed hosts needs to have one provision interface.  **Choices:**   - `false` - `true` |
| **subnet**  string | IPv4 Subnet name |
| **subnet6**  string | IPv6 Subnet name |
| **tag**  string | VLAN tag, this attribute has precedence over the subnet VLAN ID.  Only for virtual interfaces. |
| **type**  string | Interface type.  **Choices:**   - `"interface"` - `"bmc"` - `"bond"` - `"bridge"` |
| **username**  string | Username for BMC authentication.  Only for BMC interfaces. |
| **virtual**  boolean | Alias or VLAN device  **Choices:**   - `false` - `true` |
| **ip**  string | IP address of the primary interface of the host. |
| **kickstart_repository**  string | Kickstart repository name.  You need to provide this to use the “Synced Content” feature.  Mutually exclusive with *medium*.  Only available for Katello installations. |
| **lifecycle_environment**  string | Lifecycle environment.  Only available for Katello installations. |
| **location**  string | Name of related location |
| **mac**  string | MAC address of the primary interface of the host.  Please include leading zeros and separate nibbles by colons, otherwise the execution will not be idempotent.  Example EE:BB:01:02:03:04 |
| **managed**  boolean | Whether a host is managed or unmanaged.  Forced to true when *build=true*  **Choices:**   - `false` - `true` |
| **medium**  aliases: media  string | Medium name  Mutually exclusive with *kickstart_repository*. |
| **name**  string / required | Fully Qualified Domain Name of host |
| **openscap_proxy**  string | OpenSCAP proxy name.  Only available when the OpenSCAP plugin is installed. |
| **operatingsystem**  string | Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **organization**  string | Name of related organization |
| **owner**  string | Owner (user) of the host.  Users are looked up by their `login`.  Mutually exclusive with *owner_group*. |
| **owner_group**  string | Owner (user group) of the host.  Mutually exclusive with *owner*. |
| **parameters**  list / elements=dictionary | Entity domain specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  **Choices:**   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **provision_method**  string | The method used to provision the host.  *provision_method=bootdisk* is only available if the bootdisk plugin is installed.  **Choices:**   - `"build"` - `"image"` - `"bootdisk"` |
| **ptable**  string | Partition table name |
| **puppet_ca_proxy**  string | Puppet CA proxy name |
| **puppet_proxy**  string | Puppet server proxy name |
| **puppetclasses**  list / elements=string | List of puppet classes to include in this host group. Must exist for hostgroup’s puppet environment. |
| **pxe_loader**  string | PXE Bootloader  **Choices:**   - `"PXELinux BIOS"` - `"PXELinux UEFI"` - `"Grub UEFI"` - `"Grub2 BIOS"` - `"Grub2 ELF"` - `"Grub2 UEFI"` - `"Grub2 UEFI SecureBoot"` - `"Grub2 UEFI HTTP"` - `"Grub2 UEFI HTTPS"` - `"Grub2 UEFI HTTPS SecureBoot"` - `"iPXE Embedded"` - `"iPXE UEFI HTTP"` - `"iPXE Chain BIOS"` - `"iPXE Chain UEFI"` - `"None"` |
| **realm**  string | Realm name |
| **root_pass**  string | Root password.  Will result in the entity always being updated, as the current password cannot be retrieved. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet**  string | IPv4 Subnet name |
| **subnet6**  string | IPv6 Subnet name |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](host_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](host_module.md#id5)

```yaml+jinja
- name: "Create a host"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    hostgroup: my_hostgroup
    state: present

- name: "Create a host with build context"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    hostgroup: my_hostgroup
    build: true
    state: present

- name: "Create an unmanaged host"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    managed: false
    state: present

- name: "Create a VM with 2 CPUs and 4GB RAM"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    compute_attributes:
      cpus: 2
      memory_mb: 4096
    state: present

- name: "Create a VM and start it after creation"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    compute_attributes:
      start: "1"
    state: present

- name: "Create a VM on specific ovirt network"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    interfaces_attributes:
    - type: "interface"
      compute_attributes:
        name: "nic1"
        network: "969efbe6-f9e0-4383-a19a-a7ee65ad5007"
        interface: "virtio"
    state: present

- name: "Create a VM with 2 NICs on specific ovirt networks"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    interfaces_attributes:
    - type: "interface"
      primary: true
      compute_attributes:
        name: "nic1"
        network: "969efbe6-f9e0-4383-a19a-a7ee65ad5007"
        interface: "virtio"
    - type: "interface"
      name: "new_host_nic2"
      managed: true
      compute_attributes:
        name: "nic2"
        network: "969efbe6-f9e0-4383-a19a-a7ee65ad5008"
        interface: "e1000"
    state: present

- name: "Delete a host"
  theforeman.foreman.host:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "new_host"
    state: absent
```

## [Return Values](host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **hosts**  list / elements=dictionary | List of hosts.  **Returned:** success |

### Authors

- Bernhard Hopfenmueller (@Fobhep) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
