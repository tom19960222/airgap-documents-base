---
collection: ansible
version: "6"
title: "ansible-console"
source_url: https://docs.ansible.com/projects/ansible/6/cli/ansible-console.html
fetched_at: 2026-07-27T16:40:34+00:00
---
# ansible-console

**REPL console for executing Ansible tasks.**

- [Synopsis](ansible-console.md#synopsis)
- [Description](ansible-console.md#description)
- [Common Options](ansible-console.md#common-options)
- [Environment](ansible-console.md#environment)
- [Files](ansible-console.md#files)
- [Author](ansible-console.md#author)
- [License](ansible-console.md#license)
- [See also](ansible-console.md#see-also)

## [Synopsis](ansible-console.md#id2)

```bash
usage: ansible-console [-h] [--version] [-v] [-b]
                    [--become-method BECOME_METHOD]
                    [--become-user BECOME_USER]
                    [-K | --become-password-file BECOME_PASSWORD_FILE]
                    [-i INVENTORY] [--list-hosts] [-l SUBSET]
                    [--private-key PRIVATE_KEY_FILE] [-u REMOTE_USER]
                    [-c CONNECTION] [-T TIMEOUT]
                    [--ssh-common-args SSH_COMMON_ARGS]
                    [--sftp-extra-args SFTP_EXTRA_ARGS]
                    [--scp-extra-args SCP_EXTRA_ARGS]
                    [--ssh-extra-args SSH_EXTRA_ARGS]
                    [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
                    [-C] [--syntax-check] [-D] [--vault-id VAULT_IDS]
                    [--ask-vault-password | --vault-password-file VAULT_PASSWORD_FILES]
                    [-f FORKS] [-M MODULE_PATH] [--playbook-dir BASEDIR]
                    [-e EXTRA_VARS] [--task-timeout TASK_TIMEOUT] [--step]
                    [pattern]
```

## [Description](ansible-console.md#id3)

A REPL that allows for running ad-hoc tasks against a chosen inventory
from a nice shell with built-in tab completion (based on dominis’
ansible-shell).

It supports several commands, and you can modify its configuration at
runtime:

- cd [pattern]: change host/group (you can use host patterns eg.: app\*.dc\*:!app01\*)
- list: list available hosts in the current path
- list groups: list groups included in the current path
- become: toggle the become flag
- !: forces shell module instead of the ansible module (!yum update -y)
- verbosity [num]: set the verbosity level
- forks [num]: set the number of forks
- become_user [user]: set the become_user
- remote_user [user]: set the remote_user
- become_method [method]: set the privilege escalation method
- check [bool]: toggle check mode
- diff [bool]: toggle diff mode
- timeout [integer]: set the timeout of tasks in seconds (0 to disable)
- help [command/module]: display documentation for the command or module
- exit: exit ansible-console

## [Common Options](ansible-console.md#id4)

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--become-method <BECOME_METHOD>
:   privilege escalation method to use (default=sudo), use ansible-doc -t become -l to list valid choices.

--become-password-file <BECOME_PASSWORD_FILE>, --become-pass-file <BECOME_PASSWORD_FILE>
:   Become password file

--become-user <BECOME_USER>
:   run operations as this user (default=root)

--connection-password-file <CONNECTION_PASSWORD_FILE>, --conn-pass-file <CONNECTION_PASSWORD_FILE>
:   Connection password file

--list-hosts
:   outputs a list of matching hosts; does not execute anything else

--playbook-dir <BASEDIR>
:   Since this tool does not use playbooks, use this as a substitute playbook directory. This sets the relative path for many features including roles/ group_vars/ etc.

--private-key <PRIVATE_KEY_FILE>, --key-file <PRIVATE_KEY_FILE>
:   use this file to authenticate the connection

--scp-extra-args <SCP_EXTRA_ARGS>
:   specify extra arguments to pass to scp only (e.g. -l)

--sftp-extra-args <SFTP_EXTRA_ARGS>
:   specify extra arguments to pass to sftp only (e.g. -f, -l)

--ssh-common-args <SSH_COMMON_ARGS>
:   specify common arguments to pass to sftp/scp/ssh (e.g. ProxyCommand)

--ssh-extra-args <SSH_EXTRA_ARGS>
:   specify extra arguments to pass to ssh only (e.g. -R)

--step
:   one-step-at-a-time: confirm each task before running

--syntax-check
:   perform a syntax check on the playbook, but do not execute it

--task-timeout <TASK_TIMEOUT>
:   set task timeout limit in seconds, must be positive integer.

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

--version
:   show program’s version number, config file location, configured module search path, module location, executable location and exit

-C, --check
:   don’t make any changes; instead, try to predict some of the changes that may occur

-D, --diff
:   when changing (small) files and templates, show the differences in those files; works great with –check

-K, --ask-become-pass
:   ask for privilege escalation password

-M, --module-path
:   prepend colon-separated path(s) to module library (default=~/.ansible/plugins/modules:/usr/share/ansible/plugins/modules)

-T <TIMEOUT>, --timeout <TIMEOUT>
:   override the connection timeout in seconds (default=10)

-b, --become
:   run operations with become (does not imply password prompting)

-c <CONNECTION>, --connection <CONNECTION>
:   connection type to use (default=smart)

-e, --extra-vars
:   set additional variables as key=value or YAML/JSON, if filename prepend with @

-f <FORKS>, --forks <FORKS>
:   specify number of parallel processes to use (default=5)

-h, --help
:   show this help message and exit

-i, --inventory, --inventory-file
:   specify inventory host path or comma separated host list. –inventory-file is deprecated

-k, --ask-pass
:   ask for connection password

-l <SUBSET>, --limit <SUBSET>
:   further limit selected hosts to an additional pattern

-u <REMOTE_USER>, --user <REMOTE_USER>
:   connect as this user (default=None)

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

## [Environment](ansible-console.md#id5)

The following environment variables may be specified.

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-console.md#id6)

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-console.md#id7)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-console.md#id8)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-console.md#id9)

*ansible(1)*, *ansible-config(1)*, *ansible-console(1)*, *ansible-doc(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-playbook(1)*, *ansible-pull(1)*, *ansible-vault(1)*,
