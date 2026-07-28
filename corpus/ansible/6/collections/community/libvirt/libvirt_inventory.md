---
collection: ansible
version: "6"
title: "community.libvirt.libvirt inventory – Libvirt inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/libvirt/libvirt_inventory.html
fetched_at: 2026-07-27T17:16:01+00:00
---
# community.libvirt.libvirt inventory – Libvirt inventory source

> **Note:**
>
> This inventory plugin is part of the [community.libvirt collection](https://galaxy.ansible.com/community/libvirt) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.libvirt`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](libvirt_inventory.md#ansible-collections-community-libvirt-libvirt-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.libvirt.libvirt`.

New in community.libvirt 2.10.0

- [Synopsis](libvirt_inventory.md#synopsis)
- [Requirements](libvirt_inventory.md#requirements)
- [Parameters](libvirt_inventory.md#parameters)
- [Examples](libvirt_inventory.md#examples)

## [Synopsis](libvirt_inventory.md#id1)

- Get libvirt guests in an inventory source.

## [Requirements](libvirt_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- python >= 2.6
- libvirt python bindings

## [Parameters](libvirt_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **inventory_hostname**  string | What to register as the inventory hostname.  If set to ‘uuid’ the uuid of the server will be used and a group will be created for the server name. If set to ‘name’ the name of the server will be used unless there are more than one server with the same name in which case the ‘uuid’ logic will be used. Default is to do ‘name’.  Choices:   - `"name"` ← (default) - `"uuid"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **plugin**  string / required | Token that ensures this is a source file for the ‘libvirt’ plugin.  Choices:   - `"libvirt"` - `"community.libvirt.libvirt"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **uri**  string / required | Libvirt Connection URI |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](libvirt_inventory.md#id4)

```yaml+jinja
# Connect to lxc host
plugin: community.libvirt.libvirt
uri: 'lxc:///'

# Connect to qemu
plugin: community.libvirt.libvirt
uri: 'qemu:///system'
```

### Authors

- Dave Olsthoorn (@daveol)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.libvirt/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.libvirt)
