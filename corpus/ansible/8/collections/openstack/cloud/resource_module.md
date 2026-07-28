---
collection: ansible
version: "8"
title: "openstack.cloud.resource module – Manage a OpenStack cloud resource"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/resource_module.html
fetched_at: 2026-07-28T02:48:34+00:00
---
# openstack.cloud.resource module – Manage a OpenStack cloud resource

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
> see [Requirements](resource_module.md#ansible-collections-openstack-cloud-resource-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.resource`.

- [Synopsis](resource_module.md#synopsis)
- [Requirements](resource_module.md#requirements)
- [Parameters](resource_module.md#parameters)
- [Notes](resource_module.md#notes)
- [Examples](resource_module.md#examples)
- [Return Values](resource_module.md#return-values)

## [Synopsis](resource_module.md#id1)

- Create, update and delete a OpenStack cloud resource.

## [Requirements](resource_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](resource_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **attributes**  dictionary / required | Resource attributes which are defined in openstacksdk’s resource classes.  *attributes* is a set of key-value pairs where each key is a attribute name such as `id` and value holds its corresponding attribute value such `ddad2d86-02a6-444d-80ae-1cc2fb023784`.  Define attribute keys `id` or `name` or any set of attribute keys which uniquely identify a resource. This module fails if multiple resources match the given set of attributes.  For a complete list of attributes open any resource class inside openstacksdk such as file `openstack/compute/v2/server.py` in <https://opendev.org/openstack/openstacksdk/> for server attributes. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **non_updateable_attributes**  list / elements=string | List of attribute names which cannot be updated.  When *non_updateable_attributes* is not specified, then all attributes in *attributes* will be compared to an existing resource during updates.  When both *updateable_attributes* and *non_updateable_attributes* are specified, then only attributes which are listed in *updateable_attributes* but not in *non_updateable_attributes* will will be considered during updates. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **service**  string / required | OpenStack service which this resource is part of.  Examples are `block_storage`, `compute` or `network`.  *service* must be a `lowercase` name of a OpenStack service as used in openstacksdk. For a list of available services visit <https://opendev.org/openstack/openstacksdk>: Most subdirectories in the `openstack` directory correspond to a OpenStack service, except `cloud`, `common` and other auxiliary directories. |
| **state**  string | Whether the resource should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **type**  string / required | Typename of the resource.  Examples are `ip`, `network`, `router` or `server`.  *type* must be a `lowercase` name of a openstacksdk resource class. Resource classes are defined in openstacksdk’s service folders. For example, visit <https://opendev.org/openstack/openstacksdk>, change to `openstack` directory, change to any service directory such as `compute`, choose a api version directory such as `v2` and find all available resource classes such as `Server` inside `*.py` files. |
| **updateable_attributes**  list / elements=string | List of attribute names which can be updated.  When *updateable_attributes* is not specified, then all attributes in *attributes* will be compared to an existing resource during updates.  When both *updateable_attributes* and *non_updateable_attributes* are specified, then only attributes which are listed in *updateable_attributes* but not in *non_updateable_attributes* will will be considered during updates. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Whether Ansible should wait until the resource has reached its target *state*.  Only a subset of OpenStack resources report a status. Resources which do not support status processing will block indefinitely if *wait* is set to `true`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](resource_module.md#id4)

> **Note:**
>
> - This module does not support all OpenStack cloud resources. Resource handling must follow openstacksdk’s CRUD structure using and providing `<service>.<type>s`, `<service>.find_<type>`, `<service>.create_<type>`, `<service>.update_<type>` and `<service>.delete_<type>` functions. The module will fail before applying any changes if these functions cannot be found.
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](resource_module.md#id5)

```yaml+jinja
- name: Create external network
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: network
    attributes:
      name: ansible_network_external
      is_router_external: true
    wait: true
  register: network_external

- name: Create external subnet
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: subnet
    attributes:
      cidr: 10.6.6.0/24
      ip_version: 4
      name: ansible_external_subnet
      network_id: "{{ network_external.resource.id }}"
  register: subnet_external

- name: Create external port
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: port
    attributes:
      name: ansible_port_external
      network_id: "{{ network_external.resource.id }}"
      fixed_ips:
        - ip_address: 10.6.6.50
    non_updateable_attributes:
      - fixed_ips

- name: Create internal network
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: network
    attributes:
      name: ansible_network_internal
      is_router_external: false
    wait: true
  register: network_internal

- name: Create internal subnet
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: subnet
    attributes:
      cidr: 10.7.7.0/24
      ip_version: 4
      name: ansible_internal_subnet
      network_id: "{{ network_internal.resource.id }}"
  register: subnet_internal

- name: Create internal port
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: port
    attributes:
      name: ansible_port_internal
      network_id: "{{ network_internal.resource.id }}"
      fixed_ips:
        - ip_address: 10.7.7.100
          subnet_id: "{{ subnet_internal.resource.id }}"
  register: port_internal

- name: Create router
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: router
    attributes:
      name: ansible_router
      external_gateway_info:
        enable_snat: true
        external_fixed_ips:
          - ip_address: 10.6.6.10
            subnet_id: "{{ subnet_external.resource.id }}"
        network_id: "{{ network_external.resource.id }}"
    wait: true

- name: Attach router to internal subnet
  openstack.cloud.router:
    cloud: devstack-admin
    name: ansible_router
    network: "{{ network_external.resource.id }}"
    external_fixed_ips:
      - ip: 10.6.6.10
        subnet: "{{ subnet_external.resource.id }}"
    interfaces:
      - net: "{{ network_internal.resource.id }}"
        subnet: "{{ subnet_internal.resource.id }}"
        portip: 10.7.7.1

- name: Create floating ip address
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: ip
    attributes:
      name: 10.6.6.150
      floating_ip_address: 10.6.6.150
      floating_network_id: "{{ network_external.resource.id }}"
      port_id: "{{ port_internal.resource.id }}"
  register: ip

- name: List images
  openstack.cloud.resources:
    cloud: devstack-admin
    service: image
    type: image
  register: images

- name: Identify CirrOS image id
  set_fact:
    image_id: "{{
      images.resources|community.general.json_query(query)|first }}"
  vars:
    query: "[?starts_with(name, 'cirros')].id"

- name: List compute flavors
  openstack.cloud.resources:
    cloud: devstack-admin
    service: compute
    type: flavor
  register: flavors

- name: Identify m1.tiny flavor id
  set_fact:
    flavor_id: "{{
      flavors.resources|community.general.json_query(query)|first }}"
  vars:
    query: "[?name == 'm1.tiny'].id"

- name: Create server
  openstack.cloud.resource:
    cloud: devstack-admin
    service: compute
    type: server
    attributes:
      name: ansible_server
      image_id: "{{ image_id }}"
      flavor_id: "{{ flavor_id }}"
      networks:
        - uuid: "{{ network_internal.resource.id }}"
          port: "{{ port_internal.resource.id }}"
    non_updateable_attributes:
      - name
      - image_id
      - flavor_id
      - networks
    wait: true

- name: Detach floating ip address
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: ip
    attributes:
      floating_ip_address: 10.6.6.150
      port_id: !!null

- name: Delete server
  openstack.cloud.resource:
    cloud: devstack-admin
    service: compute
    type: server
    attributes:
      name: ansible_server
    state: absent
    wait: true

- name: Delete floating ip address
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: ip
    attributes:
      floating_ip_address: 10.6.6.150
    state: absent

- name: Detach router from internal subnet
  openstack.cloud.router:
    cloud: devstack-admin
    name: ansible_router
    network: "{{ network_external.resource.id }}"
    external_fixed_ips:
      - ip: 10.6.6.10
        subnet: "{{ subnet_external.resource.id }}"
    interfaces: []

- name: Delete router
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: router
    attributes:
      name: ansible_router
    state: absent
    wait: true

- name: Delete internal port
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: port
    attributes:
      name: ansible_port_internal
    state: absent

- name: Delete internal subnet
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: subnet
    attributes:
      name: ansible_internal_subnet
    state: absent

- name: Delete internal network
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: network
    attributes:
      name: ansible_network_internal
    state: absent
    wait: true

- name: Delete external port
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: port
    attributes:
      name: ansible_port_external
    state: absent

- name: Delete external subnet
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: subnet
    attributes:
      name: ansible_external_subnet
    state: absent

- name: Delete external network
  openstack.cloud.resource:
    cloud: devstack-admin
    service: network
    type: network
    attributes:
      name: ansible_network_external
    state: absent
    wait: true
```

## [Return Values](resource_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resource**  dictionary | Dictionary describing the identified (and possibly modified) OpenStack cloud resource.  **Returned:** On success when *state* is `present`. |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
