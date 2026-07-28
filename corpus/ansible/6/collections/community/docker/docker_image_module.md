---
collection: ansible
version: "6"
title: "community.docker.docker_image module – Manage docker images"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_image_module.html
fetched_at: 2026-07-27T17:07:18+00:00
---
# community.docker.docker_image module – Manage docker images

> **Note:**
>
> This module is part of the [community.docker collection](https://galaxy.ansible.com/community/docker) (version 2.7.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this module,
> see [Requirements](docker_image_module.md#ansible-collections-community-docker-docker-image-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_image`.

- [Synopsis](docker_image_module.md#synopsis)
- [Requirements](docker_image_module.md#requirements)
- [Parameters](docker_image_module.md#parameters)
- [Notes](docker_image_module.md#notes)
- [Examples](docker_image_module.md#examples)
- [Return Values](docker_image_module.md#return-values)

## [Synopsis](docker_image_module.md#id1)

- Build, load or pull an image, making the image available for creating containers. Also supports tagging an image, pushing an image, and archiving an image to a `.tar` file.

## [Requirements](docker_image_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.20
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.8.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)

## [Parameters](docker_image_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **archive_path**  path | Use with state `present` to archive an image to a .tar file. |
| **build**  dictionary | Specifies options used for building images. |
| **args**  dictionary | Provide a dictionary of `key:value` build arguments that map to Dockerfile ARG directive.  Docker expects the value to be a string. For convenience any non-string values will be converted to strings.  Requires Docker API >= 1.21. |
| **cache_from**  list / elements=string | List of image names to consider as cache source. |
| **container_limits**  dictionary | A dictionary of limits applied to each container created by the build process. |
| **cpusetcpus**  string | CPUs in which to allow execution.  For example, `0-3` or `0,1`. |
| **cpushares**  integer | CPU shares (relative weight). |
| **memory**  integer | Set memory limit for build. |
| **memswap**  integer | Total memory (memory + swap).  Use `-1` to disable swap. |
| **dockerfile**  string | Use with state `present` and source `build` to provide an alternate name for the Dockerfile to use when building an image.  This can also include a relative path (relative to *path*). |
| **etc_hosts**  dictionary | Extra hosts to add to `/etc/hosts` in building containers, as a mapping of hostname to IP address. |
| **http_timeout**  integer | Timeout for HTTP requests during the image build operation. Provide a positive integer value for the number of seconds. |
| **network**  string | The network to use for `RUN` build instructions. |
| **nocache**  boolean | Do not use cache when building an image.  Choices:   - `false` ← (default) - `true` |
| **path**  path / required | Use with state ‘present’ to build an image. Will be the path to a directory containing the context and Dockerfile for building an image. |
| **platform**  string  added in community.docker 1.1.0 | Platform in the format `os[/arch[/variant]]`. |
| **pull**  boolean | When building an image downloads any updates to the FROM image in Dockerfile.  Choices:   - `false` ← (default) - `true` |
| **rm**  boolean | Remove intermediate containers after build.  Choices:   - `false` - `true` ← (default) |
| **target**  string | When building an image specifies an intermediate build stage by name as a final stage for the resulting image. |
| **use_config_proxy**  boolean | If set to `true` and a proxy configuration is specified in the docker client configuration (by default `$HOME/.docker/config.json`), the corresponding environment variables will be set in the container being built.  Needs Docker SDK for Python >= 3.7.0.  Choices:   - `false` - `true` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **force_absent**  boolean | Use with state *absent* to un-tag and remove all images matching the specified name.  Choices:   - `false` ← (default) - `true` |
| **force_source**  boolean | Use with state `present` to build, load or pull an image (depending on the value of the *source* option) when the image already exists.  Choices:   - `false` ← (default) - `true` |
| **force_tag**  boolean | Use with state `present` to force tagging an image.  Choices:   - `false` ← (default) - `true` |
| **load_path**  path | Use with state `present` to load an image from a .tar file.  Set *source* to `load` if you want to load the image. |
| **name**  string / required | Image name. Name format will be one of: `name`, `repository/name`, `registry_server:port/name`. When pushing or pulling an image the name can optionally include the tag by appending `:tag_name`.  Note that image IDs (hashes) are only supported for *state=absent*, for *state=present* with *source=load*, and for *state=present* with *source=local*. |
| **pull**  dictionary  added in community.docker 1.3.0 | Specifies options used for pulling images. |
| **platform**  string | When pulling an image, ask for this specific platform.  Note that this value is not used to determine whether the image needs to be pulled. This might change in the future in a minor release, though. |
| **push**  boolean | Push the image to the registry. Specify the registry as part of the *name* or *repository* parameter.  Choices:   - `false` ← (default) - `true` |
| **repository**  string | Use with state `present` to tag the image.  Expects format `repository:tag`. If no tag is provided, will use the value of the *tag* parameter or `latest`.  If *push=true*, *repository* must either include a registry, or will be assumed to belong to the default registry (Docker Hub). |
| **source**  string | Determines where the module will try to retrieve the image from.  Use `build` to build the image from a `Dockerfile`. *build.path* must be specified when this value is used.  Use `load` to load the image from a `.tar` file. *load_path* must be specified when this value is used.  Use `pull` to pull the image from a registry.  Use `local` to make sure that the image is already available on the local docker daemon. This means that the module does not try to build, pull or load the image.  Choices:   - `"build"` - `"load"` - `"pull"` - `"local"` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **state**  string | Make assertions about the state of an image.  When `absent` an image will be removed. Use the force option to un-tag and remove all images matching the provided name.  When `present` check if an image exists using the provided name and tag. If the image is not found or the force option is used, the image will either be pulled, built or loaded, depending on the *source* option.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tag**  string | Used to select an image when pulling. Will be added to the image when pushing, tagging or building. Defaults to *latest*.  If *name* parameter format is *name:tag*, then tag value from *name* will take precedence.  Default: `"latest"` |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_image_module.md#id4)

> **Note:**
>
> - Building images is done using Docker daemon’s API. It is not possible to use BuildKit / buildx this way.
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_image_module.md#id5)

```yaml+jinja
- name: Pull an image
  community.docker.docker_image:
    name: pacur/centos-7
    source: pull
    # Select platform for pulling. If not specified, will pull whatever docker prefers.
    pull:
      platform: amd64

- name: Tag and push to docker hub
  community.docker.docker_image:
    name: pacur/centos-7:56
    repository: dcoppenhagan/myimage:7.56
    push: true
    source: local

- name: Tag and push to local registry
  community.docker.docker_image:
    # Image will be centos:7
    name: centos
    # Will be pushed to localhost:5000/centos:7
    repository: localhost:5000/centos
    tag: 7
    push: true
    source: local

- name: Add tag latest to image
  community.docker.docker_image:
    name: myimage:7.1.2
    repository: myimage:latest
    # As 'latest' usually already is present, we need to enable overwriting of existing tags:
    force_tag: true
    source: local

- name: Remove image
  community.docker.docker_image:
    state: absent
    name: registry.ansible.com/chouseknecht/sinatra
    tag: v1

- name: Build an image and push it to a private repo
  community.docker.docker_image:
    build:
      path: ./sinatra
    name: registry.ansible.com/chouseknecht/sinatra
    tag: v1
    push: true
    source: build

- name: Archive image
  community.docker.docker_image:
    name: registry.ansible.com/chouseknecht/sinatra
    tag: v1
    archive_path: my_sinatra.tar
    source: local

- name: Load image from archive and push to a private registry
  community.docker.docker_image:
    name: localhost:5000/myimages/sinatra
    tag: v1
    push: true
    load_path: my_sinatra.tar
    source: load

- name: Build image and with build args
  community.docker.docker_image:
    name: myimage
    build:
      path: /path/to/build/dir
      args:
        log_volume: /var/log/myapp
        listen_port: 8080
    source: build

- name: Build image using cache source
  community.docker.docker_image:
    name: myimage:latest
    build:
      path: /path/to/build/dir
      # Use as cache source for building myimage
      cache_from:
        - nginx:latest
        - alpine:3.8
    source: build
```

## [Return Values](docker_image_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **image**  dictionary | Image inspection results for the affected image.  Returned: success  Sample: `{}` |
| **stdout**  string  added in community.docker 1.0.0 | Docker build output when building an image.  Returned: success  Sample: `""` |

### Authors

- Pavel Antonov (@softzilla)
- Chris Houseknecht (@chouseknecht)
- Sorin Sbarnea (@ssbarnea)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
