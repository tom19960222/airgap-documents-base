---
collection: ansible
version: "8"
title: "ansible.builtin.blockinfile module – Insert/update/remove a text block surrounded by marker lines"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/blockinfile_module.html
fetched_at: 2026-07-28T01:07:23+00:00
---
# ansible.builtin.blockinfile module – Insert/update/remove a text block surrounded by marker lines

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `blockinfile` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.blockinfile` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](blockinfile_module.md#synopsis)
- [Parameters](blockinfile_module.md#parameters)
- [Attributes](blockinfile_module.md#attributes)
- [Notes](blockinfile_module.md#notes)
- [Examples](blockinfile_module.md#examples)

## [Synopsis](blockinfile_module.md#id1)

- This module will insert/update/remove a block of multi-line text surrounded by customizable marker lines.

## [Parameters](blockinfile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **block**  aliases: content  string | The text to insert inside the marker lines.  If it is missing or an empty string, the block will be removed as if `state` were specified to `absent`.  **Default:** `""` |
| **create**  boolean | Create a new file if it does not exist.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **insertafter**  string | If specified and no begin/ending `marker` lines are found, the block will be inserted after the last match of specified regular expression.  A special value is available; `EOF` for inserting the block at the end of the file.  If specified regular expression has no matches, `EOF` will be used instead.  The presence of the multiline flag (?m) in the regular expression controls whether the match is done line by line or with multiple lines. This behaviour was added in ansible-core 2.14.  **Choices:**   - `"EOF"` ← (default) - `"*regex*"` |
| **insertbefore**  string | If specified and no begin/ending `marker` lines are found, the block will be inserted before the last match of specified regular expression.  A special value is available; `BOF` for inserting the block at the beginning of the file.  If specified regular expression has no matches, the block will be inserted at the end of the file.  The presence of the multiline flag (?m) in the regular expression controls whether the match is done line by line or with multiple lines. This behaviour was added in ansible-core 2.14.  **Choices:**   - `"BOF"` - `"*regex*"` |
| **marker**  string | The marker line template.  `{mark}` will be replaced with the values in `marker_begin` (default=”BEGIN”) and `marker_end` (default=”END”).  Using a custom marker without the `{mark}` variable may result in the block being repeatedly inserted on subsequent playbook runs.  Multi-line markers are not supported and will result in the block being repeatedly inserted on subsequent playbook runs.  A newline is automatically appended by the module to `marker_begin` and `marker_end`.  **Default:** `"# {mark} ANSIBLE MANAGED BLOCK"` |
| **marker_begin**  string | This will be inserted at `{mark}` in the opening ansible block marker.  **Default:** `"BEGIN"` |
| **marker_end**  string | This will be inserted at `{mark}` in the closing ansible block marker.  **Default:** `"END"` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  aliases: dest, destfile, name  path / required | The file to modify.  Before Ansible 2.3 this option was only usable as *dest*, *destfile* and *name*. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Whether the block should be there or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **validate**  string | The validation command to run before copying the updated file into the final destination.  A temporary file path is used to validate, passed in through ‘%s’ which must be present as in the examples below.  Also, the command is passed securely so shell features such as expansion and pipes will not work.  For an example on how to handle more complex validation than what this option provides, see [handling complex validation](../../../reference_appendices/faq.md#complex-configuration-validation). |

## [Attributes](blockinfile_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |
| **safe_file_operations** | **Support:** **full** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | **Support:** **none** | Can automatically decrypt Ansible vaulted files |

## [Notes](blockinfile_module.md#id4)

> **Note:**
>
> - When using ‘with_\*’ loops be aware that if you do not set a unique mark the block will be overwritten on each iteration.
> - As of Ansible 2.3, the *dest* option has been changed to *path* as default, but *dest* still works as well.
> - Option *follow* has been removed in Ansible 2.5, because this module modifies the contents of the file so *follow=no* doesn’t make sense.
> - When more then one block should be handled in one file you must change the *marker* per task.

## [Examples](blockinfile_module.md#id5)

```yaml+jinja
# Before Ansible 2.3, option 'dest' or 'name' was used instead of 'path'
- name: Insert/Update "Match User" configuration block in /etc/ssh/sshd_config
  ansible.builtin.blockinfile:
    path: /etc/ssh/sshd_config
    block: |
      Match User ansible-agent
      PasswordAuthentication no

- name: Insert/Update eth0 configuration stanza in /etc/network/interfaces
        (it might be better to copy files into /etc/network/interfaces.d/)
  ansible.builtin.blockinfile:
    path: /etc/network/interfaces
    block: |
      iface eth0 inet static
          address 192.0.2.23
          netmask 255.255.255.0

- name: Insert/Update configuration using a local file and validate it
  ansible.builtin.blockinfile:
    block: "{{ lookup('ansible.builtin.file', './local/sshd_config') }}"
    path: /etc/ssh/sshd_config
    backup: yes
    validate: /usr/sbin/sshd -T -f %s

- name: Insert/Update HTML surrounded by custom markers after <body> line
  ansible.builtin.blockinfile:
    path: /var/www/html/index.html
    marker: "<!-- {mark} ANSIBLE MANAGED BLOCK -->"
    insertafter: "<body>"
    block: |
      <h1>Welcome to {{ ansible_hostname }}</h1>
      <p>Last updated on {{ ansible_date_time.iso8601 }}</p>

- name: Remove HTML as well as surrounding markers
  ansible.builtin.blockinfile:
    path: /var/www/html/index.html
    marker: "<!-- {mark} ANSIBLE MANAGED BLOCK -->"
    block: ""

- name: Add mappings to /etc/hosts
  ansible.builtin.blockinfile:
    path: /etc/hosts
    block: |
      {{ item.ip }} {{ item.name }}
    marker: "# {mark} ANSIBLE MANAGED BLOCK {{ item.name }}"
  loop:
    - { name: host1, ip: 10.10.1.10 }
    - { name: host2, ip: 10.10.1.11 }
    - { name: host3, ip: 10.10.1.12 }

- name: Search with a multiline search flags regex and if found insert after
  blockinfile:
    path: listener.ora
    block: "{{ listener_line | indent(width=8, first=True) }}"
    insertafter: '(?m)SID_LIST_LISTENER_DG =\n.*\(SID_LIST ='
    marker: "    <!-- {mark} ANSIBLE MANAGED BLOCK -->"
```

### Authors

- Yaegashi Takeshi (@yaegashi)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
