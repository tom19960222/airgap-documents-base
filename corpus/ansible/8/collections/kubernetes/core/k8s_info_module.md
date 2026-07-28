---
collection: ansible
version: "8"
title: "kubernetes.core.k8s_info module – Describe Kubernetes (K8s) objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/k8s_info_module.html
fetched_at: 2026-07-28T02:40:13+00:00
---
# kubernetes.core.k8s_info module – Describe Kubernetes (K8s) objects

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
> see [Requirements](k8s_info_module.md#ansible-collections-kubernetes-core-k8s-info-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_info`.

- [Synopsis](k8s_info_module.md#synopsis)
- [Requirements](k8s_info_module.md#requirements)
- [Parameters](k8s_info_module.md#parameters)
- [Notes](k8s_info_module.md#notes)
- [Examples](k8s_info_module.md#examples)
- [Return Values](k8s_info_module.md#return-values)

## [Synopsis](k8s_info_module.md#id1)

- Use the Kubernetes Python client to perform read operations on K8s objects.
- Access to the full range of K8s APIs.
- Authenticate using either a config file, certificates, password or token.
- Supports check mode.
- This module was called `k8s_facts` before Ansible 2.9. The usage did not change.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](k8s_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **api_version**  aliases: api, version  string | Use to specify the API version.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *kind*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *apiVersion* value from the *resource_definition* will override this option.  **Default:** `"v1"` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **field_selectors**  list / elements=string | List of field selectors to use to filter results |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  *added in kubernetes.core 2.3.0* | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  *added in kubernetes.core 2.3.0* | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kind**  string / required | Use to specify an object model.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *api_version*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *kind* value from the *resource_definition* will override this option. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  Multiple Kubernetes config file can be provided using separator ‘;’ for Windows platform or ‘:’ for others platforms.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **label_selectors**  list / elements=string | List of label selectors to use to filter results |
| **name**  string | Use to specify an object name.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *api_version*, *kind* and *namespace* to identify a specific object.  If *resource definition* is provided, the *metadata.name* value from the *resource_definition* will override this option. |
| **namespace**  string | Use to specify an object namespace.  Useful when creating, deleting, or discovering an object without providing a full resource definition.  Use in conjunction with *api_version*, *kind*, and *name* to identify a specific object.  If *resource definition* is provided, the *metadata.namespace* value from the *resource_definition* will override this option. |
| **no_proxy**  string  *added in kubernetes.core 2.3.0* | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  **Choices:**   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  *added in kubernetes.core 2.0.0* | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight=proxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Whether to wait for certain resource kinds to end up in the desired state.  By default the module exits once Kubernetes has received the request.  Implemented for `state=present` for `Deployment`, `DaemonSet` and `Pod`, and for `state=absent` for all resource kinds.  For resource kinds without an implementation, `wait` returns immediately unless `wait_condition` is set.  **Choices:**   - `false` ← (default) - `true` |
| **wait_condition**  dictionary | Specifies a custom condition on the status to wait for.  Ignored if `wait` is not set or is set to False. |
| **reason**  string | The value of the reason field in your desired condition  For example, if a `Deployment` is paused, The `Progressing` `type` will have the `DeploymentPaused` reason.  The possible reasons in a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **status**  string | The value of the status field in your desired condition.  For example, if a `Deployment` is paused, the `Progressing` `type` will have the `Unknown` status.  **Choices:**   - `"True"` ← (default) - `"False"` - `"Unknown"` |
| **type**  string | The type of condition to wait for.  For example, the `Pod` resource will set the `Ready` condition (among others).  Required if you are specifying a `wait_condition`.  If left empty, the `wait_condition` field will be ignored.  The possible types for a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  **Default:** `5` |
| **wait_timeout**  integer | How long in seconds to wait for the resource to end up in the desired state.  Ignored if `wait` is not set.  **Default:** `120` |

## [Notes](k8s_info_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_info_module.md#id5)

```yaml+jinja
- name: Get an existing Service object
  kubernetes.core.k8s_info:
    api_version: v1
    kind: Service
    name: web
    namespace: testing
  register: web_service

- name: Get a list of all service objects
  kubernetes.core.k8s_info:
    api_version: v1
    kind: Service
    namespace: testing
  register: service_list

- name: Get a list of all pods from any namespace
  kubernetes.core.k8s_info:
    kind: Pod
  register: pod_list

- name: Search for all Pods labelled app=web
  kubernetes.core.k8s_info:
    kind: Pod
    label_selectors:
      - app = web
      - tier in (dev, test)

- name: Using vars while using label_selectors
  kubernetes.core.k8s_info:
    kind: Pod
    label_selectors:
      - "app = {{ app_label_web }}"
  vars:
    app_label_web: web

- name: Search for all running pods
  kubernetes.core.k8s_info:
    kind: Pod
    field_selectors:
      - status.phase=Running

- name: List custom objects created using CRD
  kubernetes.core.k8s_info:
    kind: MyCustomObject
    api_version: "stable.example.com/v1"

- name: Wait till the Object is created
  kubernetes.core.k8s_info:
    kind: Pod
    wait: yes
    name: pod-not-yet-created
    namespace: default
    wait_sleep: 10
    wait_timeout: 360
```

## [Return Values](k8s_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_found**  boolean | Whether the specified api_version and kind were successfully mapped to an existing API on the targeted cluster.  Version added 1.2.0.  **Returned:** always |
| **resources**  complex | The object(s) that exists  **Returned:** success |
| **api_version**  string | The versioned schema of this representation of an object.  **Returned:** success |
| **kind**  string | Represents the REST resource this object represents.  **Returned:** success |
| **metadata**  dictionary | Standard object metadata. Includes name, namespace, annotations, labels, etc.  **Returned:** success |
| **spec**  dictionary | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  **Returned:** success |
| **status**  dictionary | Current status details for the object.  **Returned:** success |

### Authors

- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
