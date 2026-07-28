---
collection: ansible
version: "8"
title: "community.docker.docker_machine inventory – Docker Machine inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/docker/docker_machine_inventory.html
fetched_at: 2026-07-28T01:44:04+00:00
---
# community.docker.docker_machine inventory – Docker Machine inventory source

> **Note:**
>
> This inventory plugin is part of the [community.docker collection](https://galaxy.ansible.com/ui/repo/published/community/docker/) (version 3.4.11).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.docker`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](docker_machine_inventory.md#ansible-collections-community-docker-docker-machine-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.docker.docker_machine`.

- [Synopsis](docker_machine_inventory.md#synopsis)
- [Requirements](docker_machine_inventory.md#requirements)
- [Parameters](docker_machine_inventory.md#parameters)
- [Examples](docker_machine_inventory.md#examples)

## [Synopsis](docker_machine_inventory.md#id1)

- Get inventory hosts from Docker Machine.
- Uses a YAML configuration file that ends with docker_machine.(yml|yaml).
- The plugin sets standard host variables `ansible_host`, `ansible_port`, `ansible_user` and `ansible_ssh_private_key`.
- The plugin stores the Docker Machine ‘env’ output variables in `dm_` prefixed host variables.

## [Requirements](docker_machine_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- [Docker Machine](https://docs.docker.com/machine/)

## [Parameters](docker_machine_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **daemon_env**  string | Whether docker daemon connection environment variables should be fetched, and how to behave if they cannot be fetched.  With `require` and `require-silently`, fetch them and skip any host for which they cannot be fetched. A warning will be issued for any skipped host if the choice is `require`.  With `optional` and `optional-silently`, fetch them and not skip hosts for which they cannot be fetched. A warning will be issued for hosts where they cannot be fetched if the choice is `optional`.  With `skip`, do not attempt to fetch the docker daemon connection environment variables.  If fetched successfully, the variables will be prefixed with `dm_` and stored as host variables.  **Choices:**   - `"require"` ← (default) - `"require-silently"` - `"optional"` - `"optional-silently"` - `"skip"` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | token that ensures this is a source file for the `docker_machine` plugin.  **Choices:**   - `"docker_machine"` - `"community.docker.docker_machine"` |
| **running_required**  boolean | When `true`, hosts which Docker Machine indicates are in a state other than `running` will be skipped.  **Choices:**   - `false` - `true` ← (default) |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **verbose_output**  boolean | When `true`, include all available nodes metadata (for example `Image`, `Region`, `Size`) as a JSON object named `docker_machine_node_attributes`.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](docker_machine_inventory.md#id4)

```yaml+jinja
# Minimal example
plugin: community.docker.docker_machine

# Example using constructed features to create a group per Docker Machine driver
# (https://docs.docker.com/machine/drivers/), for example:
#   $ docker-machine create --driver digitalocean ... mymachine
#   $ ansible-inventory -i ./path/to/docker-machine.yml --host=mymachine
#   {
#     ...
#     "digitalocean": {
#       "hosts": [
#           "mymachine"
#       ]
#     ...
#   }
strict: false
keyed_groups:
  - separator: ''
    key: docker_machine_node_attributes.DriverName

# Example grouping hosts by Digital Machine tag
strict: false
keyed_groups:
  - prefix: tag
    key: 'dm_tags'

# Example using compose to override the default SSH behaviour of asking the user to accept the remote host key
compose:
  ansible_ssh_common_args: '"-o StrictHostKeyChecking=accept-new"'
```

### Authors

- Ximon Eighteen (@ximon18)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.docker/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.docker)
- [Submit a bug report](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-docker)
