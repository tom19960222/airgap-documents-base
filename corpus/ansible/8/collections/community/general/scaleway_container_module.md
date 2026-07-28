---
collection: ansible
version: "8"
title: "community.general.scaleway_container module – Scaleway Container management"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_container_module.html
fetched_at: 2026-07-28T01:50:09+00:00
---
# community.general.scaleway_container module – Scaleway Container management

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](scaleway_container_module.md#ansible-collections-community-general-scaleway-container-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.scaleway_container`.

New in community.general 6.0.0

- [Synopsis](scaleway_container_module.md#synopsis)
- [Requirements](scaleway_container_module.md#requirements)
- [Parameters](scaleway_container_module.md#parameters)
- [Attributes](scaleway_container_module.md#attributes)
- [Notes](scaleway_container_module.md#notes)
- [Examples](scaleway_container_module.md#examples)
- [Return Values](scaleway_container_module.md#return-values)

## [Synopsis](scaleway_container_module.md#id1)

- This module manages container on Scaleway account.

## [Requirements](scaleway_container_module.md#id2)

The below requirements are needed on the host that executes this module.

- passlib[argon2] >= 1.7.4

## [Parameters](scaleway_container_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **container_timeout**  string | The length of time your handler can spend processing a request before being stopped. |
| **description**  string | Description of the container namespace.  **Default:** `""` |
| **environment_variables**  dictionary | Environment variables of the container namespace.  Injected in container at runtime.  **Default:** `{}` |
| **max_concurrency**  integer | Maximum number of connections per container.  This parameter will be used to trigger autoscaling. |
| **max_scale**  integer | Maximum number of replicas for the container. |
| **memory_limit**  integer | Resources define performance characteristics of your container.  They are allocated to your container at runtime. |
| **min_scale**  integer | Minimum number of replicas for the container. |
| **name**  string / required | Name of the container namespace. |
| **namespace_id**  string / required | Container namespace identifier. |
| **port**  integer | Listen port used to expose the container. |
| **privacy**  string | Privacy policies define whether a container can be executed anonymously.  Choose `public` to enable anonymous execution, or `private` to protect your container with an authentication mechanism provided by the Scaleway API.  **Choices:**   - `"public"` ← (default) - `"private"` |
| **protocol**  string | Communication protocol of the container.  **Choices:**   - `"http1"` ← (default) - `"h2c"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **redeploy**  boolean | Redeploy the container if update is required.  **Choices:**   - `false` ← (default) - `true` |
| **region**  string / required | Scaleway region to use (for example `fr-par`).  **Choices:**   - `"fr-par"` - `"nl-ams"` - `"pl-waw"` |
| **registry_image**  string / required | The name of image used for the container. |
| **secret_environment_variables**  dictionary | Secret environment variables of the container namespace.  Updating those values will not output a `changed` state in Ansible.  Injected in container at runtime.  **Default:** `{}` |
| **state**  string | Indicate desired state of the container.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the resource to reach its desired state before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_sleep_time**  integer | Time to wait before every attempt to check the state of the resource.  **Default:** `3` |
| **wait_timeout**  integer | Time to wait for the resource to reach the expected state.  **Default:** `300` |

## [Attributes](scaleway_container_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_container_module.md#id5)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_container_module.md#id6)

```yaml+jinja
- name: Create a container
  community.general.scaleway_container:
    namespace_id: '{{ scw_container_namespace }}'
    state: present
    region: fr-par
    name: my-awesome-container
    registry_image: rg.fr-par.scw.cloud/funcscwtestrgy2f9zw/nginx:latest
    environment_variables:
      MY_VAR: my_value
    secret_environment_variables:
      MY_SECRET_VAR: my_secret_value
  register: container_creation_task

- name: Make sure container is deleted
  community.general.scaleway_container:
    namespace_id: '{{ scw_container_namespace }}'
    state: absent
    region: fr-par
    name: my-awesome-container
```

## [Return Values](scaleway_container_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container**  dictionary | The container information.  **Returned:** when `state=present`  **Sample:** `{"cpu_limit": 140, "description": "Container used for testing scaleway_container ansible module", "domain_name": "cnansibletestgfogtjod-cn-ansible-test.functions.fnc.fr-par.scw.cloud", "environment_variables": {"MY_VAR": "my_value"}, "error_message": null, "http_option": "", "id": "c9070eb0-d7a4-48dd-9af3-4fb139890721", "max_concurrency": 50, "max_scale": 5, "memory_limit": 256, "min_scale": 0, "name": "cn-ansible-test", "namespace_id": "75e299f1-d1e5-4e6b-bc6e-4fb51cfe1e69", "port": 80, "privacy": "public", "protocol": "http1", "region": "fr-par", "registry_image": "rg.fr-par.scw.cloud/namespace-ansible-ci/nginx:latest", "secret_environment_variables": [{"key": "MY_SECRET_VAR", "value": "$argon2id$v=19$m=65536,t=1,p=2$tb6UwSPWx/rH5Vyxt9Ujfw$5ZlvaIjWwNDPxD9Rdght3NarJz4IETKjpvAU3mMSmFg"}], "status": "created", "timeout": "300s"}` |

### Authors

- Guillaume MARTINEZ (@Lunik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
