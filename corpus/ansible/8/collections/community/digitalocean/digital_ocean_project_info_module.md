---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_project_info module – Gather information about DigitalOcean Projects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_project_info_module.html
fetched_at: 2026-07-28T01:43:10+00:00
---
# community.digitalocean.digital_ocean_project_info module – Gather information about DigitalOcean Projects

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_project_info`.

New in community.digitalocean 1.6.0

- [Synopsis](digital_ocean_project_info_module.md#synopsis)
- [Parameters](digital_ocean_project_info_module.md#parameters)
- [Examples](digital_ocean_project_info_module.md#examples)
- [Return Values](digital_ocean_project_info_module.md#return-values)

## [Synopsis](digital_ocean_project_info_module.md#id1)

- This module can be used to gather information about Projects.

## [Parameters](digital_ocean_project_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **id**  string | Project ID that can be used to identify and reference a project. |
| **name**  string | Project name that can be used to identify and reference a project. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_project_info_module.md#id3)

```yaml+jinja
# Get specific project by id
- community.digitalocean.digital_ocean_project_info:
    id: cb1ef55e-3cd8-4c7c-aa5d-07c32bf41627

# Get specific project by name
- community.digitalocean.digital_ocean_project_info:
    name: my-project-name

# Get all projects
- community.digitalocean.digital_ocean_project_info:
  register: projects
```

## [Return Values](digital_ocean_project_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | DigitalOcean project information  **Returned:** success  **Sample:** `[{"created_at": "2021-03-11T00:00:00Z", "description": "My project description", "environment": "Development", "id": "12345678-abcd-efgh-5678-10111213", "is_default": false, "name": "my-test-project", "owner_id": 12345678, "owner_uuid": "12345678-1234-4321-abcd-20212223", "purpose": "", "updated_at": "2021-03-11T00:00:00Z"}]` |

### Authors

- Tyler Auerbeck (@tylerauerbeck)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
