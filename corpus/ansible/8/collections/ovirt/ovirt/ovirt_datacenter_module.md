---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_datacenter module – Module to manage data centers in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_datacenter_module.html
fetched_at: 2026-07-28T02:49:17+00:00
---
# ovirt.ovirt.ovirt_datacenter module – Module to manage data centers in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_datacenter_module.md#ansible-collections-ovirt-ovirt-ovirt-datacenter-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_datacenter`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_datacenter_module.md#synopsis)
- [Requirements](ovirt_datacenter_module.md#requirements)
- [Parameters](ovirt_datacenter_module.md#parameters)
- [Notes](ovirt_datacenter_module.md#notes)
- [Examples](ovirt_datacenter_module.md#examples)
- [Return Values](ovirt_datacenter_module.md#return-values)

## [Synopsis](ovirt_datacenter_module.md#id1)

- Module to manage data centers in oVirt/RHV

## [Requirements](ovirt_datacenter_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_datacenter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **comment**  string | Comment of the data center. |
| **compatibility_version**  string | Compatibility version of the data center. |
| **description**  string | Description of the data center. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | This parameter can be used only when removing a data center. If *True* data center will be forcibly removed, even though it contains some clusters. Default value is *False*, which means that only empty data center can be removed.  **Choices:**   - `false` - `true` |
| **id**  string | ID of the datacenter to manage. |
| **iscsi_bonds**  list / elements=dictionary | List of iscsi bonds, which should be created in datacenter. |
| **name**  string | Name of the iscsi bond. |
| **networks**  list / elements=string | List of network names in bond. |
| **storage_connections**  list / elements=string | List of storage_connection IDs. Used when you want to use specific storage connection instead of all in storage domain.  **Default:** `[]` |
| **storage_domains**  list / elements=string | List of storage domain names and it will automatically get all storage_connections in the domain.  **Default:** `[]` |
| **local**  boolean | *True* if the data center should be local, *False* if should be shared.  Default value is set by engine.  **Choices:**   - `false` - `true` |
| **mac_pool**  string | MAC pool to be used by this datacenter.  IMPORTANT: This option is deprecated in oVirt/RHV 4.1. You should use `mac_pool` in `ovirt_clusters` module, as MAC pools are set per cluster since 4.1. |
| **name**  string / required | Name of the data center to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **quota_mode**  string | Quota mode of the data center. One of *disabled*, *audit* or *enabled*  **Choices:**   - `"disabled"` - `"audit"` - `"enabled"` |
| **state**  string | Should the data center be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_datacenter_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_datacenter_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create datacenter
- ovirt.ovirt.ovirt_datacenter:
    name: mydatacenter
    local: True
    compatibility_version: 4.0
    quota_mode: enabled

# Remove datacenter
- ovirt.ovirt.ovirt_datacenter:
    state: absent
    name: mydatacenter

# Change Datacenter Name
- ovirt.ovirt.ovirt_datacenter:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_datacenter_name"

# Create datacenter with iscsi bond
- ovirt.ovirt.ovirt_datacenter:
    name: mydatacenter
    iscsi_bonds:
      - name: bond1
        networks:
            - network1
            - network2
        storage_domains:
            - storage1
      - name: bond2
        networks:
            - network3
        storage_connections:
            - cf780201-6a4f-43c1-a019-e65c4220ab73

# Remove all iscsi bonds
- ovirt.ovirt.ovirt_datacenter:
    name: mydatacenter
    iscsi_bonds: []
```

## [Return Values](ovirt_datacenter_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data_center**  dictionary | Dictionary of all the datacenter attributes. Datacenter attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/datacenter>.  **Returned:** On success if datacenter is found. |
| **id**  string | ID of the managed datacenter  **Returned:** On success if datacenter is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
