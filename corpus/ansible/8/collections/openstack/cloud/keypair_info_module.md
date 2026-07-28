---
collection: ansible
version: "8"
title: "openstack.cloud.keypair_info module – Get information about keypairs from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/keypair_info_module.html
fetched_at: 2026-07-28T02:48:04+00:00
---
# openstack.cloud.keypair_info module – Get information about keypairs from OpenStack

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
> see [Requirements](keypair_info_module.md#ansible-collections-openstack-cloud-keypair-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.keypair_info`.

- [Synopsis](keypair_info_module.md#synopsis)
- [Requirements](keypair_info_module.md#requirements)
- [Parameters](keypair_info_module.md#parameters)
- [Notes](keypair_info_module.md#notes)
- [Examples](keypair_info_module.md#examples)
- [Return Values](keypair_info_module.md#return-values)

## [Synopsis](keypair_info_module.md#id1)

- Get information about keypairs that are associated with the account

## [Requirements](keypair_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](keypair_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **limit**  integer | Requests a page size of items.  Returns a number of items up to a limit value. |
| **marker**  string | The last-seen item. |
| **name**  string | Name or ID of the keypair |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **user_id**  string | It allows admin users to operate key-pairs of specified user ID. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](keypair_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](keypair_info_module.md#id5)

```yaml+jinja
- name: Get information about keypairs
  openstack.cloud.keypair_info:
  register: result

- name: Get information about keypairs using optional parameters
  openstack.cloud.keypair_info:
    name: "test"
    user_id: "fed75b36fd7a4078a769178d2b1bd844"
    limit: 10
    marker: "jdksl"
  register: result
```

## [Return Values](keypair_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **keypairs**  list / elements=dictionary | Lists keypairs that are associated with the account.  **Returned:** always |
| **created_at**  string | The date and time when the resource was created.  **Returned:** success  **Sample:** `"2021-01-19T14:52:07.261634"` |
| **fingerprint**  string | The fingerprint for the keypair.  **Returned:** success  **Sample:** `"7e:eb:ab:24:ba:d1:e1:88:ae:9a:fb:66:53:df:d3:bd"` |
| **id**  string | The id identifying the keypair  **Returned:** success  **Sample:** `"keypair-5d935425-31d5-48a7-a0f1-e76e9813f2c3"` |
| **is_deleted**  boolean | A boolean indicates whether this keypair is deleted or not.  **Returned:** success |
| **name**  string | A keypair name which will be used to reference it later.  **Returned:** success  **Sample:** `"keypair-5d935425-31d5-48a7-a0f1-e76e9813f2c3"` |
| **private_key**  string | The private key for the keypair.  **Returned:** success  **Sample:** `"MIICXAIBAAKBgQCqGKukO ... hZj6+H0qtjTkVxwTCpvKe4eCZ0FPq"` |
| **public_key**  string | The keypair public key.  **Returned:** success  **Sample:** `"ssh-rsa AAAAB3NzaC1yc ... 8rPsBUHNLQp Generated-by-Nova"` |
| **type**  string | The type of the keypair.  Allowed values are ssh or x509.  **Returned:** success  **Sample:** `"ssh"` |
| **user_id**  string | It allows admin users to operate key-pairs of specified user ID.  **Returned:** success  **Sample:** `"59b10f2a2138428ea9358e10c7e44444"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
