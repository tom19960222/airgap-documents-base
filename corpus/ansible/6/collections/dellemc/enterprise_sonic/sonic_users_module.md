---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_users module – Manage users and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_users_module.html
fetched_at: 2026-07-27T17:25:00+00:00
---
# dellemc.enterprise_sonic.sonic_users module – Manage users and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_users`.

New in dellemc.enterprise_sonic 1.1.0

- [Synopsis](sonic_users_module.md#synopsis)
- [Parameters](sonic_users_module.md#parameters)
- [Notes](sonic_users_module.md#notes)
- [Examples](sonic_users_module.md#examples)
- [Return Values](sonic_users_module.md#return-values)

## [Synopsis](sonic_users_module.md#id1)

- This module provides configuration management of users parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_users_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the users related configuration. |
| **name**  string / required | Specifies the name of the user. |
| **password**  string | Specifies the password of the user. |
| **role**  string | Specifies the role of the user.  Choices:   - `"admin"` - `"operator"` |
| **update_password**  string | Specifies the update password flag.  In case of always, password will be updated every time.  In case of on_create, password will be updated only when user is created.  Choices:   - `"always"` ← (default) - `"on_create"` |
| **state**  string | Specifies the operation to be performed on the users configured on the device.  In case of merged, the input configuration will be merged with the existing users configuration on the device.  In case of deleted the existing users configuration will be removed from the device.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_users_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_users_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#do show running-configuration
#!
#username admin password $6$sdZt2C7F$3oPSRkkJyLZtsKlFNGWdwssblQWBj5dXM6qAJAQl7dgOfqLSpZJ/n6xf8zPRcqPUFCu5ZKpEtynJ9sZ/S8Mgj. role admin
#username sysadmin password $6$3QNqJzpFAPL9JqHA$417xFKw6SRn.CiqMFJkDfQJXKJGjeYwi2A8BIyfuWjGimvunOOjTRunVluudey/W9l8jhzN1oewBW5iLxmq2Q1 role admin
#username sysoperator password $6$s1eTVjcX4Udi69gY$zlYgqwoKRGC6hGL5iKDImN/4BL7LXKNsx9e5PoSsBLs6C80ShYj2LoJAUZ58ia2WNjcHXhTD1p8eU9wyRTCiE0 role operator
#
- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_users:
    config:
      - name: sysoperator
    state: deleted
# After state:
# ------------
#
#do show running-configuration
#!
#username admin password $6$sdZt2C7F$3oPSRkkJyLZtsKlFNGWdwssblQWBj5dXM6qAJAQl7dgOfqLSpZJ/n6xf8zPRcqPUFCu5ZKpEtynJ9sZ/S8Mgj. role admin
#username sysadmin password $6$3QNqJzpFAPL9JqHA$417xFKw6SRn.CiqMFJkDfQJXKJGjeYwi2A8BIyfuWjGimvunOOjTRunVluudey/W9l8jhzN1oewBW5iLxmq2Q1 role admin

# Using deleted
#
# Before state:
# -------------
#
#do show running-configuration
#!
#username admin password $6$sdZt2C7F$3oPSRkkJyLZtsKlFNGWdwssblQWBj5dXM6qAJAQl7dgOfqLSpZJ/n6xf8zPRcqPUFCu5ZKpEtynJ9sZ/S8Mgj. role admin
#username sysadmin password $6$3QNqJzpFAPL9JqHA$417xFKw6SRn.CiqMFJkDfQJXKJGjeYwi2A8BIyfuWjGimvunOOjTRunVluudey/W9l8jhzN1oewBW5iLxmq2Q1 role admin
#username sysoperator password $6$s1eTVjcX4Udi69gY$zlYgqwoKRGC6hGL5iKDImN/4BL7LXKNsx9e5PoSsBLs6C80ShYj2LoJAUZ58ia2WNjcHXhTD1p8eU9wyRTCiE0 role operator
#
- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_users:
    config:
    state: deleted

# After state:
# ------------
#
#do show running-configuration
#!
#username admin password $6$sdZt2C7F$3oPSRkkJyLZtsKlFNGWdwssblQWBj5dXM6qAJAQl7dgOfqLSpZJ/n6xf8zPRcqPUFCu5ZKpEtynJ9sZ/S8Mgj. role admin

# Using merged
#
# Before state:
# -------------
#
#do show running-configuration
#!
#username admin password $6$sdZt2C7F$3oPSRkkJyLZtsKlFNGWdwssblQWBj5dXM6qAJAQl7dgOfqLSpZJ/n6xf8zPRcqPUFCu5ZKpEtynJ9sZ/S8Mgj. role admin
#
- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_users:
    config:
      - name: sysadmin
        role: admin
        password: admin
        update_password: always
      - name: sysoperator
        role: operator
        password: operator
        update_password: always
    state: merged

# After state:
# ------------
#!
#do show running-configuration
#!
#username admin password $6$sdZt2C7F$3oPSRkkJyLZtsKlFNGWdwssblQWBj5dXM6qAJAQl7dgOfqLSpZJ/n6xf8zPRcqPUFCu5ZKpEtynJ9sZ/S8Mgj. role admin
#username sysadmin password $6$3QNqJzpFAPL9JqHA$417xFKw6SRn.CiqMFJkDfQJXKJGjeYwi2A8BIyfuWjGimvunOOjTRunVluudey/W9l8jhzN1oewBW5iLxmq2Q1 role admin
#username sysoperator password $6$s1eTVjcX4Udi69gY$zlYgqwoKRGC6hGL5iKDImN/4BL7LXKNsx9e5PoSsBLs6C80ShYj2LoJAUZ58ia2WNjcHXhTD1p8eU9wyRTCiE0 role operator
```

## [Return Values](sonic_users_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
