---
collection: ansible
version: "8"
title: "ansible.builtin.known_hosts module – Add or remove a host from the known_hosts file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/known_hosts_module.html
fetched_at: 2026-07-28T01:07:35+00:00
---
# ansible.builtin.known_hosts module – Add or remove a host from the `known_hosts` file

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `known_hosts` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.known_hosts` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](known_hosts_module.md#synopsis)
- [Parameters](known_hosts_module.md#parameters)
- [Attributes](known_hosts_module.md#attributes)
- [Examples](known_hosts_module.md#examples)

## [Synopsis](known_hosts_module.md#id1)

- The `known_hosts` module lets you add or remove a host keys from the `known_hosts` file.
- Starting at Ansible 2.2, multiple entries per host are allowed, but only one for each key type supported by ssh. This is useful if you’re going to want to use the [ansible.builtin.git](git_module.md#ansible-collections-ansible-builtin-git-module) module over ssh, for example.
- If you have a very large number of host keys to manage, you will find the [ansible.builtin.template](template_module.md#ansible-collections-ansible-builtin-template-module) module more useful.

## [Parameters](known_hosts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hash_host**  boolean | Hash the hostname in the known_hosts file.  **Choices:**   - `false` ← (default) - `true` |
| **key**  string | The SSH public host key, as a string.  Required if `state=present`, optional when `state=absent`, in which case all keys for the host are removed.  The key must be in the right format for SSH (see sshd(8), section “SSH_KNOWN_HOSTS FILE FORMAT”).  Specifically, the key should not match the format that is found in an SSH pubkey file, but should rather have the hostname prepended to a line that includes the pubkey, the same way that it would appear in the known_hosts file. The value prepended to the line must also match the value of the name parameter.  Should be of format `<hostname[,IP]> ssh-rsa <pubkey>`.  For custom SSH port, `key` needs to specify port as well. See example section. |
| **name**  aliases: host  string / required | The host to add or remove (must match a host specified in key). It will be converted to lowercase so that ssh-keygen can find it.  Must match with <hostname> or <ip> present in key attribute.  For custom SSH port, `name` needs to specify port as well. See example section. |
| **path**  path | The known_hosts file to edit.  The known_hosts file will be created if needed. The rest of the path must exist prior to running the module.  **Default:** `"~/.ssh/known_hosts"` |
| **state**  string | *present* to add the host key.  *absent* to remove it.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](known_hosts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Examples](known_hosts_module.md#id4)

```yaml+jinja
- name: Tell the host about our servers it might want to ssh to
  ansible.builtin.known_hosts:
    path: /etc/ssh/ssh_known_hosts
    name: foo.com.invalid
    key: "{{ lookup('ansible.builtin.file', 'pubkeys/foo.com.invalid') }}"

- name: Another way to call known_hosts
  ansible.builtin.known_hosts:
    name: host1.example.com   # or 10.9.8.77
    key: host1.example.com,10.9.8.77 ssh-rsa ASDeararAIUHI324324  # some key gibberish
    path: /etc/ssh/ssh_known_hosts
    state: present

- name: Add host with custom SSH port
  ansible.builtin.known_hosts:
    name: '[host1.example.com]:2222'
    key: '[host1.example.com]:2222 ssh-rsa ASDeararAIUHI324324' # some key gibberish
    path: /etc/ssh/ssh_known_hosts
    state: present
```

### Authors

- Matthew Vernon (@mcv21)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
