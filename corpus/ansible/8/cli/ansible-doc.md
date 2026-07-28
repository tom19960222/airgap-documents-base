---
collection: ansible
version: "8"
title: "ansible-doc"
source_url: https://docs.ansible.com/projects/ansible/8/cli/ansible-doc.html
fetched_at: 2026-07-28T00:59:47+00:00
---
# ansible-doc

**plugin documentation tool**

- [Synopsis](ansible-doc.md#synopsis)
- [Description](ansible-doc.md#description)
- [Common Options](ansible-doc.md#common-options)
- [Environment](ansible-doc.md#environment)
- [Files](ansible-doc.md#files)
- [Author](ansible-doc.md#author)
- [License](ansible-doc.md#license)
- [See also](ansible-doc.md#see-also)

## [Synopsis](ansible-doc.md#id2)

```bash
usage: ansible-doc [-h] [--version] [-v] [-M MODULE_PATH]
                [--playbook-dir BASEDIR]
                [-t {become,cache,callback,cliconf,connection,httpapi,inventory,lookup,netconf,shell,vars,module,strategy,test,filter,role,keyword}]
                [-j] [-r ROLES_PATH]
                [-e ENTRY_POINT | -s | -F | -l | --metadata-dump]
                [--no-fail-on-errors]
                [plugin ...]
```

## [Description](ansible-doc.md#id3)

displays information on modules installed in Ansible libraries.
It displays a terse listing of plugins and their short descriptions,
provides a printout of their DOCUMENTATION strings,
and it can create a short “snippet” which can be pasted into a playbook.

## [Common Options](ansible-doc.md#id4)

--metadata-dump
:   **For internal use only** Dump json metadata for all entries, ignores other options.

--no-fail-on-errors
:   **For internal use only** Only used for –metadata-dump. Do not fail on errors. Report the error message in the JSON instead.

--playbook-dir <BASEDIR>
:   Since this tool does not use playbooks, use this as a substitute playbook directory. This sets the relative path for many features including roles/ group_vars/ etc.

--version
:   show program’s version number, config file location, configured module search path, module location, executable location and exit

-F, --list_files
:   Show plugin names and their source files without summaries (implies –list). A supplied argument will be used for filtering, can be a namespace or full collection name.

-M, --module-path
:   prepend colon-separated path(s) to module library (default={{ ANSIBLE_HOME ~ “/plugins/modules:/usr/share/ansible/plugins/modules” }})

-e <ENTRY_POINT>, --entry-point <ENTRY_POINT>
:   Select the entry point for role(s).

-h, --help
:   show this help message and exit

-j, --json
:   Change output into json format.

-l, --list
:   List available plugins. A supplied argument will be used for filtering, can be a namespace or full collection name.

-r, --roles-path
:   The path to the directory containing your roles.

-s, --snippet
:   Show playbook snippet for these plugin types: inventory, lookup, module

-t <TYPE>, --type <TYPE>
:   Choose which plugin type (defaults to “module”). Available plugin types are : (‘become’, ‘cache’, ‘callback’, ‘cliconf’, ‘connection’, ‘httpapi’, ‘inventory’, ‘lookup’, ‘netconf’, ‘shell’, ‘vars’, ‘module’, ‘strategy’, ‘test’, ‘filter’, ‘role’, ‘keyword’)

-v, --verbose
:   Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv, connection debugging might require -vvvv.

## [Environment](ansible-doc.md#id5)

The following environment variables may be specified.

[`ANSIBLE_LIBRARY`](../reference_appendices/config.md#envvar-ANSIBLE_LIBRARY) – Override the default ansible module library path

[`ANSIBLE_CONFIG`](../reference_appendices/config.md#envvar-ANSIBLE_CONFIG) – Override the default ansible config file

Many more are available for most options in ansible.cfg

## [Files](ansible-doc.md#id6)

`/etc/ansible/ansible.cfg` – Config file, used if present

`~/.ansible.cfg` – User config file, overrides the default config if present

## [Author](ansible-doc.md#id7)

Ansible was originally written by Michael DeHaan.

See the AUTHORS file for a complete list of contributors.

## [License](ansible-doc.md#id8)

Ansible is released under the terms of the GPLv3+ License.

## [See also](ansible-doc.md#id9)

*ansible(1)*, *ansible-config(1)*, *ansible-console(1)*, *ansible-galaxy(1)*, *ansible-inventory(1)*, *ansible-playbook(1)*, *ansible-pull(1)*, *ansible-vault(1)*
