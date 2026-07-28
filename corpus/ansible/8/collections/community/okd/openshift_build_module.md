---
collection: ansible
version: "8"
title: "community.okd.openshift_build module – Start a new build or Cancel running, pending, or new builds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/okd/openshift_build_module.html
fetched_at: 2026-07-28T01:58:20+00:00
---
# community.okd.openshift_build module – Start a new build or Cancel running, pending, or new builds.

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
> see [Requirements](openshift_build_module.md#ansible-collections-community-okd-openshift-build-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_build`.

New in community.okd 2.3.0

- [Synopsis](openshift_build_module.md#synopsis)
- [Requirements](openshift_build_module.md#requirements)
- [Parameters](openshift_build_module.md#parameters)
- [Notes](openshift_build_module.md#notes)
- [Examples](openshift_build_module.md#examples)
- [Return Values](openshift_build_module.md#return-values)

## [Synopsis](openshift_build_module.md#id1)

- This module starts a new build from the provided build config or build name.
- This module also cancel a new, pending or running build by requesting a graceful shutdown of the build. There may be a delay between requesting the build and the time the build is terminated.
- This can also restart a new build when the current is cancelled.
- Analogous to `oc cancel-build` and `oc start-build`.

## [Requirements](openshift_build_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0

## [Parameters](openshift_build_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **build_args**  list / elements=dictionary | Specify a list of key-value pair to pass to Docker during the build. |
| **name**  string / required | docker build argument name. |
| **value**  string / required | docker build argument value. |
| **build_config_name**  string | Specify the name of a build config from which a new build will be run.  Mutually exclusive with parameter *build_name*. |
| **build_name**  string | Specify the name of a build which should be re-run.  Mutually exclusive with parameter *build_config_name*. |
| **build_phases**  list / elements=string | List of state for build to cancel.  Ignored when `state=started`.  **Choices:**   - `"New"` - `"Pending"` - `"Running"`   **Default:** `[]` |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **commit**  string | Specify the source code commit identifier the build should use; requires a build based on a Git repository. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **env_vars**  list / elements=dictionary | Specify a list of key-value pair for an environment variable to set for the build container. |
| **name**  string / required | Environment variable name. |
| **value**  string / required | Environment variable value. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  *added in kubernetes.core 2.3.0* | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  *added in kubernetes.core 2.3.0* | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **incremental**  boolean | Overrides the incremental setting in a source-strategy build, ignored if not specified.  **Choices:**   - `false` - `true` |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  Multiple Kubernetes config file can be provided using separator ‘;’ for Windows platform or ‘:’ for others platforms.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **namespace**  string / required | Specify the namespace for the build or the build config. |
| **no_cache**  boolean | Overrides the noCache setting in a docker-strategy build, ignored if not specified.  **Choices:**   - `false` - `true` |
| **no_proxy**  string  *added in kubernetes.core 2.3.0* | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  **Choices:**   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  *added in kubernetes.core 2.0.0* | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight=proxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **state**  string | Determines if a Build should be started ,cancelled or restarted.  When set to `restarted` a new build will be created after the current build is cancelled.  **Choices:**   - `"started"` ← (default) - `"cancelled"` - `"restarted"` |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  **Choices:**   - `false` - `true` |
| **wait**  boolean | When `state=started`, specify whether to wait for a build to complete and exit with a non-zero return code if the build fails.  When *state=cancelled*, specify whether to wait for a build phase to be Cancelled.  **Choices:**   - `false` ← (default) - `true` |
| **wait_sleep**  integer | Number of seconds to sleep between checks.  Ignored if `wait=false`.  **Default:** `5` |
| **wait_timeout**  integer | How long in seconds to wait for a build to complete.  Ignored if `wait=false`.  **Default:** `120` |

## [Notes](openshift_build_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_build_module.md#id5)

```yaml+jinja
# Starts build from build config default/hello-world
- name: Starts build from build config
  community.okd.openshift_build:
    namespace: default
    build_config_name: hello-world

# Starts build from a previous build "default/hello-world-1"
- name: Starts build from a previous build
  community.okd.openshift_build:
    namespace: default
    build_name: hello-world-1

# Cancel the build with the given name
- name: Cancel build from default namespace
  community.okd.openshift_build:
    namespace: "default"
    build_name: ruby-build-1
    state: cancelled

# Cancel the named build and create a new one with the same parameters
- name: Cancel build from default namespace and create a new one
  community.okd.openshift_build:
    namespace: "default"
    build_name: ruby-build-1
    state: restarted

# Cancel all builds created from 'ruby-build' build configuration that are in 'new' state
- name: Cancel build from default namespace and create a new one
  community.okd.openshift_build:
    namespace: "default"
    build_config_name: ruby-build
    build_phases:
      - New
    state: cancelled
```

## [Return Values](openshift_build_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **builds**  complex | The builds that were started/cancelled.  **Returned:** success |
| **api_version**  string | The versioned schema of this representation of an object.  **Returned:** success |
| **kind**  string | Represents the REST resource this object represents.  **Returned:** success |
| **metadata**  dictionary | Standard object metadata. Includes name, namespace, annotations, labels, etc.  **Returned:** success |
| **spec**  dictionary | Specific attributes of the build.  **Returned:** success |
| **status**  dictionary | Current status details for the object.  **Returned:** success |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/openshift/community.okd/issues)
- [Repository (Sources)](https://github.com/openshift/community.okd)
