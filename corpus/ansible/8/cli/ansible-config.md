---
collection: ansible
version: "8"
title: "ansible-config"
source_url: https://docs.ansible.com/projects/ansible/8/cli/ansible-config.html
fetched_at: 2026-07-28T00:59:45+00:00
---
# ansible-config

**View ansible configuration.**

- [Synopsis](ansible-config.md#synopsis)
- [Description](ansible-config.md#description)
- [Common Options](ansible-config.md#common-options)
- [Actions](ansible-config.md#actions)

  - [list](ansible-config.md#list)
  - [dump](ansible-config.md#dump)
  - [view](ansible-config.md#view)
  - [init](ansible-config.md#init)
- [Environment](ansible-config.md#environment)
- [Files](ansible-config.md#files)
- [Author](ansible-config.md#author)
- [License](ansible-config.md#license)
- [See also](ansible-config.md#see-also)

## [Synopsis](ansible-config.md#id2)

```bash
usage: ansible-config [-h] [--version] [-v] {list,dump,view,init} ...
```

## [Description](ansible-config.md#id3)

Config command line class

## [Common Options](ansible-config.md#id4)

--version
:   show program’s version number, config file location, configured module search path, module location, executable location and exit

-h, --help
:   show this help message and exit

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

## [Actions](ansible-config.md#id5)

### [list](ansible-config.md#id6)

list and output available configs

--format  <FORMAT>, -f  <FORMAT>
:   Output format for list

-c  <CONFIG_FILE>, --config  <CONFIG_FILE>
:   path to configuration file, defaults to first file found in precedence.

-t  <TYPE>, --type  <TYPE>
:   Filter down to a specific plugin type.

### [dump](ansible-config.md#id7)

Shows the current settings, merges ansible.cfg if specified

--format  <FORMAT>, -f  <FORMAT>
:   Output format for dump

--only-changed, --changed-only
:   Only show configurations that have changed from the default

-c  <CONFIG_FILE>, --config  <CONFIG_FILE>
:   path to configuration file, defaults to first file found in precedence.

-t  <TYPE>, --type  <TYPE>
:   Filter down to a specific plugin type.

### [view](ansible-config.md#id8)

Displays the current config file

-c  <CONFIG_FILE>, --config  <CONFIG_FILE>
:   path to configuration file, defaults to first file found in precedence.

-t  <TYPE>, --type  <TYPE>
:   Filter down to a specific plugin type.

### [init](ansible-config.md#id9)

Create initial configuration

--disabled
:   Prefixes all entries with a comment character to disable them

--format  <FORMAT>, -f  <FORMAT>
:   Output format for init

-c  <CONFIG_FILE>, --config  <CONFIG_FILE>
:   path to configuration file, defaults to first file found in precedence.

-t  <TYPE>, --type  <TYPE>
:   Filter down to a specific plugin type.

## [Environment](ansible-config.md#id10)

The following environment variables may be specified.

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-config.md#id11)

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-config.md#id12)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-config.md#id13)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-config.md#id14)

*ansible(1)*, *ansible-console(1)*, *ansible-doc(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-playbook(1)*, *ansible-pull(1)*, *ansible-vault(1)*
