---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_host_network module – Module to manage host networks in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_host_network_module.html
fetched_at: 2026-07-28T00:17:34+00:00
---
# ovirt.ovirt.ovirt_host_network module – Module to manage host networks in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ovirt/ovirt) (version 2.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_host_network_module.md#ansible-collections-ovirt-ovirt-ovirt-host-network-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_host_network`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_host_network_module.md#synopsis)
- [Requirements](ovirt_host_network_module.md#requirements)
- [Parameters](ovirt_host_network_module.md#parameters)
- [Notes](ovirt_host_network_module.md#notes)
- [Examples](ovirt_host_network_module.md#examples)
- [Return Values](ovirt_host_network_module.md#return-values)

## [Synopsis](ovirt_host_network_module.md#id1)

- Module to manage host networks in oVirt/RHV.

## [Requirements](ovirt_host_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_host_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  Choices:   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  Choices:   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  Choices:   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **bond**  dictionary | Dictionary describing network bond: |
| **interfaces**  string | List of interfaces to create a bond. |
| **mode**  string | Bonding mode. |
| **name**  string | Bond name. |
| **options**  string | Bonding options. |
| **check**  boolean | If *true* verify connectivity between host and engine.  Network configuration changes will be rolled back if connectivity between engine and the host is lost after changing network configuration.  Choices:   - `false` - `true` |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **interface**  string | Name of the network interface where logical network should be attached. |
| **labels**  list / elements=string | List of names of the network label to be assigned to bond or interface. |
| **name**  aliases: host  string / required | Name of the host to manage networks for. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **networks**  list / elements=dictionary | List of dictionary describing networks to be attached to interface or bond: |
| **address**  string | IP address in case of *static* boot protocol is used. |
| **boot_protocol**  string | Boot protocol.  Choices:   - `"none"` - `"static"` - `"dhcp"` |
| **custom_properties**  string | Custom properties applied to the host network.  Custom properties is a list of dictionary which can have following values. |
| **name**  string | Name of custom property. |
| **value**  string | Value of custom property. |
| **gateway**  string | Gateway in case of *static* boot protocol is used. |
| **name**  string | Name of the logical network to be assigned to bond or interface. |
| **netmask**  string | Subnet mask in case of *static* boot protocol is used. |
| **version**  string | IP version. Either v4 or v6. Default is v4. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **save**  boolean | If *true* network configuration will be persistent, otherwise it is temporary. Default *true* since Ansible 2.8.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Should the host be present/absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **sync_networks**  boolean | If *true* all networks will be synchronized before modification  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_host_network_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_host_network_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# In all examples the durability of the configuration created is dependent on the 'save' option value:

# Create bond on eth0 and eth1 interface, and put 'myvlan' network on top of it and persist the new configuration:
- name: Bonds
  ovirt.ovirt.ovirt_host_network:
    name: myhost
    save: yes
    bond:
      name: bond0
      mode: 2
      interfaces:
        - eth1
        - eth2
    networks:
      - name: myvlan
        boot_protocol: static
        address: 1.2.3.4
        netmask: 255.255.255.0
        gateway: 1.2.3.4
        version: v4

# Create bond on eth1 and eth2 interface, specifying both mode and miimon:
- name: Bonds
  ovirt.ovirt.ovirt_host_network:
    name: myhost
    bond:
      name: bond0
      mode: 1
      options:
        miimon: 200
      interfaces:
        - eth1
        - eth2

# Remove bond0 bond from host interfaces:
- ovirt.ovirt.ovirt_host_network:
    state: absent
    name: myhost
    bond:
      name: bond0

# Assign myvlan1 and myvlan2 vlans to host eth0 interface:
- ovirt.ovirt.ovirt_host_network:
    name: myhost
    interface: eth0
    networks:
      - name: myvlan1
      - name: myvlan2

# Remove myvlan2 vlan from host eth0 interface:
- ovirt.ovirt.ovirt_host_network:
    state: absent
    name: myhost
    interface: eth0
    networks:
      - name: myvlan2

# Remove all networks/vlans from host eth0 interface:
- ovirt.ovirt.ovirt_host_network:
    state: absent
    name: myhost
    interface: eth0

# Add custom_properties to network:
- ovirt.ovirt.ovirt_host_network:
    name: myhost
    interface: eth0
    networks:
      - name: myvlan1
        custom_properties:
          - name: bridge_opts
            value: gc_timer=10
```

## [Return Values](ovirt_host_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_nic**  dictionary | Dictionary of all the host NIC attributes. Host NIC attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/host_nic>.  Returned: On success if host NIC is found. |
| **id**  string | ID of the host NIC which is managed  Returned: On success if host NIC is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
