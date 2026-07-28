---
collection: ansible
version: "8"
title: "awx.awx.token module – create, update, or destroy Automation Platform Controller tokens."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/token_module.html
fetched_at: 2026-07-28T01:11:45+00:00
---
# awx.awx.token module – create, update, or destroy Automation Platform Controller tokens.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/ui/repo/published/awx/awx/) (version 22.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.token`.

New in awx.awx 2.3.0

- [Synopsis](token_module.md#synopsis)
- [Parameters](token_module.md#parameters)
- [Notes](token_module.md#notes)
- [Examples](token_module.md#examples)
- [Return Values](token_module.md#return-values)

## [Synopsis](token_module.md#id1)

- Create or destroy Automation Platform Controller tokens. See <https://www.ansible.com/tower> for an overview.
- In addition, the module sets an Ansible fact which can be passed into other controller modules as the parameter controller_oauthtoken. See examples for usage.
- Because of the sensitive nature of tokens, the created token value is only available once through the Ansible fact. (See RETURN for details)
- Due to the nature of tokens this module is not idempotent. A second will with the same parameters will create a new token.
- If you are creating a temporary token for use with modules you should delete the token when you are done with it. See the example for how to do it.

Aliases: tower_token

## [Parameters](token_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **application**  string | The application name, ID, or named URL tied to this token. |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **description**  string | Optional description of this access token. |
| **existing_token**  dictionary | The data structure produced from token in create mode to be used with state absent. |
| **existing_token_id**  string | A token ID (number) which can be used to delete an arbitrary token with state absent. |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **scope**  string | Allowed scopes, further restricts user’s permissions. Must be a simple space-separated string with allowed scopes [‘read’, ‘write’].  **Choices:**   - `"read"` - `"write"` |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](token_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](token_module.md#id4)

```yaml+jinja
- block:
    - name: Create a new token using an existing token
      token:
        description: '{{ token_description }}'
        scope: "write"
        state: present
        controller_oauthtoken: "{{ my_existing_token }}"

    - name: Delete this token
      token:
        existing_token: "{{ controller_token }}"
        state: absent

    - name: Create a new token using username/password
      token:
        description: '{{ token_description }}'
        scope: "write"
        state: present
        controller_username: "{{ my_username }}"
        controller_password: "{{ my_password }}"

    - name: Use our new token to make another call
      job_list:
        controller_oauthtoken: "{{ controller_token }}"

  always:
    - name: Delete our Token with the token we created
      token:
        existing_token: "{{ controller_token }}"
        state: absent
      when: token is defined

- name: Delete a token by its id
  token:
    existing_token_id: 4
    state: absent
```

## [Return Values](token_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **controller_token**  dictionary | An Ansible Fact variable representing a token object which can be used for auth in subsequent modules. See examples for usage.  **Returned:** on successful create |
| **id**  string | The numeric ID of the token created  **Returned:** success |
| **token**  string | The token that was generated. This token can never be accessed again, make sure this value is noted before it is lost.  **Returned:** success |

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
