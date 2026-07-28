---
collection: ansible
version: "6"
title: "Ansible and BSD"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/intro_bsd.html
fetched_at: 2026-07-27T16:40:30+00:00
---
# Ansible and BSD

Managing BSD machines is different from managing other Unix-like machines. If you have managed nodes running BSD, review these topics.

- [Connecting to BSD nodes](intro_bsd.md#connecting-to-bsd-nodes)
- [Bootstrapping BSD](intro_bsd.md#bootstrapping-bsd)
- [Setting the Python interpreter](intro_bsd.md#setting-the-python-interpreter)

  - [FreeBSD packages and ports](intro_bsd.md#freebsd-packages-and-ports)
  - [INTERPRETER_PYTHON_FALLBACK](intro_bsd.md#interpreter-python-fallback)
  - [Debug the discovery of Python](intro_bsd.md#debug-the-discovery-of-python)
  - [Additional variables](intro_bsd.md#additional-variables)
- [Which modules are available?](intro_bsd.md#which-modules-are-available)
- [Using BSD as the control node](intro_bsd.md#using-bsd-as-the-control-node)
- [BSD facts](intro_bsd.md#bsd-facts)
- [BSD efforts and contributions](intro_bsd.md#bsd-efforts-and-contributions)

## [Connecting to BSD nodes](intro_bsd.md#id2)

Ansible connects to managed nodes using OpenSSH by default. This works on BSD if you use SSH keys for authentication. However, if you use SSH passwords for authentication, Ansible relies on sshpass. Most
versions of sshpass do not deal well with BSD login prompts, so when using SSH passwords against BSD machines, use `paramiko` to connect instead of OpenSSH. You can do this in ansible.cfg globally or you can set it as an inventory/group/host variable. For example:

```
[freebsd]
mybsdhost1 ansible_connection=paramiko
```

## [Bootstrapping BSD](intro_bsd.md#id3)

Ansible is agentless by default, however, it requires Python on managed nodes. Only the [raw](../collections/ansible/builtin/raw_module.md#raw-module) module will operate without Python. Although this module can be used to bootstrap Ansible and install Python on BSD variants (see below), it is very limited and the use of Python is required to make full use of Ansible’s features.

The following example installs Python which includes the json library required for full functionality of Ansible.
On your control machine you can execute the following for most versions of FreeBSD:

```bash
ansible -m raw -a "pkg install -y python" mybsdhost1
```

Or for OpenBSD:

```bash
ansible -m raw -a "pkg_add python%3.8"
```

Once this is done you can now use other Ansible modules apart from the `raw` module.

> **Note:**
>
> This example demonstrated using pkg on FreeBSD and pkg_add on OpenBSD, however you should be able to substitute the appropriate package tool for your BSD; the package name may also differ. Refer to the package list or documentation of the BSD variant you are using for the exact Python package name you intend to install.

## [Setting the Python interpreter](intro_bsd.md#id4)

To support a variety of Unix-like operating systems and distributions, Ansible cannot always rely on the existing environment or `env` variables to locate the correct Python binary. By default, modules point at `/usr/bin/python` as this is the most common location. On BSD variants, this path may differ, so it is advised to inform Ansible of the binary’s location. See [INTERPRETER_PYTHON](../reference_appendices/config.md#interpreter-python). For example, set `ansible_python_interpreter` inventory variable:

```ini
[freebsd:vars]
ansible_python_interpreter=/usr/local/bin/python
[openbsd:vars]
ansible_python_interpreter=/usr/local/bin/python3.8
```

### [FreeBSD packages and ports](intro_bsd.md#id5)

In FreeBSD, there is no guarantee that either `/usr/local/bin/python` executable file or a link to an executable file is installed by default. The best practice for a remote host, with respect to Ansible, is to install at least the Python version supported by Ansible, for example, `lang/python38`, and both meta ports `lang/python3` and `lang/python`. Quoting from */usr/ports/lang/python3/pkg-descr*:

```
This is a meta port to the Python 3.x interpreter and provides symbolic links
to bin/python3, bin/pydoc3, bin/idle3 and so on to allow compatibility with
minor version agnostic python scripts.
```

Quoting from */usr/ports/lang/python/pkg-descr*:

```
This is a meta port to the Python interpreter and provides symbolic links
to bin/python, bin/pydoc, bin/idle and so on to allow compatibility with
version agnostic python scripts.
```

As a result, the following packages are installed:

```
shell> pkg info | grep python
python-3.8_3,2                 "meta-port" for the default version of Python interpreter
python3-3_3                    Meta-port for the Python interpreter 3.x
python38-3.8.12_1              Interpreted object-oriented programming language
```

and the following executables and links

```
shell> ll /usr/local/bin/ | grep python
lrwxr-xr-x  1 root  wheel       7 Jan 24 08:30 python@ -> python3
lrwxr-xr-x  1 root  wheel      14 Jan 24 08:30 python-config@ -> python3-config
lrwxr-xr-x  1 root  wheel       9 Jan 24 08:29 python3@ -> python3.8
lrwxr-xr-x  1 root  wheel      16 Jan 24 08:29 python3-config@ -> python3.8-config
-r-xr-xr-x  1 root  wheel    5248 Jan 13 01:12 python3.8*
-r-xr-xr-x  1 root  wheel    3153 Jan 13 01:12 python3.8-config*
```

### [INTERPRETER_PYTHON_FALLBACK](intro_bsd.md#id6)

Since version 2.8 Ansible provides a useful variable `ansible_interpreter_python_fallback` to specify a list of paths to search for Python. See [INTERPRETER_PYTHON_FALLBACK](../reference_appendices/config.md#interpreter-python-fallback). This list will be searched and the first item found will be used. For example, the configuration below would make the installation of the meta-ports in the previous section redundant, that is, if you don’t install the Python meta ports the first two items in the list will be skipped and `/usr/local/bin/python3.8` will be discovered.

```ini
ansible_interpreter_python_fallback=['/usr/local/bin/python', '/usr/local/bin/python3', '/usr/local/bin/python3.8']
```

You can use this variable, prolonged by the lower versions of Python, and put it, for example, into the `group_vars/all`. Then, override it for specific groups in `group_vars/{group1, group2, ...}` and for specific hosts in `host_vars/{host1, host2, ...}` if needed. See [Variable precedence: Where should I put a variable?](playbooks_variables.md#ansible-variable-precedence).

### [Debug the discovery of Python](intro_bsd.md#id7)

For example, given the inventory

```ini
shell> cat hosts
[test]
test_11
test_12
test_13

[test:vars]
ansible_connection=ssh
ansible_user=admin
ansible_become=yes
ansible_become_user=root
ansible_become_method=sudo
ansible_interpreter_python_fallback=['/usr/local/bin/python', '/usr/local/bin/python3', '/usr/local/bin/python3.8']
ansible_perl_interpreter=/usr/local/bin/perl
```

The playbook below

```yaml+jinja
shell> cat playbook.yml
- hosts: test_11
  gather_facts: false
  tasks:
    - command: which python
      register: result
    - debug:
        var: result.stdout
    - debug:
        msg: |-
          {% for i in _vars %}
          {{ i }}:
            {{ lookup('vars', i)|to_nice_yaml|indent(2) }}
          {% endfor %}
      vars:
        _vars: "{{ query('varnames', '.*python.*') }}"
```

displays the details

```yaml
shell> ansible-playbook -i hosts playbook.yml

PLAY [test_11] *******************************************************************************

TASK [command] *******************************************************************************
[WARNING]: Platform freebsd on host test_11 is using the discovered Python interpreter at
/usr/local/bin/python, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.12/reference_appendices/interpreter_discovery.html for more information.
changed: [test_11]

TASK [debug] *********************************************************************************
ok: [test_11] =>
  result.stdout: /usr/local/bin/python

TASK [debug] *********************************************************************************
ok: [test_11] =>
  msg: |-
    ansible_interpreter_python_fallback:
      - /usr/local/bin/python
      - /usr/local/bin/python3
      - /usr/local/bin/python3.8

    discovered_interpreter_python:
      /usr/local/bin/python

    ansible_playbook_python:
      /usr/bin/python3
```

You can see that the first item from the list `ansible_interpreter_python_fallback` was discovered at the FreeBSD remote host. The variable `ansible_playbook_python` keeps the path to Python at the Linux controller that ran the playbook.

Regarding the warning, quoting from [INTERPRETER_PYTHON](../reference_appendices/config.md#interpreter-python)

```
The fallback behavior will issue a warning that the interpreter
should be set explicitly (since interpreters installed later may
change which one is used). This warning behavior can be disabled by
setting auto_silent or auto_legacy_silent. ...
```

You can either ignore it or get rid of it by setting the variable `ansible_python_interpreter=auto_silent` because this is, actually, what you want by using `/usr/local/bin/python` (*“interpreters installed later may change which one is used”*). For example

```ini
shell> cat hosts
[test]
test_11
test_12
test_13

[test:vars]
ansible_connection=ssh
ansible_user=admin
ansible_become=yes
ansible_become_user=root
ansible_become_method=sudo
ansible_interpreter_python_fallback=['/usr/local/bin/python', '/usr/local/bin/python3', '/usr/local/bin/python3.8']
ansible_python_interpreter=auto_silent
ansible_perl_interpreter=/usr/local/bin/perl
```

> **See also:**
>
> - [Interpreter Discovery](../reference_appendices/interpreter_discovery.md#interpreter-discovery)
> - [FreeBSD Wiki: Ports/DEFAULT_VERSIONS](https://wiki.freebsd.org/Ports/DEFAULT_VERSIONS)

### [Additional variables](intro_bsd.md#id8)

If you use additional plugins beyond those bundled with Ansible, you can set similar variables for `bash`, `perl` or `ruby`, depending on how the plugin is written. For example:

```ini
[freebsd:vars]
ansible_python_interpreter=/usr/local/bin/python
ansible_perl_interpreter=/usr/local/bin/perl
```

## [Which modules are available?](intro_bsd.md#id9)

The majority of the core Ansible modules are written for a combination of Unix-like machines and other generic services, so most should function well on the BSDs with the obvious exception of those that are aimed at Linux-only technologies (such as LVG).

## [Using BSD as the control node](intro_bsd.md#id10)

Using BSD as the control machine is as simple as installing the Ansible package for your BSD variant or by following the `pip` or ‘from source’ instructions.

## [BSD facts](intro_bsd.md#id11)

Ansible gathers facts from the BSDs in a similar manner to Linux machines, but since the data, names and structures can vary for network, disks and other devices, one should expect the output to be slightly different yet still familiar to a BSD administrator.

## [BSD efforts and contributions](intro_bsd.md#id12)

BSD support is important to us at Ansible. Even though the majority of our contributors use and target Linux we have an active BSD community and strive to be as BSD-friendly as possible.
Please feel free to report any issues or incompatibilities you discover with BSD; pull requests with an included fix are also welcome!

> **See also:**
>
> [Introduction to ad hoc commands](intro_adhoc.md#intro-adhoc)
> :   Examples of basic commands
>
> [Working with playbooks](playbooks.md#working-with-playbooks)
> :   Learning ansible’s configuration management language
>
> [Should you develop a module?](../dev_guide/developing_modules.md#developing-modules)
> :   How to write modules
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
