---
collection: ansible
version: "6"
title: "kubernetes.core.k8s lookup – Query the K8s API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/k8s_lookup.html
fetched_at: 2026-07-27T17:55:00+00:00
---
# kubernetes.core.k8s lookup – Query the K8s API

> **Note:**
>
> This lookup plugin is part of the [kubernetes.core collection](https://galaxy.ansible.com/kubernetes/core) (version 2.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](k8s_lookup.md#ansible-collections-kubernetes-core-k8s-lookup-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.k8s`.

- [Synopsis](k8s_lookup.md#synopsis)
- [Requirements](k8s_lookup.md#requirements)
- [Keyword parameters](k8s_lookup.md#keyword-parameters)
- [Notes](k8s_lookup.md#notes)
- [Examples](k8s_lookup.md#examples)
- [Return Value](k8s_lookup.md#return-value)

## [Synopsis](k8s_lookup.md#id1)

- Uses the Kubernetes Python client to fetch a specific object by name, all matching objects within a namespace, or all matching objects for all namespaces, as well as information about the cluster.
- Provides access the full range of K8s APIs.
- Enables authentication via config file, certificates, password or token.

## [Requirements](k8s_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Keyword parameters](k8s_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('kubernetes.core.k8s', key1=value1, key2=value2, ...)` and `query('kubernetes.core.k8s', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **api_version**  string | Use to specify the API version. If *resource definition* is provided, the *apiVersion* from the *resource_definition* will override this option.  Default: `"v1"` |
| **ca_cert**  aliases: ssl_ca_cert  string | Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  string | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  string | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **cluster_info**  string | Use to specify the type of cluster information you are attempting to retrieve. Will take priority over all the other options. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **field_selector**  string | Specific fields on which to query. Ignored when *resource_name* is provided. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **kind**  string / required | Use to specify an object model. If *resource definition* is provided, the *kind* from a *resource_definition* will override this option. |
| **kubeconfig**  string | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable. |
| **label_selector**  string | Additional labels to include in the query. Ignored when *resource_name* is provided. |
| **namespace**  string | Limit the objects returned to a specific namespace. If *resource definition* is provided, the *metadata.namespace* value from the *resource_definition* will override this option. |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable. |
| **resource_definition**  string | Provide a YAML configuration for an object. NOTE: *kind*, *api_version*, *resource_name*, and *namespace* will be overwritten by corresponding values found in the provided *resource_definition*. |
| **resource_name**  string | Fetch a specific object by name. If *resource definition* is provided, the *metadata.name* value from the *resource_definition* will override this option. |
| **src**  string | Provide a path to a file containing a valid YAML definition of an object dated. Mutually exclusive with *resource_definition*. NOTE: *kind*, *api_version*, *resource_name*, and *namespace* will be overwritten by corresponding values found in the configuration read in from the *src* file.  Reads from the local file system. To read from the Ansible controller’s file system, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to *resource_definition*. See Examples below. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](k8s_lookup.md#id4)

> **Note:**
>
> - While querying, please use `query` or `lookup` format with `wantlist=True` to provide an easier and more consistent interface. For more details, see <https://docs.ansible.com/ansible/latest/plugins/lookup.html#forcing-lookups-to-return-lists-query-and-wantlist-true>.

## [Examples](k8s_lookup.md#id5)

```yaml+jinja
- name: Fetch a list of namespaces
  set_fact:
    projects: "{{ query('kubernetes.core.k8s', api_version='v1', kind='Namespace') }}"

- name: Fetch all deployments
  set_fact:
    deployments: "{{ query('kubernetes.core.k8s', kind='Deployment') }}"

- name: Fetch all deployments in a namespace
  set_fact:
    deployments: "{{ query('kubernetes.core.k8s', kind='Deployment', namespace='testing') }}"

- name: Fetch a specific deployment by name
  set_fact:
    deployments: "{{ query('kubernetes.core.k8s', kind='Deployment', namespace='testing', resource_name='elastic') }}"

- name: Fetch with label selector
  set_fact:
    service: "{{ query('kubernetes.core.k8s', kind='Service', label_selector='app=galaxy') }}"

# Use parameters from a YAML config

- name: Load config from the Ansible controller filesystem
  set_fact:
    config: "{{ lookup('file', 'service.yml') | from_yaml }}"

- name: Using the config (loaded from a file in prior task), fetch the latest version of the object
  set_fact:
    service: "{{ query('kubernetes.core.k8s', resource_definition=config) }}"

- name: Use a config from the local filesystem
  set_fact:
    service: "{{ query('kubernetes.core.k8s', src='service.yml') }}"
```

## [Return Value](k8s_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | One ore more object definitions returned from the API.  Returned: success  Sample: `[{"apiVersion": "v1", "data": {"key1": "val1"}, "kind": "ConfigMap", "metadata": {"creationTimestamp": "2022-03-04T13:59:49Z", "name": "my-config-map", "namespace": "default", "resourceVersion": "418", "uid": "5714b011-d090-4eac-8272-a0ea82ec0abd"}}]` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Fabian von Feilitzsch (@fabianvf)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
