---
collection: ansible
version: "6"
title: "awx.awx.group module – create, update, or destroy Automation Platform Controller group."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/group_module.html
fetched_at: 2026-07-27T16:45:25+00:00
---
# awx.awx.group module – create, update, or destroy Automation Platform Controller group.

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
> To use it in a playbook, specify: `awx.awx.group`.

- [Synopsis](group_module.md#synopsis)
- [Parameters](group_module.md#parameters)
- [Notes](group_module.md#notes)
- [Examples](group_module.md#examples)

## [Synopsis](group_module.md#id1)

- Create, update, or destroy Automation Platform Controller groups. See <https://www.ansible.com/tower> for an overview.

## [Parameters](group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **children**  aliases: groups  list / elements=string | List of groups that should be nested inside in this group. |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **description**  string | The description to use for the group. |
| **hosts**  list / elements=string | List of hosts that should be put in this group. |
| **inventory**  string / required | Inventory the group should be made a member of. |
| **name**  string / required | The name to use for the group. |
| **new_name**  string | A new name for this group (for renaming) |
| **preserve_existing_children**  aliases: preserve_existing_groups  boolean | Provide option (False by default) to preserves existing children in an existing group.  Choices:   - `false` ← (default) - `true` |
| **preserve_existing_hosts**  boolean | Provide option (False by default) to preserves existing hosts in an existing group.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |
| **variables**  dictionary | Variables to use for the group. |

## [Notes](group_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](group_module.md#id4)

```yaml+jinja
- name: Add group
  group:
    name: localhost
    description: "Local Host Group"
    inventory: "Local Inventory"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add group
  group:
    name: Cities
    description: "Local Host Group"
    inventory: Default Inventory
    hosts:
      - fda
    children:
      - NewYork
    preserve_existing_hosts: True
    preserve_existing_children: True
```

### Authors

- Wayne Witzel III (@wwitzel3)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
