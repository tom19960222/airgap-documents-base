---
collection: ansible
version: "8"
title: "Cache plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/cache.html
fetched_at: 2026-07-28T01:00:12+00:00
---
# Cache plugins

- [Enabling fact cache plugins](cache.md#enabling-fact-cache-plugins)
- [Enabling inventory cache plugins](cache.md#enabling-inventory-cache-plugins)
- [Using cache plugins](cache.md#using-cache-plugins)
- [Plugin list](cache.md#plugin-list)

Cache plugins allow Ansible to store gathered facts or inventory source data without the performance hit of retrieving them from source.

The default cache plugin is the [memory](../collections/ansible/builtin/memory_cache.md#memory-cache) plugin, which only caches the data for the current execution of Ansible. Other plugins with persistent storage are available to allow caching the data across runs. Some of these cache plugins write to files, others write to databases.

You can use different cache plugins for inventory and facts. If you enable inventory caching without setting an inventory-specific cache plugin, Ansible uses the fact cache plugin for both facts and inventory. If necessary, you can [create custom cache plugins](../dev_guide/developing_plugins.md#developing-cache-plugins).

## [Enabling fact cache plugins](cache.md#id2)

Fact caching is always enabled. However, only one fact cache plugin can be active at a time. You can select the cache plugin to use for fact caching in the Ansible configuration, either with an environment variable:

```shell
export ANSIBLE_CACHE_PLUGIN=jsonfile
```

or in the `ansible.cfg` file:

```ini
[defaults]
fact_caching=redis
```

If the cache plugin is in a collection use the fully qualified name:

```ini
[defaults]
fact_caching = namespace.collection_name.cache_plugin_name
```

To enable a custom cache plugin, save it in a `cache_plugins` directory adjacent to your play, inside a role, or in one of the directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

You also need to configure other settings specific to each plugin. Consult the individual plugin documentation or the Ansible [configuration](../reference_appendices/config.md#ansible-configuration-settings) for more details.

## [Enabling inventory cache plugins](cache.md#id3)

Inventory caching is disabled by default. To cache inventory data, you must enable inventory caching and then select the specific cache plugin you want to use. Not all inventory plugins support caching, so check the documentation for the inventory plugin(s) you want to use. You can enable inventory caching with an environment variable:

```shell
export ANSIBLE_INVENTORY_CACHE=True
```

or in the `ansible.cfg` file:

```ini
[inventory]
cache=True
```

or if the inventory plugin accepts a YAML configuration source, in the configuration file:

```yaml
# dev.aws_ec2.yaml
plugin: aws_ec2
cache: True
```

Only one inventory cache plugin can be active at a time. You can set it with an environment variable:

```shell
export ANSIBLE_INVENTORY_CACHE_PLUGIN=jsonfile
```

or in the ansible.cfg file:

```ini
[inventory]
cache_plugin=jsonfile
```

or if the inventory plugin accepts a YAML configuration source, in the configuration file:

```yaml
# dev.aws_ec2.yaml
plugin: aws_ec2
cache_plugin: jsonfile
```

To cache inventory with a custom plugin in your plugin path, follow the [developer guide on cache plugins](../dev_guide/developing_plugins.md#developing-cache-plugins).

To cache inventory with a cache plugin in a collection, use the FQCN:

```ini
[inventory]
cache_plugin=collection_namespace.collection_name.cache_plugin
```

If you enable caching for inventory plugins without selecting an inventory-specific cache plugin, Ansible falls back to caching inventory with the fact cache plugin you configured. Consult the individual inventory plugin documentation or the Ansible [configuration](../reference_appendices/config.md#ansible-configuration-settings) for more details.

## [Using cache plugins](cache.md#id4)

Cache plugins are used automatically once they are enabled.

## [Plugin list](cache.md#id5)

You can use `ansible-doc -t cache -l` to see the list of available plugins.
Use `ansible-doc -t cache <plugin name>` to see plugin-specific documentation and examples.

> **See also:**
>
> [Action plugins](action.md#action-plugins)
> :   Action plugins
>
> [Callback plugins](callback.md#callback-plugins)
> :   Callback plugins
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
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
