---
collection: ansible
version: "8"
title: "Terminal plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/terminal.html
fetched_at: 2026-07-28T01:00:21+00:00
---
# Terminal plugins

- [Adding terminal plugins](terminal.md#adding-terminal-plugins)
- [Using terminal plugins](terminal.md#using-terminal-plugins)

Terminal plugins contain information on how to prepare a particular network device’s SSH shell is properly initialized to be used with Ansible. This typically includes disabling automatic paging, detecting errors in output, and enabling privileged mode if supported and required on the device.

These plugins correspond one-to-one to network device platforms. Ansible loads the appropriate terminal plugin automatically based on the `ansible_network_os` variable.

## [Adding terminal plugins](terminal.md#id2)

You can extend Ansible to support other network devices by dropping a custom plugin into the `terminal_plugins` directory.

## [Using terminal plugins](terminal.md#id3)

Ansible determines which terminal plugin to use automatically from the `ansible_network_os` variable. There should be no reason to override this functionality.

Terminal plugins operate without configuration. All options to control the terminal are exposed in the `network_cli` connection plugin.

Plugins are self-documenting. Each plugin should document its configuration options.

> **See also:**
>
> [Ansible for Network Automation](../network/index.md#network-guide)
> :   An overview of using Ansible to automate networking devices.
>
> [Connection plugins](connection.md#connection-plugins)
> :   Connection plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [irc.libera.chat](https://libera.chat/)
> :   #ansible-network IRC chat channel
