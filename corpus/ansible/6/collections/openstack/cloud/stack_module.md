---
collection: ansible
version: "6"
title: "openstack.cloud.stack module – Add/Remove Heat Stack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/stack_module.html
fetched_at: 2026-07-28T00:17:10+00:00
---
# openstack.cloud.stack module – Add/Remove Heat Stack

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
> see [Requirements](stack_module.md#ansible-collections-openstack-cloud-stack-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.stack`.

- [Synopsis](stack_module.md#synopsis)
- [Requirements](stack_module.md#requirements)
- [Parameters](stack_module.md#parameters)
- [Notes](stack_module.md#notes)
- [Examples](stack_module.md#examples)
- [Return Values](stack_module.md#return-values)

## [Synopsis](stack_module.md#id1)

- Add or Remove a Stack to an OpenStack Heat

## [Requirements](stack_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](stack_module.md#id3)

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
| **environment**  list / elements=string | List of environment files that should be used for the stack creation |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **name**  string / required | Name of the stack that should be created, name could be char and digit, no space |
| **parameters**  dictionary | Dictionary of parameters for the stack creation |
| **region_name**  string | Name of the region. |
| **rollback**  boolean | Rollback stack creation  Choices:   - `false` ← (default) - `true` |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Indicate desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag**  string | Tag for the stack that should be created, name could be char and digit, no space |
| **template**  string | Path of the template file to use for the stack creation |
| **timeout**  integer | Maximum number of seconds to wait for the stack creation  Default: `3600` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](stack_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](stack_module.md#id5)

```yaml+jinja
---
- name: create stack
  ignore_errors: True
  register: stack_create
  openstack.cloud.stack:
    name: "{{ stack_name }}"
    tag: "{{ tag_name }}"
    state: present
    template: "/path/to/my_stack.yaml"
    environment:
    - /path/to/resource-registry.yaml
    - /path/to/environment.yaml
    parameters:
        bmc_flavor: m1.medium
        bmc_image: CentOS
        key_name: default
        private_net: "{{ private_net_param }}"
        node_count: 2
        name: undercloud
        image: CentOS
        my_flavor: m1.large
        external_net: "{{ external_net_param }}"
```

## [Return Values](stack_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Stack ID.  Returned: always  Sample: `"97a3f543-8136-4570-920e-fd7605c989d6"` |
| **stack**  complex | stack info  Returned: always |
| **action**  string | Action, could be Create or Update.  Returned: success  Sample: `"CREATE"` |
| **creation_time**  string | Time when the action has been made.  Returned: success  Sample: `"2016-07-05T17:38:12Z"` |
| **description**  string | Description of the Stack provided in the heat template.  Returned: success  Sample: `"HOT template to create a new instance and networks"` |
| **id**  string | Stack ID.  Returned: success  Sample: `"97a3f543-8136-4570-920e-fd7605c989d6"` |
| **identifier**  string | Identifier of the current Stack action.  Returned: success  Sample: `"test-stack/97a3f543-8136-4570-920e-fd7605c989d6"` |
| **links**  list / elements=dictionary | Links to the current Stack.  Returned: success  Sample: `"[{'href': 'http://foo:8004/v1/7f6a/stacks/test-stack/97a3f543-8136-4570-920e-fd7605c989d6']"` |
| **name**  string | Name of the Stack  Returned: success  Sample: `"test-stack"` |
| **outputs**  list / elements=dictionary | Output returned by the Stack.  Returned: success  Sample: `"{'description': 'IP address of server1 in private network', 'output_key': 'server1_private_ip', 'output_value': '10.1.10.103'}"` |
| **parameters**  dictionary | Parameters of the current Stack  Returned: success  Sample: `"{'OS::project_id': '7f6a3a3e01164a4eb4eecb2ab7742101', 'OS::stack_id': '97a3f543-8136-4570-920e-fd7605c989d6', 'OS::stack_name': 'test-stack', 'stack_status': 'CREATE_COMPLETE', 'stack_status_reason': 'Stack CREATE completed successfully', 'status': 'COMPLETE', 'template_description': 'HOT template to create a new instance and networks', 'timeout_mins': 60, 'updated_time': null}"` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
