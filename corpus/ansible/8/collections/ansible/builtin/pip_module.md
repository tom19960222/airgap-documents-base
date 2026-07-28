---
collection: ansible
version: "8"
title: "ansible.builtin.pip module – Manages Python library dependencies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/pip_module.html
fetched_at: 2026-07-28T01:07:39+00:00
---
# ansible.builtin.pip module – Manages Python library dependencies

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `pip` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.pip` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](pip_module.md#synopsis)
- [Requirements](pip_module.md#requirements)
- [Parameters](pip_module.md#parameters)
- [Attributes](pip_module.md#attributes)
- [Notes](pip_module.md#notes)
- [Examples](pip_module.md#examples)
- [Return Values](pip_module.md#return-values)

## [Synopsis](pip_module.md#id1)

- Manage Python library dependencies. To use this module, one of the following keys is required: `name` or `requirements`.

## [Requirements](pip_module.md#id2)

The below requirements are needed on the host that executes this module.

- pip
- virtualenv
- setuptools

## [Parameters](pip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chdir**  path | cd into this directory before running the command |
| **editable**  boolean | Pass the editable flag.  **Choices:**   - `false` ← (default) - `true` |
| **executable**  path | The explicit executable or pathname for the pip executable, if different from the Ansible Python interpreter. For example `pip3.3`, if there are both Python 2.7 and 3.3 installations in the system and you want to run pip for the Python 3.3 installation.  Mutually exclusive with *virtualenv* (added in 2.1).  Does not affect the Ansible Python interpreter.  The setuptools package must be installed for both the Ansible Python interpreter and for the version of Python specified by this option. |
| **extra_args**  string | Extra arguments passed to pip. |
| **name**  list / elements=string | The name of a Python library to install or the url(bzr+,hg+,git+,svn+) of the remote package.  This can be a list (since 2.2) and contain version specifiers (since 2.7). |
| **requirements**  string | The path to a pip requirements file, which should be local to the remote system. File can be specified as a relative path if using the chdir option. |
| **state**  string | The state of module  The ‘forcereinstall’ option is only available in Ansible 2.1 and above.  **Choices:**   - `"absent"` - `"forcereinstall"` - `"latest"` - `"present"` ← (default) |
| **umask**  string | The system umask to apply before installing the pip package. This is useful, for example, when installing on systems that have a very restrictive umask by default (e.g., “0077”) and you want to pip install packages which are to be used by all users. Note that this requires you to specify desired umask mode as an octal string, (e.g., “0022”). |
| **version**  string | The version number to install of the Python library specified in the *name* parameter. |
| **virtualenv**  path | An optional path to a *virtualenv* directory to install into. It cannot be specified together with the ‘executable’ parameter (added in 2.1). If the virtualenv does not exist, it will be created before installing packages. The optional virtualenv_site_packages, virtualenv_command, and virtualenv_python options affect the creation of the virtualenv. |
| **virtualenv_command**  path | The command or a pathname to the command to create the virtual environment with. For example `pyvenv`, `virtualenv`, `virtualenv2`, `~/bin/virtualenv`, `/usr/local/bin/virtualenv`.  **Default:** `"virtualenv"` |
| **virtualenv_python**  string | The Python executable used for creating the virtual environment. For example `python3.5`, `python2.7`. When not specified, the Python version used to run the ansible module is used. This parameter should not be used when `virtualenv_command` is using `pyvenv` or the `-m venv` module. |
| **virtualenv_site_packages**  boolean | Whether the virtual environment will inherit packages from the global site-packages directory. Note that if this setting is changed on an already existing virtual environment it will not have any effect, the environment must be deleted and newly created.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](pip_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](pip_module.md#id5)

> **Note:**
>
> - Python installations marked externally-managed (as defined by PEP668) cannot be updated by pip versions >= 23.0.1 without the use of a virtual environment or setting the environment variable ``PIP_BREAK_SYSTEM_PACKAGES=1``.
> - The virtualenv (<http://www.virtualenv.org/>) must be installed on the remote host if the virtualenv parameter is specified and the virtualenv needs to be created.
> - Although it executes using the Ansible Python interpreter, the pip module shells out to run the actual pip command, so it can use any pip version you specify with *executable*. By default, it uses the pip version for the Ansible Python interpreter. For example, pip3 on python 3, and pip2 or pip on python 2.
> - The interpreter used by Ansible (see [ansible_python_interpreter](../../../inventory_guide/intro_inventory.md#ansible-python-interpreter)) requires the setuptools package, regardless of the version of pip set with the *executable* option.

## [Examples](pip_module.md#id6)

```yaml+jinja
- name: Install bottle python package
  ansible.builtin.pip:
    name: bottle

