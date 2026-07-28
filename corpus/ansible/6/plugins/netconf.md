---
collection: ansible
version: "6"
title: "Netconf plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/netconf.html
fetched_at: 2026-07-27T16:40:42+00:00
---
# Netconf plugins

- [Adding netconf plugins](netconf.md#adding-netconf-plugins)
- [Using netconf plugins](netconf.md#using-netconf-plugins)
- [Listing netconf plugins](netconf.md#listing-netconf-plugins)

Netconf plugins are abstractions over the Netconf interface to network devices. They provide a standard interface for Ansible to execute tasks on those network devices.

These plugins generally correspond one-to-one to network device platforms. Ansible loads the appropriate netconf plugin automatically based on the `ansible_network_os` variable. If the platform supports standard Netconf implementation as defined in the Netconf RFC specification, Ansible loads the `default` netconf plugin. If the platform supports propriety Netconf RPCs, Ansible loads the platform-specific netconf plugin.

## [Adding netconf plugins](netconf.md#id2)

You can extend Ansible to support other network devices by dropping a custom plugin into the `netconf_plugins` directory.

## [Using netconf plugins](netconf.md#id3)

The netconf plugin to use is determined automatically from the `ansible_network_os` variable. There should be no reason to override this functionality.

Most netconf plugins can operate without configuration. A few have additional options that can be set to affect how tasks are translated into netconf commands. A ncclient device specific handler name can be set in the netconf plugin or else the value of `default` is used as per ncclient device handler.

Plugins are self-documenting. Each plugin should document its configuration options.

## [Listing netconf plugins](netconf.md#id4)

These plugins have migrated to collections on [Ansible Galaxy](https://galaxy.ansible.com). If you installed Ansible version 2.10 or later using `pip`, you have access to several netconf plugins. To list all available netconf plugins on your control node, type `ansible-doc -t netconf -l`. To view plugin-specific documentation and examples, use `ansible-doc -t netconf`.

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
