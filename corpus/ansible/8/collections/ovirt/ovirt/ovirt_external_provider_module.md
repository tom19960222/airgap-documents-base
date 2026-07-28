---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_external_provider module – Module to manage external providers in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_external_provider_module.html
fetched_at: 2026-07-28T02:49:25+00:00
---
# ovirt.ovirt.ovirt_external_provider module – Module to manage external providers in oVirt/RHV

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
> see [Requirements](ovirt_external_provider_module.md#ansible-collections-ovirt-ovirt-ovirt-external-provider-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_external_provider`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_external_provider_module.md#synopsis)
- [Requirements](ovirt_external_provider_module.md#requirements)
- [Parameters](ovirt_external_provider_module.md#parameters)
- [Notes](ovirt_external_provider_module.md#notes)
- [Examples](ovirt_external_provider_module.md#examples)
- [Return Values](ovirt_external_provider_module.md#return-values)

## [Synopsis](ovirt_external_provider_module.md#id2)

- Module to manage external providers in oVirt/RHV

## [Requirements](ovirt_external_provider_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_external_provider_module.md#id4)

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
| **authentication_keys**  aliases: auth_keys  list / elements=dictionary | List of authentication keys.  When you will not pass these keys and there are already some of them defined in the system they will be removed.  Applicable for *os_volume*.  **Default:** `[]` |
| **uuid**  string | The uuid which will be used. |
| **value**  string | The value which will be used. |
| **authentication_url**  aliases: auth_url  string | Keystone authentication URL of the openstack provider.  Applicable for those types: *os_image*, *os_volume* and *network*. |
| **data_center**  string | Name of the data center where provider should be attached.  Applicable for those type: *os_volume*. |
| **description**  string | Description of the external provider. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | Name of the external provider to manage. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **network_type**  string | Type of the external network provider either external (for example OVN) or neutron.  Applicable if `type` is *network*.  **Choices:**   - `"external"` ← (default) - `"neutron"` |
| **password**  string | Password of the user specified in `username` parameter.  Applicable for all types. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **read_only**  boolean | Specify if the network should be read only.  Applicable if `type` is *network*.  **Choices:**   - `false` - `true` |
| **state**  string | Should the external be present or absent  When you are using absent for *os_volume*, you need to make sure that SD is not attached to the data center!  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_name**  aliases: tenant  string | Name of the tenant.  Applicable for those types: *os_image*, *os_volume* and *network*. |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **type**  aliases: provider  string / required | Type of the external provider.  **Choices:**   - `"os_image"` - `"network"` - `"os_volume"` - `"foreman"` |
| **url**  string | URL where external provider is hosted.  Applicable for those types: *os_image*, *os_volume*, *network* and *foreman*. |
| **username**  string | Username to be used for login to external provider.  Applicable for all types. |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ovirt_external_provider_module.md#id5)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_external_provider_module.md#id6)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add image external provider:
- ovirt.ovirt.ovirt_external_provider:
    name: image_provider
    type: os_image
    url: http://1.2.3.4:9292
    username: admin
    password: 123456
    tenant: admin
    auth_url: http://1.2.3.4:35357/v2.0

# Add volume external provider:
- ovirt.ovirt.ovirt_external_provider:
    name: image_provider
    type: os_volume
    url: http://1.2.3.4:9292
    username: admin
    password: 123456
    tenant: admin
    auth_url: http://1.2.3.4:5000/v2.0
    authentication_keys:
      -
        uuid: "1234567-a1234-12a3-a234-123abc45678"
        value: "ABCD00000000111111222333445w=="

# Add foreman provider:
- ovirt.ovirt.ovirt_external_provider:
    name: foreman_provider
    type: foreman
    url: https://foreman.example.com
    username: admin
    password: 123456

# Add external network provider for OVN:
- ovirt.ovirt.ovirt_external_provider:
    name: ovn_provider
    type: network
    network_type: external
    url: http://1.2.3.4:9696

# Remove image external provider:
- ovirt.ovirt.ovirt_external_provider:
    state: absent
    name: image_provider
    type: os_image
```

## [Return Values](ovirt_external_provider_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **external_host_provider**  dictionary | Dictionary of all the external_host_provider attributes. External provider attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/external_host_provider>.  **Returned:** On success and if parameter ‘type: foreman’ is used. |
| **id**  string | ID of the external provider which is managed  **Returned:** On success if external provider is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **openstack_image_provider**  dictionary | Dictionary of all the openstack_image_provider attributes. External provider attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/openstack_image_provider>.  **Returned:** On success and if parameter ‘type: os_image’ is used. |
| **openstack_network_provider**  dictionary | Dictionary of all the openstack_network_provider attributes. External provider attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/openstack_network_provider>.  **Returned:** On success and if parameter ‘type: network’ is used. |
| **openstack_volume_provider**  dictionary | Dictionary of all the openstack_volume_provider attributes. External provider attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/openstack_volume_provider>.  **Returned:** On success and if parameter ‘type: os_volume’ is used. |

### Authors

- Ondra Machacek (@machacekondra)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
