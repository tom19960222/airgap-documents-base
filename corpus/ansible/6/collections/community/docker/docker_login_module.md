---
collection: ansible
version: "6"
title: "community.docker.docker_login module – Log into a Docker registry."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_login_module.html
fetched_at: 2026-07-27T17:07:20+00:00
---
# community.docker.docker_login module – Log into a Docker registry.

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
> see [Requirements](docker_login_module.md#ansible-collections-community-docker-docker-login-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_login`.

- [Synopsis](docker_login_module.md#synopsis)
- [Requirements](docker_login_module.md#requirements)
- [Parameters](docker_login_module.md#parameters)
- [Notes](docker_login_module.md#notes)
- [Examples](docker_login_module.md#examples)
- [Return Values](docker_login_module.md#return-values)

## [Synopsis](docker_login_module.md#id1)

- Provides functionality similar to the `docker login` command.
- Authenticate with a docker registry and add the credentials to your local Docker config file respectively the credentials store associated to the registry. Adding the credentials to the config files resp. the credential store allows future connections to the registry using tools such as Ansible’s Docker modules, the Docker CLI and Docker SDK for Python without needing to provide credentials.
- Running in check mode will perform the authentication without updating the config file.

## [Requirements](docker_login_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.20
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.8.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)
- Python bindings for docker credentials store API >= 0.2.1 (use [docker-pycreds](https://pypi.org/project/docker-pycreds/) when using Docker SDK for Python < 4.0.0)

## [Parameters](docker_login_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **config_path**  aliases: dockercfg_path  path | Custom path to the Docker CLI configuration file.  Default: `"~/.docker/config.json"` |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **password**  string | The plaintext password for the registry account.  Required when *state* is `present`. |
| **reauthorize**  aliases: reauth  boolean | Refresh existing authentication found in the configuration file.  Choices:   - `false` ← (default) - `true` |
| **registry_url**  aliases: registry, url  string | The registry URL.  Default: `"https://index.docker.io/v1/"` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **state**  string | This controls the current state of the user. `present` will login in a user, `absent` will log them out.  To logout you only need the registry server, which defaults to DockerHub.  Before 2.1 you could ONLY log in.  Docker does not support ‘logout’ with a custom config file.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **username**  string | The username for the registry account.  Required when *state* is `present`. |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_login_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_login_module.md#id5)

```yaml+jinja
- name: Log into DockerHub
  community.docker.docker_login:
    username: docker
    password: rekcod

- name: Log into private registry and force re-authorization
  community.docker.docker_login:
    registry_url: your.private.registry.io
    username: yourself
    password: secrets3
    reauthorize: true

- name: Log into DockerHub using a custom config file
  community.docker.docker_login:
    username: docker
    password: rekcod
    config_path: /tmp/.mydockercfg

- name: Log out of DockerHub
  community.docker.docker_login:
    state: absent
```

## [Return Values](docker_login_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **login_results**  dictionary | Results from the login.  Returned: when state=’present’  Sample: `{"serveraddress": "localhost:5000", "username": "testuser"}` |

### Authors

- Olaf Kilian (@olsaki)
- Chris Houseknecht (@chouseknecht)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
