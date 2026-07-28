---
collection: ansible
version: "6"
title: "ansible.builtin.toml inventory – Uses a specific TOML file as an inventory source."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/toml_inventory.html
fetched_at: 2026-07-27T16:44:18+00:00
---
# ansible.builtin.toml inventory – Uses a specific TOML file as an inventory source.

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `toml` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

New in Ansible 2.8

- [Synopsis](toml_inventory.md#synopsis)
- [Notes](toml_inventory.md#notes)
- [Examples](toml_inventory.md#examples)

## [Synopsis](toml_inventory.md#id1)

- TOML based inventory format
- File MUST have a valid ‘.toml’ file extension

## [Notes](toml_inventory.md#id2)

> **Note:**
>
> - Requires the ‘toml’ python library

## [Examples](toml_inventory.md#id3)

```yaml+jinja
# fmt: toml
# Example 1
[all.vars]
has_java = false

[web]
children = [
    "apache",
    "nginx"
]
vars = { http_port = 8080, myvar = 23 }

[web.hosts]
host1 = {}
host2 = { ansible_port = 222 }

[apache.hosts]
tomcat1 = {}
tomcat2 = { myvar = 34 }
tomcat3 = { mysecret = "03#pa33w0rd" }

[nginx.hosts]
jenkins1 = {}

[nginx.vars]
has_java = true

# Example 2
[all.vars]
has_java = false

[web]
children = [
    "apache",
    "nginx"
]

[web.vars]
http_port = 8080
myvar = 23

[web.hosts.host1]
[web.hosts.host2]
ansible_port = 222

[apache.hosts.tomcat1]

[apache.hosts.tomcat2]
myvar = 34

[apache.hosts.tomcat3]
mysecret = "03#pa33w0rd"

[nginx.hosts.jenkins1]

[nginx.vars]
has_java = true

# Example 3
[ungrouped.hosts]
host1 = {}
host2 = { ansible_host = "127.0.0.1", ansible_port = 44 }
host3 = { ansible_host = "127.0.0.1", ansible_port = 45 }

[g1.hosts]
host4 = {}

[g2.hosts]
host4 = {}
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
