---
collection: ansible
version: "8"
title: "community.general.proxmox inventory – Proxmox inventory source"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_inventory.html
fetched_at: 2026-07-28T01:52:36+00:00
---
# community.general.proxmox inventory – Proxmox inventory source

> **Note:**
>
> This inventory plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox`.

New in community.general 1.2.0

- [Synopsis](proxmox_inventory.md#synopsis)
- [Requirements](proxmox_inventory.md#requirements)
- [Parameters](proxmox_inventory.md#parameters)
- [Examples](proxmox_inventory.md#examples)

## [Synopsis](proxmox_inventory.md#id1)

- Get inventory hosts from a Proxmox PVE cluster.
- Uses a configuration file as an inventory source, it must end in `.proxmox.yml` or `.proxmox.yaml`
- Will retrieve the first network interface with an IP for Proxmox nodes.
- Can retrieve LXC/QEMU configuration as facts.

## [Requirements](proxmox_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- requests >= 1.1

## [Parameters](proxmox_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **cache**  boolean | Toggle to enable/disable the caching of the inventory’s source data, requires a cache plugin setup to work.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory]   cache = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_CACHE`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE) |
| **cache_connection**  string | Cache connection data or path, read cache plugin documentation for specifics.  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_connection = VALUE   ```  ```YAML+Jinja   [inventory]   cache_connection = VALUE   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION) |
| **cache_plugin**  string | Cache plugin to use for the inventory’s source data.  **Default:** `"memory"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching = memory   ```  ```YAML+Jinja   [inventory]   cache_plugin = memory   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN) |
| **cache_prefix**  string | Prefix to use for cache plugin files/tables  **Default:** `"ansible_inventory_"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [default]   fact_caching_prefix = ansible_inventory_   ```  Removed in: version 2.16 of ansible.builtin  Why: Fixes typing error in INI section name  Alternative: Use the ‘defaults’ section instead  ```YAML+Jinja   [defaults]   fact_caching_prefix = ansible_inventory_   ```  ```YAML+Jinja   [inventory]   cache_prefix = ansible_inventory_   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX) |
| **cache_timeout**  integer | Cache duration in seconds  **Default:** `3600`  **Configuration:**   - INI entries:  ```YAML+Jinja   [defaults]   fact_caching_timeout = 3600   ```  ```YAML+Jinja   [inventory]   cache_timeout = 3600   ``` - Environment variable: [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT) - Environment variable: [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](../../../reference_appendices/config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT) |
| **compose**  dictionary  *added in community.general 2.5.0* | Create vars from jinja2 expressions.  **Default:** `{}` |
| **facts_prefix**  string | Prefix to apply to LXC/QEMU config facts.  **Default:** `"proxmox_"` |
| **filters**  list / elements=string  *added in community.general 4.6.0* | A list of Jinja templates that allow filtering hosts.  **Default:** `[]` |
| **group_prefix**  string | Prefix to apply to Proxmox groups.  **Default:** `"proxmox_"` |
| **groups**  dictionary  *added in community.general 2.5.0* | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **keyed_groups**  list / elements=dictionary  *added in community.general 2.5.0* | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **password**  string | Proxmox authentication password.  If the value is not specified in the inventory configuration, the value of environment variable [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) will be used instead.  Since community.general 4.7.0 you can also use templating to specify the value of the `password`.  If you do not specify a password, you must set `token_id` and `token_secret` instead.  **Configuration:**   - Environment variable: [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD)  *added in community.general 2.0.0* |
| **plugin**  string / required | The name of this plugin, it should always be set to `community.general.proxmox` for this plugin to recognize it as it’s own.  **Choices:**   - `"community.general.proxmox"` |
| **qemu_extended_statuses**  boolean  *added in community.general 5.1.0* | Requires `want_facts` to be set to `true` to function. This will allow you to differentiate between `paused` and `prelaunch` statuses of the QEMU VMs.  This introduces multiple groups [prefixed with `group_prefix`] `prelaunch` and `paused`.  **Choices:**   - `false` ← (default) - `true` |
| **strict**  boolean  *added in community.general 2.5.0* | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **token_id**  string  *added in community.general 4.8.0* | Proxmox authentication token ID.  If the value is not specified in the inventory configuration, the value of environment variable [`PROXMOX_TOKEN_ID`](../../environment_variables.md#envvar-PROXMOX_TOKEN_ID) will be used instead.  To use token authentication, you must also specify `token_secret`. If you do not specify `token_id` and `token_secret`, you must set a password instead.  Make sure to grant explicit pve permissions to the token or disable ‘privilege separation’ to use the users’ privileges instead.  **Configuration:**   - Environment variable: [`PROXMOX_TOKEN_ID`](../../environment_variables.md#envvar-PROXMOX_TOKEN_ID) |
| **token_secret**  string  *added in community.general 4.8.0* | Proxmox authentication token secret.  If the value is not specified in the inventory configuration, the value of environment variable [`PROXMOX_TOKEN_SECRET`](../../environment_variables.md#envvar-PROXMOX_TOKEN_SECRET) will be used instead.  To use token authentication, you must also specify `token_id`. If you do not specify `token_id` and `token_secret`, you must set a password instead.  **Configuration:**   - Environment variable: [`PROXMOX_TOKEN_SECRET`](../../environment_variables.md#envvar-PROXMOX_TOKEN_SECRET) |
| **url**  string | URL to Proxmox cluster.  If the value is not specified in the inventory configuration, the value of environment variable [`PROXMOX_URL`](../../environment_variables.md#envvar-PROXMOX_URL) will be used instead.  Since community.general 4.7.0 you can also use templating to specify the value of the `url`.  **Default:** `"http://localhost:8006"`  **Configuration:**   - Environment variable: [`PROXMOX_URL`](../../environment_variables.md#envvar-PROXMOX_URL)  *added in community.general 2.0.0* |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **user**  string / required | Proxmox authentication user.  If the value is not specified in the inventory configuration, the value of environment variable [`PROXMOX_USER`](../../environment_variables.md#envvar-PROXMOX_USER) will be used instead.  Since community.general 4.7.0 you can also use templating to specify the value of the `user`.  **Configuration:**   - Environment variable: [`PROXMOX_USER`](../../environment_variables.md#envvar-PROXMOX_USER)  *added in community.general 2.0.0* |
| **validate_certs**  boolean | Verify SSL certificate if using HTTPS.  **Choices:**   - `false` - `true` ← (default) |
| **want_facts**  boolean | Gather LXC/QEMU configuration facts.  When `want_facts` is set to `true` more details about QEMU VM status are possible, besides the running and stopped states. Currently if the VM is running and it is suspended, the status will be running and the machine will be in `running` group, but its actual state will be paused. See `qemu_extended_statuses` for how to retrieve the real status.  **Choices:**   - `false` ← (default) - `true` |
| **want_proxmox_nodes_ansible_host**  boolean  *added in community.general 3.0.0* | Whether to set `ansible_host` for proxmox nodes.  When set to `true` (default), will use the first available interface. This can be different from what you expect.  The default of this option changed from `true` to `false` in community.general 6.0.0.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](proxmox_inventory.md#id4)

```yaml+jinja
# Minimal example which will not gather additional facts for QEMU/LXC guests
# By not specifying a URL the plugin will attempt to connect to the controller host on port 8006
# my.proxmox.yml
plugin: community.general.proxmox
user: ansible@pve
password: secure
# Note that this can easily give you wrong values as ansible_host. See further below for
# an example where this is set to `false` and where ansible_host is set with `compose`.
want_proxmox_nodes_ansible_host: true

# Instead of login with password, proxmox supports api token authentication since release 6.2.
plugin: community.general.proxmox
user: ci@pve
token_id: gitlab-1
token_secret: fa256e9c-26ab-41ec-82da-707a2c079829

# The secret can also be a vault string or passed via the environment variable TOKEN_SECRET.
token_secret: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          62353634333163633336343265623632626339313032653563653165313262343931643431656138
          6134333736323265656466646539663134306166666237630a653363623262636663333762316136
          34616361326263383766366663393837626437316462313332663736623066656237386531663731
          3037646432383064630a663165303564623338666131353366373630656661333437393937343331
          32643131386134396336623736393634373936356332623632306561356361323737313663633633
          6231313333666361656537343562333337323030623732323833

# More complete example demonstrating the use of 'want_facts' and the constructed options
# Note that using facts returned by 'want_facts' in constructed options requires 'want_facts=true'
# my.proxmox.yml
plugin: community.general.proxmox
url: http://pve.domain.com:8006
user: ansible@pve
password: secure
validate_certs: false
want_facts: true
keyed_groups:
    # proxmox_tags_parsed is an example of a fact only returned when 'want_facts=true'
  - key: proxmox_tags_parsed
    separator: ""
    prefix: group
groups:
  webservers: "'web' in (proxmox_tags_parsed|list)"
  mailservers: "'mail' in (proxmox_tags_parsed|list)"
compose:
  ansible_port: 2222
# Note that this can easily give you wrong values as ansible_host. See further below for
# an example where this is set to `false` and where ansible_host is set with `compose`.
want_proxmox_nodes_ansible_host: true

# Using the inventory to allow ansible to connect via the first IP address of the VM / Container
# (Default is connection by name of QEMU/LXC guests)
# Note: my_inv_var demonstrates how to add a string variable to every host used by the inventory.
# my.proxmox.yml
plugin: community.general.proxmox
url: http://pve.domain.com:8006
user: ansible@pve
password: secure
validate_certs: false
want_facts: true
want_proxmox_nodes_ansible_host: false
compose:
  ansible_host: proxmox_ipconfig0.ip | default(proxmox_net0.ip) | ipaddr('address')
  my_inv_var_1: "'my_var1_value'"
  my_inv_var_2: >
    "my_var_2_value"

# Specify the url, user and password using templating
# my.proxmox.yml
plugin: community.general.proxmox
url: "{{ lookup('ansible.builtin.ini', 'url', section='proxmox', file='file.ini') }}"
user: "{{ lookup('ansible.builtin.env','PM_USER') | default('ansible@pve') }}"
password: "{{ lookup('community.general.random_string', base64=True) }}"
# Note that this can easily give you wrong values as ansible_host. See further up for
# an example where this is set to `false` and where ansible_host is set with `compose`.
want_proxmox_nodes_ansible_host: true
```

### Authors

- Jeffrey van Pelt (@Thulium-Drake)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
