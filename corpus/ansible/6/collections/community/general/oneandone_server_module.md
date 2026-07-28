---
collection: ansible
version: "6"
title: "community.general.oneandone_server module – Create, destroy, start, stop, and reboot a 1&1 Host server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneandone_server_module.html
fetched_at: 2026-07-27T17:11:21+00:00
---
# community.general.oneandone_server module – Create, destroy, start, stop, and reboot a 1&1 Host server

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](oneandone_server_module.md#ansible-collections-community-general-oneandone-server-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneandone_server`.

- [Synopsis](oneandone_server_module.md#synopsis)
- [Requirements](oneandone_server_module.md#requirements)
- [Parameters](oneandone_server_module.md#parameters)
- [Examples](oneandone_server_module.md#examples)
- [Return Values](oneandone_server_module.md#return-values)

## [Synopsis](oneandone_server_module.md#id1)

- Create, destroy, update, start, stop, and reboot a 1&1 Host server. When the server is created it can optionally wait for it to be ‘running’ before returning.

## [Requirements](oneandone_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- 1and1
- python >= 2.6

## [Parameters](oneandone_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_url**  string | Custom API URL. Overrides the ONEANDONE_API_URL environment variable. |
| **appliance**  string | The operating system name or ID for the server. It is required only for ‘present’ state. |
| **auth_token**  string | Authenticating API token provided by 1&1. Overrides the ONEANDONE_AUTH_TOKEN environment variable. |
| **auto_increment**  boolean | When creating multiple servers at once, whether to differentiate hostnames by appending a count after them or substituting the count where there is a %02d or %03d in the hostname string.  Choices:   - `false` - `true` ← (default) |
| **cores_per_processor**  integer | The number of cores per processor. It must be provided with vcore, ram, and hdds parameters. |
| **count**  integer | The number of servers to create.  Default: `1` |
| **datacenter**  string | The datacenter location.  Choices:   - `"US"` ← (default) - `"ES"` - `"DE"` - `"GB"` |
| **description**  string | The description of the server. |
| **firewall_policy**  string | The firewall policy name or ID. |
| **fixed_instance_size**  string | The instance size name or ID of the server. It is required only for ‘present’ state, and it is mutually exclusive with vcore, cores_per_processor, ram, and hdds parameters.  The available choices are: `S`, `M`, `L`, `XL`, `XXL`, `3XL`, `4XL`, `5XL` |
| **hdds**  list / elements=dictionary | A list of hard disks with nested “size” and “is_main” properties. It must be provided with vcore, cores_per_processor, and ram parameters. |
| **hostname**  string | The hostname or ID of the server. Only used when state is ‘present’. |
| **load_balancer**  string | The load balancer name or ID. |
| **monitoring_policy**  string | The monitoring policy name or ID. |
| **private_network**  string | The private network name or ID. |
| **ram**  float | The amount of RAM memory. It must be provided with with vcore, cores_per_processor, and hdds parameters. |
| **server**  string | Server identifier (ID or hostname). It is required for all states except ‘running’ and ‘present’. |
| **server_type**  string | The type of server to be built.  Choices:   - `"cloud"` ← (default) - `"baremetal"` - `"k8s_node"` |
| **ssh_key**  any | User’s public SSH key (contents, not path). |
| **state**  string | Define a server’s state to create, remove, start or stop it.  Choices:   - `"present"` ← (default) - `"absent"` - `"running"` - `"stopped"` |
| **vcore**  integer | The total number of processors. It must be provided with cores_per_processor, ram, and hdds parameters. |
| **wait**  boolean | Wait for the server to be in state ‘running’ before returning. Also used for delete operation (set to ‘false’ if you don’t want to wait for each individual server to be deleted before moving on with other tasks.)  Choices:   - `false` - `true` ← (default) |
| **wait_interval**  integer | Defines the number of seconds to wait when using the wait_for methods  Default: `5` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  Default: `600` |

## [Examples](oneandone_server_module.md#id4)

```yaml+jinja
- name: Create three servers and enumerate their names
  community.general.oneandone_server:
    auth_token: oneandone_private_api_key
    hostname: node%02d
    fixed_instance_size: XL
    datacenter: US
    appliance: C5A349786169F140BCBC335675014C08
    auto_increment: true
    count: 3

- name: Create three servers, passing in an ssh_key
  community.general.oneandone_server:
    auth_token: oneandone_private_api_key
    hostname: node%02d
    vcore: 2
    cores_per_processor: 4
    ram: 8.0
    hdds:
      - size: 50
        is_main: false
    datacenter: ES
    appliance: C5A349786169F140BCBC335675014C08
    count: 3
    wait: true
    wait_timeout: 600
    wait_interval: 10
    ssh_key: SSH_PUBLIC_KEY

- name: Removing server
  community.general.oneandone_server:
    auth_token: oneandone_private_api_key
    state: absent
    server: 'node01'

- name: Starting server
  community.general.oneandone_server:
    auth_token: oneandone_private_api_key
    state: running
    server: 'node01'

- name: Stopping server
  community.general.oneandone_server:
    auth_token: oneandone_private_api_key
    state: stopped
    server: 'node01'
```

## [Return Values](oneandone_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **servers**  list / elements=string | Information about each server that was processed  Returned: always  Sample: `[{"hostname": "my-server", "id": "server-id"}]` |

### Authors

- Amel Ajdinovic (@aajdinov)
- Ethan Devenport (@edevenport)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
