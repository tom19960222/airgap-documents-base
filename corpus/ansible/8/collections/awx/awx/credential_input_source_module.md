---
collection: ansible
version: "8"
title: "awx.awx.credential_input_source module – create, update, or destroy Automation Platform Controller credential input sources."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/credential_input_source_module.html
fetched_at: 2026-07-28T01:11:25+00:00
---
# awx.awx.credential_input_source module – create, update, or destroy Automation Platform Controller credential input sources.

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
> To use it in a playbook, specify: `awx.awx.credential_input_source`.

New in awx.awx 2.3.0

- [Synopsis](credential_input_source_module.md#synopsis)
- [Parameters](credential_input_source_module.md#parameters)
- [Notes](credential_input_source_module.md#notes)
- [Examples](credential_input_source_module.md#examples)

## [Synopsis](credential_input_source_module.md#id1)

- Create, update, or destroy Automation Platform Controller credential input sources. See <https://www.ansible.com/tower> for an overview.

Aliases: tower_credential_input_source

## [Parameters](credential_input_source_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **description**  string | The description to use for the credential input source. |
| **input_field_name**  string / required | The input field the credential source will be used for |
| **metadata**  dictionary | A JSON or YAML string |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **source_credential**  string | The credential name, ID, or named URL which is the source of the credential lookup |
| **state**  string | Desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"exists"` |
| **target_credential**  string / required | The credential name, ID, or named URL which will have its input defined by this source |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](credential_input_source_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](credential_input_source_module.md#id4)

```yaml+jinja
- name: Use CyberArk Lookup credential as password source
  credential_input_source:
    input_field_name: password
    target_credential: new_cred
    source_credential: cyberark_lookup
    metadata:
      object_query: "Safe=MY_SAFE;Object=awxuser"
      object_query_format: "Exact"
    state: present
```

### Authors

- Tom Page (@Tompage1994)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
