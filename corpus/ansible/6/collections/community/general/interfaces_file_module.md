---
collection: ansible
version: "6"
title: "community.general.interfaces_file module – Tweak settings in /etc/network/interfaces files"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/interfaces_file_module.html
fetched_at: 2026-07-27T17:09:49+00:00
---
# community.general.interfaces_file module – Tweak settings in /etc/network/interfaces files

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.interfaces_file`.

- [Synopsis](interfaces_file_module.md#synopsis)
- [Parameters](interfaces_file_module.md#parameters)
- [Notes](interfaces_file_module.md#notes)
- [Examples](interfaces_file_module.md#examples)
- [Return Values](interfaces_file_module.md#return-values)

## [Synopsis](interfaces_file_module.md#id1)

- Manage (add, remove, change) individual interface options in an interfaces-style file without having to manage the file as a whole with, say, [ansible.builtin.template](../../ansible/builtin/template_module.md#ansible-collections-ansible-builtin-template-module) or [ansible.builtin.assemble](../../ansible/builtin/assemble_module.md#ansible-collections-ansible-builtin-assemble-module). Interface has to be presented in a file.
- Read information about interfaces from interfaces-styled files

## [Parameters](interfaces_file_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address_family**  string | Address family of the interface, useful if same interface name is used for both inet and inet6 |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  Choices:   - `false` ← (default) - `true` |
| **dest**  path | Path to the interfaces file  Default: `"/etc/network/interfaces"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **iface**  string | Name of the interface, required for value changes or option remove |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **option**  string | Name of the option, required for value changes or option remove |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | If set to `absent` the option or section will be removed if present instead of created.  Choices:   - `"present"` ← (default) - `"absent"` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |
| **value**  string | If *option* is not presented for the *interface* and *state* is `present` option will be added. If *option* already exists and is not `pre-up`, `up`, `post-up` or `down`, it’s value will be updated. `pre-up`, `up`, `post-up` and `down` options can’t be updated, only adding new options, removing existing ones or cleaning the whole option set are supported |

## [Notes](interfaces_file_module.md#id3)

> **Note:**
>
> - If option is defined multiple times last one will be updated but all will be deleted in case of an absent state

## [Examples](interfaces_file_module.md#id4)

```yaml+jinja
- name: Set eth1 mtu configuration value to 8000
  community.general.interfaces_file:
    dest: /etc/network/interfaces.d/eth1.cfg
    iface: eth1
    option: mtu
    value: 8000
    backup: true
    state: present
  register: eth1_cfg
```

## [Return Values](interfaces_file_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest**  string | destination file/path  Returned: success  Sample: `"/etc/network/interfaces"` |
| **ifaces**  complex | interfaces dictionary  Returned: success |
| **ifaces**  dictionary | interface dictionary  Returned: success |
| **eth0**  dictionary | Name of the interface  Returned: success |
| **address_family**  string | interface address family  Returned: success  Sample: `"inet"` |
| **down**  list / elements=string | list of `down` scripts  Returned: success  Sample: `["route del -net 10.10.10.0/24 gw 10.10.10.1 dev eth1", "route del -net 10.10.11.0/24 gw 10.10.11.1 dev eth2"]` |
| **method**  string | interface method  Returned: success  Sample: `"manual"` |
| **mtu**  string | other options, all values returned as strings  Returned: success  Sample: `"1500"` |
| **post-up**  list / elements=string | list of `post-up` scripts  Returned: success  Sample: `["route add -net 10.10.10.0/24 gw 10.10.10.1 dev eth1", "route add -net 10.10.11.0/24 gw 10.10.11.1 dev eth2"]` |
| **pre-up**  list / elements=string | list of `pre-up` scripts  Returned: success  Sample: `["route add -net 10.10.10.0/24 gw 10.10.10.1 dev eth1", "route add -net 10.10.11.0/24 gw 10.10.11.1 dev eth2"]` |
| **up**  list / elements=string | list of `up` scripts  Returned: success  Sample: `["route add -net 10.10.10.0/24 gw 10.10.10.1 dev eth1", "route add -net 10.10.11.0/24 gw 10.10.11.1 dev eth2"]` |

### Authors

- Roman Belyakovsky (@hryamzik)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
