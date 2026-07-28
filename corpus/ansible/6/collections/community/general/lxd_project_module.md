---
collection: ansible
version: "6"
title: "community.general.lxd_project module – Manage LXD projects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lxd_project_module.html
fetched_at: 2026-07-27T17:10:42+00:00
---
# community.general.lxd_project module – Manage LXD projects

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.lxd_project`.

New in community.general 4.8.0

- [Synopsis](lxd_project_module.md#synopsis)
- [Parameters](lxd_project_module.md#parameters)
- [Notes](lxd_project_module.md#notes)
- [Examples](lxd_project_module.md#examples)
- [Return Values](lxd_project_module.md#return-values)

## [Synopsis](lxd_project_module.md#id1)

- Management of LXD projects.

## [Parameters](lxd_project_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  aliases: cert_file  path | The client certificate file path.  If not specified, it defaults to `$HOME/.config/lxc/client.crt`. |
| **client_key**  aliases: key_file  path | The client certificate key file path.  If not specified, it defaults to `$HOME/.config/lxc/client.key`. |
| **config**  dictionary | The config for the project (for example `{"features.profiles": "true"}`). See <https://linuxcontainers.org/lxd/docs/master/projects/>.  If the project already exists and its “config” value in metadata obtained from `GET /1.0/projects/<name>` <https://linuxcontainers.org/lxd/docs/master/api/#/projects/project_get> are different, then this module tries to apply the configurations. |
| **description**  string | Description of the project. |
| **merge_project**  boolean | Merge the configuration of the present project with the new desired configuration, instead of replacing it. If configuration is the same after merged, no change will be made.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the project. |
| **new_name**  string | A new name of a project.  If this parameter is specified a project will be renamed to this name. See <https://linuxcontainers.org/lxd/docs/master/api/#/projects/project_post>. |
| **snap_url**  string | The Unix domain socket path when LXD is installed by snap package manager.  Default: `"unix:/var/snap/lxd/common/lxd/unix.socket"` |
| **state**  string | Define the state of a project.  Choices:   - `"present"` ← (default) - `"absent"` |
| **trust_password**  string | The client trusted password.  You need to set this password on the LXD server before running this module using the following command: `lxc config set core.trust_password <some random password>` See <https://www.stgraber.org/2016/04/18/lxd-api-direct-interaction/>.  If *trust_password* is set, this module send a request for authentication before sending any requests. |
| **url**  string | The Unix domain socket path or the https URL for the LXD server.  Default: `"unix:/var/lib/lxd/unix.socket"` |

## [Notes](lxd_project_module.md#id3)

> **Note:**
>
> - Projects must have a unique name. If you attempt to create a project with a name that already existed in the users namespace the module will simply return as “unchanged”.

## [Examples](lxd_project_module.md#id4)

```yaml+jinja
# An example for creating a project
- hosts: localhost
  connection: local
  tasks:
    - name: Create a project
      community.general.lxd_project:
        name: ansible-test-project
        state: present
        config: {}
        description: my new project

# An example for renaming a project
- hosts: localhost
  connection: local
  tasks:
    - name: Rename ansible-test-project to ansible-test-project-new-name
      community.general.lxd_project:
        name: ansible-test-project
        new_name: ansible-test-project-new-name
        state: present
        config: {}
        description: my new project
```

## [Return Values](lxd_project_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  list / elements=string | List of actions performed for the project.  Returned: success  Sample: `["create"]` |
| **logs**  list / elements=dictionary | The logs of requests and responses.  Returned: when ansible-playbook is invoked with -vvvv. |
| **request**  dictionary | HTTP request sent to LXD server.  Returned: success |
| **json**  string | JSON body of HTTP request.  Returned: success  Sample: `"(too long to be placed here)"` |
| **method**  string | Method of HTTP request.  Returned: success  Sample: `"GET"` |
| **timeout**  integer | Timeout of HTTP request, `null` if unset.  Returned: success |
| **url**  string | URL path of HTTP request.  Returned: success  Sample: `"/1.0/projects/test-project"` |
| **response**  dictionary | HTTP response received from LXD server.  Returned: success |
| **json**  string | JSON of HTTP response.  Returned: success  Sample: `"(too long to be placed here)"` |
| **type**  string | Type of actions performed, currently only `sent request`.  Returned: success  Sample: `"sent request"` |
| **old_state**  string | The old state of the project.  Returned: success  Sample: `"absent"` |

### Authors

- Raymond Chang (@we10710aa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
