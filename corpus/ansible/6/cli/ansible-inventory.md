---
collection: ansible
version: "6"
title: "ansible-inventory"
source_url: https://docs.ansible.com/projects/ansible/6/cli/ansible-inventory.html
fetched_at: 2026-07-27T16:40:36+00:00
---
# ansible-inventory

**None**

- [Synopsis](ansible-inventory.md#synopsis)
- [Description](ansible-inventory.md#description)
- [Common Options](ansible-inventory.md#common-options)
- [Environment](ansible-inventory.md#environment)
- [Files](ansible-inventory.md#files)
- [Author](ansible-inventory.md#author)
- [License](ansible-inventory.md#license)
- [See also](ansible-inventory.md#see-also)

## [Synopsis](ansible-inventory.md#id2)

```bash
usage: ansible-inventory [-h] [--version] [-v] [-i INVENTORY]
                      [--vault-id VAULT_IDS]
                      [--ask-vault-password | --vault-password-file VAULT_PASSWORD_FILES]
                      [--playbook-dir BASEDIR] [-e EXTRA_VARS] [--list]
                      [--host HOST] [--graph] [-y] [--toml] [--vars]
                      [--export] [--output OUTPUT_FILE]
                      [host|group]
```

## [Description](ansible-inventory.md#id3)

used to display or dump the configured inventory as Ansible sees it

## [Common Options](ansible-inventory.md#id4)

--ask-vault-password, --ask-vault-pass
:   ask for vault password

--export
:   When doing an –list, represent in a way that is optimized for export,not as an accurate representation of how Ansible has processed it

--graph
:   create inventory graph, if supplying pattern it must be a valid group name

--host <HOST>
:   Output specific host info, works as inventory script

--list
:   Output all hosts info, works as inventory script

--list-hosts
:   ==SUPPRESS==

--output <OUTPUT_FILE>
:   When doing –list, send the inventory to a file instead of to the screen

--playbook-dir <BASEDIR>
:   Since this tool does not use playbooks, use this as a substitute playbook directory. This sets the relative path for many features including roles/ group_vars/ etc.

--toml
:   Use TOML format instead of default JSON, ignored for –graph

--vars
:   Add vars to graph display, ignored unless used with –graph

--vault-id
:   the vault identity to use

--vault-password-file, --vault-pass-file
:   vault password file

--version
:   show program’s version number, config file location, configured module search path, module location, executable location and exit

-e, --extra-vars
:   set additional variables as key=value or YAML/JSON, if filename prepend with @

-h, --help
:   show this help message and exit

-i, --inventory, --inventory-file
:   specify inventory host path or comma separated host list. –inventory-file is deprecated

-l, --limit
:   ==SUPPRESS==

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

-y, --yaml
:   Use YAML format instead of default JSON, ignored for –graph

## [Environment](ansible-inventory.md#id5)

The following environment variables may be specified.

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-inventory.md#id6)

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-inventory.md#id7)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-inventory.md#id8)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-inventory.md#id9)

*ansible(1)*, *ansible-config(1)*, *ansible-console(1)*, *ansible-doc(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-playbook(1)*, *ansible-pull(1)*, *ansible-vault(1)*,
