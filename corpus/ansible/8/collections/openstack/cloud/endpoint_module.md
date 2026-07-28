---
collection: ansible
version: "8"
title: "openstack.cloud.endpoint module – Manage OpenStack Identity service endpoints"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/endpoint_module.html
fetched_at: 2026-07-28T02:47:40+00:00
---
# openstack.cloud.endpoint module – Manage OpenStack Identity service endpoints

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
> see [Requirements](endpoint_module.md#ansible-collections-openstack-cloud-endpoint-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.endpoint`.

- [Synopsis](endpoint_module.md#synopsis)
- [Requirements](endpoint_module.md#requirements)
- [Parameters](endpoint_module.md#parameters)
- [Notes](endpoint_module.md#notes)
- [Examples](endpoint_module.md#examples)
- [Return Values](endpoint_module.md#return-values)

## [Synopsis](endpoint_module.md#id1)

- Create, update, or delete OpenStack Identity service endpoints. If a service with the same combination of *service*, *interface* and *region* exist, the *url*, *enabled* and *state* (`present` or `absent`) will be updated.

## [Requirements](endpoint_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](endpoint_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **enabled**  boolean | Is the service enabled.  **Choices:**   - `false` - `true` ← (default) |
| **endpoint_interface**  string / required | Interface of the service.  **Choices:**   - `"admin"` - `"public"` - `"internal"` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **region**  string | ID of the region that the service belongs to. Note that *region* is used for authentication. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **service**  string / required | Name or id of the service. |
| **state**  string | Should the resource be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **url**  string / required | URL of the service. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](endpoint_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](endpoint_module.md#id5)

```yaml+jinja
- name: Create a service for glance
  openstack.cloud.endpoint:
     cloud: mycloud
     service: glance
     endpoint_interface: public
     url: http://controller:9292
     region: RegionOne
     state: present

- name: Delete a service for nova
  openstack.cloud.endpoint:
     cloud: mycloud
     service: nova
     endpoint_interface: public
     region: RegionOne
     state: absent
```

## [Return Values](endpoint_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **endpoint**  dictionary | Dictionary describing the endpoint.  **Returned:** On success when *state* is `present` |
| **id**  string | Endpoint ID.  **Returned:** success  **Sample:** `"3292f020780b4d5baf27ff7e1d224c44"` |
| **interface**  string | Endpoint Interface.  **Returned:** success  **Sample:** `"public"` |
| **is_enabled**  boolean | Service status.  **Returned:** success  **Sample:** `true` |
| **links**  string | Links for the endpoint  **Returned:** success  **Sample:** `"http://controller/identity/v3/endpoints/123"` |
| **name**  string | Name of the endpoint  **Returned:** success  **Sample:** `"cinder"` |
| **region_id**  string | Region ID.  **Returned:** success  **Sample:** `"RegionOne"` |
| **service_id**  string | Service ID.  **Returned:** success  **Sample:** `"b91f1318f735494a825a55388ee118f3"` |
| **url**  string | Service URL.  **Returned:** success  **Sample:** `"http://controller:9292"` |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
