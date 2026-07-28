---
collection: ansible
version: "8"
title: "community.general.python_requirements_info module – Show python path and assert dependency versions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/python_requirements_info_module.html
fetched_at: 2026-07-28T01:49:30+00:00
---
# community.general.python_requirements_info module – Show python path and assert dependency versions

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
> To use it in a playbook, specify: `community.general.python_requirements_info`.

- [Synopsis](python_requirements_info_module.md#synopsis)
- [Parameters](python_requirements_info_module.md#parameters)
- [Attributes](python_requirements_info_module.md#attributes)
- [Examples](python_requirements_info_module.md#examples)
- [Return Values](python_requirements_info_module.md#return-values)

## [Synopsis](python_requirements_info_module.md#id1)

- Get info about available Python requirements on the target host, including listing required libraries and gathering versions.
- This module was called `python_requirements_facts` before Ansible 2.9. The usage did not change.

Aliases: system.python_requirements_info

## [Parameters](python_requirements_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dependencies**  list / elements=string | A list of version-likes or module names to check for installation. Supported operators: <, >, <=, >=, or ==. The bare module name like `ansible`, the module with a specific version like `boto3==1.6.1`, or a partial version like `requests>2` are all valid specifications.  **Default:** `[]` |

## [Attributes](python_requirements_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](python_requirements_info_module.md#id4)

```yaml+jinja
- name: Show python lib/site paths
  community.general.python_requirements_info:

- name: Check for modern boto3 and botocore versions
  community.general.python_requirements_info:
    dependencies:
      - boto3>1.6
      - botocore<2
```

## [Return Values](python_requirements_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **mismatched**  dictionary | A dictionary of dependencies that did not satisfy the desired version  **Returned:** always  **Sample:** `{"botocore": {"desired": "botocore>2", "installed": "1.10.60"}}` |
| **not_found**  list / elements=string | A list of packages that could not be imported at all, and are not installed  **Returned:** always  **Sample:** `["boto4", "requests"]` |
| **python**  string | path to python version used  **Returned:** always  **Sample:** `"/usr/local/opt/python@2/bin/python2.7"` |
| **python_system_path**  list / elements=string | List of paths python is looking for modules in  **Returned:** always  **Sample:** `["/usr/local/opt/python@2/site-packages/", "/usr/lib/python/site-packages/"]` |
| **python_version**  string | version of python  **Returned:** always  **Sample:** `"2.7.15 (default, May  1 2018, 16:44:08) [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)]"` |
| **python_version_info**  dictionary  *added in community.general 4.2.0* | breakdown version of python  **Returned:** always |
| **major**  integer | The `major` component of the python interpreter version.  **Returned:** always  **Sample:** `3` |
| **micro**  integer | The `micro` component of the python interpreter version.  **Returned:** always  **Sample:** `10` |
| **minor**  integer | The `minor` component of the python interpreter version.  **Returned:** always  **Sample:** `8` |
| **releaselevel**  string | The `releaselevel` component of the python interpreter version.  **Returned:** always  **Sample:** `"final"` |
| **serial**  integer | The `serial` component of the python interpreter version.  **Returned:** always  **Sample:** `0` |
| **valid**  dictionary | A dictionary of dependencies that matched their desired versions. If no version was specified, then `desired` will be null  **Returned:** always  **Sample:** `{"boto3": {"desired": null, "installed": "1.7.60"}, "botocore": {"desired": "botocore<2", "installed": "1.10.60"}}` |

### Authors

- Will Thames (@willthames)
- Ryan Scott Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
