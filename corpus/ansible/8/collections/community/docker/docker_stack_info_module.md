---
collection: ansible
version: "8"
title: "community.docker.docker_stack_info module – Return information on all docker stacks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_stack_info_module.html
fetched_at: 2026-07-28T01:43:55+00:00
---
# community.docker.docker_stack_info module – Return information on all docker stacks

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/ui/repo/published/community/docker/) (version 3.4.11).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
>
> To use it in a playbook, specify: `community.docker.docker_stack_info`.

- [Synopsis](docker_stack_info_module.md#synopsis)
- [Attributes](docker_stack_info_module.md#attributes)
- [See Also](docker_stack_info_module.md#see-also)
- [Examples](docker_stack_info_module.md#examples)
- [Return Values](docker_stack_info_module.md#return-values)

## [Synopsis](docker_stack_info_module.md#id1)

- Retrieve information on docker stacks using the `docker stack` command on the target node (see examples).

## [Attributes](docker_stack_info_module.md#id2)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](docker_stack_info_module.md#id3)

> **See also:**
>
> [community.docker.docker_stack_task_info](docker_stack_task_info_module.md#ansible-collections-community-docker-docker-stack-task-info-module)
> :   To retrieve detailed information about the services under a specific stack use the [community.docker.docker_stack_task_info](docker_stack_task_info_module.md#ansible-collections-community-docker-docker-stack-task-info-module) module.

## [Examples](docker_stack_info_module.md#id4)

```yaml+jinja
- name: Shows stack info
  community.docker.docker_stack_info:
  register: result

- name: Show results
  ansible.builtin.debug:
    var: result.results
```

## [Return Values](docker_stack_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  list / elements=dictionary | List of dictionaries containing the list of stacks on the target node  **Returned:** always  **Sample:** `[{"name": "grafana", "namespace": "default", "orchestrator": "Kubernetes", "services": "2"}]` |

### Authors

- Jose Angel Munoz (@imjoseangel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
