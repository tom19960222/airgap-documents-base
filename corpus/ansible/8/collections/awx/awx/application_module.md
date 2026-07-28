---
collection: ansible
version: "8"
title: "awx.awx.application module – create, update, or destroy Automation Platform Controller applications"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/application_module.html
fetched_at: 2026-07-28T01:11:22+00:00
---
# awx.awx.application module – create, update, or destroy Automation Platform Controller applications

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
> To use it in a playbook, specify: `awx.awx.application`.

- [Synopsis](application_module.md#synopsis)
- [Parameters](application_module.md#parameters)
- [Notes](application_module.md#notes)
- [Examples](application_module.md#examples)

## [Synopsis](application_module.md#id1)

- Create, update, or destroy Automation Platform Controller applications. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_application

## [Parameters](application_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authorization_grant_type**  string | The grant type the user must use for acquire tokens for this application.  **Choices:**   - `"password"` - `"authorization-code"` |
| **client_type**  string | Set to public or confidential depending on how secure the client device is.  **Choices:**   - `"public"` - `"confidential"` |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **description**  string | Description of the application. |
| **name**  string / required | Name of the application. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **organization**  string / required | Name, ID, or named URL of organization for application. |
| **redirect_uris**  list / elements=string | Allowed urls list, space separated. Required when authorization-grant-type=authorization-code |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **skip_authorization**  boolean | Set True to skip authorization step for completely trusted applications.  **Choices:**   - `false` - `true` |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](application_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](application_module.md#id4)

```yaml+jinja
- name: Add Foo application
  application:
    name: "Foo"
    description: "Foo bar application"
    organization: "test"
    state: present
    authorization_grant_type: password
    client_type: public

- name: Add Foo application
  application:
    name: "Foo"
    description: "Foo bar application"
    organization: "test"
    state: present
    authorization_grant_type: authorization-code
    client_type: confidential
    redirect_uris:
      - http://tower.com/api/v2/
```

### Authors

- Geoffrey Bacheot (@jffz)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
