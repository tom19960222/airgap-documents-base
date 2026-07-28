---
collection: ansible
version: "8"
title: "openstack.cloud.stack_info module – Retrieve information about Heat stacks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/stack_info_module.html
fetched_at: 2026-07-28T02:48:56+00:00
---
# openstack.cloud.stack_info module – Retrieve information about Heat stacks

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
> see [Requirements](stack_info_module.md#ansible-collections-openstack-cloud-stack-info-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.stack_info`.

- [Synopsis](stack_info_module.md#synopsis)
- [Requirements](stack_info_module.md#requirements)
- [Parameters](stack_info_module.md#parameters)
- [Notes](stack_info_module.md#notes)
- [Examples](stack_info_module.md#examples)
- [Return Values](stack_info_module.md#return-values)

## [Synopsis](stack_info_module.md#id1)

- Get information about Heat stack in OpenStack

## [Requirements](stack_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](stack_info_module.md#id3)

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
| **name**  string | Name of the stack. |
| **owner**  aliases: owner_id  string | Name or ID of the parent stack. |
| **project**  aliases: project_id  string | Name or ID of the project. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **status**  string | Status of the stack such as `available` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](stack_info_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](stack_info_module.md#id5)

```yaml+jinja
- name: Fetch all Heat stacks
  openstack.cloud.stack_info:
    cloud: devstack

- name: Fetch a single Heat stack
  openstack.cloud.stack_info:
    cloud: devstack
    name: my_stack
```

## [Return Values](stack_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stacks**  list / elements=dictionary | List of dictionaries describing stacks.  **Returned:** always. |
| **added**  list / elements=string | List of resource objects that will be added.  **Returned:** success |
| **capabilities**  list / elements=string | AWS compatible template listing capabilities.  **Returned:** success |
| **created_at**  string | Time when created.  **Returned:** success  **Sample:** `"2016-07-05T17:38:12Z"` |
| **deleted**  list / elements=string | A list of resource objects that will be deleted.  **Returned:** success |
| **deleted_at**  string | Time when the deleted.  **Returned:** success  **Sample:** `"2016-07-05T17:38:12Z"` |
| **description**  string | Description of the Stack provided in the heat template.  **Returned:** success  **Sample:** `"HOT template to create a new instance and networks"` |
| **environment**  dictionary | A JSON environment for the stack.  **Returned:** success |
| **environment_files**  list / elements=string | An ordered list of names for environment files found in the files dict.  **Returned:** success |
| **files**  dictionary | Additional files referenced in the template or the environment  **Returned:** success |
| **files_container**  string | Name of swift container with child templates and files.  **Returned:** success |
| **id**  string | Stack ID.  **Returned:** success  **Sample:** `"97a3f543-8136-4570-920e-fd7605c989d6"` |
| **is_rollback_disabled**  boolean | Whether the stack will support a rollback.  **Returned:** success |
| **links**  list / elements=dictionary | Links to the current Stack.  **Returned:** success  **Sample:** `"[{'href': 'http://foo:8004/v1/7f6a/stacks/test-stack/ 97a3f543-8136-4570-920e-fd7605c989d6']"` |
| **name**  string | Name of the Stack  **Returned:** success  **Sample:** `"test-stack"` |
| **notification_topics**  string | Stack related events.  **Returned:** success  **Sample:** `"HOT template to create a new instance and networks"` |
| **outputs**  list / elements=dictionary | Output returned by the Stack.  **Returned:** success  **Sample:** `"[{'description': 'IP of server1 in private network', 'output_key': 'server1_private_ip', 'output_value': '10.1.10.103'}]"` |
| **owner_id**  string | The ID of the owner stack if any.  **Returned:** success |
| **parameters**  dictionary | Parameters of the current Stack  **Returned:** success  **Sample:** `"{'OS::project_id': '7f6a3a3e01164a4eb4eecb2ab7742101', 'OS::stack_id': '97a3f543-8136-4570-920e-fd7605c989d6', 'OS::stack_name': 'test-stack', 'stack_status': 'CREATE_COMPLETE', 'stack_status_reason': 'Stack CREATE completed successfully', 'status': 'COMPLETE', 'template_description': 'HOT template to create a new instance and nets', 'timeout_mins': 60, 'updated_time': null}"` |
| **parent_id**  string | The ID of the parent stack if any.  **Returned:** success |
| **replaced**  string | A list of resource objects that will be replaced.  **Returned:** success |
| **status**  string | stack status.  **Returned:** success |
| **status_reason**  string | Explaining how the stack transits to its current status.  **Returned:** success |
| **tags**  list / elements=string | A list of strings used as tags on the stack  **Returned:** success |
| **template**  dictionary | A dict containing the template use for stack creation.  **Returned:** success |
| **template_description**  string | Stack template description text.  **Returned:** success |
| **template_url**  string | The URL where a stack template can be found.  **Returned:** success |
| **timeout_mins**  string | Stack operation timeout in minutes.  **Returned:** success |
| **unchanged**  list / elements=string | A list of resource objects that will remain unchanged if a stack.  **Returned:** success |
| **updated**  list / elements=string | A list of resource objects that will have their properties updated.  **Returned:** success |
| **updated_at**  string | Timestamp of last update on the stack.  **Returned:** success |
| **user_project_id**  string | The ID of the user project created for this stack.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
