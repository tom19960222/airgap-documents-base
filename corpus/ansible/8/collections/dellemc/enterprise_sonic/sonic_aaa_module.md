---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_aaa module – Manage AAA and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_aaa_module.html
fetched_at: 2026-07-28T02:03:24+00:00
---
# dellemc.enterprise_sonic.sonic_aaa module – Manage AAA and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_aaa`.

New in dellemc.enterprise_sonic 1.1.0

- [Synopsis](sonic_aaa_module.md#synopsis)
- [Parameters](sonic_aaa_module.md#parameters)
- [Notes](sonic_aaa_module.md#notes)
- [Examples](sonic_aaa_module.md#examples)
- [Return Values](sonic_aaa_module.md#return-values)

## [Synopsis](sonic_aaa_module.md#id1)

- This module is used for configuration management of aaa parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_aaa_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the aaa related configurations |
| **authentication**  dictionary | Specifies the configurations required for aaa authentication |
| **data**  dictionary | Specifies the data required for aaa authentication |
| **fail_through**  boolean | Specifies the state of failthrough  **Choices:**   - `false` - `true` |
| **group**  string | Specifies the method of aaa authentication  **Choices:**   - `"ldap"` - `"radius"` - `"tacacs+"` |
| **local**  boolean | Enable or Disable local authentication  **Choices:**   - `false` - `true` |
| **state**  string | Specifies the operation to be performed on the aaa parameters configured on the device.  In case of merged, the input configuration will be merged with the existing aaa configuration on the device.  In case of deleted the existing aaa configuration will be removed from the device.  In case of replaced, the existing aaa configuration will be replaced with provided configuration.  In case of overridden, the existing aaa configuration will be overridden with the provided configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"overridden"` - `"replaced"` |

## [Notes](sonic_aaa_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_aaa_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local

- name: Delete aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        data:
          local: True
    state: deleted

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method :

# Using deleted
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local

- name: Delete aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
    state: deleted

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  :
# login-method :

# Using merged
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : False
# login-method :

- name: Merge aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        data:
          local: true
          fail_through: true
    state: merged

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local

# Using replaced
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : False
# login-method : local, radius

- name: Replace aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        data:
          group: ldap
          fail_through: true
    state: replaced

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local, ldap

# Using overridden
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : False
# login-method : local, radius

- name: Override aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        data:
          group: tacacs+
          fail_through: true
    state: overridden

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : tacacs+
```

## [Return Values](sonic_aaa_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
