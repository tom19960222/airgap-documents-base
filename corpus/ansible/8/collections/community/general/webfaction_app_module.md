---
collection: ansible
version: "8"
title: "community.general.webfaction_app module – Add or remove applications on a Webfaction host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/webfaction_app_module.html
fetched_at: 2026-07-28T01:51:24+00:00
---
# community.general.webfaction_app module – Add or remove applications on a Webfaction host

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.webfaction_app`.

- [DEPRECATED](webfaction_app_module.md#deprecated)
- [Synopsis](webfaction_app_module.md#synopsis)
- [Parameters](webfaction_app_module.md#parameters)
- [Attributes](webfaction_app_module.md#attributes)
- [Notes](webfaction_app_module.md#notes)
- [Examples](webfaction_app_module.md#examples)
- [Status](webfaction_app_module.md#status)

## [DEPRECATED](webfaction_app_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   the endpoints this module relies on do not exist any more and do not resolve to IPs in DNS.

Alternative:
:   no known alternative at this point

## [Synopsis](webfaction_app_module.md#id2)

- Add or remove applications on a Webfaction host. Further documentation at <https://github.com/quentinsf/ansible-webfaction>.

Aliases: cloud.webfaction.webfaction_app

## [Parameters](webfaction_app_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autostart**  boolean | Whether the app should restart with an `autostart.cgi` script  **Choices:**   - `false` ← (default) - `true` |
| **extra_info**  string | Any extra parameters required by the app  **Default:** `""` |
| **login_name**  string / required | The webfaction account to use |
| **login_password**  string / required | The webfaction password to use |
| **machine**  string | The machine name to use (optional for accounts with only one machine) |
| **name**  string / required | The name of the application |
| **port_open**  boolean | IF the port should be opened  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether the application should exist  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | The type of application to create. See the Webfaction docs at <https://docs.webfaction.com/xmlrpc-api/apps.html> for a list. |

## [Attributes](webfaction_app_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](webfaction_app_module.md#id5)

> **Note:**
>
> - You can run playbooks that use this on a local machine, or on a Webfaction host, or elsewhere, since the scripts use the remote webfaction API. The location is not important. However, running them on multiple hosts *simultaneously* is best avoided. If you do not specify `localhost` as your host, you may want to add `serial=1` to the plays.
> - See [the webfaction API](https://docs.webfaction.com/xmlrpc-api/) for more info.

## [Examples](webfaction_app_module.md#id6)

```yaml+jinja
- name: Create a test app
  community.general.webfaction_app:
    name: "my_wsgi_app1"
    state: present
    type: mod_wsgi35-python27
    login_name: "{{webfaction_user}}"
    login_password: "{{webfaction_passwd}}"
    machine: "{{webfaction_machine}}"
```

## [Status](webfaction_app_module.md#id7)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](webfaction_app_module.md#deprecated).

### Authors

- Quentin Stafford-Fraser (@quentinsf)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
