---
collection: ansible
version: "6"
title: "community.docker.docker_secret module – Manage docker secrets."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_secret_module.html
fetched_at: 2026-07-27T17:07:25+00:00
---
# community.docker.docker_secret module – Manage docker secrets.

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
> see [Requirements](docker_secret_module.md#ansible-collections-community-docker-docker-secret-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_secret`.

- [Synopsis](docker_secret_module.md#synopsis)
- [Requirements](docker_secret_module.md#requirements)
- [Parameters](docker_secret_module.md#parameters)
- [Notes](docker_secret_module.md#notes)
- [Examples](docker_secret_module.md#examples)
- [Return Values](docker_secret_module.md#return-values)

## [Synopsis](docker_secret_module.md#id1)

- Create and remove Docker secrets in a Swarm environment. Similar to `docker secret create` and `docker secret rm`.
- Adds to the metadata of new secrets `ansible_key`, an encrypted hash representation of the data, which is then used in future runs to test if a secret has changed. If `ansible_key` is not present, then a secret will not be updated unless the *force* option is set.
- Updates to secrets are performed by removing the secret and creating it again.

## [Requirements](docker_secret_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.25
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). This module does \*not\* work with docker-py.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 2.1.0
- Python >= 2.7

## [Parameters](docker_secret_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **data**  string | The value of the secret.  Mutually exclusive with *data_src*. One of *data* and *data_src* is required if *state=present*. |
| **data_is_b64**  boolean | If set to `true`, the data is assumed to be Base64 encoded and will be decoded before being used.  To use binary *data*, it is better to keep it Base64 encoded and let it be decoded by this option.  Choices:   - `false` ← (default) - `true` |
| **data_src**  path  added in community.docker 1.10.0 | The file on the target from which to read the secret.  Mutually exclusive with *data*. One of *data* and *data_src* is required if *state=present*. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **force**  boolean | Use with state `present` to always remove and recreate an existing secret.  If `true`, an existing secret will be replaced, even if it has not changed.  Choices:   - `false` ← (default) - `true` |
| **labels**  dictionary | A map of key:value meta data, where both key and value are expected to be strings.  If new meta data is provided, or existing meta data is modified, the secret will be updated by removing it and creating it again. |
| **name**  string / required | The name of the secret. |
| **rolling_versions**  boolean  added in community.docker 2.2.0 | If set to `true`, secrets are created with an increasing version number appended to their name.  Adds a label containing the version number to the managed secrets with the name `ansible_version`.  Choices:   - `false` ← (default) - `true` |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **state**  string | Set to `present`, if the secret should exist, and `absent`, if it should not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | The maximum amount of time in seconds to wait on a response from the API.  If the value is not specified in the task, the value of environment variable `DOCKER_TIMEOUT` will be used instead. If the environment variable is not set, the default value will be used.  Default: `60` |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | For SSH transports, use the `ssh` CLI tool instead of paramiko.  Requires Docker SDK for Python 4.4.0 or newer.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **versions_to_keep**  integer  added in community.docker 2.2.0 | When using *rolling_versions*, the number of old versions of the secret to keep.  Extraneous old secrets are deleted after the new one is created.  Set to `-1` to keep everything or to `0` or `1` to keep only the current one.  Default: `5` |

## [Notes](docker_secret_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_secret_module.md#id5)

```yaml+jinja
- name: Create secret foo (from a file on the control machine)
  community.docker.docker_secret:
    name: foo
    # If the file is JSON or binary, Ansible might modify it (because
    # it is first decoded and later re-encoded). Base64-encoding the
    # file directly after reading it prevents this to happen.
    data: "{{ lookup('file', '/path/to/secret/file') | b64encode }}"
    data_is_b64: true
    state: present

- name: Create secret foo (from a file on the target machine)
  community.docker.docker_secret:
    name: foo
    data_src: /path/to/secret/file
    state: present

- name: Change the secret data
  community.docker.docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: baz
      one: '1'
    state: present

- name: Add a new label
  community.docker.docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: baz
      one: '1'
      # Adding a new label will cause a remove/create of the secret
      two: '2'
    state: present

- name: No change
  community.docker.docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: baz
      one: '1'
      # Even though 'two' is missing, there is no change to the existing secret
    state: present

- name: Update an existing label
  community.docker.docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: monkey   # Changing a label will cause a remove/create of the secret
      one: '1'
    state: present

- name: Force the removal/creation of the secret
  community.docker.docker_secret:
    name: foo
    data: Goodnight everyone!
    force: true
    state: present

- name: Remove secret foo
  community.docker.docker_secret:
    name: foo
    state: absent
```

## [Return Values](docker_secret_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **secret_id**  string | The ID assigned by Docker to the secret object.  Returned: success and *state* is `present`  Sample: `"hzehrmyjigmcp2gb6nlhmjqcv"` |
| **secret_name**  string  added in community.docker 2.2.0 | The name of the created secret object.  Returned: success and *state* is `present`  Sample: `"awesome_secret"` |

### Authors

- Chris Houseknecht (@chouseknecht)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
