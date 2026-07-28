---
collection: ansible
version: "8"
title: "community.docker.docker_container_copy_into module – Copy a file into a Docker container"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_container_copy_into_module.html
fetched_at: 2026-07-28T01:43:43+00:00
---
# community.docker.docker_container_copy_into module – Copy a file into a Docker container

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
> see [Requirements](docker_container_copy_into_module.md#ansible-collections-community-docker-docker-container-copy-into-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_container_copy_into`.

New in community.docker 3.4.0

- [Synopsis](docker_container_copy_into_module.md#synopsis)
- [Requirements](docker_container_copy_into_module.md#requirements)
- [Parameters](docker_container_copy_into_module.md#parameters)
- [Attributes](docker_container_copy_into_module.md#attributes)
- [Notes](docker_container_copy_into_module.md#notes)
- [Examples](docker_container_copy_into_module.md#examples)
- [Return Values](docker_container_copy_into_module.md#return-values)

## [Synopsis](docker_container_copy_into_module.md#id1)

- Copy a file into a Docker container.
- Similar to `docker cp`.
- To copy files in a non-running container, you must provide the `owner_id` and `group_id` options. This is also necessary if the container does not contain a `/bin/sh` shell with an `id` tool.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](docker_container_copy_into_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- backports.ssl_match_hostname (when using TLS on Python 2)
- paramiko (when using SSH with `use_ssh_client=false`)
- pyOpenSSL (when using TLS)
- pywin32 (when using named pipes on Windows 32)
- requests

## [Parameters](docker_container_copy_into_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by this collection and the docker daemon.  If the value is not specified in the task, the value of environment variable [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `ca.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `cert.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `key.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **container**  string / required | The name of the container to copy files to. |
| **container_path**  string / required | Path to a file inside the Docker container.  Must be an absolute path. |
| **content**  string | The file’s content.  If you plan to provide binary data, provide it pre-encoded to base64, and set `content_is_b64=true`.  Mutually exclusive with `path`. One of `content` and `path` is required. |
| **content_is_b64**  boolean | If set to `true`, the content in `content` is assumed to be Base64 encoded and will be decoded before being used.  To use binary `content`, it is better to keep it Base64 encoded and let it be decoded by this option. Otherwise you risk the data to be interpreted as UTF-8 and corrupted.  **Choices:**   - `false` ← (default) - `true` |
| **debug**  boolean | Debug mode  **Choices:**   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"unix://var/run/docker.sock"` |
| **follow**  boolean | This flag indicates that filesystem links in the Docker container, if they exist, should be followed.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | If set to `true`, force writing the file (without performing any idempotency checks).  If set to `false`, only write the file if it does not exist on the target. If a filesystem object exists at the destination, the module will not do any change.  If this option is not specified, the module will be idempotent. To verify idempotency, it will try to get information on the filesystem object in the container, and if everything seems to match will download the file from the container to compare it to the file to upload.  **Choices:**   - `false` - `true` |
| **group_id**  integer | The group ID to use when writing the file to disk.  If provided, `owner_id` must also be provided.  If not provided, the module will try to determine the user and group ID for the current user in the container. This will only work if `/bin/sh` is present in the container and the `id` binary or shell builtin is available. Also the container must be running. |
| **local_follow**  boolean | This flag indicates that filesystem links in the source tree (where the module is executed), if they exist, should be followed.  **Choices:**   - `false` - `true` ← (default) |
| **mode**  integer | The file mode to use when writing the file to disk.  Will use the file’s mode from the source system if this option is not provided. |
| **owner_id**  integer | The owner ID to use when writing the file to disk.  If provided, `group_id` must also be provided.  If not provided, the module will try to determine the user and group ID for the current user in the container. This will only work if `/bin/sh` is present in the container and the `id` binary or shell builtin is available. Also the container must be running. |
| **path**  path | Path to a file on the managed node.  Mutually exclusive with `content`. One of `content` and `path` is required. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by [SSL Python module](https://docs.python.org/3/library/ssl.html).  If the value is not specified in the task, the value of environment variable [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION) will be used instead. |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if `validate_certs` is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.  Note that this option had a default value `localhost` in older versions. It was removed in community.docker 3.0.0. |
| **use_ssh_client**  boolean  *added in community.docker 1.5.0* | For SSH transports, use the `ssh` CLI tool instead of paramiko.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](docker_container_copy_into_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.docker.docker**, **docker** | Use `group/docker` or `group/community.docker.docker` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full**  Additional data will need to be transferred to compute diffs.  The module uses [the MAX_FILE_SIZE_FOR_DIFF ansible-core configuration](../../../reference_appendices/config.md#max-file-size-for-diff) to determine for how large files diffs should be computed. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](docker_container_copy_into_module.md#id5)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST), [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME), [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION), [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH), [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION), [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS), [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) and [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT). If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - This module does **not** use the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon. It uses code derived from the Docker SDK or Python that is included in this collection.

## [Examples](docker_container_copy_into_module.md#id6)

```yaml+jinja
- name: Copy a file into the container
  community.docker.docker_container_copy_into:
    container: mydata
    path: /home/user/data.txt
    container_path: /data/input.txt

- name: Copy a file into the container with owner, group, and mode set
  community.docker.docker_container_copy_into:
    container: mydata
    path: /home/user/bin/runme.o
    container_path: /bin/runme
    owner: 0  # root
    group: 0  # root
    mode: 0o755  # readable and executable by all users, writable by root
```

## [Return Values](docker_container_copy_into_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container_path**  string | The actual path in the container.  Can only be different from `container_path` when `follow=true`.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
