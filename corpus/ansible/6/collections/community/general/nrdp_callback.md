---
collection: ansible
version: "6"
title: "community.general.nrdp callback – Post task results to a Nagios server through nrdp"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/nrdp_callback.html
fetched_at: 2026-07-27T17:14:33+00:00
---
# community.general.nrdp callback – Post task results to a Nagios server through nrdp

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.nrdp`.

- [Callback plugin](nrdp_callback.md#callback-plugin)
- [Synopsis](nrdp_callback.md#synopsis)
- [Parameters](nrdp_callback.md#parameters)

## [Callback plugin](nrdp_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](nrdp_callback.md#id2)

- This callback send playbook result to Nagios.
- Nagios shall use NRDP to recive passive events.
- The passive check is sent to a dedicated host/service for Ansible.

## [Parameters](nrdp_callback.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | Hostname where the passive check is linked to.  Configuration:   - INI entry:  ```YAML+Jinja   [callback_nrdp]   hostname = VALUE   ``` - Environment variable: [`NRDP_HOSTNAME`](../../environment_variables.md#envvar-NRDP_HOSTNAME) |
| **servicename**  string / required | Service where the passive check is linked to.  Configuration:   - INI entry:  ```YAML+Jinja   [callback_nrdp]   servicename = VALUE   ``` - Environment variable: [`NRDP_SERVICENAME`](../../environment_variables.md#envvar-NRDP_SERVICENAME) |
| **token**  string / required | Token to be allowed to push nrdp events.  Configuration:   - INI entry:  ```YAML+Jinja   [callback_nrdp]   token = VALUE   ``` - Environment variable: [`NRDP_TOKEN`](../../environment_variables.md#envvar-NRDP_TOKEN) |
| **url**  string / required | URL of the nrdp server.  Configuration:   - INI entry:  ```YAML+Jinja   [callback_nrdp]   url = VALUE   ``` - Environment variable: [`NRDP_URL`](../../environment_variables.md#envvar-NRDP_URL) |
| **validate_certs**  aliases: validate_nrdp_certs  boolean | Validate the SSL certificate of the nrdp server. (Used for HTTPS URLs.)  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entries:  ```YAML+Jinja   [callback_nrdp]   validate_nrdp_certs = false   ```  ```YAML+Jinja   [callback_nrdp]   validate_certs = false   ``` - Environment variable: [`NRDP_VALIDATE_CERTS`](../../environment_variables.md#envvar-NRDP_VALIDATE_CERTS) |

### Authors

- Remi VERCHERE (@rverchere)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
