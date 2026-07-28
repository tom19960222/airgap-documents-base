---
collection: ansible
version: "6"
title: "kubernetes.core.k8s_drain module – Drain, Cordon, or Uncordon node in k8s cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/k8s_drain_module.html
fetched_at: 2026-07-27T17:54:53+00:00
---
# kubernetes.core.k8s_drain module – Drain, Cordon, or Uncordon node in k8s cluster

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
> see [Requirements](k8s_drain_module.md#ansible-collections-kubernetes-core-k8s-drain-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_drain`.

New in kubernetes.core 2.2.0

- [Synopsis](k8s_drain_module.md#synopsis)
- [Requirements](k8s_drain_module.md#requirements)
- [Parameters](k8s_drain_module.md#parameters)
- [Notes](k8s_drain_module.md#notes)
- [Examples](k8s_drain_module.md#examples)
- [Return Values](k8s_drain_module.md#return-values)

## [Synopsis](k8s_drain_module.md#id1)

- Drain node in preparation for maintenance same as kubectl drain.
- Cordon will mark the node as unschedulable.
- Uncordon will mark the node as schedulable.
- The given node will be marked unschedulable to prevent new pods from arriving.
- Then drain deletes all pods except mirror pods (which cannot be deleted through the API server).

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_drain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0

## [Parameters](k8s_drain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **delete_options**  dictionary | Specify options to delete pods.  This option has effect only when `state` is set to *drain*. |
| **delete_emptydir_data**  boolean  added in kubernetes.core 2.3.0 | Continue even if there are pods using emptyDir (local data that will be deleted when the node is drained).  Choices:   - `false` ← (default) - `true` |
| **disable_eviction**  boolean | Forces drain to use delete rather than evict.  Choices:   - `false` ← (default) - `true` |
| **force**  boolean | Continue even if there are pods not managed by a ReplicationController, Job, or DaemonSet.  Choices:   - `false` ← (default) - `true` |
| **ignore_daemonsets**  boolean | Ignore DaemonSet-managed pods.  Choices:   - `false` ← (default) - `true` |
| **terminate_grace_period**  integer | Specify how many seconds to wait before forcefully terminating.  If not specified, the default grace period for the object type will be used.  The value zero indicates delete immediately. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  Ignored if `wait_timeout` is not set.  Default: `5` |
| **wait_timeout**  integer | The length of time to wait in seconds for pod to be deleted before giving up, zero means infinite. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **name**  string / required | The name of the node. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **state**  string | Determines whether to drain, cordon, or uncordon node.  Choices:   - `"cordon"` - `"drain"` ← (default) - `"uncordon"` |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](k8s_drain_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_drain_module.md#id5)

```yaml+jinja
- name: Drain node "foo", even if there are pods not managed by a ReplicationController, Job, or DaemonSet on it.
  kubernetes.core.k8s_drain:
    state: drain
    name: foo
    force: yes

- name: Drain node "foo", but abort if there are pods not managed by a ReplicationController, Job, or DaemonSet, and use a grace period of 15 minutes.
  kubernetes.core.k8s_drain:
    state: drain
    name: foo
    delete_options:
        terminate_grace_period: 900

- name: Mark node "foo" as schedulable.
  kubernetes.core.k8s_drain:
    state: uncordon
    name: foo

- name: Mark node "foo" as unschedulable.
  kubernetes.core.k8s_drain:
    state: cordon
    name: foo
```

## [Return Values](k8s_drain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | The node status and the number of pods deleted.  Returned: success |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
