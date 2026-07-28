---
collection: ansible
version: "6"
title: "kubernetes.core.helm_info module – Get information from Helm package deployed inside the cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/helm_info_module.html
fetched_at: 2026-07-27T17:54:47+00:00
---
# kubernetes.core.helm_info module – Get information from Helm package deployed inside the cluster

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
> see [Requirements](helm_info_module.md#ansible-collections-kubernetes-core-helm-info-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.helm_info`.

New in kubernetes.core 0.11.0

- [Synopsis](helm_info_module.md#synopsis)
- [Requirements](helm_info_module.md#requirements)
- [Parameters](helm_info_module.md#parameters)
- [Examples](helm_info_module.md#examples)
- [Return Values](helm_info_module.md#return-values)

## [Synopsis](helm_info_module.md#id1)

- Get information (values, states, …) from Helm package deployed inside the cluster.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](helm_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- helm (<https://github.com/helm/helm/releases>)
- yaml (<https://pypi.org/project/PyYAML/>)

## [Parameters](helm_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string  added in kubernetes.core 1.2.0 | Token used to authenticate with the API. Can also be specified via `K8S_AUTH_API_KEY` environment variable. |
| **binary_path**  path | The path of a helm binary to use. |
| **ca_cert**  aliases: ssl_ca_cert  path  added in kubernetes.core 1.2.0 | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via `K8S_AUTH_SSL_CA_CERT` environment variable. |
| **context**  aliases: kube_context  string | Helm option to specify which kubeconfig context to use.  If the value is not specified in the task, the value of environment variable `K8S_AUTH_CONTEXT` will be used instead. |
| **host**  string  added in kubernetes.core 1.2.0 | Provide a URL for accessing the API. Can also be specified via `K8S_AUTH_HOST` environment variable. |
| **kubeconfig**  aliases: kubeconfig_path  path | Helm option to specify kubeconfig path to use.  If the value is not specified in the task, the value of environment variable `K8S_AUTH_KUBECONFIG` will be used instead. |
| **release_name**  aliases: name  string / required | Release name to manage. |
| **release_namespace**  aliases: namespace  string / required | Kubernetes namespace where the chart should be installed. |
| **release_state**  list / elements=string  added in kubernetes.core 2.3.0 | Show releases as per their states.  Default value is `deployed` and `failed`.  If set to `all`, show all releases without any filter applied.  If set to `deployed`, show deployed releases.  If set to `failed`, show failed releases.  If set to `pending`, show pending releases.  If set to `superseded`, show superseded releases.  If set to `uninstalled`, show uninstalled releases, if `helm uninstall --keep-history` was used.  If set to `uninstalling`, show releases that are currently being uninstalled. |
| **validate_certs**  aliases: verify_ssl  boolean  added in kubernetes.core 1.2.0 | Whether or not to verify the API server’s SSL certificates. Can also be specified via `K8S_AUTH_VERIFY_SSL` environment variable.  Choices:   - `false` - `true` ← (default) |

## [Examples](helm_info_module.md#id4)

```yaml+jinja
- name: Gather information of Grafana chart inside monitoring namespace
  kubernetes.core.helm_info:
    name: test
    release_namespace: monitoring

- name: Gather information about test-chart with pending state
  kubernetes.core.helm_info:
    name: test-chart
    release_namespace: testenv
    release_state:
    - pending
```

## [Return Values](helm_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **status**  complex | A dictionary of status output  Returned: only when release exists |
| **app_version**  string | Version of app deployed  Returned: always |
| **chart**  string | Chart name and chart version  Returned: always |
| **name**  string | Name of the release  Returned: always |
| **namespace**  string | Namespace where the release is deployed  Returned: always |
| **revision**  string | Number of time where the release has been updated  Returned: always |
| **status**  string | Status of release (can be DEPLOYED, FAILED, …)  Returned: always |
| **updated**  string | The Date of last update  Returned: always |
| **values**  string | Dict of Values used to deploy  Returned: always |

### Authors

- Lucas Boisserie (@LucasBoisserie)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
