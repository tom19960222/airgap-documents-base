---
collection: ansible
version: "6"
title: "kubernetes.core.k8s_json_patch module – Apply JSON patch operations to existing objects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/k8s_json_patch_module.html
fetched_at: 2026-07-27T17:54:55+00:00
---
# kubernetes.core.k8s_json_patch module – Apply JSON patch operations to existing objects

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
> see [Requirements](k8s_json_patch_module.md#ansible-collections-kubernetes-core-k8s-json-patch-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_json_patch`.

New in kubernetes.core 2.0.0

- [Synopsis](k8s_json_patch_module.md#synopsis)
- [Requirements](k8s_json_patch_module.md#requirements)
- [Parameters](k8s_json_patch_module.md#parameters)
- [Notes](k8s_json_patch_module.md#notes)
- [Examples](k8s_json_patch_module.md#examples)
- [Return Values](k8s_json_patch_module.md#return-values)

## [Synopsis](k8s_json_patch_module.md#id1)

- This module is used to apply RFC 6902 JSON patch operations only.
- Use the [kubernetes.core.k8s](k8s_module.md#ansible-collections-kubernetes-core-k8s-module) module for strategic merge or JSON merge operations.
- The jsonpatch library is required for check mode.

## [Requirements](k8s_json_patch_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11
- jsonpatch

## [Parameters](k8s_json_patch_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **api_version**  aliases: api, version  string | Use to specify the API version.  Use in conjunction with *kind*, *name*, and *namespace* to identify a specific object.  Default: `"v1"` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kind**  string / required | Use to specify an object model.  Use in conjunction with *api_version*, *name*, and *namespace* to identify a specific object. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **name**  string / required | Use to specify an object name.  Use in conjunction with *api_version*, *kind*, and *namespace* to identify a specific object. |
| **namespace**  string | Use to specify an object namespace.  Use in conjunction with *api_version*, *kind*, and *name* to identify a specific object. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **patch**  list / elements=dictionary / required | List of JSON patch operations. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **wait**  boolean | Whether to wait for certain resource kinds to end up in the desired state.  By default the module exits once Kubernetes has received the request.  Implemented for `state=present` for `Deployment`, `DaemonSet` and `Pod`, and for `state=absent` for all resource kinds.  For resource kinds without an implementation, `wait` returns immediately unless `wait_condition` is set.  Choices:   - `false` ← (default) - `true` |
| **wait_condition**  dictionary | Specifies a custom condition on the status to wait for.  Ignored if `wait` is not set or is set to False. |
| **reason**  string | The value of the reason field in your desired condition  For example, if a `Deployment` is paused, The `Progressing` `type` will have the `DeploymentPaused` reason.  The possible reasons in a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **status**  string | The value of the status field in your desired condition.  For example, if a `Deployment` is paused, the `Progressing` `type` will have the `Unknown` status.  Choices:   - `"True"` ← (default) - `"False"` - `"Unknown"` |
| **type**  string | The type of condition to wait for.  For example, the `Pod` resource will set the `Ready` condition (among others).  Required if you are specifying a `wait_condition`.  If left empty, the `wait_condition` field will be ignored.  The possible types for a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  Default: `5` |
| **wait_timeout**  integer | How long in seconds to wait for the resource to end up in the desired state.  Ignored if `wait` is not set.  Default: `120` |

## [Notes](k8s_json_patch_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_json_patch_module.md#id5)

```yaml+jinja
- name: Apply multiple patch operations to an existing Pod
  kubernetes.core.k8s_json_patch:
    kind: Pod
    namespace: testing
    name: mypod
    patch:
      - op: add
        path: /metadata/labels/app
        value: myapp
      - op: replace
        patch: /spec/containers/0/image
        value: nginx
```

## [Return Values](k8s_json_patch_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **duration**  integer | Elapsed time of task in seconds.  Returned: when `wait` is true  Sample: `48` |
| **error**  dictionary | The error when patching the object.  Returned: error  Sample: `{"exception": "Traceback (most recent call last): ...", "msg": "Failed to import the required Python library (jsonpatch) ..."}` |
| **result**  dictionary | The modified object.  Returned: success |
| **api_version**  string | The versioned schema of this representation of an object.  Returned: success |
| **kind**  string | The REST resource this object represents.  Returned: success |
| **metadata**  dictionary | Standard object metadata. Includes name, namespace, annotations, labels, etc.  Returned: success |
| **spec**  dictionary | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  Returned: success |
| **status**  dictionary | Current status details for the object.  Returned: success |

### Authors

- Mike Graves (@gravesm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
