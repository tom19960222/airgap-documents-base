---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.objects_user module – Manages objects users on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/objects_user_module.html
fetched_at: 2026-07-28T01:39:58+00:00
---
# cloudscale_ch.cloud.objects_user module – Manages objects users on the cloudscale.ch IaaS service

> **Note:**
>
> This module is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/ui/repo/published/cloudscale_ch/cloud/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.objects_user`.

New in cloudscale_ch.cloud 1.1.0

- [Synopsis](objects_user_module.md#synopsis)
- [Parameters](objects_user_module.md#parameters)
- [Notes](objects_user_module.md#notes)
- [Examples](objects_user_module.md#examples)
- [Return Values](objects_user_module.md#return-values)

## [Synopsis](objects_user_module.md#id1)

- Create, update and remove objects users cloudscale.ch IaaS service.

## [Parameters](objects_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **display_name**  aliases: name  string | Display name of the objects user.  Either *display_name* or *id* is required. |
| **id**  string | Name of the objects user.  Either *display_name* or *id* is required. |
| **state**  string | State of the objects user.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tags associated with the objects user. Set this to `{}` to clear any tags. |

## [Notes](objects_user_module.md#id3)

> **Note:**
>
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](objects_user_module.md#id4)

```yaml+jinja
- name: Create an objects user
  cloudscale_ch.cloud.objects_user:
    display_name: alan
    tags:
      project: luna
    api_token: xxxxxx
  register: object_user

- name: print keys
  debug:
    var: object_user.keys

- name: Update an objects user
  cloudscale_ch.cloud.objects_user:
    display_name: alan
    tags:
      project: gemini
    api_token: xxxxxx

- name: Remove an objects user
  cloudscale_ch.cloud.objects_user:
    display_name: alan
    state: absent
    api_token: xxxxxx
```

## [Return Values](objects_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **display_name**  string | The display name of the objects user.  **Returned:** success  **Sample:** `"alan"` |
| **href**  string | The API URL to get details about this resource.  **Returned:** success when state == present  **Sample:** `"https://api.cloudscale.ch/v1/objects-users/6fe39134bf4178747eebc429f82cfafdd08891d4279d0d899bc4012db1db6a15"` |
| **id**  string | The ID of the objects user.  **Returned:** success  **Sample:** `"6fe39134bf4178747eebc429f82cfafdd08891d4279d0d899bc4012db1db6a15"` |
| **keys**  complex | List of key objects.  **Returned:** success |
| **access_key**  string | The access key.  **Returned:** success  **Sample:** `"0ZTAIBKSGYBRHQ09G11W"` |
| **secret_key**  string | The secret key.  **Returned:** success  **Sample:** `"bn2ufcwbIa0ARLc5CLRSlVaCfFxPHOpHmjKiH34T"` |
| **state**  string | The current status of the objects user.  **Returned:** success  **Sample:** `"present"` |
| **tags**  dictionary | Tags assosiated with the objects user.  **Returned:** success  **Sample:** `{"project": "my project"}` |

### Authors

- Rene Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
