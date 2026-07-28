---
collection: ansible
version: "8"
title: "awx.awx.instance module – create, update, or destroy Automation Platform Controller instances."
source_url: https://docs.ansible.com/projects/ansible/8/collections/awx/awx/instance_module.html
fetched_at: 2026-07-28T01:11:30+00:00
---
# awx.awx.instance module – create, update, or destroy Automation Platform Controller instances.

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
> To use it in a playbook, specify: `awx.awx.instance`.

New in awx.awx 4.3.0

- [Synopsis](instance_module.md#synopsis)
- [Parameters](instance_module.md#parameters)
- [Notes](instance_module.md#notes)
- [Examples](instance_module.md#examples)

## [Synopsis](instance_module.md#id1)

- Create, update, or destroy Automation Platform Controller instances. See <https://www.ansible.com/tower> for an overview.

## [Parameters](instance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capacity_adjustment**  float | Capacity adjustment (0 <= capacity_adjustment <= 1) |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  *added in awx.awx 3.7.0* | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **enabled**  boolean | If true, the instance will be enabled and used.  **Choices:**   - `false` - `true` |
| **hostname**  string / required | Hostname of this instance. |
| **listener_port**  integer | Port that Receptor will listen for incoming connections on. |
| **managed_by_policy**  boolean | Managed by policy  **Choices:**   - `false` - `true` |
| **node_state**  string | Indicates the current life cycle stage of this instance.  **Choices:**   - `"deprovisioning"` - `"installed"` |
| **node_type**  string | Role that this node plays in the mesh.  **Choices:**   - `"execution"` |
| **request_timeout**  float | Specify the timeout Ansible should use in requests to the controller host.  Defaults to 10s, but this is handled by the shared module_utils code |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  **Choices:**   - `false` - `true` |

## [Notes](instance_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](instance_module.md#id4)

```yaml+jinja
- name: Create an instance
  awx.awx.instance:
    hostname: my-instance.prod.example.com
    capacity_adjustment: 0.4
    listener_port: 31337

- name: Deprovision the instance
  awx.awx.instance:
    hostname: my-instance.prod.example.com
    node_state: deprovisioning
```

### Authors

- Rick Elrod (@relrod)

### Collection links

- [Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
- [Homepage](https://www.ansible.com/)
- [Repository (Sources)](https://github.com/ansible/awx)
