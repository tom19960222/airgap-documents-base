---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_storage_connection module – Module to manage storage connections in oVirt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_storage_connection_module.html
fetched_at: 2026-07-28T02:49:55+00:00
---
# ovirt.ovirt.ovirt_storage_connection module – Module to manage storage connections in oVirt

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
> see [Requirements](ovirt_storage_connection_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-connection-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_storage_connection`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_storage_connection_module.md#synopsis)
- [Requirements](ovirt_storage_connection_module.md#requirements)
- [Parameters](ovirt_storage_connection_module.md#parameters)
- [Notes](ovirt_storage_connection_module.md#notes)
- [Examples](ovirt_storage_connection_module.md#examples)
- [Return Values](ovirt_storage_connection_module.md#return-values)

## [Synopsis](ovirt_storage_connection_module.md#id1)

- Module to manage storage connections in oVirt

## [Requirements](ovirt_storage_connection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_storage_connection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Address of the storage server. E.g.: myserver.mydomain.com |
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
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | This parameter is relevant only when updating a connection.  If *true* the storage domain don’t have to be in *MAINTENANCE* state, so the storage connection is updated.  **Choices:**   - `false` ← (default) - `true` |
| **id**  string | Id of the storage connection to manage. |
| **mount_options**  string | Option which will be passed when mounting storage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **nfs_retrans**  integer | The number of times to retry a request before attempting further recovery actions. Range 0 to 65535. |
| **nfs_timeout**  integer | The time in tenths of a second to wait for a response before retrying NFS requests. Range 0 to 65535. |
| **nfs_version**  string | NFS version. One of: *auto*, *v3*, *v4* or *v4_1*. |
| **password**  string | A CHAP password for logging into a target. |
| **path**  string | Path of the mount point of the storage. E.g.: /path/to/my/data |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **port**  integer | Port of the iSCSI storage server. |
| **state**  string | Should the storage connection be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage**  string | Name of the storage domain to be used with storage connection. |
| **target**  string | The target IQN for the storage device. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **type**  string | Storage type. For example: *nfs*, *iscsi*, etc. |
| **username**  string | A CHAP username for logging into a target. |
| **vfs_type**  string | Virtual File System type. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_storage_connection_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_storage_connection_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add new storage connection:
- ovirt.ovirt.ovirt_storage_connection:
    storage: myiscsi
    address: 10.34.63.199
    target: iqn.2016-08-09.domain-01:nickname
    port: 3260
    type: iscsi

# Update the existing storage connection address:
- ovirt.ovirt.ovirt_storage_connection:
    id: 26915c96-92ff-47e5-9e77-b581db2f2d36
    address: 10.34.63.204
    force: true

# Remove storage connection:
- ovirt.ovirt.ovirt_storage_connection:
    id: 26915c96-92ff-47e5-9e77-b581db2f2d36
```

## [Return Values](ovirt_storage_connection_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the storage connection which is managed  **Returned:** On success if storage connection is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **storage_connection**  dictionary | Dictionary of all the storage connection attributes. Storage connection attributes can be found on your oVirt instance at following url: <https://ovirt.example.com/ovirt-engine/api/model#types/storage_connection>.  **Returned:** On success if storage connection is found. |

### Authors

- Ondra Machacek (@machacekondra)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
