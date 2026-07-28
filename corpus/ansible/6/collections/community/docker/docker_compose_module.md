---
collection: ansible
version: "6"
title: "community.docker.docker_compose module – Manage multi-container Docker applications with Docker Compose."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/docker_compose_module.html
fetched_at: 2026-07-27T17:07:14+00:00
---
# community.docker.docker_compose module – Manage multi-container Docker applications with Docker Compose.

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
> see [Requirements](docker_compose_module.md#ansible-collections-community-docker-docker-compose-module-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_compose`.

- [Synopsis](docker_compose_module.md#synopsis)
- [Requirements](docker_compose_module.md#requirements)
- [Parameters](docker_compose_module.md#parameters)
- [Notes](docker_compose_module.md#notes)
- [Examples](docker_compose_module.md#examples)
- [Return Values](docker_compose_module.md#return-values)

## [Synopsis](docker_compose_module.md#id1)

- Uses Docker Compose to start, shutdown and scale services. **This module requires docker-compose < 2.0.0.**
- Configuration can be read from a `docker-compose.yml` or `docker-compose.yaml` file or inline using the *definition* option.
- See the examples for more details.
- Supports check mode.
- This module was called `docker_service` before Ansible 2.8. The usage did not change.

## [Requirements](docker_compose_module.md#id2)

The below requirements are needed on the host that executes this module.

- Docker API >= 1.20
- Docker SDK for Python: Please note that the [docker-py](https://pypi.org/project/docker-py/) Python module has been superseded by [docker](https://pypi.org/project/docker/) (see [here](https://github.com/docker/docker-py/issues/1310) for details). For Python 2.6, `docker-py` must be used. Otherwise, it is recommended to install the `docker` Python module. Note that both modules should \*not\* be installed at the same time. Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) >= 1.8.0 (use [docker-py](https://pypi.org/project/docker-py/) for Python 2.6)
- PyYAML >= 3.11
- docker-compose >= 1.7.0, < 2.0.0

## [Parameters](docker_compose_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  aliases: docker_api_version  string | The version of the Docker API running on the Docker Host.  Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.  If the value is not specified in the task, the value of environment variable `DOCKER_API_VERSION` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"auto"` |
| **build**  boolean | Use with *state* `present` to always build images prior to starting the application.  Same as running `docker-compose build` with the pull option.  Images will only be rebuilt if Docker detects a change in the Dockerfile or build directory contents.  Use the *nocache* option to ignore the image cache when performing the build.  If an existing image is replaced, services using the image will be recreated unless *recreate* is `never`.  Choices:   - `false` ← (default) - `true` |
| **ca_cert**  aliases: tls_ca_cert, cacert_path  path | Use a CA certificate when performing server verification by providing the path to a CA certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `ca.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_cert**  aliases: tls_client_cert, cert_path  path | Path to the client’s TLS certificate file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `cert.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **client_key**  aliases: tls_client_key, key_path  path | Path to the client’s TLS key file.  If the value is not specified in the task and the environment variable `DOCKER_CERT_PATH` is set, the file `key.pem` from the directory specified in the environment variable `DOCKER_CERT_PATH` will be used. |
| **debug**  boolean | Debug mode  Choices:   - `false` ← (default) - `true` |
| **definition**  dictionary | Compose file describing one or more services, networks and volumes.  Mutually exclusive with *project_src* and *files*. |
| **dependencies**  boolean | When *state* is `present` specify whether or not to include linked services.  Choices:   - `false` - `true` ← (default) |
| **docker_host**  aliases: docker_url  string | The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, `tcp://192.0.2.23:2376`. If TLS is used to encrypt the connection, the module will automatically replace `tcp` in the connection URL with `https`.  If the value is not specified in the task, the value of environment variable `DOCKER_HOST` will be used instead. If the environment variable is not set, the default value will be used.  Default: `"unix://var/run/docker.sock"` |
| **env_file**  path  added in community.docker 1.9.0 | By default environment files are loaded from a `.env` file located directly under the *project_src* directory.  *env_file* can be used to specify the path of a custom environment file instead.  The path is relative to the *project_src* directory.  Requires `docker-compose` version 1.25.0 or greater.  Note: `docker-compose` versions `<=1.28` load the env file from the current working directory of the `docker-compose` command rather than *project_src*. |
| **files**  list / elements=path | List of Compose file names relative to *project_src*. Overrides `docker-compose.yml` or `docker-compose.yaml`.  Files are loaded and merged in the order given. |
| **hostname_check**  boolean | Whether or not to check the Docker daemon’s hostname against the name provided in the client certificate.  Choices:   - `false` ← (default) - `true` |
| **nocache**  boolean | Use with the *build* option to ignore the cache during the image build process.  Choices:   - `false` ← (default) - `true` |
| **profiles**  list / elements=string  added in community.docker 1.8.0 | List of profiles to enable when starting services.  Equivalent to `docker-compose --profile`.  Requires `docker-compose` version 1.28.0 or greater. |
| **project_name**  string | Provide a project name. If not provided, the project name is taken from the basename of *project_src*.  Required when *definition* is provided. |
| **project_src**  path | Path to a directory containing a `docker-compose.yml` or `docker-compose.yaml` file.  Mutually exclusive with *definition*.  Required when no *definition* is provided. |
| **pull**  boolean | Use with *state* `present` to always pull images prior to starting the application.  Same as running `docker-compose pull`.  When a new image is pulled, services using the image will be recreated unless *recreate* is `never`.  Choices:   - `false` ← (default) - `true` |
| **recreate**  string | By default containers will be recreated when their configuration differs from the service definition.  Setting to `never` ignores configuration differences and leaves existing containers unchanged.  Setting to `always` forces recreation of all existing containers.  Choices:   - `"always"` - `"never"` - `"smart"` ← (default) |
| **remove_images**  string | Use with *state* `absent` to remove all images or only local images.  Choices:   - `"all"` - `"local"` |
| **remove_orphans**  boolean | Remove containers for services not defined in the Compose file.  Choices:   - `false` ← (default) - `true` |
| **remove_volumes**  boolean | Use with *state* `absent` to remove data volumes.  Choices:   - `false` ← (default) - `true` |
| **restarted**  boolean | Use with *state* `present` to restart all containers defined in the Compose file.  If *services* is defined, only the containers listed there will be restarted.  Choices:   - `false` ← (default) - `true` |
| **scale**  dictionary | When *state* is `present` scale services. Provide a dictionary of key/value pairs where the key is the name of the service and the value is an integer count for the number of containers. |
| **services**  list / elements=string | When *state* is `present` run `docker-compose up` resp. `docker-compose stop` (with *stopped*) resp. `docker-compose restart` (with *restarted*) on a subset of services.  If empty, which is the default, the operation will be performed on all services defined in the Compose file (or inline *definition*). |
| **ssl_version**  string | Provide a valid SSL version number. Default value determined by ssl.py module.  If the value is not specified in the task, the value of environment variable `DOCKER_SSL_VERSION` will be used instead. |
| **state**  string | Desired state of the project.  Specifying `present` is the same as running `docker-compose up` resp. `docker-compose stop` (with *stopped*) resp. `docker-compose restart` (with *restarted*).  Specifying `absent` is the same as running `docker-compose down`.  Choices:   - `"absent"` - `"present"` ← (default) |
| **stopped**  boolean | Use with *state* `present` to stop all containers defined in the Compose file.  If *services* is defined, only the containers listed there will be stopped.  Requires `docker-compose` version 1.17.0 or greater for full support. For older versions, the services will first be started and then stopped when the service is supposed to be created as stopped.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | Timeout in seconds for container shutdown when attached or when containers are already running.  By default `compose` will use a `10s` timeout unless `default_grace_period` is defined for a particular service in the *project_src*. |
| **tls**  boolean | Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Note that if *validate_certs* is set to `true` as well, it will take precedence.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |
| **tls_hostname**  string | When verifying the authenticity of the Docker Host server, provide the expected name of the server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_HOSTNAME` will be used instead. If the environment variable is not set, the default value will be used.  The current default value is `localhost`. This default is deprecated and will change in community.docker 2.0.0 to be a value computed from *docker_host*. Explicitly specify `localhost` to make sure this value will still be used, and to disable the deprecation message which will be shown otherwise. |
| **use_ssh_client**  boolean  added in community.docker 1.5.0 | Currently ignored for this module, but might suddenly be supported later on.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  aliases: tls_verify  boolean | Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.  If the value is not specified in the task, the value of environment variable `DOCKER_TLS_VERIFY` will be used instead. If the environment variable is not set, the default value will be used.  Choices:   - `false` ← (default) - `true` |

## [Notes](docker_compose_module.md#id4)

> **Note:**
>
> - Connect to the Docker daemon by providing parameters with each task or by defining environment variables. You can define `DOCKER_HOST`, `DOCKER_TLS_HOSTNAME`, `DOCKER_API_VERSION`, `DOCKER_CERT_PATH`, `DOCKER_SSL_VERSION`, `DOCKER_TLS`, `DOCKER_TLS_VERIFY` and `DOCKER_TIMEOUT`. If you are using docker machine, run the script shipped with the product that sets up the environment. It will set these variables for you. See <https://docs.docker.com/machine/reference/env/> for more details.
> - When connecting to Docker daemon with TLS, you might need to install additional Python packages. For the Docker SDK for Python, version 2.4 or newer, this can be done by installing `docker[tls]` with [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - Note that the Docker SDK for Python only allows to specify the path to the Docker configuration for very few functions. In general, it will use `$HOME/.docker/config.json` if the `DOCKER_CONFIG` environment variable is not specified, and use `$DOCKER_CONFIG/config.json` otherwise.
> - This module uses the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) to communicate with the Docker daemon.

## [Examples](docker_compose_module.md#id5)

```yaml+jinja
# Examples use the django example at https://docs.docker.com/compose/django. Follow it to create the
# flask directory

- name: Run using a project directory
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Tear down existing services
      community.docker.docker_compose:
        project_src: flask
        state: absent

    - name: Create and start services
      community.docker.docker_compose:
        project_src: flask
      register: output

    - ansible.builtin.debug:
        var: output

    - name: Run `docker-compose up` again
      community.docker.docker_compose:
        project_src: flask
        build: false
      register: output

    - ansible.builtin.debug:
        var: output

    - ansible.builtin.assert:
        that: not output.changed

    - name: Stop all services
      community.docker.docker_compose:
        project_src: flask
        build: false
        stopped: true
      register: output

    - ansible.builtin.debug:
        var: output

    - ansible.builtin.assert:
        that:
          - "not web.flask_web_1.state.running"
          - "not db.flask_db_1.state.running"

    - name: Restart services
      community.docker.docker_compose:
        project_src: flask
        build: false
        restarted: true
      register: output

    - ansible.builtin.debug:
        var: output

    - ansible.builtin.assert:
        that:
          - "web.flask_web_1.state.running"
          - "db.flask_db_1.state.running"

- name: Scale the web service to 2
  hosts: localhost
  gather_facts: false
  tasks:
    - community.docker.docker_compose:
        project_src: flask
        scale:
          web: 2
      register: output

    - ansible.builtin.debug:
        var: output

- name: Run with inline Compose file version 2
  # https://docs.docker.com/compose/compose-file/compose-file-v2/
  hosts: localhost
  gather_facts: false
  tasks:
    - community.docker.docker_compose:
        project_src: flask
        state: absent

    - community.docker.docker_compose:
        project_name: flask
        definition:
          version: '2'
          services:
            db:
              image: postgres
            web:
              build: "{{ playbook_dir }}/flask"
              command: "python manage.py runserver 0.0.0.0:8000"
              volumes:
                - "{{ playbook_dir }}/flask:/code"
              ports:
                - "8000:8000"
              depends_on:
                - db
      register: output

    - ansible.builtin.debug:
        var: output

    - ansible.builtin.assert:
        that:
          - "web.flask_web_1.state.running"
          - "db.flask_db_1.state.running"

- name: Run with inline Compose file version 1
  # https://docs.docker.com/compose/compose-file/compose-file-v1/
  hosts: localhost
  gather_facts: false
  tasks:
    - community.docker.docker_compose:
        project_src: flask
        state: absent

    - community.docker.docker_compose:
        project_name: flask
        definition:
            db:
              image: postgres
            web:
              build: "{{ playbook_dir }}/flask"
              command: "python manage.py runserver 0.0.0.0:8000"
              volumes:
                - "{{ playbook_dir }}/flask:/code"
              ports:
                - "8000:8000"
              links:
                - db
      register: output

    - ansible.builtin.debug:
        var: output

    - ansible.builtin.assert:
        that:
          - "web.flask_web_1.state.running"
          - "db.flask_db_1.state.running"
```

## [Return Values](docker_compose_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  complex | Provides the actions to be taken on each service as determined by compose.  Returned: when in check mode or *debug* is `true` |
| **service_name**  complex | Name of the service.  Returned: always |
| **action**  list / elements=string | A descriptive name of the action to be performed on the service’s containers.  Returned: always |
| **id**  string | the container’s long ID  Returned: always |
| **name**  string | the container’s name  Returned: always |
| **short_id**  string | the container’s short ID  Returned: always |
| **built_image**  complex | Provides image details when a new image is built for the service.  Returned: on image build |
| **id**  string | image hash  Returned: always |
| **name**  string | name of the image  Returned: always |
| **pulled_image**  complex | Provides image details when a new image is pulled for the service.  Returned: on image pull |
| **id**  string | image hash  Returned: always |
| **name**  string | name of the image  Returned: always |
| **services**  complex | A dictionary mapping the service’s name to a dictionary of containers.  Returned: success |
| **container_name**  complex | Name of the container. Format is `project_service_#`.  Returned: success |
| **cmd**  list / elements=string | One or more commands to be executed in the container.  Returned: success  Sample: `["postgres"]` |
| **image**  string | Name of the image from which the container was built.  Returned: success  Sample: `"postgres"` |
| **labels**  dictionary | Meta data assigned to the container.  Returned: success  Sample: `{"...": null}` |
| **networks**  list / elements=dictionary | Contains a dictionary for each network to which the container is a member.  Returned: success |
| **aliases**  list / elements=string | Aliases assigned to the container by the network.  Returned: success  Sample: `["db"]` |
| **globalIPv6**  string | IPv6 address assigned to the container.  Returned: success  Sample: `""` |
| **globalIPv6PrefixLen**  integer | IPv6 subnet length.  Returned: success  Sample: `0` |
| **IPAddress**  string | The IP address assigned to the container.  Returned: success  Sample: `"172.17.0.2"` |
| **IPPrefixLen**  integer | Number of bits used by the subnet.  Returned: success  Sample: `16` |
| **links**  list / elements=string | List of container names to which this container is linked.  Returned: success |
| **macAddress**  string | Mac Address assigned to the virtual NIC.  Returned: success  Sample: `"02:42:ac:11:00:02"` |
| **state**  dictionary | Information regarding the current disposition of the container.  Returned: success |
| **running**  boolean | Whether or not the container is up with a running process.  Returned: success  Sample: `true` |
| **status**  string | Description of the running state.  Returned: success  Sample: `"running"` |

### Authors

- Chris Houseknecht (@chouseknecht)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-docker)
