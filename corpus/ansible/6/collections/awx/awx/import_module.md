---
collection: ansible
version: "6"
title: "awx.awx.import module – import resources into Automation Platform Controller."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/import_module.html
fetched_at: 2026-07-27T16:45:26+00:00
---
# awx.awx.import module – import resources into Automation Platform Controller.

> **Note:**
>
> This module is part of the [awx.awx collection](https://galaxy.ansible.com/awx/awx) (version 21.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install awx.awx`.
> You need further requirements to be able to use this module,
> see [Requirements](import_module.md#ansible-collections-awx-awx-import-module-requirements) for details.
>
> To use it in a playbook, specify: `awx.awx.import`.

New in awx.awx 3.7.0

- [Synopsis](import_module.md#synopsis)
- [Requirements](import_module.md#requirements)
- [Parameters](import_module.md#parameters)
- [Notes](import_module.md#notes)
- [Examples](import_module.md#examples)

## [Synopsis](import_module.md#id1)

- Import assets into Automation Platform Controller. See <https://www.ansible.com/tower> for an overview.

## [Requirements](import_module.md#id2)

The below requirements are needed on the host that executes this module.

- awxkit >= 9.3.0

## [Parameters](import_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **assets**  dictionary / required | The assets to import.  This can be the output of the export module or loaded from a file |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |

## [Notes](import_module.md#id4)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](import_module.md#id5)

```yaml+jinja
- name: Export all assets
  export:
    all: True
  register: export_output

- name: Import all assets from our export
  import:
    assets: "{{ export_output.assets }}"

- name: Load data from a json file created by a command like awx export --organization Default
  import:
    assets: "{{ lookup('file', 'org.json') | from_json() }}"
```

### Authors

- John Westcott (@john-westcott-iv)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
