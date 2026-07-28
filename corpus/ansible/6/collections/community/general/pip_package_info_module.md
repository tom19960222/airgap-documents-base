---
collection: ansible
version: "6"
title: "community.general.pip_package_info module – Pip package information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pip_package_info_module.html
fetched_at: 2026-07-27T17:11:52+00:00
---
# community.general.pip_package_info module – Pip package information

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pip_package_info_module.md#ansible-collections-community-general-pip-package-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pip_package_info`.

- [Synopsis](pip_package_info_module.md#synopsis)
- [Requirements](pip_package_info_module.md#requirements)
- [Parameters](pip_package_info_module.md#parameters)
- [Examples](pip_package_info_module.md#examples)
- [Return Values](pip_package_info_module.md#return-values)

## [Synopsis](pip_package_info_module.md#id1)

- Return information about installed pip packages

## [Requirements](pip_package_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- The requested pip executables must be installed on the target.

## [Parameters](pip_package_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clients**  list / elements=path | A list of the pip executables that will be used to get the packages. They can be supplied with the full path or just the executable name, for example `pip3.7`.  Default: `["pip"]` |

## [Examples](pip_package_info_module.md#id4)

```yaml+jinja
- name: Just get the list from default pip
  community.general.pip_package_info:

- name: Get the facts for default pip, pip2 and pip3.6
  community.general.pip_package_info:
    clients: ['pip', 'pip2', 'pip3.6']

- name: Get from specific paths (virtualenvs?)
  community.general.pip_package_info:
    clients: '/home/me/projec42/python/pip3.5'
```

## [Return Values](pip_package_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **packages**  dictionary | a dictionary of installed package data  Returned: always |
| **python**  dictionary | A dictionary with each pip client which then contains a list of dicts with python package information  Returned: always  Sample: `{"packages": {"pip": {"Babel": [{"name": "Babel", "source": "pip", "version": "2.6.0"}], "Flask": [{"name": "Flask", "source": "pip", "version": "1.0.2"}], "Flask-SQLAlchemy": [{"name": "Flask-SQLAlchemy", "source": "pip", "version": "2.3.2"}], "Jinja2": [{"name": "Jinja2", "source": "pip", "version": "2.10"}]}}}` |

### Authors

- Matthew Jones (@matburt)
- Brian Coca (@bcoca)
- Adam Miller (@maxamillion)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
