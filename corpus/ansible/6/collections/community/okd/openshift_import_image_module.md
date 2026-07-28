---
collection: ansible
version: "6"
title: "community.okd.openshift_import_image module – Import the latest image information from a tag in a container image registry."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_import_image_module.html
fetched_at: 2026-07-27T17:20:12+00:00
---
# community.okd.openshift_import_image module – Import the latest image information from a tag in a container image registry.

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
> see [Requirements](openshift_import_image_module.md#ansible-collections-community-okd-openshift-import-image-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_import_image`.

New in community.okd 2.2.0

- [Synopsis](openshift_import_image_module.md#synopsis)
- [Requirements](openshift_import_image_module.md#requirements)
- [Parameters](openshift_import_image_module.md#parameters)
- [Notes](openshift_import_image_module.md#notes)
- [Examples](openshift_import_image_module.md#examples)
- [Return Values](openshift_import_image_module.md#return-values)

## [Synopsis](openshift_import_image_module.md#id1)

- Image streams allow you to control which images are rolled out to your builds and applications.
- This module fetches the latest version of an image from a remote repository and updates the image stream tag if it does not match the previous value.
- Running the module multiple times will not create duplicate entries.
- When importing an image, only the image metadata is copied, not the image contents.
- Analogous to `oc import-image`.

## [Requirements](openshift_import_image_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- docker-image-py

## [Parameters](openshift_import_image_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all**  boolean | If set to *true*, import all tags from the provided source on creation or if `source` is specified.  Choices:   - `false` ← (default) - `true` |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **name**  any / required | Image stream to import tag into.  This can be provided as a list of images streams or a single value. |
| **namespace**  string / required | Use to specify namespace for image stream to create/update. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **reference_policy**  string | Allow to request pullthrough for external image when set to *local*.  Choices:   - `"source"` ← (default) - `"local"` |
| **scheduled**  boolean | Set each imported Docker image to be periodically imported from a remote repository.  Choices:   - `false` ← (default) - `true` |
| **source**  string | A Docker image repository to import images from.  Should be provided as ‘registry.io/repo/image’ |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **validate_registry_certs**  boolean | If set to *true*, allow importing from registries that have invalid HTTPS certificates. or are hosted via HTTP. This parameter will take precedence over the insecure annotation.  Choices:   - `false` - `true` |

## [Notes](openshift_import_image_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_import_image_module.md#id5)

```yaml+jinja
# Import tag latest into a new image stream.
- name: Import tag latest into new image stream
  community.okd.openshift_import_image:
    namespace: testing
    name: mystream
    source: registry.io/repo/image:latest

# Update imported data for tag latest in an already existing image stream.
- name: Update imported data for tag latest
  community.okd.openshift_import_image:
    namespace: testing
    name: mystream

# Update imported data for tag 'stable' in an already existing image stream.
- name: Update imported data for tag latest
  community.okd.openshift_import_image:
    namespace: testing
    name: mystream:stable

# Update imported data for all tags in an existing image stream.
- name: Update imported data for all tags
  community.okd.openshift_import_image:
    namespace: testing
    name: mystream
    all: true

# Import all tags into a new image stream.
- name: Import all tags into a new image stream.
  community.okd.openshift_import_image:
    namespace: testing
    name: mystream
    source: registry.io/repo/image:latest
    all: true

# Import all tags into a new image stream for a list of image streams
- name: Import all tags into a new image stream.
  community.okd.openshift_import_image:
    namespace: testing
    name:
      - mystream1
      - mystream2
      - mystream3
    source: registry.io/repo/image:latest
    all: true
```

## [Return Values](openshift_import_image_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  list / elements=dictionary | List with all ImageStreamImport that have been created.  Returned: success |
| **api_version**  string | The versioned schema of this representation of an object.  Returned: success |
| **kind**  string | Represents the REST resource this object represents.  Returned: success |
| **metadata**  dictionary | Standard object metadata. Includes name, namespace, annotations, labels, etc.  Returned: success |
| **spec**  dictionary | Specific attributes of the object. Will vary based on the *api_version* and *kind*.  Returned: success |
| **status**  dictionary | Current status details for the object.  Returned: success |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
