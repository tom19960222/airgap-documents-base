---
collection: ansible
version: "6"
title: "community.docker.current_container_facts module – Return facts about whether the module runs in a Docker container"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/current_container_facts_module.html
fetched_at: 2026-07-27T17:07:13+00:00
---
# community.docker.current_container_facts module – Return facts about whether the module runs in a Docker container

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
> To use it in a playbook, specify: `community.docker.current_container_facts`.

New in community.docker 1.1.0

- [Synopsis](current_container_facts_module.md#synopsis)
- [Examples](current_container_facts_module.md#examples)
- [Returned Facts](current_container_facts_module.md#returned-facts)

## [Synopsis](current_container_facts_module.md#id1)

- Return facts about whether the module runs in a Docker container.
- This module attempts a best-effort detection. There might be special cases where it does not work; if you encounter one, [please file an issue](https://github.com/ansible-collections/community.docker/issues/new?assignees%3D%26labels%3D%26template%3Dbug_report.md).

## [Examples](current_container_facts_module.md#id2)

```yaml+jinja
- name: Get facts on current container
  community.docker.current_container_facts:

- name: Print information on current container when running in a container
  ansible.builtin.debug:
    msg: "Container ID is {{ ansible_module_container_id }}"
  when: ansible_module_running_in_container
```

## [Returned Facts](current_container_facts_module.md#id3)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_module_container_id**  string | The detected container ID.  Contains an empty string if no container was detected.  Returned: always |
| **ansible_module_container_type**  string | The detected container environment.  Contains an empty string if no container was detected, or a non-empty string identifying the container environment.  `github_actions` is supported since community.docker 2.4.0.  Returned: always  Can only return:   - `""` - `"docker"` - `"azure_pipelines"` - `"github_actions"` |
| **ansible_module_running_in_container**  boolean | Whether the module was able to detect that it runs in a container or not.  Returned: always |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
