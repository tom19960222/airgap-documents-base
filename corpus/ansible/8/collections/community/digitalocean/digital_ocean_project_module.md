---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_project module – Manage a DigitalOcean project"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_project_module.html
fetched_at: 2026-07-28T01:43:09+00:00
---
# community.digitalocean.digital_ocean_project module – Manage a DigitalOcean project

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_project`.

New in community.digitalocean 1.6.0

- [Synopsis](digital_ocean_project_module.md#synopsis)
- [Parameters](digital_ocean_project_module.md#parameters)
- [Examples](digital_ocean_project_module.md#examples)
- [Return Values](digital_ocean_project_module.md#return-values)

## [Synopsis](digital_ocean_project_module.md#id1)

- Manage a project in DigitalOcean

## [Parameters](digital_ocean_project_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description of the project. The maximum length is 255 characters. |
| **environment**  string | The environment of the projects resources.  **Choices:**   - `"Development"` - `"Staging"` - `"Production"` |
| **id**  string | UUID of the project |
| **is_default**  boolean | If true, all resources will be added to this project if no project is specified.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The human-readable name for the project. The maximum length is 175 characters and the name must be unique. |
| **oauth_token**  aliases: API_TOKEN  string / required | DigitalOcean OAuth token. Can be specified in `DO_API_KEY`, `DO_API_TOKEN`, or `DO_OAUTH_TOKEN` environment variables |
| **purpose**  string | The purpose of the project. The maximum length is 255 characters  Required if state is `present`  If not one of DO provided purposes, will be prefixed with `Other`  DO provided purposes can be found below  `Just trying out DigitalOcean`  `Class project/Educational Purposes`  `Website or blog`  `Web Application`  `Service or API`  `Mobile Application`  `Machine Learning/AI/Data Processing`  `IoT`  `Operational/Developer tooling` |
| **state**  string | Indicate desired state of the target.  `present` will create the project  `absent` will delete the project, if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](digital_ocean_project_module.md#id3)

```yaml+jinja
# Creates a new project
- community.digitalocean.digital_ocean_project:
    name: "TestProj"
    state: "present"
    description: "This is a test project"
    purpose: "IoT"
    environment: "Development"

# Updates the existing project with the new environment
- community.digitalocean.digital_ocean_project:
    name: "TestProj"
    state: "present"
    description: "This is a test project"
    purpose: "IoT"
    environment: "Production"

# This renames an existing project by utilizing the id of the project
- community.digitalocean.digital_ocean_project:
    name: "TestProj2"
    id: "12312312-abcd-efgh-ijkl-123123123123"
    state: "present"
    description: "This is a test project"
    purpose: "IoT"
    environment: "Development"

# This creates a project that results with a purpose of "Other: My Prod App"
- community.digitalocean.digital_ocean_project:
    name: "ProdProj"
    state: "present"
    description: "This is a prod app"
    purpose: "My Prod App"
    environment: "Production"

# This removes a project
- community.digitalocean.digital_ocean_project:
    name: "ProdProj"
    state: "absent"
```

## [Return Values](digital_ocean_project_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | a DigitalOcean Project  **Returned:** changed  **Sample:** `{"project": {"created_at": "2021-05-28T00:00:00Z", "description": "This is a test description", "environment": "Development", "id": "12312312-abcd-efgh-1234-abcdefgh123", "is_default": false, "name": "Test123", "owner_id": 1234567, "owner_uuid": "12312312-1234-5678-abcdefghijklm", "purpose": "IoT", "updated_at": "2021-05-29T00:00:00Z"}}` |

### Authors

- Tyler Auerbeck (@tylerauerbeck)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
