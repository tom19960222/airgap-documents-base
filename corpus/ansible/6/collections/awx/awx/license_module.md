---
collection: ansible
version: "6"
title: "awx.awx.license module – Set the license for Automation Platform Controller"
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/license_module.html
fetched_at: 2026-07-27T16:45:31+00:00
---
# awx.awx.license module – Set the license for Automation Platform Controller

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
> To use it in a playbook, specify: `awx.awx.license`.

- [Synopsis](license_module.md#synopsis)
- [Parameters](license_module.md#parameters)
- [Notes](license_module.md#notes)
- [Examples](license_module.md#examples)

## [Synopsis](license_module.md#id1)

- Get or Set Automation Platform Controller license. See <https://www.ansible.com/tower> for an overview.

## [Parameters](license_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **force**  boolean | By default, the license manifest will only be applied if Tower is currently unlicensed or trial licensed. When force=true, the license is always applied.  Choices:   - `false` ← (default) - `true` |
| **manifest**  string | file path to a Red Hat subscription manifest (a .zip file) |
| **pool_id**  string | Red Hat or Red Hat Satellite pool_id to attach to |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |

## [Notes](license_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](license_module.md#id4)

```yaml+jinja
- name: Set the license using a file
  license:
    manifest: "/tmp/my_manifest.zip"

- name: Attach to a pool
  license:
    pool_id: 123456

- name: Remove license
  license:
    state: absent
```

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
