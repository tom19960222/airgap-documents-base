---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_quota_info module – Retrieve information about one or more oVirt/RHV quotas"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_quota_info_module.html
fetched_at: 2026-07-28T02:49:49+00:00
---
# ovirt.ovirt.ovirt_quota_info module – Retrieve information about one or more oVirt/RHV quotas

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
> see [Requirements](ovirt_quota_info_module.md#ansible-collections-ovirt-ovirt-ovirt-quota-info-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_quota_info`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_quota_info_module.md#synopsis)
- [Requirements](ovirt_quota_info_module.md#requirements)
- [Parameters](ovirt_quota_info_module.md#parameters)
- [Notes](ovirt_quota_info_module.md#notes)
- [Examples](ovirt_quota_info_module.md#examples)
- [Return Values](ovirt_quota_info_module.md#return-values)

## [Synopsis](ovirt_quota_info_module.md#id1)

- Retrieve information about one or more oVirt/RHV quotas.
- This module was called `ovirt_quota_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [ovirt.ovirt.ovirt_quota_info](ovirt_quota_info_module.md#ansible-collections-ovirt-ovirt-ovirt-quota-info-module) module no longer returns `ansible_facts`!

## [Requirements](ovirt_quota_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_quota_info_module.md#id3)

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
| **data_center**  string / required | Name of the datacenter where quota resides. |
| **fetch_nested**  boolean | If *yes* the module will fetch additional data from the API.  It will fetch only IDs of nested entity. It doesn’t fetch multiple levels of nested attributes. Only the attributes of the current entity. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  This parameter is deprecated and replaced by `follow`.  **Choices:**   - `false` ← (default) - `true` |
| **follow**  aliases: follows  list / elements=string  *added in ovirt.ovirt 1.5.0* | List of linked entities, which should be fetched along with the main entity.  This parameter replaces usage of `fetch_nested` and `nested_attributes`.  All follow parameters can be found at following url: <https://ovirt.github.io/ovirt-engine-api-model/master/#types/quota/links_summary> |
| **name**  string | Name of the quota, can be used as glob expression. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*.  This parameter is deprecated and replaced by `follow`. |

## [Notes](ovirt_quota_info_module.md#id4)

> **Note:**
>
> - This module returns a variable `ovirt_quotas`, which contains a list of quotas. You need to register the result with the *register* keyword to use it.
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: pip: name=ovirt-engine-sdk-python version=4.4.0

## [Examples](ovirt_quota_info_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Gather information about quota named C<myquota> in Default datacenter:
- ovirt.ovirt.ovirt_quota_info:
    data_center: Default
    name: myquota
  register: result
- ansible.builtin.debug:
    msg: "{{ result.ovirt_quotas }}"
```

## [Return Values](ovirt_quota_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ovirt_quotas**  list / elements=string | List of dictionaries describing the quotas. Quota attributes are mapped to dictionary keys, all quotas attributes can be found at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/quota>.  **Returned:** On success. |

### Authors

- Maor Lipchuk (@machacekondra)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
