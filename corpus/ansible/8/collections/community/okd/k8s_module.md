---
collection: ansible
version: "8"
title: "community.okd.k8s module – Manage OpenShift objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/okd/k8s_module.html
fetched_at: 2026-07-28T01:58:14+00:00
---
# community.okd.k8s module – Manage OpenShift objects

> **Note:**
>
> This module is part of the [community.okd collection](https://galaxy.ansible.com/ui/repo/published/community/okd/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.okd`.
> You need further requirements to be able to use this module,
> see [Requirements](k8s_module.md#ansible-collections-community-okd-k8s-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.k8s`.

- [Synopsis](k8s_module.md#synopsis)
- [Requirements](k8s_module.md#requirements)
- [Parameters](k8s_module.md#parameters)
- [Notes](k8s_module.md#notes)
- [Examples](k8s_module.md#examples)
- [Return Values](k8s_module.md#return-values)

## [Synopsis](k8s_module.md#id1)

- Use the Kubernetes Python client to perform CRUD operations on K8s objects.
- Pass the object definition from a source file or inline. See examples for reading files and using Jinja templates or vault-encrypted files.
- Access to the full range of K8s APIs.
- Use the [kubernetes.core.k8s_info](../../kubernetes/core/k8s_info_module.md#ansible-collections-kubernetes-core-k8s-info-module) module to obtain a list of items about an object of type `kind`.
- Authenticate using either a config file, certificates, password or token.
- Supports check mode.
- Optimized for OKD/OpenShift Kubernetes flavors.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](k8s_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](k8s_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **api_version**  aliases: api, version  string | Use to specify the API version.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *kind*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *apiVersion* value from the *resource_definition* will override this option.  **Default:** `"v1"` |
| **append_hash**  boolean | Whether to append a hash to a resource name for immutability purposes  Applies only to ConfigMap and Secret resources  The parameter will be silently ignored for other resource kinds  The full definition of an object is needed to generate the hash - this means that deleting an object created with append_hash will only work if the same object is passed with state=absent (alternatively, just use state=absent with the name including the generated hash and append_hash=no)  **Choices:**   - `false` ← (default) - `true` |
| **apply**  boolean | `apply` compares the desired resource definition with the previously supplied resource definition, ignoring properties that are automatically generated  `apply` works better with Services than ‘force=yes’  mutually exclusive with `merge_type`  **Choices:**   - `false` ← (default) - `true` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **continue_on_error**  boolean  *added in community.okd 2.0.0* | Whether to continue on creation/deletion errors when multiple resources are defined.  This has no effect on the validation step which is controlled by the `validate.fail_on_error` parameter.  **Choices:**   - `false` ← (default) - `true` |
| **delete_options**  dictionary  *added in kubernetes.core 1.2.0* | Configure behavior when deleting an object.  Only used when *state=absent*. |
| **gracePeriodSeconds**  integer | Specify how many seconds to wait before forcefully terminating.  Only implemented for Pod resources.  If not specified, the default grace period for the object type will be used. |
| **preconditions**  dictionary | Specify condition that must be met for delete to proceed. |
| **resourceVersion**  string | Specify the resource version of the target object. |
| **uid**  string | Specify the UID of the target object. |
| **propagationPolicy**  string | Use to control how dependent objects are deleted.  If not specified, the default policy for the object type will be used. This may vary across object types.  **Choices:**   - `"Foreground"` - `"Background"` - `"Orphan"` |
| **force**  boolean | If set to `yes`, and *state* is `present`, an existing object will be replaced.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  *added in kubernetes.core 2.3.0* | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  *added in kubernetes.core 2.3.0* | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kind**  string | Use to specify an object model.  Use to create, delete, or discover an object without providing a full resource definition.  Use in conjunction with *api_version*, *name*, and *namespace* to identify a specific object.  If *resource definition* is provided, the *kind* value from the *resource_definition* will override this option. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  Multiple Kubernetes config file can be provided using separator ‘;’ for Windows platform or ‘:’ for others platforms.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **merge_type**  list / elements=string | Whether to override the default patch merge approach with a specific type. By default, the strategic merge will typically be used.  For example, Custom Resource Definitions typically aren’t updatable by the usual strategic merge. You may want to use `merge` if you see “strategic merge patch format is not supported”  See <https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/#use-a-json-merge-patch-to-update-a-deployment>  If more than one merge_type is given, the merge_types will be tried in order  Defaults to `['strategic-merge', 'merge']`, which is ideal for using the same parameters on resource kinds that combine Custom Resources and built-in resources.  mutually exclusive with `apply`  *merge_type=json* is deprecated and will be removed in version 3.0.0. Please use [kubernetes.core.k8s_json_patch](../../kubernetes/core/k8s_json_patch_module.md#ansible-collections-kubernetes-core-k8s-json-patch-module) instead.  **Choices:**   - `"json"` - `"merge"` - `"strategic-merge"` |
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
| **resource_definition**  aliases: definition, inline  string | Provide a valid YAML definition (either as a string, list, or dict) for an object when creating or updating.  NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the provided *resource_definition*. |
| **src**  path | Provide a path to a file containing a valid YAML definition of an object or objects to be created or updated. Mutually exclusive with *resource_definition*. NOTE: *kind*, *api_version*, *name*, and *namespace* will be overwritten by corresponding values found in the configuration read in from the *src* file.  Reads from the local file system. To read from the Ansible controller’s file system, including vaulted files, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to *resource_definition*. See Examples below.  The URL to manifest files that can be used to create the resource. Added in version 2.4.0.  Mutually exclusive with *template* in case of [kubernetes.core.k8s](../../kubernetes/core/k8s_module.md#ansible-collections-kubernetes-core-k8s-module) module. |
| **state**  string | Determines if an object should be created, patched, or deleted. When set to `present`, an object will be created, if it does not already exist. If set to `absent`, an existing object will be deleted. If set to `present`, an existing object will be patched, if its attributes differ from those specified using *resource_definition* or *src*.  `patched` state is an existing resource that has a given patch applied. If the resource doesn’t exist, silently skip it (do not raise an error).  **Choices:**   - `"absent"` - `"present"` ← (default) - `"patched"` |
| **template**  any  *added in community.okd 2.0.0* | Provide a valid YAML template definition file for an object when creating or updating.  Value can be provided as string or dictionary.  Mutually exclusive with `src` and `resource_definition`.  Template files needs to be present on the Ansible Controller’s file system.  Additional parameters can be specified using dictionary.  Valid additional parameters -  `newline_sequence` (str): Specify the newline sequence to use for templating files. valid choices are “\n”, “\r”, “\r\n”. Default value “\n”.  `block_start_string` (str): The string marking the beginning of a block. Default value “{%”.  `block_end_string` (str): The string marking the end of a block. Default value “%}”.  `variable_start_string` (str): The string marking the beginning of a print statement. Default value “{{“.  `variable_end_string` (str): The string marking the end of a print statement. Default value “}}”.  `trim_blocks` (bool): Determine when newlines should be removed from blocks. When set to `yes` the first newline after a block is removed (block, not variable tag!). Default value is true.  `lstrip_blocks` (bool): Determine when leading spaces and tabs should be stripped. When set to `yes` leading spaces and tabs are stripped from the start of a line to a block. This functionality requires Jinja 2.7 or newer. Default value is false. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate**  dictionary | how (if at all) to validate the resource definition against the kubernetes schema. Requires the kubernetes-validate python module |
| **fail_on_error**  boolean | whether to fail on validation errors.  **Choices:**   - `false` - `true` |
| **strict**  boolean | whether to fail when passing unexpected properties  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | version of Kubernetes to validate against. defaults to Kubernetes server version |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Whether to wait for certain resource kinds to end up in the desired state.  By default the module exits once Kubernetes has received the request.  Implemented for `state=present` for `Deployment`, `DaemonSet` and `Pod`, and for `state=absent` for all resource kinds.  For resource kinds without an implementation, `wait` returns immediately unless `wait_condition` is set.  **Choices:**   - `false` ← (default) - `true` |
| **wait_condition**  dictionary | Specifies a custom condition on the status to wait for.  Ignored if `wait` is not set or is set to False. |
| **reason**  string | The value of the reason field in your desired condition  For example, if a `Deployment` is paused, The `Progressing` `type` will have the `DeploymentPaused` reason.  The possible reasons in a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **status**  string | The value of the status field in your desired condition.  For example, if a `Deployment` is paused, the `Progressing` `type` will have the `Unknown` status.  **Choices:**   - `"True"` ← (default) - `"False"` - `"Unknown"` |
| **type**  string | The type of condition to wait for.  For example, the `Pod` resource will set the `Ready` condition (among others).  Required if you are specifying a `wait_condition`.  If left empty, the `wait_condition` field will be ignored.  The possible types for a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  **Default:** `5` |
| **wait_timeout**  integer | How long in seconds to wait for the resource to end up in the desired state.  Ignored if `wait` is not set.  **Default:** `120` |

## [Notes](k8s_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](k8s_module.md#id5)

```yaml+jinja
- name: Create a k8s namespace
  community.okd.k8s:
    name: testing
    api_version: v1
    kind: Namespace
    state: present

- name: Create a Service object from an inline definition
  community.okd.k8s:
    state: present
    definition:
      apiVersion: v1
      kind: Service
      metadata:
        name: web
        namespace: testing
        labels:
          app: galaxy
          service: web
      spec:
        selector:
          app: galaxy
          service: web
        ports:
        - protocol: TCP
          targetPort: 8000
          name: port-8000-tcp
          port: 8000

- name: Remove an existing Service object
  community.okd.k8s:
    state: absent
    api_version: v1
    kind: Service
    namespace: testing
    name: web

# Passing the object definition from a file

- name: Create a Deployment by reading the definition from a local file
  community.okd.k8s:
    state: present
    src: /testing/deployment.yml

- name: >-
    Read definition file from the Ansible controller file system.
    If the definition file has been encrypted with Ansible Vault it will automatically be decrypted.
  community.okd.k8s:
    state: present
    definition: "{{ lookup('file', '/testing/deployment.yml') | from_yaml }}"

- name: Read definition file from the Ansible controller file system after Jinja templating
  community.okd.k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') | from_yaml }}"

- name: fail on validation errors
  community.okd.k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') | from_yaml }}"
    validate:
      fail_on_error: yes

- name: warn on validation errors, check for unexpected properties
  community.okd.k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') | from_yaml }}"
    validate:
      fail_on_error: no
      strict: yes
```

## [Return Values](k8s_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The created, patched, or otherwise present object. Will be empty in the case of a deletion.  **Returned:** success |
| **api_version**  string | The versioned schema of this representation of an object.  **Returned:** success |
| **duration**  integer | elapsed time of task in seconds  **Returned:** when `wait` is true  **Sample:** `48` |
| **error**  complex | error while trying to create/delete the object.  **Returned:** error |
| **items**  list / elements=string | Returned only when multiple yaml documents are passed to src or resource_definition  **Returned:** when resource_definition or src contains list of objects |
| **kind**  string | Represents the REST resource this object represents.  **Returned:** success |
| **metadata**  complex | Standard object metadata. Includes name, namespace, annotations, labels, etc.  **Returned:** success |
| **spec**  complex | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  **Returned:** success |
| **status**  complex | Current status details for the object.  **Returned:** success |

### Authors

- Chris Houseknecht (@chouseknecht)
- Fabian von Feilitzsch (@fabianvf)

### Collection links

- [Issue Tracker](https://github.com/openshift/community.okd/issues)
- [Repository (Sources)](https://github.com/openshift/community.okd)
