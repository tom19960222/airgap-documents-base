---
collection: ansible
version: "8"
title: "community.general.gunicorn module – Run gunicorn with various settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/gunicorn_module.html
fetched_at: 2026-07-28T01:45:57+00:00
---
# community.general.gunicorn module – Run gunicorn with various settings

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](gunicorn_module.md#ansible-collections-community-general-gunicorn-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.gunicorn`.

- [Synopsis](gunicorn_module.md#synopsis)
- [Requirements](gunicorn_module.md#requirements)
- [Parameters](gunicorn_module.md#parameters)
- [Attributes](gunicorn_module.md#attributes)
- [Notes](gunicorn_module.md#notes)
- [Examples](gunicorn_module.md#examples)
- [Return Values](gunicorn_module.md#return-values)

## [Synopsis](gunicorn_module.md#id1)

- Starts gunicorn with the parameters specified. Common settings for gunicorn configuration are supported. For additional configuration use a config file See <https://gunicorn-docs.readthedocs.io/en/latest/settings.html> for more options. It’s recommended to always use the chdir option to avoid problems with the location of the app.

Aliases: web_infrastructure.gunicorn

## [Requirements](gunicorn_module.md#id2)

The below requirements are needed on the host that executes this module.

- gunicorn

## [Parameters](gunicorn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app**  aliases: name  string / required | The app module. A name refers to a WSGI callable that should be found in the specified module. |
| **chdir**  path | Chdir to specified directory before apps loading. |
| **config**  aliases: conf  path | Path to the gunicorn configuration file. |
| **pid**  path | A filename to use for the PID file. If not set and not found on the configuration file a tmp pid file will be created to check a successful run of gunicorn. |
| **user**  string | Switch worker processes to run as this user. |
| **venv**  aliases: virtualenv  path | Path to the virtualenv directory. |
| **worker**  string | The type of workers to use. The default class (sync) should handle most “normal” types of workloads.  **Choices:**   - `"sync"` - `"eventlet"` - `"gevent"` - `"tornado "` - `"gthread"` - `"gaiohttp"` |

## [Attributes](gunicorn_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](gunicorn_module.md#id5)

> **Note:**
>
> - If not specified on config file, a temporary error log will be created on /tmp dir. Please make sure you have write access in /tmp dir. Not needed but will help you to identify any problem with configuration.

## [Examples](gunicorn_module.md#id6)

```yaml+jinja
- name: Simple gunicorn run example
  community.general.gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'

- name: Run gunicorn on a virtualenv
  community.general.gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'
    venv: '/workspace/example/venv'

- name: Run gunicorn with a config file
  community.general.gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'
    conf: '/workspace/example/gunicorn.cfg'

- name: Run gunicorn as ansible user with specified pid and config file
  community.general.gunicorn:
    app: 'wsgi'
    chdir: '/workspace/example'
    conf: '/workspace/example/gunicorn.cfg'
    venv: '/workspace/example/venv'
    pid: '/workspace/example/gunicorn.pid'
    user: 'ansible'
```

## [Return Values](gunicorn_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **gunicorn**  string | process id of gunicorn  **Returned:** changed  **Sample:** `"1234"` |

### Authors

- Alejandro Gomez (@agmezr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
