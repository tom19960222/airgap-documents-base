---
collection: ansible
version: "6"
title: "community.okd.openshift_process module – Process an OpenShift template.openshift.io/v1 Template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_process_module.html
fetched_at: 2026-07-27T17:20:12+00:00
---
# community.okd.openshift_process module – Process an OpenShift template.openshift.io/v1 Template

> **Note:**
>
> This module is part of the [community.okd collection](https://galaxy.ansible.com/community/okd) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.okd`.
> You need further requirements to be able to use this module,
> see [Requirements](openshift_process_module.md#ansible-collections-community-okd-openshift-process-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_process`.

New in community.okd 0.3.0

- [Synopsis](openshift_process_module.md#synopsis)
- [Requirements](openshift_process_module.md#requirements)
- [Parameters](openshift_process_module.md#parameters)
- [Notes](openshift_process_module.md#notes)
- [Examples](openshift_process_module.md#examples)
- [Return Values](openshift_process_module.md#return-values)

## [Synopsis](openshift_process_module.md#id1)

- Processes a specified OpenShift template with the provided template.
- Templates can be provided inline, from a file, or specified by name and namespace in the cluster.
- Analogous to `oc process`.
- For CRUD operations on Template resources themselves, see the community.okd.k8s module.

## [Requirements](openshift_process_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](openshift_process_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **name**  string | The name of the Template to process.  The Template must be present in the cluster.  When provided, *namespace* is required.  Mutually exclusive with *resource_definition* or *src* |
| **namespace**  string | The namespace that the template can be found in. |
| **namespace_target**  string | The namespace that resources should be created, updated, or deleted in.  Only used when *state* is present or absent. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **parameter_file**  string | A path to a file containing template parameter values to override/set values in the Template.  Corresponds to the `–param-file` argument to oc process. |
| **parameters**  dictionary | A set of key: value pairs that will be used to set/override values in the Template.  Corresponds to the `–param` argument to oc process. |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **resource_definition**  aliases: definition, inline  string | Provide a valid YAML definition (either as a string, list, or dict) for an object when creating or updating.  NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the provided *resource_definition*. |
| **src**  path | Provide a path to a file containing a valid YAML definition of an object or objects to be created or updated. Mutually exclusive with *resource_definition*. NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the configuration read in from the *src* file.  Reads from the local file system. To read from the Ansible controller’s file system, including vaulted files, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to *resource_definition*. See Examples below.  Mutually exclusive with *template* in case of [kubernetes.core.k8s](../../kubernetes/core/k8s_module.md#ansible-collections-kubernetes-core-k8s-module) module. |
| **state**  string | Determines what to do with the rendered Template.  The state *rendered* will render the Template based on the provided parameters, and return the rendered objects in the *resources* field. These can then be referenced in future tasks.  The state *present* will cause the resources in the rendered Template to be created if they do not already exist, and patched if they do.  The state *absent* will delete the resources in the rendered Template.  Choices:   - `"absent"` - `"present"` - `"rendered"` ← (default) |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **wait**  boolean | Whether to wait for certain resource kinds to end up in the desired state.  By default the module exits once Kubernetes has received the request.  Implemented for `state=present` for `Deployment`, `DaemonSet` and `Pod`, and for `state=absent` for all resource kinds.  For resource kinds without an implementation, `wait` returns immediately unless `wait_condition` is set.  Choices:   - `false` ← (default) - `true` |
| **wait_condition**  dictionary | Specifies a custom condition on the status to wait for.  Ignored if `wait` is not set or is set to False. |
| **reason**  string | The value of the reason field in your desired condition  For example, if a `Deployment` is paused, The `Progressing` `type` will have the `DeploymentPaused` reason.  The possible reasons in a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **status**  string | The value of the status field in your desired condition.  For example, if a `Deployment` is paused, the `Progressing` `type` will have the `Unknown` status.  Choices:   - `"True"` ← (default) - `"False"` - `"Unknown"` |
| **type**  string | The type of condition to wait for.  For example, the `Pod` resource will set the `Ready` condition (among others).  Required if you are specifying a `wait_condition`.  If left empty, the `wait_condition` field will be ignored.  The possible types for a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  Default: `5` |
| **wait_timeout**  integer | How long in seconds to wait for the resource to end up in the desired state.  Ignored if `wait` is not set.  Default: `120` |

## [Notes](openshift_process_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_process_module.md#id5)

```yaml+jinja
- name: Process a template in the cluster
  community.okd.openshift_process:
    name: nginx-example
    namespace: openshift # only needed if using a template already on the server
    parameters:
      NAMESPACE: openshift
      NAME: test123
    state: rendered
  register: result

- name: Create the rendered resources using apply
  community.okd.k8s:
    namespace: default
    definition: '{{ item }}'
    wait: yes
    apply: yes
  loop: '{{ result.resources }}'

- name: Process a template with parameters from an env file and create the resources
  community.okd.openshift_process:
    name: nginx-example
    namespace: openshift
    namespace_target: default
    parameter_file: 'files/nginx.env'
    state: present
    wait: yes

- name: Process a local template and create the resources
  community.okd.openshift_process:
    src: files/example-template.yaml
    parameter_file: files/example.env
    namespace_target: default
    state: present

- name: Process a local template, delete the resources, and wait for them to terminate
  community.okd.openshift_process:
    src: files/example-template.yaml
    parameter_file: files/example.env
    namespace_target: default
    state: absent
    wait: yes
```

## [Return Values](openshift_process_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | The rendered resources defined in the Template  Returned: on success when state is rendered |
| **apiVersion**  string | The versioned schema of this representation of an object.  Returned: success |
| **kind**  string | Represents the REST resource this object represents.  Returned: success |
| **metadata**  complex | Standard object metadata. Includes name, namespace, annotations, labels, etc.  Returned: success |
| **name**  string | The name of the resource  Returned: success |
| **namespace**  string | The namespace of the resource  Returned: success |
| **spec**  dictionary | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  Returned: success |
| **status**  dictionary | Current status details for the object.  Returned: success |
| **conditions**  complex | Array of status conditions for the object. Not guaranteed to be present  Returned: success |
| **result**  complex | The created, patched, or otherwise present object. Will be empty in the case of a deletion.  Returned: on success when state is present or absent |
| **apiVersion**  string | The versioned schema of this representation of an object.  Returned: success |
| **duration**  integer | elapsed time of task in seconds  Returned: when `wait` is true  Sample: `48` |
| **items**  list / elements=string | Returned only when multiple yaml documents are passed to src or resource_definition  Returned: when resource_definition or src contains list of objects |
| **kind**  string | Represents the REST resource this object represents.  Returned: success |
| **metadata**  complex | Standard object metadata. Includes name, namespace, annotations, labels, etc.  Returned: success |
| **name**  string | The name of the resource  Returned: success |
| **namespace**  string | The namespace of the resource  Returned: success |
| **spec**  dictionary | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  Returned: success |
| **status**  complex | Current status details for the object.  Returned: success |
| **conditions**  complex | Array of status conditions for the object. Not guaranteed to be present  Returned: success |

### Authors

- Fabian von Feilitzsch (@fabianvf)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
