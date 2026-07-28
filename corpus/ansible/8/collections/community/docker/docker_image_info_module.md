---
collection: ansible
version: "8"
title: "community.docker.docker_image_info module – Inspect docker images"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_image_info_module.html
fetched_at: 2026-07-28T01:43:47+00:00
---
# community.docker.docker_image_info module – Inspect docker images

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/ui/repo/published/community/docker/) (version 3.4.11).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this module,
> see [Requirements](docker_image_info_module.md#ansible-collections-community-docker-docker-image-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_image_info`.

- [Synopsis](docker_image_info_module.md#synopsis)
- [Requirements](docker_image_info_module.md#requirements)
- [Parameters](docker_image_info_module.md#parameters)
- [Attributes](docker_image_info_module.md#attributes)
- [Notes](docker_image_info_module.md#notes)
- [Examples](docker_image_info_module.md#examples)
- [Return Values](docker_image_info_module.md#return-values)

## [Synopsis](docker_image_info_module.md#id1)

- Provide one or more image names, and the module will inspect each, returning an array of inspection results.
- If an image does not exist locally, it will not appear in the results. If you want to check whether an image exists locally, you can call the module with the image name, then check whether the result list is empty (image does not exist) or has one element (the image exists locally).
- The module will not attempt to pull images from registries. Use [community.docker.docker_image](docker_image_module.md#ansible-collections-community-docker-docker-image-module) with `source=pull` to ensure an image is pulled.

## [Requirements](docker_image_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- backports.ssl_match_hostname (when using TLS on Python 2)
- paramiko (when using SSH with `use_ssh_client=false`)
- pyOpenSSL (when using TLS)
- pywin32 (when using named pipes on Windows 32)
- requests

## [Parameters](docker_image_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by this collection and the docker daemon.  If the value is not specified in the task, the value of environment variable [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `ca.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `cert.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `key.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **debug**  boolean | Debug mode  **Choices:**   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"unix://var/run/docker.sock"` |
| **name**  list / elements=string | An image name or a list of image names. Name format will be `name[:tag]` or `repository/name[:tag]`, where `tag` is optional. If a tag is not provided, `latest` will be used. Instead of image names, also image IDs can be used.  If no name is provided, a list of all images will be returned. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by [SSL Python module](https://docs.python.org/3/library/ssl.html).  If the value is not specified in the task, the value of environment variable [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION) will be used instead. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if `validate_certs` is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.  Note that this option had a default value `localhost` in older versions. It was removed in community.docker 3.0.0. |
| **use_ssh_client**  boolean  *added in community.docker 1.5.0* | For SSH transports, use the `ssh` CLI tool instead of paramiko.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](docker_image_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.docker.docker**, **docker** | Use `group/docker` or `group/community.docker.docker` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](docker_image_info_module.md#id5)

> **Note:**
>
> - This module was called `docker_image_facts` before Ansible 2.8. The usage did not change.
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST), [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME), [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION), [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH), [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION), [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS), [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) and [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT). If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - This module does **not** use the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon. It uses code derived from the Docker SDK or Python that is included in this collection.

## [Examples](docker_image_info_module.md#id6)

```yaml+jinja
- name: Inspect a single image
  community.docker.docker_image_info:
    name: pacur/centos-7

- name: Inspect multiple images
  community.docker.docker_image_info:
    name:
      - pacur/centos-7
      - sinatra
  register: result

- name: Make sure that both images pacur/centos-7 and sinatra exist locally
  ansible.builtin.assert:
    that:
      - result.images | length == 2
```

## [Return Values](docker_image_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **images**  list / elements=dictionary | Inspection results for the selected images.  The list only contains inspection results of images existing locally.  **Returned:** always  **Sample:** `[{"Architecture": "amd64", "Author": "", "Comment": "", "Config": {"AttachStderr": false, "AttachStdin": false, "AttachStdout": false, "Cmd": ["/etc/docker/registry/config.yml"], "Domainname": "", "Entrypoint": ["/bin/registry"], "Env": ["PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"], "ExposedPorts": {"5000/tcp": {}}, "Hostname": "e5c68db50333", "Image": "c72dce2618dc8f7b794d2b2c2b1e64e0205ead5befc294f8111da23bd6a2c799", "Labels": {}, "OnBuild": [], "OpenStdin": false, "StdinOnce": false, "Tty": false, "User": "", "Volumes": {"/var/lib/registry": {}}, "WorkingDir": ""}, "Container": "e83a452b8fb89d78a25a6739457050131ca5c863629a47639530d9ad2008d610", "ContainerConfig": {"AttachStderr": false, "AttachStdin": false, "AttachStdout": false, "Cmd": ["/bin/sh", "-c", "#(nop) CMD [\"/etc/docker/registry/config.yml\"]"], "Domainname": "", "Entrypoint": ["/bin/registry"], "Env": ["PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"], "ExposedPorts": {"5000/tcp": {}}, "Hostname": "e5c68db50333", "Image": "c72dce2618dc8f7b794d2b2c2b1e64e0205ead5befc294f8111da23bd6a2c799", "Labels": {}, "OnBuild": [], "OpenStdin": false, "StdinOnce": false, "Tty": false, "User": "", "Volumes": {"/var/lib/registry": {}}, "WorkingDir": ""}, "Created": "2016-03-08T21:08:15.399680378Z", "DockerVersion": "1.9.1", "GraphDriver": {"Data": null, "Name": "aufs"}, "Id": "53773d8552f07b730f3e19979e32499519807d67b344141d965463a950a66e08", "Name": "registry:2", "Os": "linux", "Parent": "f0b1f729f784b755e7bf9c8c2e65d8a0a35a533769c2588f02895f6781ac0805", "RepoDigests": [], "RepoTags": ["registry:2"], "Size": 0, "VirtualSize": 165808884}]` |

### Authors

- Chris Houseknecht (@chouseknecht)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
