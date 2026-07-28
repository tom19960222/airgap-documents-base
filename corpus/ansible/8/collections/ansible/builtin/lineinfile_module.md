---
collection: ansible
version: "8"
title: "ansible.builtin.lineinfile module – Manage lines in text files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/lineinfile_module.html
fetched_at: 2026-07-28T01:03:58+00:00
---
# ansible.builtin.lineinfile module – Manage lines in text files

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `lineinfile` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.lineinfile` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](lineinfile_module.md#synopsis)
- [Parameters](lineinfile_module.md#parameters)
- [Attributes](lineinfile_module.md#attributes)
- [Notes](lineinfile_module.md#notes)
- [See Also](lineinfile_module.md#see-also)
- [Examples](lineinfile_module.md#examples)

## [Synopsis](lineinfile_module.md#id1)

- This module ensures a particular line is in a file, or replace an existing line using a back-referenced regular expression.
- This is primarily useful when you want to change a single line in a file only.
- See the [ansible.builtin.replace](replace_module.md#ansible-collections-ansible-builtin-replace-module) module if you want to change multiple, similar lines or check [ansible.builtin.blockinfile](blockinfile_module.md#ansible-collections-ansible-builtin-blockinfile-module) if you want to insert/update/remove a block of lines in a file. For other cases, see the [ansible.builtin.copy](copy_module.md#ansible-collections-ansible-builtin-copy-module) or [ansible.builtin.template](template_module.md#ansible-collections-ansible-builtin-template-module) modules.

## [Parameters](lineinfile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backrefs**  boolean | Used with `state=present`.  If set, `line` can contain backreferences (both positional and named) that will get populated if the `regexp` matches.  This parameter changes the operation of the module slightly; `insertbefore` and `insertafter` will be ignored, and if the `regexp` does not match anywhere in the file, the file will be left unchanged.  If the `regexp` does match, the last matching line will be replaced by the expanded line parameter.  Mutually exclusive with `search_string`.  **Choices:**   - `false` ← (default) - `true` |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **create**  boolean | Used with `state=present`.  If specified, the file will be created if it does not already exist.  By default it will fail if the file is missing.  **Choices:**   - `false` ← (default) - `true` |
| **firstmatch**  boolean | Used with `insertafter` or `insertbefore`.  If set, `insertafter` and `insertbefore` will work with the first line that matches the given regular expression.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **insertafter**  string | Used with `state=present`.  If specified, the line will be inserted after the last match of specified regular expression.  If the first match is required, use(firstmatch=yes).  A special value is available; `EOF` for inserting the line at the end of the file.  If specified regular expression has no matches, EOF will be used instead.  If `insertbefore` is set, default value `EOF` will be ignored.  If regular expressions are passed to both `regexp` and `insertafter`, `insertafter` is only honored if no match for `regexp` is found.  May not be used with `backrefs` or `insertbefore`.  **Choices:**   - `"EOF"` ← (default) - `"*regex*"` |
| **insertbefore**  string | Used with `state=present`.  If specified, the line will be inserted before the last match of specified regular expression.  If the first match is required, use `firstmatch=yes`.  A value is available; `BOF` for inserting the line at the beginning of the file.  If specified regular expression has no matches, the line will be inserted at the end of the file.  If regular expressions are passed to both `regexp` and `insertbefore`, `insertbefore` is only honored if no match for `regexp` is found.  May not be used with `backrefs` or `insertafter`.  **Choices:**   - `"BOF"` - `"*regex*"` |
| **line**  aliases: value  string | The line to insert/replace into the file.  Required for `state=present`.  If `backrefs` is set, may contain backreferences that will get expanded with the `regexp` capture groups if the regexp matches. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **others**  string | All arguments accepted by the [ansible.builtin.file](file_module.md#ansible-collections-ansible-builtin-file-module) module also work here. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  aliases: dest, destfile, name  path / required | The file to modify.  Before Ansible 2.3 this option was only usable as *dest*, *destfile* and *name*. |
| **regexp**  aliases: regex  string | The regular expression to look for in every line of the file.  For `state=present`, the pattern to replace if found. Only the last line found will be replaced.  For `state=absent`, the pattern of the line(s) to remove.  If the regular expression is not matched, the line will be added to the file in keeping with `insertbefore` or `insertafter` settings.  When modifying a line the regexp should typically match both the initial state of the line as well as its state after replacement by `line` to ensure idempotence.  Uses Python regular expressions. See <https://docs.python.org/3/library/re.html>. |
| **search_string**  string  *added in ansible-core 2.11* | The literal string to look for in every line of the file. This does not have to match the entire line.  For `state=present`, the line to replace if the string is found in the file. Only the last line found will be replaced.  For `state=absent`, the line(s) to remove if the string is in the line.  If the literal expression is not matched, the line will be added to the file in keeping with `insertbefore` or `insertafter` settings.  Mutually exclusive with `backrefs` and `regexp`. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the line should be there or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **validate**  string | The validation command to run before copying the updated file into the final destination.  A temporary file path is used to validate, passed in through ‘%s’ which must be present as in the examples below.  Also, the command is passed securely so shell features such as expansion and pipes will not work.  For an example on how to handle more complex validation than what this option provides, see [handling complex validation](../../../reference_appendices/faq.md#complex-configuration-validation). |

## [Attributes](lineinfile_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | **Support:** **none** | Can automatically decrypt Ansible vaulted files |

## [Notes](lineinfile_module.md#id4)

> **Note:**
>
> - As of Ansible 2.3, the *dest* option has been changed to *path* as default, but *dest* still works as well.

## [See Also](lineinfile_module.md#id5)

> **See also:**
>
> [ansible.builtin.blockinfile](blockinfile_module.md#ansible-collections-ansible-builtin-blockinfile-module)
> :   Insert/update/remove a text block surrounded by marker lines.
>
> [ansible.builtin.copy](copy_module.md#ansible-collections-ansible-builtin-copy-module)
> :   Copy files to remote locations.
>
> [ansible.builtin.file](file_module.md#ansible-collections-ansible-builtin-file-module)
> :   Manage files and file properties.
>
> [ansible.builtin.replace](replace_module.md#ansible-collections-ansible-builtin-replace-module)
> :   Replace all instances of a particular string in a file using a back-referenced regular expression.
>
> [ansible.builtin.template](template_module.md#ansible-collections-ansible-builtin-template-module)
> :   Template a file out to a target host.
>
> [community.windows.win_lineinfile](../../community/windows/win_lineinfile_module.md#ansible-collections-community-windows-win-lineinfile-module)
> :   Ensure a particular line is in a file, or replace an existing line using a back-referenced regular expression.

## [Examples](lineinfile_module.md#id6)

```yaml+jinja
# NOTE: Before 2.3, option 'dest', 'destfile' or 'name' was used instead of 'path'
- name: Ensure SELinux is set to enforcing mode
  ansible.builtin.lineinfile:
    path: /etc/selinux/config
    regexp: '^SELINUX='
    line: SELINUX=enforcing

