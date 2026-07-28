---
collection: ansible
version: "8"
title: "openstack.cloud.federation_idp module – Manage an identity provider in a OpenStack cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/federation_idp_module.html
fetched_at: 2026-07-28T02:47:41+00:00
---
# openstack.cloud.federation_idp module – Manage an identity provider in a OpenStack cloud

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
> see [Requirements](federation_idp_module.md#ansible-collections-openstack-cloud-federation-idp-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.federation_idp`.

- [Synopsis](federation_idp_module.md#synopsis)
- [Requirements](federation_idp_module.md#requirements)
- [Parameters](federation_idp_module.md#parameters)
- [Notes](federation_idp_module.md#notes)
- [Examples](federation_idp_module.md#examples)
- [Return Values](federation_idp_module.md#return-values)

## [Synopsis](federation_idp_module.md#id1)

- Create, update or delete an identity provider of the OpenStack identity (Keystone) service.

## [Requirements](federation_idp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](federation_idp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **description**  string | The description of the identity provider. |
| **domain_id**  string | The ID of a domain that is associated with the identity provider.  Federated users that authenticate with the identity provider will be created under the domain specified.  Required when creating a new identity provider. |
| **id**  aliases: name  string / required | The ID (and name) of the identity provider. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_enabled**  aliases: enabled  boolean | Whether the identity provider is enabled or not.  Will default to `false` when creating a new identity provider.  **Choices:**   - `false` - `true` |
| **region_name**  string | Name of the region. |
| **remote_ids**  list / elements=string | List of the unique identity provider’s remote IDs.  Will default to an empty list when creating a new identity provider. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Whether the identity provider should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](federation_idp_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](federation_idp_module.md#id5)

```yaml+jinja
- name: Create an identity provider
  openstack.cloud.federation_idp:
    cloud: example_cloud
    name: example_provider
    domain_id: 0123456789abcdef0123456789abcdef
    description: 'My example IDP'
    remote_ids:
      - 'https://auth.example.com/auth/realms/ExampleRealm'

- name: Delete an identity provider
  openstack.cloud.federation_idp:
    cloud: example_cloud
    name: example_provider
    state: absent
```

## [Return Values](federation_idp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **identity_provider**  dictionary | Dictionary describing the identity providers  **Returned:** On success when *state* is `present`. |
| **description**  string | Identity provider description  **Returned:** success  **Sample:** `"demodescription"` |
| **domain_id**  string | Domain to which the identity provider belongs  **Returned:** success  **Sample:** `"default"` |
| **id**  string | Identity provider ID  **Returned:** success  **Sample:** `"test-idp"` |
| **is_enabled**  boolean | Indicates whether the identity provider is enabled  **Returned:** success |
| **name**  string | Name of the identity provider, equals its ID.  **Returned:** success  **Sample:** `"test-idp"` |
| **remote_ids**  list / elements=string | Remote IDs associated with the identity provider  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
