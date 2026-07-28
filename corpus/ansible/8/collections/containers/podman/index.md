---
collection: ansible
version: "8"
title: "Containers.Podman"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/index.html
fetched_at: 2026-07-28T01:02:27+00:00
---
# Containers.Podman

Collection version 1.11.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Podman container Ansible modules

**Authors:**

- Sagi Shnaidman <[sshnaidm@redhat.com](mailto:sshnaidm%40redhat.com)>
- Ansible team

**Supported ansible-core versions:**

- 2.8 or newer

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)

## [Plugin Index](index.md#id2)

These are the plugins in the containers.podman collection:

### Modules

- [podman_container module](podman_container_module.md#ansible-collections-containers-podman-podman-container-module) – Manage podman containers
- [podman_container_exec module](podman_container_exec_module.md#ansible-collections-containers-podman-podman-container-exec-module) – Executes a command in a running container.
- [podman_container_info module](podman_container_info_module.md#ansible-collections-containers-podman-podman-container-info-module) – Gather facts about containers using podman
- [podman_containers module](podman_containers_module.md#ansible-collections-containers-podman-podman-containers-module) – Manage podman containers in a batch
- [podman_export module](podman_export_module.md#ansible-collections-containers-podman-podman-export-module) – Export a podman container
- [podman_generate_systemd module](podman_generate_systemd_module.md#ansible-collections-containers-podman-podman-generate-systemd-module) – Generate systemd unit from a pod or a container
- [podman_image module](podman_image_module.md#ansible-collections-containers-podman-podman-image-module) – Pull images for use by podman
- [podman_image_info module](podman_image_info_module.md#ansible-collections-containers-podman-podman-image-info-module) – Gather info about images using podman
- [podman_import module](podman_import_module.md#ansible-collections-containers-podman-podman-import-module) – Import Podman container from a tar file.
- [podman_load module](podman_load_module.md#ansible-collections-containers-podman-podman-load-module) – Load image from a tar file.
- [podman_login module](podman_login_module.md#ansible-collections-containers-podman-podman-login-module) – Login to a container registry using podman
- [podman_login_info module](podman_login_info_module.md#ansible-collections-containers-podman-podman-login-info-module) – Return the logged-in user if any for a given registry
- [podman_logout module](podman_logout_module.md#ansible-collections-containers-podman-podman-logout-module) – Log out of a container registry using podman
- [podman_network module](podman_network_module.md#ansible-collections-containers-podman-podman-network-module) – Manage podman networks
- [podman_network_info module](podman_network_info_module.md#ansible-collections-containers-podman-podman-network-info-module) – Gather info about podman networks
- [podman_play module](podman_play_module.md#ansible-collections-containers-podman-podman-play-module) – Play kubernetes YAML file using podman
- [podman_pod module](podman_pod_module.md#ansible-collections-containers-podman-podman-pod-module) – Manage Podman pods
- [podman_pod_info module](podman_pod_info_module.md#ansible-collections-containers-podman-podman-pod-info-module) – Gather info about podman pods
- [podman_prune module](podman_prune_module.md#ansible-collections-containers-podman-podman-prune-module) – Allows to prune various podman objects
- [podman_runlabel module](podman_runlabel_module.md#ansible-collections-containers-podman-podman-runlabel-module) – Run given label from given image
- [podman_save module](podman_save_module.md#ansible-collections-containers-podman-podman-save-module) – Saves podman image to tar file
- [podman_secret module](podman_secret_module.md#ansible-collections-containers-podman-podman-secret-module) – Manage podman secrets
- [podman_tag module](podman_tag_module.md#ansible-collections-containers-podman-podman-tag-module) – Add an additional name to a local image
- [podman_volume module](podman_volume_module.md#ansible-collections-containers-podman-podman-volume-module) – Manage Podman volumes
- [podman_volume_info module](podman_volume_info_module.md#ansible-collections-containers-podman-podman-volume-info-module) – Gather info about podman volumes

### Become Plugins

- [podman_unshare become](podman_unshare_become.md#ansible-collections-containers-podman-podman-unshare-become) – Run tasks using podman unshare

### Connection Plugins

- [buildah connection](buildah_connection.md#ansible-collections-containers-podman-buildah-connection) – Interact with an existing buildah container
- [podman connection](podman_connection.md#ansible-collections-containers-podman-podman-connection) – Interact with an existing podman container

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
