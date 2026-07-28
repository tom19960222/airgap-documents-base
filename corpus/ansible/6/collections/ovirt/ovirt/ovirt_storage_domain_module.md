---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_storage_domain module – Module to manage storage domains in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_storage_domain_module.html
fetched_at: 2026-07-28T00:17:47+00:00
---
# ovirt.ovirt.ovirt_storage_domain module – Module to manage storage domains in oVirt/RHV

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
> see [Requirements](ovirt_storage_domain_module.md#ansible-collections-ovirt-ovirt-ovirt-storage-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_storage_domain`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_storage_domain_module.md#synopsis)
- [Requirements](ovirt_storage_domain_module.md#requirements)
- [Parameters](ovirt_storage_domain_module.md#parameters)
- [Notes](ovirt_storage_domain_module.md#notes)
- [Examples](ovirt_storage_domain_module.md#examples)
- [Return Values](ovirt_storage_domain_module.md#return-values)

## [Synopsis](ovirt_storage_domain_module.md#id1)

- Module to manage storage domains in oVirt/RHV

## [Requirements](ovirt_storage_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_storage_domain_module.md#id3)

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
| **backup**  boolean | Boolean flag which indicates whether the storage domain is configured as backup or not.  Choices:   - `false` - `true` |
| **comment**  string | Comment of the storage domain. |
| **critical_space_action_blocker**  integer | Indicates the minimal free space the storage domain should contain in percentages. |
| **data_center**  string | Data center name where storage domain should be attached.  This parameter isn’t idempotent, it’s not possible to change data center of storage domain. |
| **description**  string | Description of the storage domain. |
| **destroy**  boolean | Logical remove of the storage domain. If *true* retains the storage domain’s data for import.  This parameter is relevant only when `state` is *absent*.  Choices:   - `false` - `true` |
| **discard_after_delete**  boolean | If *True* storage domain blocks will be discarded upon deletion. Enabled by default.  This parameter is relevant only for block based storage domains.  Choices:   - `false` - `true` |
| **domain_function**  aliases: type  string | Function of the storage domain.  This parameter isn’t idempotent, it’s not possible to change domain function of storage domain.  Choices:   - `"data"` ← (default) - `"iso"` - `"export"` |
| **fcp**  dictionary | Dictionary with values for fibre channel storage type:  Note that these parameters are not idempotent. |
| **lun_id**  string | LUN id. |
| **override_luns**  boolean | If *True* FCP storage domain LUNs will be overridden before adding.  Choices:   - `false` - `true` |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **format**  boolean | If *True* storage domain will be formatted after removing it from oVirt/RHV.  This parameter is relevant only when `state` is *absent*.  Choices:   - `false` - `true` |
| **glusterfs**  dictionary | Dictionary with values for GlusterFS storage type:  Note that these parameters are not idempotent. |
| **address**  string | Address of the Gluster server. E.g.: myserver.mydomain.com |
| **mount_options**  string | Option which will be passed when mounting storage. |
| **path**  string | Path of the mount point. E.g.: /path/to/my/data |
| **host**  string | Host to be used to mount storage. |
| **id**  string | Id of the storage domain to be imported. |
| **iscsi**  dictionary | Dictionary with values for iSCSI storage type:  Note that these parameters are not idempotent. |
| **address**  string | Address of the iSCSI storage server. |
| **lun_id**  string | LUN id(s). |
| **override_luns**  boolean | If *True* ISCSI storage domain luns will be overridden before adding.  Choices:   - `false` - `true` |
| **password**  string | A CHAP password for logging into a target. |
| **port**  string | Port of the iSCSI storage server. |
| **target**  string | The target IQN for the storage device. |
| **target_lun_map**  string | List of dictionary containing targets and LUNs. |
| **username**  string | A CHAP user name for logging into a target. |
| **localfs**  dictionary | Dictionary with values for localfs storage type:  Note that these parameters are not idempotent. |
| **path**  string | Path of the mount point. E.g.: /path/to/my/data |
| **managed_block_storage**  dictionary | Dictionary with values for managed block storage type  Note: available from ovirt 4.3 |
| **driver_options**  list / elements=dictionary | The options to be passed when creating a storage domain using a cinder driver.  List of dictionary containing `name` and `value` of driver option |
| **driver_sensitive_options**  list / elements=dictionary | Parameters containing sensitive information, to be passed when creating a storage domain using a cinder driver.  List of dictionary containing `name` and `value` of driver sensitive option |
| **name**  string | Name of the storage domain to manage. (Not required when state is *imported*) |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **nfs**  dictionary | Dictionary with values for NFS storage type:  Note that these parameters are not idempotent. |
| **address**  string | Address of the NFS server. E.g.: myserver.mydomain.com |
| **mount_options**  string | Option which will be passed when mounting storage. |
| **path**  string | Path of the mount point. E.g.: /path/to/my/data |
| **retrans**  string | The number of times to retry a request before attempting further recovery actions. Range 0 to 65535. |
| **timeout**  string | The time in tenths of a second to wait for a response before retrying NFS requests. Range 0 to 65535. |
| **version**  string | NFS version. One of: *auto*, *v3*, *v4* or *v4_1*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **posixfs**  dictionary | Dictionary with values for PosixFS storage type:  Note that these parameters are not idempotent. |
| **mount_options**  string | Option which will be passed when mounting storage. |
| **path**  string | Path of the mount point. E.g.: /path/to/my/data |
| **vfs_type**  string | Virtual File System type. |
| **state**  string | Should the storage domain be present/absent/maintenance/unattached/imported/update_ovf_store  *imported* is supported since version 2.4.  *update_ovf_store* is supported since version 2.5, currently if `wait` is (true), we don’t wait for update.  Choices:   - `"present"` ← (default) - `"absent"` - `"maintenance"` - `"unattached"` - `"imported"` - `"update_ovf_store"` |
| **storage_format**  string | One of v1, v2, v3, v4, v5 - sets the storage format of the domain. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |
| **warning_low_space**  integer | Indicates the minimum percentage of a free space in a storage domain to present a warning. |
| **wipe_after_delete**  boolean | Boolean flag which indicates whether the storage domain should wipe the data after delete.  Choices:   - `false` - `true` |

## [Notes](ovirt_storage_domain_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_storage_domain_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add data NFS storage domain
- ovirt.ovirt.ovirt_storage_domain:
    name: data_nfs
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/data

# Add data NFS storage domain with id for data center
- ovirt.ovirt.ovirt_storage_domain:
    name: data_nfs
    host: myhost
    data_center: 11111
    nfs:
      address: 10.34.63.199
      path: /path/data
      mount_options: noexec,nosuid

# Add data NFS storage domain in an older format
# E.g. the following will work if the data center is in 4.2 level.
# Without this, you might get as error like:
#     Cannot attach Storage. Storage Domain format V5 is illegal.
- ovirt.ovirt.ovirt_storage_domain:
    name: data_nfs
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/data
    storage_format: v4

# Add data localfs storage domain
- ovirt.ovirt.ovirt_storage_domain:
    name: data_localfs
    host: myhost
    data_center: mydatacenter
    localfs:
      path: /path/to/data

# Add data iSCSI storage domain:
- ovirt.ovirt.ovirt_storage_domain:
    name: data_iscsi
    host: myhost
    data_center: mydatacenter
    iscsi:
      target: iqn.2016-08-09.domain-01:nickname
      lun_id:
       - 1IET_000d0001
       - 1IET_000d0002
      address: 10.34.63.204
    discard_after_delete: True
    backup: False
    critical_space_action_blocker: 5
    warning_low_space: 10

# Since Ansible 2.5 you can specify multiple targets for storage domain,
# Add data iSCSI storage domain with multiple targets:
- ovirt.ovirt.ovirt_storage_domain:
    name: data_iscsi
    host: myhost
    data_center: mydatacenter
    iscsi:
      target_lun_map:
        - target: iqn.2016-08-09.domain-01:nickname
          lun_id: 1IET_000d0001
        - target: iqn.2016-08-09.domain-02:nickname
          lun_id: 1IET_000d0002
      address: 10.34.63.204
    discard_after_delete: True

# Add data glusterfs storage domain
- ovirt.ovirt.ovirt_storage_domain:
    name: glusterfs_1
    host: myhost
    data_center: mydatacenter
    glusterfs:
      address: 10.10.10.10
      path: /path/data

# Create export NFS storage domain:
- ovirt.ovirt.ovirt_storage_domain:
    name: myexportdomain
    domain_function: export
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/export
    wipe_after_delete: False
    backup: True
    critical_space_action_blocker: 2
    warning_low_space: 5

# Import export NFS storage domain:
- ovirt.ovirt.ovirt_storage_domain:
    state: imported
    domain_function: export
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/export

# Import FCP storage domain:
- ovirt.ovirt.ovirt_storage_domain:
    state: imported
    name: data_fcp
    host: myhost
    data_center: mydatacenter
    fcp: {}

# Update OVF_STORE:
- ovirt.ovirt.ovirt_storage_domain:
    state: update_ovf_store
    name: domain

# Create ISO NFS storage domain
- ovirt.ovirt.ovirt_storage_domain:
    name: myiso
    domain_function: iso
    host: myhost
    data_center: mydatacenter
    nfs:
      address: 10.34.63.199
      path: /path/iso

# Create managed storage domain
# Available from ovirt 4.3 and ansible 2.9
- ovirt.ovirt.ovirt_storage_domain:
    name: my_managed_domain
    host: myhost
    data_center: mydatacenter
    managed_block_storage:
      driver_options:
        - name: rbd_pool
          value: pool1
        - name: rbd_user
          value: admin
        - name: volume_driver
          value: cinder.volume.drivers.rbd.RBDDriver
        - name: rbd_keyring_conf
          value: /etc/ceph/keyring
      driver_sensitive_options:
        - name: secret_password
          value: password

# Remove storage domain
- ovirt.ovirt.ovirt_storage_domain:
    state: absent
    name: mystorage_domain
    format: true
```

## [Return Values](ovirt_storage_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the storage domain which is managed  Returned: On success if storage domain is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **storage_domain**  dictionary | Dictionary of all the storage domain attributes. Storage domain attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/storage_domain>.  Returned: On success if storage domain is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
