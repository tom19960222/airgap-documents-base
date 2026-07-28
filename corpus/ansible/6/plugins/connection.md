---
collection: ansible
version: "6"
title: "Connection plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/connection.html
fetched_at: 2026-07-27T16:40:39+00:00
---
# Connection plugins

- [`ssh` plugins](connection.md#ssh-plugins)
- [Adding connection plugins](connection.md#adding-connection-plugins)
- [Using connection plugins](connection.md#using-connection-plugins)
- [Plugin list](connection.md#plugin-list)

Connection plugins allow Ansible to connect to the target hosts so it can execute tasks on them. Ansible ships with many connection plugins, but only one can be used per host at a time.

By default, Ansible ships with several connection plugins. The most commonly used are the [paramiko SSH](https://docs.ansible.com/ansible/2.9/plugins/connection/paramiko_ssh.html#paramiko-ssh-connection "(in Ansible v2.9)"), native ssh (just called [ssh](../collections/ansible/builtin/ssh_connection.md#ssh-connection)), and [local](../collections/ansible/builtin/local_connection.md#local-connection) connection types. All of these can be used in playbooks and with **/usr/bin/ansible** to decide how you want to talk to remote machines. If necessary, you can [create custom connection plugins](../dev_guide/developing_plugins.md#developing-connection-plugins).

The basics of these connection types are covered in the [getting started](https://docs.ansible.com/ansible/5/user_guide/intro_getting_started.html#intro-getting-started "(in Ansible v5)") section.

## [`ssh` plugins](connection.md#id3)

Because ssh is the default protocol used in system administration and the protocol most used in Ansible, ssh options are included in the command line tools. See [ansible-playbook](../cli/ansible-playbook.md#ansible-playbook) for more details.

## [Adding connection plugins](connection.md#id4)

You can extend Ansible to support other transports (such as SNMP or message bus) by dropping a custom plugin
into the `connection_plugins` directory.

## [Using connection plugins](connection.md#id5)

You can set the connection plugin globally via [configuration](../reference_appendices/config.md#ansible-configuration-settings), at the command line (`-c`, `--connection`), as a [keyword](../reference_appendices/playbooks_keywords.md#playbook-keywords) in your play, or by setting a [variable](../user_guide/intro_inventory.md#behavioral-parameters), most often in your inventory.
For example, for Windows machines you might want to set the [winrm](../collections/ansible/builtin/winrm_connection.md#winrm-connection) plugin as an inventory variable.

Most connection plugins can operate with minimal configuration. By default they use the [inventory hostname](../collections/ansible/builtin/inventory_hostnames_lookup.md#inventory-hostnames-lookup) and defaults to find the target host.

Plugins are self-documenting. Each plugin should document its configuration options. The following are connection variables common to most connection plugins:

[ansible_host](../user_guide/playbooks_vars_facts.md#magic-variables-and-hostvars)
:   The name of the host to connect to, if different from the [inventory](../user_guide/intro_inventory.md#intro-inventory) hostname.

[ansible_port](../reference_appendices/faq.md#faq-setting-users-and-ports)
:   The ssh port number, for [ssh](../collections/ansible/builtin/ssh_connection.md#ssh-connection) and [paramiko_ssh](https://docs.ansible.com/ansible/2.9/plugins/connection/paramiko_ssh.html#paramiko-ssh-connection "(in Ansible v2.9)") it defaults to 22.

[ansible_user](../reference_appendices/faq.md#faq-setting-users-and-ports)
:   The default user name to use for log in. Most plugins default to the ‘current user running Ansible’.

Each plugin might also have a specific version of a variable that overrides the general version. For example, `ansible_ssh_host` for the [ssh](../collections/ansible/builtin/ssh_connection.md#ssh-connection) plugin.

## [Plugin list](connection.md#id6)

You can use `ansible-doc -t connection -l` to see the list of available plugins.
Use `ansible-doc -t connection <plugin name>` to see detailed documentation and examples.

> **See also:**
>
> [Working with Playbooks](../user_guide/playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
>
> [Callback plugins](callback.md#callback-plugins)
> :   Callback plugins
>
> [Filter plugins](filter.md#filter-plugins)
> :   Filter plugins
>
> [Test plugins](test.md#test-plugins)
> :   Test plugins
>
> [Lookup plugins](lookup.md#lookup-plugins)
> :   Lookup plugins
>
> [Vars plugins](vars.md#vars-plugins)
> :   Vars plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
