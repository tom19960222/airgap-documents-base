---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_tag module – Module to manage tags in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_tag_module.html
fetched_at: 2026-07-28T02:50:02+00:00
---
# ovirt.ovirt.ovirt_tag module – Module to manage tags in oVirt/RHV

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
> see [Requirements](ovirt_tag_module.md#ansible-collections-ovirt-ovirt-ovirt-tag-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_tag`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_tag_module.md#synopsis)
- [Requirements](ovirt_tag_module.md#requirements)
- [Parameters](ovirt_tag_module.md#parameters)
- [Notes](ovirt_tag_module.md#notes)
- [Examples](ovirt_tag_module.md#examples)
- [Return Values](ovirt_tag_module.md#return-values)

## [Synopsis](ovirt_tag_module.md#id1)

- This module manage tags in oVirt/RHV. It can also manage assignments of those tags to entities.

## [Requirements](ovirt_tag_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_tag_module.md#id3)

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
| **description**  string | Description of the tag to manage. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **hosts**  list / elements=string | List of the hosts names, which should have assigned this tag. |
| **id**  string | ID of the tag to manage. |
| **name**  string / required | Name of the tag to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **parent**  string | Name of the parent tag. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **state**  string | Should the tag be present/absent/attached/detached.  `Note`: *attached* and *detached* states are supported since version 2.4.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"attached"` - `"detached"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **vms**  list / elements=string | List of the VMs names, which should have assigned this tag. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_tag_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_tag_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create(if not exists) and assign tag to vms vm1 and vm2:
- ovirt.ovirt.ovirt_tag:
    name: mytag
    vms:
      - vm1
      - vm2

# Attach a tag to VM 'vm3', keeping the rest already attached tags on VM:
- ovirt.ovirt.ovirt_tag:
    name: mytag
    state: attached
    vms:
      - vm3

# Detach a tag from VM 'vm3', keeping the rest already attached tags on VM:
- ovirt.ovirt.ovirt_tag:
    name: mytag
    state: detached
    vms:
      - vm3

# To detach all VMs from tag:
- ovirt.ovirt.ovirt_tag:
    name: mytag
    vms: []

# Remove tag
- ovirt.ovirt.ovirt_tag:
    state: absent
    name: mytag

# Change Tag Name
- ovirt.ovirt.ovirt_tag:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_tag_name"
```

## [Return Values](ovirt_tag_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the tag which is managed  **Returned:** On success if tag is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **tag**  dictionary | Dictionary of all the tag attributes. Tag attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/tag>.  **Returned:** On success if tag is found. |

### Authors

- Ondra Machacek (@machacekondra)
- Martin Necas (@mnecas)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
