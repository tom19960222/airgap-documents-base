---
collection: ansible
version: "6"
title: "kubernetes.core.kustomize lookup – Build a set of kubernetes resources using a ‘kustomization.yaml’ file."
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/kustomize_lookup.html
fetched_at: 2026-07-27T16:43:31+00:00
---
# kubernetes.core.kustomize lookup – Build a set of kubernetes resources using a ‘kustomization.yaml’ file.

> **Note:**
>
> This lookup plugin is part of the [kubernetes.core collection](https://galaxy.ansible.com/kubernetes/core) (version 2.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](kustomize_lookup.md#ansible-collections-kubernetes-core-kustomize-lookup-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.kustomize`.

New in kubernetes.core 2.2.0

- [Synopsis](kustomize_lookup.md#synopsis)
- [Requirements](kustomize_lookup.md#requirements)
- [Keyword parameters](kustomize_lookup.md#keyword-parameters)
- [Notes](kustomize_lookup.md#notes)
- [Examples](kustomize_lookup.md#examples)
- [Return Value](kustomize_lookup.md#return-value)

## [Synopsis](kustomize_lookup.md#id1)

- Uses the kustomize or the kubectl tool.
- Return the result of `kustomize build` or `kubectl kustomize`.

## [Requirements](kustomize_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6

## [Keyword parameters](kustomize_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('kubernetes.core.kustomize', key1=value1, key2=value2, ...)` and `query('kubernetes.core.kustomize', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **binary_path**  string | The path of a kustomize or kubectl binary to use. |
| **dir**  string | The directory path containing ‘kustomization.yaml’, or a git repository URL with a path suffix specifying same with respect to the repository root.  If omitted, ‘.’ is assumed.  Default: `"."` |
| **opt_dirs**  string | An optional list of directories to search for the executable in addition to PATH. |

## [Notes](kustomize_lookup.md#id4)

> **Note:**
>
> - If both kustomize and kubectl are part of the PATH, kustomize will be used by the plugin.

## [Examples](kustomize_lookup.md#id5)

```yaml+jinja
- name: Run lookup using kustomize
  set_fact:
    resources: "{{ lookup('kubernetes.core.kustomize', binary_path='/path/to/kustomize') }}"

- name: Run lookup using kubectl kustomize
  set_fact:
    resources: "{{ lookup('kubernetes.core.kustomize', binary_path='/path/to/kubectl') }}"

- name: Create kubernetes resources for lookup output
  k8s:
    definition: "{{ lookup('kubernetes.core.kustomize', dir='/path/to/kustomization') }}"
```

## [Return Value](kustomize_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | YAML string for the object definitions returned from the tool execution.  Returned: success  Sample: `"{'apiVersion': 'v1', 'data': {'key1': 'val1'}, 'kind': 'ConfigMap', 'metadata': {'name': 'my-config-map', 'namespace': 'default'}}"` |

### Authors

- Aubin Bikouo (@abikouo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
