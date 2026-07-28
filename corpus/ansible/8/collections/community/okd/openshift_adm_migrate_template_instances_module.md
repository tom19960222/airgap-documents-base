---
collection: ansible
version: "8"
title: "community.okd.openshift_adm_migrate_template_instances module – Update TemplateInstances to point to the latest group-version-kinds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/okd/openshift_adm_migrate_template_instances_module.html
fetched_at: 2026-07-28T01:58:15+00:00
---
# community.okd.openshift_adm_migrate_template_instances module – Update TemplateInstances to point to the latest group-version-kinds

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
> see [Requirements](openshift_adm_migrate_template_instances_module.md#ansible-collections-community-okd-openshift-adm-migrate-template-instances-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_adm_migrate_template_instances`.

New in community.okd 2.2.0

- [Synopsis](openshift_adm_migrate_template_instances_module.md#synopsis)
- [Requirements](openshift_adm_migrate_template_instances_module.md#requirements)
- [Parameters](openshift_adm_migrate_template_instances_module.md#parameters)
- [Notes](openshift_adm_migrate_template_instances_module.md#notes)
- [Examples](openshift_adm_migrate_template_instances_module.md#examples)
- [Return Values](openshift_adm_migrate_template_instances_module.md#return-values)

## [Synopsis](openshift_adm_migrate_template_instances_module.md#id1)

- Update TemplateInstances to point to the latest group-version-kinds.
- Analogous to `oc adm migrate template-instances`.

## [Requirements](openshift_adm_migrate_template_instances_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0

## [Parameters](openshift_adm_migrate_template_instances_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  *added in kubernetes.core 2.3.0* | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  *added in kubernetes.core 2.3.0* | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  Multiple Kubernetes config file can be provided using separator ‘;’ for Windows platform or ‘:’ for others platforms.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **namespace**  string | The namespace that the template can be found in.  If no namespace if specified, migrate objects in all namespaces. |
| **no_proxy**  string  *added in kubernetes.core 2.3.0* | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  **Choices:**   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  *added in kubernetes.core 2.0.0* | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight=proxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Whether to wait for certain resource kinds to end up in the desired state.  By default the module exits once Kubernetes has received the request.  Implemented for `state=present` for `Deployment`, `DaemonSet` and `Pod`, and for `state=absent` for all resource kinds.  For resource kinds without an implementation, `wait` returns immediately unless `wait_condition` is set.  **Choices:**   - `false` ← (default) - `true` |
| **wait_condition**  dictionary | Specifies a custom condition on the status to wait for.  Ignored if `wait` is not set or is set to False. |
| **reason**  string | The value of the reason field in your desired condition  For example, if a `Deployment` is paused, The `Progressing` `type` will have the `DeploymentPaused` reason.  The possible reasons in a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **status**  string | The value of the status field in your desired condition.  For example, if a `Deployment` is paused, the `Progressing` `type` will have the `Unknown` status.  **Choices:**   - `"True"` ← (default) - `"False"` - `"Unknown"` |
| **type**  string | The type of condition to wait for.  For example, the `Pod` resource will set the `Ready` condition (among others).  Required if you are specifying a `wait_condition`.  If left empty, the `wait_condition` field will be ignored.  The possible types for a condition are specific to each resource type in Kubernetes.  See the API documentation of the status field for a given resource to see possible choices. |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  **Default:** `5` |
| **wait_timeout**  integer | How long in seconds to wait for the resource to end up in the desired state.  Ignored if `wait` is not set.  **Default:** `120` |

## [Notes](openshift_adm_migrate_template_instances_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_adm_migrate_template_instances_module.md#id5)

```yaml+jinja
- name: Migrate TemplateInstances in namespace=test
  community.okd.openshift_adm_migrate_template_instances:
    namespace: test
  register: _result

- name: Migrate TemplateInstances in all namespaces
  community.okd.openshift_adm_migrate_template_instances:
  register: _result
```

## [Return Values](openshift_adm_migrate_template_instances_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  list / elements=dictionary | List with all TemplateInstances that have been migrated.  **Returned:** success  **Sample:** `[{"apiVersion": "template.openshift.io/v1", "kind": "TemplateInstance", "metadata": {"creationTimestamp": "2021-11-10T11:12:09Z", "finalizers": ["template.openshift.io/finalizer"], "managedFields": [{"apiVersion": "template.openshift.io/v1", "fieldsType": "FieldsV1", "fieldsV1": {"f:spec": {"f:template": {"f:metadata": {"f:name": {}}, "f:objects": {}, "f:parameters": {}}}}, "manager": "kubectl-create", "operation": "Update", "time": "2021-11-10T11:12:09Z"}, {"apiVersion": "template.openshift.io/v1", "fieldsType": "FieldsV1", "fieldsV1": {"f:metadata": {"f:finalizers": {".": {}, "v:\"template.openshift.io/finalizer\"": {}}}, "f:status": {"f:conditions": {}}}, "manager": "openshift-controller-manager", "operation": "Update", "time": "2021-11-10T11:12:09Z"}, {"apiVersion": "template.openshift.io/v1", "fieldsType": "FieldsV1", "fieldsV1": {"f:status": {"f:objects": {}}}, "manager": "OpenAPI-Generator", "operation": "Update", "time": "2021-11-10T11:12:33Z"}], "name": "demo", "namespace": "test", "resourceVersion": "545370", "uid": "09b795d7-7f07-4d94-bf0f-2150ee66f88d"}, "spec": {"requester": {"groups": ["system:masters", "system:authenticated"], "username": "system:admin"}, "template": {"metadata": {"creationTimestamp": null, "name": "template"}, "objects": [{"apiVersion": "v1", "kind": "Secret", "metadata": {"labels": {"foo": "bar"}, "name": "secret"}}, {"apiVersion": "apps/v1", "kind": "Deployment", "metadata": {"name": "deployment"}, "spec": {"replicas": 0, "selector": {"matchLabels": {"key": "value"}}, "template": {"metadata": {"labels": {"key": "value"}}, "spec": {"containers": [{"image": "k8s.gcr.io/e2e-test-images/agnhost:2.32", "name": "hello-openshift"}]}}}}, {"apiVersion": "v1", "kind": "Route", "metadata": {"name": "route"}, "spec": {"to": {"name": "foo"}}}], "parameters": [{"name": "NAME", "value": "${NAME}"}]}}, "status": {"conditions": [{"lastTransitionTime": "2021-11-10T11:12:09Z", "message": "", "reason": "Created", "status": "True", "type": "Ready"}], "objects": [{"ref": {"apiVersion": "v1", "kind": "Secret", "name": "secret", "namespace": "test", "uid": "33fad364-6d47-4f9c-9e51-92cba5602a57"}}, {"ref": {"apiVersion": "apps/v1", "kind": "Deployment", "name": "deployment", "namespace": "test", "uid": "3b527f88-42a1-4811-9e2f-baad4e4d8807"}}, {"ref": {"apiVersion": "route.openshift.io/v1.Route", "kind": "Route", "name": "route", "namespace": "test", "uid": "5b5411de-8769-4e27-ba52-6781630e4008"}}]}}, "..."]` |

### Authors

- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/openshift/community.okd/issues)
- [Repository (Sources)](https://github.com/openshift/community.okd)
