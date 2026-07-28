---
collection: ansible
version: "8"
title: "ansible.builtin.assemble module – Assemble configuration files from fragments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/assemble_module.html
fetched_at: 2026-07-28T01:04:15+00:00
---
# ansible.builtin.assemble module – Assemble configuration files from fragments

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `assemble` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.assemble` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](assemble_module.md#synopsis)
- [Parameters](assemble_module.md#parameters)
- [Attributes](assemble_module.md#attributes)
- [See Also](assemble_module.md#see-also)
- [Examples](assemble_module.md#examples)

## [Synopsis](assemble_module.md#id1)

- Assembles a configuration file from fragments.
- Often a particular program will take a single configuration file and does not support a `conf.d` style structure where it is easy to build up the configuration from multiple sources. `assemble` will take a directory of files that can be local or have already been transferred to the system, and concatenate them together to produce a destination file.
- Files are assembled in string sorting order.
- Puppet calls this idea *fragments*.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](assemble_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file (if `true`), including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **decrypt**  boolean | This option controls the autodecryption of source files using vault.  **Choices:**   - `false` - `true` ← (default) |
| **delimiter**  string | A delimiter to separate the file contents. |
| **dest**  path / required | A file to create using the concatenation of all of the source files. |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **ignore_hidden**  boolean | A boolean that controls if files that start with a ‘.’ will be included or not.  **Choices:**   - `false` ← (default) - `true` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **regexp**  string | Assemble files only if `regex` matches the filename.  If not set, all files are assembled.  Every `\` (backslash) must be escaped as `\\` to comply to YAML syntax.  Uses [Python regular expressions](https://docs.python.org/3/library/re.html). |
| **remote_src**  boolean | If `false`, it will search for src at originating/master machine.  If `true`, it will go to the remote/target machine for the src.  **Choices:**   - `false` - `true` ← (default) |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **src**  path / required | An already existing directory full of source files. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **validate**  string | The validation command to run before copying into place.  The path to the file to validate is passed in via ‘%s’ which must be present as in the sshd example below.  The command is passed securely so shell features like expansion and pipes won’t work. |

## [Attributes](assemble_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | **Support:** **full** | Can automatically decrypt Ansible vaulted files |

## [See Also](assemble_module.md#id4)

> **See also:**
>
> [ansible.builtin.copy](copy_module.md#ansible-collections-ansible-builtin-copy-module)
> :   Copy files to remote locations.
>
> [ansible.builtin.template](template_module.md#ansible-collections-ansible-builtin-template-module)
> :   Template a file out to a target host.
>
> [ansible.windows.win_copy](../windows/win_copy_module.md#ansible-collections-ansible-windows-win-copy-module)
> :   Copies files to remote locations on windows hosts.

## [Examples](assemble_module.md#id5)

```yaml+jinja
- name: Assemble from fragments from a directory
  ansible.builtin.assemble:
    src: /etc/someapp/fragments
    dest: /etc/someapp/someapp.conf

- name: Insert the provided delimiter between fragments
  ansible.builtin.assemble:
    src: /etc/someapp/fragments
    dest: /etc/someapp/someapp.conf
    delimiter: '### START FRAGMENT ###'

- name: Assemble a new "sshd_config" file into place, after passing validation with sshd
  ansible.builtin.assemble:
    src: /etc/ssh/conf.d/
    dest: /etc/ssh/sshd_config
    validate: /usr/sbin/sshd -t -f %s
```

### Authors

- Stephen Fromm (@sfromm)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
