---
collection: ansible
version: "6"
title: "community.docker.docker_stack_info module – Return information on a docker stack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_stack_info_module.html
fetched_at: 2026-07-27T17:07:26+00:00
---
# community.docker.docker_stack_info module – Return information on a docker stack

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
>
> To use it in a playbook, specify: `community.docker.docker_stack_info`.

- [Synopsis](docker_stack_info_module.md#synopsis)
- [Examples](docker_stack_info_module.md#examples)
- [Return Values](docker_stack_info_module.md#return-values)

## [Synopsis](docker_stack_info_module.md#id1)

- Retrieve information on docker stacks using the `docker stack` command on the target node (see examples).

## [Examples](docker_stack_info_module.md#id2)

```yaml+jinja
- name: Shows stack info
  community.docker.docker_stack_info:
  register: result

- name: Show results
  ansible.builtin.debug:
    var: result.results
```

## [Return Values](docker_stack_info_module.md#id3)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  list / elements=dictionary | List of dictionaries containing the list of stacks or tasks associated to a stack name.  Returned: always  Sample: `[{"name": "grafana", "namespace": "default", "orchestrator": "Kubernetes", "services": "2"}]` |

### Authors

- Jose Angel Munoz (@imjoseangel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
