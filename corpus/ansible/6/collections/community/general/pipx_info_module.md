---
collection: ansible
version: "6"
title: "community.general.pipx_info module – Rretrieves information about applications installed with pipx"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pipx_info_module.html
fetched_at: 2026-07-27T17:11:54+00:00
---
# community.general.pipx_info module – Rretrieves information about applications installed with pipx

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
> To use it in a playbook, specify: `community.general.pipx_info`.

New in community.general 5.6.0

- [Synopsis](pipx_info_module.md#synopsis)
- [Parameters](pipx_info_module.md#parameters)
- [Notes](pipx_info_module.md#notes)
- [Examples](pipx_info_module.md#examples)
- [Return Values](pipx_info_module.md#return-values)

## [Synopsis](pipx_info_module.md#id1)

- Retrieve details about Python applications installed in isolated virtualenvs using pipx.

## [Parameters](pipx_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **executable**  path | Path to the `pipx` installed in the system.  If not specified, the module will use `python -m pipx` to run the tool, using the same Python interpreter as ansible itself. |
| **include_deps**  boolean | Include dependent packages in the output.  Choices:   - `false` ← (default) - `true` |
| **include_injected**  boolean | Include injected packages in the output.  Choices:   - `false` ← (default) - `true` |
| **include_raw**  boolean | Returns the raw output of `pipx list --json`.  The raw output is not affected by *include_deps* or *include_injected*.  Choices:   - `false` ← (default) - `true` |
| **name**  string | Name of an application installed with `pipx`. |

## [Notes](pipx_info_module.md#id3)

> **Note:**
>
> - This module does not install the `pipx` python package, however that can be easily done with the module [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - This module does not require `pipx` to be in the shell `PATH`, but it must be loadable by Python as a module.
> - Please note that `pipx` requires Python 3.6 or above.
> - See also the `pipx` documentation at <https://pypa.github.io/pipx/>.

## [Examples](pipx_info_module.md#id4)

```yaml+jinja
- name: retrieve all installed applications
  community.general.pipx_info: {}

- name: retrieve all installed applications, include dependencies and injected packages
  community.general.pipx_info:
    include_deps: true
    include_injected: true

- name: retrieve application tox
  community.general.pipx_info:
    name: tox
    include_deps: true

- name: retrieve application ansible-lint, include dependencies
  community.general.pipx_info:
    name: ansible-lint
    include_deps: true
```

## [Return Values](pipx_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **application**  list / elements=dictionary | The list of installed applications  Returned: success |
| **dependencies**  list / elements=string | The dependencies of the installed application, when *include_deps=true*.  Returned: success  Sample: `["virtualenv"]` |
| **injected**  dictionary | The injected packages for the installed application, when *include_injected=true*.  Returned: success  Sample: `{"licenses": "0.6.1"}` |
| **name**  string | The name of the installed application.  Returned: success  Sample: `"tox"` |
| **version**  string | The version of the installed application.  Returned: success  Sample: `"3.24.0"` |
| **cmd**  list / elements=string | Command executed to obtain the list of installed applications.  Returned: success  Sample: `["/usr/bin/python3.10", "-m", "pipx", "list", "--include-injected", "--json"]` |
| **raw_output**  dictionary | The raw output of the `pipx list` command, when *include_raw=true*. Used for debugging.  Returned: success |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