- name: Make sure group wheel is not in the sudoers configuration
  ansible.builtin.lineinfile:
    path: /etc/sudoers
    state: absent
    regexp: '^%wheel'

- name: Replace a localhost entry with our own
  ansible.builtin.lineinfile:
    path: /etc/hosts
    regexp: '^127\.0\.0\.1'
    line: 127.0.0.1 localhost
    owner: root
    group: root
    mode: '0644'

- name: Replace a localhost entry searching for a literal string to avoid escaping
  ansible.builtin.lineinfile:
    path: /etc/hosts
    search_string: '127.0.0.1'
    line: 127.0.0.1 localhost
    owner: root
    group: root
    mode: '0644'

- name: Ensure the default Apache port is 8080
  ansible.builtin.lineinfile:
    path: /etc/httpd/conf/httpd.conf
    regexp: '^Listen '
    insertafter: '^#Listen '
    line: Listen 8080

- name: Ensure php extension matches new pattern
  ansible.builtin.lineinfile:
    path: /etc/httpd/conf/httpd.conf
    search_string: '<FilesMatch ".php[45]?$">'
    insertafter: '^\t<Location \/>\n'
    line: '        <FilesMatch ".php[34]?$">'

- name: Ensure we have our own comment added to /etc/services
  ansible.builtin.lineinfile:
    path: /etc/services
    regexp: '^# port for http'
    insertbefore: '^www.*80/tcp'
    line: '# port for http by default'

- name: Add a line to a file if the file does not exist, without passing regexp
  ansible.builtin.lineinfile:
    path: /tmp/testfile
    line: 192.168.1.99 foo.lab.net foo
    create: yes

# NOTE: Yaml requires escaping backslashes in double quotes but not in single quotes
- name: Ensure the JBoss memory settings are exactly as needed
  ansible.builtin.lineinfile:
    path: /opt/jboss-as/bin/standalone.conf
    regexp: '^(.*)Xms(\d+)m(.*)$'
    line: '\1Xms${xms}m\3'
    backrefs: yes

# NOTE: Fully quoted because of the ': ' on the line. See the Gotchas in the YAML docs.
- name: Validate the sudoers file before saving
  ansible.builtin.lineinfile:
    path: /etc/sudoers
    state: present
    regexp: '^%ADMIN ALL='
    line: '%ADMIN ALL=(ALL) NOPASSWD: ALL'
    validate: /usr/sbin/visudo -cf %s

# See https://docs.python.org/3/library/re.html for further details on syntax
- name: Use backrefs with alternative group syntax to avoid conflicts with variable values
  ansible.builtin.lineinfile:
    path: /tmp/config
    regexp: ^(host=).*
    line: \g<1>{{ hostname }}
    backrefs: yes
```

### Authors

- Daniel Hokka Zakrissoni (@dhozac)
- Ahti Kitsik (@ahtik)
- Jose Angel Munoz (@imjoseangel)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
