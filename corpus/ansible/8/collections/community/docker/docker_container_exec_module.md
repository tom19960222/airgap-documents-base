---
collection: ansible
version: "8"
title: "community.docker.docker_container_exec module – Execute command in a docker container"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_container_exec_module.html
fetched_at: 2026-07-28T01:43:44+00:00
---
# community.docker.docker_container_exec module – Execute command in a docker container

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
> see [Requirements](docker_container_exec_module.md#ansible-collections-community-docker-docker-container-exec-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_container_exec`.

New in community.docker 1.5.0

- [Synopsis](docker_container_exec_module.md#synopsis)
- [Requirements](docker_container_exec_module.md#requirements)
- [Parameters](docker_container_exec_module.md#parameters)
- [Attributes](docker_container_exec_module.md#attributes)
- [Notes](docker_container_exec_module.md#notes)
- [Examples](docker_container_exec_module.md#examples)
- [Return Values](docker_container_exec_module.md#return-values)

## [Synopsis](docker_container_exec_module.md#id1)

- Executes a command in a Docker container.

## [Requirements](docker_container_exec_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- backports.ssl_match_hostname (when using TLS on Python 2)
- paramiko (when using SSH with `use_ssh_client=false`)
- pyOpenSSL (when using TLS)
- pywin32 (when using named pipes on Windows 32)
- requests

## [Parameters](docker_container_exec_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by this collection and the docker daemon.  If the value is not specified in the task, the value of environment variable [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"auto"` |
| **argv**  list / elements=string | The command to execute.  Since this is a list of arguments, no quoting is needed.  Exactly one of `argv` or `command` must be specified. |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `ca.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **chdir**  string | The directory to run the command in. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `cert.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) is set, the file `key.pem` from the directory specified in the environment variable [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH) will be used. |
| **command**  string | The command to execute.  Exactly one of `argv` or `command` must be specified. |
| **container**  string / required | The name of the container to execute the command in. |
| **debug**  boolean | Debug mode  **Choices:**   - `false` ← (default) - `true` |
| **detach**  boolean  *added in community.docker 2.1.0* | Whether to run the command synchronously (`detach=false`, default) or asynchronously (`detach=true`).  If set to `true`, `stdin` cannot be provided, and the return values `stdout`, `stderr`, and `rc` are not returned.  **Choices:**   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `"unix://var/run/docker.sock"` |
| **env**  dictionary  *added in community.docker 2.1.0* | Dictionary of environment variables with their respective values to be passed to the command ran inside the container.  Values which might be parsed as numbers, booleans or other types by the YAML parser must be quoted (for example `"true"`) in order to avoid data loss.  Please note that if you are passing values in with Jinja2 templates, like `"{{ value }}"`, you need to add `| string` to prevent Ansible to convert strings such as `"true"` back to booleans. The correct way is to use `"{{ value | string }}"`. |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by [SSL Python module](https://docs.python.org/3/library/ssl.html).  If the value is not specified in the task, the value of environment variable [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION) will be used instead. |
| **stdin**  string | Set the stdin of the command directly to the specified value.  Can only be used if `detach=false`. |
| **stdin_add_newline**  boolean | If set to `true`, appends a newline to `stdin`.  **Choices:**   - `false` - `true` ← (default) |
| **strip_empty_ends**  boolean | Strip empty lines from the end of stdout/stderr in result.  **Choices:**   - `false` - `true` ← (default) |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.  **Default:** `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if `validate_certs` is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.  Note that this option had a default value `localhost` in older versions. It was removed in community.docker 3.0.0. |
| **tty**  boolean | Whether to allocate a TTY.  **Choices:**   - `false` ← (default) - `true` |
| **use_ssh_client**  boolean  *added in community.docker 1.5.0* | For SSH transports, use the `ssh` CLI tool instead of paramiko.  **Choices:**   - `false` ← (default) - `true` |
| **user**  string | If specified, the user to execute this command with. |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](docker_container_exec_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action groups:** **community.docker.docker**, **docker** | Use `group/docker` or `group/community.docker.docker` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](docker_container_exec_module.md#id5)

> **Note:**
>
> - Does not support `check_mode`.
> - Does **not work with TCP TLS sockets** when using `stdin`. This is caused by the inability to send `close_notify` without closing the connection with Python’s `SSLSocket`s. See <https://github.com/ansible-collections/community.docker/issues/605> for more information.
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define [`DOCKER_HOST`](docsite/scenario_guide.md#envvar-DOCKER_HOST), [`DOCKER_TLS_HOSTNAME`](docsite/scenario_guide.md#envvar-DOCKER_TLS_HOSTNAME), [`DOCKER_API_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_API_VERSION), [`DOCKER_CERT_PATH`](docsite/scenario_guide.md#envvar-DOCKER_CERT_PATH), [`DOCKER_SSL_VERSION`](docsite/scenario_guide.md#envvar-DOCKER_SSL_VERSION), [`DOCKER_TLS`](docsite/scenario_guide.md#envvar-DOCKER_TLS), [`DOCKER_TLS_VERIFY`](docsite/scenario_guide.md#envvar-DOCKER_TLS_VERIFY) and [`DOCKER_TIMEOUT`](docsite/scenario_guide.md#envvar-DOCKER_TIMEOUT). If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - This module does **not** use the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon. It uses code derived from the Docker SDK or Python that is included in this collection.

## [Examples](docker_container_exec_module.md#id6)

```yaml+jinja
- name: Run a simple command (command)
  community.docker.docker_container_exec:
    container: foo
    command: /bin/bash -c "ls -lah"
    chdir: /root
  register: result

- name: Print stdout
  ansible.builtin.debug:
    var: result.stdout

- name: Run a simple command (argv)
  community.docker.docker_container_exec:
    container: foo
    argv:
      - /bin/bash
      - "-c"
      - "ls -lah > /dev/stderr"
    chdir: /root
  register: result

- name: Print stderr lines
  ansible.builtin.debug:
    var: result.stderr_lines
```

## [Return Values](docker_container_exec_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exec_id**  string  *added in community.docker 2.1.0* | The execution ID of the command.  **Returned:** success and `detach=true`  **Sample:** `"249d9e3075655baf705ed8f40488c5e9434049cf3431976f1bfdb73741c574c5"` |
| **rc**  integer | The exit code of the command.  **Returned:** success and `detach=false`  **Sample:** `0` |
| **stderr**  string | The standard error output of the container command.  **Returned:** success and `detach=false` |
| **stdout**  string | The standard output of the container command.  **Returned:** success and `detach=false` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
