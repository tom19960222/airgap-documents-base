---
collection: ansible
version: "6"
title: "kubernetes.core.k8s_scale module – Set a new size for a Deployment, ReplicaSet, Replication Controller, or Job."
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/k8s_scale_module.html
fetched_at: 2026-07-27T17:54:57+00:00
---
# kubernetes.core.k8s_scale module – Set a new size for a Deployment, ReplicaSet, Replication Controller, or Job.

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
> see [Requirements](k8s_scale_module.md#ansible-collections-kubernetes-core-k8s-scale-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s_scale`.

- [Synopsis](k8s_scale_module.md#synopsis)
- [Requirements](k8s_scale_module.md#requirements)
- [Parameters](k8s_scale_module.md#parameters)
- [Notes](k8s_scale_module.md#notes)
- [Examples](k8s_scale_module.md#examples)
- [Return Values](k8s_scale_module.md#return-values)

## [Synopsis](k8s_scale_module.md#id1)

- Similar to the kubectl scale command. Use to set the number of replicas for a Deployment, ReplicaSet, or Replication Controller, or the parallelism attribute of a Job. Supports check mode.
- `wait` parameter is not supported for Jobs.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_scale_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](k8s_scale_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **api_version**  aliases: api, version  string | Use to specify the API version.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *kind*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *apiVersion* value from the *resource_definition* will override this option.  Default: `"v1"` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **continue_on_error**  boolean  added in kubernetes.core 2.0.0 | Whether to continue on errors when multiple resources are defined.  Choices:   - `false` ← (default) - `true` |
| **current_replicas**  integer | For Deployment, ReplicaSet, Replication Controller, only scale, if the number of existing replicas matches. In the case of a Job, update parallelism only if the current parallelism value matches. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kind**  string | Use to specify an object model.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *api_version*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *kind* value from the *resource_definition* will override this option. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **label_selectors**  list / elements=string  added in kubernetes.core 2.0.0 | List of label selectors to use to filter results. |
| **name**  string | Use to specify an object name.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *api_version*, *kind* and *namespace* to identify a specific object.  If *resource definition* is provided, the *metadata.name* value from the *resource_definition* will override this option. |
| **namespace**  string | Use to specify an object namespace.  Useful when creating, deleting, or discovering an object without providing a full resource definition.  Use in conjunction with *api_version*, *kind*, and *name* to identify a specific object.  If *resource definition* is provided, the *metadata.namespace* value from the *resource_definition* will override this option. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **replicas**  integer / required | The desired number of replicas. |
| **resource_definition**  aliases: definition, inline  string | Provide a valid YAML definition (either as a string, list, or dict) for an object when creating or updating.  NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the provided *resource_definition*. |
| **resource_version**  string | Only attempt to scale, if the current object version matches. |
| **src**  path | Provide a path to a file containing a valid YAML definition of an object or objects to be created or updated. Mutually exclusive with *resource_definition*. NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the configuration read in from the *src* file.  Reads from the local file system. To read from the Ansible controller’s file system, including vaulted files, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to *resource_definition*. See Examples below.  Mutually exclusive with *template* in case of [kubernetes.core.k8s](k8s_module.md#ansible-collections-kubernetes-core-k8s-module) module. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](../../community/okd/k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **wait**  boolean | For Deployment, ReplicaSet, Replication Controller, wait for the status value of *ready_replicas* to change to the number of *replicas*. In the case of a Job, this option is ignored.  Choices:   - `false` - `true` ← (default) |
| **wait_sleep**  integer  added in kubernetes.core 2.0.0 | Number of seconds to sleep between checks.  Default: `5` |
| **wait_timeout**  integer | When `wait` is *True*, the number of seconds to wait for the *ready_replicas* status to equal *replicas*. If the status is not reached within the allotted time, an error will result. In the case of a Job, this option is ignored.  Default: `20` |

## [Notes](k8s_scale_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_scale_module.md#id5)

```yaml+jinja
- name: Scale deployment up, and extend timeout
  kubernetes.core.k8s_scale:
    api_version: v1
    kind: Deployment
    name: elastic
    namespace: myproject
    replicas: 3
    wait_timeout: 60

- name: Scale deployment down when current replicas match
  kubernetes.core.k8s_scale:
    api_version: v1
    kind: Deployment
    name: elastic
    namespace: myproject
    current_replicas: 3
    replicas: 2

- name: Increase job parallelism
  kubernetes.core.k8s_scale:
    api_version: batch/v1
    kind: job
    name: pi-with-timeout
    namespace: testing
    replicas: 2

# Match object using local file or inline definition

- name: Scale deployment based on a file from the local filesystem
  kubernetes.core.k8s_scale:
    src: /myproject/elastic_deployment.yml
    replicas: 3
    wait: no

- name: Scale deployment based on a template output
  kubernetes.core.k8s_scale:
    resource_definition: "{{ lookup('template', '/myproject/elastic_deployment.yml') | from_yaml }}"
    replicas: 3
    wait: no

- name: Scale deployment based on a file from the Ansible controller filesystem
  kubernetes.core.k8s_scale:
    resource_definition: "{{ lookup('file', '/myproject/elastic_deployment.yml') | from_yaml }}"
    replicas: 3
    wait: no

- name: Scale deployment using label selectors (continue operation in case error occured on one resource)
  kubernetes.core.k8s_scale:
    replicas: 3
    kind: Deployment
    namespace: test
    label_selectors:
      - app=test
    continue_on_error: true
```

## [Return Values](k8s_scale_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | If a change was made, will return the patched object, otherwise returns the existing object.  Returned: success |
| **api_version**  string | The versioned schema of this representation of an object.  Returned: success |
| **duration**  integer | elapsed time of task in seconds  Returned: when `wait` is true  Sample: `48` |
| **kind**  string | Represents the REST resource this object represents.  Returned: success |
| **metadata**  complex | Standard object metadata. Includes name, namespace, annotations, labels, etc.  Returned: success |
| **spec**  complex | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  Returned: success |
| **status**  complex | Current status details for the object.  Returned: success |

### Authors

- Chris Houseknecht (@chouseknecht)
- Fabian von Feilitzsch (@fabianvf)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
