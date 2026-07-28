---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_user module – Module to manage users in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_user_module.html
fetched_at: 2026-07-28T02:50:07+00:00
---
# ovirt.ovirt.ovirt_user module – Module to manage users in oVirt/RHV

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
> see [Requirements](ovirt_user_module.md#ansible-collections-ovirt-ovirt-ovirt-user-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_user`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_user_module.md#synopsis)
- [Requirements](ovirt_user_module.md#requirements)
- [Parameters](ovirt_user_module.md#parameters)
- [Notes](ovirt_user_module.md#notes)
- [Examples](ovirt_user_module.md#examples)
- [Return Values](ovirt_user_module.md#return-values)

## [Synopsis](ovirt_user_module.md#id1)

- Module to manage users in oVirt/RHV.

## [Requirements](ovirt_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_user_module.md#id3)

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
| **authz_name**  aliases: domain  string / required | Authorization provider of the user. In previous versions of oVirt/RHV known as domain. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the user to manage. In most LDAPs it’s *uid* of the user, but in Active Directory you must specify *UPN* of the user. |
| **namespace**  string | Namespace where the user resides. When using the authorization provider that stores users in the LDAP server, this attribute equals the naming context of the LDAP server. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **ssh_public_key**  string  *added in ovirt.ovirt 1.4.0* | The user public key. |
| **state**  string | Should the user be present/absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_user_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_user_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add user user1 from authorization provider example.com-authz
- ovirt.ovirt.ovirt_user:
    name: user1
    domain: example.com-authz

# Add user user1 from authorization provider example.com-authz
# In case of Active Directory specify UPN:
- ovirt.ovirt.ovirt_user:
    name: user1@ad2.example.com
    domain: example.com-authz

# Remove user user1 with authorization provider example.com-authz
- ovirt.ovirt.ovirt_user:
    state: absent
    name: user1
    authz_name: example.com-authz

# Remove ssh_public_key
- ovirt.ovirt.ovirt_user:
    name: user1
    authz_name: example.com-authz
    ssh_public_key: ""
```

## [Return Values](ovirt_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the user which is managed  **Returned:** On success if user is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **user**  dictionary | Dictionary of all the user attributes. User attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/user>.  **Returned:** On success if user is found. |

### Authors

- Ondra Machacek (@machacekondra)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
