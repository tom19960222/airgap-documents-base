---
collection: ansible
version: "8"
title: "awx.awx.organization module – create, update, or destroy Automation Platform Controller organizations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/organization_module.html
fetched_at: 2026-07-28T01:11:40+00:00
---
# awx.awx.organization module – create, update, or destroy Automation Platform Controller organizations

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
> To use it in a playbook, specify: `awx.awx.organization`.

- [Synopsis](organization_module.md#synopsis)
- [Parameters](organization_module.md#parameters)
- [Notes](organization_module.md#notes)
- [Examples](organization_module.md#examples)

## [Synopsis](organization_module.md#id1)

- Create, update, or destroy Automation Platform Controller organizations. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_organization

## [Parameters](organization_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **custom_virtualenv**  string | Local absolute file path containing a custom Python virtualenv to use.  Only compatible with older versions of AWX/Tower  Deprecated, will be removed in the future |
| **default_environment**  string | Default Execution Environment name, ID, or named URL to use for jobs owned by the Organization. |
| **description**  string | The description to use for the organization. |
| **galaxy_credentials**  list / elements=string | list of Ansible Galaxy credential names, IDs, or named URLs to associate to the organization |
| **instance_groups**  list / elements=string | list of Instance Group names, IDs, or named URLs for this Organization to run on. |
| **max_hosts**  integer | The max hosts allowed in this organizations |
| **name**  string / required | Name to use for the organization. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **notification_templates_approvals**  list / elements=string | list of notifications to send on start |
| **notification_templates_error**  list / elements=string | list of notifications to send on error |
| **notification_templates_started**  list / elements=string | list of notifications to send on start |
| **notification_templates_success**  list / elements=string | list of notifications to send on success |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](organization_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](organization_module.md#id4)

```yaml+jinja
- name: Create organization
  organization:
    name: "Foo"
    description: "Foo bar organization"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Create organization using 'foo-venv' as default Python virtualenv
  organization:
    name: "Foo"
    description: "Foo bar organization using foo-venv"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Create organization that pulls content from galaxy.ansible.com
  organization:
    name: "Foo"
    state: present
    galaxy_credentials:
      - Ansible Galaxy
    controller_config_file: "~/tower_cli.cfg"
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
