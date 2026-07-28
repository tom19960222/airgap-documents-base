---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_snapshot module – Module to manage Virtual Machine Snapshots in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_snapshot_module.html
fetched_at: 2026-07-28T00:17:45+00:00
---
# ovirt.ovirt.ovirt_snapshot module – Module to manage Virtual Machine Snapshots in oVirt/RHV

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
> see [Requirements](ovirt_snapshot_module.md#ansible-collections-ovirt-ovirt-ovirt-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_snapshot`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_snapshot_module.md#synopsis)
- [Requirements](ovirt_snapshot_module.md#requirements)
- [Parameters](ovirt_snapshot_module.md#parameters)
- [Notes](ovirt_snapshot_module.md#notes)
- [Examples](ovirt_snapshot_module.md#examples)
- [Return Values](ovirt_snapshot_module.md#return-values)

## [Synopsis](ovirt_snapshot_module.md#id1)

- Module to manage Virtual Machine Snapshots in oVirt/RHV

## [Requirements](ovirt_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_snapshot_module.md#id3)

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
| **description**  string | Description of the snapshot. |
| **disk_id**  string | Disk id which you want to upload or download  To get disk, you need to define disk_id or disk_name |
| **disk_name**  string | Disk name which you want to upload or download |
| **disks**  list / elements=dictionary | List of disks which should be created with snapshot. |
| **id**  string | Id of the disk which should will be created. |
| **name**  string | Name of the disk which should will be created. |
| **download_image_path**  string | Path on a file system where snapshot should be downloaded.  Note that you must have an valid oVirt/RHV engine CA in your system trust store or you must provide it in `ca_file` parameter.  Note that the snapshot is not downloaded when the file already exists, but you can forcibly download the snapshot when using `force` I (true). |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **keep_days_old**  integer | Number of days after which should snapshot be deleted.  It will check all snapshots of virtual machine and delete them, if they are older. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **snapshot_id**  string | ID of the snapshot to manage. |
| **state**  string | Should the Virtual Machine snapshot be restore/present/absent.  Choices:   - `"restore"` - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **upload_image_path**  string | Path to disk image, which should be uploaded. |
| **use_memory**  aliases: restore_memory, save_memory  boolean | If *true* and `state` is *present* save memory of the Virtual Machine if it’s running.  If *true* and `state` is *restore* restore memory of the Virtual Machine.  Note that Virtual Machine will be paused while saving the memory.  Choices:   - `false` - `true` |
| **vm_id**  string  added in ovirt.ovirt 2.2.0 | ID of the Virtual Machine to manage. Required one of `vm_name` or `vm_id`. |
| **vm_name**  string | Name of the Virtual Machine to manage. Required one of `vm_name` or `vm_id`. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_snapshot_module.md#id4)

> **Note:**
>
> - Note that without a guest agent the data on the created snapshot may be inconsistent.
> - Deleting a snapshot does not remove any information from the virtual machine - it simply removes a return-point. However, restoring a virtual machine from a snapshot deletes any content that was written to the virtual machine after the time the snapshot was taken.
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_snapshot_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create snapshot:
- ovirt.ovirt.ovirt_snapshot:
    vm_name: rhel7
    description: MySnapshot
  register: snapshot

# Create snapshot and save memory:
- ovirt.ovirt.ovirt_snapshot:
    vm_name: rhel7
    description: SnapWithMem
    use_memory: true
  register: snapshot

# Restore snapshot:
- ovirt.ovirt.ovirt_snapshot:
    state: restore
    vm_name: rhel7
    snapshot_id: "{{ snapshot.id }}"

# Remove snapshot:
- ovirt.ovirt.ovirt_snapshot:
    state: absent
    vm_name: rhel7
    snapshot_id: "{{ snapshot.id }}"

# Upload local image to disk and attach it to vm:
# Since Ansible 2.8
- ovirt.ovirt.ovirt_snapshot:
    name: mydisk
    vm_name: myvm
    upload_image_path: /path/to/mydisk.qcow2

# Download snapshot to local file system:
# Since Ansible 2.8
- ovirt.ovirt.ovirt_snapshot:
    snapshot_id: 7de90f31-222c-436c-a1ca-7e655bd5b60c
    disk_name: DiskName
    vm_name: myvm
    download_image_path: /home/user/mysnaphost.qcow2

# Delete all snapshots older than 2 days
- ovirt.ovirt.ovirt_snapshot:
    vm_name: test
    keep_days_old: 2

- name: Select which disks should be add to snapshot
  ovirt.ovirt.ovirt_snapshot:
    vm_name: test
    disks:
      - id: 7de90f31-222c-436c-a1ca-7e655bd5b60c
      - name: my_disk_name
```

## [Return Values](ovirt_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the snapshot which is managed  Returned: On success if snapshot is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **snapshot**  dictionary | Dictionary of all the snapshot attributes. Snapshot attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/snapshot>.  Returned: On success if snapshot is found. |
| **snapshots**  list / elements=string | List of deleted snapshots when keep_days_old is defined and snapshot is older than the input days  Returned: On success returns deleted snapshots |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
