---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_mac_pool module – Module to manage MAC pools in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_mac_pool_module.html
fetched_at: 2026-07-28T02:49:38+00:00
---
# ovirt.ovirt.ovirt_mac_pool module – Module to manage MAC pools in oVirt/RHV

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
> see [Requirements](ovirt_mac_pool_module.md#ansible-collections-ovirt-ovirt-ovirt-mac-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_mac_pool`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_mac_pool_module.md#synopsis)
- [Requirements](ovirt_mac_pool_module.md#requirements)
- [Parameters](ovirt_mac_pool_module.md#parameters)
- [Notes](ovirt_mac_pool_module.md#notes)
- [Examples](ovirt_mac_pool_module.md#examples)
- [Return Values](ovirt_mac_pool_module.md#return-values)

## [Synopsis](ovirt_mac_pool_module.md#id1)

- This module manage MAC pools in oVirt/RHV.

## [Requirements](ovirt_mac_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_mac_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_duplicates**  boolean | If *true* allow a MAC address to be used multiple times in a pool.  Default value is set by oVirt/RHV engine to *false*.  **Choices:**   - `false` - `true` |
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
| **description**  string | Description of the MAC pool. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **id**  string | ID of the mac pool to manage. |
| **name**  string / required | Name of the MAC pool to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **ranges**  list / elements=string | List of MAC ranges. The from and to should be split by comma.  For example: 00:1a:4a:16:01:51,00:1a:4a:16:01:61 |
| **state**  string | Should the mac pool be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_mac_pool_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_mac_pool_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create MAC pool:
- ovirt.ovirt.ovirt_mac_pool:
    name: mymacpool
    allow_duplicates: false
    ranges:
      - 00:1a:4a:16:01:51,00:1a:4a:16:01:61
      - 00:1a:4a:16:02:51,00:1a:4a:16:02:61

# Remove MAC pool:
- ovirt.ovirt.ovirt_mac_pool:
    state: absent
    name: mymacpool

# Change MAC pool Name
- ovirt.ovirt.ovirt_nic:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_mac_pool_name"
```

## [Return Values](ovirt_mac_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the MAC pool which is managed  **Returned:** On success if MAC pool is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **template**  dictionary | Dictionary of all the MAC pool attributes. MAC pool attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/mac_pool>.  **Returned:** On success if MAC pool is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
