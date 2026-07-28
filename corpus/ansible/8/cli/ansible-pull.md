---
collection: ansible
version: "8"
title: "ansible-pull"
source_url: https://docs.ansible.com/projects/ansible/8/cli/ansible-pull.html
fetched_at: 2026-07-28T00:59:49+00:00
---
# ansible-pull

**pulls playbooks from a VCS repo and executes them for the local host**

- [Synopsis](ansible-pull.md#synopsis)
- [Description](ansible-pull.md#description)
- [Common Options](ansible-pull.md#common-options)
- [ARGUMENTS](ansible-pull.md#arguments)
- [Environment](ansible-pull.md#environment)
- [Files](ansible-pull.md#files)
- [Author](ansible-pull.md#author)
- [License](ansible-pull.md#license)
- [See also](ansible-pull.md#see-also)

## [Synopsis](ansible-pull.md#id2)

```bash
usage: ansible-pull [-h] [--version] [-v] [--private-key PRIVATE_KEY_FILE]
                 [-u REMOTE_USER] [-c CONNECTION] [-T TIMEOUT]
                 [--ssh-common-args SSH_COMMON_ARGS]
                 [--sftp-extra-args SFTP_EXTRA_ARGS]
                 [--scp-extra-args SCP_EXTRA_ARGS]
                 [--ssh-extra-args SSH_EXTRA_ARGS]
                 [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
                 [--vault-id VAULT_IDS]
                 [--ask-vault-password | --vault-password-file VAULT_PASSWORD_FILES]
                 [-e EXTRA_VARS] [-t TAGS] [--skip-tags SKIP_TAGS]
                 [-i INVENTORY] [--list-hosts] [-l SUBSET] [-M MODULE_PATH]
                 [-K | --become-password-file BECOME_PASSWORD_FILE]
                 [--purge] [-o] [-s SLEEP] [-f] [-d DEST] [-U URL] [--full]
                 [-C CHECKOUT] [--accept-host-key] [-m MODULE_NAME]
                 [--verify-commit] [--clean] [--track-subs] [--check]
                 [--diff]
                 [playbook.yml ...]
```

## [Description](ansible-pull.md#id3)

Used to pull a remote copy of ansible on each managed node,
each set to run via cron and update playbook source via a source repository.
This inverts the default *push* architecture of ansible into a *pull* architecture,
which has near-limitless scaling potential.

None of the CLI tools are designed to run concurrently with themselves,
you should use an external scheduler and/or locking to ensure there are no clashing operations.

The setup playbook can be tuned to change the cron frequency, logging locations, and parameters to ansible-pull.
This is useful both for extreme scale-out as well as periodic remediation.
Usage of the ‘fetch’ module to retrieve logs from ansible-pull runs would be an
excellent way to gather and analyze remote logs from ansible-pull.

## [Common Options](ansible-pull.md#id4)

--accept-host-key
:   adds the hostkey for the repo url if not already added

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--become-password-file <BECOME_PASSWORD_FILE>, --become-pass-file <BECOME_PASSWORD_FILE>
:   Become password file

--check
:   don’t make any changes; instead, try to predict some of the changes that may occur

--clean
:   modified files in the working repository will be discarded

--connection-password-file <CONNECTION_PASSWORD_FILE>, --conn-pass-file <CONNECTION_PASSWORD_FILE>
:   Connection password file

--diff
:   when changing (small) files and templates, show the differences in those files; works great with –check

--full
:   Do a full clone, instead of a shallow one.

--list-hosts
:   outputs a list of matching hosts; does not execute anything else

--private-key <PRIVATE_KEY_FILE>, --key-file <PRIVATE_KEY_FILE>
:   use this file to authenticate the connection

--purge
:   purge checkout after playbook run

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

--track-subs
:   submodules will track the latest changes. This is equivalent to specifying the –remote flag to git submodule update

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

--verify-commit
:   verify GPG signature of checked out commit, if it fails abort running the playbook. This needs the corresponding VCS module to support such an operation

--version
:   show program’s version number, config file location, configured module search path, module location, executable location and exit

-C <CHECKOUT>, --checkout <CHECKOUT>
:   branch/tag/commit to checkout. Defaults to behavior of repository module.

-K, --ask-become-pass
:   ask for privilege escalation password

-M, --module-path
:   prepend colon-separated path(s) to module library (default={{ ANSIBLE_HOME ~ “/plugins/modules:/usr/share/ansible/plugins/modules” }})

-T <TIMEOUT>, --timeout <TIMEOUT>
:   override the connection timeout in seconds (default=10)

-U <URL>, --url <URL>
:   URL of the playbook repository

-c <CONNECTION>, --connection <CONNECTION>
:   connection type to use (default=smart)

-d <DEST>, --directory <DEST>
:   path to the directory to which Ansible will checkout the repository.

-e, --extra-vars
:   set additional variables as key=value or YAML/JSON, if filename prepend with @

-f, --force
:   run the playbook even if the repository could not be updated

-h, --help
:   show this help message and exit

-i, --inventory, --inventory-file
:   specify inventory host path or comma separated host list. –inventory-file is deprecated

-k, --ask-pass
:   ask for connection password

-l <SUBSET>, --limit <SUBSET>
:   further limit selected hosts to an additional pattern

-m <MODULE_NAME>, --module-name <MODULE_NAME>
:   Repository module name, which ansible will use to check out the repo. Choices are (‘git’, ‘subversion’, ‘hg’, ‘bzr’). Default is git.

-o, --only-if-changed
:   only run the playbook if the repository has been updated

-s <SLEEP>, --sleep <SLEEP>
:   sleep for random interval (between 0 and n number of seconds) before starting. This is a useful way to disperse git requests

-t, --tags
:   only run plays and tasks tagged with these values

-u <REMOTE_USER>, --user <REMOTE_USER>
:   connect as this user (default=None)

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

## [ARGUMENTS](ansible-pull.md#id5)

playbook.yml
:   The name of one the YAML format files to run as an Ansible playbook.This can be a relative path within the checkout. By default, Ansible willlook for a playbook based on the host’s fully-qualified domain name,on the host hostname and finally a playbook named *local.yml*.

## [Environment](ansible-pull.md#id6)

The following environment variables may be specified.

[`ANSIBLE_INVENTORY`](../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY) – Override the default ansible inventory file

[`ANSIBLE_LIBRARY`](../reference_appendices/config.md#envvar-ANSIBLE_LIBRARY) – Override the default ansible module library path

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-pull.md#id7)

`/etc/ansible/hosts` – Default inventory file

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-pull.md#id8)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-pull.md#id9)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-pull.md#id10)

*ansible(1)*, *ansible-config(1)*, *ansible-console(1)*, *ansible-doc(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-playbook(1)*, *ansible-vault(1)*
