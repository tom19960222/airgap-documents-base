---
collection: ansible
version: "6"
title: "ansible.builtin.sysvinit module – Manage SysV services."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/sysvinit_module.html
fetched_at: 2026-07-27T16:44:10+00:00
---
# ansible.builtin.sysvinit module – Manage SysV services.

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `sysvinit` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](sysvinit_module.md#synopsis)
- [Requirements](sysvinit_module.md#requirements)
- [Parameters](sysvinit_module.md#parameters)
- [Attributes](sysvinit_module.md#attributes)
- [Notes](sysvinit_module.md#notes)
- [Examples](sysvinit_module.md#examples)
- [Return Values](sysvinit_module.md#return-values)

## [Synopsis](sysvinit_module.md#id1)

- Controls services on target hosts that use the SysV init system.

## [Requirements](sysvinit_module.md#id2)

The below requirements are needed on the host that executes this module.

- That the service managed has a corresponding init script.

## [Parameters](sysvinit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arguments**  aliases: args  string | Additional arguments provided on the command line that some init scripts accept. |
| **daemonize**  boolean | Have the module daemonize as the service itself might not do so properly.  This is useful with badly written init scripts or daemons, which commonly manifests as the task hanging as it is still holding the tty or the service dying when the task is over as the connection closes the session.  Choices:   - `false` ← (default) - `true` |
| **enabled**  boolean | Whether the service should start on boot. **At least one of state and enabled are required.**  Choices:   - `false` - `true` |
| **name**  aliases: service  string / required | Name of the service. |
| **pattern**  string | A substring to look for as would be found in the output of the *ps* command as a stand-in for a status result.  If the string is found, the service will be assumed to be running.  This option is mainly for use with init scripts that don’t support the ‘status’ option. |
| **runlevels**  list / elements=string | The runlevels this script should be enabled/disabled from.  Use this to override the defaults set by the package or init script itself. |
| **sleep**  integer | If the service is being `restarted` or `reloaded` then sleep this many seconds between the stop and start command. This helps to workaround badly behaving services.  Default: `1` |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary. Not all init scripts support `restarted` nor `reloaded` natively, so these will both trigger a stop and start as needed.  Choices:   - `"started"` - `"stopped"` - `"restarted"` - `"reloaded"` |

## [Attributes](sysvinit_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Notes](sysvinit_module.md#id5)

> **Note:**
>
> - One option other than name is required.
> - The service names might vary by specific OS/distribution

## [Examples](sysvinit_module.md#id6)

```yaml+jinja
- name: Make sure apache2 is started
  ansible.builtin.sysvinit:
      name: apache2
      state: started
      enabled: yes

- name: Make sure apache2 is started on runlevels 3 and 5
  ansible.builtin.sysvinit:
      name: apache2
      state: started
      enabled: yes
      runlevels:
        - 3
        - 5
```

## [Return Values](sysvinit_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  complex | results from actions taken  Returned: always  Sample: `{"attempts": 1, "changed": true, "name": "apache2", "status": {"enabled": {"changed": true, "rc": 0, "stderr": "", "stdout": ""}, "stopped": {"changed": true, "rc": 0, "stderr": "", "stdout": "Stopping web server: apache2.\n"}}}` |

### Authors

- Ansible Core Team

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
