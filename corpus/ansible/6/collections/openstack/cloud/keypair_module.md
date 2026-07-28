---
collection: ansible
version: "6"
title: "openstack.cloud.keypair module – Add/Delete a keypair from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/keypair_module.html
fetched_at: 2026-07-28T00:16:45+00:00
---
# openstack.cloud.keypair module – Add/Delete a keypair from OpenStack

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](keypair_module.md#ansible-collections-openstack-cloud-keypair-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.keypair`.

- [Synopsis](keypair_module.md#synopsis)
- [Requirements](keypair_module.md#requirements)
- [Parameters](keypair_module.md#parameters)
- [Notes](keypair_module.md#notes)
- [Examples](keypair_module.md#examples)
- [Return Values](keypair_module.md#return-values)

## [Synopsis](keypair_module.md#id1)

- Add or Remove key pair from OpenStack

## [Requirements](keypair_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](keypair_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Name that has to be given to the key pair |
| **public_key**  string | The public key that would be uploaded to nova and injected into VMs upon creation. |
| **public_key_file**  string | Path to local file containing ssh public key. Mutually exclusive with public_key. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent. If state is replace and the key exists but has different content, delete it and recreate it with the new content.  Choices:   - `"present"` ← (default) - `"absent"` - `"replace"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](keypair_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](keypair_module.md#id5)

```yaml+jinja
# Creates a key pair with the running users public key
- openstack.cloud.keypair:
      cloud: mordred
      state: present
      name: ansible_key
      public_key_file: /home/me/.ssh/id_rsa.pub

# Creates a new key pair and the private key returned after the run.
- openstack.cloud.keypair:
      cloud: rax-dfw
      state: present
      name: ansible_key
```

## [Return Values](keypair_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Unique UUID.  Returned: success |
| **name**  string | Name given to the keypair.  Returned: success |
| **private_key**  string | The private key value for the keypair.  Returned: Only when a keypair is generated for the user (e.g., when creating one and a public key is not specified). |
| **public_key**  string | The public key value for the keypair.  Returned: success |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
