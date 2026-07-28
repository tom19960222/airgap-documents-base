---
collection: ansible
version: "8"
title: "community.general.django_manage module – Manages a Django application"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/django_manage_module.html
fetched_at: 2026-07-28T01:45:23+00:00
---
# community.general.django_manage module – Manages a Django application

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
> see [Requirements](django_manage_module.md#ansible-collections-community-general-django-manage-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.django_manage`.

- [Synopsis](django_manage_module.md#synopsis)
- [Requirements](django_manage_module.md#requirements)
- [Parameters](django_manage_module.md#parameters)
- [Attributes](django_manage_module.md#attributes)
- [Notes](django_manage_module.md#notes)
- [See Also](django_manage_module.md#see-also)
- [Examples](django_manage_module.md#examples)

## [Synopsis](django_manage_module.md#id1)

- Manages a Django application using the `manage.py` application frontend to `django-admin`. With the `virtualenv` parameter, all management commands will be executed by the given `virtualenv` installation.

Aliases: web_infrastructure.django_manage

## [Requirements](django_manage_module.md#id2)

The below requirements are needed on the host that executes this module.

- virtualenv
- django

## [Parameters](django_manage_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ack_venv_creation_deprecation**  boolean  *added in community.general 5.8.0* | When a `virtualenv` is set but the virtual environment does not exist, the current behavior is to create a new virtual environment. That behavior is deprecated and if that case happens it will generate a deprecation warning. Set this flag to `true` to suppress the deprecation warning.  Please note that you will receive no further warning about this being removed until the module will start failing in such cases from community.general 9.0.0 on.  **Choices:**   - `false` - `true` |
| **apps**  string | A list of space-delimited apps to target. Used by the `test` command. |
| **cache_table**  string | The name of the table used for database-backed caching. Used by the `createcachetable` command. |
| **clear**  boolean | Clear the existing files before trying to copy or link the original file.  Used only with the `collectstatic` command. The `--noinput` argument will be added automatically.  **Choices:**   - `false` ← (default) - `true` |
| **command**  string / required | The name of the Django management command to run. The commands listed below are built in this module and have some basic parameter validation.  `cleanup` - clean up old data from the database (deprecated in Django 1.5). This parameter will be removed in community.general 9.0.0. Use `clearsessions` instead.  `collectstatic` - Collects the static files into `STATIC_ROOT`.  `createcachetable` - Creates the cache tables for use with the database cache backend.  `flush` - Removes all data from the database.  `loaddata` - Searches for and loads the contents of the named `fixtures` into the database.  `migrate` - Synchronizes the database state with models and migrations.  `syncdb` - Synchronizes the database state with models and migrations (deprecated in Django 1.7). This parameter will be removed in community.general 9.0.0. Use `migrate` instead.  `test` - Runs tests for all installed apps.  `validate` - Validates all installed models (deprecated in Django 1.7). This parameter will be removed in community.general 9.0.0. Use `check` instead.  Other commands can be entered, but will fail if they are unknown to Django. Other commands that may prompt for user input should be run with the `--noinput` flag. |
| **database**  string | The database to target. Used by the `createcachetable`, `flush`, `loaddata`, `syncdb`, and `migrate` commands. |
| **failfast**  aliases: fail_fast  boolean | Fail the command immediately if a test fails. Used by the `test` command.  **Choices:**   - `false` ← (default) - `true` |
| **fixtures**  string | A space-delimited list of fixture file names to load in the database. **Required** by the `loaddata` command. |
| **link**  boolean | Will create links to the files instead of copying them, you can only use this parameter with `collectstatic` command.  **Choices:**   - `false` - `true` |
| **merge**  boolean | Will run out-of-order or missing migrations as they are not rollback migrations, you can only use this parameter with `migrate` command.  **Choices:**   - `false` - `true` |
| **project_path**  aliases: app_path, chdir  path / required | The path to the root of the Django application where `manage.py` lives. |
| **pythonpath**  aliases: python_path  path | A directory to add to the Python path. Typically used to include the settings module if it is located external to the application directory.  This would be equivalent to adding `pythonpath`‘s value to the `PYTHONPATH` environment variable. |
| **settings**  path | The Python path to the application’s settings module, such as `myapp.settings`. |
| **skip**  boolean | Will skip over out-of-order missing migrations, you can only use this parameter with `migrate` command.  **Choices:**   - `false` - `true` |
| **testrunner**  aliases: test_runner  string | Controls the test runner class that is used to execute tests.  This parameter is passed as-is to `manage.py`. |
| **virtualenv**  aliases: virtual_env  path | An optional path to a `virtualenv` installation to use while running the manage application. |

## [Attributes](django_manage_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](django_manage_module.md#id5)

> **Note:**
>
> - **ATTENTION - DEPRECATION**: Support for Django releases older than 4.1 will be removed in community.general version 9.0.0 (estimated to be released in May 2024). Please notice that Django 4.1 requires Python 3.8 or greater.
> - `virtualenv` (<http://www.virtualenv.org>) must be installed on the remote host if the `virtualenv` parameter is specified. This requirement is deprecated and will be removed in community.general version 9.0.0.
> - This module will create a virtualenv if the `virtualenv` parameter is specified and a virtual environment does not already exist at the given location. This behavior is deprecated and will be removed in community.general version 9.0.0.
> - The parameter `virtualenv` will remain in use, but it will require the specified virtualenv to exist. The recommended way to create one in Ansible is by using [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - This module assumes English error messages for the `createcachetable` command to detect table existence, unfortunately.
> - To be able to use the `migrate` command with django versions < 1.7, you must have `south` installed and added as an app in your settings.
> - To be able to use the `collectstatic` command, you must have enabled staticfiles in your settings.
> - Your `manage.py` application must be executable (`rwxr-xr-x`), and must have a valid shebang, for example `#!/usr/bin/env python`, for invoking the appropriate Python interpreter.

## [See Also](django_manage_module.md#id6)

> **See also:**
>
> [django-admin and manage.py Reference](https://docs.djangoproject.com/en/4.1/ref/django-admin/)
> :   Reference for `django-admin` or `manage.py` commands.
>
> [Django Download page](https://www.djangoproject.com/download/)
> :   The page showing how to get Django and the timeline of supported releases.
>
> [What Python version can I use with Django?](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django)
> :   From the Django FAQ, the response to Python requirements for the framework.

## [Examples](django_manage_module.md#id7)

```yaml+jinja
- name: Run cleanup on the application installed in django_dir
  community.general.django_manage:
    command: cleanup
    project_path: "{{ django_dir }}"

- name: Load the initial_data fixture into the application
  community.general.django_manage:
    command: loaddata
    project_path: "{{ django_dir }}"
    fixtures: "{{ initial_data }}"

- name: Run syncdb on the application
  community.general.django_manage:
    command: syncdb
    project_path: "{{ django_dir }}"
    settings: "{{ settings_app_name }}"
    pythonpath: "{{ settings_dir }}"
    virtualenv: "{{ virtualenv_dir }}"

- name: Run the SmokeTest test case from the main app. Useful for testing deploys
  community.general.django_manage:
    command: test
    project_path: "{{ django_dir }}"
    apps: main.SmokeTest

- name: Create an initial superuser
  community.general.django_manage:
    command: "createsuperuser --noinput --username=admin --email=admin@example.com"
    project_path: "{{ django_dir }}"
```

### Authors

- Alexei Znamensky (@russoz)
- Scott Anderson (@tastychutney)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
