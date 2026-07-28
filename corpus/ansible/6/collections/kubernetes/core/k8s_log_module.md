---
collection: ansible
version: "6"
title: "kubernetes.core.k8s_log module – Fetch logs from Kubernetes resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/k8s_log_module.html
fetched_at: 2026-07-27T17:54:55+00:00
---
# kubernetes.core.k8s_log module – Fetch logs from Kubernetes resources

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
> see [Requirements](k8s_log_module.md#ansible-collections-kubernetes-core-k8s-log-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_log`.

New in kubernetes.core 0.10.0

- [Synopsis](k8s_log_module.md#synopsis)
- [Requirements](k8s_log_module.md#requirements)
- [Parameters](k8s_log_module.md#parameters)
- [Notes](k8s_log_module.md#notes)
- [Examples](k8s_log_module.md#examples)
- [Return Values](k8s_log_module.md#return-values)

## [Synopsis](k8s_log_module.md#id1)

- Use the Kubernetes Python client to perform read operations on K8s log endpoints.
- Authenticate using either a config file, certificates, password or token.
- Supports check mode.
- Analogous to `kubectl logs` or `oc logs`

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_log_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](k8s_log_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **api_version**  aliases: api, version  string | Use to specify the API version.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *kind*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *apiVersion* value from the *resource_definition* will override this option.  Default: `"v1"` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **container**  string | Use to specify the container within a pod to grab the log from.  If there is only one container, this will default to that container.  If there is more than one container, this option is required. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kind**  string | Use to specify an object model.  Use in conjunction with *api_version*, *name*, and *namespace* to identify a specific object.  If using *label_selectors*, cannot be overridden.  Default: `"Pod"` |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **label_selectors**  list / elements=string | List of label selectors to use to filter results  Only one of *name* or *label_selectors* may be provided. |
| **name**  string | Use to specify an object name.  Use in conjunction with *api_version*, *kind* and *namespace* to identify a specific object.  Only one of *name* or *label_selectors* may be provided. |
| **namespace**  string | Use to specify an object namespace.  Useful when creating, deleting, or discovering an object without providing a full resource definition.  Use in conjunction with *api_version*, *kind*, and *name* to identify a specific object.  If *resource definition* is provided, the *metadata.namespace* value from the *resource_definition* will override this option. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **since_seconds**  string  added in kubernetes.core 2.2.0 | A relative time in seconds before the current time from which to show logs. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](k8s_log_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_log_module.md#id5)

```yaml+jinja
- name: Get a log from a Pod
  kubernetes.core.k8s_log:
    name: example-1
    namespace: testing
  register: log

# This will get the log from the first Pod found matching the selector
- name: Log a Pod matching a label selector
  kubernetes.core.k8s_log:
    namespace: testing
    label_selectors:
    - app=example
  register: log

# This will get the log from a single Pod managed by this Deployment
- name: Get a log from a Deployment
  kubernetes.core.k8s_log:
    api_version: apps/v1
    kind: Deployment
    namespace: testing
    name: example
    since_seconds: "4000"
  register: log

# This will get the log from a single Pod managed by this DeploymentConfig
- name: Get a log from a DeploymentConfig
  kubernetes.core.k8s_log:
    api_version: apps.openshift.io/v1
    kind: DeploymentConfig
    namespace: testing
    name: example
  register: log
```

## [Return Values](k8s_log_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **log**  string | The text log of the object  Returned: success |
| **log_lines**  list / elements=string | The log of the object, split on newlines  Returned: success |

### Authors

- Fabian von Feilitzsch (@fabianvf)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
