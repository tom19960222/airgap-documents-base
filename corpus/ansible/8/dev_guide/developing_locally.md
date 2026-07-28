---
collection: ansible
version: "8"
title: "Adding modules and plugins locally"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/developing_locally.html
fetched_at: 2026-07-28T00:59:04+00:00
---
# Adding modules and plugins locally

You can extend Ansible by adding custom modules or plugins. You can create them from scratch or copy existing ones for local use. You can store a local module or plugin on your Ansible control node and share it with your team or organization. You can also share plugins and modules by including them in a collection, then publishing the collection on Ansible Galaxy.

If you are using a local module or plugin but Ansible cannot find it, this page is all you need.

If you want to create a plugin or a module, see [Developing plugins](developing_plugins.md#developing-plugins), [Developing modules](developing_modules_general.md#developing-modules-general) and [Developing collections](developing_collections.md#developing-collections).

Extending Ansible with local modules and plugins offers shortcuts such as:

- You can copy other people’s modules and plugins.
- When writing a new module, you can choose any programming language you like.
- You do not have to clone any repositories.
- You do not have to open a pull request.
- You do not have to add tests (though we recommend that you do!).

- [Modules and plugins: what is the difference?](developing_locally.md#modules-and-plugins-what-is-the-difference)
- [Adding modules and plugins in collections](developing_locally.md#adding-modules-and-plugins-in-collections)
- [Adding a module or plugin outside of a collection](developing_locally.md#adding-a-module-or-plugin-outside-of-a-collection)

  - [Adding standalone local modules for all playbooks and roles](developing_locally.md#adding-standalone-local-modules-for-all-playbooks-and-roles)
  - [Adding standalone local modules for selected playbooks or a single role](developing_locally.md#adding-standalone-local-modules-for-selected-playbooks-or-a-single-role)
- [Adding a non-module plugin locally outside of a collection](developing_locally.md#adding-a-non-module-plugin-locally-outside-of-a-collection)

  - [Adding local non-module plugins for all playbooks and roles](developing_locally.md#adding-local-non-module-plugins-for-all-playbooks-and-roles)
  - [Adding standalone local plugins for selected playbooks or a single role](developing_locally.md#adding-standalone-local-plugins-for-selected-playbooks-or-a-single-role)
- [Using `ansible.legacy` to access custom versions of an `ansible.builtin` module](developing_locally.md#using-ansible-legacy-to-access-custom-versions-of-an-ansible-builtin-module)

## [Modules and plugins: what is the difference?](developing_locally.md#id1)

If you are looking to add functionality to Ansible, you might wonder whether you need a module or a plugin. Here is a quick overview to help you understand what you need:

- [Plugins](../plugins/plugins.md#working-with-plugins) extend Ansible’s core functionality. Most plugin types execute on the control node within the `/usr/bin/ansible` process. Plugins offer options and extensions for the core features of Ansible: transforming data, logging output, connecting to inventory, and more.
- Modules are a type of plugin that execute automation tasks on a ‘target’ (usually a remote system). Modules work as standalone scripts that Ansible executes in their own process outside of the control node. Modules interface with Ansible mostly with JSON, accepting arguments and returning information by printing a JSON string to stdout before exiting. Unlike the other plugins (which must be written in Python), modules can be written in any language; although Ansible provides modules in Python and Powershell only.

## [Adding modules and plugins in collections](developing_locally.md#id2)

You can add modules and plugins by [creating a collection](developing_collections.md#developing-collections). With a collection, you can use custom modules and plugins in any playbook or role. You can share your collection easily at any time through Ansible Galaxy.

The rest of this page describes other methods of using local, standalone modules or plugins.

## [Adding a module or plugin outside of a collection](developing_locally.md#id3)

You can configure Ansible to load standalone local modules or plugins in specific locations and make them available to all playbooks and roles (using configured paths). Alternatively, you can make a non-collection local module or plugin available only to certain playbooks or roles (with adjacent paths).

### [Adding standalone local modules for all playbooks and roles](developing_locally.md#id4)

To load standalone local modules automatically and make them available to all playbooks and roles, use the [DEFAULT_MODULE_PATH](../reference_appendices/config.md#default-module-path) configuration setting or the `ANSIBLE_LIBRARY` environment variable. The configuration setting and environment variable take a colon-separated list, similar to `$PATH`. You have two options:

- Add your standalone local module to one of the default configured locations. See the [DEFAULT_MODULE_PATH](../reference_appendices/config.md#default-module-path) configuration setting for details. Default locations may change without notice.
- Add the location of your standalone local module to an environment variable or configuration:
  :   - the `ANSIBLE_LIBRARY` environment variable
      - the [DEFAULT_MODULE_PATH](../reference_appendices/config.md#default-module-path) configuration setting

To view your current configuration settings for modules:

```
ansible-config dump |grep DEFAULT_MODULE_PATH
```

After you save your module file in one of these locations, Ansible loads it and you can use it in any local task, playbook, or role.

To confirm that `my_local_module` is available:

- type `ansible localhost -m my_local_module` to see the output for that module, or
- type `ansible-doc -t module my_local_module` to see the documentation for that module

> **Note:**
>
> This applies to all plugin types but requires specific configuration and/or adjacent directories for each plugin type, see below.

> **Note:**
>
> The `ansible-doc` command can parse module documentation from modules written in Python or an adjacent YAML file. If you have a module written in a programming language other than Python, you should write the documentation in a Python or YAML file adjacent to the module file. [Adjacent YAML documentation files](sidecar.md#adjacent-yaml-doc)

### [Adding standalone local modules for selected playbooks or a single role](developing_locally.md#id5)

Ansible automatically loads all executable files from certain directories adjacent to your playbook or role as modules. Standalone modules in these locations are available only to the specific playbook, playbooks, or role in the parent directory.

- To use a standalone module only in a selected playbook or playbooks, store the module in a subdirectory called `library` in the directory that contains the playbook or playbooks.
- To use a standalone module only in a single role, store the module in a subdirectory called `library` within that role.

> **Note:**
>
> This applies to all plugin types but requires specific configuration and/or adjacent directories for each plugin type, see below.

> **Warning:**
>
> Roles contained in collections cannot contain any modules or other plugins. All plugins in a collection must live in the collection `plugins` directory tree. All plugins in that tree are accessible to all roles in the collection. If you are developing new modules, we recommend distributing them in [collections](developing_collections.md#developing-collections), not in roles.

## [Adding a non-module plugin locally outside of a collection](developing_locally.md#id6)

You can configure Ansible to load standalone local plugins in a specified location or locations and make them available to all playbooks and roles. Alternatively, you can make a standalone local plugin available only to specific playbooks or roles.

> **Note:**
>
> Although modules are plugins, the naming patterns for directory names and environment variables that apply to other plugin types do not apply to modules. See [Adding a module or plugin outside of a collection](developing_locally.md#local-modules).

### [Adding local non-module plugins for all playbooks and roles](developing_locally.md#id7)

To load standalone local plugins automatically and make them available to all playbooks and roles, use the configuration setting or environment variable for the type of plugin you are adding. These configuration settings and environment variables take a colon-separated list, similar to `$PATH`. You have two options:

- Add your local plugin to one of the default configured locations. See [configuration settings](../reference_appendices/config.md#ansible-configuration-settings) for details on the correct configuration setting for the plugin type. Default locations may change without notice.
- Add the location of your local plugin to an environment variable or configuration:
  :   - the relevant `ANSIBLE_plugin_type_PLUGINS` environment variable - for example, `$ANSIBLE_INVENTORY_PLUGINS` or `$ANSIBLE_VARS_PLUGINS`
      - the relevant `plugin_type_PATH` configuration setting, most of which begin with `DEFAULT_` - for example, `DEFAULT_CALLBACK_PLUGIN_PATH` or `DEFAULT_FILTER_PLUGIN_PATH` or `BECOME_PLUGIN_PATH`

To view your current configuration settings for non-module plugins:

```
ansible-config dump |grep plugin_type_PATH
```

After your plugin file is added to one of these locations, Ansible loads it and you can use it in any local module, task, playbook, or role. For more information on environment variables and configuration settings, see [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings).

To confirm that `plugins/plugin_type/my_local_plugin` is available:

- type `ansible-doc -t <plugin_type> my_local_lookup_plugin` to see the documentation for that plugin - for example, `ansible-doc -t lookup my_local_lookup_plugin`

The `ansible-doc` command works for most plugin types, but not for action, filter, or test plugins. See [ansible-doc](../cli/ansible-doc.md#ansible-doc) for more details.

### [Adding standalone local plugins for selected playbooks or a single role](developing_locally.md#id8)

Ansible automatically loads all plugins from certain directories adjacent to your playbook or role, loading each type of plugin separately from a directory named for the type of plugin. Standalone plugins in these locations are available only to the specific playbook, playbooks, or role in the parent directory.

- To use a standalone plugin only in a selected playbook or playbooks, store the plugin in a subdirectory for the correct `plugin_type` (for example, `callback_plugins` or `inventory_plugins`) in the directory that contains the playbooks. These directories must use the `_plugins` suffix. For a full list of plugin types, see [Working with plugins](../plugins/plugins.md#working-with-plugins).
- To use a standalone plugin only in a single role, store the plugin in a subdirectory for the correct `plugin_type` (for example, `cache_plugins` or `strategy_plugins`) within that role. When shipped as part of a role, the plugin is available as soon as the role is executed. These directories must use the `_plugins` suffix. For a full list of plugin types, see [Working with plugins](../plugins/plugins.md#working-with-plugins).

> **Warning:**
>
> Roles contained in collections cannot contain any plugins. All plugins in a collection must live in the collection `plugins` directory tree. All plugins in that tree are accessible to all roles in the collection. If you are developing new plugins, we recommend distributing them in [collections](developing_collections.md#developing-collections), not in roles.

## [Using `ansible.legacy` to access custom versions of an `ansible.builtin` module](developing_locally.md#id9)

If you need to override one of the `ansible.builtin` modules and are using FQCN, you need to use `ansible.legacy` as part of the fully-qualified collection name (FQCN). For example, if you had your own `copy` module, you would access it as `ansible.legacy.copy`. See [Using ansible.legacy to access local custom modules from collections-based roles](migrating_roles.md#using-ansible-legacy) for details on how to use custom modules with roles within a collection.
