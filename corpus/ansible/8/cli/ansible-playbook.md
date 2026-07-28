---
collection: ansible
version: "8"
title: "ansible-playbook"
source_url: https://docs.ansible.com/projects/ansible/8/cli/ansible-playbook.html
fetched_at: 2026-07-28T00:59:49+00:00
---
# ansible-playbook

**Runs Ansible playbooks, executing the defined tasks on the targeted hosts.**

- [Synopsis](ansible-playbook.md#synopsis)
- [Description](ansible-playbook.md#description)
- [Common Options](ansible-playbook.md#common-options)
- [Environment](ansible-playbook.md#environment)
- [Files](ansible-playbook.md#files)
- [Author](ansible-playbook.md#author)
- [License](ansible-playbook.md#license)
- [See also](ansible-playbook.md#see-also)

## [Synopsis](ansible-playbook.md#id2)

```bash
usage: ansible-playbook [-h] [--version] [-v] [--private-key PRIVATE_KEY_FILE]
                     [-u REMOTE_USER] [-c CONNECTION] [-T TIMEOUT]
                     [--ssh-common-args SSH_COMMON_ARGS]
                     [--sftp-extra-args SFTP_EXTRA_ARGS]
                     [--scp-extra-args SCP_EXTRA_ARGS]
                     [--ssh-extra-args SSH_EXTRA_ARGS]
                     [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
                     [--force-handlers] [--flush-cache] [-b]
                     [--become-method BECOME_METHOD]
                     [--become-user BECOME_USER]
                     [-K | --become-password-file BECOME_PASSWORD_FILE]
                     [-t TAGS] [--skip-tags SKIP_TAGS] [-C] [-D]
                     [-i INVENTORY] [--list-hosts] [-l SUBSET]
                     [-e EXTRA_VARS] [--vault-id VAULT_IDS]
                     [--ask-vault-password | --vault-password-file VAULT_PASSWORD_FILES]
                     [-f FORKS] [-M MODULE_PATH] [--syntax-check]
                     [--list-tasks] [--list-tags] [--step]
                     [--start-at-task START_AT_TASK]
                     playbook [playbook ...]
```

## [Description](ansible-playbook.md#id3)

the tool to run *Ansible playbooks*, which are a configuration and multinode deployment system.
See the project home page (<https://docs.ansible.com>) for more information.

## [Common Options](ansible-playbook.md#id4)

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

--flush-cache
:   clear the fact cache for every host in inventory

--force-handlers
:   run handlers even if a task fails

--list-hosts
:   outputs a list of matching hosts; does not execute anything else

--list-tags
:   list all available tags

--list-tasks
:   list all tasks that would be executed

--private-key <PRIVATE_KEY_FILE>, --key-file <PRIVATE_KEY_FILE>
:   use this file to authenticate the connection

--scp-extra-args <SCP_EXTRA_ARGS>
:   specify extra arguments to pass to scp only (e.g. -l)

--sftp-extra-args <SFTP_EXTRA_ARGS>
:   specify extra arguments to pass to sftp only (e.g. -f, -l)

--skip-tags
:   only run plays and tasks whose tags do not match these values

--ssh-common-args <SSH_COMMON_ARGS>
:   specify common arguments to pass to sftp/scp/ssh (e.g. ProxyCommand)

--ssh-extra-args <SSH_EXTRA_ARGS>
:   specify extra arguments to pass to ssh only (e.g. -R)

--start-at-task <START_AT_TASK>
:   start the playbook at the task matching this name

--step
:   one-step-at-a-time: confirm each task before running

--syntax-check
:   perform a syntax check on the playbook, but do not execute it

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
:   prepend colon-separated path(s) to module library (default={{ ANSIBLE_HOME ~ “/plugins/modules:/usr/share/ansible/plugins/modules” }})

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

-t, --tags
:   only run plays and tasks tagged with these values

-u <REMOTE_USER>, --user <REMOTE_USER>
:   connect as this user (default=None)

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

## [Environment](ansible-playbook.md#id5)

The following environment variables may be specified.

[`ANSIBLE_INVENTORY`](../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY) – Override the default ansible inventory file

[`ANSIBLE_LIBRARY`](../reference_appendices/config.md#envvar-ANSIBLE_LIBRARY) – Override the default ansible module library path

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-playbook.md#id6)

`/etc/ansible/hosts` – Default inventory file

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-playbook.md#id7)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-playbook.md#id8)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-playbook.md#id9)

*ansible(1)*, *ansible-config(1)*, *ansible-console(1)*, *ansible-doc(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-pull(1)*, *ansible-vault(1)*
