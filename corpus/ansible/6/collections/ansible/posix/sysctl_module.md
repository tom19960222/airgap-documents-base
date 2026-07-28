---
collection: ansible
version: "6"
title: "ansible.posix.sysctl module – Manage entries in sysctl.conf."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/sysctl_module.html
fetched_at: 2026-07-27T16:44:44+00:00
---
# ansible.posix.sysctl module – Manage entries in sysctl.conf.

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ansible/posix) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
>
> To use it in a playbook, specify: `ansible.posix.sysctl`.

New in ansible.posix 1.0.0

- [Synopsis](sysctl_module.md#synopsis)
- [Parameters](sysctl_module.md#parameters)
- [Examples](sysctl_module.md#examples)

## [Synopsis](sysctl_module.md#id1)

- This module manipulates sysctl entries and optionally performs a `/sbin/sysctl -p` after changing them.

## [Parameters](sysctl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ignoreerrors**  boolean | Use this option to ignore errors about unknown keys.  Choices:   - `false` ← (default) - `true` |
| **name**  aliases: key  string / required | The dot-separated path (also known as *key*) specifying the sysctl variable. |
| **reload**  boolean | If `yes`, performs a */sbin/sysctl -p* if the `sysctl_file` is updated. If `no`, does not reload *sysctl* even if the `sysctl_file` is updated.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Whether the entry should be present or absent in the sysctl file.  Choices:   - `"present"` ← (default) - `"absent"` |
| **sysctl_file**  path | Specifies the absolute path to `sysctl.conf`, if not `/etc/sysctl.conf`.  Default: `"/etc/sysctl.conf"` |
| **sysctl_set**  boolean | Verify token value with the sysctl command and set with -w if necessary  Choices:   - `false` ← (default) - `true` |
| **value**  aliases: val  string | Desired value of the sysctl key. |

## [Examples](sysctl_module.md#id3)

```yaml+jinja
# Set vm.swappiness to 5 in /etc/sysctl.conf
- ansible.posix.sysctl:
    name: vm.swappiness
    value: '5'
    state: present

# Remove kernel.panic entry from /etc/sysctl.conf
- ansible.posix.sysctl:
    name: kernel.panic
    state: absent
    sysctl_file: /etc/sysctl.conf

# Set kernel.panic to 3 in /tmp/test_sysctl.conf
- ansible.posix.sysctl:
    name: kernel.panic
    value: '3'
    sysctl_file: /tmp/test_sysctl.conf
    reload: no

# Set ip forwarding on in /proc and verify token value with the sysctl command
- ansible.posix.sysctl:
    name: net.ipv4.ip_forward
    value: '1'
    sysctl_set: yes

# Set ip forwarding on in /proc and in the sysctl file and reload if necessary
- ansible.posix.sysctl:
    name: net.ipv4.ip_forward
    value: '1'
    sysctl_set: yes
    state: present
    reload: yes
```

### Authors

- David CHANIAL (@davixx)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
