---
collection: ansible
version: "8"
title: "containers.podman.podman_play module – Play kubernetes YAML file using podman"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_play_module.html
fetched_at: 2026-07-28T02:03:13+00:00
---
# containers.podman.podman_play module – Play kubernetes YAML file using podman

> **Note:**
>
> This module is part of the [containers.podman collection](https://galaxy.ansible.com/ui/repo/published/containers/podman/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
> You need further requirements to be able to use this module,
> see [Requirements](podman_play_module.md#ansible-collections-containers-podman-podman-play-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_play`.

- [Synopsis](podman_play_module.md#synopsis)
- [Requirements](podman_play_module.md#requirements)
- [Parameters](podman_play_module.md#parameters)
- [Examples](podman_play_module.md#examples)

## [Synopsis](podman_play_module.md#id1)

- The module reads in a structured file of Kubernetes YAML. It will then recreate the pod and containers described in the YAML.

## [Requirements](podman_play_module.md#id2)

The below requirements are needed on the host that executes this module.

- Podman installed on host

## [Parameters](podman_play_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authfile**  path | Path of the authentication file. Default is ${XDG_RUNTIME_DIR}/containers/auth.json, which is set using podman login. If the authorization state is not found there, $HOME/.docker/config.json is checked, which is set using docker login. Note - You can also override the default path of the authentication file by setting the REGISTRY_AUTH_FILE environment variable. export REGISTRY_AUTH_FILE=path |
| **build**  boolean | Build images even if they are found in the local storage.  It is required to exist subdirectories matching the image names to be build.  **Choices:**   - `false` - `true` |
| **cert_dir**  path | Use certificates at path (\*.crt, \*.cert, \*.key) to connect to the registry. Default certificates directory is /etc/containers/certs.d. (This option is not available with the remote Podman client) |
| **configmap**  list / elements=path | Use Kubernetes configmap YAML at path to provide a source for environment variable values within the containers of the pod. Note - The configmap option can be used multiple times to pass multiple Kubernetes configmap YAMLs |
| **context_dir**  path | Use path as the build context directory for each image. Requires build option be true. |
| **debug**  boolean | Enable debug for the module.  **Choices:**   - `false` - `true` |
| **executable**  string | Name of executable to run, by default ‘podman’  **Default:** `"podman"` |
| **kube_file**  path / required | Path to file with YAML configuration for a Pod. |
| **log_driver**  string | Set logging driver for all created containers. |
| **log_level**  string | Set logging level for podman calls. Log messages above specified level (“debug”|”info”|”warn”|”error”|”fatal”|”panic”) (default “error”)  **Choices:**   - `"debug"` - `"info"` - `"warn"` - `"error"` - `"fatal"` - `"panic"` |
| **network**  list / elements=string | List of the names of CNI networks the pod should join. |
| **password**  string | The username and password to use to authenticate with the registry if required. |
| **quiet**  boolean | Hide image pulls logs from output.  **Choices:**   - `false` - `true` |
| **recreate**  boolean | If pod already exists, delete it and run the new one.  **Choices:**   - `false` - `true` |
| **seccomp_profile_root**  path | Directory path for seccomp profiles (default is “/var/lib/kubelet/seccomp”). This option is not available with the remote Podman client |
| **state**  string / required | Start the pod after creating it, or to leave it created only.  **Choices:**   - `"created"` - `"started"` - `"absent"` |
| **tls_verify**  boolean | Require HTTPS and verify certificates when contacting registries (default is true). If explicitly set to true, then TLS verification will be used. If set to false, then TLS verification will not be used. If not specified, TLS verification will be used unless the target registry is listed as an insecure registry in registries.conf.  **Choices:**   - `false` - `true` |
| **username**  string | The username and password to use to authenticate with the registry if required. |
| **userns**  string | Set the user namespace mode for all the containers in a pod. It defaults to the PODMAN_USERNS environment variable. An empty value (“”) means user namespaces are disabled. |

## [Examples](podman_play_module.md#id4)

```yaml+jinja
- name: Play kube file
  containers.podman.podman_play:
    kube_file: ~/kube.yaml
    state: started
```

### Authors

- Sagi Shnaidman (@sshnaidm)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
