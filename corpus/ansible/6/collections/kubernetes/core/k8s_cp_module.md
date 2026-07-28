---
collection: ansible
version: "6"
title: "kubernetes.core.k8s_cp module – Copy files and directories to and from pod."
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/k8s_cp_module.html
fetched_at: 2026-07-27T17:54:52+00:00
---
# kubernetes.core.k8s_cp module – Copy files and directories to and from pod.

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
> see [Requirements](k8s_cp_module.md#ansible-collections-kubernetes-core-k8s-cp-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_cp`.

New in kubernetes.core 2.2.0

- [Synopsis](k8s_cp_module.md#synopsis)
- [Requirements](k8s_cp_module.md#requirements)
- [Parameters](k8s_cp_module.md#parameters)
- [Notes](k8s_cp_module.md#notes)
- [Examples](k8s_cp_module.md#examples)
- [Return Values](k8s_cp_module.md#return-values)

## [Synopsis](k8s_cp_module.md#id1)

- Use the Kubernetes Python client to copy files and directories to and from containers inside a pod.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_cp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0

## [Parameters](k8s_cp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **container**  string | The name of the container in the pod to copy files/directories from/to.  Defaults to the only container if there is only one container in the pod. |
| **content**  string | When used instead of *local_path*, sets the contents of a local file directly to the specified value.  Works only when *remote_path* is a file. Creates the file if it does not exist.  For advanced formatting or if the content contains a variable, use the [ansible.builtin.template](../../ansible/builtin/template_module.md#ansible-collections-ansible-builtin-template-module) module.  Mutually exclusive with *local_path*. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **local_path**  path | Path of the local file or directory.  Required when *state* is set to `from_pod`.  Mutually exclusive with *content*. |
| **namespace**  string / required | The pod namespace name. |
| **no_preserve**  boolean | The copied file/directory’s ownership and permissions will not be preserved in the container.  This option is ignored when *content* is set or when *state* is set to `from_pod`.  Choices:   - `false` ← (default) - `true` |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **pod**  string / required | The pod name. |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **remote_path**  path / required | Path of the file or directory to copy. |
| **state**  string | When set to `to_pod`, the local *local_path* file or directory will be copied to *remote_path* into the pod.  When set to `from_pod`, the remote file or directory *remote_path* from pod will be copied locally to *local_path*.  Choices:   - `"to_pod"` ← (default) - `"from_pod"` |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](k8s_cp_module.md#id4)

> **Note:**
>
> - the tar binary is required on the container when copying from local filesystem to pod.
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_cp_module.md#id5)

```yaml+jinja
# kubectl cp /tmp/foo some-namespace/some-pod:/tmp/bar
- name: Copy /tmp/foo local file to /tmp/bar in a remote pod
  kubernetes.core.k8s_cp:
    namespace: some-namespace
    pod: some-pod
    remote_path: /tmp/bar
    local_path: /tmp/foo

# kubectl cp /tmp/foo_dir some-namespace/some-pod:/tmp/bar_dir
- name: Copy /tmp/foo_dir local directory to /tmp/bar_dir in a remote pod
  kubernetes.core.k8s_cp:
    namespace: some-namespace
    pod: some-pod
    remote_path: /tmp/bar_dir
    local_path: /tmp/foo_dir

# kubectl cp /tmp/foo some-namespace/some-pod:/tmp/bar -c some-container
- name: Copy /tmp/foo local file to /tmp/bar in a remote pod in a specific container
  kubernetes.core.k8s_cp:
    namespace: some-namespace
    pod: some-pod
    container: some-container
    remote_path: /tmp/bar
    local_path: /tmp/foo
    no_preserve: True
    state: to_pod

# kubectl cp some-namespace/some-pod:/tmp/foo /tmp/bar
- name: Copy /tmp/foo from a remote pod to /tmp/bar locally
  kubernetes.core.k8s_cp:
    namespace: some-namespace
    pod: some-pod
    remote_path: /tmp/foo
    local_path: /tmp/bar
    state: from_pod

# copy content into a file in the remote pod
- name: Copy /tmp/foo from a remote pod to /tmp/bar locally
  kubernetes.core.k8s_cp:
    state: to_pod
    namespace: some-namespace
    pod: some-pod
    remote_path: /tmp/foo.txt
    content: "This content will be copied into remote file"
```

## [Return Values](k8s_cp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | message describing the copy operation successfully done.  Returned: success |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
