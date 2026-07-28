---
collection: ansible
version: "8"
title: "Test plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/test.html
fetched_at: 2026-07-28T01:00:22+00:00
---
# Test plugins

- [Enabling test plugins](test.md#enabling-test-plugins)
- [Using test plugins](test.md#using-test-plugins)

  - [Using test plugins with lists](test.md#using-test-plugins-with-lists)
- [Plugin list](test.md#plugin-list)

Test plugins evaluate template expressions and return True or False. With test plugins you can create [conditionals](../playbook_guide/playbooks_conditionals.md#playbooks-conditionals) to implement the logic of your tasks, blocks, plays, playbooks, and roles. Ansible uses the [standard tests](https://jinja.palletsprojects.com/en/latest/templates/#builtin-tests) shipped as part of Jinja and adds some specialized test plugins. You can [create custom Ansible test plugins](../dev_guide/developing_plugins.md#developing-test-plugins).

## [Enabling test plugins](test.md#id2)

You can add a custom test plugin by dropping it into a `test_plugins` directory adjacent to your play, inside a role, or by putting it in one of the test plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using test plugins](test.md#id3)

You can use tests anywhere you can use templating in Ansible: in a play, in a variables file, or in a Jinja2 template for the [template](../collections/ansible/builtin/template_module.md#template-module) module. For more information on using test plugins, see [Tests](../playbook_guide/playbooks_tests.md#playbooks-tests).

Tests always return `True` or `False`, they are always a boolean, if you need a different return type, you should be looking at filters.

You can recognize test plugins by the use of the `is` statement in a template, they can also be used as part of the `select` family of filters.

```YAML+Jinja
vars:
  is_ready: '{{ task_result is success }}'

tasks:
- name: conditionals are always in 'template' context
  action: dostuff
  when: task_result is failed
```

Tests will always have an `_input` and this is normally what is on the left side of `is`. Tests can also take additional parameters as you would to most programming functions. These parameters can be either `positional` (passed in order) or `named` (passed as key=value pairs). When passing both types, positional arguments should go first.

```YAML+Jinja
tasks:
- name: pass a positional parameter to match test
  action: dostuff
  when: myurl is match("https://example.com/users/.*/resources")

- name: pass named parameter to truthy test
  action: dostuff
  when: myvariable is truthy(convert_bool=True)

- name: pass both types to 'version' test
  action: dostuff
  when: sample_semver_var is version('2.0.0-rc.1+build.123', 'lt', version_type='semver')
```

### [Using test plugins with lists](test.md#id4)

As mentioned above, one way to use tests is with the `select` family of filters (`select`, `reject`, `selectattr`, `rejectattr`).

```YAML+Jinja
# give me only defined variables from a list of variables, using 'defined' test
good_vars: "{{ all_vars|select('defined') }}"

# this uses the 'equalto' test to filter out non 'fixed' type of addresses from a list
only_fixed_addresses:  "{{ all_addresses|selectattr('type', 'equalto', 'fixed') }}"

# this does the opposite of the previous one
only_fixed_addresses:  "{{ all_addresses|rejectattr('type', 'equalto', 'fixed') }}"
```

## [Plugin list](test.md#id5)

You can use `ansible-doc -t test -l` to see the list of available plugins. Use `ansible-doc -t test <plugin name>` to see plugin-specific documentation and examples.

> **See also:**
>
> [Ansible playbooks](../playbook_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Tests](../playbook_guide/playbooks_tests.md#playbooks-tests)
> :   Using tests
>
> [Conditionals](../playbook_guide/playbooks_conditionals.md#playbooks-conditionals)
> :   Using conditional statements
>
> [Filter plugins](filter.md#filter-plugins)
> :   Filter plugins
>
> [Tests](../playbook_guide/playbooks_tests.md#playbooks-tests)
> :   Using tests
>
> [Lookup plugins](lookup.md#lookup-plugins)
> :   Lookup plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