- name: Install bottle python package on version 0.11
  ansible.builtin.pip:
    name: bottle==0.11

- name: Install bottle python package with version specifiers
  ansible.builtin.pip:
    name: bottle>0.10,<0.20,!=0.11

- name: Install multi python packages with version specifiers
  ansible.builtin.pip:
    name:
      - django>1.11.0,<1.12.0
      - bottle>0.10,<0.20,!=0.11

- name: Install python package using a proxy
  ansible.builtin.pip:
    name: six
  environment:
    http_proxy: 'http://127.0.0.1:8080'
    https_proxy: 'https://127.0.0.1:8080'

# You do not have to supply '-e' option in extra_args
- name: Install MyApp using one of the remote protocols (bzr+,hg+,git+,svn+)
  ansible.builtin.pip:
    name: svn+http://myrepo/svn/MyApp#egg=MyApp

- name: Install MyApp using one of the remote protocols (bzr+,hg+,git+)
  ansible.builtin.pip:
    name: git+http://myrepo/app/MyApp

- name: Install MyApp from local tarball
  ansible.builtin.pip:
    name: file:///path/to/MyApp.tar.gz

- name: Install bottle into the specified (virtualenv), inheriting none of the globally installed modules
  ansible.builtin.pip:
    name: bottle
    virtualenv: /my_app/venv

- name: Install bottle into the specified (virtualenv), inheriting globally installed modules
  ansible.builtin.pip:
    name: bottle
    virtualenv: /my_app/venv
    virtualenv_site_packages: yes

- name: Install bottle into the specified (virtualenv), using Python 2.7
  ansible.builtin.pip:
    name: bottle
    virtualenv: /my_app/venv
    virtualenv_command: virtualenv-2.7

- name: Install bottle within a user home directory
  ansible.builtin.pip:
    name: bottle
    extra_args: --user

- name: Install specified python requirements
  ansible.builtin.pip:
    requirements: /my_app/requirements.txt

- name: Install specified python requirements in indicated (virtualenv)
  ansible.builtin.pip:
    requirements: /my_app/requirements.txt
    virtualenv: /my_app/venv

- name: Install specified python requirements and custom Index URL
  ansible.builtin.pip:
    requirements: /my_app/requirements.txt
    extra_args: -i https://example.com/pypi/simple

- name: Install specified python requirements offline from a local directory with downloaded packages
  ansible.builtin.pip:
    requirements: /my_app/requirements.txt
    extra_args: "--no-index --find-links=file:///my_downloaded_packages_dir"

- name: Install bottle for Python 3.3 specifically, using the 'pip3.3' executable
  ansible.builtin.pip:
    name: bottle
    executable: pip3.3

- name: Install bottle, forcing reinstallation if it's already installed
  ansible.builtin.pip:
    name: bottle
    state: forcereinstall

- name: Install bottle while ensuring the umask is 0022 (to ensure other users can use it)
  ansible.builtin.pip:
    name: bottle
    umask: "0022"
  become: True
```

## [Return Values](pip_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | pip command used by the module  **Returned:** success  **Sample:** `"pip2 install ansible six"` |
| **name**  list / elements=string | list of python modules targeted by pip  **Returned:** success  **Sample:** `["ansible", "six"]` |
| **requirements**  string | Path to the requirements file  **Returned:** success, if a requirements file was provided  **Sample:** `"/srv/git/project/requirements.txt"` |
| **version**  string | Version of the package specified in ‘name’  **Returned:** success, if a name and version were provided  **Sample:** `"2.5.1"` |
| **virtualenv**  string | Path to the virtualenv  **Returned:** success, if a virtualenv path was provided  **Sample:** `"/tmp/virtualenv"` |

### Authors

- Matt Wright (@mattupstate)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
