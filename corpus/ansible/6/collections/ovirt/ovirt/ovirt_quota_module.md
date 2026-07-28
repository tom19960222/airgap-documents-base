---
collection: ansible
version: "6"
title: "ovirt.ovirt.ovirt_quota module – Module to manage datacenter quotas in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ovirt/ovirt/ovirt_quota_module.html
fetched_at: 2026-07-28T00:17:42+00:00
---
# ovirt.ovirt.ovirt_quota module – Module to manage datacenter quotas in oVirt/RHV

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
> see [Requirements](ovirt_quota_module.md#ansible-collections-ovirt-ovirt-ovirt-quota-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_quota`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_quota_module.md#synopsis)
- [Requirements](ovirt_quota_module.md#requirements)
- [Parameters](ovirt_quota_module.md#parameters)
- [Notes](ovirt_quota_module.md#notes)
- [Examples](ovirt_quota_module.md#examples)
- [Return Values](ovirt_quota_module.md#return-values)

## [Synopsis](ovirt_quota_module.md#id1)

- Module to manage datacenter quotas in oVirt/RHV

## [Requirements](ovirt_quota_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_quota_module.md#id3)

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
| **cluster_grace**  aliases: cluster_hard_limit  integer | Cluster grace(hard limit) defined in percentage (1-100). |
| **cluster_threshold**  aliases: cluster_soft_limit  integer | Cluster threshold(soft limit) defined in percentage (0-100). |
| **clusters**  list / elements=dictionary | List of dictionary of cluster limits, which is valid to specific cluster.  If cluster isn’t specified it’s valid to all clusters in system: |
| **cluster**  string | Name of the cluster. |
| **cpu**  string | CPU limit. |
| **memory**  string | Memory limit (in GiB). |
| **data_center**  string / required | Name of the datacenter where quota should be managed. |
| **description**  string | Description of the quota to manage. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  Choices:   - `false` ← (default) - `true` |
| **id**  string | ID of the quota to manage. |
| **name**  string / required | Name of the quota to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  Default: `3` |
| **state**  string | Should the quota be present/absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_grace**  aliases: storage_hard_limit  integer | Storage grace(hard limit) defined in percentage (1-100). |
| **storage_threshold**  aliases: storage_soft_limit  integer | Storage threshold(soft limit) defined in percentage (0-100). |
| **storages**  list / elements=dictionary | List of dictionary of storage limits, which is valid to specific storage.  If storage isn’t specified it’s valid to all storages in system: |
| **size**  string | Size limit (in GiB). |
| **storage**  string | Name of the storage. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  Default: `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  Choices:   - `false` - `true` ← (default) |

## [Notes](ovirt_quota_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_quota_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add cluster quota to cluster cluster1 with memory limit 20GiB and CPU limit to 10:
- ovirt.ovirt.ovirt_quota:
    name: quota1
    data_center: dcX
    clusters:
        - name: cluster1
          memory: 20
          cpu: 10

# Add cluster quota to all clusters with memory limit 30GiB and CPU limit to 15:
- ovirt.ovirt.ovirt_quota:
    name: quota2
    data_center: dcX
    clusters:
        - memory: 30
          cpu: 15

# Add storage quota to storage data1 with size limit to 100GiB
- ovirt.ovirt.ovirt_quota:
    name: quota3
    data_center: dcX
    storage_grace: 40
    storage_threshold: 60
    storages:
        - name: data1
          size: 100

# Remove quota quota1 (Note the quota must not be assigned to any VM/disk):
- ovirt.ovirt.ovirt_quota:
    state: absent
    data_center: dcX
    name: quota1

# Change Quota Name
- ovirt.ovirt.ovirt_quota:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_quota_name"
    data_center: dcX
```

## [Return Values](ovirt_quota_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the quota which is managed  Returned: On success if quota is found.  Sample: `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **quota**  dictionary | Dictionary of all the quota attributes. Quota attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/quota>.  Returned: On success if quota is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

[Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
[Homepage](https://www.ovirt.org/)
[Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
