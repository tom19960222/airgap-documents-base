---
collection: ansible
version: "8"
title: "community.general.scaleway_function module – Scaleway Function management"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_function_module.html
fetched_at: 2026-07-28T01:50:14+00:00
---
# community.general.scaleway_function module – Scaleway Function management

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
> see [Requirements](scaleway_function_module.md#ansible-collections-community-general-scaleway-function-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.scaleway_function`.

New in community.general 6.0.0

- [Synopsis](scaleway_function_module.md#synopsis)
- [Requirements](scaleway_function_module.md#requirements)
- [Parameters](scaleway_function_module.md#parameters)
- [Attributes](scaleway_function_module.md#attributes)
- [Notes](scaleway_function_module.md#notes)
- [Examples](scaleway_function_module.md#examples)
- [Return Values](scaleway_function_module.md#return-values)

## [Synopsis](scaleway_function_module.md#id1)

- This module manages function on Scaleway account.

## [Requirements](scaleway_function_module.md#id2)

The below requirements are needed on the host that executes this module.

- passlib[argon2] >= 1.7.4

## [Parameters](scaleway_function_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **description**  string | Description of the function.  **Default:** `""` |
| **environment_variables**  dictionary | Environment variables of the function.  Injected in function at runtime.  **Default:** `{}` |
| **function_timeout**  string | The length of time your handler can spend processing a request before being stopped. |
| **handler**  string | The `module-name.export` value in your function. |
| **max_scale**  integer | Maximum number of replicas for the function. |
| **memory_limit**  integer | Resources define performance characteristics of your function.  They are allocated to your function at runtime. |
| **min_scale**  integer | Minimum number of replicas for the function. |
| **name**  string / required | Name of the function. |
| **namespace_id**  string / required | Function namespace identifier. |
| **privacy**  string | Privacy policies define whether a function can be executed anonymously.  Choose `public` to enable anonymous execution, or `private` to protect your function with an authentication mechanism provided by the Scaleway API.  **Choices:**   - `"public"` ← (default) - `"private"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **redeploy**  boolean | Redeploy the function if update is required.  **Choices:**   - `false` ← (default) - `true` |
| **region**  string / required | Scaleway region to use (for example `fr-par`).  **Choices:**   - `"fr-par"` - `"nl-ams"` - `"pl-waw"` |
| **runtime**  string / required | Runtime of the function  See <https://www.scaleway.com/en/docs/compute/functions/reference-content/functions-lifecycle/> for all available runtimes |
| **secret_environment_variables**  dictionary | Secret environment variables of the function.  Updating those values will not output a `changed` state in Ansible.  Injected in function at runtime.  **Default:** `{}` |
| **state**  string | Indicate desired state of the function.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the resource to reach its desired state before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_sleep_time**  integer | Time to wait before every attempt to check the state of the resource.  **Default:** `3` |
| **wait_timeout**  integer | Time to wait for the resource to reach the expected state.  **Default:** `300` |

## [Attributes](scaleway_function_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_function_module.md#id5)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_function_module.md#id6)

```yaml+jinja
- name: Create a function
  community.general.scaleway_function:
    namespace_id: '{{ scw_function_namespace }}'
    region: fr-par
    state: present
    name: my-awesome-function
    runtime: python3
    environment_variables:
      MY_VAR: my_value
    secret_environment_variables:
      MY_SECRET_VAR: my_secret_value
  register: function_creation_task

- name: Make sure function is deleted
  community.general.scaleway_function:
    namespace_id: '{{ scw_function_namespace }}'
    region: fr-par
    state: absent
    name: my-awesome-function
```

## [Return Values](scaleway_function_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **function**  dictionary | The function information.  **Returned:** when `state=present`  **Sample:** `{"cpu_limit": 140, "description": "Function used for testing scaleway_function ansible module", "domain_name": "fnansibletestfxamabuc-fn-ansible-test.functions.fnc.fr-par.scw.cloud", "environment_variables": {"MY_VAR": "my_value"}, "error_message": null, "handler": "handler.handle", "http_option": "", "id": "ceb64dc4-4464-4196-8e20-ecef705475d3", "max_scale": 5, "memory_limit": 256, "min_scale": 0, "name": "fn-ansible-test", "namespace_id": "82737d8d-0ebb-4d89-b0ad-625876eca50d", "privacy": "public", "region": "fr-par", "runtime": "python310", "runtime_message": "", "secret_environment_variables": [{"key": "MY_SECRET_VAR", "value": "$argon2id$v=19$m=65536,t=1,p=2$tb6UwSPWx/rH5Vyxt9Ujfw$5ZlvaIjWwNDPxD9Rdght3NarJz4IETKjpvAU3mMSmFg"}], "status": "created", "timeout": "300s"}` |

### Authors

- Guillaume MARTINEZ (@Lunik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
