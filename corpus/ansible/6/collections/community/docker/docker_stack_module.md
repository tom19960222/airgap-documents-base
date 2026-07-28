---
collection: ansible
version: "6"
title: "community.docker.docker_stack module – docker stack module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_stack_module.html
fetched_at: 2026-07-27T17:07:25+00:00
---
# community.docker.docker_stack module – docker stack module

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this module,
> see [Requirements](docker_stack_module.md#ansible-collections-community-docker-docker-stack-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_stack`.

- [Synopsis](docker_stack_module.md#synopsis)
- [Requirements](docker_stack_module.md#requirements)
- [Parameters](docker_stack_module.md#parameters)
- [Notes](docker_stack_module.md#notes)
- [Examples](docker_stack_module.md#examples)
- [Return Values](docker_stack_module.md#return-values)

## [Synopsis](docker_stack_module.md#id1)

- Manage docker stacks using the `docker stack` command on the target node (see examples).

## [Requirements](docker_stack_module.md#id2)

The below requirements are needed on the host that executes this module.

- jsondiff
- pyyaml

## [Parameters](docker_stack_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **absent_retries**  integer | If `>0` and *state* is `absent` the module will retry up to *absent_retries* times to delete the stack until all the resources have been effectively deleted. If the last try still reports the stack as not completely removed the module will fail.  Default: `0` |
| **absent_retries_interval**  integer | Interval in seconds between consecutive *absent_retries*.  Default: `1` |
| **compose**  list / elements=any | List of compose definitions. Any element may be a string referring to the path of the compose file on the target host or the YAML contents of a compose file nested as dictionary.  Default: `[]` |
| **name**  string / required | Stack name |
| **prune**  boolean | If true will add the `--prune` option to the `docker stack deploy` command. This will have docker remove the services not present in the current stack definition.  Choices:   - `false` ← (default) - `true` |
| **resolve_image**  string | If set will add the `--resolve-image` option to the `docker stack deploy` command. This will have docker query the registry to resolve image digest and supported platforms. If not set, docker use “always” by default.  Choices:   - `"always"` - `"changed"` - `"never"` |
| **state**  string | Service state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **with_registry_auth**  boolean | If true will add the `--with-registry-auth` option to the `docker stack deploy` command. This will have docker send registry authentication details to Swarm agents.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_stack_module.md#id4)

> **Note:**
>
> - Return values *out* and *err* have been deprecated and will be removed in community.docker 3.0.0. Use *stdout* and *stderr* instead.

## [Examples](docker_stack_module.md#id5)

```yaml+jinja
- name: Deploy stack from a compose file
  community.docker.docker_stack:
    state: present
    name: mystack
    compose:
      - /opt/docker-compose.yml

- name: Deploy stack from base compose file and override the web service
  community.docker.docker_stack:
    state: present
    name: mystack
    compose:
      - /opt/docker-compose.yml
      - version: '3'
        services:
          web:
            image: nginx:latest
            environment:
              ENVVAR: envvar

- name: Remove stack
  community.docker.docker_stack:
    name: mystack
    state: absent
```

## [Return Values](docker_stack_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stack_spec_diff**  dictionary | dictionary containing the differences between the ‘Spec’ field of the stack services before and after applying the new stack definition.  Returned: on change  Sample: `"\"stack_spec_diff\": {'test_stack_test_service': {u'TaskTemplate': {u'ContainerSpec': {delete: [u'Env']}}}}\n"` |

### Authors

- Dario Zanzico (@dariko)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
