---
collection: ansible
version: "8"
title: "Vars plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/vars.html
fetched_at: 2026-07-28T01:00:23+00:00
---
# Vars plugins

- [Enabling vars plugins](vars.md#enabling-vars-plugins)
- [Using vars plugins](vars.md#using-vars-plugins)
- [Plugin list](vars.md#plugin-list)

Vars plugins inject additional variable data into Ansible runs that did not come from an inventory source, playbook, or command line. Playbook constructs like ‘host_vars’ and ‘group_vars’ work using vars plugins. For more details about variables in Ansible, see [Using Variables](../playbook_guide/playbooks_variables.md#playbooks-variables).

Vars plugins were partially implemented in Ansible 2.0 and rewritten to be fully implemented starting with Ansible 2.4.

The [host_group_vars](../collections/ansible/builtin/host_group_vars_vars.md#host-group-vars-vars) plugin shipped with Ansible enables reading variables from [Assigning a variable to one machine: host variables](../inventory_guide/intro_inventory.md#host-variables) and [Assigning a variable to many machines: group variables](../inventory_guide/intro_inventory.md#group-variables).

## [Enabling vars plugins](vars.md#id2)

You can activate a custom vars plugin by either dropping it into a `vars_plugins` directory adjacent to your play, inside a role, or by putting it in one of the directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

Most vars plugins are disabled by default. To enable a vars plugin, set `vars_plugins_enabled` in the `defaults` section of [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings) or set the `ANSIBLE_VARS_ENABLED` environment variable to the list of vars plugins you want to execute. By default, the [host_group_vars](../collections/ansible/builtin/host_group_vars_vars.md#host-group-vars-vars) plugin shipped with Ansible is enabled.

Starting in Ansible 2.10, you can use vars plugins in collections. All vars plugins in collections must be explicitly enabled and must use the fully qualified collection name in the format `namespace.collection_name.vars_plugin_name`.

```yaml
[defaults]
vars_plugins_enabled = host_group_vars,namespace.collection_name.vars_plugin_name
```

## [Using vars plugins](vars.md#id3)

By default, vars plugins are used on demand automatically after they are enabled.

Starting in Ansible 2.10, vars plugins can be made to run at specific times. ansible-inventory does not use these settings, and always loads vars plugins.

The global setting `RUN_VARS_PLUGINS` can be set in `ansible.cfg` using `run_vars_plugins` in the `defaults` section or by the `ANSIBLE_RUN_VARS_PLUGINS` environment variable. The default option, `demand`, runs any enabled vars plugins relative to inventory sources whenever variables are demanded by tasks. You can use the option `start` to run any enabled vars plugins relative to inventory sources after importing that inventory source instead.

You can also control vars plugin execution on a per-plugin basis for vars plugins that support the `stage` option. To run the [host_group_vars](../collections/ansible/builtin/host_group_vars_vars.md#host-group-vars-vars) plugin after importing inventory you can add the following to [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings):

```ini
[vars_host_group_vars]
stage = inventory
```

## [Plugin list](vars.md#id4)

You can use `ansible-doc -t vars -l` to see the list of available vars plugins. Use `ansible-doc -t vars <plugin name>` to see plugin-specific documentation and examples.

> **See also:**
>
> [Cache plugins](cache.md#cache-plugins)
> :   Cache plugins
>
> [Lookup plugins](lookup.md#lookup-plugins)
> :   Lookup plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
