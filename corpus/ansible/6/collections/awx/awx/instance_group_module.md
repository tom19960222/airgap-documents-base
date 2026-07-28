---
collection: ansible
version: "6"
title: "awx.awx.instance_group module – create, update, or destroy Automation Platform Controller instance groups."
source_url: https://docs.ansible.com/projects/ansible/6/collections/awx/awx/instance_group_module.html
fetched_at: 2026-07-27T16:45:27+00:00
---
# awx.awx.instance_group module – create, update, or destroy Automation Platform Controller instance groups.

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
> To use it in a playbook, specify: `awx.awx.instance_group`.

New in awx.awx 4.0.0

- [Synopsis](instance_group_module.md#synopsis)
- [Parameters](instance_group_module.md#parameters)
- [Notes](instance_group_module.md#notes)
- [Examples](instance_group_module.md#examples)

## [Synopsis](instance_group_module.md#id1)

- Create, update, or destroy Automation Platform Controller instance groups. See <https://www.ansible.com/tower> for an overview.

## [Parameters](instance_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **controller_config_file**  aliases: tower_config_file  path | Path to the controller config file.  If provided, the other locations for config files will not be considered. |
| **controller_host**  aliases: tower_host  string | URL to your Automation Platform Controller instance.  If value not set, will try environment variable `CONTROLLER_HOST` and then config files  If value not specified by any means, the value of `127.0.0.1` will be used |
| **controller_oauthtoken**  aliases: tower_oauthtoken  any  added in awx.awx 3.7.0 | The OAuth token to use.  This value can be in one of two formats.  A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)  A dictionary structure as returned by the token module.  If value not set, will try environment variable `CONTROLLER_OAUTH_TOKEN` and then config files |
| **controller_password**  aliases: tower_password  string | Password for your controller instance.  If value not set, will try environment variable `CONTROLLER_PASSWORD` and then config files |
| **controller_username**  aliases: tower_username  string | Username for your controller instance.  If value not set, will try environment variable `CONTROLLER_USERNAME` and then config files |
| **credential**  string | Credential to authenticate with Kubernetes or OpenShift. Must be of type “OpenShift or Kubernetes API Bearer Token”. |
| **instances**  list / elements=string | The instances associated with this instance_group |
| **is_container_group**  boolean | Signifies that this InstanceGroup should act as a ContainerGroup. If no credential is specified, the underlying Pod’s ServiceAccount will be used.  Choices:   - `false` ← (default) - `true` |
| **max_concurrent_jobs**  integer | Maximum number of concurrent jobs to run on this group. Zero means no limit.  Default: `0` |
| **max_forks**  integer | Max forks to execute on this group. Zero means no limit.  Default: `0` |
| **name**  string / required | Name of this instance group. |
| **new_name**  string | Setting this option will change the existing name (looked up via the name field. |
| **pod_spec_override**  string | A custom Kubernetes or OpenShift Pod specification. |
| **policy_instance_list**  list / elements=string | List of exact-match Instances that will be assigned to this group |
| **policy_instance_minimum**  integer | Static minimum number of Instances that will be automatically assign to this group when new instances come online.  Default: `0` |
| **policy_instance_percentage**  integer | Minimum percentage of all instances that will be automatically assigned to this group when new instances come online.  Default: `0` |
| **state**  string | Desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  aliases: tower_verify_ssl  boolean | Whether to allow insecure connections to AWX.  If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  If value not set, will try environment variable `CONTROLLER_VERIFY_SSL` and then config files  Choices:   - `false` - `true` |

## [Notes](instance_group_module.md#id3)

> **Note:**
>
> - If no *config_file* is provided we will attempt to use the tower-cli library defaults to find your host information.
> - *config_file* should be in the following format host=hostname username=username password=password

## [Examples](instance_group_module.md#id4)

```yaml+jinja

```

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

[Issue Tracker](https://github.com/ansible/awx/issues?q=is%3Aissue+label%3Acomponent%3Aawx_collection)
[Homepage](https://www.ansible.com/)
[Repository (Sources)](https://github.com/ansible/awx)
