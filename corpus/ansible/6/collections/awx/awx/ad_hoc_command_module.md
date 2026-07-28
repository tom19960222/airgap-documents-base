---
collection: ansible
version: "6"
title: "awx.awx.ad_hoc_command module – create, update, or destroy Automation Platform Controller ad hoc commands."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/ad_hoc_command_module.html
fetched_at: 2026-07-27T16:45:21+00:00
---
# awx.awx.ad_hoc_command module – create, update, or destroy Automation Platform Controller ad hoc commands.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
>
> To use it in a playbook, specify: `awx.awx.ad_hoc_command`.

New in awx.awx 4.0.0

- [Synopsis](ad_hoc_command_module.md#synopsis)
- [Parameters](ad_hoc_command_module.md#parameters)
- [Notes](ad_hoc_command_module.md#notes)
- [Examples](ad_hoc_command_module.md#examples)
- [Return Values](ad_hoc_command_module.md#return-values)

## [Synopsis](ad_hoc_command_module.md#id1)

- Create, update, or destroy Automation Platform Controller ad hoc commands. See <https://www.ansible.com/tower> for an overview.

## [Parameters](ad_hoc_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_enabled**  boolean | If the become flag should be set.  Choices:   - `false` - `true` |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credential**  string / required | Credential to use for ad hoc command. |
| **diff_mode**  boolean | Show the changes made by Ansible tasks where supported  Choices:   - `false` - `true` |
| **execution_environment**  string | Execution Environment to use for the ad hoc command. |
| **extra_vars**  dictionary | Extra variables to use for the ad hoc command.. |
| **forks**  integer | The number of forks to use for this ad hoc execution. |
| **interval**  float | The interval to request an update from the controller.  Default: `2.0` |
| **inventory**  string / required | Inventory to use for the ad hoc command. |
| **job_type**  string | Job_type to use for the ad hoc command.  Choices:   - `"run"` - `"check"` |
| **limit**  string | Limit to use for the ad hoc command. |
| **module_args**  string | The arguments to pass to the module.  Default: `""` |
| **module_name**  string / required | The Ansible module to execute. |
| **timeout**  integer | If waiting for the command to complete this will abort after this amount of seconds |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **verbosity**  integer | Verbosity level for this ad hoc command run  Choices:   - `0` - `1` - `2` - `3` - `4` - `5` |
| **wait**  boolean | Wait for the command to complete.  Choices:   - `false` ← (default) - `true` |

## [Notes](ad_hoc_command_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](ad_hoc_command_module.md#id4)

```yaml+jinja

```

## [Return Values](ad_hoc_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  integer | id of the newly launched command  Returned: success  Sample: `86` |
| **status**  string | status of newly launched command  Returned: success  Sample: `"pending"` |

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
