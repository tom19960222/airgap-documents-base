---
collection: ansible
version: "6"
title: "kubernetes.core.helm_repository module – Manage Helm repositories."
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/helm_repository_module.html
fetched_at: 2026-07-27T17:54:49+00:00
---
# kubernetes.core.helm_repository module – Manage Helm repositories.

> **Note:**
>
> This module is part of the [kubernetes.core collection](https://galaxy.ansible.com/kubernetes/core) (version 2.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
> You need further requirements to be able to use this module,
> see [Requirements](helm_repository_module.md#ansible-collections-kubernetes-core-helm-repository-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.helm_repository`.

New in kubernetes.core 0.11.0

- [Synopsis](helm_repository_module.md#synopsis)
- [Requirements](helm_repository_module.md#requirements)
- [Parameters](helm_repository_module.md#parameters)
- [Examples](helm_repository_module.md#examples)
- [Return Values](helm_repository_module.md#return-values)

## [Synopsis](helm_repository_module.md#id1)

- Manage Helm repositories.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](helm_repository_module.md#id2)

The below requirements are needed on the host that executes this module.

- helm (<https://github.com/helm/helm/releases>)
- yaml (<https://pypi.org/project/PyYAML/>)

## [Parameters](helm_repository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string  added in kubernetes.core 2.3.0 | Token used to authenticate with the API. Can also be specified via `K8S_AUTH_API_KEY` environment variable. |
| **binary_path**  path | The path of a helm binary to use. |
| **ca_cert**  aliases: ssl_ca_cert  path  added in kubernetes.core 2.3.0 | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via `K8S_AUTH_SSL_CA_CERT` environment variable. |
| **host**  string  added in kubernetes.core 2.3.0 | Provide a URL for accessing the API. Can also be specified via `K8S_AUTH_HOST` environment variable. |
| **pass_credentials**  boolean  added in kubernetes.core 2.3.0 | Pass credentials to all domains.  Choices:   - `false` ← (default) - `true` |
| **repo_name**  aliases: name  string / required | Chart repository name. |
| **repo_password**  aliases: password  string | Chart repository password for repository with basic auth.  Required if chart_repo_username is specified. |
| **repo_state**  aliases: state  string | Desired state of repository.  Choices:   - `"present"` ← (default) - `"absent"` |
| **repo_url**  aliases: url  string | Chart repository url |
| **repo_username**  aliases: username  string | Chart repository username for repository with basic auth.  Required if chart_repo_password is specified. |
| **validate_certs**  aliases: verify_ssl  boolean  added in kubernetes.core 2.3.0 | Whether or not to verify the API server’s SSL certificates. Can also be specified via `K8S_AUTH_VERIFY_SSL` environment variable.  Choices:   - `false` - `true` ← (default) |

## [Examples](helm_repository_module.md#id4)

```yaml+jinja
- name: Add a repository
  kubernetes.core.helm_repository:
    name: stable
    repo_url: https://kubernetes.github.io/ingress-nginx

- name: Add Red Hat Helm charts repository
  kubernetes.core.helm_repository:
    name: redhat-charts
    repo_url: https://redhat-developer.github.com/redhat-helm-charts
```

## [Return Values](helm_repository_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `helm` command built by this module, in case you want to re-run the command outside the module or debug a problem.  Returned: always  Sample: `"/usr/local/bin/helm repo add bitnami https://charts.bitnami.com/bitnami"` |
| **msg**  string | Error message returned by `helm` command  Returned: on failure  Sample: `"Repository already have a repository named bitnami"` |
| **stderr**  string | Full `helm` command stderr, in case you want to display it or examine the event log  Returned: always  Sample: `""` |
| **stderr_lines**  list / elements=string | Full `helm` command stderr in list, in case you want to display it or examine the event log  Returned: always  Sample: `[""]` |
| **stdout**  string | Full `helm` command stdout, in case you want to display it or examine the event log  Returned: always  Sample: `"\"bitnami\" has been added to your repositories"` |
| **stdout_lines**  list / elements=string | Full `helm` command stdout in list, in case you want to display it or examine the event log  Returned: always  Sample: `["\"bitnami\" has been added to your repositories"]` |

### Authors

- Lucas Boisserie (@LucasBoisserie)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
