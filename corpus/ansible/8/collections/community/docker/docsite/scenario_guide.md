---
collection: ansible
version: "8"
title: "Docker Guide"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docsite/scenario_guide.html
fetched_at: 2026-07-28T01:05:28+00:00
---
# Docker Guide

The [community.docker collection](https://galaxy.ansible.com/ui/repo/published/community/docker/) offers several modules and plugins for orchestrating Docker containers and Docker Swarm.

- [Requirements](scenario_guide.md#requirements)
- [Connecting to the Docker API](scenario_guide.md#connecting-to-the-docker-api)
- [Plain Docker daemon: images, networks, volumes, and containers](scenario_guide.md#plain-docker-daemon-images-networks-volumes-and-containers)
- [Docker Compose](scenario_guide.md#docker-compose)
- [Docker Machine](scenario_guide.md#docker-machine)
- [Docker stack](scenario_guide.md#docker-stack)
- [Docker Swarm](scenario_guide.md#docker-swarm)
- [Helpful links](scenario_guide.md#helpful-links)

## [Requirements](scenario_guide.md#id2)

Most of the modules and plugins in community.docker require the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/). The SDK needs to be installed on the machines where the modules and plugins are executed, and for the Python version(s) with which the modules and plugins are executed. You can use the [community.general.python_requirements_info module](../../general/python_requirements_info_module.md#ansible-collections-community-general-python-requirements-info-module) to make sure that the Docker SDK for Python is installed on the correct machine and for the Python version used by Ansible.

Note that plugins (inventory plugins and connection plugins) are always executed in the context of Ansible itself. If you use a plugin that requires the Docker SDK for Python, you need to install it on the machine running `ansible` or `ansible-playbook` and for the same Python interpreter used by Ansible. To see which Python is used, run `ansible --version`.

You can install the Docker SDK for Python for Python 3.6 or later as follows:

```bash
$ pip install docker
```

For Python 2.7, you need to use a version between 2.0.0 and 4.4.4 since the Python package for Docker removed support for Python 2.7 on 5.0.0. You can install the specific version of the Docker SDK for Python as follows:

```bash
$ pip install 'docker==4.4.4'
```

Note that the Docker SDK for Python was called `docker-py` on PyPi before version 2.0.0. Please avoid installing this really old version, and make sure to not install both `docker` and `docker-py`. Installing both will result in a broken installation. If this happens, Ansible will detect it and inform you about it. If that happens, you must uninstall both and reinstall the correct version. If in doubt, always install `docker` and never `docker-py`.

## [Connecting to the Docker API](scenario_guide.md#id3)

You can connect to a local or remote API using parameters passed to each task or by setting environment variables. The order of precedence is command line parameters and then environment variables. If neither a command line option nor an environment variable is found, Ansible uses the default value provided under [Parameters](scenario_guide.md#parameters).

### Parameters

Most plugins and modules can be configured by the following parameters:

> docker_host
> :   The URL or Unix socket path used to connect to the Docker API. Defaults to `unix://var/run/docker.sock`. To connect to a remote host, provide the TCP connection string (for example: `tcp://192.0.2.23:2376`). If TLS is used to encrypt the connection to the API, then the module will automatically replace ‘tcp’ in the connection URL with ‘https’.
>
> api_version
> :   The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by the Docker SDK for Python installed.
>
> timeout
> :   The maximum amount of time in seconds to wait on a response from the API. Defaults to 60 seconds.
>
> tls
> :   Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server. Defaults to `false`.
>
> validate_certs
> :   Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server. Default is `false`.
>
> cacert_path
> :   Use a CA certificate when performing server verification by providing the path to a CA certificate file.
>
> cert_path
> :   Path to the client’s TLS certificate file.
>
> key_path
> :   Path to the client’s TLS key file.
>
> tls_hostname
> :   When verifying the authenticity of the Docker Host server, provide the expected name of the server. Defaults to `localhost`.
>
> ssl_version
> :   Provide a valid SSL version number. The default value is determined by the Docker SDK for Python.

### Environment variables

You can also control how the plugins and modules connect to the Docker API by setting the following environment variables.

For plugins, they have to be set for the environment Ansible itself runs in. For modules, they have to be set for the environment the modules are executed in. For modules running on remote machines, the environment variables have to be set on that machine for the user used to execute the modules with.

DOCKER_HOST
:   The URL or Unix socket path used to connect to the Docker API.

DOCKER_API_VERSION
:   The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported
    by Docker SDK for Python.

DOCKER_TIMEOUT
:   The maximum amount of time in seconds to wait on a response from the API.

DOCKER_CERT_PATH
:   Path to the directory containing the client certificate, client key and CA certificate.

DOCKER_SSL_VERSION
:   Provide a valid SSL version number.

DOCKER_TLS
:   Secure the connection to the API by using TLS without verifying the authenticity of the Docker Host.

DOCKER_TLS_HOSTNAME
:   When verifying the authenticity of the Docker Host, uses this hostname to compare to the host’s certificate.

DOCKER_TLS_VERIFY
:   Secure the connection to the API by using TLS and verify the authenticity of the Docker Host.

## [Plain Docker daemon: images, networks, volumes, and containers](scenario_guide.md#id4)

For working with a plain Docker daemon, that is without Swarm, there are connection plugins, an inventory plugin, and several modules available:

> docker connection plugin
> :   The [community.docker.docker connection plugin](../docker_connection.md#ansible-collections-community-docker-docker-connection) uses the Docker CLI utility to connect to Docker containers and execute modules in them. It essentially wraps `docker exec` and `docker cp`. This connection plugin is supported by the [ansible.posix.synchronize module](../../../ansible/posix/synchronize_module.md#ansible-collections-ansible-posix-synchronize-module).
>
> docker_api connection plugin
> :   The [community.docker.docker_api connection plugin](../docker_api_connection.md#ansible-collections-community-docker-docker-api-connection) talks directly to the Docker daemon to connect to Docker containers and execute modules in them.
>
> docker_containers inventory plugin
> :   The [community.docker.docker_containers inventory plugin](../docker_containers_inventory.md#ansible-collections-community-docker-docker-containers-inventory) allows you to dynamically add Docker containers from a Docker Daemon to your Ansible inventory. See [Working with dynamic inventory](../../../../inventory_guide/intro_dynamic_inventory.md#dynamic-inventory) for details on dynamic inventories.
>
>     The [docker inventory script](https://github.com/ansible-community/contrib-scripts/blob/main/inventory/docker.py) is deprecated. Please use the inventory plugin instead. The inventory plugin has several compatibility options. If you need to collect Docker containers from multiple Docker daemons, you need to add every Docker daemon as an individual inventory source.
>
> docker_host_info module
> :   The [community.docker.docker_host_info module](../docker_host_info_module.md#ansible-collections-community-docker-docker-host-info-module) allows you to retrieve information on a Docker daemon, such as all containers, images, volumes, networks and so on.
>
> docker_login module
> :   The [community.docker.docker_login module](../docker_login_module.md#ansible-collections-community-docker-docker-login-module) allows you to log in and out of a remote registry, such as Docker Hub or a private registry. It provides similar functionality to the `docker login` and `docker logout` CLI commands.
>
> docker_prune module
> :   The [community.docker.docker_prune module](../docker_prune_module.md#ansible-collections-community-docker-docker-prune-module) allows you to prune no longer needed containers, images, volumes and so on. It provides similar functionality to the `docker prune` CLI command.
>
> docker_image module
> :   The [community.docker.docker_image module](../docker_image_module.md#ansible-collections-community-docker-docker-image-module) provides full control over images, including: build, pull, push, tag and remove.
>
> docker_image_load
> :   The [community.docker.docker_image_load module](../docker_image_load_module.md#ansible-collections-community-docker-docker-image-load-module) allows you to import one or multiple images from tarballs.
>
> docker_image_info module
> :   The [community.docker.docker_image_info module](../docker_image_info_module.md#ansible-collections-community-docker-docker-image-info-module) allows you to list and inspect images.
>
> docker_network module
> :   The [community.docker.docker_network module](../docker_network_module.md#ansible-collections-community-docker-docker-network-module) provides full control over Docker networks.
>
> docker_network_info module
> :   The [community.docker.docker_network_info module](../docker_network_info_module.md#ansible-collections-community-docker-docker-network-info-module) allows you to inspect Docker networks.
>
> docker_volume_info module
> :   The [community.docker.docker_volume_info module](../docker_volume_info_module.md#ansible-collections-community-docker-docker-volume-info-module) provides full control over Docker volumes.
>
> docker_volume module
> :   The [community.docker.docker_volume module](../docker_volume_module.md#ansible-collections-community-docker-docker-volume-module) allows you to inspect Docker volumes.
>
> docker_container module
> :   The [community.docker.docker_container module](../docker_container_module.md#ansible-collections-community-docker-docker-container-module) manages the container lifecycle by providing the ability to create, update, stop, start and destroy a Docker container.
>
> docker_container_copy_into
> :   The [community.docker.docker_container_copy_into module](../docker_container_copy_into_module.md#ansible-collections-community-docker-docker-container-copy-into-module) allows you to copy files from the control node into a container.
>
> docker_container_exec
> :   The [community.docker.docker_container_exec module](../docker_container_exec_module.md#ansible-collections-community-docker-docker-container-exec-module) allows you to execute commands in a running container.
>
> docker_container_info module
> :   The [community.docker.docker_container_info module](../docker_container_info_module.md#ansible-collections-community-docker-docker-container-info-module) allows you to inspect a Docker container.
>
> docker_plugin
> :   The [community.docker.docker_plugin module](../docker_plugin_module.md#ansible-collections-community-docker-docker-plugin-module) allows you to manage Docker plugins.

## [Docker Compose](scenario_guide.md#id5)

The [community.docker.docker_compose module](../docker_compose_module.md#ansible-collections-community-docker-docker-compose-module)
allows you to use your existing Docker compose files to orchestrate containers on a single Docker daemon or on Swarm.
Supports compose versions 1 and 2.

Next to Docker SDK for Python, you need to install [docker-compose](https://github.com/docker/compose) on the remote machines to use the module.

## [Docker Machine](scenario_guide.md#id6)

The [community.docker.docker_machine inventory plugin](../docker_machine_inventory.md#ansible-collections-community-docker-docker-machine-inventory) allows you to dynamically add Docker Machine hosts to your Ansible inventory.

## [Docker stack](scenario_guide.md#id7)

The [community.docker.docker_stack module](../docker_stack_module.md#ansible-collections-community-docker-docker-stack-module) module allows you to control Docker stacks. Information on stacks can be retrieved by the [community.docker.docker_stack_info module](../docker_stack_info_module.md#ansible-collections-community-docker-docker-stack-info-module), and information on stack tasks can be retrieved by the [community.docker.docker_stack_task_info module](../docker_stack_task_info_module.md#ansible-collections-community-docker-docker-stack-task-info-module).

## [Docker Swarm](scenario_guide.md#id8)

The community.docker collection provides multiple plugins and modules for managing Docker Swarms.

### Swarm management

One inventory plugin and several modules are provided to manage Docker Swarms:

> docker_swarm inventory plugin
> :   The [community.docker.docker_swarm inventory plugin](../docker_swarm_inventory.md#ansible-collections-community-docker-docker-swarm-inventory) allows you to dynamically add all Docker Swarm nodes to your Ansible inventory.
>
> docker_swarm module
> :   The [community.docker.docker_swarm module](../docker_swarm_module.md#ansible-collections-community-docker-docker-swarm-module) allows you to globally configure Docker Swarm manager nodes to join and leave swarms, and to change the Docker Swarm configuration.
>
> docker_swarm_info module
> :   The [community.docker.docker_swarm_info module](../docker_swarm_info_module.md#ansible-collections-community-docker-docker-swarm-info-module) allows you to retrieve information on Docker Swarm.
>
> docker_node module
> :   The [community.docker.docker_node module](../docker_node_module.md#ansible-collections-community-docker-docker-node-module) allows you to manage Docker Swarm nodes.
>
> docker_node_info module
> :   The [community.docker.docker_node_info module](../docker_node_info_module.md#ansible-collections-community-docker-docker-node-info-module) allows you to retrieve information on Docker Swarm nodes.

### Configuration management

The community.docker collection offers modules to manage Docker Swarm configurations and secrets:

> docker_config module
> :   The [community.docker.docker_config module](../docker_config_module.md#ansible-collections-community-docker-docker-config-module) allows you to create and modify Docker Swarm configs.
>
> docker_secret module
> :   The [community.docker.docker_secret module](../docker_secret_module.md#ansible-collections-community-docker-docker-secret-module) allows you to create and modify Docker Swarm secrets.

### Swarm services

Docker Swarm services can be created and updated with the [community.docker.docker_swarm_service module](../docker_swarm_service_module.md#ansible-collections-community-docker-docker-swarm-service-module), and information on them can be queried by the [community.docker.docker_swarm_service_info module](../docker_swarm_service_info_module.md#ansible-collections-community-docker-docker-swarm-service-info-module).

## [Helpful links](scenario_guide.md#id9)

Still using Dockerfile to build images? Check out [ansible-bender](https://github.com/ansible-community/ansible-bender), and start building images from your Ansible playbooks.

Use [Ansible Operator](https://learn.openshift.com/ansibleop/ansible-operator-overview/) to launch your docker-compose file on [OpenShift](https://www.okd.io/). Go from an app on your laptop to a fully scalable app in the cloud with Kubernetes in just a few moments.
