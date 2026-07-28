---
collection: ansible
version: "8"
title: "awx.awx.subscriptions module – Get subscription list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/subscriptions_module.html
fetched_at: 2026-07-28T01:11:44+00:00
---
# awx.awx.subscriptions module – Get subscription list

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
> To use it in a playbook, specify: `awx.awx.subscriptions`.

- [Synopsis](subscriptions_module.md#synopsis)
- [Parameters](subscriptions_module.md#parameters)
- [Notes](subscriptions_module.md#notes)
- [Examples](subscriptions_module.md#examples)
- [Return Values](subscriptions_module.md#return-values)

## [Synopsis](subscriptions_module.md#id1)

- Get subscriptions available to Automation Platform Controller. See <https://www.ansible.com/tower> for an overview.

## [Parameters](subscriptions_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **filters**  dictionary | Client side filters to apply to the subscriptions.  For any entries in this dict, if there is a corresponding entry in the subscription it must contain the value from this dict  Note This is a client side search, not an API side search  **Default:** `{}` |
| **password**  string / required | Red Hat or Red Hat Satellite password to get available subscriptions.  The credentials you use will be stored for future use in retrieving renewal or expanded subscriptions |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **username**  string / required | Red Hat or Red Hat Satellite username to get available subscriptions.  The credentials you use will be stored for future use in retrieving renewal or expanded subscriptions |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](subscriptions_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](subscriptions_module.md#id4)

```yaml+jinja
- name: Get subscriptions
  subscriptions:
    username: "my_username"
    password: "My Password"

- name: Get subscriptions with a filter
  subscriptions:
    username: "my_username"
    password: "My Password"
    filters:
      product_name: "Red Hat Ansible Automation Platform"
      support_level: "Self-Support"
```

## [Return Values](subscriptions_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subscriptions**  dictionary | dictionary containing information about the subscriptions  **Returned:** If login succeeded |

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
