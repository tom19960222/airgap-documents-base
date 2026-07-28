---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_vnic_profile module – Module to manage vNIC profile of network in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_vnic_profile_module.html
fetched_at: 2026-07-28T00:17:58+00:00
---
# ovirt.ovirt.ovirt_vnic_profile module – Module to manage vNIC profile of network in oVirt/RHV

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
> see [Requirements](ovirt_vnic_profile_module.md#ansible-collections-ovirt-ovirt-ovirt-vnic-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_vnic_profile`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_vnic_profile_module.md#synopsis)
- [Requirements](ovirt_vnic_profile_module.md#requirements)
- [Parameters](ovirt_vnic_profile_module.md#parameters)
- [Notes](ovirt_vnic_profile_module.md#notes)
- [Examples](ovirt_vnic_profile_module.md#examples)
- [Return Values](ovirt_vnic_profile_module.md#return-values)

## [Synopsis](ovirt_vnic_profile_module.md#id1)

- Module to manage vNIC profile of network in oVirt/RHV

## [Requirements](ovirt_vnic_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_vnic_profile_module.md#id3)

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
| **custom_properties**  list / elements=dictionary | Custom properties applied to the vNIC profile.  Custom properties is a list of dictionary which can have following values: |
| **name**  string | Name of the custom property. For example: *hugepages*, *vhost*, *sap_agent*, etc. |
| **regexp**  string | Regular expression to set for custom property. |
| **value**  string | Value to set for custom property. |
| **data_center**  string / required | Datacenter name where network reside. |
| **description**  string | A human-readable description in plain text. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **migratable**  boolean | Marks whether pass_through NIC is migratable or not.  Choices:   - `false` - `true` |
| **name**  string / required | A human-readable name in plain text. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **network**  string / required | Name of network to which is vNIC attached. |
| **network_filter**  string | The network filter enables to filter packets send to/from the VM’s nic according to defined rules. |
| **pass_through**  string | Enables passthrough to an SR-IOV-enabled host NIC.  When enabled `qos` and `network_filter` are automatically set to None and `port_mirroring` to False.  When enabled and `migratable` not specified then `migratable` is enabled.  Port mirroring, QoS and network filters are not supported on passthrough profiles.  Choices:   - `"disabled"` - `"enabled"` |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **port_mirroring**  boolean | Enables port mirroring.  Choices:   - `false` - `true` |
| **qos**  string | Quality of Service attributes regulate inbound and outbound network traffic of the NIC. |
| **state**  string | Should the vNIC be absent/present.  Choices:   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_vnic_profile_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_vnic_profile_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:
- name: Add vNIC
  ovirt.ovirt.ovirt_vnic_profile:
    name: myvnic
    network: mynetwork
    state: present
    data_center: datacenter

- name: Editing vNICs network_filter, custom_properties, qos
  ovirt.ovirt.ovirt_vnic_profile:
    name: myvnic
    network: mynetwork
    data_center: datacenter
    qos: myqos
    custom_properties:
      - name: SecurityGroups
        value: 9bd9bde9-39da-44a8-9541-aa39e1a81c9d
    network_filter: allow-dhcp

- name: Remove vNICs network_filter, custom_properties, qos
  ovirt.ovirt.ovirt_vnic_profile:
    name: myvnic
    network: mynetwork
    data_center: datacenter
    qos: ""
    custom_properties: ""
    network_filter: ""

- name: Dont use migratable
  ovirt.ovirt.ovirt_vnic_profile:
    name: myvnic
    network: mynetwork
    data_center: datacenter
    migratable: False
    pass_through: enabled

- name: Remove vNIC
  ovirt.ovirt.ovirt_vnic_profile:
    name: myvnic
    network: mynetwork
    state: absent
    data_center: datacenter
```

## [Return Values](ovirt_vnic_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the vNIC profile which is managed  Returned: On success if vNIC profile is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **vnic**  dictionary | Dictionary of all the vNIC profile attributes. Network interface attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/nic>.  Returned: On success if vNIC profile is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
