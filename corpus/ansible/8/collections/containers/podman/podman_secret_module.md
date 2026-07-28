---
collection: ansible
version: "8"
title: "containers.podman.podman_secret module – Manage podman secrets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_secret_module.html
fetched_at: 2026-07-28T02:03:17+00:00
---
# containers.podman.podman_secret module – Manage podman secrets

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
> see [Requirements](podman_secret_module.md#ansible-collections-containers-podman-podman-secret-module-requirements) for details.
>
> To use it in a playbook, specify: `containers.podman.podman_secret`.

New in containers.podman 1.7.0

- [Synopsis](podman_secret_module.md#synopsis)
- [Requirements](podman_secret_module.md#requirements)
- [Parameters](podman_secret_module.md#parameters)
- [Examples](podman_secret_module.md#examples)

## [Synopsis](podman_secret_module.md#id1)

- Manage podman secrets

## [Requirements](podman_secret_module.md#id2)

The below requirements are needed on the host that executes this module.

- podman

## [Parameters](podman_secret_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data**  string | The value of the secret. Required when `state` is `present`. |
| **driver**  string | Override default secrets driver, currently podman uses `file` which is unencrypted. |
| **driver_opts**  dictionary | Driver-specific key-value options. |
| **executable**  string | Path to `podman` executable if it is not in the `$PATH` on the machine running `podman`  **Default:** `"podman"` |
| **force**  boolean | Use it when `state` is `present` to remove and recreate an existing secret.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the secret. |
| **skip_existing**  boolean | Use it when `state` is `present` and secret with the same name already exists. If set to `true`, the secret will NOT be recreated and remains as is.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether to create or remove the named secret.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Examples](podman_secret_module.md#id4)

```yaml+jinja
- name: Create secret
  containers.podman.podman_secret:
    state: present
    name: mysecret
    data: "my super secret content"

- name: Create container that uses the secret
  containers.podman.podman_container:
    name: showmysecret
    image: docker.io/alpine:3.14
    secrets:
      - mysecret
    detach: false
    command: cat /run/secrets/mysecret
    register: container

- name: Output secret data
  debug:
    msg: '{{ container.stdout }}'

- name: Remove secret
  containers.podman.podman_secret:
    state: absent
    name: mysecret
```

### Authors

- Aliaksandr Mianzhynski (@amenzhinsky)

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
