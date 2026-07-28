---
collection: ansible
version: "8"
title: "openstack.cloud.identity_user module – Manage a OpenStack identity (Keystone) user"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/identity_user_module.html
fetched_at: 2026-07-28T02:47:59+00:00
---
# openstack.cloud.identity_user module – Manage a OpenStack identity (Keystone) user

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
> see [Requirements](identity_user_module.md#ansible-collections-openstack-cloud-identity-user-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.identity_user`.

- [Synopsis](identity_user_module.md#synopsis)
- [Requirements](identity_user_module.md#requirements)
- [Parameters](identity_user_module.md#parameters)
- [Notes](identity_user_module.md#notes)
- [Examples](identity_user_module.md#examples)
- [Return Values](identity_user_module.md#return-values)

## [Synopsis](identity_user_module.md#id1)

- Create, update or delete a OpenStack identity (Keystone) user.

## [Requirements](identity_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](identity_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **default_project**  string | Name or ID of the project, the user should be created in. |
| **description**  string | Description about the user. |
| **domain**  string | Domain to create the user in if the cloud supports domains. |
| **email**  string | Email address for the user. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_enabled**  aliases: enabled  boolean | Whether the user is enabled or not.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | Name of the user.  *name* cannot be updated without deleting and re-creating the user. |
| **password**  string | Password for the user. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **update_password**  string | When *update_password* is `always`, then the password will always be updated.  When *update_password* is `on_create`, the the password is only set when creating a user.  **Choices:**   - `"always"` - `"on_create"` ← (default) |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](identity_user_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](identity_user_module.md#id5)

```yaml+jinja
- name: Create a user
  openstack.cloud.identity_user:
    cloud: mycloud
    state: present
    name: demouser
    password: secret
    email: demo@example.com
    domain: default
    default_project: demo

- name: Delete a user
  openstack.cloud.identity_user:
    cloud: mycloud
    state: absent
    name: demouser

- name: Create a user but don't update password if user exists
  openstack.cloud.identity_user:
    cloud: mycloud
    state: present
    name: demouser
    password: secret
    update_password: on_create
    email: demo@example.com
    domain: default
    default_project: demo

- name: Create a user without password
  openstack.cloud.identity_user:
    cloud: mycloud
    state: present
    name: demouser
    email: demo@example.com
    domain: default
    default_project: demo
```

## [Return Values](identity_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  dictionary | Dictionary describing the identity user.  **Returned:** On success when *state* is `present`. |
| **default_project_id**  string | User default project ID. Only present with Keystone >= v3.  **Returned:** success  **Sample:** `"4427115787be45f08f0ec22a03bfc735"` |
| **description**  string | The description of this user  **Returned:** success  **Sample:** `"a user"` |
| **domain_id**  string | User domain ID. Only present with Keystone >= v3.  **Returned:** success  **Sample:** `"default"` |
| **email**  string | User email address  **Returned:** success  **Sample:** `"demo@example.com"` |
| **id**  string | User ID  **Returned:** success  **Sample:** `"f59382db809c43139982ca4189404650"` |
| **is_enabled**  boolean | Indicates whether the user is enabled  **Returned:** success |
| **links**  dictionary | The links for the user resource  **Returned:** success |
| **name**  string | Unique user name, within the owning domain  **Returned:** success  **Sample:** `"demouser"` |
| **password**  string | Credential used during authentication  **Returned:** success |
| **password_expires_at**  string | The date and time when the password expires. The time zone is UTC. A none value means the password never expires  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
