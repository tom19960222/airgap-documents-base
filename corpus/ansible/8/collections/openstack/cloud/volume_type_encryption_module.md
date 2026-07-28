---
collection: ansible
version: "8"
title: "openstack.cloud.volume_type_encryption module – Manage OpenStack volume type encryption"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/volume_type_encryption_module.html
fetched_at: 2026-07-28T02:49:08+00:00
---
# openstack.cloud.volume_type_encryption module – Manage OpenStack volume type encryption

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](volume_type_encryption_module.md#ansible-collections-openstack-cloud-volume-type-encryption-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.volume_type_encryption`.

- [Synopsis](volume_type_encryption_module.md#synopsis)
- [Requirements](volume_type_encryption_module.md#requirements)
- [Parameters](volume_type_encryption_module.md#parameters)
- [Notes](volume_type_encryption_module.md#notes)
- [Examples](volume_type_encryption_module.md#examples)
- [Return Values](volume_type_encryption_module.md#return-values)

## [Synopsis](volume_type_encryption_module.md#id1)

- Add, remove or update volume type encryption in OpenStack.

## [Requirements](volume_type_encryption_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](volume_type_encryption_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **encryption_cipher**  string | encryption algorithm or mode  admin only |
| **encryption_control_location**  string | Set the notional service where the encryption is performed  admin only  **Choices:**   - `"front-end"` - `"back-end"` |
| **encryption_key_size**  integer | Set the size of the encryption key of this volume type  admin only  **Choices:**   - `128` - `256` - `512` |
| **encryption_provider**  string | class that provides encryption support for the volume type  admin only |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource.  When *state* is `present`, then *encryption options* are required.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **volume_type**  string / required | Volume type name or id. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](volume_type_encryption_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](volume_type_encryption_module.md#id5)

```yaml+jinja
- name: Create volume type encryption
  openstack.cloud.volume_type_encryption:
    volume_type: test_type
    state: present
    encryption_provider: nova.volume.encryptors.luks.LuksEncryptor
    encryption_cipher: aes-xts-plain64
    encryption_control_location: front-end
    encryption_key_size: 256

- name: Delete volume type encryption
  openstack.cloud.volume_type_encryption:
    volume_type: test_type
    state: absent
  register: the_result
```

## [Return Values](volume_type_encryption_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **encryption**  dictionary | Dictionary describing volume type encryption  **Returned:** On success when *state* is ‘present’ |
| **cipher**  string | encryption cipher  **Returned:** success  **Sample:** `"aes-xts-plain64"` |
| **control_location**  string | encryption location  **Returned:** success  **Sample:** `"front-end"` |
| **created_at**  string | Resource creation date and time  **Returned:** success  **Sample:** `"2023-08-04T10:23:03.000000"` |
| **deleted**  string | Boolean if the resource was deleted  **Returned:** success  **Sample:** `"false,"` |
| **deleted_at**  string | Resource delete date and time  **Returned:** success  **Sample:** `"null,"` |
| **encryption_id**  string | UUID of the volume type encryption  **Returned:** success  **Sample:** `"b75d8c5c-a6d8-4a5d-8c86-ef4f1298525d"` |
| **id**  string | Alias to encryption_id  **Returned:** success  **Sample:** `"b75d8c5c-a6d8-4a5d-8c86-ef4f1298525d"` |
| **key_size**  string | Size of the key  **Returned:** success  **Sample:** `"256,"` |
| **provider**  string | Encryption provider  **Returned:** success  **Sample:** `"nova.volume.encryptors.luks.LuksEncryptor"` |
| **updated_at**  string | Resource last update date and time  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
