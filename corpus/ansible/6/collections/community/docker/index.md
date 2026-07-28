---
collection: ansible
version: "6"
title: "Community.Docker"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/docker/
fetched_at: 2026-07-28T00:24:47+00:00
---
# Community.Docker

Collection version 2.7.3

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Scenario Guide](index.md#scenario-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Modules and plugins for working with Docker

**Author:**

- Ansible Docker Working Group

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.docker)
[Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Scenario Guide](index.md#id3)

- [Docker Guide](docsite/scenario_guide.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.docker collection:

### Modules

- [current_container_facts module](current_container_facts_module.md#ansible-collections-community-docker-current-container-facts-module) – Return facts about whether the module runs in a Docker container
- [docker_compose module](docker_compose_module.md#ansible-collections-community-docker-docker-compose-module) – Manage multi-container Docker applications with Docker Compose.
- [docker_config module](docker_config_module.md#ansible-collections-community-docker-docker-config-module) – Manage docker configs.
- [docker_container module](docker_container_module.md#ansible-collections-community-docker-docker-container-module) – manage docker containers
- [docker_container_exec module](docker_container_exec_module.md#ansible-collections-community-docker-docker-container-exec-module) – Execute command in a docker container
- [docker_container_info module](docker_container_info_module.md#ansible-collections-community-docker-docker-container-info-module) – Retrieves facts about docker container
- [docker_host_info module](docker_host_info_module.md#ansible-collections-community-docker-docker-host-info-module) – Retrieves facts about docker host and lists of objects of the services.
- [docker_image module](docker_image_module.md#ansible-collections-community-docker-docker-image-module) – Manage docker images
- [docker_image_info module](docker_image_info_module.md#ansible-collections-community-docker-docker-image-info-module) – Inspect docker images
- [docker_image_load module](docker_image_load_module.md#ansible-collections-community-docker-docker-image-load-module) – Load docker image(s) from archives
- [docker_login module](docker_login_module.md#ansible-collections-community-docker-docker-login-module) – Log into a Docker registry.
- [docker_network module](docker_network_module.md#ansible-collections-community-docker-docker-network-module) – Manage Docker networks
- [docker_network_info module](docker_network_info_module.md#ansible-collections-community-docker-docker-network-info-module) – Retrieves facts about docker network
- [docker_node module](docker_node_module.md#ansible-collections-community-docker-docker-node-module) – Manage Docker Swarm node
- [docker_node_info module](docker_node_info_module.md#ansible-collections-community-docker-docker-node-info-module) – Retrieves facts about docker swarm node from Swarm Manager
- [docker_plugin module](docker_plugin_module.md#ansible-collections-community-docker-docker-plugin-module) – Manage Docker plugins
- [docker_prune module](docker_prune_module.md#ansible-collections-community-docker-docker-prune-module) – Allows to prune various docker objects
- [docker_secret module](docker_secret_module.md#ansible-collections-community-docker-docker-secret-module) – Manage docker secrets.
- [docker_stack module](docker_stack_module.md#ansible-collections-community-docker-docker-stack-module) – docker stack module
- [docker_stack_info module](docker_stack_info_module.md#ansible-collections-community-docker-docker-stack-info-module) – Return information on a docker stack
- [docker_stack_task_info module](docker_stack_task_info_module.md#ansible-collections-community-docker-docker-stack-task-info-module) – Return information of the tasks on a docker stack
- [docker_swarm module](docker_swarm_module.md#ansible-collections-community-docker-docker-swarm-module) – Manage Swarm cluster
- [docker_swarm_info module](docker_swarm_info_module.md#ansible-collections-community-docker-docker-swarm-info-module) – Retrieves facts about Docker Swarm cluster.
- [docker_swarm_service module](docker_swarm_service_module.md#ansible-collections-community-docker-docker-swarm-service-module) – docker swarm service
- [docker_swarm_service_info module](docker_swarm_service_info_module.md#ansible-collections-community-docker-docker-swarm-service-info-module) – Retrieves information about docker services from a Swarm Manager
- [docker_volume module](docker_volume_module.md#ansible-collections-community-docker-docker-volume-module) – Manage Docker volumes
- [docker_volume_info module](docker_volume_info_module.md#ansible-collections-community-docker-docker-volume-info-module) – Retrieve facts about Docker volumes

### Connection Plugins

- [docker connection](docker_connection.md#ansible-collections-community-docker-docker-connection) – Run tasks in docker containers
- [docker_api connection](docker_api_connection.md#ansible-collections-community-docker-docker-api-connection) – Run tasks in docker containers
- [nsenter connection](nsenter_connection.md#ansible-collections-community-docker-nsenter-connection) – execute on host running controller container

### Inventory Plugins

- [docker_containers inventory](docker_containers_inventory.md#ansible-collections-community-docker-docker-containers-inventory) – Ansible dynamic inventory plugin for Docker containers.
- [docker_machine inventory](docker_machine_inventory.md#ansible-collections-community-docker-docker-machine-inventory) – Docker Machine inventory source
- [docker_swarm inventory](docker_swarm_inventory.md#ansible-collections-community-docker-docker-swarm-inventory) – Ansible dynamic inventory plugin for Docker swarm nodes.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
