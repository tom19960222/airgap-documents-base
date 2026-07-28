---
collection: ansible
version: "8"
title: "community.general.pipx module – Manages applications installed with pipx"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pipx_module.html
fetched_at: 2026-07-28T01:49:02+00:00
---
# community.general.pipx module – Manages applications installed with pipx

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
> To use it in a playbook, specify: `community.general.pipx`.

New in community.general 3.8.0

- [Synopsis](pipx_module.md#synopsis)
- [Parameters](pipx_module.md#parameters)
- [Attributes](pipx_module.md#attributes)
- [Notes](pipx_module.md#notes)
- [Examples](pipx_module.md#examples)

## [Synopsis](pipx_module.md#id1)

- Manage Python applications installed in isolated virtualenvs using pipx.

Aliases: packaging.language.pipx

## [Parameters](pipx_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **editable**  boolean  *added in community.general 4.6.0* | Install the project in editable mode.  **Choices:**   - `false` ← (default) - `true` |
| **executable**  path | Path to the `pipx` installed in the system.  If not specified, the module will use `python -m pipx` to run the tool, using the same Python interpreter as ansible itself. |
| **force**  boolean | Force modification of the application’s virtual environment. See `pipx` for details.  Only used when `state=install`, `state=upgrade`, `state=upgrade_all`, `state=latest`, or `state=inject`.  **Choices:**   - `false` ← (default) - `true` |
| **include_injected**  boolean | Upgrade the injected packages along with the application.  Only used when `state=upgrade`, `state=upgrade_all`, or `state=latest`.  This is used with `state=upgrade` and `state=latest` since community.general 6.6.0.  **Choices:**   - `false` ← (default) - `true` |
| **index_url**  string | Base URL of Python Package Index.  Only used when `state=install`, `state=upgrade`, `state=latest`, or `state=inject`. |
| **inject_packages**  list / elements=string | Packages to be injected into an existing virtual environment.  Only used when `state=inject`. |
| **install_apps**  boolean  *added in community.general 6.5.0* | Add apps from the injected packages.  Only used when `state=inject`.  **Choices:**   - `false` ← (default) - `true` |
| **install_deps**  boolean | Include applications of dependent packages.  Only used when `state=install`, `state=latest`, or `state=inject`.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of the application to be installed. It must to be a simple package name. For passing package specifications or installing from URLs or directories, please use the `source` option. |
| **pip_args**  string  *added in community.general 4.6.0* | Arbitrary arguments to pass directly to `pip`. |
| **python**  string | Python version to be used when creating the application virtual environment. Must be 3.6+.  Only used when `state=install`, `state=latest`, `state=reinstall`, or `state=reinstall_all`. |
| **source**  string | If the application source, such as a package with version specifier, or an URL, directory or any other accepted specification. See `pipx` documentation for more details.  When specified, the `pipx` command will use `source` instead of `name`. |
| **state**  string | Desired state for the application.  The states `present` and `absent` are aliases to `install` and `uninstall`, respectively.  The state `latest` is equivalent to executing the task twice, with state `install` and then `upgrade`. It was added in community.general 5.5.0.  **Choices:**   - `"present"` - `"absent"` - `"install"` ← (default) - `"uninstall"` - `"uninstall_all"` - `"inject"` - `"upgrade"` - `"upgrade_all"` - `"reinstall"` - `"reinstall_all"` - `"latest"` |
| **system_site_packages**  boolean  *added in community.general 6.6.0* | Give application virtual environment access to the system site-packages directory.  Only used when `state=install` or `state=latest`.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](pipx_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pipx_module.md#id4)

> **Note:**
>
> - This module does not install the `pipx` python package, however that can be easily done with the module [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).
> - This module does not require `pipx` to be in the shell `PATH`, but it must be loadable by Python as a module.
> - This module will honor `pipx` environment variables such as but not limited to `PIPX_HOME` and `PIPX_BIN_DIR` passed using the [environment Ansible keyword](../../../playbook_guide/playbooks_environment.md#playbooks-environment).
> - This module requires `pipx` version 0.16.2.1 or above.
> - Please note that `pipx` requires Python 3.6 or above.
> - This first implementation does not verify whether a specified version constraint has been installed or not. Hence, when using version operators, `pipx` module will always try to execute the operation, even when the application was previously installed. This feature will be added in the future.
> - See also the `pipx` documentation at <https://pypa.github.io/pipx/>.

## [Examples](pipx_module.md#id5)

```yaml+jinja
- name: Install tox
  community.general.pipx:
    name: tox

- name: Install tox from git repository
  community.general.pipx:
    name: tox
    source: git+https://github.com/tox-dev/tox.git

- name: Upgrade tox
  community.general.pipx:
    name: tox
    state: upgrade

- name: Reinstall black with specific Python version
  community.general.pipx:
    name: black
    state: reinstall
    python: 3.7

- name: Uninstall pycowsay
  community.general.pipx:
    name: pycowsay
    state: absent
```

### Authors

- Alexei Znamensky (@russoz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
