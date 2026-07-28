---
collection: ansible
version: "8"
title: "Using Ansible modules and plugins"
source_url: https://docs.ansible.com/projects/ansible/8/module_plugin_guide/index.html
fetched_at: 2026-07-28T00:57:43+00:00
---
# Using Ansible modules and plugins

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the Ansible guide for working with modules, plugins, and collections.

Ansible modules are units of code that can control system resources or execute system commands.
Ansible provides a module library that you can execute directly on remote hosts or through playbooks.
You can also write custom modules.

Similar to modules are plugins, which are pieces of code that extend core Ansible functionality.
Ansible uses a plugin architecture to enable a rich, flexible, and expandable feature set.
Ansible ships with several plugins and lets you easily use your own plugins.

- [Introduction to modules](modules_intro.md)
- [Module maintenance and support](modules_support.md)
  - [Maintenance](modules_support.md#maintenance)
  - [Issue Reporting](modules_support.md#issue-reporting)
  - [Support](modules_support.md#support)
- [Rejecting modules](plugin_filtering_config.md)
- [Working with plugins](../plugins/plugins.md)
  - [Action plugins](../plugins/action.md)
  - [Become plugins](../plugins/become.md)
  - [Cache plugins](../plugins/cache.md)
  - [Callback plugins](../plugins/callback.md)
  - [Cliconf plugins](../plugins/cliconf.md)
  - [Connection plugins](../plugins/connection.md)
  - [Docs fragments](../plugins/docs_fragment.md)
  - [Filter plugins](../plugins/filter.md)
  - [Httpapi plugins](../plugins/httpapi.md)
  - [Inventory plugins](../plugins/inventory.md)
  - [Lookup plugins](../plugins/lookup.md)
  - [Modules](../plugins/module.md)
  - [Module utilities](../plugins/module_util.md)
  - [Netconf plugins](../plugins/netconf.md)
  - [Shell plugins](../plugins/shell.md)
  - [Strategy plugins](../plugins/strategy.md)
  - [Terminal plugins](../plugins/terminal.md)
  - [Test plugins](../plugins/test.md)
  - [Vars plugins](../plugins/vars.md)
- [Modules and plugins index](modules_plugins_index.md)
