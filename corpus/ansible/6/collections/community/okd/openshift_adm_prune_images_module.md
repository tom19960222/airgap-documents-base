---
collection: ansible
version: "6"
title: "community.okd.openshift_adm_prune_images module – Remove unreferenced images"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_adm_prune_images_module.html
fetched_at: 2026-07-27T17:20:10+00:00
---
# community.okd.openshift_adm_prune_images module – Remove unreferenced images

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
> see [Requirements](openshift_adm_prune_images_module.md#ansible-collections-community-okd-openshift-adm-prune-images-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_adm_prune_images`.

New in community.okd 2.2.0

- [Synopsis](openshift_adm_prune_images_module.md#synopsis)
- [Requirements](openshift_adm_prune_images_module.md#requirements)
- [Parameters](openshift_adm_prune_images_module.md#parameters)
- [Notes](openshift_adm_prune_images_module.md#notes)
- [Examples](openshift_adm_prune_images_module.md#examples)
- [Return Values](openshift_adm_prune_images_module.md#return-values)

## [Synopsis](openshift_adm_prune_images_module.md#id1)

- This module allow administrators to remove references images.
- Note that if the `namespace` is specified, only references images on Image stream for the corresponding namespace will be candidate for prune if only they are not used or references in another Image stream from another namespace.
- Analogous to `oc adm prune images`.

## [Requirements](openshift_adm_prune_images_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- docker-image-py

## [Parameters](openshift_adm_prune_images_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_images**  boolean | Include images that were imported from external registries as candidates for pruning.  If pruned, all the mirrored objects associated with them will also be removed from the integrated registry.  Choices:   - `false` - `true` ← (default) |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **ignore_invalid_refs**  boolean | If set to *True*, the pruning process will ignore all errors while parsing image references.  This means that the pruning process will ignore the intended connection between the object and the referenced image.  As a result an image may be incorrectly deleted as unused.  Choices:   - `false` ← (default) - `true` |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **keep_younger_than**  integer | Specify the minimum age (in minutes) of an image and its referrers for it to be considered a candidate for pruning. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **namespace**  string | Use to specify namespace for objects. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **prune_over_size_limit**  boolean | Specify if images which are exceeding LimitRanges specified in the same namespace, should be considered for pruning.  Choices:   - `false` ← (default) - `true` |
| **prune_registry**  boolean | If set to *False*, the prune operation will clean up image API objects, but none of the associated content in the registry is removed.  Choices:   - `false` - `true` ← (default) |
| **registry_ca_cert**  path | Path to a CA certificate used to contact registry. The full certificate chain must be provided to avoid certificate validation errors. |
| **registry_url**  string | The address to use when contacting the registry, instead of using the default value.  This is useful if you can’t resolve or reach the default registry but you do have an alternative route that works.  Particular transport protocol can be enforced using ‘<scheme>://’ prefix. |
| **registry_validate_certs**  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](openshift_adm_prune_images_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_adm_prune_images_module.md#id5)

```yaml+jinja
# Prune if only images and their referrers were more than an hour old
- name: Prune image with referrer been more than an hour old
  community.okd.openshift_adm_prune_images:
    keep_younger_than: 60

# Remove images exceeding currently set limit ranges
- name: Remove images exceeding currently set limit ranges
  community.okd.openshift_adm_prune_images:
    prune_over_size_limit: true

# Force the insecure http protocol with the particular registry host name
- name: Prune images using custom registry
  community.okd.openshift_adm_prune_images:
    registry_url: http://registry.example.org
    registry_validate_certs: false
```

## [Return Values](openshift_adm_prune_images_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **deleted_images**  list / elements=dictionary | The images deleted.  Returned: success  Sample: `[{"apiVersion": "image.openshift.io/v1", "dockerImageLayers": [{"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:5e0b432e8ba9d9029a000e627840b98ffc1ed0c5172075b7d3e869be0df0fe9b", "size": 54932878}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:a84cfd68b5cea612a8343c346bfa5bd6c486769010d12f7ec86b23c74887feb2", "size": 5153424}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:e8b8f2315954535f1e27cd13d777e73da4a787b0aebf4241d225beff3c91cbb1", "size": 10871995}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:0598fa43a7e793a76c198e8d45d8810394e1cfc943b2673d7fcf5a6fdc4f45b3", "size": 54567844}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:83098237b6d3febc7584c1f16076a32ac01def85b0d220ab46b6ebb2d6e7d4d4", "size": 196499409}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:b92c73d4de9a6a8f6b96806a04857ab33cf6674f6411138603471d744f44ef55", "size": 6290769}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:ef9b6ee59783b84a6ec0c8b109c409411ab7c88fa8c53fb3760b5fde4eb0aa07", "size": 16812698}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:c1f6285e64066d36477a81a48d3c4f1dc3c03dddec9e72d97da13ba51bca0d68", "size": 234}, {"mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "name": "sha256:a0ee7333301245b50eb700f96d9e13220cdc31871ec9d8e7f0ff7f03a17c6fb3", "size": 2349241}], "dockerImageManifestMediaType": "application/vnd.docker.distribution.manifest.v2+json", "dockerImageMetadata": {"Architecture": "amd64", "Config": {"Cmd": ["python3"], "Env": ["PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "LANG=C.UTF-8", "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568", "PYTHON_VERSION=3.8.12", "PYTHON_PIP_VERSION=21.2.4", "PYTHON_SETUPTOOLS_VERSION=57.5.0", "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py", "PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309"], "Image": "sha256:cc3a2931749afa7dede97e32edbbe3e627b275c07bf600ac05bc0dc22ef203de"}, "Container": "b43fcf5052feb037f6d204247d51ac8581d45e50f41c6be2410d94b5c3a3453d", "ContainerConfig": {"Cmd": ["/bin/sh", "-c", "#(nop) ", "CMD [\"python3\"]"], "Env": ["PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "LANG=C.UTF-8", "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568", "PYTHON_VERSION=3.8.12", "PYTHON_PIP_VERSION=21.2.4", "PYTHON_SETUPTOOLS_VERSION=57.5.0", "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py", "PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309"], "Hostname": "b43fcf5052fe", "Image": "sha256:cc3a2931749afa7dede97e32edbbe3e627b275c07bf600ac05bc0dc22ef203de"}, "Created": "2021-12-03T01:53:41Z", "DockerVersion": "20.10.7", "Id": "sha256:f746089c9d02d7126bbe829f788e093853a11a7f0421049267a650d52bbcac37", "Size": 347487141, "apiVersion": "image.openshift.io/1.0", "kind": "DockerImage"}, "dockerImageMetadataVersion": "1.0", "dockerImageReference": "python@sha256:a874dcabc74ca202b92b826521ff79dede61caca00ceab0b65024e895baceb58", "kind": "Image", "metadata": {"annotations": {"image.openshift.io/dockerLayersOrder": "ascending"}, "creationTimestamp": "2021-12-07T07:55:30Z", "name": "sha256:a874dcabc74ca202b92b826521ff79dede61caca00ceab0b65024e895baceb58", "resourceVersion": "1139214", "uid": "33be6ab4-af79-4f44-a0fd-4925bd473c1f"}}, "..."]` |
| **updated_image_streams**  list / elements=dictionary | The images streams updated.  Returned: success  Sample: `[{"apiVersion": "image.openshift.io/v1", "kind": "ImageStream", "metadata": {"annotations": {"openshift.io/image.dockerRepositoryCheck": "2021-12-07T07:55:30Z"}, "creationTimestamp": "2021-12-07T07:55:30Z", "generation": 1, "name": "python", "namespace": "images", "resourceVersion": "1139215", "uid": "443bad2c-9fd4-4c8f-8a24-3eca4426b07f"}, "spec": {"lookupPolicy": {"local": false}, "tags": [{"annotations": null, "from": {"kind": "DockerImage", "name": "python:3.8.12"}, "generation": 1, "importPolicy": {"insecure": true}, "name": "3.8.12", "referencePolicy": {"type": "Source"}}]}, "status": {"dockerImageRepository": "image-registry.openshift-image-registry.svc:5000/images/python", "publicDockerImageRepository": "default-route-openshift-image-registry.apps-crc.testing/images/python", "tags": []}}, "..."]` |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
