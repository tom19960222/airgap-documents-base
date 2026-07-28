---
collection: ansible
version: "8"
title: "ansible.builtin.ini inventory – Uses an Ansible INI file as inventory source."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/ini_inventory.html
fetched_at: 2026-07-28T01:04:09+00:00
---
# ansible.builtin.ini inventory – Uses an Ansible INI file as inventory source.

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `ini`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.ini` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](ini_inventory.md#synopsis)
- [Notes](ini_inventory.md#notes)
- [Examples](ini_inventory.md#examples)

## [Synopsis](ini_inventory.md#id1)

- INI file based inventory, sections are groups or group related with special `:modifiers`.
- Entries in sections `[group_1]` are hosts, members of the group.
- Hosts can have variables defined inline as key/value pairs separated by `=`.
- The `children` modifier indicates that the section contains groups.
- The `vars` modifier indicates that the section contains variables assigned to members of the group.
- Anything found outside a section is considered an ‘ungrouped’ host.
- Values passed in the INI format using the `key=value` syntax are interpreted differently depending on where they are declared within your inventory.
- When declared inline with the host, INI values are processed by Python’s ast.literal_eval function (<https://docs.python.org/3/library/ast.html#ast.literal_eval>) and interpreted as Python literal structures (strings, numbers, tuples, lists, dicts, booleans, None). If you want a number to be treated as a string, you must quote it. Host lines accept multiple `key=value` parameters per line. Therefore they need a way to indicate that a space is part of a value rather than a separator.
- When declared in a `:vars` section, INI values are interpreted as strings. For example `var=FALSE` would create a string equal to `FALSE`. Unlike host lines, `:vars` sections accept only a single entry per line, so everything after the `=` must be the value for the entry.
- Do not rely on types set during definition, always make sure you specify type with a filter when needed when consuming the variable.
- See the Examples for proper quoting to prevent changes to variable type.

## [Notes](ini_inventory.md#id2)

> **Note:**
>
> - Enabled in configuration by default.
> - Consider switching to YAML format for inventory sources to avoid confusion on the actual type of a variable. The YAML inventory plugin processes variable values consistently and correctly.

## [Examples](ini_inventory.md#id3)

```ini
# fmt: ini
# Example 1
[web]
host1
host2 ansible_port=222 # defined inline, interpreted as an integer

[web:vars]
http_port=8080 # all members of 'web' will inherit these
myvar=23 # defined in a :vars section, interpreted as a string

[web:children] # child groups will automatically add their hosts to parent group
apache
nginx

[apache]
tomcat1
tomcat2 myvar=34 # host specific vars override group vars
tomcat3 mysecret="'03#pa33w0rd'" # proper quoting to prevent value changes

[nginx]
jenkins1

[nginx:vars]
has_java = True # vars in child groups override same in parent

[all:vars]
has_java = False # 'all' is 'top' parent

# Example 2
host1 # this is 'ungrouped'

# both hosts have same IP but diff ports, also 'ungrouped'
host2 ansible_host=127.0.0.1 ansible_port=44
host3 ansible_host=127.0.0.1 ansible_port=45

[g1]
host4

[g2]
host4 # same host as above, but member of 2 groups, will inherit vars from both
      # inventory hostnames are unique
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
