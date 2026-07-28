---
collection: ansible
version: "8"
title: "ansible.builtin.constructed inventory – Uses Jinja2 to construct vars and groups based on existing inventory."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/constructed_inventory.html
fetched_at: 2026-07-28T01:04:26+00:00
---
# ansible.builtin.constructed inventory – Uses Jinja2 to construct vars and groups based on existing inventory.

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `constructed`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.constructed` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](constructed_inventory.md#synopsis)
- [Parameters](constructed_inventory.md#parameters)
- [Examples](constructed_inventory.md#examples)

## [Synopsis](constructed_inventory.md#id1)

- Uses a YAML configuration file with a valid YAML or `.config` extension to define var expressions and group conditionals
- The Jinja2 conditionals that qualify a host for membership.
- The Jinja2 expressions are calculated and assigned to the variables
- Only variables already available from previous inventories or the fact cache can be used for templating.
- When *strict* is False, failed expressions will be ignored (assumes vars were missing).

## [Parameters](constructed_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | token that ensures this is a source file for the ‘constructed’ plugin.  **Choices:**   - `"ansible.builtin.constructed"` - `"constructed"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_vars_plugins**  boolean  *added in ansible-core 2.11* | Normally, for performance reasons, vars plugins get executed after the inventory sources complete the base inventory, this option allows for getting vars related to hosts/groups from those plugins.  The host_group_vars (enabled by default) ‘vars plugin’ is the one responsible for reading host_vars/ and group_vars/ directories.  This will execute all vars plugins, even those that are not supposed to execute at the ‘inventory’ stage. See vars plugins docs for details on ‘stage’.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](constructed_inventory.md#id3)

```yaml+jinja
# inventory.config file in YAML format
plugin: ansible.builtin.constructed
strict: False
compose:
    var_sum: var1 + var2

    # this variable will only be set if I have a persistent fact cache enabled (and have non expired facts)
    # `strict: False` will skip this instead of producing an error if it is missing facts.
    server_type: "ansible_hostname | regex_replace ('(.{6})(.{2}).*', '\\2')"
groups:
    # simple name matching
    webservers: inventory_hostname.startswith('web')

    # using ec2 'tags' (assumes aws inventory)
    development: "'devel' in (ec2_tags|list)"

    # using other host properties populated in inventory
    private_only: not (public_dns_name is defined or ip_address is defined)

    # complex group membership
    multi_group: (group_names | intersect(['alpha', 'beta', 'omega'])) | length >= 2

keyed_groups:
    # this creates a group per distro (distro_CentOS, distro_Debian) and assigns the hosts that have matching values to it,
    # using the default separator "_"
    - prefix: distro
      key: ansible_distribution

    # the following examples assume the first inventory is from the `aws_ec2` plugin
    # this creates a group per ec2 architecture and assign hosts to the matching ones (arch_x86_64, arch_sparc, etc)
    - prefix: arch
      key: architecture

    # this creates a group per ec2 region like "us_west_1"
    - prefix: ""
      separator: ""
      key: placement.region

    # this creates a common parent group for all ec2 availability zones
    - key: placement.availability_zone
      parent_group: all_ec2_zones
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
