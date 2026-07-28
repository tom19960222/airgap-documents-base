---
collection: ansible
version: "8"
title: "kubernetes.core.k8s_service module – Manage Services on Kubernetes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/k8s_service_module.html
fetched_at: 2026-07-28T02:40:16+00:00
---
# kubernetes.core.k8s_service module – Manage Services on Kubernetes

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
> see [Requirements](k8s_service_module.md#ansible-collections-kubernetes-core-k8s-service-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_service`.

- [Synopsis](k8s_service_module.md#synopsis)
- [Requirements](k8s_service_module.md#requirements)
- [Parameters](k8s_service_module.md#parameters)
- [Notes](k8s_service_module.md#notes)
- [Examples](k8s_service_module.md#examples)
- [Return Values](k8s_service_module.md#return-values)

## [Synopsis](k8s_service_module.md#id1)

- Use Kubernetes Python SDK to manage Services on Kubernetes

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0

## [Parameters](k8s_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **apply**  boolean | `apply` compares the desired resource definition with the previously supplied resource definition, ignoring properties that are automatically generated  `apply` works better with Services than ‘force=yes’  mutually exclusive with `merge_type`  **Choices:**   - `false` ← (default) - `true` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **force**  boolean | If set to `yes`, and *state* is `present`, an existing object will be replaced.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  *added in kubernetes.core 2.3.0* | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  *added in kubernetes.core 2.3.0* | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  Multiple Kubernetes config file can be provided using separator ‘;’ for Windows platform or ‘:’ for others platforms.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **merge_type**  list / elements=string | Whether to override the default patch merge approach with a specific type. By default, the strategic merge will typically be used.  For example, Custom Resource Definitions typically aren’t updatable by the usual strategic merge. You may want to use `merge` if you see “strategic merge patch format is not supported”  See <https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/#use-a-json-merge-patch-to-update-a-deployment>  If more than one `merge_type` is given, the merge_types will be tried in order  This defaults to `['strategic-merge', 'merge']`, which is ideal for using the same parameters on resource kinds that combine Custom Resources and built-in resources.  **Choices:**   - `"json"` - `"merge"` - `"strategic-merge"` |
| **name**  string / required | Use to specify a Service object name. |
| **namespace**  string / required | Use to specify a Service object namespace. |
| **no_proxy**  string  *added in kubernetes.core 2.3.0* | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  **Choices:**   - `false` - `true` |
| **ports**  list / elements=dictionary | A list of ports to expose.  <https://kubernetes.io/docs/concepts/services-networking/service/#multi-port-services> |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  *added in kubernetes.core 2.0.0* | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight=proxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **resource_definition**  aliases: definition, inline  string | Provide a valid YAML definition (either as a string, list, or dict) for an object when creating or updating.  NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the provided *resource_definition*. |
| **selector**  dictionary | Label selectors identify objects this Service should apply to.  <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/> |
| **src**  path | Provide a path to a file containing a valid YAML definition of an object or objects to be created or updated. Mutually exclusive with *resource_definition*. NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the configuration read in from the *src* file.  Reads from the local file system. To read from the Ansible controller’s file system, including vaulted files, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to *resource_definition*. See Examples below.  The URL to manifest files that can be used to create the resource. Added in version 2.4.0.  Mutually exclusive with *template* in case of [kubernetes.core.k8s](k8s_module.md#ansible-collections-kubernetes-core-k8s-module) module. |
| **state**  string | Determines if an object should be created, patched, or deleted. When set to `present`, an object will be created, if it does not already exist. If set to `absent`, an existing object will be deleted. If set to `present`, an existing object will be patched, if its attributes differ from those specified using *resource_definition* or *src*.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string | Specifies the type of Service to create.  See <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>  **Choices:**   - `"NodePort"` - `"ClusterIP"` - `"LoadBalancer"` - `"ExternalName"` |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  **Choices:**   - `false` - `true` |

## [Notes](k8s_service_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_service_module.md#id5)

```yaml+jinja
- name: Expose https port with ClusterIP
  kubernetes.core.k8s_service:
    state: present
    name: test-https
    namespace: default
    ports:
    - port: 443
      protocol: TCP
    selector:
      key: special

- name: Expose https port with ClusterIP using spec
  kubernetes.core.k8s_service:
    state: present
    name: test-https
    namespace: default
    inline:
      spec:
        ports:
        - port: 443
          protocol: TCP
        selector:
          key: special
```

## [Return Values](k8s_service_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The created, patched, or otherwise present Service object. Will be empty in the case of a deletion.  **Returned:** success |
| **api_version**  string | The versioned schema of this representation of an object.  **Returned:** success |
| **kind**  string | Always ‘Service’.  **Returned:** success |
| **metadata**  complex | Standard object metadata. Includes name, namespace, annotations, labels, etc.  **Returned:** success |
| **spec**  complex | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  **Returned:** success |
| **status**  complex | Current status details for the object.  **Returned:** success |

### Authors

- KubeVirt Team (@kubevirt)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
