---
collection: ansible
version: "8"
title: "community.okd.oc connection – Execute tasks in pods running on OpenShift."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/okd/oc_connection.html
fetched_at: 2026-07-28T01:58:23+00:00
---
# community.okd.oc connection – Execute tasks in pods running on OpenShift.

> **Note:**
>
> This connection plugin is part of the [community.okd collection](https://galaxy.ansible.com/ui/repo/published/community/okd/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.okd`.
> You need further requirements to be able to use this connection plugin,
> see [Requirements](oc_connection.md#ansible-collections-community-okd-oc-connection-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.oc`.

- [Synopsis](oc_connection.md#synopsis)
- [Requirements](oc_connection.md#requirements)
- [Parameters](oc_connection.md#parameters)

## [Synopsis](oc_connection.md#id1)

- Use the oc exec command to run tasks in, or put/fetch files to, pods running on the OpenShift container platform.

## [Requirements](oc_connection.md#id2)

The below requirements are needed on the local controller node that executes this connection.

- oc (go binary)

## [Parameters](oc_connection.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: oc_ssl_ca_cert  string | Path to a CA certificate used to authenticate with the API.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_SSL_CA_CERT`](../../environment_variables.md#envvar-K8S_AUTH_SSL_CA_CERT) - Variable: ansible_oc_ssl_ca_cert - Variable: ansible_oc_ca_cert |
| **client_cert**  aliases: oc_cert_file  string | Path to a certificate used to authenticate with the API.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_CERT_FILE`](../../environment_variables.md#envvar-K8S_AUTH_CERT_FILE) - Variable: ansible_oc_cert_file - Variable: ansible_oc_client_cert |
| **client_key**  aliases: oc_key_file  string | Path to a key file used to authenticate with the API.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_KEY_FILE`](../../environment_variables.md#envvar-K8S_AUTH_KEY_FILE) - Variable: ansible_oc_key_file - Variable: ansible_oc_client_key |
| **oc_container**  string | Container name. Required when a pod contains more than one container.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_CONTAINER`](../../environment_variables.md#envvar-K8S_AUTH_CONTAINER) - Variable: ansible_oc_container |
| **oc_context**  string | The name of a context found in the K8s config file.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_CONTEXT`](../../environment_variables.md#envvar-K8S_AUTH_CONTEXT) - Variable: ansible_oc_context |
| **oc_extra_args**  string | Extra arguments to pass to the oc command line.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_EXTRA_ARGS`](../../environment_variables.md#envvar-K8S_AUTH_EXTRA_ARGS) - Variable: ansible_oc_extra_args |
| **oc_host**  string | URL for accessing the API.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_HOST`](../../environment_variables.md#envvar-K8S_AUTH_HOST) - Environment variable: [`K8S_AUTH_SERVER`](../../environment_variables.md#envvar-K8S_AUTH_SERVER) - Variable: ansible_oc_host - Variable: ansible_oc_server |
| **oc_kubeconfig**  string | Path to a oc config file. Defaults to *~/.kube/config*  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_KUBECONFIG`](../../environment_variables.md#envvar-K8S_AUTH_KUBECONFIG) - Variable: ansible_oc_kubeconfig - Variable: ansible_oc_config |
| **oc_namespace**  string | The namespace of the pod  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_NAMESPACE`](../../environment_variables.md#envvar-K8S_AUTH_NAMESPACE) - Variable: ansible_oc_namespace |
| **oc_pod**  string | Pod name. Required when the host name does not match pod name.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_POD`](../../environment_variables.md#envvar-K8S_AUTH_POD) - Variable: ansible_oc_pod |
| **oc_token**  string | API authentication bearer token.  **Configuration:**   - Environment variable: [`K8S_AUTH_TOKEN`](../../environment_variables.md#envvar-K8S_AUTH_TOKEN) - Environment variable: [`K8S_AUTH_API_KEY`](../../environment_variables.md#envvar-K8S_AUTH_API_KEY) - Variable: ansible_oc_token - Variable: ansible_oc_api_key |
| **validate_certs**  aliases: oc_verify_ssl  string | Whether or not to verify the API server’s SSL certificate. Defaults to *true*.  **Default:** `""`  **Configuration:**   - Environment variable: [`K8S_AUTH_VERIFY_SSL`](../../environment_variables.md#envvar-K8S_AUTH_VERIFY_SSL) - Variable: ansible_oc_verify_ssl - Variable: ansible_oc_validate_certs |

### Authors

- xuxinkun (@xuxinkun)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/openshift/community.okd/issues)
- [Repository (Sources)](https://github.com/openshift/community.okd)
