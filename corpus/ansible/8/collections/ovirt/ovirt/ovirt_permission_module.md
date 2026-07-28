---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_permission module – Module to manage permissions of users/groups in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_permission_module.html
fetched_at: 2026-07-28T02:49:44+00:00
---
# ovirt.ovirt.ovirt_permission module – Module to manage permissions of users/groups in oVirt/RHV

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
> see [Requirements](ovirt_permission_module.md#ansible-collections-ovirt-ovirt-ovirt-permission-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_permission`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_permission_module.md#synopsis)
- [Requirements](ovirt_permission_module.md#requirements)
- [Parameters](ovirt_permission_module.md#parameters)
- [Notes](ovirt_permission_module.md#notes)
- [Examples](ovirt_permission_module.md#examples)
- [Return Values](ovirt_permission_module.md#return-values)

## [Synopsis](ovirt_permission_module.md#id1)

- Module to manage permissions of users/groups in oVirt/RHV.

## [Requirements](ovirt_permission_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_permission_module.md#id3)

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
| **authz_name**  aliases: domain  string / required | Authorization provider of the user/group. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **group_name**  string | Name of the group to manage.  Note that if group does not exist in the system this module will fail, you should ensure the group exists by using ovirt.ovirt.ovirt_groups module. |
| **namespace**  string | Namespace of the authorization provider, where user/group resides. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **object_id**  string | ID of the object where the permissions should be managed. |
| **object_name**  string | Name of the object where the permissions should be managed. |
| **object_type**  string | The object where the permissions should be managed.  **Choices:**   - `"cluster"` - `"cpu_profile"` - `"data_center"` - `"disk"` - `"disk_profile"` - `"host"` - `"network"` - `"storage_domain"` - `"system"` - `"template"` - `"vm"` ← (default) - `"vm_pool"` - `"vnic_profile"` - `"mac_pool"` |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **quota_name**  string | Name of the quota to assign permission. Works only with `object_type` *data_center*. |
| **role**  string | Name of the role to be assigned to user/group on specific object.  **Default:** `"UserRole"` |
| **state**  string | Should the permission be present/absent.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **user_name**  string | Username of the user to manage. In most LDAPs it’s *uid* of the user, but in Active Directory you must specify *UPN* of the user.  Note that if user does not exist in the system this module will fail, you should ensure the user exists by using ovirt.ovirt.ovirt_users module. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_permission_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_permission_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Add user user1 from authorization provider example.com-authz
  ovirt.ovirt.ovirt_permission:
    user_name: user1
    authz_name: example.com-authz
    object_type: vm
    object_name: myvm
    role: UserVmManager

- name: Remove permission from user
  ovirt.ovirt.ovirt_permission:
    state: absent
    user_name: user1
    authz_name: example.com-authz
    object_type: cluster
    object_name: mycluster
    role: ClusterAdmin

- name: Assign QuotaConsumer role to user
  ovirt.ovirt.ovirt_permissions:
    state: present
    user_name: user1
    authz_name: example.com-authz
    object_type: data_center
    object_name: mydatacenter
    quota_name: myquota
    role: QuotaConsumer

- name: Assign QuotaConsumer role to group
  ovirt.ovirt.ovirt_permissions:
    state: present
    group_name: group1
    authz_name: example.com-authz
    object_type: data_center
    object_name: mydatacenter
    quota_name: myquota
    role: QuotaConsumer

- ovirt.ovirt.ovirt_permission:
    user_name: user1
    authz_name: example.com-authz
    object_type: mac_pool
    object_name: Default
    role: MacPoolUser
```

## [Return Values](ovirt_permission_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the permission which is managed  **Returned:** On success if permission is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **permission**  dictionary | Dictionary of all the permission attributes. Permission attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/permission>.  **Returned:** On success if permission is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
