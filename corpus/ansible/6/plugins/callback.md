---
collection: ansible
version: "6"
title: "Callback plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/callback.html
fetched_at: 2026-07-27T16:40:38+00:00
---
# Callback plugins

- [Example callback plugins](callback.md#example-callback-plugins)
- [Enabling callback plugins](callback.md#enabling-callback-plugins)
- [Setting a callback plugin for `ansible-playbook`](callback.md#setting-a-callback-plugin-for-ansible-playbook)
- [Setting a callback plugin for ad hoc commands](callback.md#setting-a-callback-plugin-for-ad-hoc-commands)
- [Types of callback plugins](callback.md#types-of-callback-plugins)
- [Plugin list](callback.md#plugin-list)

Callback plugins enable adding new behaviors to Ansible when responding to events. By default, callback plugins control most of the output you see when running the command line programs, but can also be used to add additional output, integrate with other tools and marshal the events to a storage backend. If necessary, you can [create custom callback plugins](../dev_guide/developing_plugins.md#developing-callbacks).

## [Example callback plugins](callback.md#id2)

The [log_plays](https://docs.ansible.com/ansible/2.9/plugins/callback/log_plays.html#log-plays-callback "(in Ansible v2.9)") callback is an example of how to record playbook events to a log file, and the [mail](https://docs.ansible.com/ansible/2.9/plugins/callback/mail.html#mail-callback "(in Ansible v2.9)") callback sends email on playbook failures.

The [say](https://docs.ansible.com/ansible/2.9/plugins/callback/say.html#say-callback "(in Ansible v2.9)") callback responds with computer synthesized speech in relation to playbook events.

## [Enabling callback plugins](callback.md#id3)

You can activate a custom callback by either dropping it into a `callback_plugins` directory adjacent to your play, inside a role, or by putting it in one of the callback directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

Plugins are loaded in alphanumeric order. For example, a plugin implemented in a file named 1_first.py would run before a plugin file named 2_second.py.

Most callbacks shipped with Ansible are disabled by default and need to be enabled in your [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings) file in order to function. For example:

```ini
#callbacks_enabled = timer, mail, profile_roles, collection_namespace.collection_name.custom_callback
```

## [Setting a callback plugin for `ansible-playbook`](callback.md#id4)

You can only have one plugin be the main manager of your console output. If you want to replace the default, you should define `CALLBACK_TYPE = stdout` in the subclass and then configure the stdout plugin in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings). For example:

```ini
stdout_callback = dense
```

or for my custom callback:

```ini
stdout_callback = mycallback
```

This only affects [ansible-playbook](../cli/ansible-playbook.md#ansible-playbook) by default.

## [Setting a callback plugin for ad hoc commands](callback.md#id5)

The [ansible](../cli/ansible.md#ansible) ad hoc command specifically uses a different callback plugin for stdout, so there is an extra setting in [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings) you need to add to use the stdout callback defined above:

```ini
[defaults]
bin_ansible_callbacks=True
```

You can also set this as an environment variable:

```shell
export ANSIBLE_LOAD_CALLBACK_PLUGINS=1
```

## [Types of callback plugins](callback.md#id6)

There are three types of callback plugins:

stdout callback plugins:
:   These plugins handle the main console output. Only one of these can be active.

aggregate callback plugins:
:   Aggregate callbacks can add additional console output next to a stdout callback. This can be aggregate information at the end of a playbook run, additional per-task output, or anything else.

notification callback plugins:
:   Notification callbacks inform other applications, services, or systems. This can be anything from logging to databases, informing on errors in Instant Messaging applications, or sending emails when a server is unreachable.

## [Plugin list](callback.md#id7)

You can use `ansible-doc -t callback -l` to see the list of available plugins.
Use `ansible-doc -t callback <plugin name>` to see specific documents and examples.

> **See also:**
>
> [Action plugins](action.md#action-plugins)
> :   Action plugins
>
> [Cache plugins](cache.md#cache-plugins)
> :   Cache plugins
>
> [Connection plugins](connection.md#connection-plugins)
> :   Connection plugins
>
> [Inventory plugins](inventory.md#inventory-plugins)
> :   Inventory plugins
>
> [Shell plugins](shell.md#shell-plugins)
> :   Shell plugins
>
> [Strategy plugins](strategy.md#strategy-plugins)
> :   Strategy plugins
>
> [Vars plugins](vars.md#vars-plugins)
> :   Vars plugins
>
> [User Mailing List](https://groups.google.com/forum/#!forum/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
