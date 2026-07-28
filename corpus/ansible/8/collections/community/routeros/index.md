---
collection: ansible
version: "8"
title: "Community.Routeros"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/index.html
fetched_at: 2026-07-28T01:02:21+00:00
---
# Community.Routeros

Collection version 2.11.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Guides](index.md#guides)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Modules for MikroTik RouterOS

**Authors:**

- Egor Zaitsev (github.com/heuels)
- Nikolay Dachev (github.com/NikolayDachev)
- Felix Fontein (github.com/felixfontein)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.routeros)
- [Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Guides](index.md#id3)

- [How to connect to RouterOS devices with the RouterOS API](docsite/api-guide.md)
- [How to connect to RouterOS devices with SSH](docsite/ssh-guide.md)
- [How to quote and unquote commands and arguments](docsite/quoting.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.routeros collection:

### Modules

- [api module](api_module.md#ansible-collections-community-routeros-api-module) – Ansible module for RouterOS API
- [api_facts module](api_facts_module.md#ansible-collections-community-routeros-api-facts-module) – Collect facts from remote devices running MikroTik RouterOS using the API
- [api_find_and_modify module](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module) – Find and modify information using the API
- [api_info module](api_info_module.md#ansible-collections-community-routeros-api-info-module) – Retrieve information from API
- [api_modify module](api_modify_module.md#ansible-collections-community-routeros-api-modify-module) – Modify data at paths with API
- [command module](command_module.md#ansible-collections-community-routeros-command-module) – Run commands on remote devices running MikroTik RouterOS
- [facts module](facts_module.md#ansible-collections-community-routeros-facts-module) – Collect facts from remote devices running MikroTik RouterOS

### Cliconf Plugins

- [routeros cliconf](routeros_cliconf.md#ansible-collections-community-routeros-routeros-cliconf) – Use routeros cliconf to run command on MikroTik RouterOS platform

### Filter Plugins

- [join filter](join_filter.md#ansible-collections-community-routeros-join-filter) – Join a list of arguments to a command
- [list_to_dict filter](list_to_dict_filter.md#ansible-collections-community-routeros-list-to-dict-filter) – Convert a list of arguments to a dictionary
- [quote_argument filter](quote_argument_filter.md#ansible-collections-community-routeros-quote-argument-filter) – Quote an argument
- [quote_argument_value filter](quote_argument_value_filter.md#ansible-collections-community-routeros-quote-argument-value-filter) – Quote an argument value
- [split filter](split_filter.md#ansible-collections-community-routeros-split-filter) – Split a command into arguments

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
