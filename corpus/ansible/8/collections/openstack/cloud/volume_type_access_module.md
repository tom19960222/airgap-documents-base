---
collection: ansible
version: "8"
title: "openstack.cloud.volume_type_access module – Manage access to OpenStack block-storage volume type"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/volume_type_access_module.html
fetched_at: 2026-07-28T02:49:07+00:00
---
# openstack.cloud.volume_type_access module – Manage access to OpenStack block-storage volume type

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
> see [Requirements](volume_type_access_module.md#ansible-collections-openstack-cloud-volume-type-access-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.volume_type_access`.

- [Synopsis](volume_type_access_module.md#synopsis)
- [Requirements](volume_type_access_module.md#requirements)
- [Parameters](volume_type_access_module.md#parameters)
- [Notes](volume_type_access_module.md#notes)
- [Examples](volume_type_access_module.md#examples)
- [Return Values](volume_type_access_module.md#return-values)

## [Synopsis](volume_type_access_module.md#id1)

- Add or remove access to OpenStack block-storage volume type

## [Requirements](volume_type_access_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](volume_type_access_module.md#id3)

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
| **name**  string / required | Name or ID of the block-storage volume type. |
| **project**  string / required | ID or Name of project to grant.  Allow *project* to access private volume type (name or ID). |
| **project_domain**  string | Domain the project belongs to (name or ID).  This can be used in case collisions between project names exist. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate whether project should have access to volume type or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](volume_type_access_module.md#id4)

> **Note:**
>
> - A volume type must not be private to manage project access.
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](volume_type_access_module.md#id5)

```yaml+jinja
- name: Grant access to volume type vol-type-001
  openstack.cloud.volume_type_access:
    cloud: devstack
    name: vol-type-001
    project: demo
    state: present

- name: Revoke access to volume type
  openstack.cloud.volume_type_access:
    cloud: devstack
    name: vol-type-001
    project: demo
    state: absent
```

## [Return Values](volume_type_access_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volume_type**  dictionary | Dictionary describing the volume type.  **Returned:** success |
| **description**  string | Description of the type.  **Returned:** success |
| **extra_specs**  dictionary | A dict of extra specifications. “capabilities” is a usual key.  **Returned:** success |
| **id**  string | Volume type ID.  **Returned:** success |
| **is_public**  boolean | Volume type is accessible to the public.  **Returned:** success |
| **name**  string | Volume type name.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
