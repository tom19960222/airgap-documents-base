---
collection: ansible
version: "6"
title: "community.okd.openshift inventory – OpenShift inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_inventory.html
fetched_at: 2026-07-27T17:20:15+00:00
---
# community.okd.openshift inventory – OpenShift inventory source

> **Note:**
>
> This inventory plugin is part of the [community.okd collection](https://galaxy.ansible.com/community/okd) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.okd`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](openshift_inventory.md#ansible-collections-community-okd-openshift-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift`.

- [Synopsis](openshift_inventory.md#synopsis)
- [Requirements](openshift_inventory.md#requirements)
- [Parameters](openshift_inventory.md#parameters)
- [Examples](openshift_inventory.md#examples)

## [Synopsis](openshift_inventory.md#id1)

- Fetch containers, services and routes for one or more clusters
- Groups by cluster name, namespace, namespace_services, namespace_pods, namespace_routes, and labels
- Uses openshift.(yml|yaml) YAML configuration file to set parameter values.

## [Requirements](openshift_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 3.6
- kubernetes >= 12.0.0
- PyYAML >= 3.11

## [Parameters](openshift_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **connections**  string | Optional list of cluster connection settings. If no connections are provided, the default *~/.kube/config* and active context will be used, and objects will be returned for all namespaces the active user is authorized to access. |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  string | Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  string | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  string | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **kubeconfig**  string | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable. |
| **name**  string | Optional name to assign to the cluster. If not provided, a name is constructed from the server and port. |
| **namespaces**  string | List of namespaces. If not specified, will fetch all containers for all namespaces user is authorized to access. |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **plugin**  string / required | token that ensures this is a source file for the ‘openshift’ plugin.  Choices:   - `"openshift"` - `"community.okd.openshift"` |

## [Examples](openshift_inventory.md#id4)

```yaml+jinja
# File must be named openshift.yaml or openshift.yml

# Authenticate with token, and return all pods and services for all namespaces
plugin: community.okd.openshift
connections:
  - host: https://192.168.64.4:8443
    api_key: xxxxxxxxxxxxxxxx
    verify_ssl: false

# Use default config (~/.kube/config) file and active context, and return objects for a specific namespace
plugin: community.okd.openshift
connections:
  - namespaces:
    - testing

# Use a custom config file, and a specific context.
plugin: community.okd.openshift
connections:
  - kubeconfig: /path/to/config
    context: 'awx/192-168-64-4:8443/developer'
```

### Authors

- Chris Houseknecht <@chouseknecht>

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
