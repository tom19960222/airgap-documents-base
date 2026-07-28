---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_disk module – Module to manage Virtual Machine and floating disks in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_disk_module.html
fetched_at: 2026-07-28T00:17:26+00:00
---
# ovirt.ovirt.ovirt_disk module – Module to manage Virtual Machine and floating disks in oVirt/RHV

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
> see [Requirements](ovirt_disk_module.md#ansible-collections-ovirt-ovirt-ovirt-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_disk`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_disk_module.md#synopsis)
- [Requirements](ovirt_disk_module.md#requirements)
- [Parameters](ovirt_disk_module.md#parameters)
- [Notes](ovirt_disk_module.md#notes)
- [Examples](ovirt_disk_module.md#examples)
- [Return Values](ovirt_disk_module.md#return-values)

## [Synopsis](ovirt_disk_module.md#id1)

- Module to manage Virtual Machine and floating disks in oVirt/RHV.
- WARNING: If you are installing the collection from ansible galaxy you need to install ‘qemu-img’ package.

## [Requirements](ovirt_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activate**  boolean | *True* if the disk should be activated.  When creating disk of virtual machine it is set to *True*.  Choices:   - `false` - `true` |
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
| **backup**  string  added in ovirt.ovirt 1.1.0 | The backup behavior supported by the disk.  Choices:   - `"incremental"` |
| **bootable**  boolean | *True* if the disk should be bootable. By default when disk is created it isn’t bootable.  Choices:   - `false` - `true` |
| **content_type**  string | Specify if the disk is a data disk or ISO image or a one of a the Hosted Engine disk types  The Hosted Engine disk content types are available with Engine 4.3+ and Ansible 2.8  Choices:   - `"data"` ← (default) - `"iso"` - `"hosted_engine"` - `"hosted_engine_sanlock"` - `"hosted_engine_metadata"` - `"hosted_engine_configuration"` |
| **description**  string | Description of the disk image to manage. |
| **download_image_path**  string | Path on a file system where disk should be downloaded.  Note that you must have an valid oVirt/RHV engine CA in your system trust store or you must provide it in `ca_file` parameter.  Note that the disk is not downloaded when the file already exists, but you can forcibly download the disk when using `force` I (true). |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **force**  boolean | Please take a look at `image_path` documentation to see the correct usage of this parameter.  Choices:   - `false` ← (default) - `true` |
| **format**  string | Specify format of the disk.  Note that this option isn’t idempotent as it’s not currently possible to change format of the disk via API.  Choices:   - `"raw"` - `"cow"` ← (default) |
| **host**  string | When the hypervisor name is specified the newly created disk or an existing disk will refresh its information about the underlying storage( Disk size, Serial, Product ID, Vendor ID …) The specified host will be used for gathering the storage related information. This option is only valid for passthrough disks. This option requires at least the logical_unit.id to be specified |
| **id**  string | ID of the disk to manage. Either `id` or `name` is required. |
| **image_provider**  string | When `state` is *exported* disk is exported to given Glance image provider.  When `state` is *imported* disk is imported from given Glance image provider.  `**IMPORTANT**`  There is no reliable way to achieve idempotency, so every time you specify this parameter the disk is exported, so please handle your playbook accordingly to not export the disk all the time. This option is valid only for template disks. |
| **interface**  string | Driver of the storage interface.  It’s required parameter when creating the new disk.  Choices:   - `"virtio"` - `"ide"` - `"sata"` - `"virtio_scsi"` |
| **logical_unit**  dictionary | Dictionary which describes LUN to be directly attached to VM: |
| **address**  string | Address of the storage server. Used by iSCSI. |
| **lun_id**  string | LUN id. |
| **password**  string | CHAP Password of the user to be used to access storage server. Used by iSCSI. |
| **port**  string | Port of the storage server. Used by iSCSI. |
| **storage_type**  string | Storage type either *fcp* or *iscsi*. |
| **target**  string | iSCSI target. |
| **username**  string | CHAP Username to be used to access storage server. Used by iSCSI. |
| **max_workers**  integer  added in ovirt.ovirt 1.7.0 | The number of workers which should be used in the upload/download of the image.  The use of multiple workers can speed up the process. |
| **name**  aliases: alias  string | Name of the disk to manage. Either `id` or `name`/`alias` is required. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **openstack_volume_type**  string | Name of the openstack volume type. This is valid when working with cinder. |
| **pass_discard**  boolean  added in ovirt.ovirt 1.2.0 | Defines whether the virtual machine passes discard commands to the storage.  Choices:   - `false` - `true` |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **profile**  string | Disk profile name to be attached to disk. By default profile is chosen by oVirt/RHV engine. |
| **propagate_errors**  boolean  added in ovirt.ovirt 1.2.0 | Indicates if disk errors should cause virtual machine to be paused or if disk errors should be  propagated to the the guest operating system instead.  Choices:   - `false` - `true` |
| **quota_id**  string | Disk quota ID to be used for disk. By default quota is chosen by oVirt/RHV engine. |
| **read_only**  boolean | *True* if the disk should be read_only. By default when disk is created it isn’t read_only.  Choices:   - `false` - `true` |
| **scsi_passthrough**  string  added in ovirt.ovirt 1.2.0 | Indicates whether SCSI passthrough is enable and its policy.  Setting a value of `filtered`/`unfiltered` will enable SCSI passthrough for a LUN disk with unprivileged/privileged SCSI I/O.  To disable SCSI passthrough the value should be set to `disabled`  Choices:   - `"disabled"` - `"filtered"` - `"unfiltered"` |
| **shareable**  boolean | *True* if the disk should be shareable. By default when disk is created it isn’t shareable.  Choices:   - `false` - `true` |
| **size**  string | Size of the disk. Size should be specified using IEC standard units. For example 10GiB, 1024MiB, etc.  Size can be only increased, not decreased.  If the disk is referenced by `name` and is attached to a VM, make sure to specify `vm_name`/`vm_id` to prevent extension of another disk that is not attached to the VM. |
| **sparse**  boolean | *True* if the disk should be sparse (also known as *thin provision*). If the parameter is omitted, cow disks will be created as sparse and raw disks as *preallocated*  Note that this option isn’t idempotent as it’s not currently possible to change sparseness of the disk via API.  Choices:   - `false` - `true` |
| **sparsify**  boolean | *True* if the disk should be sparsified.  Sparsification frees space in the disk image that is not used by its filesystem. As a result, the image will occupy less space on the storage.  Note that this parameter isn’t idempotent, as it’s not possible to check if the disk should be or should not be sparsified.  Choices:   - `false` - `true` |
| **state**  string | Should the Virtual Machine disk be present/absent/attached/detached/exported/imported.  Choices:   - `"present"` ← (default) - `"absent"` - `"attached"` - `"detached"` - `"exported"` - `"imported"` |
| **storage_domain**  string | Storage domain name where disk should be created. |
| **storage_domains**  list / elements=string | Storage domain names where disk should be copied.  `**IMPORTANT**`  There is no reliable way to achieve idempotency, so every time you specify this parameter the disks are copied, so please handle your playbook accordingly to not copy the disks all the time. This is valid only for VM and floating disks, template disks works as expected. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **upload_image_path**  aliases: image_path  string | Path to disk image, which should be uploaded.  Note if `size` is not specified the size of the disk will be determined by the size of the specified image.  Note that currently we support only compatibility version 0.10 of the qcow disk.  Note that you must have an valid oVirt/RHV engine CA in your system trust store or you must provide it in `ca_file` parameter.  Note that there is no reliable way to achieve idempotency, so if you want to upload the disk even if the disk with `id` or `name` exists, then please use `force` *true*. If you will use `force` *false*, which is default, then the disk image won’t be uploaded.  Note that to upload iso the `format` should be ‘raw’ |
| **uses_scsi_reservation**  boolean  added in ovirt.ovirt 1.2.0 | Defines whether SCSI reservation is enabled for this disk.  Choices:   - `false` - `true` |
| **vm_id**  string | ID of the Virtual Machine to manage. Either `vm_id` or `vm_name` is required if `state` is *attached* or *detached*. |
| **vm_name**  string | Name of the Virtual Machine to manage. Either `vm_id` or `vm_name` is required if `state` is *attached* or *detached*. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |
| **wipe_after_delete**  boolean | If the disk’s Wipe After Delete is enabled, then the disk is first wiped.  Choices:   - `false` - `true` |

## [Notes](ovirt_disk_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_disk_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create and attach new disk to VM
- ovirt.ovirt.ovirt_disk:
    name: myvm_disk
    vm_name: rhel7
    size: 10GiB
    format: cow
    interface: virtio
    storage_domain: data

# Attach logical unit to VM rhel7
- ovirt.ovirt.ovirt_disk:
    vm_name: rhel7
    logical_unit:
      target: iqn.2016-08-09.brq.str-01:omachace
      id: 1IET_000d0001
      address: 10.34.63.204
    interface: virtio

# Detach disk from VM
- ovirt.ovirt.ovirt_disk:
    state: detached
    name: myvm_disk
    vm_name: rhel7
    size: 10GiB
    format: cow
    interface: virtio

# Change Disk Name
- ovirt.ovirt.ovirt_disk:
    id: 00000000-0000-0000-0000-000000000000
    storage_domain: data
    name: "new_disk_name"
    vm_name: rhel7

# Upload local image to disk and attach it to vm:
# Since Ansible 2.3
- ovirt.ovirt.ovirt_disk:
    name: mydisk
    vm_name: myvm
    interface: virtio
    size: 10GiB
    format: cow
    image_path: /path/to/mydisk.qcow2
    storage_domain: data

# Download disk to local file system:
# Since Ansible 2.3
- ovirt.ovirt.ovirt_disk:
    id: 7de90f31-222c-436c-a1ca-7e655bd5b60c
    download_image_path: /home/user/mydisk.qcow2

# Export disk as image to Glance domain
# Since Ansible 2.4
- ovirt.ovirt.ovirt_disk:
    id: 7de90f31-222c-436c-a1ca-7e655bd5b60c
    image_provider: myglance
    state: exported

# Defining a specific quota while creating a disk image:
# Since Ansible 2.5
- ovirt.ovirt.ovirt_quotas_info:
    data_center: Default
    name: myquota
  register: quota
- ovirt.ovirt.ovirt_disk:
    name: mydisk
    size: 10GiB
    storage_domain: data
    description: somedescriptionhere
    quota_id: "{{ quota.ovirt_quotas[0]['id'] }}"

# Upload an ISO image
# Since Ansible 2.8
- ovirt.ovirt.ovirt_disk:
    name: myiso
    upload_image_path: /path/to/iso/image
    storage_domain: data
    size: 4 GiB
    wait: true
    bootable: true
    format: raw
    content_type: iso

# Add fiber chanel disk
- name: Create disk
  ovirt.ovirt.ovirt_disk:
    name: fcp_disk
    host: my_host
    logical_unit:
        id: 3600a09803830447a4f244c4657597777
        storage_type: fcp
```

## [Return Values](ovirt_disk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **disk**  dictionary | Dictionary of all the disk attributes. Disk attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/disk>.  Returned: On success if disk is found and `vm_id` or `vm_name` wasn’t passed. |
| **disk_attachment**  dictionary | Dictionary of all the disk attachment attributes. Disk attachment attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/disk_attachment>.  Returned: On success if disk is found and `vm_id` or `vm_name` was passed and VM was found. |
| **id**  string | ID of the managed disk  Returned: On success if disk is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
