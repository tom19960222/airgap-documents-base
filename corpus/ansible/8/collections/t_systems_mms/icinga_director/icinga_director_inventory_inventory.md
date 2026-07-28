---
collection: ansible
version: "8"
title: "t_systems_mms.icinga_director.icinga_director_inventory inventory – Returns Ansible inventory from Icinga"
source_url: https://docs.ansible.com/projects/ansible/8/collections/t_systems_mms/icinga_director/icinga_director_inventory_inventory.html
fetched_at: 2026-07-28T01:05:59+00:00
---
# t_systems_mms.icinga_director.icinga_director_inventory inventory – Returns Ansible inventory from Icinga

> **Note:**
>
> This inventory plugin is part of the [t_systems_mms.icinga_director collection](https://galaxy.ansible.com/ui/repo/published/t_systems_mms/icinga_director/) (version 1.33.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install t_systems_mms.icinga_director`.
>
> To use it in a playbook, specify: `t_systems_mms.icinga_director.icinga_director_inventory`.

- [Synopsis](icinga_director_inventory_inventory.md#synopsis)
- [Parameters](icinga_director_inventory_inventory.md#parameters)
- [Examples](icinga_director_inventory_inventory.md#examples)

## [Synopsis](icinga_director_inventory_inventory.md#id1)

- Returns Ansible inventory from Icinga

## [Parameters](icinga_director_inventory_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **compose**  dictionary | Create vars from jinja2 expressions.  **Default:** `{}` |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  dictionary | Add hosts to group based on Jinja2 conditionals.  **Default:** `{}` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **keyed_groups**  list / elements=dictionary | Add hosts to group based on the values of a variable.  **Default:** `[]` |
| **default_value**  string  *added in ansible-core 2.12* | The default value when the host variable’s value is an empty string.  This option is mutually exclusive with `trailing_separator`. |
| **key**  string | The key from input dictionary used to generate groups |
| **parent_group**  string | parent group for keyed group |
| **prefix**  string | A keyed group name will start with this prefix  **Default:** `""` |
| **separator**  string | separator used to build the keyed group name  **Default:** `"_"` |
| **trailing_separator**  boolean  *added in ansible-core 2.12* | Set this option to *False* to omit the `separator` after the host variable when the value is an empty string.  This option is mutually exclusive with `default_value`.  **Choices:**   - `false` - `true` ← (default) |
| **leading_separator**  boolean  *added in ansible-core 2.11* | Use in conjunction with keyed_groups.  By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.  This is because the default prefix is “” and the default separator is “_”.  Set this option to False to omit the leading underscore (or other separator) if no prefix is given.  If the group name is derived from a mapping the separator is still used to concatenate the items.  To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.  **Choices:**   - `false` - `true` ← (default) |
| **plugin**  string / required | Name of the plugin  **Choices:**   - `"t_systems_mms.icinga_director.icinga_director_inventory"` |
| **strict**  boolean | If `yes` make invalid entries a fatal error, otherwise skip and continue.  Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.  **Choices:**   - `false` ← (default) - `true` |
| **url**  string / required | Icinga URL to connect to |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_extra_vars**  boolean  *added in ansible-core 2.11* | Merge extra vars into the available variables for composition (highest precedence).  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [inventory_plugins]   use_extra_vars = false   ``` - Environment variable: [`ANSIBLE_INVENTORY_USE_EXTRA_VARS`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_USE_EXTRA_VARS) |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](icinga_director_inventory_inventory.md#id3)

```yaml+jinja
plugin: t_systems_mms.icinga_director.icinga_director_inventory
url: 'https://example.com'
url_username: foo
url_password: bar
force_basic_auth: False
strict: False

# use the object_name you defined as hostname
compose:
  hostname: object_name

# create a group based on the operating system defined in a custom variable
keyed_groups:
  - prefix: os
    key: vars.HostOS

# create groups based on jinja templates
# here we create a group called "rb" if the host variable "check_period" is "24/7"
groups:
  rb: check_period == "24/7"
```

### Authors

- Sebastian Gumprich (@rndmh3ro)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/T-Systems-MMS/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/T-Systems-MMS/ansible-collection-icinga-director)
