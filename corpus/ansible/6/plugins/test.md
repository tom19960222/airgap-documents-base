---
collection: ansible
version: "6"
title: "Test plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/test.html
fetched_at: 2026-07-27T16:40:44+00:00
---
# Test plugins

- [Enabling test plugins](test.md#enabling-test-plugins)
- [Using test plugins](test.md#using-test-plugins)

Test plugins evaluate template expressions and return True or False. With test plugins you can create [conditionals](../user_guide/playbooks_conditionals.md#playbooks-conditionals) to implement the logic of your tasks, blocks, plays, playbooks, and roles. Ansible uses the standard tests `_ shipped as part of Jinja, and adds some specialized test plugins. You can :ref:`create custom Ansible test plugins <developing_test_plugins>.

## [Enabling test plugins](test.md#id2)

You can add a custom test plugin by dropping it into a `test_plugins` directory adjacent to your play, inside a role, or by putting it in one of the test plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using test plugins](test.md#id3)

The User Guide offers detailed documentation on [using test plugins](../user_guide/playbooks_tests.md#playbooks-tests).

> **See also:**
>
> [Intro to playbooks](../user_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Tests](../user_guide/playbooks_tests.md#playbooks-tests)
> :   Using tests
>
> [Conditionals](../user_guide/playbooks_conditionals.md#playbooks-conditionals)
> :   Using conditional statements
>
> [Filter plugins](filter.md#filter-plugins)
> :   Filter plugins
>
> [Using filters to manipulate data](../user_guide/playbooks_filters.md#playbooks-filters)
> :   Using filters
>
> [Lookup plugins](lookup.md#lookup-plugins)
> :   Lookup plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
