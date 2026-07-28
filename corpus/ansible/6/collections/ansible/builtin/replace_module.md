---
collection: ansible
version: "6"
title: "ansible.builtin.replace module – Replace all instances of a particular string in a file using a back-referenced regular expression"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/replace_module.html
fetched_at: 2026-07-27T16:42:40+00:00
---
# ansible.builtin.replace module – Replace all instances of a particular string in a file using a back-referenced regular expression

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `replace` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](replace_module.md#synopsis)
- [Parameters](replace_module.md#parameters)
- [Attributes](replace_module.md#attributes)
- [Notes](replace_module.md#notes)
- [Examples](replace_module.md#examples)

## [Synopsis](replace_module.md#id1)

- This module will replace all instances of a pattern within a file.
- It is up to the user to maintain idempotence by ensuring that the same pattern would never match any replacements made.

## [Parameters](replace_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  string | If specified, only content after this match will be replaced/removed.  Can be used in combination with `before`.  Uses Python regular expressions; see <https://docs.python.org/3/library/re.html>.  Uses DOTALL, which means the `.` special character *can match newlines*. |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  Choices:   - `false` ← (default) - `true` |
| **before**  string | If specified, only content before this match will be replaced/removed.  Can be used in combination with `after`.  Uses Python regular expressions; see <https://docs.python.org/3/library/re.html>.  Uses DOTALL, which means the `.` special character *can match newlines*. |
| **encoding**  string | The character encoding for reading and writing the file.  Default: `"utf-8"` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **others**  string | All arguments accepted by the [ansible.builtin.file](file_module.md#ansible-collections-ansible-builtin-file-module) module also work here. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **path**  aliases: dest, destfile, name  path / required | The file to modify.  Before Ansible 2.3 this option was only usable as *dest*, *destfile* and *name*. |
| **regexp**  string / required | The regular expression to look for in the contents of the file.  Uses Python regular expressions; see <https://docs.python.org/3/library/re.html>.  Uses MULTILINE mode, which means `^` and `$` match the beginning and end of the file, as well as the beginning and end respectively of *each line* of the file.  Does not use DOTALL, which means the `.` special character matches any character *except newlines*. A common mistake is to assume that a negated character set like `[^#]` will also not match newlines.  In order to exclude newlines, they must be added to the set like `[^#\n]`.  Note that, as of Ansible 2.0, short form tasks should have any escape sequences backslash-escaped in order to prevent them being parsed as string literal escapes. See the examples. |
| **replace**  string | The string to replace regexp matches.  May contain backreferences that will get expanded with the regexp capture groups if the regexp matches.  If not set, matches are removed entirely.  Backreferences can be used ambiguously like `\1`, or explicitly like `\g<1>`. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |
| **validate**  string | The validation command to run before copying the updated file into the final destination.  A temporary file path is used to validate, passed in through ‘%s’ which must be present as in the examples below.  Also, the command is passed securely so shell features such as expansion and pipes will not work.  For an example on how to handle more complex validation than what this option provides, see [Complex configuration validation](https://docs.ansible.com/ansible/devel/reference_appendices/faq.html). |

## [Attributes](replace_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |
| **safe_file_operations** | Support: full | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | Support: none | Can automatically decrypt Ansible vaulted files |

## [Notes](replace_module.md#id4)

> **Note:**
>
> - As of Ansible 2.3, the *dest* option has been changed to *path* as default, but *dest* still works as well.
> - As of Ansible 2.7.10, the combined use of *before* and *after* works properly. If you were relying on the previous incorrect behavior, you may be need to adjust your tasks. See <https://github.com/ansible/ansible/issues/31354> for details.
> - Option *follow* has been removed in Ansible 2.5, because this module modifies the contents of the file so *follow=no* doesn’t make sense.

## [Examples](replace_module.md#id5)

```yaml+jinja
- name: Replace old hostname with new hostname (requires Ansible >= 2.4)
  ansible.builtin.replace:
    path: /etc/hosts
    regexp: '(\s+)old\.host\.name(\s+.*)?$'
    replace: '\1new.host.name\2'

- name: Replace after the expression till the end of the file (requires Ansible >= 2.4)
  ansible.builtin.replace:
    path: /etc/apache2/sites-available/default.conf
    after: 'NameVirtualHost [*]'
    regexp: '^(.+)$'
    replace: '# \1'

- name: Replace before the expression till the begin of the file (requires Ansible >= 2.4)
  ansible.builtin.replace:
    path: /etc/apache2/sites-available/default.conf
    before: '# live site config'
    regexp: '^(.+)$'
    replace: '# \1'

# Prior to Ansible 2.7.10, using before and after in combination did the opposite of what was intended.
# see https://github.com/ansible/ansible/issues/31354 for details.
- name: Replace between the expressions (requires Ansible >= 2.4)
  ansible.builtin.replace:
    path: /etc/hosts
    after: '<VirtualHost [*]>'
    before: '</VirtualHost>'
    regexp: '^(.+)$'
    replace: '# \1'

- name: Supports common file attributes
  ansible.builtin.replace:
    path: /home/jdoe/.ssh/known_hosts
    regexp: '^old\.host\.name[^\n]*\n'
    owner: jdoe
    group: jdoe
    mode: '0644'

- name: Supports a validate command
  ansible.builtin.replace:
    path: /etc/apache/ports
    regexp: '^(NameVirtualHost|Listen)\s+80\s*$'
    replace: '\1 127.0.0.1:8080'
    validate: '/usr/sbin/apache2ctl -f %s -t'

- name: Short form task (in ansible 2+) necessitates backslash-escaped sequences
  ansible.builtin.replace: path=/etc/hosts regexp='\\b(localhost)(\\d*)\\b' replace='\\1\\2.localdomain\\2 \\1\\2'

- name: Long form task does not
  ansible.builtin.replace:
    path: /etc/hosts
    regexp: '\b(localhost)(\d*)\b'
    replace: '\1\2.localdomain\2 \1\2'

- name: Explicitly specifying positional matched groups in replacement
  ansible.builtin.replace:
    path: /etc/ssh/sshd_config
    regexp: '^(ListenAddress[ ]+)[^\n]+$'
    replace: '\g<1>0.0.0.0'

- name: Explicitly specifying named matched groups
  ansible.builtin.replace:
    path: /etc/ssh/sshd_config
    regexp: '^(?P<dctv>ListenAddress[ ]+)(?P<host>[^\n]+)$'
    replace: '#\g<dctv>\g<host>\n\g<dctv>0.0.0.0'
```

### Authors

- Evan Kaufman (@EvanK)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
