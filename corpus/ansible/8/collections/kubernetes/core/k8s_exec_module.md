---
collection: ansible
version: "8"
title: "kubernetes.core.k8s_exec module – Execute command in Pod"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/k8s_exec_module.html
fetched_at: 2026-07-28T02:40:12+00:00
---
# kubernetes.core.k8s_exec module – Execute command in Pod

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
> see [Requirements](k8s_exec_module.md#ansible-collections-kubernetes-core-k8s-exec-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_exec`.

New in kubernetes.core 0.10.0

- [Synopsis](k8s_exec_module.md#synopsis)
- [Requirements](k8s_exec_module.md#requirements)
- [Parameters](k8s_exec_module.md#parameters)
- [Notes](k8s_exec_module.md#notes)
- [Examples](k8s_exec_module.md#examples)
- [Return Values](k8s_exec_module.md#return-values)

## [Synopsis](k8s_exec_module.md#id1)

- Use the Kubernetes Python client to execute command on K8s pods.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_exec_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](k8s_exec_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **command**  string / required | The command to execute. |
| **container**  string | The name of the container in the pod to connect to.  Defaults to only container if there is only one container in the pod.  If not specified, will choose the first container from the given pod as kubectl cmdline does. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  *added in kubernetes.core 2.3.0* | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  *added in kubernetes.core 2.3.0* | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  Multiple Kubernetes config file can be provided using separator ‘;’ for Windows platform or ‘:’ for others platforms.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **namespace**  string / required | The pod namespace name. |
| **no_proxy**  string  *added in kubernetes.core 2.3.0* | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  **Choices:**   - `false` - `true` |
| **pod**  string / required | The pod name. |
| **proxy**  string | The URL of an HTTP proxy to use for the connection.  Can also be specified via *K8S_AUTH_PROXY* environment variable.  Please note that this module does not pick up typical proxy settings from the environment (for example, HTTP_PROXY). |
| **proxy_headers**  dictionary  *added in kubernetes.core 2.0.0* | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight=proxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  **Choices:**   - `false` - `true` |

## [Notes](k8s_exec_module.md#id4)

> **Note:**
>
> - Return code `rc` for the command executed is added in output in version 2.2.0, and deprecates return code `return_code`.
> - Return code `return_code` for the command executed is added in output in version 1.0.0.
> - The authenticated user must have at least read access to the pods resource and write access to the pods/exec resource.
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_exec_module.md#id5)

```yaml+jinja
- name: Execute a command
  kubernetes.core.k8s_exec:
    namespace: myproject
    pod: zuul-scheduler
    command: zuul-scheduler full-reconfigure

- name: Check RC status of command executed
  kubernetes.core.k8s_exec:
    namespace: myproject
    pod: busybox-test
    command: cmd_with_non_zero_exit_code
  register: command_status
  ignore_errors: True

- name: Check last command status
  debug:
    msg: "cmd failed"
  when: command_status.rc != 0

- name: Specify a container name to execute the command on
  kubernetes.core.k8s_exec:
    namespace: myproject
    pod: busybox-test
    container: manager
    command: echo "hello"
```

## [Return Values](k8s_exec_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The command object  **Returned:** success |
| **rc**  integer  *added in kubernetes.core 2.2.0* | The command status code  **Returned:** success |
| **return_code**  integer | The command status code. This attribute is deprecated and will be removed in a future release. Please use rc instead.  **Returned:** success |
| **stderr**  string | The command stderr  **Returned:** success |
| **stderr_lines**  string | The command stderr  **Returned:** success |
| **stdout**  string | The command stdout  **Returned:** success |
| **stdout_lines**  string | The command stdout  **Returned:** success |

### Authors

- Tristan de Cacqueray (@tristanC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
