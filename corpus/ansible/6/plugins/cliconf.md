---
collection: ansible
version: "6"
title: "Cliconf plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/cliconf.html
fetched_at: 2026-07-27T16:40:39+00:00
---
# Cliconf plugins

- [Adding cliconf plugins](cliconf.md#adding-cliconf-plugins)
- [Using cliconf plugins](cliconf.md#using-cliconf-plugins)
- [Viewing cliconf plugins](cliconf.md#viewing-cliconf-plugins)

Cliconf plugins are abstractions over the CLI interface to network devices. They provide a standard interface for Ansible to execute tasks on those network devices.

These plugins generally correspond one-to-one to network device platforms. Ansible loads the appropriate cliconf plugin automatically based on the `ansible_network_os` variable.

## [Adding cliconf plugins](cliconf.md#id2)

You can extend Ansible to support other network devices by dropping a custom plugin into the `cliconf_plugins` directory.

## [Using cliconf plugins](cliconf.md#id3)

The cliconf plugin to use is determined automatically from the `ansible_network_os` variable. There should be no reason to override this functionality.

Most cliconf plugins can operate without configuration. A few have additional options that can be set to affect how tasks are translated into CLI commands.

Plugins are self-documenting. Each plugin should document its configuration options.

## [Viewing cliconf plugins](cliconf.md#id4)

These plugins have migrated to collections on [Ansible Galaxy](https://galaxy.ansible.com). If you installed Ansible version 2.10 or later using `pip`, you have access to several cliconf plugins. To list all available cliconf plugins on your control node, type `ansible-doc -t cliconf -l`. To view plugin-specific documentation and examples, use `ansible-doc -t cliconf`.

> **See also:**
>
> [Ansible for Network Automation](../network/index.md#network-guide)
> :   An overview of using Ansible to automate networking devices.
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [irc.libera.chat](https://libera.chat/)
> :   #ansible-network IRC chat channel
