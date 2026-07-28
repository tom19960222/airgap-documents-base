---
collection: ansible
version: "8"
title: "kubernetes.core.helm_plugin module – Manage Helm plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/helm_plugin_module.html
fetched_at: 2026-07-28T02:40:05+00:00
---
# kubernetes.core.helm_plugin module – Manage Helm plugins

> **Note:**
>
> This module is part of the [kubernetes.core collection](https://galaxy.ansible.com/ui/repo/published/kubernetes/core/) (version 2.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
> You need further requirements to be able to use this module,
> see [Requirements](helm_plugin_module.md#ansible-collections-kubernetes-core-helm-plugin-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.helm_plugin`.

New in kubernetes.core 1.0.0

- [Synopsis](helm_plugin_module.md#synopsis)
- [Requirements](helm_plugin_module.md#requirements)
- [Parameters](helm_plugin_module.md#parameters)
- [Examples](helm_plugin_module.md#examples)
- [Return Values](helm_plugin_module.md#return-values)

## [Synopsis](helm_plugin_module.md#id1)

- Manages Helm plugins.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](helm_plugin_module.md#id2)

The below requirements are needed on the host that executes this module.

- helm (<https://github.com/helm/helm/releases>)

## [Parameters](helm_plugin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string  *added in kubernetes.core 1.2.0* | Token used to authenticate with the API. Can also be specified via `K8S_AUTH_API_KEY` environment variable. |
| **binary_path**  path | The path of a helm binary to use. |
| **ca_cert**  aliases: ssl_ca_cert  path  *added in kubernetes.core 1.2.0* | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via `K8S_AUTH_SSL_CA_CERT` environment variable. |
| **context**  aliases: kube_context  string | Helm option to specify which kubeconfig context to use.  If the value is not specified in the task, the value of environment variable `K8S_AUTH_CONTEXT` will be used instead. |
| **host**  string  *added in kubernetes.core 1.2.0* | Provide a URL for accessing the API. Can also be specified via `K8S_AUTH_HOST` environment variable. |
| **kubeconfig**  aliases: kubeconfig_path  any | Helm option to specify kubeconfig path to use.  If the value is not specified in the task, the value of environment variable `K8S_AUTH_KUBECONFIG` will be used instead.  The configuration can be provided as dictionary. Added in version 2.4.0. |
| **plugin_name**  string | Name of Helm plugin.  Required only if `state=absent` or `state=latest`. |
| **plugin_path**  string | Plugin path to a plugin on your local file system or a url of a remote VCS repo.  If plugin path from file system is provided, make sure that tar is present on remote machine and not on Ansible controller.  Required only if `state=present`. |
| **plugin_version**  string  *added in kubernetes.core 2.3.0* | Plugin version to install. If this is not specified, the latest version is installed.  Ignored when `state=absent` or `state=latest`. |
| **state**  string | If `state=present` the Helm plugin will be installed.  If `state=latest` the Helm plugin will be updated. Added in version 2.3.0.  If `state=absent` the Helm plugin will be removed.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"latest"` |
| **validate_certs**  aliases: verify_ssl  boolean  *added in kubernetes.core 1.2.0* | Whether or not to verify the API server’s SSL certificates. Can also be specified via `K8S_AUTH_VERIFY_SSL` environment variable.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](helm_plugin_module.md#id4)

```yaml+jinja
- name: Install Helm env plugin
  kubernetes.core.helm_plugin:
    plugin_path: https://github.com/adamreese/helm-env
    state: present

- name: Install Helm plugin from local filesystem
  kubernetes.core.helm_plugin:
    plugin_path: https://domain/path/to/plugin.tar.gz
    state: present

- name: Remove Helm env plugin
  kubernetes.core.helm_plugin:
    plugin_name: env
    state: absent

- name: Install Helm plugin with a specific version
  kubernetes.core.helm_plugin:
    plugin_version: 2.0.1
    plugin_path: https://domain/path/to/plugin.tar.gz
    state: present

- name: Update Helm plugin
  kubernetes.core.helm_plugin:
    plugin_name: secrets
    state: latest
```

## [Return Values](helm_plugin_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `helm` command built by this module, in case you want to re-run the command outside the module or debug a problem.  **Returned:** always  **Sample:** `"helm plugin list ..."` |
| **msg**  string | Info about successful command  **Returned:** always  **Sample:** `"Plugin installed successfully"` |
| **rc**  integer | Helm plugin command return code  **Returned:** always  **Sample:** `1` |
| **stderr**  string | Full `helm` command stderr, in case you want to display it or examine the event log  **Returned:** always  **Sample:** `""` |
| **stdout**  string | Full `helm` command stdout, in case you want to display it or examine the event log  **Returned:** always  **Sample:** `""` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
