---
collection: ansible
version: "6"
title: "community.okd.openshift_registry_info module – Display information about the integrated registry."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_registry_info_module.html
fetched_at: 2026-07-27T17:20:13+00:00
---
# community.okd.openshift_registry_info module – Display information about the integrated registry.

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
> see [Requirements](openshift_registry_info_module.md#ansible-collections-community-okd-openshift-registry-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_registry_info`.

New in community.okd 2.2.0

- [Synopsis](openshift_registry_info_module.md#synopsis)
- [Requirements](openshift_registry_info_module.md#requirements)
- [Parameters](openshift_registry_info_module.md#parameters)
- [Notes](openshift_registry_info_module.md#notes)
- [Examples](openshift_registry_info_module.md#examples)
- [Return Values](openshift_registry_info_module.md#return-values)

## [Synopsis](openshift_registry_info_module.md#id1)

- This module exposes information about the integrated registry.
- Use `check` to verify your local client can access the registry.
- If the adminstrator has not configured a public hostname for the registry then this command may fail when run outside of the server.
- Analogous to `oc registry info`.

## [Requirements](openshift_registry_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- docker-image-py

## [Parameters](openshift_registry_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **check**  boolean | Attempt to contact the integrated registry using local client.  Choices:   - `false` ← (default) - `true` |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](openshift_registry_info_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_registry_info_module.md#id5)

```yaml+jinja
# Get registry information
- name: Read integrated registry information
  community.okd.openshift_registry_info:

# Read registry integrated information and attempt to contact using local client.
- name: Attempt to contact integrated registry using local client
  community.okd.openshift_registry_info:
    check: yes
```

## [Return Values](openshift_registry_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **check**  dictionary | Whether the local client can contact or not the registry.  Returned: success |
| **msg**  string | message describing the ping operation.  Returned: always |
| **reached**  string | Whether the registry has been reached or not.  Returned: success |
| **internal_hostname**  string | The internal registry hostname.  Returned: success |
| **public_hostname**  string | The public registry hostname.  Returned: success |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
