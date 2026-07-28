---
collection: ansible
version: "6"
title: "Documenting new network platforms"
source_url: https://docs.ansible.com/projects/ansible/6/network/dev_guide/documenting_modules_network.html
fetched_at: 2026-07-27T16:40:09+00:00
---
# Documenting new network platforms

- [Modifying the platform options table](documenting_modules_network.md#modifying-the-platform-options-table)
- [Adding a platform-specific options section](documenting_modules_network.md#adding-a-platform-specific-options-section)
- [Adding your new file to the table of contents](documenting_modules_network.md#adding-your-new-file-to-the-table-of-contents)

When you create network modules for a new platform, or modify the connections provided by an existing network platform (such as `network_cli` and `httpapi`), you also need to update the [Settings by Platform](../user_guide/platform_index.md#settings-by-platform) table and add or modify the Platform Options file for your platform.

You should already have documented each module as described in [Module format and documentation](../../dev_guide/developing_modules_documenting.md#developing-modules-documenting).

## [Modifying the platform options table](documenting_modules_network.md#id1)

The [Settings by Platform](../user_guide/platform_index.md#settings-by-platform) table is a convenient summary of the connections options provided by each network platform that has modules in Ansible. Add a row for your platform to this table, in alphabetical order. For example:

```
+-------------------+-------------------------+-------------+---------+---------+----------+
| My OS             | ``myos``                | ✓           | ✓       |         | ✓        |
```

Ensure that the table stays formatted correctly. That is:

- Each row is inserted in alphabetical order.
- The cell division `|` markers line up with the `+` markers.
- The check marks appear only for the connection types provided by the network modules.

## [Adding a platform-specific options section](documenting_modules_network.md#id2)

The platform- specific sections are individual `.rst` files that provide more detailed information for the users of your network platform modules. Name your new file `platform_<name>.rst` (for example, `platform_myos.rst`). The platform name should match the module prefix. See [platform_eos.rst](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/network/user_guide/platform_eos.rst) and [EOS Platform Options](../user_guide/platform_eos.md#eos-platform-options) for an example of the details you should provide in your platform-specific options section.

Your platform-specific section should include the following:

- **Connections available table** - a deeper dive into each connection type, including details on credentials, indirect access, connections settings, and enable mode.
- **How to use each connection type** - with working examples of each connection type.

If your network platform supports SSH connections, also include the following at the bottom of your `.rst` file:

```
.. include:: shared_snippets/SSH_warning.txt
```

## [Adding your new file to the table of contents](documenting_modules_network.md#id3)

As a final step, add your new file in alphabetical order in the `platform_index.rst` file. You should then build the documentation to verify your additions. See [Contributing to the Ansible Documentation](../../community/documentation_contributions.md#community-documentation-contributions) for more details.
