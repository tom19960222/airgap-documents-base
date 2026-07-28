---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_project module – Manages projects on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_project_module.html
fetched_at: 2026-07-28T02:46:13+00:00
---
# ngine_io.cloudstack.cs_project module – Manages projects on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_project_module.md#ansible-collections-ngine-io-cloudstack-cs-project-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_project`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_project_module.md#synopsis)
- [Requirements](cs_project_module.md#requirements)
- [Parameters](cs_project_module.md#parameters)
- [Notes](cs_project_module.md#notes)
- [Examples](cs_project_module.md#examples)
- [Return Values](cs_project_module.md#return-values)

## [Synopsis](cs_project_module.md#id1)

- Create, update, suspend, activate and remove projects.

## [Requirements](cs_project_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_project_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the project is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **display_text**  string | Display text of the project.  If not specified, *name* will be used as *display_text*. |
| **domain**  string | Domain the project is related to. |
| **name**  string / required | Name of the project. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | State of the project.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"active"` - `"suspended"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  If you want to delete all tags, set a empty list e.g. *tags: []*. |

## [Notes](cs_project_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_project_module.md#id5)

```yaml+jinja
- name: Create a project
  ngine_io.cloudstack.cs_project:
    name: web
    tags:
      - { key: admin, value: john }
      - { key: foo,   value: bar }

- name: Rename a project
  ngine_io.cloudstack.cs_project:
    name: web
    display_text: my web project

- name: Suspend an existing project
  ngine_io.cloudstack.cs_project:
    name: web
    state: suspended

- name: Activate an existing project
  ngine_io.cloudstack.cs_project:
    name: web
    state: active

- name: Remove a project
  ngine_io.cloudstack.cs_project:
    name: web
    state: absent
```

## [Return Values](cs_project_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the project is related to.  **Returned:** success  **Sample:** `"example account"` |
| **display_text**  string | Display text of the project.  **Returned:** success  **Sample:** `"web project"` |
| **domain**  string | Domain the project is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the project.  **Returned:** success  **Sample:** `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **name**  string | Name of the project.  **Returned:** success  **Sample:** `"web project"` |
| **state**  string | State of the project.  **Returned:** success  **Sample:** `"Active"` |
| **tags**  list / elements=string | List of resource tags associated with the project.  **Returned:** success  **Sample:** `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
