---
collection: ansible
version: "6"
title: "kubernetes.core.kubectl connection – Execute tasks in pods running on Kubernetes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/kubectl_connection.html
fetched_at: 2026-07-27T17:54:59+00:00
---
# kubernetes.core.kubectl connection – Execute tasks in pods running on Kubernetes.

> **Note:**
>
> This connection plugin is part of the [kubernetes.core collection](https://galaxy.ansible.com/kubernetes/core) (version 2.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.kubectl`.

- [Synopsis](kubectl_connection.md#synopsis)
- [Requirements](kubectl_connection.md#requirements)
- [Parameters](kubectl_connection.md#parameters)

## [Synopsis](kubectl_connection.md#id1)

- Use the kubectl exec command to run tasks in, or put/fetch files to, pods running on the Kubernetes container platform.

## [Requirements](kubectl_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- kubectl (go binary)

## [Parameters](kubectl_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: kubectl_ssl_ca_cert  string | Path to a CA certificate used to authenticate with the API.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_SSL_CA_CERT`](../../environment_variables.md#envvar-K8S_AUTH_SSL_CA_CERT) - Variable: ansible_kubectl_ssl_ca_cert - Variable: ansible_kubectl_ca_cert |
| **client_cert**  aliases: kubectl_cert_file  string | Path to a certificate used to authenticate with the API.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_CERT_FILE`](../../environment_variables.md#envvar-K8S_AUTH_CERT_FILE) - Variable: ansible_kubectl_cert_file - Variable: ansible_kubectl_client_cert |
| **client_key**  aliases: kubectl_key_file  string | Path to a key file used to authenticate with the API.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_KEY_FILE`](../../environment_variables.md#envvar-K8S_AUTH_KEY_FILE) - Variable: ansible_kubectl_key_file - Variable: ansible_kubectl_client_key |
| **kubectl_container**  string | Container name.  Required when a pod contains more than one container.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_CONTAINER`](../../environment_variables.md#envvar-K8S_AUTH_CONTAINER) - Variable: ansible_kubectl_container |
| **kubectl_context**  string | The name of a context found in the K8s config file.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_CONTEXT`](../../environment_variables.md#envvar-K8S_AUTH_CONTEXT) - Variable: ansible_kubectl_context |
| **kubectl_extra_args**  string | Extra arguments to pass to the kubectl command line.  Please be aware that this passes information directly on the command line and it could expose sensitive data.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_EXTRA_ARGS`](../../environment_variables.md#envvar-K8S_AUTH_EXTRA_ARGS) - Variable: ansible_kubectl_extra_args |
| **kubectl_host**  string | URL for accessing the API.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_HOST`](../../environment_variables.md#envvar-K8S_AUTH_HOST) - Environment variable: [`K8S_AUTH_SERVER`](../../environment_variables.md#envvar-K8S_AUTH_SERVER) - Variable: ansible_kubectl_host - Variable: ansible_kubectl_server |
| **kubectl_kubeconfig**  string | Path to a kubectl config file. Defaults to *~/.kube/config*  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_KUBECONFIG`](../../environment_variables.md#envvar-K8S_AUTH_KUBECONFIG) - Variable: ansible_kubectl_kubeconfig - Variable: ansible_kubectl_config |
| **kubectl_namespace**  string | The namespace of the pod  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_NAMESPACE`](../../environment_variables.md#envvar-K8S_AUTH_NAMESPACE) - Variable: ansible_kubectl_namespace |
| **kubectl_password**  string | Provide a password for authenticating with the API.  Please be aware that this passes information directly on the command line and it could expose sensitive data. We recommend using the file based authentication options instead.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_PASSWORD`](../../environment_variables.md#envvar-K8S_AUTH_PASSWORD) - Variable: ansible_kubectl_password |
| **kubectl_pod**  string | Pod name.  Required when the host name does not match pod name.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_POD`](../../environment_variables.md#envvar-K8S_AUTH_POD) - Variable: ansible_kubectl_pod |
| **kubectl_token**  string | API authentication bearer token.  Please be aware that this passes information directly on the command line and it could expose sensitive data. We recommend using the file based authentication options instead.  Configuration:   - Environment variable: [`K8S_AUTH_TOKEN`](../../environment_variables.md#envvar-K8S_AUTH_TOKEN) - Environment variable: [`K8S_AUTH_API_KEY`](../../environment_variables.md#envvar-K8S_AUTH_API_KEY) - Variable: ansible_kubectl_token - Variable: ansible_kubectl_api_key |
| **kubectl_username**  string | Provide a username for authenticating with the API.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_USERNAME`](../../environment_variables.md#envvar-K8S_AUTH_USERNAME) - Variable: ansible_kubectl_username - Variable: ansible_kubectl_user |
| **validate_certs**  aliases: kubectl_verify_ssl  string | Whether or not to verify the API server’s SSL certificate. Defaults to *true*.  Default: `""`  Configuration:   - Environment variable: [`K8S_AUTH_VERIFY_SSL`](../../environment_variables.md#envvar-K8S_AUTH_VERIFY_SSL) - Variable: ansible_kubectl_verify_ssl - Variable: ansible_kubectl_validate_certs |

### Authors

- xuxinkun (@xuxinkun)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
