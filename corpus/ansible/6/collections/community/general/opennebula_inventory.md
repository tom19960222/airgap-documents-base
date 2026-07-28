---
collection: ansible
version: "6"
title: "community.general.opennebula inventory – OpenNebula inventory source"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/opennebula_inventory.html
fetched_at: 2026-07-27T17:14:50+00:00
---
# community.general.opennebula inventory – OpenNebula inventory source

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.opennebula`.

New in community.general 3.8.0

- [Synopsis](opennebula_inventory.md#synopsis)
- [Parameters](opennebula_inventory.md#parameters)
- [Examples](opennebula_inventory.md#examples)

## [Synopsis](opennebula_inventory.md#id1)

- Get inventory hosts from OpenNebula cloud.
- Uses an YAML configuration file ending with either *opennebula.yml* or *opennebula.yaml* to set parameter values.
- Uses *api_authfile*, `~/.one/one_auth`, or `ONE_AUTH` pointing to a OpenNebula credentials file.

## [Parameters](opennebula_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_authfile**  string | If both *api_username* or *api_password* are not set, then it will try authenticate with ONE auth file. Default path is `~/.one/one_auth`.  Set environment variable `ONE_AUTH` to override this path.  Configuration:   - Environment variable: [`ONE_AUTH`](../../environment_variables.md#envvar-ONE_AUTH) |
| **api_password**  string | Password or a token of the user to login into OpenNebula RPC server.  If not set, the value of the `ONE_PASSWORD` environment variable is used.  Configuration:   - Environment variable: [`ONE_PASSWORD`](../../environment_variables.md#envvar-ONE_PASSWORD) |
| **api_url**  string / required | URL of the OpenNebula RPC server.  It is recommended to use HTTPS so that the username/password are not transferred over the network unencrypted.  If not set then the value of the `ONE_URL` environment variable is used.  Configuration:   - Environment variable: [`ONE_URL`](../../environment_variables.md#envvar-ONE_URL) |
| **api_username**  string | Name of the user to login into the OpenNebula RPC server. If not set then the value of the `ONE_USERNAME` environment variable is used.  Configuration:   - Environment variable: [`ONE_USERNAME`](../../environment_variables.md#envvar-ONE_USERNAME) |
| **compose**  dictionary | Create vars from jinja2 expressions.  Default: `{}` |
| **filter_by_label**  string | Only return servers filtered by this label. |
| **group_by_labels**  boolean | Create host groups by vm labels  Choices:   - `false` - `true` ← (default) |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  Default: `{}` |
| **hostname**  string | Field to match the hostname. Note `v4_first_ip` corresponds to the first IPv4 found on VM.  Choices:   - `"v4_first_ip"` ← (default) - `"v6_first_ip"` - `"name"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  Default: `[]` |
| **default_value**  string  added in ansible-core 2.12 | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  Default: `""` |
| **separator**  string | separator used to build the keyed group name  Default: `"_"` |
| **trailing_separator**  boolean  added in ansible-core 2.12 | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  Choices:   - `false` - `true` ← (default) |
| **leading_separator**  boolean  added in ansible-core 2.11 | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  Choices:   - `false` - `true` ← (default) |
| **plugin**  string / required | Token that ensures this is a source file for the ‘opennebula’ plugin.  Choices:   - `"community.general.opennebula"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  Choices:   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  added in ansible-core 2.11 | Merge extra vars into the available variables for composition (highest precedence).  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |

## [Examples](opennebula_inventory.md#id3)

```yaml+jinja
# inventory_opennebula.yml file in YAML format
# Example command line: ansible-inventory --list -i inventory_opennebula.yml

# Pass a label filter to the API
plugin: community.general.opennebula
api_url: https://opennebula:2633/RPC2
filter_by_label: Cache
```

### Authors

- Kristian Feldsam (@feldsam)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
