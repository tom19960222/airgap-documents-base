---
collection: ansible
version: "8"
title: "openstack.cloud.routers_info module – Retrieve information about one or more OpenStack routers."
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/routers_info_module.html
fetched_at: 2026-07-28T02:48:38+00:00
---
# openstack.cloud.routers_info module – Retrieve information about one or more OpenStack routers.

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
> see [Requirements](routers_info_module.md#ansible-collections-openstack-cloud-routers-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.routers_info`.

- [Synopsis](routers_info_module.md#synopsis)
- [Requirements](routers_info_module.md#requirements)
- [Parameters](routers_info_module.md#parameters)
- [Notes](routers_info_module.md#notes)
- [Examples](routers_info_module.md#examples)
- [Return Values](routers_info_module.md#return-values)

## [Synopsis](routers_info_module.md#id1)

- Retrieve information about one or more routers from OpenStack.

## [Requirements](routers_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](routers_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **filters**  dictionary | A dictionary of meta data to use for further filtering. Elements of this dictionary may be additional dictionaries.  **Default:** `{}` |
| **description**  string | Filter the list result by the human-readable description of the resource. |
| **is_admin_state_up**  boolean | Filter the list result by the administrative state of the resource, which is up (true) or down (false).  **Choices:**   - `false` - `true` |
| **name**  string | Filter the list result by the human-readable name of the resource. |
| **project_id**  aliases: tenant_id  string | Filter the list result by the ID of the project that owns the resource. |
| **revision_number**  integer | Filter the list result by the revision number of the resource. |
| **tags**  list / elements=string | A list of tags to filter the list result by. Resources that match all tags in this list will be returned. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string | Name or ID of the router |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](routers_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](routers_info_module.md#id5)

```yaml+jinja
- name: Gather information about routers
  openstack.cloud.routers_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
  register: result

- name: Show openstack routers
  debug:
    msg: "{{ result.routers }}"

- name: Gather information about a router by name
  openstack.cloud.routers_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    name: router1
  register: result

- name: Show openstack routers
  debug:
    msg: "{{ result.routers }}"

- name: Gather information about a router with filter
  openstack.cloud.routers_info:
    auth:
      auth_url: https://identity.example.com
      username: user
      password: password
      project_name: someproject
    filters:
      is_admin_state_up: True
  register: result

- name: Show openstack routers
  debug:
    msg: "{{ result.routers }}"

- name: List all routers
  openstack.cloud.routers_info:
     cloud: devstack
  register: routers

- name: List ports of first router
  openstack.cloud.port_info:
    cloud: devstack
    filters:
      device_id: "{{ routers.routers.0.id }}"
  register: ports

- name: Show first router's fixed ips
  debug:
    msg: "{{ ports.ports
        |rejectattr('device_owner', 'equalto', 'network:router_gateway')
        |sum(attribute='fixed_ips', start=[])
        |map(attribute='ip_address')
        |sort|list }}"

- name: List ports of all routers
  loop: "{{ routers.routers }}"
  openstack.cloud.port_info:
    cloud: devstack
    filters:
      device_id: "{{ item['id'] }}"
  register: ports

- name: Transform ports for interfaces_info entries
  loop: "{{ ports.results|map(attribute='ports')|list }}"
  set_fact:
    interfaces_info: |-
        {% for port in item %}
        {% if port.device_owner != "network:router_gateway" %}
        {% for fixed_ip in port['fixed_ips'] %}
        - port_id: {{ port.id }}
          ip_address: {{ fixed_ip.ip_address }}
          subnet_id: {{ fixed_ip.subnet_id }}
        {% endfor %}
        {% endif %}
        {% endfor %}
  register: interfaces

- name: Combine router and interfaces_info entries
  loop: "{{
      routers.routers|zip(interfaces.results|map(attribute='ansible_facts'))|list
  }}"
  set_fact:
    # underscore prefix to prevent overwriting facts outside of loop
    _router: "{{
        item.0|combine({'interfaces_info': item.1.interfaces_info|from_yaml})
    }}"
  register: routers

- name: Remove set_fact artifacts from routers
  set_fact:
    routers: "{{ {
        'routers': routers.results|map(attribute='ansible_facts._router')|list
    } }}"

- debug: var=routers
```

## [Return Values](routers_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **routers**  list / elements=dictionary | has all the openstack information about the routers  **Returned:** always, but can be null |
| **availability_zone_hints**  list / elements=string | Availability zone hints  **Returned:** success |
| **availability_zones**  list / elements=string | Availability zones  **Returned:** success |
| **created_at**  string | Date and time when the router was created  **Returned:** success |
| **description**  string | Description notes of the router  **Returned:** success |
| **external_gateway_info**  dictionary | The external gateway information of the router.  **Returned:** success |
| **flavor_id**  string | ID of the flavor of the router  **Returned:** success |
| **id**  string | Unique UUID.  **Returned:** success |
| **is_admin_state_up**  boolean | Network administrative state  **Returned:** success |
| **is_distributed**  boolean | Indicates a distributed router.  **Returned:** success |
| **is_ha**  boolean | Indicates a highly-available router.  **Returned:** success |
| **name**  string | Name given to the router.  **Returned:** success |
| **project_id**  string | Project id associated with this router.  **Returned:** success |
| **revision_number**  integer | Revision number  **Returned:** success |
| **routes**  list / elements=string | The extra routes configuration for L3 router.  **Returned:** success |
| **status**  string | Router status.  **Returned:** success |
| **tags**  list / elements=string | List of tags  **Returned:** success |
| **tenant_id**  string | Owner tenant ID  **Returned:** success |
| **updated_at**  string | Date of last update on the router  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
