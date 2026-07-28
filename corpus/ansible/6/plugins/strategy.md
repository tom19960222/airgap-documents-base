---
collection: ansible
version: "6"
title: "Strategy plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/strategy.html
fetched_at: 2026-07-27T16:40:43+00:00
---
# Strategy plugins

- [Enabling strategy plugins](strategy.md#enabling-strategy-plugins)
- [Using strategy plugins](strategy.md#using-strategy-plugins)
- [Plugin list](strategy.md#plugin-list)

Strategy plugins control the flow of play execution by handling task and host scheduling. For more information on using strategy plugins and other ways to control execution order, see [Controlling playbook execution: strategies and more](../user_guide/playbooks_strategies.md#playbooks-strategies).

## [Enabling strategy plugins](strategy.md#id2)

All strategy plugins shipped with Ansible are enabled by default. You can enable a custom strategy plugin by
putting it in one of the lookup directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using strategy plugins](strategy.md#id3)

Only one strategy plugin can be used in a play, but you can use different ones for each play in a playbook or ansible run. By default Ansible uses the [linear](../collections/ansible/builtin/linear_strategy.md#linear-strategy) plugin. You can change this default in Ansible [configuration](../reference_appendices/config.md#ansible-configuration-settings) using an environment variable:

```shell
export ANSIBLE_STRATEGY=free
```

or in the ansible.cfg file:

```ini
[defaults]
strategy=linear
```

You can also specify the strategy plugin in the play via the [strategy keyword](../reference_appendices/playbooks_keywords.md#playbook-keywords) in a play:

```YAML+Jinja
- hosts: all
  strategy: debug
  tasks:
    - copy: src=myhosts dest=/etc/hosts
      notify: restart_tomcat

    - package: name=tomcat state=present

  handlers:
    - name: restart_tomcat
      service: name=tomcat state=restarted
```

## [Plugin list](strategy.md#id4)

You can use `ansible-doc -t strategy -l` to see the list of available plugins.
Use `ansible-doc -t strategy <plugin name>` to see plugin-specific specific documentation and examples.

> **See also:**
>
> [Intro to playbooks](../user_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Inventory plugins](inventory.md#inventory-plugins)
> :   Inventory plugins
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
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
