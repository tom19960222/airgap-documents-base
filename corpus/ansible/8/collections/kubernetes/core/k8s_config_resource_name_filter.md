---
collection: ansible
version: "8"
title: "kubernetes.core.k8s_config_resource_name filter – Generate resource name for the given resource of type ConfigMap, Secret"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/k8s_config_resource_name_filter.html
fetched_at: 2026-07-28T02:40:19+00:00
---
# kubernetes.core.k8s_config_resource_name filter – Generate resource name for the given resource of type ConfigMap, Secret

> **Note:**
>
> This filter plugin is part of the [kubernetes.core collection](https://galaxy.ansible.com/ui/repo/published/kubernetes/core/) (version 2.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_config_resource_name`.

- [Synopsis](k8s_config_resource_name_filter.md#synopsis)
- [Input](k8s_config_resource_name_filter.md#input)
- [Examples](k8s_config_resource_name_filter.md#examples)
- [Return Value](k8s_config_resource_name_filter.md#return-value)

## [Synopsis](k8s_config_resource_name_filter.md#id1)

- Generate resource name for the given resource of type ConfigMap, Secret.
- Resource must have a `metadata.name` key to generate a resource name

## [Input](k8s_config_resource_name_filter.md#id2)

This describes the input of the filter, the value before `| kubernetes.core.k8s_config_resource_name`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | A valid YAML definition for a ConfigMap or a Secret. |

## [Examples](k8s_config_resource_name_filter.md#id3)

```yaml+jinja
# Dump generated name for a configmap into a variable
- set_fact:
    generated_name: '{{ definition | kubernetes.core.k8s_config_resource_name }}'
  vars:
    definition:
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: myconfigmap
        namespace: mynamespace
```

## [Return Value](k8s_config_resource_name_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | Generated resource name.  **Returned:** success |

### Authors

- ansible cloud team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
